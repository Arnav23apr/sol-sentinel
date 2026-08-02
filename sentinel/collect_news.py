"""Ecosystem news via keyless RSS/Atom feeds, parsed with xml.etree.

Primary feeds (Solana-specific): solana.com news RSS, Helius blog Atom.
Supplementary (general crypto, keyword-filtered to Solana): Decrypt, The Block.
solana.com/data itself is client-rendered JS with no data in the HTML, so
Sentinel reads the same underlying sources directly instead.
"""
from __future__ import annotations

import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

from .net import fetch_text

ATOM_NS = "{http://www.w3.org/2005/Atom}"

FEEDS = [
    ("Solana.com", "https://solana.com/news/rss.xml", False),
    ("Helius", "https://www.helius.dev/blog/rss.xml", False),
    ("Decrypt", "https://decrypt.co/feed", True),       # keyword-filter
    ("The Block", "https://www.theblock.co/rss.xml", True),
]

MAX_ITEMS = 14
MAX_AGE_DAYS = 45


def _parse_date(text: str) -> float:
    text = (text or "").strip()
    for parser in (
        lambda t: parsedate_to_datetime(t),                      # RFC 822
        lambda t: datetime.fromisoformat(t.replace("Z", "+00:00")),  # ISO 8601
    ):
        try:
            dt = parser(text)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.timestamp()
        except (ValueError, TypeError):
            continue
    return 0.0


def _items_from_feed(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    items = []
    # RSS 2.0
    for item in root.iter("item"):
        items.append({
            "title": (item.findtext("title") or "").strip(),
            "link": (item.findtext("link") or "").strip(),
            "summary": (item.findtext("description") or "").strip()[:280],
            "ts": _parse_date(item.findtext("pubDate") or ""),
        })
    # Atom
    for entry in root.iter(f"{ATOM_NS}entry"):
        link_el = entry.find(f"{ATOM_NS}link")
        items.append({
            "title": (entry.findtext(f"{ATOM_NS}title") or "").strip(),
            "link": link_el.get("href", "") if link_el is not None else "",
            "summary": (entry.findtext(f"{ATOM_NS}summary") or "").strip()[:280],
            "ts": _parse_date(entry.findtext(f"{ATOM_NS}updated")
                              or entry.findtext(f"{ATOM_NS}published") or ""),
        })
    return items


def news() -> dict:
    collected, errors = [], {}
    cutoff = time.time() - MAX_AGE_DAYS * 86400
    for source, url, needs_filter in FEEDS:
        try:
            for it in _items_from_feed(fetch_text(url, timeout=15)):
                if not it["title"] or it["ts"] < cutoff:
                    continue
                if needs_filter and "solana" not in (
                        it["title"] + " " + it["summary"]).lower():
                    continue
                it["source"] = source
                collected.append(it)
        except Exception as e:  # noqa: BLE001 — a dead feed must not kill the run
            errors[source] = repr(e)

    collected.sort(key=lambda x: -x["ts"])
    seen, unique = set(), []
    for it in collected:
        key = it["title"].lower()[:80]
        if key in seen:
            continue
        seen.add(key)
        it["date"] = datetime.fromtimestamp(it["ts"], tz=timezone.utc).strftime("%Y-%m-%d")
        unique.append(it)
    return {"items": unique[:MAX_ITEMS], "feed_errors": errors or None}
