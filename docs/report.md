# Solana Ecosystem Report

*Generated 2026-08-10 23:03 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.4 robust standard deviations above its 7-day baseline: a 657.1% move to 0.05 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.9K |
| Slot time | 418.1 ms |
| Slot | 438M |
| Block height | 417M |
| Epoch | 1015 (2.71% complete, ~48.8h remaining) |
| Lifetime transactions | 537.0B |
| Circulating supply | 582.3M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,372 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 21,133 / 505,000 lamports |
| Paying base fee only | 18.60% of 7,461 sampled transactions |
| AMM write-lock congestion (150-slot window) | 16.00% of slots needed a priority fee (max 5.4M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 690 |
| Delinquent validators | 8 |
| Delinquent stake | 0.05% |
| Total active stake | 434.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.38% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.23% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $76.15 (-1.60% 24h) |
| Market cap | $44.34B (rank #7) |
| 24h volume | $1.44B |
| ATH | $293.31 (-74.04% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.83B |
| Stablecoin supply | $15.53B |
| DEX volume (24h) | $1.35B (-9.76% 1d) |
| App fees (24h, all protocols) | $9.15M |
| Chain fees (24h) | $650.66K |
| Jito MEV tips (24h) | $140.00K |
| **REV - Real Economic Value (24h)** | **$790.67K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.04B | +2.92% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.14B | +2.42% |
| USD1 | $1.04B | +2.08% |
| BUIDL | $712.85M | +5.61% |
| PYUSD | $679.60M | -0.98% |
| USDG | $644.91M | +1.43% |
| USDe | $537.62M | -0.36% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $574.61M |
| Orca DEX | $139.36M |
| BisonFi | $100.85M |
| Raydium AMM | $99.74M |
| Meteora DLMM | $99.70M |
| pump.fun | $82.75M |
| Manifest Trade | $75.76M |
| Axiom | $73.37M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.70M |
| pump.fun | $1.47M |
| Axiom | $1.35M |
| fomo Wallet | $444.27K |
| Meteora DLMM | $406.29K |
| Raydium AMM | $339.43K |
| Collector Crypt | $307.52K |
| Terminal | $177.24K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 329 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $371.52M |
| xStocks 24h DEX volume | $23.44M |
| xStocks holders | 259.5K |
| Total RWA TVL on Solana | $1.83B |

Top tokenized equities: TSLAX ($61.06M), CRCLX ($50.49M), SPYX ($43.64M), MSTRX ($37.14M), QQQX ($28.69M)

## Program activity and chain health

Chain clock drift: **+14.8 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,934 | 22.90% | 1.3 s |
| Pump.fun | 21,598 | 88.20% | 2.5 s |
| Jupiter v6 | 2,048 | 44.30% | 29.3 s |
| Orca Whirlpools | 703 | 56.50% | 84.9 s |
| Raydium AMM v4 | 683 | 44.10% | 86.1 s |

Median failure rate across the sampled programs: **44.30%** (range 22.90% to 88.20%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.02K SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 454.11K USD | DeFiLlama: 650.66K USD | -35.58% | agree (0.70x), *indicative* |
| SOL price | coingecko: 76.15 USD | Jupiter (on-chain DEX): 76.06 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 582.28M SOL | CoinGecko: 582.28M SOL | -0.00% | agree |

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
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29
- **[Setting Up Subscriptions and Recurring Payments on Solana](https://www.helius.dev/blog/solana-subscriptions-recurring-payments)** - Helius, 2026-07-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
