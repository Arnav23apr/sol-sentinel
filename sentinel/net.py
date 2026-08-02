"""HTTP helpers — Python stdlib only (urllib), zero API keys.

Every outbound call in Sentinel goes through fetch_json/fetch_text so that
timeouts, retries, fallback endpoints, and conditional requests (ETag) are
handled uniformly.
"""
from __future__ import annotations

import gzip
import io
import json
import time
import urllib.error
import urllib.request
from typing import Any, Optional

USER_AGENT = "sol-sentinel/1.0 (+https://github.com/Arnav23apr/sol-sentinel)"

# ETag cache: url -> (etag, cached_body). Process-lifetime only, so it helps
# --loop and --serve, not the one-shot CI run. Note this saves bandwidth, not
# quota: GitHub counts a 304 against the unauthenticated 60/hr limit just like
# a 200, so the call budget in collect_dev.py assumes every request counts.
_ETAG_CACHE: dict[str, tuple[str, Any]] = {}


class FetchError(Exception):
    """All fallbacks for a logical source failed."""


def _request(url: str, *, method: str = "GET", body: Optional[bytes] = None,
             headers: Optional[dict] = None, timeout: float = 20.0) -> tuple[int, dict, bytes]:
    # No Accept-Encoding header: stdlib urllib doesn't auto-decompress, and
    # identity responses keep parsing simple; the decode path below still
    # handles servers that force gzip regardless.
    req_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, text/xml, application/xml, */*",
    }
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, data=body, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            if resp.headers.get("Content-Encoding") == "gzip":
                raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
            return resp.status, dict(resp.headers), raw
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read() or b""


def fetch_json(url: str, *, post: Optional[dict] = None, timeout: float = 20.0,
               retries: int = 2, backoff: float = 1.5, use_etag: bool = False) -> Any:
    """GET (or JSON-RPC POST) a URL and parse JSON, with retries."""
    body = json.dumps(post).encode() if post is not None else None
    headers = {"Content-Type": "application/json"} if post is not None else {}
    if use_etag and url in _ETAG_CACHE:
        headers["If-None-Match"] = _ETAG_CACHE[url][0]

    last_err: Optional[str] = None
    for attempt in range(retries + 1):
        try:
            status, resp_headers, raw = _request(
                url, method="POST" if post is not None else "GET",
                body=body, headers=headers, timeout=timeout)
            if status == 304 and use_etag and url in _ETAG_CACHE:
                return _ETAG_CACHE[url][1]
            if status == 429 or status >= 500:
                last_err = f"HTTP {status}"
                retry_after = resp_headers.get("Retry-After")
                # CoinGecko keyless 429s ask for ~41s — honor up to 45s.
                time.sleep(min(float(retry_after) if retry_after and retry_after.isdigit()
                               else backoff * (attempt + 1), 45))
                continue
            if status >= 400:
                raise FetchError(f"{url} -> HTTP {status}")
            data = json.loads(raw.decode("utf-8", errors="replace"))
            etag = resp_headers.get("ETag")
            if use_etag and etag:
                _ETAG_CACHE[url] = (etag, data)
            return data
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as e:
            last_err = repr(e)
            time.sleep(backoff * (attempt + 1))
    raise FetchError(f"{url} failed after {retries + 1} attempts: {last_err}")


def fetch_text(url: str, *, timeout: float = 20.0, retries: int = 1) -> str:
    last_err: Optional[str] = None
    for attempt in range(retries + 1):
        try:
            status, _, raw = _request(url, timeout=timeout)
            if status >= 400:
                last_err = f"HTTP {status}"
                time.sleep(1.0 * (attempt + 1))
                continue
            return raw.decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_err = repr(e)
            time.sleep(1.0 * (attempt + 1))
    raise FetchError(f"{url} failed: {last_err}")


def first_ok(candidates: list, describe: str) -> Any:
    """Try a list of zero-arg callables; return the first result that works."""
    errors = []
    for fn in candidates:
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 — deliberate: any failure moves to fallback
            errors.append(repr(e))
    raise FetchError(f"all sources failed for {describe}: {errors}")
