"""Cross-metric correlation: which parts of Solana actually move together.

Every other section of this report describes one metric at a time. This one
looks for relationships between them, which is where the non-obvious
observations live: whether REV is driven by DEX volume or by congestion,
whether price leads activity or follows it, whether failure rates track load.

Two methodological choices matter, and both exist to avoid publishing
confident nonsense.

**Correlate changes, not levels.** Two series that both drift upward over a
window correlate near +1 whatever the underlying relationship, which is the
classic spurious-correlation trap for non-stationary data. Every series is
first-differenced (period-over-period change) before correlating, so the
question becomes "when this moves, does that move with it?"

**Spearman, not Pearson.** Rank correlation captures monotonic relationships
without assuming linearity, and shrugs off the heavy tails and outlier blocks
this data is full of. A single 10x fee spike would dominate a Pearson figure.

**Correct for multiple comparisons.** Sixteen metrics make 120 pairs. Testing
all of them at a 5% threshold yields about six "significant" results by pure
chance, and the first run of this module duly announced that delinquent
validators move inversely to tokenized-equity AUM. Reporting that would be
worse than reporting nothing. The Benjamini-Hochberg procedure controls the
false-discovery rate across the whole family of tests, so what survives is
worth reading. p-values come from an exact Student-t CDF implemented here,
since SciPy is unavailable under the stdlib-only rule.
"""
from __future__ import annotations

import math
from typing import Optional

from . import history

# Twelve hours at the 30-minute cadence. Set from evidence, not taste: at
# ten points the procedure surfaced a -0.73 correlation between delinquent
# validators and tokenized-equity AUM, two quantities with no plausible
# mechanism linking them, purely because eight hours is not enough history to
# tell a relationship from a coincidence. Newly-added metrics are therefore
# excluded until they have earned a real sample.
MIN_POINTS = 24

# Metrics worth relating, with display names. Deliberately excludes monotonic
# counters (block height, lifetime transactions), whose differences are
# near-constant and correlate with everything.
SERIES = {
    "tps": "Total TPS",
    "true_tps": "Non-vote TPS",
    "slot_time_ms": "Slot time",
    "median_tx_fee": "Median tx fee",
    "base_fee_only_pct": "Share paying base fee only",
    "prio_congestion_pct": "AMM write-lock congestion",
    "failure_rate_pct": "Program failure rate",
    "activity_idx": "Activity index",
    "sol_price": "SOL price",
    "tvl": "DeFi TVL",
    "stables": "Stablecoin supply",
    "dex_vol_24h": "DEX volume",
    "rev_24h": "REV",
    "app_fees_24h": "App fees",
    "validators_delinquent": "Delinquent validators",
    "xstocks_aum": "xStocks AUM",
}

# Two-sided 95% Student-t critical values by degrees of freedom, for turning a
# sample size into a minimum believable correlation. scipy is unavailable
# under the stdlib-only rule, so the table is inline.
T_95 = {
    8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160,
    14: 2.145, 15: 2.131, 16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093,
    20: 2.086, 25: 2.060, 30: 2.042, 40: 2.021, 50: 2.009, 60: 2.000,
}


def _betacf(a: float, b: float, x: float) -> float:
    """Continued fraction for the incomplete beta function (Lentz's method)."""
    TINY, EPS, MAXIT = 1e-30, 3e-16, 300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < TINY:
        d = TINY
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < TINY:
            d = TINY
        c = 1.0 + aa / c
        if abs(c) < TINY:
            c = TINY
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < TINY:
            d = TINY
        c = 1.0 + aa / c
        if abs(c) < TINY:
            c = TINY
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return h


