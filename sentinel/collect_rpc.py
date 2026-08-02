"""On-chain data straight from Solana JSON-RPC — no keys, no middlemen.

Primary endpoint is the official public mainnet RPC; two public fallbacks
cover outages. Methods used: getHealth, getVersion, getEpochInfo,
getRecentPerformanceSamples, getSupply, getRecentPrioritizationFees,
getVoteAccounts, getInflationRate, getInflationGovernor.
(getLargestAccounts is hard-disabled on public endpoints — do not add it.)
"""
from __future__ import annotations

import statistics
from typing import Any, Optional

from .net import FetchError, fetch_json

# Ankr and dRPC dropped keyless Solana access (verified 403/400) — only these
# two actually work without a key as of Aug 2026.
RPC_ENDPOINTS = [
    "https://api.mainnet-beta.solana.com",
    "https://solana-rpc.publicnode.com",
]
# publicnode never answers getSupply (hangs) — keep that method on the
# official endpoint only, with a shorter timeout instead of a fallback.
NO_FALLBACK_METHODS = {"getSupply"}

LAMPORTS = 1_000_000_000

# getRecentPrioritizationFees with no addresses returns the per-slot MINIMUM
# fee (~always 0). Passing hot AMM/aggregator accounts returns the fee needed
# to write-lock busy state — the number users actually experience.
HOT_ACCOUNTS = [
    "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8",  # Raydium AMM v4
    "JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4",   # Jupiter v6
    "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc",   # Orca Whirlpools
    "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P",   # Pump.fun
]


def rpc(method: str, params: Optional[list] = None, *, timeout: float = 25.0) -> Any:
    payload = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params:
        payload["params"] = params
    endpoints = (RPC_ENDPOINTS[:1] if method in NO_FALLBACK_METHODS
                 else RPC_ENDPOINTS)
    last = None
    for url in endpoints:
        try:
            data = fetch_json(url, post=payload, timeout=timeout, retries=1)
            if "result" in data:
                return data["result"]
            last = data.get("error")
        except FetchError as e:
            last = e
    raise FetchError(f"{method} failed on all RPC endpoints: {last}")


