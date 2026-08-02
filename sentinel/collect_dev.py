"""Protocol development tracking via GitHub's unauthenticated REST API:
open + recently-merged SIMD proposals (including Alpenglow-related ones) and
the latest Agave / Firedancer validator client releases.

Budget: 4 requests per run. Unauthenticated limit is 60/hr per IP, so a
30-minute cadence uses ~8/hr — comfortable margin.
"""
from __future__ import annotations

import re

from .net import FetchError, fetch_json

GH = "https://api.github.com"
SIMD_REPO = "solana-foundation/solana-improvement-documents"

WATCH_KEYWORDS = ("alpenglow", "0525", "vote", "consensus", "fee")


def _pr_row(pr: dict) -> dict:
    m = re.search(r"simd-?(\d{3,4})", pr.get("title", ""), re.IGNORECASE)
    return {
        "number": pr.get("number"),
        "simd": m.group(1) if m else None,
        "title": pr.get("title"),
        "url": pr.get("html_url"),
        "author": (pr.get("user") or {}).get("login"),
        "updated_at": pr.get("updated_at"),
        "merged_at": pr.get("merged_at"),
        "draft": pr.get("draft", False),
    }


def dev() -> dict:
    out: dict = {}

    def is_simd(pr: dict) -> bool:
        return "simd" in (pr.get("title") or "").lower()  # repo attracts spam PRs

    open_prs = fetch_json(f"{GH}/repos/{SIMD_REPO}/pulls?state=open&per_page=30",
                          timeout=20, use_etag=True)
    out["simd_open"] = [_pr_row(p) for p in open_prs if is_simd(p)][:12]

    closed = fetch_json(f"{GH}/repos/{SIMD_REPO}/pulls?state=closed&sort=updated"
                        "&direction=desc&per_page=30", timeout=20, use_etag=True)
    out["simd_recent_merged"] = [_pr_row(p) for p in closed
                                 if p.get("merged_at") and is_simd(p)][:8]

    watch = []
    for row in out["simd_open"] + out["simd_recent_merged"]:
        title = (row.get("title") or "").lower()
        if any(k in title for k in WATCH_KEYWORDS):
            watch.append(row)
    out["watchlist"] = watch[:6]

    def latest_release(repo: str) -> list[dict]:
        rels = fetch_json(f"{GH}/repos/{repo}/releases?per_page=5",
                          timeout=20, use_etag=True)
        return [{"tag": r.get("tag_name"), "name": r.get("name"),
                 "prerelease": r.get("prerelease"),
                 "published_at": r.get("published_at"), "url": r.get("html_url")}
                for r in rels]

    try:
        out["agave_releases"] = latest_release("anza-xyz/agave")
    except FetchError:
        pass
    try:
        out["firedancer_releases"] = latest_release("firedancer-io/firedancer")
    except FetchError:
        pass
    return out
