# Solana Ecosystem Report

*Generated 2026-08-03 09:00 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Chain fees (24h): sources disagree** (warning): sampled blocks (RPC) reports 1,079,375 USD while DeFiLlama reports 422,077 USD, a 2.56x ratio, outside the 2x band two independent measurements of this quantity should stay within. Treat this figure as uncertain until they reconverge.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.8K |
| TPS (non-vote) | 1.2K |
| Slot time | 421.1 ms |
| Slot | 437M |
| Block height | 415M |
| Epoch | 1011 (43.80% complete, ~28.4h remaining) |
| Lifetime transactions | 534.7B |
| Circulating supply | 581.2M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,412 lamports (about $0.00039) |
| Transaction fee p90 / p99 | 25,000 / 848,653 lamports |
| Paying base fee only | 25.50% of 4,816 sampled transactions |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 2.2M µlam/CU) |
| Node version (RPC) | 4.1.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 690 |
| Delinquent validators | 13 |
| Delinquent stake | 0.13% |
| Total active stake | 432.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.45% / 24.44% / 35.76% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 24.36% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 16.8M | 3.89% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.71% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.90% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.8M | 2.04% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.89% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.54% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $72.30 (-1.30% 24h) |
| Market cap | $42.02B (rank #7) |
| 24h volume | $991.04M |
| ATH | $293.31 (-75.35% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.72B |
| Stablecoin supply | $15.71B |
| DEX volume (24h) | $1.33B (+2.06% 1d) |
| App fees (24h, all protocols) | $6.89M |
| Chain fees (24h) | $422.08K |
| Jito MEV tips (24h) | $107.67K |
| **REV - Real Economic Value (24h)** | **$529.75K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.93B | -8.95% |
| USDT | $3.35B | +0.90% |
| USDGO | $1.11B | +0.45% |
| USD1 | $1.02B | -0.00% |
| PYUSD | $676.64M | -0.79% |
| BUIDL | $674.96M | +3.23% |
| USDG | $634.50M | +2.54% |
| USDe | $538.95M | +0.41% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $620.18M |
| BisonFi | $89.33M |
| Orca DEX | $75.13M |
| Meteora DLMM | $63.28M |
| GoonFi | $59.95M |
| pump.fun | $55.12M |
| Manifest Trade | $53.97M |
| Raydium AMM | $46.37M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.72M |
| pump.fun | $985.26K |
| Axiom | $753.44K |
| Sanctum Validator LSTs | $353.14K |
| Binance Staked SOL | $221.75K |
| Jito Liquid Staking | $211.44K |
| Meteora DLMM | $181.07K |
| fomo Wallet | $156.33K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 272 |
| Persistently-active cohort (capture-recapture est.) | 3.2K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $357.41M |
| xStocks 24h DEX volume | $8.98M |
| xStocks holders | 245.9K |
| Total RWA TVL on Solana | $1.77B |

Top tokenized equities: TSLAX ($58.81M), CRCLX ($46.12M), SPYX ($43.47M), MSTRX ($34.51M), QQQX ($29.89M)

## Program activity and chain health

Chain clock drift: **+14.1 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,141 | 31.80% | 1.3 s |
| Pump.fun | 6,399 | 87.10% | 9.3 s |
| Jupiter v6 | 2,124 | 49.90% | 27 s |
| Orca Whirlpools | 808 | 49.10% | 74.1 s |
| Raydium AMM v4 | 354 | 36.50% | 169.3 s |

Median failure rate across the sampled programs: **49.10%** (range 31.80% to 87.10%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **50.24 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 3 agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 1.08M USD | DeFiLlama: 422.08K USD | +87.55% | **diverge** (95% CI 0 to 3M) |
| SOL price | coingecko: 72.30 USD | Jupiter (on-chain DEX): 72.27 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 581.19M SOL | CoinGecko: 581.19M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-07-20

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-07-31
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-07-30
- [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-06-24

**Recently merged SIMDs:**

- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-07-23
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-07-20
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) (2026-07-31)

**Latest Firedancer release:** [v0.1104.40200](https://github.com/firedancer-io/firedancer/releases/tag/v0.1104.40200) (2026-07-30)

## Ecosystem news

- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29
- **[Setting Up Subscriptions and Recurring Payments on Solana](https://www.helius.dev/blog/solana-subscriptions-recurring-payments)** - Helius, 2026-07-24
- **[Solana Changelog: July 23, 2026](https://solana.com/news/solana-changelog-july-23-2026)** - Solana.com, 2026-07-23
- **[Deploying enterprise stablecoin rails on Solana in days with Crossmint](https://solana.com/news/case-study-crossmint)** - Solana.com, 2026-07-23
- **[Rent Reduction on Solana: A Data-Backed Analysis](https://solana.com/news/rent-reduction-deep-dive)** - Solana.com, 2026-07-20
- **[Solana Changelog: July 16, 2026](https://solana.com/news/solana-changelog-july-16-2026)** - Solana.com, 2026-07-16
- **[The Sun Rises in Seoul and Trades on Solana: $SKHY is Now Live](https://solana.com/news/skhy-is-now-live)** - Solana.com, 2026-07-10
- **[What is RocksDB? The Embedded Key-Value Store](https://www.helius.dev/blog/what-is-rocksdb)** - Helius, 2026-07-09

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
