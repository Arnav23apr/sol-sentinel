"""Snapshot orchestrator.

Runs every collector with per-source error isolation: one dead API degrades
that section to the last good copy (marked stale) instead of blanking the
report. The result is a single snapshot dict that renderers and the anomaly
engine consume.
"""
from __future__ import annotations

import json
import os
import time

from . import anomaly, history
from .collect_activity import activity, tokenized
from .collect_defi import defi
from .collect_dev import dev
from .collect_market import market
from .collect_news import news
from .collect_rpc import network, validators

LATEST_PATH = os.path.join("data", "latest.json")

SECTIONS = [
    ("network", network),
    ("validators", validators),
    ("market", market),
    ("defi", defi),
    ("dev", dev),
    ("news", news),
    ("activity", activity),
    ("tokenized", tokenized),
]


def _load_previous() -> dict:
    if not os.path.exists(LATEST_PATH):
        return {}
    try:
        with open(LATEST_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def collect(verbose: bool = True) -> dict:
    previous = _load_previous()
    snapshot: dict = {"ts": int(time.time()),
                      "generated_utc": time.strftime("%Y-%m-%d %H:%M UTC",
                                                     time.gmtime()),
                      "errors": {}, "stale_sections": []}

    for name, fn in SECTIONS:
        started = time.time()
        try:
            snapshot[name] = fn()
            if verbose:
                print(f"  [ok] {name} ({time.time() - started:.1f}s)")
        except Exception as e:  # noqa: BLE001 — isolation is the whole point
            snapshot["errors"][name] = repr(e)
            prev_section = previous.get(name)
            if prev_section is not None:
                snapshot[name] = prev_section
                snapshot["stale_sections"].append(name)
            if verbose:
                print(f"  [FAIL -> {'stale copy' if prev_section else 'omitted'}] "
                      f"{name}: {e!r}")

    # Market-cap fallback: non-CoinGecko price sources have no mcap, but we
    # always know circulating supply from the chain itself.
    m, n = snapshot.get("market"), snapshot.get("network")
    if (m and n and m.get("market_cap_usd") is None
            and m.get("price_usd") and (n.get("supply") or {}).get("circulating_sol")):
        m["market_cap_usd"] = round(m["price_usd"] * n["supply"]["circulating_sol"])
        m["market_cap_estimated"] = True

    # History + anomalies.
    row = history.headline_row(snapshot)
    rows = history.load()
    snapshot["anomalies"] = anomaly.detect(rows, row)
    history.append(row)
    snapshot["history"] = (rows + [row])[-1440:]  # last ~30 days for charts

    os.makedirs(os.path.dirname(LATEST_PATH), exist_ok=True)
    persist = {k: v for k, v in snapshot.items() if k != "history"}
    with open(LATEST_PATH, "w", encoding="utf-8") as f:
        json.dump(persist, f, separators=(",", ":"))

    return snapshot
