# Solana Ecosystem Report

*Generated 2026-08-07 19:43 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 2.1K |
| Slot time | 419.6 ms |
| Slot | 438M |
| Block height | 416M |
| Epoch | 1013 (54.13% complete, ~23.1h remaining) |
| Lifetime transactions | 536.0B |
| Circulating supply | 582.1M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,412 lamports (about $0.00040) |
| Transaction fee p90 / p99 | 25,000 / 562,749 lamports |
| Paying base fee only | 16.70% of 6,288 sampled transactions |
| AMM write-lock congestion (150-slot window) | 18.70% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 692 |
| Delinquent validators | 8 |
| Delinquent stake | 0.03% |
| Total active stake | 434.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.36% / 24.37% / 35.68% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.22% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 16.9M | 3.88% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 5 | `26pV…3dJx` | 9.1M | 2.10% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.04% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.82% | 7% |
| 9 | `CvSb…wycB` | 7.6M | 1.76% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $73.80 (+0.40% 24h) |
| Market cap | $42.95B (rank #7) |
| 24h volume | $1.54B |
| ATH | $293.31 (-74.84% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.73B |
| Stablecoin supply | $15.59B |
| DEX volume (24h) | $1.38B (-15.75% 1d) |
| App fees (24h, all protocols) | $8.98M |
| Chain fees (24h) | $516.12K |
| Jito MEV tips (24h) | $110.97K |
| **REV - Real Economic Value (24h)** | **$627.10K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.12B | +2.17% |
| USDT | $2.96B | -12.42% |
| USDGO | $1.14B | +4.30% |
| USD1 | $1.04B | +1.74% |
| BUIDL | $697.16M | +6.62% |
| PYUSD | $670.83M | -1.62% |
| USDG | $649.07M | +2.35% |
| USDe | $538.92M | +0.28% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $560.33M |
| BisonFi | $115.36M |
| Orca DEX | $106.02M |
| Raydium AMM | $88.36M |
| Meteora DLMM | $77.19M |
| pump.fun | $68.21M |
| Manifest Trade | $67.48M |
| Axiom | $51.82M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.87M |
| pump.fun | $1.17M |
| Axiom | $911.99K |
| fomo Wallet | $577.29K |
| Raydium AMM | $424.18K |
| Sanctum Validator LSTs | $351.73K |
| Meteora DLMM | $328.01K |
| Collector Crypt | $250.97K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 292 |
| Persistently-active cohort (capture-recapture est.) | 2.8K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $372.57M |
| xStocks 24h DEX volume | $26.95M |
| xStocks holders | 257.4K |
| Total RWA TVL on Solana | $1.81B |

Top tokenized equities: TSLAX ($60.46M), CRCLX ($51.03M), SPYX ($43.23M), MSTRX ($37.07M), QQQX ($28.74M)

## Program activity and chain health

Chain clock drift: **+15.1 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 100,238 (approx.) | 95.70% | 0.4 s |
| SPL Token | 45,472 (approx.) | 54.10% | 0.8 s |
| Jupiter v6 | 4,906 | 61.50% | 12.2 s |
| Orca Whirlpools | 1,478 | 28.60% | 39.9 s |
| Raydium AMM v4 | 1,108 | 34.20% | 53.7 s |

Median failure rate across the sampled programs: **54.10%** (range 28.60% to 95.70%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.25 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 382.27K USD | DeFiLlama: 516.12K USD | -29.80% | agree (0.74x), *indicative* |
| SOL price | coingecko: 73.80 USD | Jupiter (on-chain DEX): 73.77 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 582.05M SOL | CoinGecko: 582.05M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-07-20

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-06-24

**Recently merged SIMDs:**

- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-07-23
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-07-20
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.3.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-alpha.3) (2026-08-05)

**Latest Firedancer release:** [v1.1.3](https://github.com/firedancer-io/firedancer/releases/tag/v1.1.3) (2026-08-04)

## Ecosystem news

- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[JPMorgan says Hyperliquid faces growing competition while HYPE ETF inflows stall](https://www.theblock.co/news/markets/2026-08-06-jpmorgan-hyperliquid-competition-hype-etf-inflows-stall-411001?utm_source=rss&utm_medium=rss)** - The Block, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Top 15 Best Solana RPC Providers (2026)](https://www.helius.dev/blog/top-solana-rpcs-helius-vs-other-node-providers)** - Helius, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
