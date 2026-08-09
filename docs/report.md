# Solana Ecosystem Report

*Generated 2026-08-09 17:02 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 2.6K |
| Slot time | 424 ms |
| Slot | 438M |
| Block height | 416M |
| Epoch | 1014 (43.54% complete, ~28.7h remaining) |
| Lifetime transactions | 536.6B |
| Circulating supply | 582.2M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,454 lamports (about $0.00042) |
| Transaction fee p90 / p99 | 19,199 / 605,000 lamports |
| Paying base fee only | 20.60% of 6,734 sampled transactions |
| AMM write-lock congestion (150-slot window) | 15.30% of slots needed a priority fee (max 4.2M µlam/CU) |
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
| SOL price | $77.25 (+1.20% 24h) |
| Market cap | $44.97B (rank #7) |
| 24h volume | $1.08B |
| ATH | $293.31 (-73.66% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.85B |
| Stablecoin supply | $15.67B |
| DEX volume (24h) | $1.49B (+9.69% 1d) |
| App fees (24h, all protocols) | $9.27M |
| Chain fees (24h) | $598.67K |
| Jito MEV tips (24h) | $124.68K |
| **REV - Real Economic Value (24h)** | **$723.35K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.20B | +4.36% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.14B | +2.42% |
| USD1 | $1.04B | +1.74% |
| BUIDL | $712.22M | +5.52% |
| PYUSD | $683.76M | -0.27% |
| USDG | $632.50M | -1.66% |
| USDe | $539.00M | -0.31% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $688.11M |
| BisonFi | $114.48M |
| pump.fun | $69.50M |
| HumidiFi | $64.28M |
| Meteora DLMM | $63.18M |
| Raydium AMM | $62.95M |
| Orca DEX | $59.23M |
| Axiom | $57.57M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.35M |
| pump.fun | $1.23M |
| Axiom | $1.05M |
| fomo Wallet | $440.87K |
| Collector Crypt | $437.24K |
| Sanctum Validator LSTs | $364.62K |
| Meteora DLMM | $303.39K |
| Binance Staked SOL | $228.17K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 326 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $369.91M |
| xStocks 24h DEX volume | $7.03M |
| xStocks holders | 258.5K |
| Total RWA TVL on Solana | $1.83B |

Top tokenized equities: TSLAX ($61.08M), CRCLX ($51.66M), SPYX ($43.51M), MSTRX ($38.69M), QQQX ($28.90M)

## Program activity and chain health

Chain clock drift: **+15.3 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 84,906 (approx.) | 41.00% | 0.4 s |
| Pump.fun | 18,235 | 78.70% | 3 s |
| Jupiter v6 | 3,642 | 50.60% | 16.1 s |
| Raydium AMM v4 | 2,195 | 41.40% | 26.7 s |
| Orca Whirlpools | 1,258 | 63.50% | 46.6 s |

Median failure rate across the sampled programs: **50.60%** (range 41.00% to 78.70%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **219.58 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 563.70K USD | DeFiLlama: 598.67K USD | -6.02% | agree (0.94x), *indicative* |
| SOL price | coingecko: 77.25 USD | Jupiter (on-chain DEX): 77.17 USD | +0.10% | agree |
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
