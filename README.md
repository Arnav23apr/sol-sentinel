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

**Validators and decentralization.** Active vs delinquent validator counts, delinquent stake percentage, total active stake, Nakamoto coefficient computed from the live stake distribution, top-5/10/20 stake concentration, the full cumulative stake curve, stake-weighted commission across delegatable validators, a commission histogram, the share of stake sitting on private 100%-commission validators, and a top-validators table.

**Economic indicators.** SOL price, 24h change, market cap and rank, 24h volume, distance from ATH, a 7-day price chart, stablecoin supply on Solana with a per-asset breakdown, daily DEX volume with a top-DEX table, app fees, and **REV (Real Economic Value): chain fees plus Jito MEV tips**, current and as a 90-day series.

**Ecosystem growth.** Tokenized equities (xStocks): AUM on Solana, per-ticker breakdown, 24h DEX volume and holder count; total RWA TVL with top protocols; and an on-chain activity index Sentinel measures itself (methodology below).

**Development and upgrades.** Open SIMD proposals, recently merged SIMDs, an upgrade watchlist flagging consensus/fee/Alpenglow-related proposals, and the latest Agave and Firedancer releases.

**News.** Latest items from solana.com news and the Helius engineering blog, plus Solana-filtered items from Decrypt and The Block.

## Data sources and integration

Priority went to direct, keyless sources. Each source is isolated: if one fails, its section degrades to the last good snapshot (flagged as stale in the report) and everything else stays fresh.

| Source | Transport | Used for |
|---|---|---|
| Solana JSON-RPC `api.mainnet-beta.solana.com` (fallback `solana-rpc.publicnode.com`) | `urllib` POST | getHealth, getVersion, getEpochInfo, getRecentPerformanceSamples, getSupply, getRecentPrioritizationFees, getVoteAccounts, getInflationRate, getInflationGovernor, getBlock (activity sampling) |
| DeFiLlama (`api.llama.fi`, `stablecoins.llama.fi`) | GET | TVL and history, stablecoin supply and per-asset breakdown, DEX volumes, fees, REV components (chain fees, Jito MEV tips), xStocks, RWA protocols |
| CoinGecko (fallbacks: Jupiter lite-api, Binance, Coinbase) | GET | SOL price, market cap, rank, volume, ATH, 7d chart. If every source carrying market cap fails, mcap is estimated as price x on-chain circulating supply and labeled as estimated |
| GitHub REST (unauthenticated) | GET | SIMD PRs, Agave and Firedancer releases (4 calls per run against the 60/hr anonymous limit) |
| RSS/Atom (solana.com, Helius, Decrypt, The Block) | GET + `xml.etree` | Ecosystem news |

Notes from building this: Ankr and dRPC have dropped keyless Solana RPC access; publicnode hangs on `getSupply`, so that one method never falls back; CoinGecko's keyless tier throttles bursts hard, so calls are spaced and every price value has a fallback chain; and `solana.com/data` renders its numbers client-side, so Sentinel reads the same underlying sources directly instead of scraping it.

## Automation strategy

Two GitHub Actions workflows, both committing back to `main`:

- [`update.yml`](.github/workflows/update.yml) runs every 30 minutes: checkout, run `python -m sentinel.main --once`, commit the refreshed `docs/` and `data/`. There is no dependency-install step because there are no dependencies.
- [`dashboard.yml`](.github/workflows/dashboard.yml) runs only when `dashboard/**` changes: `npm ci && npm run build`, which writes the built app into `docs/`.

Splitting them keeps the 30-minute loop to a bare Python run rather than a Node build. Both share a concurrency group so they never race on a push. GitHub Pages serves `docs/`, so the dashboard and both reports republish automatically with no servers and no cost. Commits made with the built-in `GITHUB_TOKEN` do not retrigger workflows, so there is no run recursion.

The metric history behind trends and anomaly baselines lives in [`data/history.jsonl`](data/history.jsonl), one compact row per run, capped at about 90 days. Because the workflow commits it back, the repository itself is the database: no external storage, and anyone who clones the repo gets the full history.

## Anomaly detection

Two layers run on every snapshot (see [`sentinel/anomaly.py`](sentinel/anomaly.py)):

1. **Robust statistical outliers.** Each watched metric (TPS, non-vote TPS, slot time, delinquent validators and stake, SOL price, TVL, stablecoin supply, DEX volume, fees, activity index) is compared to its rolling 7-day baseline using median absolute deviation. A MAD z-score at |z| >= 3.5 raises a warning and |z| >= 6 raises critical. MAD is used instead of mean and standard deviation so one bad sample from a free endpoint cannot poison the baseline. Direction is respected: TPS alerts only on drops, slot time and delinquency only on spikes, prices and volumes on both.
2. **Absolute health rules.** Thresholds that matter regardless of history: TPS below 1,000, slot time above 600 ms, delinquent stake above 5% (critical above 10%), and SOL moving more than 10% in 24h (critical at 20%).

A serious incident trips both layers at once (collapsing TPS is simultaneously a 100-sigma outlier and below the absolute floor), so findings are merged to one per metric, keeping the more severe and, on a tie, the threshold rule, whose wording says what the number means rather than how unusual it is. The surviving finding records that the other layer also fired.

Every finding carries its evidence (value, baseline median, z-score) into all three outputs, so an alert is always explainable.

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
