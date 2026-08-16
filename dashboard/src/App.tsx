import { useCallback, useEffect, useMemo, useState } from "react"
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
import { MetricDialog } from "@/components/metric-dialog"
import { LoadingSkeleton } from "@/components/motion"
import {
  Card,
  Controls,
  Grid,
  Hero,
  RANGE_SECONDS,
  type RangeKey,
  LinkList,
  Pill,
  Section,
  RhoBar,
  ShareBar,
  SectionNav,
  Table,
  Tile,
} from "@/components/shell"
import { day, int, num, pct, shortKey, thin, usd } from "@/format"
import type { HistoryRow, Report } from "@/types"

const REPO = "https://github.com/Arnav23apr/sol-sentinel"

/** "updated 3 min ago" reads faster than a timestamp for a page that is
 * constantly refetching. */
function relativeTime(ms: number): string {
  const secs = Math.max(0, Math.round((Date.now() - ms) / 1000))
  if (secs < 60) return "updated just now"
  const mins = Math.round(secs / 60)
  if (mins < 60) return `updated ${mins} min ago`
  const hrs = Math.round(mins / 60)
  return `updated ${hrs} h ago`
}

/** Pull one metric out of the rolling history as a plain number[] for a
 * sparkline, newest last. */
function sparkOf(history: HistoryRow[], key: string, max = 64): number[] {
  const vals = history
    .map((r) => r[key])
    .filter((v): v is number => typeof v === "number")
  return thin(vals, max)
}

/** A cross-check reading. Small values keep two decimals: rounding a $73.63
 * vs $73.59 price comparison to "74 vs 74" would hide exactly what the check
 * is demonstrating. */
function reading(v: number): string {
  return Math.abs(v) < 1000 ? v.toFixed(2) : int(Math.round(v))
}

/** Charts take rows of objects; the collector emits [timestamp, value] pairs. */
function toRows(pairs: [number, number][] | undefined, key: string) {
  return (pairs ?? []).map(([t, v]) => ({ t, [key]: v }))
}

