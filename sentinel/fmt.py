"""Number/date formatting shared by the Markdown and HTML renderers."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional


def usd(v: Optional[float], digits: int = 2) -> str:
    if v is None:
        return "-"
    a = abs(v)
    for cut, suffix in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if a >= cut:
            return f"${v / cut:,.{digits}f}{suffix}"
    return f"${v:,.2f}"


def num(v: Optional[float], digits: int = 1) -> str:
    if v is None:
        return "-"
    a = abs(v)
    for cut, suffix in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
        if a >= cut:
            return f"{v / cut:,.{digits}f}{suffix}"
    if isinstance(v, float) and v != int(v):
        return f"{v:,.{digits}f}"
    return f"{v:,.0f}"


def exact(v: Optional[float]) -> str:
    """Thousands-separated, never abbreviated. For quantities where the digits
    themselves matter (lamport fees, transaction counts), which `num` would
    round away into something like "6K"."""
    if v is None:
        return "-"
    return f"{round(v):,}"


def pct(v: Optional[float], signed: bool = False) -> str:
    if v is None:
        return "-"
    sign = "+" if signed and v > 0 else ""
    return f"{sign}{v:,.2f}%"


def iso_day(ts: Optional[float]) -> str:
    if not ts:
        return "-"
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def short_pubkey(k: Optional[str]) -> str:
    if not k:
        return "-"
    return f"{k[:4]}…{k[-4:]}"
