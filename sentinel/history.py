"""Append-only metric history (JSON Lines) — the memory behind trends and
anomaly baselines.

Each run appends one compact row of headline metrics to data/history.jsonl.
The file is committed back to the repo by the GitHub Actions run, so history
accumulates across runs with no database or external storage.
"""
from __future__ import annotations

import json
import os
import time
from typing import Any, Optional

HISTORY_PATH = os.path.join("data", "history.jsonl")
MAX_ROWS = 4320  # ~90 days at a 30-minute cadence


def append(row: dict, path: str = HISTORY_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    rows = load(path)
    rows.append(row)
    rows = rows[-MAX_ROWS:]
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, separators=(",", ":")) + "\n")


def load(path: str = HISTORY_PATH) -> list[dict]:
    """Read the metric history, tolerating damage.

    The file is committed by CI and can also be written locally, so it is
    merged with `merge=union` (see .gitattributes). That is the right merge
    for an append-only log but it can duplicate a timestamp when two runs
    overlap, and a conflict resolved by hand could leave a stray line. Both
    are handled here rather than left to poison the anomaly baselines: rows
    are deduplicated by timestamp, keeping the most complete one, and
    returned in timestamp order.
    """
    if not os.path.exists(path):
        return []
    by_ts: dict = {}
    loose: list = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(("<<<<<<<", "=======", ">>>>>>>")):
                continue  # never let one bad line kill the run
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(row, dict):
                continue
            ts = row.get("ts")
            if ts is None:
                loose.append(row)
                continue
            prev = by_ts.get(ts)
            # More populated row wins: a later schema adds fields, and a run
            # with a stale section writes fewer.
            if prev is None or _filled(row) > _filled(prev):
                by_ts[ts] = row
    return [by_ts[k] for k in sorted(by_ts)] + loose


def _filled(row: dict) -> int:
    return sum(1 for v in row.values() if v is not None)


def series(rows: list[dict], key: str) -> list[tuple[float, float]]:
    """Extract (timestamp, value) pairs for one metric, skipping gaps."""
    out = []
    for r in rows:
        v = r.get(key)
        t = r.get("ts")
        if v is None or t is None:
            continue
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            out.append((float(t), float(v)))
    return out


def headline_row(snapshot: dict, stale: Optional[list] = None) -> dict:
    """Flatten a full snapshot into the compact row we keep history for.

    Sections named in `stale` were served from the previous snapshot rather
    than fetched this run, so their metrics are recorded as None. A gap is
    honest; repeating yesterday's number under today's timestamp is not, and
    it would quietly corrupt the anomaly baselines built from this file.
    """
    stale_sections = set(stale or ())

    def g(*path: str) -> Optional[Any]:
        if path and path[0] in stale_sections:
            return None
        cur: Any = snapshot
        for p in path:
            if not isinstance(cur, dict) or p not in cur:
                return None
            cur = cur[p]
        return cur

    return {
        "ts": snapshot.get("ts", int(time.time())),
        "slot": g("network", "slot"),
        "block_height": g("network", "block_height"),
        "tps": g("network", "tps"),
        "true_tps": g("network", "true_tps"),
        "slot_time_ms": g("network", "slot_time_ms"),
        "epoch": g("network", "epoch", "epoch"),
        "epoch_pct": g("network", "epoch", "pct"),
        "validators_active": g("validators", "active"),
        "validators_delinquent": g("validators", "delinquent"),
        "delinquent_stake_pct": g("validators", "delinquent_stake_pct"),
        "nakamoto": g("validators", "nakamoto_coefficient"),
        "avg_commission": g("validators", "avg_commission"),
        "sol_price": g("market", "price_usd"),
        "sol_change_24h": g("market", "change_24h_pct"),
        "market_cap": g("market", "market_cap_usd"),
        "tvl": g("defi", "tvl_usd"),
        "stables": g("defi", "stablecoins_usd"),
        "dex_vol_24h": g("defi", "dex_volume_24h_usd"),
        "fees_24h": g("defi", "fees_24h_usd"),
        "rev_24h": g("defi", "rev_24h_usd"),
        "median_fee_lamports": g("network", "median_prioritization_fee"),
        "activity_idx": g("activity", "activity_index"),
        "active_cohort": g("activity", "active_cohort_est"),
        "median_tx_fee": g("activity", "median_tx_fee_lamports"),
        "p90_tx_fee": g("activity", "p90_tx_fee_lamports"),
        "base_fee_only_pct": g("activity", "base_fee_only_pct"),
        "circulating_sol": g("network", "supply", "circulating_sol"),
        "staked_sol": g("validators", "total_active_stake_sol"),
        "inflation_pct": g("network", "inflation_total_pct"),
    }
