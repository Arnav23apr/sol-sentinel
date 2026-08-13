# Solana Ecosystem Report

*Generated 2026-08-13 03:05 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 38.7 robust standard deviations above its 7-day baseline: a 5744.4% move to 0.53 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 2.3K |
| Slot time | 418.1 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1016 (5.84% complete, ~47.2h remaining) |
| Lifetime transactions | 537.7B |
| Circulating supply | 582.6M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,346 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 21,000 / 409,159 lamports |
| Paying base fee only | 13.10% of 9,175 sampled transactions |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 1.2M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 686 |
| Delinquent validators | 11 |
| Delinquent stake | 0.53% |
| Total active stake | 432.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.50% / 24.57% / 35.98% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.35% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.69% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.89% | 5% |
| 4 | `3N7s…iD5g` | 12.4M | 2.86% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.08% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.92% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.71% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $75.91 (-0.70% 24h) |
| Market cap | $44.23B (rank #7) |
| 24h volume | $1.23B |
| ATH | $293.31 (-74.12% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.81B |
| Stablecoin supply | $15.49B |
| DEX volume (24h) | $1.68B (+2.01% 1d) |
| App fees (24h, all protocols) | $9.66M |
| Chain fees (24h) | $708.47K |
| Jito MEV tips (24h) | $141.72K |
| **REV - Real Economic Value (24h)** | **$850.18K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.73B | -3.81% |
| USDT | $2.96B | -6.33% |
| USDGO | $1.17B | +4.78% |
| USD1 | $1.05B | +2.92% |
| BUIDL | $740.62M | +8.04% |
| PYUSD | $673.33M | -0.74% |
| USDG | $640.76M | -1.79% |
| USDe | $537.83M | -0.14% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $556.46M |
| BisonFi | $189.81M |
| HumidiFi | $141.95M |
| Orca DEX | $116.59M |
| pump.fun | $88.50M |
| Meteora DLMM | $87.67M |
| Raydium AMM | $81.83M |
| Axiom | $68.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.45M |
| pump.fun | $1.53M |
| Axiom | $1.32M |
| Collector Crypt | $703.55K |
| fomo Wallet | $458.79K |
| Meteora DLMM | $361.58K |
| Raydium AMM | $229.44K |
| Terminal | $185.38K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 356 |
| Persistently-active cohort (capture-recapture est.) | 3.6K |
| Unique payers across sampled blocks | 2.1K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $377.02M |
| xStocks 24h DEX volume | $20.01M |
| xStocks holders | 263.2K |
| Total RWA TVL on Solana | $1.86B |

Top tokenized equities: TSLAX ($60.58M), CRCLX ($52.24M), SPYX ($44.31M), MSTRX ($37.48M), GOOGLX ($29.89M)

## Program activity and chain health

Chain clock drift: **+14.6 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 73,045 (approx.) | 38.50% | 0.4 s |
| Pump.fun | 47,453 | 85.50% | 1.3 s |
| Jupiter v6 | 2,850 | 56.70% | 20.9 s |
| Orca Whirlpools | 1,474 | 43.00% | 40.6 s |
| Raydium AMM v4 | 1,039 | 37.70% | 57.3 s |

Median failure rate across the sampled programs: **43.00%** (range 37.70% to 85.50%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.09K SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 464.06K USD | DeFiLlama: 708.47K USD | -41.69% | agree (0.66x), *indicative* |
| SOL price | coingecko: 75.91 USD | Jupiter (on-chain DEX): 75.93 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 582.61M SOL | CoinGecko: 582.61M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-06-24

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07)

**Latest Firedancer release:** [v26.08.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.0) (2026-08-12)

## Ecosystem news

- **[A Routing Bug Took Solana 86% of the Way to Losing Finality](https://decrypt.co/375404/a-routing-bug-took-solana-86-of-the-way-to-losing-finality)** - Decrypt, 2026-08-12
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[The Bull and Bear Case for Solana’s Next Price Move](https://decrypt.co/375364/solana-price-death-cross-bull-bear-case-next-move)** - Decrypt, 2026-08-11
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
