# ◎ Sol Sentinel

**An autonomous, keyless monitor for the state of the Solana ecosystem.**

Sol Sentinel collects 60+ metrics about Solana every 30 minutes, detects anomalies against rolling baselines, and publishes three synchronized outputs:

| Output | What it is |
|---|---|
| [`docs/index.html`](docs/index.html) | Interactive dashboard, dark theme, dithered charts |
| [`docs/report.md`](docs/report.md) | Human-readable Markdown report |
| [`docs/report.json`](docs/report.json) | Machine-readable structured report |

**Live dashboard:** https://arnav23apr.github.io/sol-sentinel/

The collector needs **no API keys** and **no Python packages**: every source is a public endpoint, and the entire data pipeline runs on the Python standard library. There is nothing to `pip install`.

```bash
git clone https://github.com/Arnav23apr/sol-sentinel
cd sol-sentinel
python3 -m sentinel.main --once       # one snapshot: collect, detect, render
python3 -m sentinel.main --loop 30    # headless: refresh every 30 minutes
python3 -m sentinel.main --serve 8080 # serve docs/ with background refresh
```

Requires Python 3.9+. That is the whole setup for the data side.

The test suite is standard-library `unittest` and runs offline against fixtures and stubs, so it needs no network and no keys:

```bash
python3 -m unittest discover -s tests -v
```

It covers the anomaly math and its direction filters, the key contract between `history.py` and `anomaly.py` (a typo on either side would silently stop a metric from ever alerting), per-source error isolation including the stale-fallback path, RSS and Atom parsing, and number formatting. It runs on every scheduled collection, so a regression fails the run before a bad report can be published.

The dashboard is a separate Vite + React app in [`dashboard/`](dashboard) that reads the collector's JSON. Its build output is committed to `docs/`, so **you only need Node if you want to change the dashboard itself**:

```bash
cd dashboard && npm install && npm run build
```

`npm run dev` serves the app with hot reload and reads `docs/report.json` live, so run the collector once first.

## What it covers

**Network performance.** TPS (total and non-vote), slot time, slot height, block height, epoch number with progress and time-to-completion, lifetime transaction count, RPC health, node version, SOL supply (total, circulating, non-circulating), annual inflation rate, and a congestion gauge: the share of recent slots where write-locking hot AMM accounts (Raydium, Jupiter, Orca, Pump.fun) required a priority fee.

**Transaction fees, measured from the chain.** Median, p90, p99 and mean fee for non-vote transactions, plus the share paying nothing above the 5,000-lamport base fee. Fees are read out of the same sampled blocks the activity index already fetches, so this costs no extra requests. Vote transactions are excluded deliberately: they are a fixed base fee and about half of all transactions, so including them pins every percentile to the base fee and hides what users actually pay.

**Program activity and chain health, measured directly.** Throughput and **failure rate** for five major programs (Jupiter, Raydium, Orca, Pump.fun, SPL Token), from the last 1,000 signatures on each. The failure rate is the interesting one: it is a direct read on what using Solana actually feels like, it moves sharply during congestion and bot activity, and no dashboard reporting volume alone will show it. Also chain clock drift, the gap between Solana's own timestamps and wall clock, and inflation rewards accrued but not yet withdrawn from the largest vote accounts.

Rates are timed by **slot span rather than `blockTime`**, which only has one-second resolution: the busiest programs fit all 1,000 signatures inside a single second, which would produce an invented figure. The oldest slot in each response is dropped, since a capped response holds only the tail of it and charging its full duration biases the rate down. Where the sample is still coarse, the number is labelled approximate rather than presented as precise.

**Validators and decentralization.** Active vs delinquent validator counts, delinquent stake percentage, total active stake, Nakamoto coefficient computed from the live stake distribution, top-5/10/20 stake concentration, the full cumulative stake curve, stake-weighted commission across delegatable validators, a commission histogram, the share of stake sitting on private 100%-commission validators, and a top-validators table.

**Economic indicators.** SOL price, 24h change, market cap and rank, 24h volume, distance from ATH, a 7-day price chart, stablecoin supply on Solana with a per-asset breakdown, daily DEX volume with a top-DEX table, app fees, and **REV (Real Economic Value): chain fees plus Jito MEV tips**, current and as a 90-day series.

