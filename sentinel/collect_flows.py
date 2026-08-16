"""Exchange and large-holder balances, and the direction SOL is moving.

The bounty's RPC list names `getBalance` and `getSignaturesForAddress`, which
are odd methods to want for an ecosystem report until you notice what they are
for: watching known large accounts. Exchange balances are the standard read on
supply pressure, since SOL moving onto an exchange can be sold and SOL leaving
it usually cannot.

Two things make this more than a list of numbers.

**Every label is verified against the chain before it is published.** Account
attribution comes from public sources and goes stale: addresses get retired,
and a label that was right last year can point at an empty account today. Of
ten addresses initially considered here, six turned out to hold essentially
nothing. Rather than trust the list, each account is checked at runtime and
dropped below a floor, so a stale label can never become a false claim.

**The interesting number is the change, not the level.** A balance on its own
says little; the same balance a day later says whether holders are
accumulating or distributing. The aggregate is recorded to history each run so
the net flow can be derived, which is the signal a reader actually wants.

Attribution is best-effort: Sentinel verifies that an account holds what it
says, never that a particular company controls it.
"""
from __future__ import annotations

from typing import Optional

from .collect_rpc import LAMPORTS, rpc
from .net import FetchError

# Below this an address is treated as retired or mislabelled and is not
# published, whatever its label claims.
MIN_BALANCE_SOL = 10_000

# Publicly-attributed accounts, each confirmed on-chain to hold a large
# balance at the time of writing and re-confirmed on every run.
WATCHED_ACCOUNTS = [
    ("Binance", "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM"),
    ("Binance (2)", "5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9"),
    ("Gate.io", "u6PJ8DtQuPFnfmwHbGFULQ4u4EgjDiyYKjVEsynXq2w"),
    ("Bybit", "AC5RDfQFmDS1deWZos921JfqscXdByf8BKHs5ACWjtW2"),
    ("Coinbase", "H8sMJSCQxfKiFTCfDR3DUMLPwcRbM61LGFJ8N4dK3WjS"),
    ("Coinbase (2)", "GJRs4FwHtemZ5ZE9x3FNvJ8TMwitKTh21yxdRPqn7npE"),
    ("Bitget", "A77HErqtfN1hLLpvZ9pCtu66FEtM8BveoaKbbMoZ4RiR"),
    ("Kraken", "BmFdpraQhkiDQE6SnfG5omcA1VwzqfXrwtNYBwWTymy6"),
]

SIGNATURE_SAMPLE = 100


def _recent_activity(address: str) -> dict:
    """Transactions per hour over the most recent signatures, which is a
    steadier read on how busy an account is than a raw count over an
    unspecified window."""
    try:
        sigs = rpc("getSignaturesForAddress",
                   [address, {"limit": SIGNATURE_SAMPLE}], timeout=20.0)
    except FetchError:
        return {}
    if not sigs:
        return {"recent_txs": 0}
    out: dict = {"recent_txs": len(sigs)}
    times = [s["blockTime"] for s in sigs if s.get("blockTime")]
    if len(times) >= 2:
        span = max(times) - min(times)
        if span > 0:
            out["window_hours"] = round(span / 3600, 2)
            out["tx_per_hour"] = round(len(times) / span * 3600, 1)
    failed = sum(1 for s in sigs if s.get("err"))
    out["failed_txs"] = failed
    return out


def flows(price_usd: Optional[float] = None) -> dict:
    accounts, dropped = [], []
    for label, address in WATCHED_ACCOUNTS:
        try:
            res = rpc("getBalance", [address], timeout=15.0)
        except FetchError:
            continue
        lamports = (res or {}).get("value")
        if lamports is None:
            continue
        sol = lamports / LAMPORTS
        if sol < MIN_BALANCE_SOL:
            # The label is stale or wrong; say so rather than publish it.
            dropped.append({"label": label, "address": address,
                            "balance_sol": round(sol, 4)})
            continue
        row = {"label": label, "address": address, "balance_sol": round(sol, 2)}
        if price_usd:
            row["balance_usd"] = round(sol * price_usd)
        row.update(_recent_activity(address))
        accounts.append(row)

    accounts.sort(key=lambda a: -a["balance_sol"])
    total = sum(a["balance_sol"] for a in accounts)
    out: dict = {
        "accounts": accounts,
        "verified": len(accounts),
        "dropped_failing_verification": dropped,
        "total_sol": round(total, 2),
    }
    if price_usd:
        out["total_usd"] = round(total * price_usd)
    return out


def net_flow(rows: list, current_total: Optional[float]) -> dict:
    """Change in aggregate tracked balance, which is the actual signal.

    A rise means SOL moving onto exchanges, which can be sold; a fall means it
    leaving, which usually cannot. Compares against the oldest history row
    inside each window rather than a fixed offset, so gaps in collection
    shorten the window instead of silently misdating the comparison.
    """
    if current_total is None:
        return {}
    import time as _time

    now = _time.time()
    out: dict = {}
    for label, secs in (("24h", 86_400), ("7d", 7 * 86_400)):
        window = [r for r in rows
                  if isinstance(r.get("exchange_sol"), (int, float))
                  and r.get("ts", 0) >= now - secs]
        if len(window) < 2:
            continue
        oldest = window[0]
        delta = current_total - oldest["exchange_sol"]
        out[f"change_{label}_sol"] = round(delta, 2)
        if oldest["exchange_sol"]:
            out[f"change_{label}_pct"] = round(
                delta / oldest["exchange_sol"] * 100, 3)
        out[f"observed_hours_{label}"] = round((now - oldest["ts"]) / 3600, 1)
    return out
