import { type ReactNode, useState } from "react"
import { Sparkline } from "@/components/dither-kit"
import type { DitherColor } from "@/components/dither-kit"
import { AnimatedValue } from "@/components/motion"
import { cn } from "@/lib/utils"

export function Section({
  id,
  title,
  note,
  children,
}: {
  id?: string
  title: string
  note?: string
  children: ReactNode
}) {
  return (
    // scroll-mt keeps the heading clear of the sticky nav when jumped to.
    <section id={id} className="relative z-10 mt-12 scroll-mt-14 first:mt-0">
      <div className="mb-3 flex items-baseline gap-3 border-border border-b pb-2">
        <h2 className="font-semibold text-[11px] text-muted-foreground uppercase tracking-[0.18em]">
          {title}
        </h2>
        {note && (
          <span className="text-[11px] text-muted-foreground/70">{note}</span>
        )}
      </div>
      {children}
    </section>
  )
}

export function Card({
  title,
  note,
  className,
  children,
}: {
  title?: string
  note?: string
  className?: string
  children: ReactNode
}) {
  return (
    <div
      className={cn(
        "rounded-lg border border-border bg-card p-4 transition-colors hover:border-border/80",
        className
      )}
    >
      {title && (
        <div className="mb-3 flex items-baseline justify-between gap-3">
          <h3 className="font-medium text-[12px] text-foreground/90">{title}</h3>
          {note && (
            <span className="text-[10.5px] text-muted-foreground">{note}</span>
          )}
        </div>
      )}
      {children}
    </div>
  )
}

export function Tile({
  label,
  value,
  sub,
  delta,
  deltaUp,
  spark,
  sparkColor = "blue",
  wide,
  onOpen,
}: {
  label: string
  value: string
  sub?: string
  delta?: string
  deltaUp?: boolean
  spark?: number[]
  sparkColor?: DitherColor
  wide?: boolean
  /** Present when this metric has a recorded history worth opening. */
  onOpen?: () => void
}) {
  // Below ~6 points a sparkline is a flat smear that implies "no movement"
  // rather than "not enough history yet", so hide it until the run history
  // has accumulated.
  const hasSpark = Boolean(spark && spark.length >= 6)
  return (
    <div
      className={cn(
        "group relative flex flex-col rounded-lg border border-border bg-card px-4 py-3 transition-colors hover:border-border/80",
        wide && "col-span-full",
        onOpen &&
          "cursor-pointer hover:border-sky-500/50 focus-visible:outline-2 focus-visible:outline-sky-500"
      )}
      onClick={onOpen}
      onKeyDown={(e) => {
        if (onOpen && (e.key === "Enter" || e.key === " ")) {
          e.preventDefault()
          onOpen()
        }
      }}
      tabIndex={onOpen ? 0 : undefined}
      role={onOpen ? "button" : undefined}
      aria-label={onOpen ? `${label}: open full history` : undefined}
    >
      <div className="text-[11px] text-muted-foreground">{label}</div>
      <div className="mt-1 flex items-baseline gap-2">
        <AnimatedValue
          value={value}
          className="font-semibold text-[22px] text-foreground tracking-tight"
        />
        {delta && (
          <span
            className={cn(
              "font-medium text-[11.5px]",
              deltaUp ? "text-emerald-400" : "text-rose-400"
            )}
          >
            {delta}
          </span>
        )}
      </div>
      {sub && (
        <div className="mt-0.5 text-[11px] text-muted-foreground/85 leading-snug">
          {sub}
        </div>
      )}
      {/* Inset, not full-bleed. Running the spark to the card edge made it
          read as a progress bar, and the corner radius clipped it so it
          looked like a rendering fault. mt-auto pins it to the bottom so
          sparked and unsparked tiles in the same row still line up. */}
      {hasSpark && (
        <div className="pointer-events-none mt-auto w-full pt-3">
          {/* Needs real height to read as a trend rather than a coloured bar:
              at ~16px the dither fill is thicker than the shape it encodes. */}
          <div className="h-10 w-full overflow-hidden rounded-[3px] opacity-70 transition-opacity group-hover:opacity-100">
            <Sparkline
              data={spark!}
              color={sparkColor}
              bloomOnHover
              bloom="low"
            />
          </div>
        </div>
      )}
    </div>
  )
}