**Ecosystem growth.** Tokenized equities (xStocks): AUM on Solana, per-ticker breakdown, 24h DEX volume and holder count; total RWA TVL with top protocols; and an on-chain activity index Sentinel measures itself (methodology below).

**Development and upgrades.** Open SIMD proposals, recently merged SIMDs, an upgrade watchlist flagging consensus/fee/Alpenglow-related proposals, and the latest Agave and Firedancer releases.

**News.** Latest items from solana.com news and the Helius engineering blog, plus Solana-filtered items from Decrypt and The Block.

## Data sources and integration

Priority went to direct, keyless sources. Each source is isolated: if one fails, its section degrades to the last good snapshot (flagged as stale in the report) and everything else stays fresh.

| Source | Transport | Used for |
|---|---|---|
| Solana JSON-RPC `api.mainnet-beta.solana.com` (fallback `solana-rpc.publicnode.com`) | `urllib` POST | getHealth, getVersion, getSlot, getBlockTime, getEpochInfo, getRecentPerformanceSamples, getSupply, getRecentPrioritizationFees, getVoteAccounts, getBalance, getSignaturesForAddress, getInflationRate, getInflationGovernor, getBlock |
| DeFiLlama (`api.llama.fi`, `stablecoins.llama.fi`) | GET | TVL and history, stablecoin supply and per-asset breakdown, DEX volumes, fees, REV components (chain fees, Jito MEV tips), xStocks, RWA protocols |
| CoinGecko (fallbacks: Jupiter lite-api, Binance, Coinbase) | GET | SOL price, market cap, rank, volume, ATH, 7d chart. If every source carrying market cap fails, mcap is estimated as price x on-chain circulating supply and labeled as estimated |
| GitHub REST (unauthenticated) | GET | SIMD PRs, Agave and Firedancer releases (4 calls per run against the 60/hr anonymous limit) |
| RSS/Atom (solana.com, Helius, Decrypt, The Block) | GET + `xml.etree` | Ecosystem news |

### Two named sources this deliberately does not use

The brief lists Dune Analytics and Twitter among the sources to prioritise, and also states that solutions requiring no API keys are preferred. Those two asks conflict: Dune's API is key-gated on every tier, and Twitter/X removed free programmatic read access, leaving a paid key or terms-violating scraping.

This resolves the conflict in favour of the keyless constraint, because that constraint is what makes the rest of the design work. With no keys and no packages, the collector runs on a free GitHub Actions runner every 30 minutes forever, anyone can clone the repo and get identical results with zero setup, and there is no credential to rotate, leak, or expire. Adding one keyed source would forfeit all of that for a fraction of the data.

Where those sources would have contributed, Sentinel goes to the underlying data instead. Dune dashboards are themselves built on chain data, so Sentinel queries the chain directly, and in several cases measures quantities Dune would have to be trusted for: transaction fee distribution, per-program throughput and failure rates, block production rate, and clock drift are all computed from raw RPC here. The Twitter gap is narrower: announcements arrive through the solana.com and Helius feeds, but social sentiment is genuinely not covered, and no keyless substitute for it exists.

### Other notes

Ankr and dRPC have dropped keyless Solana RPC access; publicnode hangs on `getSupply`, so that one method never falls back; CoinGecko's keyless tier throttles bursts hard, so calls are spaced and every price value has a fallback chain; and `solana.com/data` renders its numbers client-side, so Sentinel reads the same underlying sources directly instead of scraping it.

## Automation strategy

Two GitHub Actions workflows, both committing back to `main`:

- [`update.yml`](.github/workflows/update.yml) runs every 30 minutes: checkout, run `python -m sentinel.main --once`, commit the refreshed `docs/` and `data/`. There is no dependency-install step because there are no dependencies.
- [`dashboard.yml`](.github/workflows/dashboard.yml) runs only when `dashboard/**` changes: `npm ci && npm run build`, which writes the built app into `docs/`.

Splitting them keeps the 30-minute loop to a bare Python run rather than a Node build. Both share a concurrency group so they never race on a push. GitHub Pages serves `docs/`, so the dashboard and both reports republish automatically with no servers and no cost. Commits made with the built-in `GITHUB_TOKEN` do not retrigger workflows, so there is no run recursion.