export default function App() {
  const [report, setReport] = useState<Report | null>(null)
  const [history, setHistory] = useState<HistoryRow[]>([])
  const [error, setError] = useState<string | null>(null)
  const [range, setRange] = useState<RangeKey>("all")
  const [openMetric, setOpenMetric] = useState<string | null>(null)
  const [refreshing, setRefreshing] = useState(false)
  const [loadedAt, setLoadedAt] = useState<number>(() => Date.now())
  const [theme, setTheme] = useState<"dark" | "light">(
    () => (localStorage.getItem("sentinel-theme") as "dark" | "light") ?? "dark"
  )

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme)
    localStorage.setItem("sentinel-theme", theme)
  }, [theme])

  // Memoised so the polling effect and the refresh button share one loader
  // and cannot drift apart.
  const load = useCallback(async () => {
    setRefreshing(true)
    try {
      const [r, h] = await Promise.all([
        fetch(`./report.json?t=${Date.now()}`).then((x) => x.json()),
        fetch(`./history.json?t=${Date.now()}`)
          .then((x) => x.json())
          .catch(() => []),
      ])
      setReport(r)
      setHistory(Array.isArray(h) ? h : [])
      setLoadedAt(Date.now())
      setError(null)
    } catch (e) {
      setError(String(e))
    } finally {
      setRefreshing(false)
    }
  }, [])

  useEffect(() => {
    load()
    // The collector republishes every 30 minutes; poll so a tab left open
    // picks up the new snapshot without a manual reload.
    const timer = setInterval(load, 5 * 60 * 1000)
    return () => clearInterval(timer)
  }, [load])

  // Re-render once a minute so the "updated N min ago" label stays truthful
  // without refetching anything.
  const [, setTick] = useState(0)
  useEffect(() => {
    const t = setInterval(() => setTick((x) => x + 1), 60_000)
    return () => clearInterval(t)
  }, [])

  // One range control scopes every time series on the page, so the charts
  // and the sparklines always describe the same window.
  const cutoff = useMemo(() => {
    const secs = RANGE_SECONDS[range]
    return secs == null ? 0 : Date.now() / 1000 - secs
  }, [range])

  const scopedHistory = useMemo(
    () => history.filter((r) => (r.ts ?? 0) >= cutoff),
    [history, cutoff]
  )

  const inRange = useCallback(
    (pairs: [number, number][] | undefined) =>
      (pairs ?? []).filter(([t]) => t >= cutoff),
    [cutoff]
  )

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
    () => toRows(inRange(report?.market.price_history_7d), "price"),
    [report, inRange]
  )
  const tvlRows = useMemo(
    () => toRows(inRange(report?.defi.tvl_history), "tvl"),
    [report, inRange]
  )
  const dexRows = useMemo(
    () => toRows(inRange(report?.defi.dex_history), "volume"),
    [report, inRange]
  )
  const revRows = useMemo(
    () => toRows(inRange(report?.defi.rev_history), "rev"),
    [report, inRange]
  )
  const xstockRows = useMemo(
    () => toRows(inRange(report?.tokenized.xstocks_history), "aum"),
    [report, inRange]
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
  const oc = report.onchain
  const co = report.correlations
  const fl = report.flows
  const ep = n.epoch
  const anomalies = report.anomalies ?? []
  const priceUp = (m.change_24h_pct ?? 0) >= 0
  // Bars are scaled to the largest validator rather than to 100%, since the
  // top holder sits near 4% and scaling to 100 would render every bar as an
  // indistinguishable sliver.
  const topValidatorShare = Math.max(
    ...v.top_validators.map((x) => x.share_pct),
    0.01
  )

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

        <Hero
          severity={
            anomalies.some((x) => x.severity === "critical")
              ? "critical"
              : anomalies.length
                ? "warning"
                : "ok"
          }
          verdict={
            anomalies.length === 0
              ? "All systems normal"
              : `${anomalies.length} ${anomalies.length === 1 ? "alert" : "alerts"}`
          }
          detail={
            anomalies.length === 0
              ? "Every watched metric is inside its 7-day baseline and health thresholds."
              : "Details below. Each finding clears both a statistical and a minimum-size bar."
          }
          stats={[
            {
              label: "Transactions/sec",
              value: num(n.tps),
              sub: `${num(n.true_tps)} non-vote`,
            },
            {
              label: "SOL price",
              value: usd(m.price_usd),
              sub:
                m.change_24h_pct != null
                  ? `${pct(m.change_24h_pct, true)} 24h`
                  : undefined,
              tone: priceUp ? "up" : "down",
            },
            { label: "Total value locked", value: usd(d.tvl_usd) },
            {
              label: "Tx failure rate",
              value:
                oc?.median_program_failure_rate_pct != null
                  ? pct(oc.median_program_failure_rate_pct)
                  : "-",
              // Solana's failure rate is high by design, dominated by
              // arbitrage bots firing speculative transactions, so it is not
              // coloured as an alarm. The subtitle says what it is measured
              // across rather than leaving a scary number unexplained.
              sub: "median, 5 programs",
            },
          ]}
        />

        <Controls
          range={range}
          onRange={setRange}
          onRefresh={load}
          refreshing={refreshing}
          updated={relativeTime(loadedAt)}
        />

        <SectionNav
          items={[
            { id: "network", label: "Network" },
            { id: "validators", label: "Validators" },
            { id: "market", label: "Market" },
            { id: "defi", label: "DeFi" },
            { id: "activity", label: "Activity" },
            { id: "programs", label: "Programs" },
            { id: "flows", label: "Flows" },
            { id: "correlations", label: "Correlations" },
            { id: "validation", label: "Validation" },
            { id: "dev", label: "Development" },
            { id: "news", label: "News" },
          ]}
        />

        {anomalies.length > 0 && (
          <Section title="Alerts">
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
          </Section>
        )}

        <Section
          id="network"
          title="Network performance"
          note="direct from JSON-RPC"
        >
          <Grid>
            <Tile
              label="Transactions per second"
              value={num(n.tps)}
              sub="10-min median, includes votes"
              spark={sparkOf(scopedHistory, "tps")}
              onOpen={() => setOpenMetric("tps")}
            />
            <Tile
              label="Non-vote TPS"
              value={num(n.true_tps)}
              sub="user transactions only"
              spark={sparkOf(scopedHistory, "true_tps")}
              onOpen={() => setOpenMetric("true_tps")}
              sparkColor="orange"
            />
            <Tile
              label="Slot time"
              value={`${num(n.slot_time_ms)} ms`}
              sub="target 400 ms"
              spark={sparkOf(scopedHistory, "slot_time_ms")}
              onOpen={() => setOpenMetric("slot_time_ms")}
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
                spark={sparkOf(scopedHistory, "prio_congestion_pct")}
              onOpen={() => setOpenMetric("prio_congestion_pct")}
              sparkColor="orange"
            />
            )}
            <Tile
              label="Circulating supply"
              value={`${num(n.supply.circulating_sol)} SOL`}
              sub={`inflation ${pct(n.inflation_total_pct)}/yr`}
              spark={sparkOf(scopedHistory, "circulating_sol")}
              onOpen={() => setOpenMetric("circulating_sol")}
              sparkColor="blue"
            />
            {a.median_tx_fee_lamports != null && (
              <Tile
                label="Median transaction fee"
                value={`${int(a.median_tx_fee_lamports)} lam`}
                sub={
                  m.price_usd
                    ? `about $${(
                        (a.median_tx_fee_lamports / 1e9) *
                        m.price_usd
                      ).toFixed(5)} · p90 ${int(a.p90_tx_fee_lamports)}`
                    : `p90 ${int(a.p90_tx_fee_lamports)}`
                }
                spark={sparkOf(scopedHistory, "median_tx_fee")}
              onOpen={() => setOpenMetric("median_tx_fee")}
                sparkColor="orange"
              />
            )}
            {a.base_fee_only_pct != null && (
              <Tile
                label="Paying base fee only"
                value={pct(a.base_fee_only_pct)}
                sub={`of ${int(a.fee_sampled_txs)} sampled transactions · the rest bid for priority`}
                spark={sparkOf(scopedHistory, "base_fee_only_pct")}
              onOpen={() => setOpenMetric("base_fee_only_pct")}
                sparkColor="green"
              />
            )}
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

        <Section id="validators" title="Validators & decentralization">
          <Grid>
            <Tile
              label="Active validators"
              value={int(v.active)}
              spark={sparkOf(scopedHistory, "validators_active")}
              onOpen={() => setOpenMetric("validators_active")}
              sparkColor="green"
            />
            <Tile
              label="Delinquent"
              value={int(v.delinquent)}
              sub={`${pct(v.delinquent_stake_pct)} of stake`}
              spark={sparkOf(scopedHistory, "validators_delinquent")}
              onOpen={() => setOpenMetric("validators_delinquent")}
              sparkColor="red"
            />
            <Tile
              label="Nakamoto coefficient"
              value={int(v.nakamoto_coefficient)}
              sub="validators to reach 1/3 of stake"
              spark={sparkOf(scopedHistory, "nakamoto")}
              onOpen={() => setOpenMetric("nakamoto")}
              sparkColor="purple"
            />
            <Tile
              label="Total active stake"
              value={`${num(v.total_active_stake_sol)} SOL`}
              sub={`stake-weighted commission ${pct(v.avg_commission)}`}
              spark={sparkOf(scopedHistory, "staked_sol")}
              onOpen={() => setOpenMetric("staked_sol")}
              sparkColor="green"
            />
            <Tile
              label="Top-5 stake share"
              value={pct(v.top5_stake_pct)}
              sub={`top-20: ${pct(v.top20_stake_pct)}`}
              spark={sparkOf(scopedHistory, "top5_stake_pct")}
              onOpen={() => setOpenMetric("top5_stake_pct")}
              sparkColor="purple"
            />
            <Tile
              label="Private validator stake"
              value={pct(v.private_stake_pct)}
              sub="on 100%-commission (self-stake) validators"
              spark={sparkOf(scopedHistory, "private_stake_pct")}
              onOpen={() => setOpenMetric("private_stake_pct")}
              sparkColor="orange"
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
                <ShareBar
                  value={x.share_pct}
                  max={topValidatorShare}
                  label={pct(x.share_pct)}
                />,
                `${x.commission ?? "-"}%`,
              ])}
              sortKeys={v.top_validators
                .slice(0, 12)
                .map((x, i) => [i + 1, x.vote, x.stake_sol, x.share_pct, x.commission])}
            />
          </Card>
        </Section>

        <Section id="market" title="Market">
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
              spark={sparkOf(scopedHistory, "sol_price")}
              onOpen={() => setOpenMetric("sol_price")}
              sparkColor={priceUp ? "green" : "red"}
            />
            <Tile
              label="Market cap"
              value={`${usd(m.market_cap_usd)}${
                m.market_cap_estimated ? " (est.)" : ""
              }`}
              sub={m.market_cap_rank ? `rank #${m.market_cap_rank}` : undefined}
              spark={sparkOf(scopedHistory, "market_cap")}
              onOpen={() => setOpenMetric("market_cap")}
              sparkColor="blue"
            />
            <Tile label="24h volume" value={usd(m.volume_24h_usd)}   spark={sparkOf(scopedHistory, "volume_24h")}
              onOpen={() => setOpenMetric("volume_24h")}
              sparkColor="orange"
            />
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
            {/* Area rather than line, and a sparser fill than the default
                gradient. dither-kit's y-scale is always zero-based
                (buildYScale clamps the floor to 0), so a line for a ~$74
                price hugs the top of an empty plot. The area at least uses
                the space; "dotted" keeps the shape while cutting the ink of
                a solid slab. */}
            <div className="h-[210px]">
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
                <Area dataKey="price" variant="dotted" />
                <Tooltip labelKey="t" valueFormatter={(x) => usd(x)} />
              </AreaChart>
            </div>
          </Card>
        </Section>

        <Section id="defi" title="DeFi & economics">
          <Grid>
            <Tile
              label="Total value locked"
              value={usd(d.tvl_usd)}
              spark={sparkOf(scopedHistory, "tvl")}
              onOpen={() => setOpenMetric("tvl")}
            />
            <Tile
              label="Stablecoin supply"
              value={usd(d.stablecoins_usd)}
              spark={sparkOf(scopedHistory, "stables")}
              onOpen={() => setOpenMetric("stables")}
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
              spark={sparkOf(scopedHistory, "dex_vol_24h")}
              onOpen={() => setOpenMetric("dex_vol_24h")}
              sparkColor="orange"
            />
            <Tile
              label="REV 24h"
              value={usd(d.rev_24h_usd)}
              sub={`chain fees ${usd(d.chain_fees_24h_usd)} + MEV tips ${usd(
                d.jito_tips_24h_usd
              )}`}
              spark={sparkOf(scopedHistory, "rev_24h")}
              onOpen={() => setOpenMetric("rev_24h")}
              sparkColor="green"
            />
            <Tile
              label="App fees 24h"
              value={usd(d.app_fees_24h_usd)}
              sub="every protocol on Solana"
              spark={sparkOf(scopedHistory, "app_fees_24h")}
              onOpen={() => setOpenMetric("app_fees_24h")}
              sparkColor="purple"
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
                  <Area dataKey="tvl" variant="dotted" />
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
                sortKeys={(d.stablecoins_top ?? []).map((x) => [x.symbol, x.on_solana_usd, x.change_7d_pct])}
              />
            </Card>
          </div>

          <div className="mt-2.5 grid gap-2.5 lg:grid-cols-2">
            <Card title="Top DEXs" note="24h volume">
              <Table
                head={["DEX", "24h volume"]}
                align="lr"
                rows={d.dex_top.map((x) => [x.name, usd(x.volume_24h_usd)])}
                sortKeys={d.dex_top.map((x) => [x.name, x.volume_24h_usd])}
              />
            </Card>
            <Card title="Top apps by fees" note="24h">
              <Table
                head={["App", "24h fees"]}
                align="lr"
                rows={d.top_fee_apps.map((x) => [x.name, usd(x.fees_24h_usd)])}
                sortKeys={d.top_fee_apps.map((x) => [x.name, x.fees_24h_usd])}
              />
            </Card>
          </div>
        </Section>

        <Section
          id="activity"
          title="Activity & tokenized assets"
          note="activity measured on-chain by Sentinel"
        >
          <Grid>
            <Tile
              label="Activity index"
              value={num(a.activity_index)}
              sub={`unique fee payers per block · ${a.sampled_blocks} blocks sampled over 24h`}
              spark={sparkOf(scopedHistory, "activity_idx")}
              onOpen={() => setOpenMetric("activity_idx")}
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
              spark={sparkOf(scopedHistory, "active_cohort")}
              onOpen={() => setOpenMetric("active_cohort")}
              sparkColor="pink"
            />
            <Tile
              label="xStocks AUM"
              value={usd(tk.xstocks_aum_usd)}
              sub="tokenized equities on Solana"
              spark={sparkOf(scopedHistory, "xstocks_aum")}
              onOpen={() => setOpenMetric("xstocks_aum")}
              sparkColor="pink"
            />
            <Tile
              label="xStocks 24h volume"
              value={usd(tk.xstocks_volume_24h_usd)}
              sub={`${num(tk.xstocks_holders)} holders`}
              spark={sparkOf(scopedHistory, "xstocks_volume")}
              onOpen={() => setOpenMetric("xstocks_volume")}
              sparkColor="orange"
            />
            <Tile
              label="RWA TVL"
              value={usd(tk.rwa_tvl_usd)}
              sub="all real-world-asset protocols"
              spark={sparkOf(scopedHistory, "rwa_tvl")}
              onOpen={() => setOpenMetric("rwa_tvl")}
              sparkColor="blue"
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
                  <Area dataKey="aum" variant="dotted" />
                  <Tooltip labelKey="t" valueFormatter={(x) => usd(x)} />
                </AreaChart>
              </div>
            </Card>
            <Card title="Top tokenized equities">
              <Table
                head={["Ticker", "AUM"]}
                align="lr"
                rows={(tk.xstocks_top ?? []).map((x) => [x.ticker, usd(x.usd)])}
                sortKeys={(tk.xstocks_top ?? []).map((x) => [x.ticker, x.usd])}
              />
            </Card>
          </div>

          <Card title="Top RWA protocols on Solana" className="mt-2.5">
            <Table
              head={["Protocol", "TVL on Solana"]}
              align="lr"
              rows={(tk.rwa_top ?? []).map((x) => [x.name, usd(x.usd)])}
              sortKeys={(tk.rwa_top ?? []).map((x) => [x.name, x.usd])}
              />
          </Card>
        </Section>

        {oc && (oc.programs?.length || oc.drift_secs != null) && (
          <Section
            id="programs"
            title="Program activity & chain health"
            note="measured directly on-chain"
          >
            <Grid>
              {oc.drift_secs != null && (
                <Tile
                  label="Chain clock drift"
                  value={`${oc.drift_secs > 0 ? "+" : ""}${oc.drift_secs.toFixed(1)} s`}
                  sub="chain time against wall clock; slots run slightly long"
                  spark={sparkOf(scopedHistory, "clock_drift_secs")}
              onOpen={() => setOpenMetric("clock_drift_secs")}
                  sparkColor="purple"
                />
              )}
              {oc.median_program_failure_rate_pct != null && (
                <Tile
                  label="Median failure rate"
                  value={pct(oc.median_program_failure_rate_pct)}
                  sub={
                    oc.failure_rate_span_pct
                      ? `across sampled programs, range ${pct(
                          oc.failure_rate_span_pct[0]
                        )} to ${pct(oc.failure_rate_span_pct[1])}`
                      : "across sampled programs"
                  }
                  spark={sparkOf(scopedHistory, "failure_rate_pct")}
              onOpen={() => setOpenMetric("failure_rate_pct")}
                  sparkColor="red"
                />
              )}
              {oc.unwithdrawn_sol_top8 != null && (
                <Tile
                  label="Unwithdrawn rewards"
                  value={`${num(oc.unwithdrawn_sol_top8, 2)} SOL`}
                  sub="inflation rewards sitting in the top 8 vote accounts"
                  spark={sparkOf(scopedHistory, "unwithdrawn_sol")}
              onOpen={() => setOpenMetric("unwithdrawn_sol")}
              sparkColor="green"
            />
              )}
            </Grid>
            {oc.programs && oc.programs.length > 0 && (
              <Card className="mt-2.5">
                <p className="mb-3 text-[12px] text-muted-foreground leading-relaxed">
                  Throughput and failure rate for major programs, from the last{" "}
                  {int(oc.programs[0].sampled)} signatures on each, timed by
                  slot span. The failure rate is a direct read on user
                  experience and is not published by volume-only dashboards.
                </p>
                <Table
                  head={["Program", "Tx/min", "Failed", "Window"]}
                  align="lrrr"
                  rows={oc.programs.map((p) => [
                    p.name,
                    p.tx_per_min != null
                      ? `${int(p.tx_per_min)}${p.low_precision ? " approx." : ""}`
                      : p.tx_per_min_lower_bound != null
                        ? `>${int(p.tx_per_min_lower_bound)}`
                        : "-",
                    <span
                      className={
                        p.failure_rate_pct >= 50
                          ? "text-amber-400"
                          : "text-muted-foreground"
                      }
                    >
                      {pct(p.failure_rate_pct)}
                    </span>,
                    `${num(p.window_secs, 1)} s`,
                  ])}
                  sortKeys={(oc?.programs ?? []).map((p) => [p.name, p.tx_per_min ?? p.tx_per_min_lower_bound ?? null, p.failure_rate_pct, p.window_secs ?? null])}
              />
              </Card>
            )}
          </Section>
        )}

        {fl && fl.accounts.length > 0 && (
          <Section
            id="flows"
            title="Exchange & large-holder balances"
            note={`${fl.verified} verified accounts`}
          >
            <Grid>
              <Tile
                label="Tracked on exchanges"
                value={`${num(fl.total_sol, 2)} SOL`}
                sub={fl.total_usd ? usd(fl.total_usd) : undefined}
                spark={sparkOf(scopedHistory, "exchange_sol")}
                sparkColor="orange"
                onOpen={() => setOpenMetric("exchange_sol")}
              />
              {fl.change_24h_sol != null && (
                <Tile
                  label="Net flow, 24h"
                  value={`${fl.change_24h_sol > 0 ? "+" : ""}${num(fl.change_24h_sol, 2)} SOL`}
                  delta={
                    fl.change_24h_pct != null ? pct(fl.change_24h_pct, true) : undefined
                  }
                  // Inflows can be sold, so they are the bearish direction.
                  deltaUp={fl.change_24h_sol < 0}
                  sub={
                    fl.change_24h_sol > 0
                      ? "moving onto exchanges, sellable"
                      : "moving off exchanges, usually not"
                  }
                />
              )}
              {fl.change_7d_sol != null && (
                <Tile
                  label="Net flow, 7d"
                  value={`${fl.change_7d_sol > 0 ? "+" : ""}${num(fl.change_7d_sol, 2)} SOL`}
                  delta={
                    fl.change_7d_pct != null ? pct(fl.change_7d_pct, true) : undefined
                  }
                  deltaUp={fl.change_7d_sol < 0}
                />
              )}
            </Grid>
            <Card className="mt-2.5">
              <p className="mb-3 text-[12px] text-muted-foreground leading-relaxed">
                Exchange balances are the standard read on supply pressure: SOL
                sitting on an exchange can be sold, SOL that has left usually
                cannot. Every balance is re-verified on-chain each run and an
                account is dropped if it no longer holds a meaningful amount, so
                a stale label cannot become a false claim. Attribution is
                best-effort from public sources — Sentinel verifies what an
                account holds, never who controls it.
              </p>
              <Table
                head={["Account", "Balance (SOL)", "Value", "Activity", "Failed"]}
                align="lrrrr"
                rows={fl.accounts.map((acc) => [
                  acc.label,
                  num(acc.balance_sol, 2),
                  acc.balance_usd ? usd(acc.balance_usd) : "-",
                  acc.tx_per_hour != null ? `${num(acc.tx_per_hour, 1)}/h` : "-",
                  int(acc.failed_txs ?? 0),
                ])}
                sortKeys={fl.accounts.map((acc) => [
                  acc.label,
                  acc.balance_sol,
                  acc.balance_usd ?? null,
                  acc.tx_per_hour ?? null,
                  acc.failed_txs ?? null,
                ])}
              />
            </Card>
          </Section>
        )}

        {co && co.top.length > 0 && (
          <Section
            id="correlations"
            title="What moves together"
            note={`${co.significant_count} of ${co.pairs_tested} pairs survive`}
          >
            <Card>
              <p className="mb-3 text-[12px] text-muted-foreground leading-relaxed">
                Relationships between metrics rather than each metric alone,
                over {co.sample_size} observations. Changes are correlated, not
                levels, because two series that both drift upward correlate near
                +1 whatever the real relationship. Rank correlation is used so a
                single outlier cannot manufacture a result, and
                Benjamini-Hochberg false-discovery control is applied across
                all {co.pairs_tested} pairs, since testing that many at 5% would
                otherwise yield several by chance alone.
              </p>
              <Table
                head={["Relationship", "Correlation", "n", "p"]}
                align="llrr"
                rows={co.top.map((c) => [
                  <span>
                    {c.a_label}{" "}
                    <span className="text-muted-foreground">
                      {c.rho > 0 ? "moves with" : "moves against"}
                    </span>{" "}
                    {c.b_label}
                  </span>,
                  <RhoBar rho={c.rho} />,
                  int(c.n),
                  c.p < 0.0001 ? "<0.0001" : c.p.toFixed(4),
                ])}
                sortKeys={co.top.map((c) => [c.a_label, c.rho, c.n, c.p])}
              />
            </Card>
          </Section>
        )}

        {report.crosscheck && report.crosscheck.checks.length > 0 && (
          <Section
            id="validation"
            title="Cross-source validation"
            note={`${report.crosscheck.agree} of ${report.crosscheck.total} independent sources agree`}
          >
            <Card>
              <p className="mb-3 text-[12px] text-muted-foreground leading-relaxed">
                Quantities two independent sources can both observe, compared
                against each other. Agreement is evidence a number is real;
                disagreement is itself a finding, and is raised as an alert.
                The fee row extrapolates an 8-block sample using the measured
                block rate
                {n.blocks_per_day_measured
                  ? ` (${int(n.blocks_per_day_measured)} blocks/day)`
                  : ""}
                , so it is judged on landing within 2x rather than on a
                precision the sample cannot support.
              </p>
              <Table
                head={["Quantity", "Source A", "Source B", "Gap", "Verdict"]}
                align="llrrl"
                rows={report.crosscheck.checks.map((c) => [
                  c.label,
                  <span className="text-muted-foreground">
                    {c.a_source}: {reading(c.a_value)}
                  </span>,
                  <span className="text-muted-foreground">
                    {c.b_source}: {reading(c.b_value)}
                  </span>,
                  pct(c.gap_pct, true),
                  <span
                    className={
                      c.agrees ? "text-emerald-400" : "text-amber-400"
                    }
                  >
                    {c.agrees ? "agree" : "diverge"}
                    {c.ratio ? ` (${c.ratio.toFixed(2)}x)` : ""}
                    {c.alerting === false && (
                      <span className="text-muted-foreground"> · indicative</span>
                    )}
                  </span>,
                ])}
              />
            </Card>
          </Section>
        )}

        <Section id="dev" title="Protocol development">
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

        <Section id="news" title="Ecosystem news">
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

      <MetricDialog
        metricKey={openMetric}
        history={scopedHistory}
        onClose={() => setOpenMetric(null)}
      />
    </div>
  )
}
