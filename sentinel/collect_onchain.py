"""Direct on-chain observations that no third-party feed publishes.

Three RPC methods the rest of the collector does not use, each answering a
question the aggregators cannot:

* **getSignaturesForAddress** gives the most recent signatures touching an
  address. Because each entry carries a `blockTime` and an `err`, one call per
  program yields both how fast that program is being used and what share of
  those attempts *failed*. The failure rate is the interesting one: it is a
  direct read on user experience, it moves sharply during congestion and bot
  wars, and no dashboard that only reports volume will show it.
* **getBlockTime** gives the chain's own timestamp for a slot. Compared with
  wall clock it measures how far Solana's clock has drifted, which happens
  because slots run slightly longer than the nominal 400 ms.
* **getBalance** reads an account's lamports. Applied to validator vote
  accounts it tracks inflation rewards that have accrued but not yet been
  withdrawn.

Every address here is either a well-known published program ID or comes from
`getVoteAccounts` on the chain itself, so nothing is hardcoded on trust.
"""
from __future__ import annotations

import time
from typing import Optional

from .collect_rpc import LAMPORTS, rpc
from .net import FetchError

SIGNATURE_LIMIT = 1000

# Published program IDs. These are stable, widely documented, and verifiable
# against any explorer.
PROGRAMS = [
    ("Jupiter v6", "JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4"),
    ("Raydium AMM v4", "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"),
    ("Orca Whirlpools", "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc"),
    ("Pump.fun", "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"),
    ("SPL Token", "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),
]

# Fewer whole slots than this and the rate is real but coarse: one slot either
# way moves it a lot, and the hottest programs always land here because the
# 1,000-signature cap closes the window before the program slows down.
MIN_RESOLVABLE_SLOTS = 3


def _program_stats(name: str, address: str, slot_secs: float) -> Optional[dict]:
    sigs = rpc("getSignaturesForAddress",
               [address, {"limit": SIGNATURE_LIMIT}], timeout=30.0)
    if not sigs:
        return None
    failed = sum(1 for s in sigs if s.get("err"))
    out = {
        "name": name,
        "address": address,
        "sampled": len(sigs),
        "failure_rate_pct": round(failed / len(sigs) * 100, 1),
    }
    # Timed by slot span, not blockTime. blockTime has one-second granularity
    # and the busiest programs fit all 1,000 signatures inside a single second,
    # which would turn the rate into 1000/1s and print an invented 60,000/min.
    # Slots are monotonic and fine-grained, so the span stays resolvable
    # however hot the program is.
    slots = sorted(s["slot"] for s in sigs if isinstance(s.get("slot"), int))
    if len(slots) < 2:
        return out
    oldest, newest = slots[0], slots[-1]
    slot_span = newest - oldest
    if slot_span <= 0:
        # Everything landed in one slot: the request cap, not the program,
        # decided the window, so the rate is only bounded below.
        out["window_slots"] = 1
        out["window_secs"] = round(slot_secs, 1)
        out["tx_per_min_lower_bound"] = round(len(sigs) / slot_secs * 60)
        return out

    # The oldest slot is almost certainly truncated: the response is capped at
    # SIGNATURE_LIMIT, so it holds only the tail of whatever that slot
    # contained. Counting its signatures while charging its full duration
    # biases the rate down, so drop it and measure across whole slots only.
    counted = sum(1 for s in slots if s > oldest)
    span = slot_span * slot_secs
    out["window_slots"] = slot_span
    out["window_secs"] = round(span, 1)
    out["tx_per_min"] = round(counted / span * 60)
    out["counted"] = counted
    if slot_span < MIN_RESOLVABLE_SLOTS:
        # One or two whole slots is a real measurement but a coarse one, and
        # saturated programs land here, so say so rather than imply precision.
        out["low_precision"] = True
    return out


def program_activity(slot_secs: float = 0.4) -> dict:
    """Per-program throughput and failure rate. One RPC call per program."""
    rows, errors = [], {}
    for name, address in PROGRAMS:
        try:
            stats = _program_stats(name, address, slot_secs)
            if stats:
                rows.append(stats)
        except (FetchError, KeyError, TypeError, ZeroDivisionError) as e:
            errors[name] = repr(e)
    rows.sort(key=lambda r: -(r.get("tx_per_min")
                              or r.get("tx_per_min_lower_bound") or 0))
    out: dict = {"programs": rows}
    if rows:
        # The median across the sampled programs, not a chain-wide rate: these
        # five are not the whole chain, and weighting by sample size would be
        # meaningless when every program contributes the same 1,000 signatures.
        # As a consistently-computed series it is still a good trend signal.
        rates = sorted(r["failure_rate_pct"] for r in rows)
        out["median_program_failure_rate_pct"] = rates[len(rates) // 2]
        out["failure_rate_span_pct"] = [rates[0], rates[-1]]
    if errors:
        out["errors"] = errors
    return out


def chain_clock(slot_secs: float = 0.4) -> dict:
    """How far the chain's own clock has drifted from wall clock.

    Slots run slightly longer than the nominal 400 ms, so chain time falls
    progressively behind real time until a clock adjustment. A large or
    fast-growing drift is a genuine health signal, invisible in any metric
    derived from slot counts alone.

    The tip slot is fetched here rather than reused from the network section:
    that value is captured at the start of a run and this executes a minute or
    more later, so measuring against it would charge the collector's own
    runtime to the chain as drift.
    """
    tip = rpc("getSlot", timeout=15.0)
    if not isinstance(tip, int):
        return {}
    # Very recent slots may not have a block yet, so step back until one does.
    for back in (0, 25, 100, 300):
        try:
            chain_ts = rpc("getBlockTime", [tip - back], timeout=15.0)
        except FetchError:
            continue
        if not isinstance(chain_ts, (int, float)):
            continue
        # The reference slot is `back` slots old, so discount the time those
        # slots themselves took before attributing the rest to drift.
        drift = time.time() - chain_ts - back * slot_secs
        return {
            "reference_slot": tip - back,
            "chain_time": int(chain_ts),
            "drift_secs": round(drift, 1),
        }
    return {}


def vote_account_balances(top_validators: list) -> dict:
    """SOL sitting in the largest vote accounts: inflation rewards that have
    accrued but not been withdrawn. Addresses come from getVoteAccounts, so
    none of them are hardcoded."""
    rows = []
    for v in (top_validators or [])[:8]:
        pubkey = v.get("vote")
        if not pubkey:
            continue
        try:
            res = rpc("getBalance", [pubkey], timeout=15.0)
        except FetchError:
            continue
        lamports = (res or {}).get("value")
        if lamports is None:
            continue
        rows.append({
            "vote": pubkey,
            "stake_sol": v.get("stake_sol"),
            "balance_sol": round(lamports / LAMPORTS, 4),
        })
    out: dict = {"vote_accounts": rows}
    if rows:
        out["unwithdrawn_sol_top8"] = round(
            sum(r["balance_sol"] for r in rows), 4)
    return out


def onchain(slot_ms: Optional[float] = None,
            top_validators: Optional[list] = None) -> dict:
    """Assemble the direct-observation section. Each part is isolated so one
    slow or unavailable method cannot take the others down.

    `slot_ms` is the measured slot time from the network section; both the
    program rates and the drift calculation convert slots to seconds with it
    rather than assuming the nominal 400 ms.
    """
    slot_secs = (slot_ms / 1000.0) if slot_ms else 0.4
    out: dict = {"slot_secs_used": round(slot_secs, 4)}
    for key, fn in (("activity", lambda: program_activity(slot_secs)),
                    ("clock", lambda: chain_clock(slot_secs)),
                    ("balances",
                     lambda: vote_account_balances(top_validators or []))):
        try:
            out.update(fn())
        except Exception as e:  # noqa: BLE001 — isolate this observation only
            out.setdefault("errors", {})[key] = repr(e)
    return out