The metric history behind trends and anomaly baselines lives in [`data/history.jsonl`](data/history.jsonl), one compact row per run, capped at about 90 days. Because the workflow commits it back, the repository itself is the database: no external storage, and anyone who clones the repo gets the full history.

That does mean a local run can collide with the scheduled one. Only `history.jsonl` holds anything irreplaceable, so it is merged with `merge=union` (see [`.gitattributes`](.gitattributes)) — correct for an append-only log keyed by timestamp — and `history.load()` deduplicates by timestamp and skips stray conflict markers, since duplicate rows would quietly skew every rolling baseline. Everything else under `docs/` and `data/` is fully derived, so a conflict there carries no information; [`scripts/resolve-generated.sh`](scripts/resolve-generated.sh) resolves those and regenerates them.

## Anomaly detection

Two layers run on every snapshot (see [`sentinel/anomaly.py`](sentinel/anomaly.py)):

1. **Robust statistical outliers.** Each watched metric (TPS, non-vote TPS, slot time, delinquent validators and stake, SOL price, TVL, stablecoin supply, DEX volume, fees, activity index, median transaction fee, program failure rate) is compared to its rolling 7-day baseline using median absolute deviation. MAD is used instead of mean and standard deviation so one bad sample from a free endpoint cannot poison the baseline. Direction is respected: TPS alerts only on drops, slot time and delinquency only on spikes, prices and volumes on both.

   A finding has to clear **two** bars, not one: a MAD z-score of |z| >= 3.5 (critical at 6) **and** a minimum move size declared per metric. The second bar is not padding. MAD shrinks toward zero on a metric that has been stable, so a trivial change divided by a near-zero scale yields an enormous z-score, and this was not hypothetical: TVL moving 0.13%, from $4.7499B to $4.7559B, scored 415 sigma and was published as CRITICAL on the live dashboard. An alert like that spends the reader's trust in every other number on the page. Statistical unusualness alone is not a reason to raise an alarm, so a metric must be both surprising and moving enough to matter.
2. **Absolute health rules.** Thresholds that matter regardless of history: TPS below 1,000, slot time above 600 ms, delinquent stake above 5% (critical above 10%), and SOL moving more than 10% in 24h (critical at 20%).

A serious incident trips both layers at once (collapsing TPS is simultaneously a 100-sigma outlier and below the absolute floor), so findings are merged to one per metric, keeping the more severe and, on a tie, the threshold rule, whose wording says what the number means rather than how unusual it is. The surviving finding records that the other layer also fired.

Every finding carries its evidence (value, baseline median, z-score) into all three outputs, so an alert is always explainable.

## Cross-source validation

Most of this report takes each number on faith from whichever endpoint served it. Three quantities, though, are observable from two independent directions, and comparing them is worth more than either reading alone: agreement is evidence the number is real, and disagreement is itself a finding. Each snapshot checks (see [`sentinel/crosscheck.py`](sentinel/crosscheck.py)):

| Quantity | Source A | Source B |
|---|---|---|
| Chain fees (24h) | fees summed from blocks Sentinel samples itself | DeFiLlama's indexer |
| SOL price | CoinGecko, aggregating centralised venues | Jupiter, quoting the on-chain DEX price |
| Circulating supply | `getSupply` from the chain | CoinGecko's published figure |

The fee comparison is the interesting one, and it took two corrections to get honest.

First, extrapolating a per-block figure to a day needs the real block-production rate. Solana's nominal 400 ms slot implies 216,000 blocks a day, but slot time runs slightly long and a few slots are skipped, so mainnet lands nearer 205,000. Sentinel measures the rate from how far block height actually advances between runs rather than assuming it, which removes a systematic 5% overstatement. Until two runs far enough apart exist, the check is skipped rather than guessed.

Second, and more importantly, **the fee comparison does not raise alerts at all.** It was first judged against a 95% interval built from between-block variance, then against a 2x ratio band. Both were too tight. Successive live runs put our estimate at 0.63x, 0.73x, 0.90x and 2.19x of the same DeFiLlama figure, a 3.5x spread from sampling noise alone on a quantity that is heavy-tailed within a block and bursty across the day.

