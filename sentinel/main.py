"""CLI entry point.

    python -m sentinel.main --once            one collection + render pass
    python -m sentinel.main --loop 30         re-run every 30 minutes, forever
    python -m sentinel.main --serve 8080      serve docs/ and refresh in background

Outputs (all regenerated every pass):
    docs/report.md     human-readable report
    docs/report.json   machine-readable report (the dashboard's data feed)
    docs/history.json  trend series for the dashboard's sparklines
    data/latest.json   full latest snapshot (compact)
    data/history.jsonl append-only metric history

The interactive dashboard (docs/index.html) is the built React app in
dashboard/, which fetches report.json and history.json at runtime. Build it
with `npm run build` in dashboard/; this collector never overwrites it.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import os
import threading
import time

from . import render_md
from .collector import collect

DOCS = "docs"


def run_once(verbose: bool = True) -> dict:
    started = time.time()
    if verbose:
        print(f"[sentinel] collecting @ {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    snapshot = collect(verbose=verbose)

    os.makedirs(DOCS, exist_ok=True)
    with open(os.path.join(DOCS, "report.md"), "w", encoding="utf-8") as f:
        f.write(render_md.render(snapshot))
    machine = {k: v for k, v in snapshot.items() if k != "history"}
    with open(os.path.join(DOCS, "report.json"), "w", encoding="utf-8") as f:
        json.dump(machine, f, indent=1)
    # Split out of report.json so the machine-readable report stays a clean
    # point-in-time document while the dashboard still gets its trend lines.
    with open(os.path.join(DOCS, "history.json"), "w", encoding="utf-8") as f:
        json.dump(snapshot.get("history") or [], f, separators=(",", ":"))

    if verbose:
        n_anom = len(snapshot.get("anomalies") or [])
        n_err = len(snapshot.get("errors") or {})
        print(f"[sentinel] done in {time.time() - started:.1f}s | "
              f"anomalies: {n_anom} | source errors: {n_err} | "
              f"outputs: docs/report.md docs/report.json docs/history.json")
    return snapshot


def main() -> None:
    ap = argparse.ArgumentParser(prog="sentinel",
                                 description="Keyless Solana ecosystem monitor")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--once", action="store_true",
                      help="collect and render one snapshot (default)")
    mode.add_argument("--loop", type=int, metavar="MINUTES",
                      help="run forever, refreshing every N minutes")
    mode.add_argument("--serve", type=int, metavar="PORT",
                      help="serve docs/ on PORT with background refresh")
    ap.add_argument("--interval", type=int, default=30, metavar="MINUTES",
                    help="refresh interval for --serve (default 30)")
    args = ap.parse_args()

    if args.loop:
        while True:
            try:
                run_once()
            except Exception as e:  # noqa: BLE001 — the loop must survive anything
                print(f"[sentinel] run failed: {e!r}")
            time.sleep(args.loop * 60)
    elif args.serve:
        run_once()

        def refresher():
            while True:
                time.sleep(args.interval * 60)
                try:
                    run_once()
                except Exception as e:  # noqa: BLE001
                    print(f"[sentinel] refresh failed: {e!r}")

        threading.Thread(target=refresher, daemon=True).start()
        handler = functools.partial(http.server.SimpleHTTPRequestHandler,
                                    directory=DOCS)
        print(f"[sentinel] dashboard on http://localhost:{args.serve} "
              f"(refresh every {args.interval} min)")
        http.server.ThreadingHTTPServer(("", args.serve), handler).serve_forever()
    else:
        run_once()


if __name__ == "__main__":
    main()
