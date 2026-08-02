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
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue  # never let one corrupt line kill the run
    return rows


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


def headline_row(snapshot: dict) -> dict:
    """Flatten a full snapshot into the compact row we keep history for."""
    def g(*path: str) -> Optional[Any]:
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
        "circulating_sol": g("network", "supply", "circulating_sol"),
        "staked_sol": g("validators", "total_active_stake_sol"),
        "inflation_pct": g("network", "inflation_total_pct"),
    }
