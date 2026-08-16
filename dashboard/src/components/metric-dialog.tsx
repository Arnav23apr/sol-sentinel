import { useEffect } from "react"
import {
  Area,
  AreaChart,
  Grid as ChartGrid,
  Tooltip,
  XAxis,
  YAxis,
} from "@/components/dither-kit"
import type { DitherColor } from "@/components/dither-kit"
import { int, num, pct, usd } from "@/format"
import type { HistoryRow } from "@/types"

type Fmt = "usd" | "pct" | "num" | "int"

/** How each recorded metric should be titled and formatted when opened. */
export const METRICS: Record<
  string,
  { label: string; fmt: Fmt; color: DitherColor; note?: string }
> = {
  tps: { label: "Transactions per second", fmt: "num", color: "blue" },
  true_tps: { label: "Non-vote TPS", fmt: "num", color: "orange" },
  slot_time_ms: { label: "Slot time (ms)", fmt: "num", color: "purple" },
  prio_congestion_pct: {
    label: "AMM write-lock congestion",
    fmt: "pct",
    color: "orange",
  },
  median_tx_fee: {
    label: "Median transaction fee (lamports)",
    fmt: "int",
    color: "orange",
  },
  base_fee_only_pct: { label: "Paying base fee only", fmt: "pct", color: "green" },
  circulating_sol: { label: "Circulating supply (SOL)", fmt: "num", color: "blue" },
  validators_active: { label: "Active validators", fmt: "int", color: "green" },
  validators_delinquent: {
    label: "Delinquent validators",
    fmt: "int",
    color: "red",
  },
  nakamoto: { label: "Nakamoto coefficient", fmt: "int", color: "purple" },
  staked_sol: { label: "Total active stake (SOL)", fmt: "num", color: "green" },
  top5_stake_pct: { label: "Top-5 stake share", fmt: "pct", color: "purple" },
  private_stake_pct: {
    label: "Private validator stake",
    fmt: "pct",
    color: "orange",
  },
  sol_price: { label: "SOL price", fmt: "usd", color: "green" },
  market_cap: { label: "Market cap", fmt: "usd", color: "blue" },
  volume_24h: { label: "24h volume", fmt: "usd", color: "orange" },
  tvl: { label: "Total value locked", fmt: "usd", color: "blue" },
  stables: { label: "Stablecoin supply", fmt: "usd", color: "green" },
  dex_vol_24h: { label: "DEX volume (24h)", fmt: "usd", color: "orange" },
  rev_24h: { label: "REV (24h)", fmt: "usd", color: "green" },
  app_fees_24h: { label: "App fees (24h)", fmt: "usd", color: "purple" },
  activity_idx: {
    label: "Activity index",
    fmt: "num",
    color: "pink",
    note: "unique non-vote fee payers per sampled block",
  },
  active_cohort: {
    label: "Persistently-active cohort",
    fmt: "num",
    color: "pink",
  },
  xstocks_aum: { label: "xStocks AUM", fmt: "usd", color: "pink" },
  xstocks_volume: { label: "xStocks 24h volume", fmt: "usd", color: "orange" },
  rwa_tvl: { label: "RWA TVL", fmt: "usd", color: "blue" },
  failure_rate_pct: {
    label: "Median program failure rate",
    fmt: "pct",
    color: "red",
    note: "median across the five sampled programs",
  },
  clock_drift_secs: {
    label: "Chain clock drift (s)",
    fmt: "num",
    color: "purple",
  },
  exchange_sol: {
    label: "SOL held on tracked exchanges",
    fmt: "num",
    color: "orange",
    note: "aggregate across publicly-attributed accounts, verified each run",
  },
  unwithdrawn_sol: {
    label: "Unwithdrawn rewards (SOL)",
    fmt: "num",
    color: "green",
  },
}

const format = (v: number, f: Fmt) =>
  f === "usd" ? usd(v) : f === "pct" ? pct(v) : f === "int" ? int(v) : num(v)

/** Compact axis stamp. The full locale string ("Aug 2, 01:44 PM") is wide
 * enough that adjacent ticks ran into each other. */