def _betai(a: float, b: float, x: float) -> float:
    """Regularised incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
             + a * math.log(x) + b * math.log1p(-x))
    front = math.exp(lbeta)
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def t_two_sided_p(t: float, df: int) -> float:
    """Two-sided p-value for a t statistic. Exact, not a table lookup."""
    if df <= 0:
        return 1.0
    return _betai(df / 2.0, 0.5, df / (df + t * t))


def rho_p_value(rho: float, n: int) -> Optional[float]:
    """p-value for a Spearman rho via the standard t approximation."""
    df = n - 2
    if df < 1 or abs(rho) >= 1.0:
        return 0.0 if abs(rho) >= 1.0 and df >= 1 else None
    t = rho * math.sqrt(df / (1.0 - rho * rho))
    return t_two_sided_p(t, df)


def benjamini_hochberg(pvals: list, q: float = 0.05) -> list:
    """Which hypotheses survive at false-discovery rate q. Returns a boolean
    per input p-value, in the original order."""
    m = len(pvals)
    if m == 0:
        return []
    order = sorted(range(m), key=lambda i: pvals[i])
    keep = [False] * m
    cutoff_rank = -1
    for rank, idx in enumerate(order, start=1):
        if pvals[idx] <= q * rank / m:
            cutoff_rank = rank
    # Everything up to the largest passing rank is accepted, which is what
    # makes BH more powerful than Bonferroni.
    for rank, idx in enumerate(order, start=1):
        if rank <= cutoff_rank:
            keep[idx] = True
    return keep


def _t_crit(df: int) -> float:
    if df in T_95:
        return T_95[df]
    keys = sorted(T_95)
    if df < keys[0]:
        return T_95[keys[0]]
    if df > keys[-1]:
        return 1.96  # normal approximation for large samples
    # Nearest tabulated df below.
    return T_95[max(k for k in keys if k <= df)]


def critical_rho(n: int) -> Optional[float]:
    """Smallest |rho| that clears a two-sided 5% test at this sample size."""
    df = n - 2
    if df < 1:
        return None
    t = _t_crit(df)
    return t / math.sqrt(t * t + df)


def _ranks(values: list) -> list:
    """Ranks with ties averaged, which is what Spearman requires."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        shared = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[order[k]] = shared
        i = j + 1
    return ranks


def _pearson(xs: list, ys: list) -> Optional[float]:
    n = len(xs)
    if n < 2:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    dx = [x - mx for x in xs]
    dy = [y - my for y in ys]
    denom = math.sqrt(sum(a * a for a in dx) * sum(b * b for b in dy))
    if denom == 0:
        return None  # a flat series has no correlation to report
    return sum(a * b for a, b in zip(dx, dy)) / denom


def spearman(xs: list, ys: list) -> Optional[float]:
    """Spearman's rho: Pearson correlation of the ranks."""
    if len(xs) != len(ys) or len(xs) < 3:
        return None
    return _pearson(_ranks(xs), _ranks(ys))


def _aligned_changes(rows: list, a: str, b: str) -> tuple:
    """Period-over-period changes for two metrics, over rows where both are
    present and consecutive. Differencing removes the shared trend that makes
    unrelated series look correlated."""
    da, db = [], []
    prev = None
    for r in rows:
        va, vb = r.get(a), r.get(b)
        if not isinstance(va, (int, float)) or not isinstance(vb, (int, float)):
            prev = None  # a gap breaks the chain rather than spanning it
            continue
        if prev is not None:
            da.append(va - prev[0])
            db.append(vb - prev[1])
        prev = (va, vb)
    return da, db


def correlations(rows: Optional[list] = None) -> dict:
    rows = history.load() if rows is None else rows
    present = [k for k in SERIES
               if sum(1 for r in rows if isinstance(r.get(k), (int, float)))
               >= MIN_POINTS + 1]

    pairs = []
    for i, a in enumerate(present):
        for b in present[i + 1:]:
            da, db = _aligned_changes(rows, a, b)
            if len(da) < MIN_POINTS:
                continue
            rho = spearman(da, db)
            if rho is None:
                continue
            pv = rho_p_value(rho, len(da))
            if pv is None:
                continue
            pairs.append({
                "a": a, "b": b,
                "a_label": SERIES[a], "b_label": SERIES[b],
                "rho": round(rho, 3),
                "n": len(da),
                "p": round(pv, 5),
            })

    # Family-wide false-discovery control across every pair tested, not a
    # per-pair threshold. Without this, ~5% of 120 pairs pass by chance.
    keep = benjamini_hochberg([p["p"] for p in pairs], q=0.05)
    for pair, ok in zip(pairs, keep):
        pair["significant"] = ok

    pairs.sort(key=lambda p: -abs(p["rho"]))
    strong = [p for p in pairs if p["significant"]]
    return {
        "method": ("Spearman rank correlation of period-over-period changes, "
                   "with Benjamini-Hochberg false-discovery control at q=0.05 "
                   "across all pairs tested"),
        "metrics_considered": len(present),
        "pairs_tested": len(pairs),
        "significant_count": len(strong),
        "top": strong[:12],
        # Reported so a reader can see how much was tested to find this much,
        # which is the context that makes the survivors meaningful.
        "sample_size": max((p["n"] for p in pairs), default=0),
    }
