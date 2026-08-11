# Solana Ecosystem Report

*Generated 2026-08-11 03:14 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.7K |
| Slot time | 419.6 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1015 (10.98% complete, ~44.8h remaining) |
| Lifetime transactions | 537.0B |
| Circulating supply | 582.5M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,507 lamports (about $0.00042) |
| Transaction fee p90 / p99 | 25,001 / 605,000 lamports |
| Paying base fee only | 18.60% of 4,518 sampled transactions |
| AMM write-lock congestion (150-slot window) | 15.30% of slots needed a priority fee (max 27.4M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 691 |
| Delinquent validators | 7 |
| Delinquent stake | 0.01% |
| Total active stake | 434.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.37% / 35.70% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.22% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.67% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $76.12 (-0.90% 24h) |
| Market cap | $44.34B (rank #7) |
| 24h volume | $1.35B |
| ATH | $293.31 (-74.05% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.82B |
| Stablecoin supply | $15.50B |
| DEX volume (24h) | $1.55B (+14.77% 1d) |
| App fees (24h, all protocols) | $10.45M |
| Chain fees (24h) | $680.55K |
| Jito MEV tips (24h) | $137.96K |
| **REV - Real Economic Value (24h)** | **$818.51K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.00B | -0.09% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.14B | +2.43% |
| USD1 | $1.04B | +2.05% |
| BUIDL | $712.85M | +5.50% |
| PYUSD | $689.16M | +0.10% |
| USDG | $646.87M | +0.46% |
| USDe | $537.32M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $335.38M |
| BisonFi | $216.14M |
| HumidiFi | $161.21M |
| Orca DEX | $132.21M |
| Raydium AMM | $100.74M |
| Meteora DLMM | $94.44M |
| pump.fun | $86.05M |
| Manifest Trade | $74.64M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.49M |
| pump.fun | $1.43M |
| Axiom | $1.18M |
| fomo Wallet | $444.27K |
| Meteora DLMM | $380.61K |
| Raydium AMM | $377.32K |
| Collector Crypt | $371.59K |
| Sanctum Validator LSTs | $365.15K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 250 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $370.94M |
| xStocks 24h DEX volume | $23.54M |
| xStocks holders | 259.8K |
| Total RWA TVL on Solana | $1.83B |

Top tokenized equities: TSLAX ($60.92M), CRCLX ($50.59M), SPYX ($43.71M), MSTRX ($37.05M), QQQX ($28.76M)

## Program activity and chain health

Chain clock drift: **+14.9 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 54,266 (approx.) | 33.60% | 0.8 s |
| Pump.fun | 14,697 | 88.60% | 3.8 s |
| Jupiter v6 | 1,649 | 37.80% | 36.1 s |
| Raydium AMM v4 | 978 | 36.20% | 61.3 s |
| Orca Whirlpools | 944 | 63.00% | 63.4 s |

Median failure rate across the sampled programs: **37.80%** (range 33.60% to 88.60%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.05K SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 351.45K USD | DeFiLlama: 680.55K USD | -63.78% | agree (0.52x), *indicative* |
| SOL price | coingecko: 76.12 USD | Jupiter (on-chain DEX): 76.04 USD | +0.11% | agree |
| Circulating supply | getSupply (RPC): 582.48M SOL | CoinGecko: 582.48M SOL | -0.00% | agree |

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

**Latest Firedancer release:** [v1.1.4](https://github.com/firedancer-io/firedancer/releases/tag/v1.1.4) (2026-08-10)

## Ecosystem news

- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Top 15 Best Solana RPC Providers (2026)](https://www.helius.dev/blog/top-solana-rpcs-helius-vs-other-node-providers)** - Helius, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-01
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