When an estimator's own noise is wider than the threshold you would alert on, alerting from it produces warnings that are arithmetically correct, fire regularly, and mean nothing, which is the same failure the anomaly engine's minimum-move rule exists to prevent. So the row is published as corroboration, labelled *indicative*, with a band wide enough to catch only a genuine order-of-magnitude disagreement. Price and circulating supply are precise quantities where a real gap is meaningful, so those do alert, on tight relative tolerances.

Divergences are raised as warnings in the same shape as anomalies, so they render through one code path in all three outputs.

## Measured on-chain activity (methodology)

No keyless daily-active-addresses feed exists any more: DeFiLlama discontinued theirs, and Solscan, Coin Metrics and Dune are all key-gated. So Sentinel measures activity itself.

- Each run samples 8 blocks spread evenly across the trailing 24 hours via `getBlock` and counts **unique non-vote fee payers per block**. The average is the **activity index**: a consistent, comparable proxy that tracks the direction of user activity and feeds anomaly detection.
- The overlap between samples goes into a Schnabel **capture-recapture** estimator. Because always-on actors (bots, market makers) dominate recaptures, this estimates a **persistently-active cohort**, not total daily actives, and is labeled that way everywhere it appears.

Both numbers, the per-block series, and the sample count are in the JSON output. The honest limitation: total chain-wide daily actives cannot be estimated to the right order of magnitude from sparse keyless sampling, so Sentinel reports what it can actually defend rather than a number that looks authoritative and is not.

## Repository layout

```
sentinel/               the collector: Python standard library only
  net.py                HTTP core: timeouts, retries, ETag, fallback chains
  collect_rpc.py        network + validator metrics via JSON-RPC
  collect_market.py     price data with a 4-source fallback chain
  collect_defi.py       TVL, stablecoins, DEX, fees, REV via DeFiLlama
  collect_dev.py        SIMDs + client releases via GitHub REST
  collect_news.py       RSS/Atom feeds via xml.etree
  collect_activity.py   block sampling, capture-recapture, xStocks, RWA
  collector.py          orchestration + per-source error isolation
  anomaly.py            MAD z-scores + absolute health rules
  crosscheck.py         independent-source agreement checks
  collect_onchain.py    program activity, clock drift, vote balances
  history.py            append-only JSONL metric history
  render_md.py          Markdown report
  fmt.py                shared formatting
  main.py               CLI: --once / --loop / --serve
dashboard/              the interactive dashboard (Vite + React + dither-kit)
  src/App.tsx           the dashboard itself
  src/components/       shell primitives + vendored dither-kit chart engine
tests/                  stdlib unittest suite (no network, no keys)
data/                   history.jsonl + latest.json, committed by the bot
docs/                   published outputs (GitHub Pages root)
samples/                example report.md / report.json
```

## Design choices

- **The collector takes no keys and no packages.** That was treated as a hard constraint: it runs on a fresh Python install behind any IP, which is what makes the 30-minute loop free and maintenance-free.
- **The dashboard is a real front end.** Charts come from [dither-kit](https://tripwire.sh/dither-kit), whose ordered-dither canvas engine renders the area, line and bar charts. The components are vendored into `src/components/dither-kit/`, so the app builds from source in the repo with no CDN and no runtime chart dependency. The trade-off is deliberate and worth stating plainly: the data pipeline stays dependency-free, the presentation layer does not.
- **Motion is used where it carries information, not for decoration.** Two pure-CSS recipes from [transitions.dev](https://transitions.dev/) are adapted in `src/index.css`: stat-tile digits pop in when a polled value actually changes (so a refresh that moves a number is visible, while an unchanged one stays still), and a skeleton matching the real layout holds the first load so the page does not jump when data lands. Both are plain keyframes toggled by a class, with no animation library, and both collapse under `prefers-reduced-motion`.
- **Data and presentation are decoupled.** The dashboard fetches `report.json` and `history.json` at runtime, so a data refresh never rebuilds the app, and the JSON report is a first-class output rather than a byproduct.
- **Fail soft, never blank.** Per-source isolation plus last-good degradation means a partial outage produces a complete report with a stale-section note instead of a broken page.

## License

MIT
