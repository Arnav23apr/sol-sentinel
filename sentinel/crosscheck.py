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

# Fee sampling is 8 blocks out of ~216,000 in a day, so its confidence
# interval is wide; only a large divergence means anything.
FEE_TOLERANCE_PCT = 60.0
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

    # 1. Chain fees: our own block sampling vs DeFiLlama's indexer. Judged
    #    against our sample's 95% confidence interval rather than a flat
    #    tolerance, since the interval is what the sample can actually support.
    measured_sol = activity.get("measured_daily_fees_sol")
    price = market.get("price_usd")
    llama_usd = defi.get("chain_fees_24h_usd")
    low = activity.get("measured_daily_fees_sol_low")
    high = activity.get("measured_daily_fees_sol_high")
    if measured_sol is not None and price and llama_usd:
        ours = round(measured_sol * price)
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
        }
        if low is not None and high is not None:
            lo_usd, hi_usd = round(low * price), round(high * price)
            check["a_interval_95"] = [lo_usd, hi_usd]
            check["agrees"] = lo_usd <= theirs <= hi_usd
            check["basis"] = "95% CI of an 8-block sample"
        else:
            check["agrees"] = abs(check["gap_pct"] or 0) <= FEE_TOLERANCE_PCT
            check["tolerance_pct"] = FEE_TOLERANCE_PCT
            check["basis"] = "fixed tolerance"
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
        if c.get("a_interval_95"):
            lo, hi = c["a_interval_95"]
            basis = (f"outside the {lo:,} to {hi:,} {c['unit']} 95% interval "
                     f"our sample supports")
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
