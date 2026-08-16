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

from . import anomaly, correlate, crosscheck, history
from .collect_activity import activity, tokenized
from .collect_defi import defi
from .collect_dev import dev
from .collect_flows import flows, net_flow
from .collect_market import market
from .collect_news import news
from .collect_onchain import onchain
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


def _write_json(path: str, payload: dict) -> None:
    """Write via a temp file and rename, so a crash or a full disk can never
    leave a half-written JSON file behind. The CI job commits whatever is on
    disk, and a truncated report.json would break every consumer of it."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))
    os.replace(tmp, path)


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

    # Direct on-chain observations. Runs after the loop because it needs the
    # current slot and the top validators discovered above, and it is isolated
    # the same way every other section is.
    started = time.time()
    try:
        snapshot["onchain"] = onchain(
            slot_ms=(snapshot.get("network") or {}).get("slot_time_ms"),
            top_validators=(snapshot.get("validators") or {}).get("top_validators"))
        if verbose:
            n_prog = len(snapshot["onchain"].get("programs") or [])
            print(f"  [ok] onchain ({n_prog} programs, {time.time() - started:.1f}s)")
    except Exception as e:  # noqa: BLE001 — isolation is the whole point
        snapshot["errors"]["onchain"] = repr(e)
        prev_section = previous.get("onchain")
        if prev_section is not None:
            snapshot["onchain"] = prev_section
            snapshot["stale_sections"].append("onchain")
        if verbose:
            print(f"  [FAIL] onchain: {e!r}")

    # Exchange and large-holder balances. Runs after the loop because it uses
    # the SOL price for a USD figure, and is isolated like every other source.
    started = time.time()
    try:
        snapshot["flows"] = flows(
            price_usd=(snapshot.get("market") or {}).get("price_usd"))
        if verbose:
            fl = snapshot["flows"]
            print(f"  [ok] flows ({fl['verified']} accounts verified, "
                  f"{fl['total_sol']:,.0f} SOL, {time.time() - started:.1f}s)")
    except Exception as e:  # noqa: BLE001 — isolation is the whole point
        snapshot["errors"]["flows"] = repr(e)
        prev_section = previous.get("flows")
        if prev_section is not None:
            snapshot["flows"] = prev_section
            snapshot["stale_sections"].append("flows")
        if verbose:
            print(f"  [FAIL] flows: {e!r}")

    # Block-production rate measured from how far block height advanced
    # between runs. Anything extrapolated from a per-block figure needs this
    # rather than a nominal slots-per-day constant, which runs ~5% high.
    prior_rows = history.load()
    rate = history.blocks_per_day(prior_rows)
    if rate and isinstance(snapshot.get("network"), dict):
        snapshot["network"]["blocks_per_day_measured"] = round(rate)

    # Net flow needs the accumulated history, so it is derived once the prior
    # rows are loaded rather than inside the collector above.
    if isinstance(snapshot.get("flows"), dict):
        snapshot["flows"].update(
            net_flow(prior_rows, snapshot["flows"].get("total_sol")))

    # Cross-source validation: compare independently-sourced views of the same
    # quantity. Divergences become findings alongside the anomalies.
    try:
        snapshot["crosscheck"] = crosscheck.crosscheck(snapshot)
        if verbose:
            cc = snapshot["crosscheck"]
            print(f"  [ok] crosscheck ({cc['agree']}/{cc['total']} sources agree)")
    except Exception as e:  # noqa: BLE001 — a nice-to-have, never fatal
        snapshot["errors"]["crosscheck"] = repr(e)
        snapshot["crosscheck"] = {"checks": [], "agree": 0, "total": 0,
                                  "divergences": []}

    # History + anomalies. Metrics from a stale section are blanked out of the
    # recorded row: re-recording last run's number under this run's timestamp
    # would fabricate a data point. Left in, a multi-run outage would append
    # the same value repeatedly until the rolling baseline flattened to zero
    # variance, and the first real reading after recovery would then look like
    # an infinite-sigma anomaly caused purely by the outage.
    row = history.headline_row(snapshot, stale=snapshot["stale_sections"])
    rows = prior_rows
    snapshot["anomalies"] = (
        anomaly.detect(rows, row)
        + crosscheck.divergence_findings(snapshot["crosscheck"]))
    history.append(row)
    snapshot["history"] = (rows + [row])[-1440:]  # last ~30 days for charts

    # Cross-metric correlation, computed over the history including the row
    # just recorded. Isolated like everything else: a failure here must not
    # cost the run its report.
    try:
        snapshot["correlations"] = correlate.correlations(snapshot["history"])
        if verbose:
            c = snapshot["correlations"]
            print(f"  [ok] correlations ({c['significant_count']} of "
                  f"{c['pairs_tested']} pairs survive FDR)")
    except Exception as e:  # noqa: BLE001 — analysis is a nice-to-have
        snapshot["errors"]["correlations"] = repr(e)

    persist = {k: v for k, v in snapshot.items() if k != "history"}
    _write_json(LATEST_PATH, persist)

    return snapshot
