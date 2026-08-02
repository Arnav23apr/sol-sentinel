# Solana Ecosystem Report

*Generated 2026-08-02 21:31 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 2.1K |
| Slot time | 419.6 ms |
| Slot | 437M |
| Block height | 415M |
| Epoch | 1011 (21.10% complete, ~39.7h remaining) |
| Lifetime transactions | 534.5B |
| Circulating supply | 581.2M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,556 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 25,000 / 510,000 lamports |
| Paying base fee only | 22.10% of 5,279 sampled transactions |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 38.5M µlam/CU) |
| Node version (RPC) | 4.1.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 690 |
| Delinquent validators | 13 |
| Delinquent stake | 0.14% |
| Total active stake | 432.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.46% / 24.45% / 35.76% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.37% |

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
| SOL price | $73.72 (+3.40% 24h) |
| Market cap | $42.85B (rank #7) |
| 24h volume | $1.01B |
| ATH | $293.31 (-74.87% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.75B |
| Stablecoin supply | $15.68B |
| DEX volume (24h) | $1.30B (-23.14% 1d) |
| App fees (24h, all protocols) | $5.72M |
| Chain fees (24h) | $424.81K |
| Jito MEV tips (24h) | $88.87K |
| **REV - Real Economic Value (24h)** | **$513.68K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.88B | -10.51% |
| USDT | $3.35B | +0.90% |
| USDGO | $1.11B | +0.45% |
| USD1 | $1.02B | -0.00% |
| PYUSD | $685.94M | +0.83% |
| BUIDL | $674.96M | +3.23% |
| USDG | $636.27M | +2.37% |
| USDe | $539.43M | +0.42% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $642.34M |
| Orca DEX | $68.21M |
| BisonFi | $63.19M |
| pump.fun | $61.18M |
| GoonFi | $59.95M |
| Manifest Trade | $58.75M |
| Meteora DLMM | $58.09M |
| Axiom | $41.95M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.45M |
| pump.fun | $1.01M |
| Axiom | $749.63K |
| Jupiter Perpetual Exchange | $159.93K |
| fomo Wallet | $156.33K |
| Meteora DLMM | $155.02K |
| Phantom Wallet | $137.88K |
| Jupiter Lend | $134.31K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 272 |
| Persistently-active cohort (capture-recapture est.) | 2.9K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $347.55M |
| xStocks 24h DEX volume | $3.13M |
| xStocks holders | 245.7K |
| Total RWA TVL on Solana | $1.76B |

Top tokenized equities: TSLAX ($58.67M), CRCLX ($45.79M), SPYX ($43.37M), MSTRX ($35.22M), QQQX ($29.85M)

## Program activity and chain health

Chain clock drift: **+15.7 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 50,262 (approx.) | 37.60% | 0.8 s |
| Pump.fun | 32,781 | 90.90% | 1.7 s |
| Jupiter v6 | 3,230 | 57.80% | 18.5 s |
| Raydium AMM v4 | 1,059 | 52.30% | 55.8 s |
| Orca Whirlpools | 917 | 69.80% | 65 s |

Median failure rate across the sampled programs: **57.80%** (range 37.60% to 90.90%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.24 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 332.12K USD | DeFiLlama: 424.81K USD | -24.49% | agree (95% CI 235K to 430K) |
| SOL price | coingecko: 73.72 USD | Jupiter (on-chain DEX): 73.72 USD | 0.00% | agree |
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
