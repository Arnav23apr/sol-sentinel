# Solana Ecosystem Report

*Generated 2026-08-05 20:55 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 6.5 robust standard deviations above its 7-day baseline: a 30.2% move to 1,747,556,148.00 USD from a typical 1,342,682,593.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 2.6K |
| Slot time | 422.6 ms |
| Slot | 437M |
| Block height | 416M |
| Epoch | 1012 (61.81% complete, ~19.4h remaining) |
| Lifetime transactions | 535.4B |
| Circulating supply | 581.3M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,500 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 17,800 / 1,005,000 lamports |
| Paying base fee only | 19.70% of 6,194 sampled transactions |
| AMM write-lock congestion (150-slot window) | 21.30% of slots needed a priority fee (max 2.9M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 691 |
| Delinquent validators | 8 |
| Delinquent stake | 0.01% |
| Total active stake | 434.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.36% / 24.35% / 35.62% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.24% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 16.8M | 3.87% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.8M | 2.03% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.82% | 7% |
| 9 | `CvSb…wycB` | 7.5M | 1.72% | 5% |
| 10 | `Dumi…Zk4a` | 6.7M | 1.53% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $74.37 (+0.50% 24h) |
| Market cap | $43.23B (rank #7) |
| 24h volume | $1.67B |
| ATH | $293.31 (-74.64% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.81B |
| Stablecoin supply | $15.62B |
| DEX volume (24h) | $1.75B (+2.04% 1d) |
| App fees (24h, all protocols) | $10.23M |
| Chain fees (24h) | $614.00K |
| Jito MEV tips (24h) | $123.03K |
| **REV - Real Economic Value (24h)** | **$737.02K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.00B | +4.22% |
| USDT | $3.16B | -8.14% |
| USDGO | $1.12B | +0.99% |
| USD1 | $1.02B | +0.03% |
| PYUSD | $679.75M | -1.98% |
| BUIDL | $676.56M | +3.38% |
| USDG | $654.22M | +3.07% |
| USDe | $538.95M | +0.43% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $658.51M |
| BisonFi | $140.51M |
| Orca DEX | $138.32M |
| Meteora DLMM | $90.56M |
| Manifest Trade | $89.64M |
| Raydium AMM | $87.34M |
| GoonFi | $84.28M |
| pump.fun | $78.45M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.25M |
| pump.fun | $1.36M |
| Axiom | $1.12M |
| Pyth Pro | $500.58K |
| fomo Wallet | $466.21K |
| Sanctum Validator LSTs | $359.30K |
| Meteora DLMM | $324.58K |
| Collector Crypt | $285.01K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 296 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $368.36M |
| xStocks 24h DEX volume | $36.53M |
| xStocks holders | 251.3K |
| Total RWA TVL on Solana | $1.80B |

Top tokenized equities: TSLAX ($60.00M), CRCLX ($48.17M), SPYX ($43.79M), MSTRX ($37.06M), QQQX ($29.07M)

## Program activity and chain health

Chain clock drift: **+15.8 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 87,743 (approx.) | 96.70% | 0.4 s |
| SPL Token | 55,372 (approx.) | 28.00% | 0.8 s |
| Raydium AMM v4 | 2,843 | 69.00% | 20.3 s |
| Jupiter v6 | 2,472 | 55.40% | 23.7 s |
| Orca Whirlpools | 1,149 | 57.40% | 52 s |

Median failure rate across the sampled programs: **57.40%** (range 28.00% to 96.70%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.24 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 1.82M USD | DeFiLlama: 614.00K USD | +99.21% | agree (2.97x), *indicative* |
| SOL price | coingecko: 74.37 USD | Jupiter (on-chain DEX): 74.33 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 581.31M SOL | CoinGecko: 581.31M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-07-20

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-03
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

- **[Top 15 Best Solana RPC Providers (2026)](https://www.helius.dev/blog/top-solana-rpcs-helius-vs-other-node-providers)** - Helius, 2026-08-04
- **[Solana Proposal Would Increase Daily SOL Burns More Than 10-Fold](https://decrypt.co/374915/solana-proposal-increase-daily-sol-burns-10-fold)** - Decrypt, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Marmot Researchers Turn to OnlyFans for Funding—And There Are Meme Coins Too](https://decrypt.co/374874/marmot-researchers-onlyfans-memecoins-solana-onlymarms)** - Decrypt, 2026-08-03
- **[BlackRock Launches Tokenized Money Market Funds on Solana, Ethereum](https://decrypt.co/374865/blackrock-tokenized-money-market-funds-solana-ethereum)** - Decrypt, 2026-08-03
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29
- **[Setting Up Subscriptions and Recurring Payments on Solana](https://www.helius.dev/blog/solana-subscriptions-recurring-payments)** - Helius, 2026-07-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
