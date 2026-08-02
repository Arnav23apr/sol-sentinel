type Num = number | null | undefined

const compact = (v: number, digits: number) => {
  const a = Math.abs(v)
  if (a >= 1e12) return `${(v / 1e12).toFixed(digits)}T`
  if (a >= 1e9) return `${(v / 1e9).toFixed(digits)}B`
  if (a >= 1e6) return `${(v / 1e6).toFixed(digits)}M`
  if (a >= 1e3) return `${(v / 1e3).toFixed(digits)}K`
  return a >= 100 || Number.isInteger(v) ? v.toFixed(0) : v.toFixed(2)
}

export const num = (v: Num, digits = 1) =>
  v == null ? "-" : compact(v, digits)

export const usd = (v: Num, digits = 2) => {
  if (v == null) return "-"
  const a = Math.abs(v)
  if (a < 1000) return `$${v.toFixed(2)}`
  return `$${compact(v, digits)}`
}

export const pct = (v: Num, signed = false) => {
  if (v == null) return "-"
  const sign = signed && v > 0 ? "+" : ""
  return `${sign}${v.toFixed(2)}%`
}

export const int = (v: Num) => (v == null ? "-" : v.toLocaleString())

export const day = (ts: Num) =>
  ts == null
    ? "-"
    : new Date(ts * 1000).toLocaleDateString(undefined, {
        month: "short",
        day: "numeric",
      })

export const time = (ts: Num) =>
  ts == null
    ? "-"
    : new Date(ts * 1000).toLocaleString(undefined, {
        month: "short",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      })

export const shortKey = (k?: string | null) =>
  k ? `${k.slice(0, 4)}…${k.slice(-4)}` : "-"

/** Down-sample a series to at most `max` points, always keeping the last one
 * so the newest value is never dropped off the end of a sparkline. */
export function thin<T>(series: T[], max: number): T[] {
  if (series.length <= max) return series
  const step = Math.ceil(series.length / max)
  const out: T[] = []
  for (let i = series.length - 1; i >= 0; i -= step) out.unshift(series[i])
  return out
}
