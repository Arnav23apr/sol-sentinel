import { useEffect, useMemo, useState } from "react"
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  DitherGradient,
  Grid as ChartGrid,
  Legend,
  Line,
  LineChart,
  Tooltip,
  XAxis,
  YAxis,
} from "@/components/dither-kit"
import { LoadingSkeleton } from "@/components/motion"
import { Card, Grid, LinkList, Pill, Section, Table, Tile } from "@/components/shell"
import { day, int, num, pct, shortKey, thin, usd } from "@/format"
import type { HistoryRow, Report } from "@/types"

const REPO = "https://github.com/Arnav23apr/sol-sentinel"

/** Pull one metric out of the rolling history as a plain number[] for a
 * sparkline, newest last. */
function sparkOf(history: HistoryRow[], key: string, max = 64): number[] {
  const vals = history
    .map((r) => r[key])
    .filter((v): v is number => typeof v === "number")
  return thin(vals, max)
}

/** Charts take rows of objects; the collector emits [timestamp, value] pairs. */
function toRows(pairs: [number, number][] | undefined, key: string) {
  return (pairs ?? []).map(([t, v]) => ({ t, [key]: v }))
}

export default function App() {
  const [report, setReport] = useState<Report | null>(null)
  const [history, setHistory] = useState<HistoryRow[]>([])
  const [error, setError] = useState<string | null>(null)
  const [theme, setTheme] = useState<"dark" | "light">(
    () => (localStorage.getItem("sentinel-theme") as "dark" | "light") ?? "dark"
  )

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme)
    localStorage.setItem("sentinel-theme", theme)
  }, [theme])

  useEffect(() => {
    let cancelled = false
    const load = async () => {
      try {
        const [r, h] = await Promise.all([
          fetch(`./report.json?t=${Date.now()}`).then((x) => x.json()),
          fetch(`./history.json?t=${Date.now()}`)
            .then((x) => x.json())
            .catch(() => []),
        ])
        if (!cancelled) {
          setReport(r)
          setHistory(Array.isArray(h) ? h : [])
        }
      } catch (e) {
        if (!cancelled) setError(String(e))
      }
    }
    load()
    // The collector republishes every 30 minutes; poll so a tab left open
    // picks up the new snapshot without a manual reload.
    const timer = setInterval(load, 5 * 60 * 1000)
    return () => {
      cancelled = true
      clearInterval(timer)
    }
  }, [])

  const perfRows = useMemo(() => {
    const samples = [...(report?.network.perf_samples ?? [])].reverse()
    const base = Date.now() / 1000 - samples.length * 60
    return samples.map((s, i) => ({
      t: base + i * 60,
      tps: s.tps,
      true_tps: s.true_tps ?? 0,
    }))
  }, [report])

  const stakeRows = useMemo(
    () =>
      (report?.validators.stake_curve ?? []).map((share, i) => ({
        rank: i + 1,
        share,
      })),
    [report]
  )

  const commissionRows = useMemo(
    () =>
      Object.entries(report?.validators.commission_buckets ?? {}).map(
        ([bucket, count]) => ({ bucket, count })
      ),
    [report]
  )

  const priceRows = useMemo(
    () => toRows(report?.market.price_history_7d, "price"),
    [report]
  )
  const tvlRows = useMemo(() => toRows(report?.defi.tvl_history, "tvl"), [report])
  const dexRows = useMemo(
    () => toRows(report?.defi.dex_history, "volume"),
    [report]
  )
  const revRows = useMemo(() => toRows(report?.defi.rev_history, "rev"), [report])
  const xstockRows = useMemo(
    () => toRows(report?.tokenized.xstocks_history, "aum"),
    [report]
  )

  if (error) {
    return (
      <main className="mx-auto max-w-md p-10 text-[13px]">
        <h1 className="mb-2 font-semibold text-foreground">
          Could not load the snapshot
        </h1>
        <p className="text-muted-foreground">{error}</p>
        <p className="mt-3 text-muted-foreground">
          The dashboard reads <code>report.json</code> next to it. Run{" "}
          <code>python3 -m sentinel.main --once</code> to generate one.
        </p>
      </main>
    )
  }

  if (!report) return <LoadingSkeleton />

  const { network: n, validators: v, market: m, defi: d } = report
  const { activity: a, tokenized: tk, dev, news } = report
  const ep = n.epoch
  const anomalies = report.anomalies ?? []
  const priceUp = (m.change_24h_pct ?? 0) >= 0

  return (
    <div className="relative min-h-full">
      {/* Dithered wash behind the header, from the same engine as the charts. */}
      <div className="pointer-events-none absolute inset-x-0 top-0 z-0 h-64 opacity-[0.16]">
        <DitherGradient from="blue" direction="down" cell={3} />
      </div>

      <div className="relative z-10 mx-auto max-w-[1180px] px-4 pb-20">
        <header className="flex flex-wrap items-center gap-x-4 gap-y-2 py-6">
          <div className="flex items-baseline gap-2">
            <span className="text-[19px] text-sky-400">◎</span>
            <h1 className="font-semibold text-[17px] tracking-[0.12em]">
              SOL SENTINEL
            </h1>
          </div>
          <div className="flex-1 text-[11.5px] text-muted-foreground">
            <span className="mr-1.5 inline-block size-1.5 animate-pulse rounded-full bg-emerald-400 align-middle" />
            {report.generated_utc} · refreshes every 30 min
          </div>
          <div className="flex items-center gap-2">
            <a
              href="./report.md"
              className="rounded-md border border-border px-2.5 py-1 text-[11px] text-muted-foreground transition-colors hover:text-foreground"
            >
              .md
            </a>
            <a
              href="./report.json"
              className="rounded-md border border-border px-2.5 py-1 text-[11px] text-muted-foreground transition-colors hover:text-foreground"
            >
              .json
            </a>
            <button
              type="button"
              onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
              className="cursor-pointer rounded-md border border-border px-2.5 py-1 text-[11px] text-muted-foreground transition-colors hover:text-foreground"
            >
              {theme === "dark" ? "light" : "dark"}
            </button>
          </div>
        </header>

        <Section title="Alerts">
          {anomalies.length === 0 ? (
            <div className="flex items-start gap-3 rounded-lg border border-border border-l-2 border-l-emerald-400 bg-card px-4 py-3">
              <Pill tone="ok">OK</Pill>
              <p className="text-[13px] text-muted-foreground">
                <span className="text-foreground">All clear.</span> Every watched
                metric is inside its 7-day baseline and health thresholds.
              </p>
            </div>
          ) : (
            <div className="flex flex-col gap-2">
              {anomalies.map((x) => (
                <div
                  key={`${x.metric}-${x.kind}`}
                  className={`flex items-start gap-3 rounded-lg border border-border border-l-2 bg-card px-4 py-3 ${
                    x.severity === "critical"
                      ? "border-l-rose-400"
                      : "border-l-amber-400"
                  }`}
                >
                  <Pill tone={x.severity === "critical" ? "critical" : "warning"}>
                    {x.severity.toUpperCase()}
                  </Pill>
                  <p className="text-[13px] text-muted-foreground">
                    <span className="text-foreground">{x.label}</span> {x.detail}
                  </p>
                </div>
              ))}
            </div>
          )}
        </Section>

        <Section title="Network performance" note="direct from JSON-RPC">
          <Grid>
            <Tile
              label="Transactions per second"
              value={num(n.tps)}
              sub="10-min median, includes votes"
              spark={sparkOf(history, "tps")}
            />
            <Tile
              label="Non-vote TPS"
              value={num(n.true_tps)}
              sub="user transactions only"
              spark={sparkOf(history, "true_tps")}
              sparkColor="orange"
            />
            <Tile
              label="Slot time"
              value={`${num(n.slot_time_ms)} ms`}
              sub="target 400 ms"
              spark={sparkOf(history, "slot_time_ms")}
              sparkColor="purple"
            />
            <Tile label="Block height" value={num(n.block_height, 2)} />
            <Tile label="Lifetime transactions" value={num(n.tx_count_total, 2)} />
            <Tile
              label="RPC health"
              value={n.health}
              sub={`node v${n.node_version ?? "?"}`}
            />
            {n.prio_fee_nonzero_pct != null && (
              <Tile
                label="AMM write-lock congestion"
                value={pct(n.prio_fee_nonzero_pct)}
                sub={`of 150 slots needed a priority fee · max ${num(
                  n.max_prioritization_fee
                )} µlam/CU`}
              />
            )}
            <Tile
              label="Circulating supply"
              value={`${num(n.supply.circulating_sol)} SOL`}
              sub={`inflation ${pct(n.inflation_total_pct)}/yr`}
            />
          </Grid>

          <div className="mt-2.5 grid gap-2.5 lg:grid-cols-[2fr_1fr]">
            <Card title="Throughput" note="last 60 minutes">
              <div className="h-[210px]">
                <LineChart
                  data={perfRows}
                  config={{
                    tps: { label: "total TPS", color: "blue" },
                    true_tps: { label: "non-vote TPS", color: "orange" },
                  }}
                  bloom="low"
                >
                  <ChartGrid />
                  <XAxis
                    dataKey="t"
                    tickFormatter={(x) =>
                      new Date((x as number) * 1000).toLocaleTimeString([], {
                        hour: "2-digit",
                        minute: "2-digit",
                      })
                    }
                    maxTicks={5}
                  />
                  <YAxis tickFormatter={(x) => num(x, 0)} />
                  <Line dataKey="tps" isClickable />
                  <Line dataKey="true_tps" isClickable />
                  <Legend isClickable />
                  <Tooltip valueFormatter={(x) => `${num(x)} tps`} />
                </LineChart>
              </div>
            </Card>
            <Card title={`Epoch ${ep.epoch}`} note={`${pct(ep.pct)} complete`}>
              <div className="flex h-[210px] flex-col justify-center gap-3">
                <div className="h-3 overflow-hidden rounded-full border border-border bg-muted">
                  <div
                    className="h-full bg-sky-500 transition-[width] duration-700"
                    style={{ width: `${ep.pct}%` }}
                  />
                </div>
                <dl className="flex flex-col gap-1.5 text-[12px]">
                  {[
                    ["Time remaining", `~${ep.eta_hours} h`],
                    [
                      "Slot in epoch",
                      `${int(ep.slot_index)} / ${int(ep.slots_in_epoch)}`,
                    ],
                    ["Absolute slot", int(n.slot)],
                  ].map(([k, val]) => (
                    <div key={k} className="flex justify-between gap-3">
                      <dt className="text-muted-foreground">{k}</dt>
                      <dd className="text-foreground tabular-nums">{val}</dd>
                    </div>
                  ))}
                </dl>
              </div>
            </Card>
          </div>
        </Section>

        <Section title="Validators & decentralization">
          <Grid>
            <Tile
              label="Active validators"
              value={int(v.active)}
              spark={sparkOf(history, "validators_active")}
              sparkColor="green"
            />
            <Tile
              label="Delinquent"
              value={int(v.delinquent)}
              sub={`${pct(v.delinquent_stake_pct)} of stake`}
              spark={sparkOf(history, "validators_delinquent")}
              sparkColor="red"
            />
            <Tile
              label="Nakamoto coefficient"
              value={int(v.nakamoto_coefficient)}
              sub="validators to reach 1/3 of stake"
              spark={sparkOf(history, "nakamoto")}
              sparkColor="purple"
            />
            <Tile
              label="Total active stake"
              value={`${num(v.total_active_stake_sol)} SOL`}
              sub={`stake-weighted commission ${pct(v.avg_commission)}`}
            />
            <Tile
              label="Top-5 stake share"
              value={pct(v.top5_stake_pct)}
              sub={`top-20: ${pct(v.top20_stake_pct)}`}
            />
            <Tile
              label="Private validator stake"
              value={pct(v.private_stake_pct)}
              sub="on 100%-commission (self-stake) validators"
            />
          </Grid>

          <div className="mt-2.5 grid gap-2.5 lg:grid-cols-[2fr_1fr]">
            <Card title="Stake concentration" note="cumulative share by rank">
              <div className="h-[220px]">
                <AreaChart
                  data={stakeRows}
                  config={{
                    share: { label: "cumulative stake", color: "purple" },
                  }}
                  bloom="low"
                >
                  <ChartGrid />
                  <XAxis
                    dataKey="rank"
                    tickFormatter={(x) => `#${x}`}
                    maxTicks={6}
                  />
                  <YAxis tickFormatter={(x) => `${x}%`} />
                  <Area dataKey="share" variant="gradient" />
                  <Tooltip
                    labelKey="rank"
                    valueFormatter={(x) => `${x.toFixed(1)}%`}
                  />
                </AreaChart>
              </div>
            </Card>
            <Card title="Commission distribution" note="validator count">
              <div className="h-[220px]">
                <BarChart
                  data={commissionRows}
                  config={{ count: { label: "validators", color: "green" } }}
                >
                  <ChartGrid />
                  <XAxis dataKey="bucket" />
                  <YAxis tickFormatter={(x) => num(x, 0)} />
                  <Bar dataKey="count" variant="gradient" />
                  <Tooltip
                    labelKey="bucket"
                    valueFormatter={(x) => `${int(x)} validators`}
                  />
                </BarChart>
              </div>
            </Card>
          </div>

          <Card title="Top validators by stake" className="mt-2.5">
            <Table
              head={["#", "Vote account", "Stake (SOL)", "Share", "Comm."]}
              align="llrrr"
              rows={v.top_validators.slice(0, 12).map((x, i) => [
                <span className="text-muted-foreground">{i + 1}</span>,
                <code className="text-[12px]">{shortKey(x.vote)}</code>,
                num(x.stake_sol),
                pct(x.share_pct),
                `${x.commission ?? "-"}%`,
              ])}
            />
          </Card>
        </Section>

        <Section title="Market">
          <Grid>
            <Tile
              label="SOL price"
              value={usd(m.price_usd)}
              delta={
                m.change_24h_pct != null
                  ? `${pct(m.change_24h_pct, true)} 24h`
                  : undefined
              }
              deltaUp={priceUp}
              spark={sparkOf(history, "sol_price")}
              sparkColor={priceUp ? "green" : "red"}
            />
            <Tile
              label="Market cap"
              value={`${usd(m.market_cap_usd)}${
                m.market_cap_estimated ? " (est.)" : ""
              }`}
              sub={m.market_cap_rank ? `rank #${m.market_cap_rank}` : undefined}
            />
            <Tile label="24h volume" value={usd(m.volume_24h_usd)} />
            <Tile
              label="From ATH"
              value={pct(m.ath_change_pct, true)}
              sub={m.ath_usd ? `ATH ${usd(m.ath_usd)}` : undefined}
            />
            <Tile
              label="Price source"
              value={m.source}
              sub="first healthy of 4 keyless feeds"
            />
          </Grid>
          <Card title="SOL price" note="7 days" className="mt-2.5">
            <div className="h-[230px]">
              <AreaChart
                data={priceRows}
                config={{
                  price: { label: "SOL", color: priceUp ? "green" : "red" },
                }}
                bloom="low"
              >
                <ChartGrid />
                <XAxis
                  dataKey="t"
                  tickFormatter={(x) => day(x as number)}
                  maxTicks={7}
                />
                <YAxis tickFormatter={(x) => usd(x, 0)} />
                <Area dataKey="price" variant="gradient" />
                <Tooltip labelKey="t" valueFormatter={(x) => usd(x)} />
              </AreaChart>
            </div>
          </Card>
        </Section>

        <Section title="DeFi & economics">
          <Grid>
            <Tile
              label="Total value locked"
              value={usd(d.tvl_usd)}
              spark={sparkOf(history, "tvl")}
            />
            <Tile
              label="Stablecoin supply"
              value={usd(d.stablecoins_usd)}
              spark={sparkOf(history, "stables")}
              sparkColor="green"
            />
            <Tile
              label="DEX volume 24h"
              value={usd(d.dex_volume_24h_usd)}
              delta={
                d.dex_change_1d_pct != null
                  ? pct(d.dex_change_1d_pct, true)
                  : undefined
              }
              deltaUp={(d.dex_change_1d_pct ?? 0) >= 0}
              spark={sparkOf(history, "dex_vol_24h")}
              sparkColor="orange"
            />
            <Tile
              label="REV 24h"
              value={usd(d.rev_24h_usd)}
              sub={`chain fees ${usd(d.chain_fees_24h_usd)} + MEV tips ${usd(
                d.jito_tips_24h_usd
              )}`}
              spark={sparkOf(history, "rev_24h")}
              sparkColor="green"
            />
            <Tile
              label="App fees 24h"
              value={usd(d.app_fees_24h_usd)}
              sub="every protocol on Solana"
            />
          </Grid>

          <div className="mt-2.5 grid gap-2.5 lg:grid-cols-2">
            <Card title="Total value locked" note="1 year">
              <div className="h-[210px]">
                <AreaChart
                  data={tvlRows}
                  config={{ tvl: { label: "TVL", color: "blue" } }}
                  bloom="low"
                >
                  <ChartGrid />
                  <XAxis
                    dataKey="t"
                    tickFormatter={(x) => day(x as number)}
                    maxTicks={5}
                  />
                  <YAxis tickFormatter={(x) => usd(x, 1)} />
                  <Area dataKey="tvl" variant="gradient" />
                  <Tooltip labelKey="t" valueFormatter={(x) => usd(x)} />
                </AreaChart>
              </div>
            </Card>
            <Card title="Daily DEX volume" note="90 days">
              <div className="h-[210px]">
                <BarChart
                  data={dexRows}
                  config={{ volume: { label: "DEX volume", color: "orange" } }}
                >
                  <ChartGrid />
                  <XAxis
                    dataKey="t"
                    tickFormatter={(x) => day(x as number)}
                    maxTicks={4}
                  />
                  <YAxis tickFormatter={(x) => usd(x, 1)} />
                  <Bar dataKey="volume" variant="gradient" />
                  <Tooltip labelKey="t" valueFormatter={(x) => usd(x)} />
                </BarChart>
              </div>
            </Card>
          </div>

          <div className="mt-2.5 grid gap-2.5 lg:grid-cols-2">
            <Card title="Daily REV" note="chain fees + MEV tips, 90 days">
              <div className="h-[210px]">
                <BarChart
                  data={revRows}
                  config={{ rev: { label: "REV", color: "green" } }}
                >
                  <ChartGrid />
                  <XAxis
                    dataKey="t"
                    tickFormatter={(x) => day(x as number)}
                    maxTicks={4}
                  />
                  <YAxis tickFormatter={(x) => usd(x, 0)} />
                  <Bar dataKey="rev" variant="gradient" />
                  <Tooltip labelKey="t" valueFormatter={(x) => usd(x)} />
                </BarChart>
              </div>
            </Card>
            <Card title="Top stablecoins on Solana">
              <Table
                head={["Stablecoin", "On Solana", "7d"]}
                align="lrr"
                rows={(d.stablecoins_top ?? []).map((s) => [
                  s.symbol,
                  usd(s.on_solana_usd),
                  <span
                    className={
                      (s.change_7d_pct ?? 0) >= 0
                        ? "text-emerald-400"
                        : "text-rose-400"
                    }
                  >
                    {pct(s.change_7d_pct, true)}
                  </span>,
                ])}
              />
            </Card>
          </div>

          <div className="mt-2.5 grid gap-2.5 lg:grid-cols-2">
            <Card title="Top DEXs" note="24h volume">
              <Table
                head={["DEX", "24h volume"]}
                align="lr"
                rows={d.dex_top.map((x) => [x.name, usd(x.volume_24h_usd)])}
              />
            </Card>
            <Card title="Top apps by fees" note="24h">
              <Table
                head={["App", "24h fees"]}
                align="lr"
                rows={d.top_fee_apps.map((x) => [x.name, usd(x.fees_24h_usd)])}
              />
            </Card>
          </div>
        </Section>

        <Section
          title="Activity & tokenized assets"
          note="activity measured on-chain by Sentinel"
        >
          <Grid>
            <Tile
              label="Activity index"
              value={num(a.activity_index)}
              sub={`unique fee payers per block · ${a.sampled_blocks} blocks sampled over 24h`}
              spark={sparkOf(history, "activity_idx")}
              sparkColor="pink"
            />
            <Tile
              label="Persistently-active cohort"
              value={
                a.active_cohort_est != null
                  ? num(a.active_cohort_est)
                  : a.cohort_lower_bound != null
                    ? `≥${num(a.cohort_lower_bound)}`
                    : "-"
              }
              sub="capture-recapture estimate"
            />
            <Tile
              label="xStocks AUM"
              value={usd(tk.xstocks_aum_usd)}
              sub="tokenized equities on Solana"
            />
            <Tile
              label="xStocks 24h volume"
              value={usd(tk.xstocks_volume_24h_usd)}
              sub={`${num(tk.xstocks_holders)} holders`}
            />
            <Tile
              label="RWA TVL"
              value={usd(tk.rwa_tvl_usd)}
              sub="all real-world-asset protocols"
            />
          </Grid>

          <div className="mt-2.5 grid gap-2.5 lg:grid-cols-[2fr_1fr]">
            <Card title="xStocks tokenized-equity AUM" note="6 months">
              <div className="h-[210px]">
                <AreaChart
                  data={xstockRows}
                  config={{ aum: { label: "xStocks AUM", color: "pink" } }}
                  bloom="low"
                >
                  <ChartGrid />
                  <XAxis
                    dataKey="t"
                    tickFormatter={(x) => day(x as number)}
                    maxTicks={5}
                  />
                  <YAxis tickFormatter={(x) => usd(x, 0)} />
                  <Area dataKey="aum" variant="gradient" />
                  <Tooltip labelKey="t" valueFormatter={(x) => usd(x)} />
                </AreaChart>
              </div>
            </Card>
            <Card title="Top tokenized equities">
              <Table
                head={["Ticker", "AUM"]}
                align="lr"
                rows={(tk.xstocks_top ?? []).map((x) => [x.ticker, usd(x.usd)])}
              />
            </Card>
          </div>

          <Card title="Top RWA protocols on Solana" className="mt-2.5">
            <Table
              head={["Protocol", "TVL on Solana"]}
              align="lr"
              rows={(tk.rwa_top ?? []).map((x) => [x.name, usd(x.usd)])}
            />
          </Card>
        </Section>

        <Section title="Protocol development">
          <div className="grid gap-2.5 lg:grid-cols-2">
            <Card title="Upgrade watchlist" note="consensus, fees, Alpenglow">
              <LinkList
                items={dev.watchlist.map((p) => ({
                  key: p.number,
                  title: p.title,
                  url: p.url,
                  badge: p.merged_at ? "merged" : "open",
                  tone: p.merged_at ? ("merged" as const) : ("open" as const),
                  when: (p.updated_at ?? "").slice(0, 10),
                }))}
              />
              <div className="mt-4 flex flex-wrap gap-2">
                {[
                  ...(dev.agave_releases ?? []).slice(0, 2),
                  ...(dev.firedancer_releases ?? []).slice(0, 2),
                ].map((r) => (
                  <a
                    key={r.url}
                    href={r.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex flex-col gap-0.5 rounded-md border border-border bg-muted px-3 py-2 transition-colors hover:border-sky-500/60"
                  >
                    <span className="text-[12px] text-foreground">{r.tag}</span>
                    <span className="text-[10.5px] text-muted-foreground">
                      {(r.published_at ?? "").slice(0, 10)}
                    </span>
                  </a>
                ))}
              </div>
            </Card>
            <Card title="SIMD proposals" note="open and recently merged">
              <LinkList
                items={[
                  ...dev.simd_open.slice(0, 6).map((p) => ({
                    key: `o${p.number}`,
                    title: p.title,
                    url: p.url,
                    badge: p.draft ? "draft" : "open",
                    tone: "open" as const,
                    when: (p.updated_at ?? "").slice(0, 10),
                  })),
                  ...dev.simd_recent_merged.slice(0, 5).map((p) => ({
                    key: `m${p.number}`,
                    title: p.title,
                    url: p.url,
                    badge: "merged",
                    tone: "merged" as const,
                    when: (p.merged_at ?? "").slice(0, 10),
                  })),
                ]}
              />
            </Card>
          </div>
        </Section>

        <Section title="Ecosystem news">
          <Card>
            <LinkList
              items={news.items.map((it) => ({
                key: it.link,
                title: it.title,
                url: it.link,
                badge: it.source,
                when: it.date,
              }))}
            />
          </Card>
        </Section>

        <footer className="mt-14 border-border border-t pt-5 text-[11.5px] text-muted-foreground leading-relaxed">
          {report.stale_sections.length > 0 && (
            <p className="mb-2 text-amber-400/90">
              Served from the previous snapshot after source errors this run:{" "}
              {report.stale_sections.join(", ")}.
            </p>
          )}
          <p>
            Every number here was collected with Python's standard library alone,
            from public endpoints that need no API keys: Solana JSON-RPC
            (mainnet-beta with a publicnode fallback), DeFiLlama, CoinGecko
            (Jupiter, Binance and Coinbase fallbacks), GitHub REST, and the
            solana.com and Helius feeds. Active-address figures are measured by
            sampling blocks on-chain; the methodology is in the{" "}
            <a href={`${REPO}#readme`} className="text-foreground underline">
              README
            </a>
            .
          </p>
          <p className="mt-2">
            Charts by{" "}
            <a
              href="https://tripwire.sh/dither-kit"
              className="text-foreground underline"
            >
              dither-kit
            </a>
            , motion recipes from{" "}
            <a
              href="https://transitions.dev/"
              className="text-foreground underline"
            >
              transitions.dev
            </a>{" "}
            ·{" "}
            <a href="./report.md" className="text-foreground underline">
              Markdown report
            </a>{" "}
            ·{" "}
            <a href="./report.json" className="text-foreground underline">
              JSON report
            </a>{" "}
            ·{" "}
            <a href={REPO} className="text-foreground underline">
              Source
            </a>
          </p>
        </footer>
      </div>
    </div>
  )
}
