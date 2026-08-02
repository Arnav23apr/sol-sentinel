"""Ecosystem activity metrics that have no keyless feed anywhere — so
Sentinel measures them itself, straight from the chain.

Daily active addresses
----------------------
Every hosted "active addresses" feed now sits behind an API key (DeFiLlama's
users API is discontinued, Solscan/Coin Metrics/Dune are keyed). Instead of
dropping the metric, Sentinel samples K blocks spread evenly across the
trailing 24 hours, records the unique non-vote fee payers in each, and feeds
the capture-recapture overlap between samples into a Schnabel estimator:

    N_hat = sum_t(C_t * M_t) / sum_t(R_t)

where, for each successive sampled block t: C_t = payers in the sample,
M_t = distinct payers already seen ("marked"), R_t = recaptures (payers in
sample t already seen before). The estimator assumes a closed population and
homogeneous activity — both are violated in reality (documented in the
README), so the value is labeled an *estimate* and is primarily useful as a
consistent trend/anomaly series. The raw per-block uniques are also reported.

Tokenized equities (xStocks) & RWA
----------------------------------
DeFiLlama's protocol endpoint gives xStocks AUM on Solana with per-ticker
breakdown; Jupiter's lite-api token search adds 24h DEX volume and holder
counts for the same tokens. Total Solana RWA TVL comes from filtering
DeFiLlama's protocol list by category == "RWA".
"""
from __future__ import annotations

from .collect_rpc import rpc
from .net import FetchError, fetch_json

SAMPLE_BLOCKS = 8
SLOTS_PER_DAY = 216_000  # ~2.5 slots/s
VOTE_PROGRAM = "Vote111111111111111111111111111111111111111"
BASE_FEE_LAMPORTS = 5_000  # per signature, before any priority fee
LAMPORTS = 1_000_000_000

# Two-sided 95% Student-t critical values by degrees of freedom. Hardcoded
# because scipy is not available under the stdlib-only rule; the table only
# needs to cover the handful of sample sizes this collector uses.
T_95 = {2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365,
        8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179}


def _sample_block(slot: int) -> tuple[set, list, int]:
    """Read one block and return (unique non-vote fee payers, non-vote fees in
    lamports, total fees in the block including votes).

    `transactionDetails: "accounts"` already carries `meta.fee`, so the fee
    distribution is free: it rides along on the request the activity index
    was going to make anyway. Tries slot, slot+1, slot+2 since slots can be
    skipped.
    """
    for candidate in (slot, slot + 1, slot + 2):
        try:
            block = rpc("getBlock", [candidate, {
                "encoding": "json", "transactionDetails": "accounts",
                "rewards": False, "maxSupportedTransactionVersion": 0}],
                timeout=30.0)
        except FetchError:
            continue
        if not block or "transactions" not in block:
            continue
        payers: set = set()
        user_fees: list = []
        total_fees = 0
        for tx in block["transactions"]:
            keys = (tx.get("transaction") or {}).get("accountKeys") or []
            fee = (tx.get("meta") or {}).get("fee")
            if fee is not None:
                total_fees += fee
            if any(k.get("pubkey") == VOTE_PROGRAM for k in keys):
                continue  # consensus vote transaction, not user activity
            if keys:
                payers.add(keys[0]["pubkey"])
            if fee is not None:
                user_fees.append(fee)
        return payers, user_fees, total_fees
    return set(), [], 0


