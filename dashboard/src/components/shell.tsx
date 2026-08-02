import type { ReactNode } from "react"
import { Sparkline } from "@/components/dither-kit"
import type { DitherColor } from "@/components/dither-kit"
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
    <section id={id} className="relative z-10 mt-12 first:mt-0">
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
}: {
  label: string
  value: string
  sub?: string
  delta?: string
  deltaUp?: boolean
  spark?: number[]
  sparkColor?: DitherColor
  wide?: boolean
}) {
  // Below ~6 points a sparkline is a flat smear that implies "no movement"
  // rather than "not enough history yet", so hide it until the run history
  // has accumulated.
  const hasSpark = Boolean(spark && spark.length >= 6)
  return (
    <div
      className={cn(
        "group relative flex flex-col overflow-hidden rounded-lg border border-border bg-card pt-3 transition-colors hover:border-border/80",
        hasSpark ? "pb-0" : "pb-3",
        wide && "col-span-full"
      )}
    >
      <div className="px-4 text-[11px] text-muted-foreground">{label}</div>
      <div className="mt-1 flex items-baseline gap-2 px-4">
        <span className="font-semibold text-[22px] text-foreground tracking-tight">
          {value}
        </span>
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
        <div className="mt-0.5 px-4 text-[11px] text-muted-foreground/85 leading-snug">
          {sub}
        </div>
      )}
      {/* Full-bleed strip rather than a floating corner spark: at tile width
          a corner overlay lands on top of the sub text at some breakpoints. */}
      {hasSpark && (
        <div className="pointer-events-none mt-auto h-9 w-full pt-2 opacity-65 transition-opacity group-hover:opacity-100">
          <Sparkline data={spark!} color={sparkColor} bloomOnHover bloom="low" />
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

export function Table({
  head,
  rows,
  align = "",
}: {
  head: string[]
  rows: ReactNode[][]
  /** One char per column: "r" right-aligns (numbers), anything else left. */
  align?: string
}) {
  return (
    <div className="-mx-1 overflow-x-auto px-1">
      <table className="w-full border-collapse text-[12.5px]">
        <thead>
          <tr>
            {head.map((h, i) => (
              <th
                key={h}
                className={cn(
                  "border-border border-b pb-1.5 font-normal text-[10.5px] text-muted-foreground uppercase tracking-wider",
                  align[i] === "r" ? "text-right" : "text-left"
                )}
              >
                {h}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, r) => (
            // biome-ignore lint/suspicious/noArrayIndexKey: rows are positional
            <tr key={r} className="group/row">
              {row.map((cell, c) => (
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