export function Grid({
  children,
  min = 190,
}: {
  children: ReactNode
  min?: number
}) {
  return (
    <div
      className="grid gap-2.5"
      style={{
        gridTemplateColumns: `repeat(auto-fill, minmax(${min}px, 1fr))`,
      }}
    >
      {children}
    </div>
  )
}

/**
 * A table whose columns can be sorted by clicking their header.
 *
 * `sortKeys` supplies the value to sort each row by, parallel to `rows`, so
 * sorting works on the underlying number rather than on rendered text (which
 * would order "$1.2B" before "$900M"). Columns with a null key stay inert.
 */
export function Table({
  head,
  rows,
  align = "",
  sortKeys,
  initialSort,
}: {
  head: string[]
  rows: ReactNode[][]
  /** One char per column: "r" right-aligns (numbers), anything else left. */
  align?: string
  sortKeys?: (string | number | null)[][]
  initialSort?: { col: number; dir: "asc" | "desc" }
}) {
  const [sort, setSort] = useState(initialSort ?? null)

  const sortableCols = new Set<number>()
  if (sortKeys?.length) {
    for (let c = 0; c < head.length; c++) {
      if (sortKeys.some((k) => k[c] != null)) sortableCols.add(c)
    }
  }

  const order = rows.map((_, i) => i)
  if (sort && sortKeys?.length) {
    order.sort((a, b) => {
      const av = sortKeys[a]?.[sort.col]
      const bv = sortKeys[b]?.[sort.col]
      if (av == null && bv == null) return 0
      if (av == null) return 1 // missing values sink, either direction
      if (bv == null) return -1
      const cmp =
        typeof av === "number" && typeof bv === "number"
          ? av - bv
          : String(av).localeCompare(String(bv))
      return sort.dir === "asc" ? cmp : -cmp
    })
  }

  const toggle = (c: number) => {
    if (!sortableCols.has(c)) return
    setSort((prev) =>
      prev?.col === c
        ? { col: c, dir: prev.dir === "asc" ? "desc" : "asc" }
        : // Numbers are almost always most interesting largest-first.
          { col: c, dir: align[c] === "r" ? "desc" : "asc" }
    )
  }

  return (
    <div className="-mx-1 overflow-x-auto px-1">
      <table className="w-full border-collapse text-[12.5px]">
        <thead>
          <tr>
            {head.map((h, i) => {
              const on = sortableCols.has(i)
              const active = sort?.col === i
              return (
                <th
                  key={h}
                  aria-sort={
                    active
                      ? sort.dir === "asc"
                        ? "ascending"
                        : "descending"
                      : undefined
                  }
                  className={cn(
                    "border-border border-b pb-1.5 font-normal text-[10.5px] uppercase tracking-wider transition-colors",
                    align[i] === "r" ? "text-right" : "text-left",
                    on && "cursor-pointer select-none hover:text-foreground",
                    active ? "text-foreground" : "text-muted-foreground"
                  )}
                  onClick={() => toggle(i)}
                  onKeyDown={(e) => {
                    if (on && (e.key === "Enter" || e.key === " ")) {
                      e.preventDefault()
                      toggle(i)
                    }
                  }}
                  tabIndex={on ? 0 : undefined}
                >
                  {h}
                  {on && (
                    <span className="ml-1 text-[9px] opacity-70">
                      {active ? (sort.dir === "asc" ? "▲" : "▼") : "↕"}
                    </span>
                  )}
                </th>
              )
            })}
          </tr>
        </thead>
        <tbody>
          {order.map((ri) => (
            <tr key={ri} className="group/row">
              {rows[ri].map((cell, c) => (
                <td
                  // biome-ignore lint/suspicious/noArrayIndexKey: columns are positional
                  key={c}
                  className={cn(
                    "border-border/60 border-b py-1.5 text-foreground/85 transition-colors group-hover/row:text-foreground",
                    align[c] === "r" && "text-right tabular-nums",
                    c === 0 && "pr-3"
                  )}
                >
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

/**
 * The band above the fold. A reader should be able to answer "is Solana
 * healthy right now, and what is it doing" without scrolling, which the
 * previous layout could not do: the verdict was one thin strip under its own
 * section header, and every metric below it was rendered at the same weight,
 * so nothing indicated what to look at first.
 */
export function Hero({
  verdict,
  detail,
  severity,
  stats,
}: {
  verdict: string
  detail: string
  severity: "ok" | "warning" | "critical"
  stats: { label: string; value: string; sub?: string; tone?: "up" | "down" }[]
}) {
  const accent = {
    ok: "text-emerald-400 border-l-emerald-400",
    warning: "text-amber-400 border-l-amber-400",
    critical: "text-rose-400 border-l-rose-400",
  }[severity]

  return (
    <section className="relative z-10">
      <div
        className={cn(
          "rounded-lg border border-border border-l-2 bg-card px-5 py-4",
          accent
        )}
      >
        <div className="flex flex-wrap items-baseline gap-x-3 gap-y-1">
          <h2 className={cn("font-semibold text-[15px]", accent)}>{verdict}</h2>
          <p className="text-[12.5px] text-muted-foreground">{detail}</p>
        </div>

        <div className="mt-4 grid gap-x-6 gap-y-4 border-border/70 border-t pt-4 sm:grid-cols-2 lg:grid-cols-4">
          {stats.map((s) => (
            <div key={s.label}>
              <div className="text-[10.5px] text-muted-foreground uppercase tracking-[0.12em]">
                {s.label}
              </div>
              <div className="mt-1 flex items-baseline gap-2">
                <AnimatedValue
                  value={s.value}
                  className="font-semibold text-[26px] text-foreground tracking-tight"
                />
                {s.sub && (
                  <span
                    className={cn(
                      "text-[12px]",
                      s.tone === "up"
                        ? "text-emerald-400"
                        : s.tone === "down"
                          ? "text-rose-400"
                          : "text-muted-foreground"
                    )}
                  >
                    {s.sub}
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export type RangeKey = "24h" | "7d" | "30d" | "all"

export const RANGE_SECONDS: Record<RangeKey, number | null> = {
  "24h": 86_400,
  "7d": 7 * 86_400,
  "30d": 30 * 86_400,
  all: null,
}

/**
 * Time-range control. Sits in one row above the content it scopes and applies
 * to every time series on the page at once, so the numbers always agree with
 * each other. Presets rather than a calendar: nobody wants to pick dates to
 * ask "what happened today".
 */
export function Controls({
  range,
  onRange,
  onRefresh,
  refreshing,
  updated,
}: {
  range: RangeKey
  onRange: (r: RangeKey) => void
  onRefresh: () => void
  refreshing: boolean
  updated: string
}) {
  const ranges: RangeKey[] = ["24h", "7d", "30d", "all"]
  return (
    <div className="mb-3 flex flex-wrap items-center gap-x-3 gap-y-2">
      <div
        className="flex items-center gap-0.5 rounded-md border border-border bg-card p-0.5"
        role="group"
        aria-label="Time range"
      >
        {ranges.map((r) => (
          <button
            key={r}
            type="button"
            aria-pressed={range === r}
            onClick={() => onRange(r)}
            className={cn(
              "cursor-pointer rounded px-2.5 py-1 text-[11px] transition-colors",
              range === r
                ? "bg-muted text-foreground"
                : "text-muted-foreground hover:text-foreground"
            )}
          >
            {r}
          </button>
        ))}
      </div>

      <button
        type="button"
        onClick={onRefresh}
        disabled={refreshing}
        className="cursor-pointer rounded-md border border-border bg-card px-2.5 py-1 text-[11px] text-muted-foreground transition-colors hover:text-foreground disabled:opacity-50"
      >
        {refreshing ? "refreshing…" : "refresh"}
      </button>

      <span className="text-[11px] text-muted-foreground">{updated}</span>
    </div>
  )
}

/** Jump links for a page that is otherwise several screens of uniform cards. */
export function SectionNav({
  items,
}: {
  items: { id: string; label: string }[]
}) {
  return (
    <nav className="scrollbar-none sticky top-0 z-20 -mx-4 mb-2 flex gap-1 overflow-x-auto border-border/60 border-b bg-background/85 px-4 py-2 backdrop-blur">
      {items.map((it) => (
        <a
          key={it.id}
          href={`#${it.id}`}
          className="whitespace-nowrap rounded-md px-2.5 py-1 text-[11px] text-muted-foreground transition-colors hover:bg-muted hover:text-foreground"
        >
          {it.label}
        </a>
      ))}
    </nav>
  )
}

/**
 * A share rendered as a number with a proportional bar behind it.
 *
 * A column of twelve near-identical percentages is read digit by digit; the
 * bar makes the ranking and the size of the gaps legible at a glance without
 * removing the exact figure.
 */
export function ShareBar({
  value,
  max,
  label,
}: {
  value: number
  max: number
  label: string
}) {
  const width = max > 0 ? Math.max(2, (value / max) * 100) : 0
  return (
    <div className="flex items-center justify-end gap-2">
      <div
        className="h-1.5 w-16 shrink-0 overflow-hidden rounded-full bg-muted"
        role="img"
        aria-label={`${label} of total stake`}
      >
        <div
          className="h-full rounded-full bg-sky-500/70 transition-[width] duration-500"
          style={{ width: `${width}%` }}
        />
      </div>
      <span className="tabular-nums">{label}</span>
    </div>
  )
}

export function Pill({
  children,
  tone = "muted",
}: {
  children: ReactNode
  tone?: "muted" | "open" | "merged" | "critical" | "warning" | "ok"
}) {
  const tones = {
    muted: "text-muted-foreground",
    open: "text-sky-400",
    merged: "text-emerald-400",
    critical: "text-rose-400",
    warning: "text-amber-400",
    ok: "text-emerald-400",
  }
  return (
    <span
      className={cn(
        "shrink-0 rounded-full bg-muted px-2 py-0.5 font-medium text-[10px] tracking-wide",
        tones[tone]
      )}
    >
      {children}
    </span>
  )
}

export function LinkList({
  items,
}: {
  items: {
    key: string | number
    title: string
    url: string
    tone?: "muted" | "open" | "merged"
    badge?: string
    when?: string
  }[]
}) {
  if (!items.length)
    return <p className="text-[12px] text-muted-foreground">Nothing right now.</p>
  return (
    <ul className="flex flex-col">
      {items.map((it) => (
        <li
          key={it.key}
          className="flex flex-wrap items-baseline gap-2 border-border/60 border-b py-2 last:border-b-0"
        >
          <a
            href={it.url}
            target="_blank"
            rel="noopener noreferrer"
            className="min-w-[200px] flex-1 text-[12.5px] text-foreground/85 leading-snug transition-colors hover:text-sky-400"
          >
            {it.title}
          </a>
          {it.badge && <Pill tone={it.tone ?? "muted"}>{it.badge}</Pill>}
          {it.when && (
            <span className="shrink-0 text-[11px] text-muted-foreground tabular-nums">
              {it.when}
            </span>
          )}
        </li>
      ))}
    </ul>
  )
}
