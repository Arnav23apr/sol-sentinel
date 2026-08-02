# Solana Ecosystem Report

*Generated 2026-08-02 21:43 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 10.8 robust standard deviations above its 7-day baseline (now 0.21 %, typical 0.14).
- 🔴 **DeFi TVL** (critical): DeFi TVL is 415.3 robust standard deviations above its 7-day baseline (now 4,755,944,251.00 USD, typical 4,749,940,154.00).

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.8K |
| TPS (non-vote) | 2.2K |
| Slot time | 428.6 ms |
| Slot | 437M |
| Block height | 415M |
| Epoch | 1011 (21.50% complete, ~40.4h remaining) |
| Lifetime transactions | 534.6B |
| Circulating supply | 581.2M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,273 lamports (about $0.00039) |
| Transaction fee p90 / p99 | 16,800 / 605,001 lamports |
| Paying base fee only | 27.50% of 5,528 sampled transactions |
| AMM write-lock congestion (150-slot window) | 8.00% of slots needed a priority fee (max 513.7K µlam/CU) |
| Node version (RPC) | 4.1.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 14 |
| Delinquent stake | 0.21% |
| Total active stake | 431.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.47% / 24.46% / 35.78% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.38% |

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
| SOL price | $73.71 (+3.40% 24h) |
| Market cap | $42.84B (rank #7) |
| 24h volume | $1.01B |
| ATH | $293.31 (-74.87% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.76B |
| Stablecoin supply | $15.68B |
| DEX volume (24h) | $1.30B (-23.14% 1d) |
| App fees (24h, all protocols) | $5.72M |
| Chain fees (24h) | $424.81K |
| Jito MEV tips (24h) | $88.68K |
| **REV - Real Economic Value (24h)** | **$513.49K** (chain fees + MEV tips) |

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
| Meteora DLMM | $171.60K |
| Jupiter Perpetual Exchange | $159.93K |
| fomo Wallet | $156.33K |
| Phantom Wallet | $137.88K |
| Jupiter Lend | $134.31K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 290 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $347.25M |
| xStocks 24h DEX volume | $3.27M |
| xStocks holders | 245.7K |
| Total RWA TVL on Solana | $1.76B |

Top tokenized equities: TSLAX ($58.67M), CRCLX ($45.64M), SPYX ($43.35M), MSTRX ($35.21M), QQQX ($29.83M)

## Program activity and chain health

Chain clock drift: **+15.9 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 52,287 (approx.) | 42.40% | 0.9 s |
| Pump.fun | 38,311 | 89.20% | 1.3 s |
| Jupiter v6 | 3,819 | 65.20% | 15.4 s |
| Orca Whirlpools | 1,682 | 51.20% | 35.6 s |
| Raydium AMM v4 | 626 | 28.20% | 94.7 s |

Median failure rate across the sampled programs: **51.20%** (range 28.20% to 89.20%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.24 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 431.54K USD | DeFiLlama: 424.81K USD | +1.57% | agree (95% CI 236K to 627K) |
| SOL price | coingecko: 73.71 USD | Jupiter (on-chain DEX): 73.96 USD | -0.34% | agree |
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
