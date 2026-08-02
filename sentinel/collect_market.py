"""SOL market data — CoinGecko keyless primary, with a fallback chain
(Jupiter lite-api -> Binance -> Coinbase) so a single provider outage or
rate-limit never blanks the price section.
"""
from __future__ import annotations

import time

from .net import FetchError, fetch_json

CG = "https://api.coingecko.com/api/v3"
WSOL_MINT = "So11111111111111111111111111111111111111112"


def _coingecko() -> dict:
    rows = fetch_json(f"{CG}/coins/markets?vs_currency=usd&ids=solana", timeout=15)
    m = rows[0]
    out = {
        "source": "coingecko",
        "price_usd": m["current_price"],
        "change_24h_pct": m.get("price_change_percentage_24h"),
        "market_cap_usd": m.get("market_cap"),
        "market_cap_rank": m.get("market_cap_rank"),
        "volume_24h_usd": m.get("total_volume"),
        "high_24h": m.get("high_24h"),
        "low_24h": m.get("low_24h"),
        "ath_usd": m.get("ath"),
        "ath_change_pct": m.get("ath_change_percentage"),
        "circulating_supply": m.get("circulating_supply"),
    }
    try:
        # CoinGecko keyless throttles bursts hard (~5-10 req/min per IP,
        # and CI runner IPs are shared); space the second call well out.
        time.sleep(12)
        chart = fetch_json(f"{CG}/coins/solana/market_chart?vs_currency=usd&days=7",
                           timeout=15)
        # hourly [epoch_ms, price]; thin to every 2nd point to keep pages lean
        out["price_history_7d"] = [[int(t // 1000), round(p, 2)]
                                   for t, p in chart["prices"][::2]]
    except (FetchError, KeyError):
        pass
    return out


def _jupiter() -> dict:
    data = fetch_json(f"https://lite-api.jup.ag/price/v3?ids={WSOL_MINT}", timeout=15)
    tok = data[WSOL_MINT]
    return {"source": "jupiter", "price_usd": tok["usdPrice"],
            "change_24h_pct": tok.get("priceChange24h")}


def _binance() -> dict:
    t = fetch_json("https://api.binance.com/api/v3/ticker/24hr?symbol=SOLUSDT",
                   timeout=15)
    return {"source": "binance", "price_usd": float(t["lastPrice"]),
            "change_24h_pct": float(t["priceChangePercent"]),
            "high_24h": float(t["highPrice"]), "low_24h": float(t["lowPrice"])}


def _coinbase() -> dict:
    d = fetch_json("https://api.coinbase.com/v2/prices/SOL-USD/spot", timeout=15)
    return {"source": "coinbase", "price_usd": float(d["data"]["amount"])}


def market() -> dict:
    errors = []
    for fn in (_coingecko, _jupiter, _binance, _coinbase):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 — any failure falls through the chain
            errors.append(f"{fn.__name__}: {e!r}")
    raise FetchError(f"all market sources failed: {errors}")
