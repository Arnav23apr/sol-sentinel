import { useEffect, useRef, useState } from "react"
import { cn } from "@/lib/utils"

/**
 * A value that pops its characters in whenever it actually changes.
 *
 * The dashboard re-fetches every five minutes, so most tiles re-render with
 * an identical value. Animating on every render would make the page twitch
 * constantly and stop meaning anything, so the animation is keyed to a real
 * change in the rendered string.
 *
 * Pure CSS keyframes with a per-character delay (the transitions.dev
 * "number pop-in" recipe); React only toggles the class.
 */
export function AnimatedValue({
  value,
  className,
}: {
  value: string
  className?: string
}) {
  const [animating, setAnimating] = useState(false)
  const previous = useRef<string | null>(null)

  useEffect(() => {
    // Skip the very first paint: the whole page is already arriving at once,
    // and animating every tile on load reads as noise rather than as news.
    if (previous.current === null) {
      previous.current = value
      return
    }
    if (previous.current === value) return
    previous.current = value
    setAnimating(true)
    const done = setTimeout(() => setAnimating(false), 900)
    return () => clearTimeout(done)
  }, [value])

  return (
    <span
      // Re-keying on the value restarts the keyframes; without it a change
      // arriving mid-animation would be skipped.
      key={animating ? value : undefined}
      className={cn("t-digit-group", animating && "is-animating", className)}
      aria-label={value}
    >
      {value.split("").map((char, i) => (
        <span
          // biome-ignore lint/suspicious/noArrayIndexKey: position is the identity
          key={i}
          className="t-digit"
          style={{ "--digit-index": i } as React.CSSProperties}
          aria-hidden
        >
          {char}
        </span>
      ))}
    </span>
  )
}

/** Placeholder block used while the first snapshot is still loading. */
export function Skeleton({ className }: { className?: string }) {
  return <div className={cn("t-skeleton", className)} />
}

/** First-load view: the real layout with its numbers not yet filled in, so
 * the page does not visibly jump when data lands. */
export function LoadingSkeleton() {
  return (
    <div className="mx-auto max-w-[1180px] px-4 pb-20">
      <header className="flex items-center gap-3 py-6">
        <span className="text-[19px] text-sky-400">◎</span>
        <h1 className="font-semibold text-[17px] tracking-[0.12em]">
          SOL SENTINEL
        </h1>
        <span className="text-[11.5px] text-muted-foreground">
          reading the chain…
        </span>
      </header>

      <Skeleton className="h-14 w-full rounded-lg" />

      <div
        className="mt-8 grid gap-2.5"
        style={{ gridTemplateColumns: "repeat(auto-fill, minmax(190px, 1fr))" }}
      >
        {Array.from({ length: 8 }, (_, i) => (
          <div
            key={i}
            className="rounded-lg border border-border bg-card px-4 py-3"
          >
            <Skeleton className="h-3 w-24" />
            <Skeleton className="mt-2.5 h-6 w-20" />
            <Skeleton className="mt-2 h-2.5 w-28" />
          </div>
        ))}
      </div>

      <div className="mt-2.5 grid gap-2.5 lg:grid-cols-[2fr_1fr]">
        <Skeleton className="h-[250px] rounded-lg" />
        <Skeleton className="h-[250px] rounded-lg" />
      </div>
    </div>
  )
}
