"""Anomaly detection over the metric history.

Two complementary layers:

1. Robust statistical outliers — for each watched metric, the latest value is
   compared to a rolling baseline using the median and MAD (median absolute
   deviation). MAD-based z-scores shrug off the occasional bad sample that
   would poison a mean/stddev baseline, which matters when data comes from
   free public endpoints.

2. Absolute health rules — thresholds that are meaningful regardless of
   history (e.g. delinquent stake above 5%, RPC reporting unhealthy).

Every finding carries the evidence (value, baseline, z-score, threshold) so
the report can show *why* something was flagged, not just that it was.
"""
from __future__ import annotations

import math
import statistics
import time
from typing import Optional

from . import history

WINDOW = 336          # baseline window: ~7 days at a 30-min cadence
MIN_BASELINE = 12     # need at least this many points before flagging
Z_WARNING = 3.5
Z_CRITICAL = 6.0

# metric key in history -> (label, unit, direction of concern)
# direction: "both" flags spikes and drops, "drop" / "spike" only one side.
WATCHED = {
    "tps": ("Transactions per second", "tps", "drop"),
    "true_tps": ("Non-vote TPS", "tps", "drop"),
    "slot_time_ms": ("Average slot time", "ms", "spike"),
    "validators_delinquent": ("Delinquent validators", "", "spike"),
    "delinquent_stake_pct": ("Delinquent stake", "%", "spike"),
    "sol_price": ("SOL price", "USD", "both"),
    "tvl": ("DeFi TVL", "USD", "both"),
    "stables": ("Stablecoin supply", "USD", "both"),
    "dex_vol_24h": ("DEX volume (24h)", "USD", "both"),
    "fees_24h": ("Network fees (24h)", "USD", "both"),
    "activity_idx": ("Activity index (fee payers per block)", "", "both"),
    # Fees spiking is congestion worth flagging; fees falling is not an
    # incident, so this one is watched in the spike direction only.
    "median_tx_fee": ("Median transaction fee", "lamports", "spike"),
    # A jump in failed transactions is what congestion feels like to a user,
    # so it is watched in the spike direction.
    "failure_rate_pct": ("Median program failure rate", "%", "spike"),
}


def robust_z(value: float, window: list[float]) -> Optional[float]:
    """MAD-based z-score of value against window; None if the window is flat."""
    if len(window) < MIN_BASELINE:
        return None
    med = statistics.median(window)
    mad = statistics.median(abs(x - med) for x in window)
    if mad == 0:
        # Fall back to stdev for near-constant series (e.g. delinquency at 0).
        try:
            sd = statistics.stdev(window)
        except statistics.StatisticsError:
            return None
        if sd == 0:
            return None if value == med else float("inf")
        return (value - med) / sd
    return (value - med) / (1.4826 * mad)


def detect(rows: list[dict], latest: dict) -> list[dict]:
    findings: list[dict] = []
    now = int(time.time())

    # ---- Layer 1: statistical outliers ---------------------------------
    for key, (label, unit, direction) in WATCHED.items():
        value = latest.get(key)
        if value is None or isinstance(value, bool) or not isinstance(value, (int, float)):
            continue
        window = [v for _, v in history.series(rows, key)][-WINDOW:]
        # Exclude the point being scored if it is already in the window.
        if window and window[-1] == value:
            window = window[:-1]
        z = robust_z(float(value), window)
        if z is None:
            continue
        if direction == "drop" and z > 0:
            continue
        if direction == "spike" and z < 0:
            continue
        if abs(z) >= Z_WARNING:
            med = statistics.median(window)
            unit_s = (" " + unit) if unit else ""
            direction = "above" if z > 0 else "below"
            # A perfectly flat baseline (e.g. delinquency pinned at one value
            # for days) gives an infinite z-score. Reporting "inf standard
            # deviations" reads like a bug, so describe the move instead.
            if math.isinf(z):
                detail = (f"{label} moved off a previously constant baseline: "
                          f"now {value:,.2f}{unit_s}, and it had been "
                          f"{med:,.2f} for the whole 7-day window.")
            else:
                detail = (f"{label} is {abs(z):.1f} robust standard deviations "
                          f"{direction} its 7-day baseline "
                          f"(now {value:,.2f}{unit_s}, typical {med:,.2f}).")
            findings.append({
                "ts": now,
                "metric": key,
                "label": label,
                "severity": "critical" if abs(z) >= Z_CRITICAL else "warning",
                "kind": "spike" if z > 0 else "drop",
                "value": value,
                "baseline_median": med,
                "z_score": None if math.isinf(z) else round(z, 2),
                "unit": unit,
                "detail": detail,
            })

    # ---- Layer 2: absolute health rules --------------------------------
    def rule(cond: bool, metric: str, label: str, severity: str, detail: str,
             value=None) -> None:
        if cond:
            findings.append({"ts": now, "metric": metric, "label": label,
                             "severity": severity, "kind": "threshold",
                             "value": value, "detail": detail})

    tps = latest.get("tps")
    rule(isinstance(tps, (int, float)) and tps < 1000, "tps",
         "Network throughput", "critical",
         f"Total TPS at {tps:,.0f}, far below normal mainnet levels; possible "
         f"degradation or an RPC reporting artifact." if isinstance(tps, (int, float)) else "",
         tps)

    slot_ms = latest.get("slot_time_ms")
    rule(isinstance(slot_ms, (int, float)) and slot_ms > 600, "slot_time_ms",
         "Slot time", "warning",
         f"Average slot time {slot_ms:.0f} ms against a 400 ms target: blocks "
         f"are landing slowly." if isinstance(slot_ms, (int, float)) else "",
         slot_ms)

    dq_pct = latest.get("delinquent_stake_pct")
    if isinstance(dq_pct, (int, float)):
        rule(dq_pct > 5.0, "delinquent_stake_pct", "Delinquent stake",
             "critical" if dq_pct > 10 else "warning",
             f"{dq_pct:.2f}% of active stake is delinquent (5% is the alert "
             f"line; 33% would halt consensus).", dq_pct)

    chg = latest.get("sol_change_24h")
    if isinstance(chg, (int, float)) and abs(chg) >= 10:
        rule(True, "sol_change_24h", "SOL price move",
             "critical" if abs(chg) >= 20 else "warning",
             f"SOL moved {chg:+.1f}% in 24h.", chg)

    order = {"critical": 0, "warning": 1, "info": 2}

    # A bad enough move trips both layers for the same metric (TPS collapsing
    # is simultaneously a 100-sigma outlier and below the absolute floor).
    # Emitting both double-counts one incident, so keep one finding per
    # metric: the more severe, and on a tie the threshold rule, whose text
    # says what the number means rather than how unusual it is.
    def rank(f: dict) -> tuple:
        return (order.get(f["severity"], 3), 0 if f["kind"] == "threshold" else 1)

    best: dict[str, dict] = {}
    for f in findings:
        current = best.get(f["metric"])
        if current is None or rank(f) < rank(current):
            if current is not None:
                f = {**f, "also_flagged_by": current["kind"]}
            best[f["metric"]] = f
        else:
            best[f["metric"]] = {**current, "also_flagged_by": f["kind"]}

    merged = list(best.values())
    merged.sort(key=lambda f: (order.get(f["severity"], 3), f["metric"]))
    return merged
