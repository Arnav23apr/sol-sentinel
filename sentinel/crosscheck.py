"""Cross-source validation.

Most of this report takes each number on faith from whichever endpoint served
it. Several figures, though, are observable from two independent directions,
and comparing them is worth more than either reading alone: agreement is
evidence the number is real, and disagreement is itself a finding.

Three checks run each snapshot:

1. **Chain fees.** Sentinel measures fees directly from sampled blocks and
   extrapolates to a day; DeFiLlama reports the same quantity from its own
   indexer. These are fully independent paths to one number.
2. **SOL price.** CoinGecko aggregates centralised venues; Jupiter quotes the
   on-chain DEX price. A persistent gap between them is a real market
   condition (thin on-chain liquidity, or a venue lagging), not noise.
3. **Circulating supply.** The chain reports it via getSupply; CoinGecko
   publishes its own figure, which feeds its market cap.

Each check reports the relative gap and whether it exceeds a tolerance. The
tolerances are deliberately loose: these are different measurement
methodologies, not the same number twice, so small disagreements are expected
and only a large one is informative.
"""
from __future__ import annotations

from typing import Optional

from .net import FetchError, fetch_json

WSOL_MINT = "So11111111111111111111111111111111111111112"

# Fee sampling reads 8 blocks out of ~205,000 in a day, so it can corroborate
# the magnitude of an independently reported total but not pin its value. Two
# measurements of a bursty, heavy-tailed quantity landing within 2x of each
# other is real corroboration; beyond that, one of them is measuring something
# else.
FEE_RATIO_BAND = 2.0
PRICE_TOLERANCE_PCT = 2.0
SUPPLY_TOLERANCE_PCT = 2.0


def _gap_pct(a: float, b: float) -> Optional[float]:
    """Relative difference between two readings, against their mean so that
    neither source is treated as the authority."""
    mid = (a + b) / 2
    if not mid:
        return None
    return round((a - b) / mid * 100, 2)


def _check(name: str, label: str, ours: Optional[float], theirs: Optional[float],
           our_src: str, their_src: str, tolerance: float,
           unit: str = "") -> Optional[dict]:
    if ours is None or theirs is None:
        return None
    gap = _gap_pct(float(ours), float(theirs))
    if gap is None:
        return None
    return {
        "check": name,
        "label": label,
        "a_source": our_src,
        "a_value": ours,
        "b_source": their_src,
        "b_value": theirs,
        "unit": unit,
        "gap_pct": gap,
        "tolerance_pct": tolerance,
        "agrees": abs(gap) <= tolerance,
    }


def crosscheck(snapshot: dict) -> dict:
    """Compare independently-sourced views of the same quantities."""
    checks: list[dict] = []

    network = snapshot.get("network") or {}
    market = snapshot.get("market") or {}
    defi = snapshot.get("defi") or {}
    activity = snapshot.get("activity") or {}

    # 1. Chain fees: our own block sampling vs DeFiLlama's indexer.
    price = market.get("price_usd")
    llama_usd = defi.get("chain_fees_24h_usd")
    per_block = activity.get("avg_fees_per_block_sol")
    rate = network.get("blocks_per_day_measured")
    if per_block is not None and price and llama_usd and rate:
        ours = round(per_block * rate * price)
        theirs = round(llama_usd)
        check = {
            "check": "chain_fees",
            "label": "Chain fees (24h)",
            "a_source": "sampled blocks (RPC)",
            "a_value": ours,
            "b_source": "DeFiLlama",
            "b_value": theirs,
            "unit": "USD",
            "gap_pct": _gap_pct(ours, theirs),
            "blocks_per_day": round(rate),
        }
        lo, hi = (activity.get("fees_per_block_sol_low"),
                  activity.get("fees_per_block_sol_high"))
        if lo is not None and hi is not None:
            check["a_interval_95"] = [round(lo * rate * price),
                                      round(hi * rate * price)]
        # Judged on order of magnitude, not on the 95% interval. The interval
        # comes from between-block variance in a sample of eight, but fees are
        # bursty across the day as well as heavy-tailed within a block, so it
        # understates the true error and would flag a disagreement nearly
        # every run. What eight blocks can honestly support is whether an
        # independent measurement lands in the same ballpark; the interval is
        # still published as context.
        ratio = ours / theirs if theirs else None
        check["ratio"] = round(ratio, 2) if ratio else None
        check["agrees"] = bool(ratio and 1 / FEE_RATIO_BAND <= ratio <= FEE_RATIO_BAND)
        check["basis"] = f"within {FEE_RATIO_BAND:g}x (8-block sample)"
        checks.append(check)

    # 2. SOL price: centralised aggregate vs on-chain DEX quote.
    if price and market.get("source") != "jupiter":
        try:
            tok = fetch_json(f"https://lite-api.jup.ag/price/v3?ids={WSOL_MINT}",
                             timeout=12)[WSOL_MINT]
            checks.append(_check(
                "sol_price", "SOL price",
                round(float(price), 2), round(float(tok["usdPrice"]), 2),
                market.get("source", "aggregator"), "Jupiter (on-chain DEX)",
                PRICE_TOLERANCE_PCT, "USD"))
        except (FetchError, KeyError, TypeError, ValueError):
            pass

    # 3. Circulating supply: the chain itself vs CoinGecko's published figure.
    chain_supply = (network.get("supply") or {}).get("circulating_sol")
    cg_supply = market.get("circulating_supply")
    if chain_supply and cg_supply:
        checks.append(_check(
            "circulating_supply", "Circulating supply",
            round(chain_supply), round(float(cg_supply)),
            "getSupply (RPC)", "CoinGecko",
            SUPPLY_TOLERANCE_PCT, "SOL"))

    checks = [c for c in checks if c]
    return {
        "checks": checks,
        "agree": sum(1 for c in checks if c["agrees"]),
        "total": len(checks),
        "divergences": [c for c in checks if not c["agrees"]],
    }


def divergence_findings(result: dict) -> list[dict]:
    """Turn material disagreements into report findings, in the same shape the
    anomaly engine emits so both render through one code path."""
    out = []
    for c in result.get("divergences", []):
        if c.get("ratio"):
            basis = (f"a {c['ratio']:.2f}x ratio, outside the "
                     f"{FEE_RATIO_BAND:g}x band two independent measurements "
                     f"of this quantity should stay within")
        else:
            basis = (f"a {abs(c['gap_pct']):.1f}% gap against a "
                     f"{c.get('tolerance_pct', 0):.0f}% tolerance")
        out.append({
            "metric": f"crosscheck_{c['check']}",
            "label": f"{c['label']}: sources disagree",
            "severity": "warning",
            "kind": "divergence",
            "value": c["a_value"],
            "detail": (f"{c['a_source']} reports {c['a_value']:,} "
                       f"{c['unit']} while {c['b_source']} reports "
                       f"{c['b_value']:,} {c['unit']}, {basis}. Treat this "
                       f"figure as uncertain until they reconverge."),
        })
    return out