def network() -> dict:
    out: dict = {}

    try:
        out["health"] = "ok" if rpc("getHealth") == "ok" else "degraded"
    except FetchError:
        out["health"] = "unreachable"

    version = rpc("getVersion")
    out["node_version"] = version.get("solana-core")

    epoch_info = rpc("getEpochInfo")
    out["slot"] = epoch_info["absoluteSlot"]
    out["block_height"] = epoch_info["blockHeight"]
    out["tx_count_total"] = epoch_info.get("transactionCount")

    samples = rpc("getRecentPerformanceSamples", [60])
    perf = []
    for s in samples:
        secs = s.get("samplePeriodSecs") or 60
        slots = s.get("numSlots") or 0
        txs = s.get("numTransactions") or 0
        nonvote = s.get("numNonVoteTransactions")
        perf.append({
            "slot": s.get("slot"),
            "tps": round(txs / secs, 1),
            "true_tps": round(nonvote / secs, 1) if nonvote is not None else None,
            "slot_time_ms": round(secs / slots * 1000, 1) if slots else None,
        })
    out["perf_samples"] = perf  # newest first, one per minute
    recent = perf[:10]
    if recent:
        out["tps"] = round(statistics.median(p["tps"] for p in recent), 1)
        tt = [p["true_tps"] for p in recent if p["true_tps"] is not None]
        out["true_tps"] = round(statistics.median(tt), 1) if tt else None
        st = [p["slot_time_ms"] for p in recent if p["slot_time_ms"] is not None]
        out["slot_time_ms"] = round(statistics.median(st), 1) if st else None

    slots_in_epoch = epoch_info["slotsInEpoch"]
    slot_index = epoch_info["slotIndex"]
    slot_ms = out.get("slot_time_ms") or 400.0
    remaining_slots = slots_in_epoch - slot_index
    out["epoch"] = {
        "epoch": epoch_info["epoch"],
        "slot_index": slot_index,
        "slots_in_epoch": slots_in_epoch,
        "pct": round(slot_index / slots_in_epoch * 100, 2),
        "eta_hours": round(remaining_slots * slot_ms / 1000 / 3600, 1),
    }

    supply = rpc("getSupply", [{"excludeNonCirculatingAccountsList": True}])
    v = supply["value"]
    out["supply"] = {
        "total_sol": round(v["total"] / LAMPORTS),
        "circulating_sol": round(v["circulating"] / LAMPORTS),
        "non_circulating_sol": round(v["nonCirculating"] / LAMPORTS),
    }

    try:
        fees = rpc("getRecentPrioritizationFees", [HOT_ACCOUNTS])
        vals = sorted(f["prioritizationFee"] for f in fees)
        if vals:
            # Values are per-slot MINIMUMS (µlamports/CU) to write-lock the
            # hot accounts, so most slots are 0; p90/max plus the share of
            # nonzero slots is the readable signal, median stays for JSON.
            nonzero = [x for x in vals if x > 0]
            out["median_prioritization_fee"] = vals[len(vals) // 2]
            out["p90_prioritization_fee"] = vals[min(int(len(vals) * 0.9),
                                                     len(vals) - 1)]
            out["max_prioritization_fee"] = vals[-1]
            out["prio_fee_nonzero_pct"] = round(len(nonzero) / len(vals) * 100, 1)
    except (FetchError, KeyError, IndexError):
        pass

    try:
        infl = rpc("getInflationRate")
        out["inflation_total_pct"] = round(infl["total"] * 100, 3)
        out["inflation_validator_pct"] = round(infl["validator"] * 100, 3)
        gov = rpc("getInflationGovernor")
        out["inflation_terminal_pct"] = round(gov["terminal"] * 100, 2)
    except (FetchError, KeyError):
        pass

    return out


def validators() -> dict:
    va = rpc("getVoteAccounts", timeout=40.0)
    current, delinquent = va["current"], va["delinquent"]

    active_stake = sum(x["activatedStake"] for x in current)
    delinquent_stake = sum(x["activatedStake"] for x in delinquent)
    total = active_stake + delinquent_stake

    ranked = sorted(current, key=lambda x: x["activatedStake"], reverse=True)

    def share(n: int) -> float:
        return round(sum(x["activatedStake"] for x in ranked[:n]) / active_stake * 100, 2)

    # Nakamoto coefficient: fewest validators controlling >1/3 of active stake.
    nakamoto, cum = 0, 0
    for x in ranked:
        cum += x["activatedStake"]
        nakamoto += 1
        if cum > active_stake / 3:
            break

    # Cumulative-share curve, one entry per validator so the index *is* the
    # rank. Sampling it unevenly (every rank up front, every Nth later) would
    # plot a distorted curve, since the chart spaces points by index.
    curve, cum = [], 0
    for x in ranked:
        cum += x["activatedStake"]
        curve.append(round(cum / active_stake * 100, 2))

    commissions = [x.get("commission", 0) for x in current]
    # ~64 validators run 100% commission — private/institutional self-stake
    # (about a quarter of all stake). They'd wreck any "what does delegating
    # cost" average, but their stake share is itself a decentralization
    # metric, so report both.
    public = [x for x in current if x.get("commission", 0) < 100]
    public_stake = sum(x["activatedStake"] for x in public)
    weighted_commission = (sum(x["activatedStake"] * x.get("commission", 0)
                               for x in public) / public_stake
                           if public_stake else None)
    private_stake_pct = (round((active_stake - public_stake) / active_stake * 100, 2)
                         if active_stake else None)
    buckets = {"0%": 0, "1-4%": 0, "5-7%": 0, "8-10%": 0, ">10%": 0}
    for c in commissions:
        if c == 0:
            buckets["0%"] += 1
        elif c < 5:
            buckets["1-4%"] += 1
        elif c < 8:
            buckets["5-7%"] += 1
        elif c <= 10:
            buckets["8-10%"] += 1
        else:
            buckets[">10%"] += 1

    return {
        "active": len(current),
        "delinquent": len(delinquent),
        "total_active_stake_sol": round(active_stake / LAMPORTS),
        "delinquent_stake_sol": round(delinquent_stake / LAMPORTS),
        "delinquent_stake_pct": round(delinquent_stake / total * 100, 3) if total else 0.0,
        "nakamoto_coefficient": nakamoto,
        "top5_stake_pct": share(5),
        "top10_stake_pct": share(10),
        "top20_stake_pct": share(20),
        "avg_commission": round(weighted_commission, 2)
        if weighted_commission is not None else None,
        "avg_commission_unweighted": round(statistics.mean(commissions), 2)
        if commissions else None,
        "private_stake_pct": private_stake_pct,
        "commission_buckets": buckets,
        "stake_curve": curve,
        "top_validators": [
            {
                "vote": x["votePubkey"],
                "node": x["nodePubkey"],
                "stake_sol": round(x["activatedStake"] / LAMPORTS),
                "share_pct": round(x["activatedStake"] / active_stake * 100, 2),
                "commission": x.get("commission"),
            }
            for x in ranked[:15]
        ],
    }