def _fee_stats(user_fees: list, block_totals: list) -> dict:
    """Transaction-fee distribution measured directly from sampled blocks.

    Reported for non-vote transactions only. Vote transactions are a fixed
    5,000-lamport base fee and make up roughly half of all transactions, so
    including them drags every percentile to exactly the base fee and hides
    what users actually pay.
    """
    out: dict = {}
    if user_fees:
        f = sorted(user_fees)
        n = len(f)
        out["median_tx_fee_lamports"] = f[n // 2]
        out["p90_tx_fee_lamports"] = f[min(int(n * 0.9), n - 1)]
        out["p99_tx_fee_lamports"] = f[min(int(n * 0.99), n - 1)]
        out["mean_tx_fee_lamports"] = round(sum(f) / n)
        # The share paying nothing above the 5,000-lamport base fee is a
        # cleaner congestion read than the mean, which a handful of
        # multi-SOL priority bids can move by an order of magnitude.
        out["base_fee_only_pct"] = round(
            sum(1 for x in f if x <= BASE_FEE_LAMPORTS) / n * 100, 1)
        out["fee_sampled_txs"] = n
    if block_totals:
        avg_per_block = sum(block_totals) / len(block_totals)
        out["avg_fees_per_block_sol"] = round(avg_per_block / LAMPORTS, 6)
        # Extrapolated to a day so it can be cross-checked against the figure
        # DeFiLlama reports for the same window (see crosscheck.py).
        daily = avg_per_block / LAMPORTS * SLOTS_PER_DAY
        out["measured_daily_fees_sol"] = round(daily)
        # Eight blocks out of ~216,000 is a small sample of a heavy-tailed
        # quantity, so the point estimate alone would imply false precision.
        # Carry a 95% interval (Student t, n-1 df) so the cross-check can ask
        # the statistically meaningful question -- does the other source's
        # number fall inside our interval? -- instead of comparing against an
        # arbitrary tolerance.
        n = len(block_totals)
        if n >= 3:
            mean = avg_per_block
            var = sum((x - mean) ** 2 for x in block_totals) / (n - 1)
            stderr = (var ** 0.5) / (n ** 0.5)
            t = T_95.get(n - 1, 1.96)
            margin = t * stderr / LAMPORTS * SLOTS_PER_DAY
            out["measured_daily_fees_sol_low"] = round(max(0.0, daily - margin))
            out["measured_daily_fees_sol_high"] = round(daily + margin)
    return out


def activity() -> dict:
    tip = rpc("getEpochInfo")["absoluteSlot"]
    step = SLOTS_PER_DAY // SAMPLE_BLOCKS
    samples: list[set] = []
    user_fees: list = []
    block_totals: list = []
    for i in range(SAMPLE_BLOCKS):
        payers, fees, total = _sample_block(tip - 150 - i * step)
        if payers:
            samples.append(payers)
            user_fees.extend(fees)
            block_totals.append(total)

    out: dict = {"sampled_blocks": len(samples)}
    if not samples:
        return out

    out.update(_fee_stats(user_fees, block_totals))

    per_block = [len(s) for s in samples]
    out["unique_payers_per_block_avg"] = round(sum(per_block) / len(per_block))
    out["unique_payers_per_block"] = per_block

    # Schnabel capture-recapture across the sampled blocks.
    marked: set = set()
    num = den = 0
    for s in samples:
        c_t, m_t = len(s), len(marked)
        r_t = len(s & marked)
        if m_t:
            num += c_t * m_t
            den += r_t
        marked |= s
    out["union_unique_payers"] = len(marked)
    # The primary, honestly-comparable activity series: average unique
    # non-vote fee payers per block. True chain-wide DAA is NOT estimable
    # keylessly (every provider gates it), and capture-recapture across
    # sparse samples is dominated by always-on actors (bots, market makers),
    # so the Schnabel figure is labeled as the persistently-active cohort,
    # not total daily actives. Both are documented in the README.
    out["activity_index"] = out["unique_payers_per_block_avg"]
    if den > 0:
        out["active_cohort_est"] = int(num / den)
        out["estimator"] = "schnabel"
    else:
        out["active_cohort_est"] = None
        out["cohort_lower_bound"] = len(marked)
        out["estimator"] = "no-recapture-lower-bound"
    return out


def tokenized() -> dict:
    out: dict = {}
    try:
        x = fetch_json("https://api.llama.fi/protocol/xstocks", timeout=30)
        out["xstocks_aum_usd"] = round(x["currentChainTvls"]["Solana"], 0)
        tokens = (((x.get("chainTvls") or {}).get("Solana") or {})
                  .get("tokensInUsd") or [])
        if tokens:
            latest = tokens[-1].get("tokens") or {}
            top = sorted(latest.items(), key=lambda kv: -kv[1])[:8]
            out["xstocks_top"] = [{"ticker": t, "usd": round(v, 0)} for t, v in top]
        hist = [[p["date"], round(p["totalLiquidityUSD"], 0)]
                for p in (x.get("tvl") or [])][-180:]
        out["xstocks_history"] = hist
    except (FetchError, KeyError, TypeError):
        pass

    try:
        toks = fetch_json(
            "https://lite-api.jup.ag/tokens/v2/search?query=xstock&limit=100",
            timeout=20)
        vol = holders = 0
        for t in toks:
            if "xstocks" not in (t.get("tags") or []):
                continue
            s = t.get("stats24h") or {}
            vol += (s.get("buyVolume") or 0) + (s.get("sellVolume") or 0)
            holders += t.get("holderCount") or 0
        out["xstocks_volume_24h_usd"] = round(vol, 0)
        out["xstocks_holders"] = holders
    except (FetchError, TypeError):
        pass

    try:
        protos = fetch_json("https://api.llama.fi/protocols", timeout=45)
        rwa = [p for p in protos if p.get("category") == "RWA"
               and isinstance((p.get("chainTvls") or {}).get("Solana"),
                              (int, float))]
        rwa.sort(key=lambda p: -p["chainTvls"]["Solana"])
        out["rwa_tvl_usd"] = round(sum(p["chainTvls"]["Solana"] for p in rwa), 0)
        out["rwa_top"] = [{"name": p["name"],
                           "usd": round(p["chainTvls"]["Solana"], 0)}
                          for p in rwa[:8]]
    except (FetchError, KeyError, TypeError):
        pass
    return out
