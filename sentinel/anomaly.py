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

# metric key -> (label, unit, direction of concern, minimum move worth
# flagging as a percentage of the baseline).
#
# direction: "both" flags spikes and drops, "drop" / "spike" only one side.
#
# The minimum move is not optional padding, it is what keeps the z-score
# honest. MAD shrinks toward zero on a metric that has been stable, so an
# utterly trivial change divided by a near-zero scale produces an enormous
# z-score: TVL moving 0.13%, from $4.7499B to $4.7559B, scored 415 sigma and
# was published as CRITICAL. Statistical unusualness alone is not a reason to
# wake anyone up; a finding has to clear both bars, be surprising *and* be
# big enough to matter.
WATCHED = {
    "tps": ("Transactions per second", "tps", "drop", 20.0),
    "true_tps": ("Non-vote TPS", "tps", "drop", 20.0),
    "slot_time_ms": ("Average slot time", "ms", "spike", 15.0),
    "validators_delinquent": ("Delinquent validators", "", "spike", 50.0),
    # Delinquent stake sits near zero in normal operation, so a relative move
    # is meaningless noise. Real trouble is caught by the absolute rule below.
    "delinquent_stake_pct": ("Delinquent stake", "%", "spike", 200.0),
    "sol_price": ("SOL price", "USD", "both", 5.0),
    "tvl": ("DeFi TVL", "USD", "both", 5.0),
    "stables": ("Stablecoin supply", "USD", "both", 3.0),
    "dex_vol_24h": ("DEX volume (24h)", "USD", "both", 25.0),
    "fees_24h": ("Network fees (24h)", "USD", "both", 25.0),
    "activity_idx": ("Activity index (fee payers per block)", "", "both", 25.0),
    # Fees spiking is congestion worth flagging; fees falling is not an
    # incident, so this one is watched in the spike direction only.
    "median_tx_fee": ("Median transaction fee", "lamports", "spike", 50.0),
    # A jump in failed transactions is what congestion feels like to a user,
    # so it is watched in the spike direction.
    "failure_rate_pct": ("Median program failure rate", "%", "spike", 30.0),
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
    for key, (label, unit, direction, min_change_pct) in WATCHED.items():
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
        if abs(z) < Z_WARNING:
            continue

        med = statistics.median(window)
        # Second bar: the move has to be big enough to act on. Without this a
        # stable metric produces a huge z-score for a change nobody would
        # notice, and every such alert spends the reader's trust in the ones
        # that matter.
        if med:
            change_pct = abs(value - med) / abs(med) * 100
            if change_pct < min_change_pct:
                continue
        else:
            change_pct = None

        unit_s = (" " + unit) if unit else ""
        way = "above" if z > 0 else "below"
        move = f" a {change_pct:.1f}% move" if change_pct is not None else ""
        # A perfectly flat baseline (e.g. delinquency pinned at one value for
        # days) gives an infinite z-score. Reporting "inf standard deviations"
        # reads like a bug, so describe the move instead.
        if math.isinf(z):
            detail = (f"{label} moved off a previously constant baseline: "
                      f"now {value:,.2f}{unit_s}, and it had been "
                      f"{med:,.2f} for the whole 7-day window.")
        else:
            detail = (f"{label} is {abs(z):.1f} robust standard deviations "
                      f"{way} its 7-day baseline:{move} to "
                      f"{value:,.2f}{unit_s} from a typical {med:,.2f}.")
        findings.append({
            "ts": now,
            "metric": key,
            "label": label,
            "severity": "critical" if abs(z) >= Z_CRITICAL else "warning",
            "kind": "spike" if z > 0 else "drop",
            "value": value,
            "baseline_median": med,
            "z_score": None if math.isinf(z) else round(z, 2),
            "change_pct": round(change_pct, 2) if change_pct is not None else None,
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
