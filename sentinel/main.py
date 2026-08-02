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
import traceback

from . import render_md
from .collector import collect

DOCS = "docs"


def _write(path: str, text: str) -> None:
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def run_once(verbose: bool = True) -> dict:
    started = time.time()
    if verbose:
        print(f"[sentinel] collecting @ {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    snapshot = collect(verbose=verbose)

    # Every output is written to a temp file and renamed into place, so an
    # interrupted run can never leave a truncated report behind for the CI job
    # to commit.
    os.makedirs(DOCS, exist_ok=True)
    _write(os.path.join(DOCS, "report.md"), render_md.render(snapshot))
    machine = {k: v for k, v in snapshot.items() if k != "history"}
    _write(os.path.join(DOCS, "report.json"), json.dumps(machine, indent=1))
    # Split out of report.json so the machine-readable report stays a clean
    # point-in-time document while the dashboard still gets its trend lines.
    _write(os.path.join(DOCS, "history.json"),
           json.dumps(snapshot.get("history") or [], separators=(",", ":")))

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
        try:
            run_once()
        except Exception as e:  # noqa: BLE001 — serve whatever is on disk
            print(f"[sentinel] initial collection failed, serving the existing "
                  f"docs/ as-is: {e!r}")

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
        # Deliberately not swallowed. Per-source failures are already isolated
        # inside collect(), so anything reaching here is a real defect, and the
        # scheduled job must go red rather than quietly publish nothing.
        # Outputs are written atomically, so the last good report survives.
        try:
            run_once()
        except Exception:
            traceback.print_exc()
            print("\n[sentinel] collection failed; docs/ still holds the last "
                  "good report.")
            raise SystemExit(1)


if __name__ == "__main__":
    main()
