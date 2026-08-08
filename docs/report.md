# Solana Ecosystem Report

*Generated 2026-08-08 21:19 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.8K |
| TPS (non-vote) | 2.2K |
| Slot time | 422.5 ms |
| Slot | 438M |
| Block height | 416M |
| Epoch | 1014 (4.61% complete, ~48.4h remaining) |
| Lifetime transactions | 536.3B |
| Circulating supply | 582.2M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,612 lamports (about $0.00043) |
| Transaction fee p90 / p99 | 22,187 / 962,639 lamports |
| Paying base fee only | 15.50% of 5,682 sampled transactions |
| AMM write-lock congestion (150-slot window) | 24.00% of slots needed a priority fee (max 4.3M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 691 |
| Delinquent validators | 7 |
| Delinquent stake | 0.01% |
| Total active stake | 434.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.39% / 35.74% |
| Commission (stake-weighted, delegatable validators) | 3.82% |
| Stake on private (100% commission) validators | 24.26% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 16.9M | 3.90% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.88% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.83% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $76.24 (+3.10% 24h) |
| Market cap | $44.38B (rank #7) |
| 24h volume | $1.42B |
| ATH | $293.31 (-74.01% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.82B |
| Stablecoin supply | $15.66B |
| DEX volume (24h) | $1.36B (-1.28% 1d) |
| App fees (24h, all protocols) | $8.15M |
| Chain fees (24h) | $552.24K |
| Jito MEV tips (24h) | $103.92K |
| **REV - Real Economic Value (24h)** | **$656.16K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.18B | +3.54% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.14B | +2.42% |
| USD1 | $1.04B | +1.74% |
| BUIDL | $712.22M | +5.52% |
| PYUSD | $684.08M | -0.30% |
| USDG | $633.71M | -2.62% |
| USDe | $538.89M | -0.41% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $396.73M |
| BisonFi | $147.36M |
| HumidiFi | $79.38M |
| Raydium AMM | $73.17M |
| pump.fun | $69.58M |
| Orca DEX | $69.43M |
| Meteora DLMM | $65.10M |
| Manifest Trade | $56.87M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.04M |
| pump.fun | $1.19M |
| Axiom | $916.99K |
| Meteora DLMM | $437.30K |
| fomo Wallet | $416.49K |
| Collector Crypt | $280.89K |
| Raydium AMM | $275.69K |
| Phantom Wallet | $196.22K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 256 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $375.79M |
| xStocks 24h DEX volume | $10.87M |
| xStocks holders | 259.6K |
| Total RWA TVL on Solana | $1.83B |

Top tokenized equities: TSLAX ($61.13M), CRCLX ($51.33M), SPYX ($43.46M), MSTRX ($38.21M), QQQX ($28.82M)

## Program activity and chain health

Chain clock drift: **+15.1 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 98,840 (approx.) | 40.00% | 0.4 s |
| Pump.fun | 64,615 (approx.) | 92.00% | 0.8 s |
| Raydium AMM v4 | 7,834 | 68.40% | 7.6 s |
| Jupiter v6 | 2,291 | 47.40% | 25.3 s |
| Orca Whirlpools | 1,128 | 71.50% | 52.8 s |

Median failure rate across the sampled programs: **68.40%** (range 40.00% to 92.00%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.25K SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 550.69K USD | DeFiLlama: 552.24K USD | -0.28% | agree (1.00x), *indicative* |
| SOL price | coingecko: 76.24 USD | Jupiter (on-chain DEX): 76.28 USD | -0.05% | agree |
| Circulating supply | getSupply (RPC): 582.17M SOL | CoinGecko: 582.17M SOL | -0.00% | agree |

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

**Latest Agave release:** [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07)

**Latest Firedancer release:** [v1.1.3](https://github.com/firedancer-io/firedancer/releases/tag/v1.1.3) (2026-08-04)

## Ecosystem news

- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Top 15 Best Solana RPC Providers (2026)](https://www.helius.dev/blog/top-solana-rpcs-helius-vs-other-node-providers)** - Helius, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29
- **[Setting Up Subscriptions and Recurring Payments on Solana](https://www.helius.dev/blog/solana-subscriptions-recurring-payments)** - Helius, 2026-07-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
