# Solana Ecosystem Report

*Generated 2026-08-14 00:04 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.8K |
| Slot time | 416.7 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1016 (47.77% complete, ~26.1h remaining) |
| Lifetime transactions | 537.9B |
| Circulating supply | 582.6M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,412 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 26,318 / 605,000 lamports |
| Paying base fee only | 16.40% of 6,651 sampled transactions |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 26.2M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 688 |
| Delinquent validators | 9 |
| Delinquent stake | 0.01% |
| Total active stake | 434.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.42% / 24.44% / 35.79% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.23% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.4M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $76.24 (+1.00% 24h) |
| Market cap | $44.42B (rank #7) |
| 24h volume | $1.16B |
| ATH | $293.31 (-74.01% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.85B |
| Stablecoin supply | $15.52B |
| DEX volume (24h) | $1.73B (+4.53% 1d) |
| App fees (24h, all protocols) | $9.67M |
| Chain fees (24h) | $708.47K |
| Jito MEV tips (24h) | $129.82K |
| **REV - Real Economic Value (24h)** | **$838.28K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.77B | -3.33% |
| USDT | $2.96B | -6.33% |
| USDGO | $1.17B | +4.78% |
| USD1 | $1.05B | +2.92% |
| BUIDL | $740.89M | +8.08% |
| PYUSD | $677.34M | -0.16% |
| USDG | $636.26M | -2.44% |
| USDe | $538.08M | -0.08% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $556.46M |
| BisonFi | $189.81M |
| HumidiFi | $141.95M |
| Orca DEX | $110.83M |
| Aquifer | $98.35M |
| pump.fun | $88.50M |
| Raydium AMM | $86.11M |
| Meteora DLMM | $76.62M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.45M |
| pump.fun | $1.53M |
| Axiom | $1.32M |
| fomo Wallet | $401.53K |
| Collector Crypt | $343.63K |
| Meteora DLMM | $282.58K |
| Raydium AMM | $222.86K |
| Terminal | $186.60K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 294 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $383.93M |
| xStocks 24h DEX volume | $19.49M |
| xStocks holders | 265.3K |
| Total RWA TVL on Solana | $1.87B |

Top tokenized equities: TSLAX ($62.61M), CRCLX ($55.23M), SPYX ($44.15M), MSTRX ($38.07M), GOOGLX ($30.28M)

## Program activity and chain health

Chain clock drift: **+14.0 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 44,060 | 22.80% | 1.3 s |
| Pump.fun | 32,829 | 90.50% | 1.3 s |
| Jupiter v6 | 2,413 | 53.50% | 19.2 s |
| Raydium AMM v4 | 1,005 | 27.70% | 59.6 s |
| Orca Whirlpools | 616 | 50.60% | 96.7 s |

Median failure rate across the sampled programs: **50.60%** (range 22.80% to 90.50%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.27 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 452.20K USD | DeFiLlama: 708.47K USD | -44.16% | agree (0.64x), *indicative* |
| SOL price | coingecko: 76.24 USD | Jupiter (on-chain DEX): 76.22 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 582.61M SOL | CoinGecko: 582.61M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-06-24
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-08-03

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) (2026-08-13)

**Latest Firedancer release:** [v26.08.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.0) (2026-08-12)

## Ecosystem news

- **[Solana Can Be the 'Everything Chain' as Crypto Apps Go Mainstream: 6th Man Ventures Co-Founder](https://decrypt.co/375605/solana-everything-chain-crypto-apps-mainstream)** - Decrypt, 2026-08-13
- **[A Routing Bug Took Solana 86% of the Way to Losing Finality](https://decrypt.co/375404/a-routing-bug-took-solana-86-of-the-way-to-losing-finality)** - Decrypt, 2026-08-12
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[The Bull and Bear Case for Solana’s Next Price Move](https://decrypt.co/375364/solana-price-death-cross-bull-bear-case-next-move)** - Decrypt, 2026-08-11
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