const axisStamp = (ts: number) => {
  const d = new Date(ts * 1000)
  const day = d.toLocaleDateString(undefined, { month: "short", day: "numeric" })
  const hm = d.toLocaleTimeString(undefined, {
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  })
  return `${day} ${hm}`
}

/**
 * Full history for one metric, opened by clicking its tile.
 *
 * The collector records ~34 metrics every half hour but the page could only
 * ever show the latest value plus a thumbnail, so the accumulated history was
 * effectively unreachable. This makes every tile a way into its own series.
 */
export function MetricDialog({
  metricKey,
  history,
  onClose,
}: {
  metricKey: string | null
  history: HistoryRow[]
  onClose: () => void
}) {
  useEffect(() => {
    if (!metricKey) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose()
    }
    window.addEventListener("keydown", onKey)
    // Stop the page behind the dialog from scrolling under it.
    const prev = document.body.style.overflow
    document.body.style.overflow = "hidden"
    return () => {
      window.removeEventListener("keydown", onKey)
      document.body.style.overflow = prev
    }
  }, [metricKey, onClose])

  if (!metricKey) return null
  const meta = METRICS[metricKey]
  if (!meta) return null

  const points = history
    .filter((r) => typeof r[metricKey] === "number" && r.ts)
    .map((r) => ({ t: r.ts, v: r[metricKey] as number }))

  const values = points.map((p) => p.v)
  const first = values[0]
  const last = values[values.length - 1]
  const change =
    first != null && last != null && first !== 0
      ? ((last - first) / Math.abs(first)) * 100
      : null

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-4 backdrop-blur-sm"
      role="dialog"
      aria-modal="true"
      aria-label={meta.label}
      onClick={onClose}
      onKeyDown={(e) => e.key === "Escape" && onClose()}
    >
      <div
        className="max-h-[88vh] w-full max-w-3xl overflow-y-auto rounded-lg border border-border bg-card p-5"
        // Clicks inside must not fall through to the backdrop's close.
        onClick={(e) => e.stopPropagation()}
        onKeyDown={(e) => e.stopPropagation()}
      >
        <div className="flex items-start justify-between gap-4">
          <div>
            <h2 className="font-semibold text-[15px] text-foreground">
              {meta.label}
            </h2>
            <p className="mt-0.5 text-[11.5px] text-muted-foreground">
              {points.length} recorded {points.length === 1 ? "point" : "points"}
              {meta.note ? ` · ${meta.note}` : ""}
            </p>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="cursor-pointer rounded-md border border-border px-2.5 py-1 text-[11px] text-muted-foreground transition-colors hover:text-foreground"
          >
            close
          </button>
        </div>

        {points.length < 2 ? (
          <p className="py-10 text-center text-[12.5px] text-muted-foreground">
            Not enough history yet. This metric is recorded every 30 minutes;
            check back once a few more snapshots have landed.
          </p>
        ) : (
          <>
            <div className="mt-4 flex flex-wrap gap-x-8 gap-y-2 border-border/70 border-t pt-4">
              {[
                ["Latest", format(last, meta.fmt)],
                ["Low", format(Math.min(...values), meta.fmt)],
                ["High", format(Math.max(...values), meta.fmt)],
                [
                  "Change over window",
                  change == null ? "-" : pct(change, true),
                ],
              ].map(([k, val]) => (
                <div key={k}>
                  <div className="text-[10.5px] text-muted-foreground uppercase tracking-[0.1em]">
                    {k}
                  </div>
                  <div className="mt-0.5 font-semibold text-[16px] text-foreground tabular-nums">
                    {val}
                  </div>
                </div>
              ))}
            </div>

            <div className="mt-4 h-[300px]">
              <AreaChart
                data={points}
                config={{ v: { label: meta.label, color: meta.color } }}
                bloom="low"
              >
                <ChartGrid />
                <XAxis
                  dataKey="t"
                  tickFormatter={(x) => axisStamp(x as number)}
                  maxTicks={4}
                />
                <YAxis tickFormatter={(x) => format(x, meta.fmt)} />
                <Area dataKey="v" variant="dotted" />
                <Tooltip
                  labelKey="t"
                  valueFormatter={(x) => format(x, meta.fmt)}
                />
              </AreaChart>
            </div>
          </>
        )}
      </div>
    </div>
  )
}
