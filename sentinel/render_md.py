"""Human-readable Markdown report."""
from __future__ import annotations

from . import fmt

SEV_ICON = {"critical": "🔴", "warning": "🟠", "info": "🔵"}


def render(s: dict) -> str:
    L: list[str] = []
    add = L.append

    add("# Solana Ecosystem Report")
    add("")
    add(f"*Generated {s.get('generated_utc', '-')} by "
        f"[sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - "
        f"auto-updating, keyless, Python-stdlib-only.*")
    add("")

    # ---- Alerts ----------------------------------------------------------
    anomalies = s.get("anomalies") or []
    add("## Alerts")
    add("")
    if anomalies:
        for a in anomalies:
            add(f"- {SEV_ICON.get(a['severity'], '•')} **{a['label']}** "
                f"({a['severity']}): {a['detail']}")
    else:
        add("- 🟢 No anomalies detected. All watched metrics are within their "
            "7-day baselines and absolute health thresholds.")
    add("")

    # ---- Network ---------------------------------------------------------
    n = s.get("network", {})
    ep = n.get("epoch", {})
    sup = n.get("supply", {})
    add("## Network performance")
    add("")
    add("| Metric | Value |")
    add("|---|---|")
    add(f"| RPC health | {n.get('health', '-')} |")
    add(f"| TPS (total, 10-min median) | {fmt.num(n.get('tps'))} |")
    add(f"| TPS (non-vote) | {fmt.num(n.get('true_tps'))} |")
    add(f"| Slot time | {fmt.num(n.get('slot_time_ms'))} ms |")
    add(f"| Slot | {fmt.num(n.get('slot'), 0) if n.get('slot') else '-'} |")
    add(f"| Block height | {fmt.num(n.get('block_height'), 0) if n.get('block_height') else '-'} |")
    add(f"| Epoch | {ep.get('epoch', '-')} ({fmt.pct(ep.get('pct'))} complete, "
        f"~{ep.get('eta_hours', '-')}h remaining) |")
    add(f"| Lifetime transactions | {fmt.num(n.get('tx_count_total'))} |")
    add(f"| Circulating supply | {fmt.num(sup.get('circulating_sol'))} SOL |")
    add(f"| Inflation (annual) | {fmt.pct(n.get('inflation_total_pct'))} |")
    act = s.get("activity", {})
    if act.get("median_tx_fee_lamports") is not None:
        price = (s.get("market") or {}).get("price_usd")
        med = act["median_tx_fee_lamports"]
        usd_note = f" (about ${med / 1e9 * price:.5f})" if price else ""
        add(f"| Median transaction fee | {fmt.exact(med)} lamports{usd_note} |")
        add(f"| Transaction fee p90 / p99 | "
            f"{fmt.exact(act.get('p90_tx_fee_lamports'))} / "
            f"{fmt.exact(act.get('p99_tx_fee_lamports'))} lamports |")
        add(f"| Paying base fee only | {fmt.pct(act.get('base_fee_only_pct'))} "
            f"of {fmt.exact(act.get('fee_sampled_txs'))} sampled transactions |")
    if n.get("prio_fee_nonzero_pct") is not None:
        add(f"| AMM write-lock congestion (150-slot window) | "
            f"{fmt.pct(n['prio_fee_nonzero_pct'])} of slots needed a priority "
            f"fee (max {fmt.num(n.get('max_prioritization_fee'), 1)} µlam/CU) |")
    add(f"| Node version (RPC) | {n.get('node_version', '-')} |")
    add("")

    # ---- Validators ------------------------------------------------------
    v = s.get("validators", {})
    add("## Validators & decentralization")
    add("")
    add("| Metric | Value |")
    add("|---|---|")
    add(f"| Active validators | {v.get('active', '-')} |")
    add(f"| Delinquent validators | {v.get('delinquent', '-')} |")
    add(f"| Delinquent stake | {fmt.pct(v.get('delinquent_stake_pct'))} |")
    add(f"| Total active stake | {fmt.num(v.get('total_active_stake_sol'))} SOL |")
    add(f"| Nakamoto coefficient | {v.get('nakamoto_coefficient', '-')} |")
    add(f"| Top-5 / Top-10 / Top-20 stake share | {fmt.pct(v.get('top5_stake_pct'))} / "
        f"{fmt.pct(v.get('top10_stake_pct'))} / {fmt.pct(v.get('top20_stake_pct'))} |")
    add(f"| Commission (stake-weighted, delegatable validators) | "
        f"{fmt.pct(v.get('avg_commission'))} |")
    add(f"| Stake on private (100% commission) validators | "
        f"{fmt.pct(v.get('private_stake_pct'))} |")
    add("")
    top = v.get("top_validators") or []
    if top:
        add("### Top validators by stake")
        add("")
        add("| # | Vote account | Stake (SOL) | Share | Commission |")
        add("|---|---|---|---|---|")
        for i, t in enumerate(top[:10], 1):
            add(f"| {i} | `{fmt.short_pubkey(t['vote'])}` | {fmt.num(t['stake_sol'])} "
                f"| {fmt.pct(t['share_pct'])} | {t.get('commission', '-')}% |")
        add("")

    # ---- Market ----------------------------------------------------------
    m = s.get("market", {})
    add("## Market")
    add("")
    add("| Metric | Value |")
    add("|---|---|")
    add(f"| SOL price | {fmt.usd(m.get('price_usd'))} "
        f"({fmt.pct(m.get('change_24h_pct'), signed=True)} 24h) |")
    mcap = fmt.usd(m.get("market_cap_usd"))
    if m.get("market_cap_estimated"):
        mcap += " (est.)"
    add(f"| Market cap | {mcap}"
        + (f" (rank #{m['market_cap_rank']})" if m.get("market_cap_rank") else "")
        + " |")
    add(f"| 24h volume | {fmt.usd(m.get('volume_24h_usd'))} |")
    if m.get("ath_usd"):
        add(f"| ATH | {fmt.usd(m.get('ath_usd'))} "
            f"({fmt.pct(m.get('ath_change_pct'), signed=True)} from ATH) |")
    add(f"| Price source | {m.get('source', '-')} |")
    add("")

    # ---- DeFi ------------------------------------------------------------
    d = s.get("defi", {})
    add("## DeFi & economic indicators")
    add("")
    add("| Metric | Value |")
    add("|---|---|")
    add(f"| TVL | {fmt.usd(d.get('tvl_usd'))} |")
    add(f"| Stablecoin supply | {fmt.usd(d.get('stablecoins_usd'))} |")
    add(f"| DEX volume (24h) | {fmt.usd(d.get('dex_volume_24h_usd'))} "
        f"({fmt.pct(d.get('dex_change_1d_pct'), signed=True)} 1d) |")
    add(f"| App fees (24h, all protocols) | {fmt.usd(d.get('app_fees_24h_usd'))} |")
    add(f"| Chain fees (24h) | {fmt.usd(d.get('chain_fees_24h_usd'))} |")
    add(f"| Jito MEV tips (24h) | {fmt.usd(d.get('jito_tips_24h_usd'))} |")
    add(f"| **REV - Real Economic Value (24h)** | **{fmt.usd(d.get('rev_24h_usd'))}** "
        f"(chain fees + MEV tips) |")
    add("")
    for title, key, cols in (
        ("Top stablecoins on Solana", "stablecoins_top",
         [("symbol", "Symbol"), ("on_solana_usd", "$ on Solana"),
          ("change_7d_pct", "7d Δ")]),
        ("Top DEXs by 24h volume", "dex_top",
         [("name", "DEX"), ("volume_24h_usd", "24h volume")]),
        ("Top apps by 24h fees", "top_fee_apps",
         [("name", "App"), ("fees_24h_usd", "24h fees")]),
    ):
        rows = d.get(key) or []
        if not rows:
            continue
        add(f"### {title}")
        add("")
        add("| " + " | ".join(c[1] for c in cols) + " |")
        add("|" + "---|" * len(cols))
        for r in rows:
            cells = []
            for k, _ in cols:
                val = r.get(k)
                if k.endswith("_usd"):
                    cells.append(fmt.usd(val))
                elif k.endswith("_pct"):
                    cells.append(fmt.pct(val, signed=True))
                else:
                    cells.append(str(val))
            add("| " + " | ".join(cells) + " |")
        add("")

    # ---- Activity & tokenized assets --------------------------------------
    a, t = s.get("activity", {}), s.get("tokenized", {})
    add("## Activity & tokenized assets")
    add("")
    add("| Metric | Value |")
    add("|---|---|")
    add(f"| Activity index: unique fee payers per block (24h sampled avg) | "
        f"{fmt.num(a.get('activity_index'))} |")
    cohort = a.get("active_cohort_est")
    if cohort:
        add(f"| Persistently-active cohort (capture-recapture est.) | "
            f"{fmt.num(cohort)} |")
    elif a.get("cohort_lower_bound"):
        add(f"| Persistently-active cohort (lower bound) | "
            f">={fmt.num(a['cohort_lower_bound'])} |")
    add(f"| Unique payers across sampled blocks | "
        f"{fmt.num(a.get('union_unique_payers'))} "
        f"({a.get('sampled_blocks', 0)} blocks over 24h) |")
    add(f"| xStocks tokenized-equity AUM | {fmt.usd(t.get('xstocks_aum_usd'))} |")
    add(f"| xStocks 24h DEX volume | {fmt.usd(t.get('xstocks_volume_24h_usd'))} |")
    add(f"| xStocks holders | {fmt.num(t.get('xstocks_holders'))} |")
    add(f"| Total RWA TVL on Solana | {fmt.usd(t.get('rwa_tvl_usd'))} |")
    add("")
    if t.get("xstocks_top"):
        add("Top tokenized equities: " + ", ".join(
            f"{x['ticker']} ({fmt.usd(x['usd'])})" for x in t["xstocks_top"][:5]))
        add("")

    # ---- Direct on-chain observations ---------------------------------------
    oc = s.get("onchain") or {}
    progs = oc.get("programs") or []
    if progs or oc.get("drift_secs") is not None:
        add("## Program activity and chain health")
        add("")
        if oc.get("drift_secs") is not None:
            add(f"Chain clock drift: **{oc['drift_secs']:+.1f} s** against wall "
                f"clock (slots run slightly longer than the nominal 400 ms, so "
                f"chain time falls behind real time).")
            add("")
        if progs:
            add(f"Throughput and failure rate for major programs, from the last "
                f"{fmt.exact(progs[0].get('sampled'))} signatures on each, timed "
                f"by slot span. The failure rate is a direct read on user "
                f"experience and is not published by volume-only dashboards.")
            add("")
            add("| Program | Transactions/min | Failed | Sample window |")
            add("|---|---|---|---|")
            for p in progs:
                if p.get("tx_per_min") is not None:
                    rate = fmt.exact(p["tx_per_min"])
                    if p.get("low_precision"):
                        rate += " (approx.)"
                elif p.get("tx_per_min_lower_bound") is not None:
                    rate = f">{fmt.exact(p['tx_per_min_lower_bound'])}"
                else:
                    rate = "-"
                window = (f"{fmt.num(p['window_secs'], 1)} s"
                          if p.get("window_secs") else "-")
                add(f"| {p['name']} | {rate} "
                    f"| {fmt.pct(p.get('failure_rate_pct'))} | {window} |")
            add("")
            if oc.get("median_program_failure_rate_pct") is not None:
                span = oc.get("failure_rate_span_pct") or []
                span_note = (f" (range {fmt.pct(span[0])} to {fmt.pct(span[1])})"
                             if len(span) == 2 else "")
                add(f"Median failure rate across the sampled programs: "
                    f"**{fmt.pct(oc['median_program_failure_rate_pct'])}**"
                    f"{span_note}. This is a consistent trend signal across "
                    f"these five programs, not a chain-wide rate.")
                add("")
        if oc.get("unwithdrawn_sol_top8") is not None:
            add(f"Unwithdrawn inflation rewards sitting in the top 8 vote "
                f"accounts: **{fmt.num(oc['unwithdrawn_sol_top8'], 2)} SOL**.")
            add("")

    # ---- Cross-metric correlation -------------------------------------------
    co = s.get("correlations") or {}
    if co.get("top"):
        add("## What moves together")
        add("")
        add(f"Relationships between metrics, rather than each metric on its "
            f"own. {co['significant_count']} of {co['pairs_tested']} tested "
            f"pairs survive, over {co.get('sample_size', 0)} observations.")
        add("")
        add(f"*Method: {co.get('method', '')}. Changes are correlated rather "
            f"than levels, because two series that both drift upward correlate "
            f"near +1 whatever the real relationship. Rank correlation is used "
            f"so a single outlier cannot manufacture a result.*")
        add("")
        add("| Relationship | rho | n | p |")
        add("|---|---|---|---|")
        for c in co["top"]:
            direction = "moves with" if c["rho"] > 0 else "moves against"
            add(f"| {c['a_label']} {direction} {c['b_label']} "
                f"| {c['rho']:+.3f} | {c['n']} | {c['p']:.4f} |")
        add("")

    # ---- Cross-source validation -------------------------------------------
    cc = s.get("crosscheck") or {}
    if cc.get("checks"):
        add("## Cross-source validation")
        add("")
        add(f"Quantities that two independent sources can both see, compared "
            f"against each other. {cc.get('agree', 0)} of {cc.get('total', 0)} "
            f"agree this run. Rows marked *indicative* are reported for "
            f"corroboration but never raise an alert, because their own "
            f"measurement noise is wider than any threshold worth acting on.")
        add("")
        add("| Quantity | Source A | Source B | Gap | Verdict |")
        add("|---|---|---|---|---|")
        for c in cc["checks"]:
            unit = f" {c['unit']}" if c.get("unit") else ""
            verdict = "agree" if c["agrees"] else "**diverge**"
            if c.get("ratio"):
                verdict += f" ({c['ratio']:.2f}x)"
            if not c.get("alerting", True):
                verdict += ", *indicative*"
            add(f"| {c['label']} | {c['a_source']}: {fmt.num(c['a_value'], 2)}{unit} "
                f"| {c['b_source']}: {fmt.num(c['b_value'], 2)}{unit} "
                f"| {fmt.pct(c.get('gap_pct'), signed=True)} | {verdict} |")
        add("")

    # ---- Development ------------------------------------------------------
    dv = s.get("dev", {})
    add("## Protocol development")
    add("")
    watch = dv.get("watchlist") or []
    if watch:
        add("**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):")
        add("")
        for w in watch:
            state = "merged" if w.get("merged_at") else "open"
            add(f"- [{w['title']}]({w['url']}) - *{state}*, updated "
                f"{(w.get('updated_at') or '')[:10]}")
        add("")
    for label, key in (("Open SIMD proposals", "simd_open"),
                       ("Recently merged SIMDs", "simd_recent_merged")):
        rows = dv.get(key) or []
        if rows:
            add(f"**{label}:**")
            add("")
            for r in rows[:6]:
                add(f"- [{r['title']}]({r['url']}) - updated {(r.get('updated_at') or '')[:10]}")
            add("")
    for label, key in (("Agave", "agave_releases"),
                       ("Firedancer", "firedancer_releases")):
        rels = dv.get(key) or []
        if rels:
            r = rels[0]
            add(f"**Latest {label} release:** [{r['tag']}]({r['url']}) "
                f"({(r.get('published_at') or '')[:10]})")
            add("")

    # ---- News --------------------------------------------------------------
    items = (s.get("news") or {}).get("items") or []
    if items:
        add("## Ecosystem news")
        add("")
        for it in items[:10]:
            add(f"- **[{it['title']}]({it['link']})** - {it['source']}, {it['date']}")
        add("")

    # ---- Footer ------------------------------------------------------------
    add("---")
    add("")
    add("**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + "
        "publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase "
        "fallbacks), GitHub REST, solana.com & Helius RSS.")
    stale = s.get("stale_sections") or []
    if stale:
        add("")
        add(f"⚠️ *Sections served from the previous snapshot due to source "
            f"errors this run: {', '.join(stale)}.*")
    errors = s.get("errors") or {}
    if errors:
        add("")
        add("<details><summary>Collection errors this run</summary>")
        add("")
        for k, e in errors.items():
            add(f"- `{k}`: `{e}`")
        add("")
        add("</details>")
    add("")
    return "\n".join(L)
