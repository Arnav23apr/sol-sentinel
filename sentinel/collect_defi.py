"""DeFi & economic indicators from DeFiLlama's open (keyless) APIs:
TVL, stablecoin supply, DEX volume, fees, and REV (Real Economic Value =
chain base fees + priority fees + Jito MEV tips, per DeFiLlama's chain entry
plus the Jito MEV Tips protocol entry).
"""
from __future__ import annotations

import time
from .net import FetchError, fetch_json

LLAMA = "https://api.llama.fi"
STABLES = "https://stablecoins.llama.fi"

TVL_HISTORY_DAYS = 365
CHART_DAYS = 90


def _trim(chart: list, days: int, drop_partial_last: bool = False) -> list:
    cutoff = time.time() - days * 86400
    rows = [[int(d), round(v, 2)] for d, v in chart if d >= cutoff]
    # Daily-sum charts (DEX volume, fees) report today as a partial day that
    # always looks like a crash — drop it. Level charts (TVL) keep it.
    if drop_partial_last and rows:
        rows = rows[:-1]
    return rows


def tvl() -> dict:
    out: dict = {}
    chains = fetch_json(f"{LLAMA}/v2/chains", timeout=20)
    sol = next(c for c in chains if c.get("name") == "Solana")
    out["tvl_usd"] = round(sol["tvl"], 0)

    hist = fetch_json(f"{LLAMA}/v2/historicalChainTvl/Solana", timeout=20)
    out["tvl_history"] = _trim([[p["date"], p["tvl"]] for p in hist], TVL_HISTORY_DAYS)

    rows = fetch_json(f"{STABLES}/stablecoinchains", timeout=20)
    srow = next(r for r in rows if r.get("name") == "Solana")
    pegged = srow.get("totalCirculatingUSD", {})
    out["stablecoins_usd"] = round(sum(v for v in pegged.values()
                                       if isinstance(v, (int, float))), 0)
    return out


def stablecoin_breakdown() -> list[dict]:
    data = fetch_json(f"{STABLES}/stablecoins?includePrices=true", timeout=30)
    out = []
    for asset in data.get("peggedAssets", []):
        chain = asset.get("chainCirculating", {}).get("Solana")
        if not chain:
            continue
        cur = (chain.get("current") or {}).get("peggedUSD")
        prev_week = (chain.get("circulatingPrevWeek") or {}).get("peggedUSD")
        if not cur or cur < 10_000_000:
            continue
        price = asset.get("price") or 1.0
        out.append({
            "symbol": asset.get("symbol"),
            "name": asset.get("name"),
            "on_solana_usd": round(cur * price, 0),
            "change_7d_pct": round((cur - prev_week) / prev_week * 100, 2)
            if prev_week else None,
        })
    out.sort(key=lambda x: -x["on_solana_usd"])
    return out[:8]


def dex() -> dict:
    d = fetch_json(f"{LLAMA}/overview/dexs/solana?excludeTotalDataChartBreakdown=true",
                   timeout=25)
    protos = sorted((p for p in d.get("protocols", []) if p.get("total24h")),
                    key=lambda p: -p["total24h"])
    return {
        "dex_volume_24h_usd": round(d.get("total24h") or 0, 0),
        "dex_volume_7d_usd": round(d.get("total7d") or 0, 0),
        "dex_change_1d_pct": d.get("change_1d"),
        "dex_history": _trim(d.get("totalDataChart") or [], CHART_DAYS,
                             drop_partial_last=True),
        "dex_top": [{"name": p.get("displayName") or p.get("name"),
                     "volume_24h_usd": round(p["total24h"], 0)} for p in protos[:8]],
    }


def fees_and_rev() -> dict:
    out: dict = {}
    f = fetch_json(f"{LLAMA}/overview/fees/solana?dataType=dailyFees"
                   "&excludeTotalDataChartBreakdown=true", timeout=25)
    out["app_fees_24h_usd"] = round(f.get("total24h") or 0, 0)

    chain_fees = jito_tips = None
    top = []
    for p in f.get("protocols", []):
        if p.get("protocolType") == "chain":
            chain_fees = p.get("total24h")
        elif p.get("name") == "Jito MEV Tips":
            jito_tips = p.get("total24h")
        if p.get("total24h") and p.get("protocolType") != "chain":
            top.append({"name": p.get("displayName") or p.get("name"),
                        "fees_24h_usd": round(p["total24h"], 0)})
    top.sort(key=lambda x: -x["fees_24h_usd"])
    out["top_fee_apps"] = top[:8]
    out["chain_fees_24h_usd"] = round(chain_fees, 0) if chain_fees else None
    out["jito_tips_24h_usd"] = round(jito_tips, 0) if jito_tips else None
    if chain_fees is not None:
        out["rev_24h_usd"] = round(chain_fees + (jito_tips or 0), 0)
    out["fees_24h_usd"] = out["app_fees_24h_usd"]

    # Historical REV series = chain fees history + Jito tips history.
    try:
        chain_hist = fetch_json(f"{LLAMA}/summary/fees/solana?dataType=dailyFees",
                                timeout=25).get("totalDataChart") or []
        jito_hist = fetch_json(f"{LLAMA}/summary/fees/jito-mev-tips?dataType=dailyFees",
                               timeout=25).get("totalDataChart") or []
        jito_by_day = {int(d): v for d, v in jito_hist}
        rev = [[int(d), round(v + jito_by_day.get(int(d), 0), 2)]
               for d, v in chain_hist]
        out["rev_history"] = _trim(rev, CHART_DAYS, drop_partial_last=True)
    except (FetchError, KeyError, TypeError):
        pass
    return out


def defi() -> dict:
    out: dict = {}
    for part in (tvl, dex, fees_and_rev):
        out.update(part())
    try:
        out["stablecoins_top"] = stablecoin_breakdown()
    except Exception:  # noqa: BLE001 — breakdown is a nice-to-have
        pass
    return out
