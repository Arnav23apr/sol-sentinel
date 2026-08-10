# Solana Ecosystem Report

*Generated 2026-08-10 12:42 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.9K |
| Slot time | 421.1 ms |
| Slot | 438M |
| Block height | 416M |
| Epoch | 1014 (82.29% complete, ~9.0h remaining) |
| Lifetime transactions | 536.8B |
| Circulating supply | 582.2M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 7,000 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 40,210 / 681,591 lamports |
| Paying base fee only | 14.50% of 8,474 sampled transactions |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 1.5M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 690 |
| Delinquent validators | 8 |
| Delinquent stake | 0.01% |
| Total active stake | 434.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.39% / 35.75% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 24.27% |

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
| SOL price | $76.67 (+0.80% 24h) |
| Market cap | $44.64B (rank #7) |
| 24h volume | $1.26B |
| ATH | $293.31 (-73.86% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.85B |
| Stablecoin supply | $15.59B |
| DEX volume (24h) | $1.35B (-9.76% 1d) |
| App fees (24h, all protocols) | $9.01M |
| Chain fees (24h) | $650.66K |
| Jito MEV tips (24h) | $142.01K |
| **REV - Real Economic Value (24h)** | **$792.67K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.13B | +4.23% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.14B | +2.42% |
| USD1 | $1.04B | +1.74% |
| BUIDL | $712.22M | +5.52% |
| PYUSD | $680.61M | -0.77% |
| USDG | $632.78M | -0.50% |
| USDe | $537.85M | -0.27% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $574.61M |
| BisonFi | $100.85M |
| Orca DEX | $92.66M |
| pump.fun | $82.75M |
| Raydium AMM | $80.35M |
| Meteora DLMM | $73.93M |
| Axiom | $73.37M |
| HumidiFi | $68.76M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.70M |
| pump.fun | $1.47M |
| Axiom | $1.35M |
| fomo Wallet | $444.26K |
| Meteora DLMM | $330.51K |
| Collector Crypt | $313.77K |
| Raydium AMM | $252.15K |
| Terminal | $177.24K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 324 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $375.36M |
| xStocks 24h DEX volume | $15.03M |
| xStocks holders | 258.6K |
| Total RWA TVL on Solana | $1.83B |

Top tokenized equities: TSLAX ($61.01M), CRCLX ($51.42M), SPYX ($43.39M), MSTRX ($37.81M), QQQX ($28.89M)

## Program activity and chain health

Chain clock drift: **+15.2 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 80,931 (approx.) | 44.10% | 0.4 s |
| Pump.fun | 58,490 (approx.) | 95.20% | 0.8 s |
| Jupiter v6 | 2,527 | 52.00% | 23.6 s |
| Raydium AMM v4 | 653 | 37.90% | 91 s |
| Orca Whirlpools | 496 | 37.40% | 120.9 s |

Median failure rate across the sampled programs: **44.10%** (range 37.40% to 95.20%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.26 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 842.96K USD | DeFiLlama: 650.66K USD | +25.75% | agree (1.30x), *indicative* |
| SOL price | coingecko: 76.67 USD | Jupiter (on-chain DEX): 76.72 USD | -0.07% | agree |
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
