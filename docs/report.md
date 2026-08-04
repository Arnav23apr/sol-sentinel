# Solana Ecosystem Report

*Generated 2026-08-04 11:36 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 9.5 robust standard deviations above its 7-day baseline: a 28.3% move to 1,703,017,065.00 USD from a typical 1,327,543,713.00.
- 🔴 **Network fees (24h)** (critical): Network fees (24h) is 36.4 robust standard deviations above its 7-day baseline: a 44.3% move to 8,321,864.00 USD from a typical 5,767,298.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.7K |
| Slot time | 421.1 ms |
| Slot | 437M |
| Block height | 415M |
| Epoch | 1011 (96.20% complete, ~1.9h remaining) |
| Lifetime transactions | 535.0B |
| Circulating supply | 581.2M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,478 lamports (about $0.00040) |
| Transaction fee p90 / p99 | 22,693 / 672,500 lamports |
| Paying base fee only | 21.90% of 5,289 sampled transactions |
| AMM write-lock congestion (150-slot window) | 18.00% of slots needed a priority fee (max 1.4M µlam/CU) |
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
| SOL price | $73.63 (+1.30% 24h) |
| Market cap | $42.79B (rank #7) |
| 24h volume | $1.45B |
| ATH | $293.31 (-74.90% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.75B |
| Stablecoin supply | $15.83B |
| DEX volume (24h) | $1.70B (+26.84% 1d) |
| App fees (24h, all protocols) | $8.32M |
| Chain fees (24h) | $614.78K |
| Jito MEV tips (24h) | $143.66K |
| **REV - Real Economic Value (24h)** | **$758.44K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.03B | -10.35% |
| USDT | $3.35B | -0.59% |
| USDGO | $1.11B | -0.00% |
| USD1 | $1.02B | +0.03% |
| PYUSD | $679.22M | -2.19% |
| BUIDL | $675.66M | +3.29% |
| USDG | $649.65M | +1.63% |
| USDe | $538.83M | +0.33% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $731.06M |
| BisonFi | $134.69M |
| Orca DEX | $126.14M |
| Meteora DLMM | $82.96M |
| GoonFi | $79.60M |
| Manifest Trade | $75.22M |
| Raydium AMM | $72.71M |
| pump.fun | $70.54M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.27M |
| pump.fun | $1.26M |
| Axiom | $1.11M |
| Collector Crypt | $722.72K |
| fomo Wallet | $303.49K |
| Phantom Wallet | $232.04K |
| Meteora DLMM | $220.35K |
| Raydium AMM | $193.58K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 286 |
| Persistently-active cohort (capture-recapture est.) | 3.2K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $359.56M |
| xStocks 24h DEX volume | $23.53M |
| xStocks holders | 248.7K |
| Total RWA TVL on Solana | $1.77B |

Top tokenized equities: TSLAX ($60.44M), CRCLX ($45.05M), SPYX ($43.48M), MSTRX ($35.20M), QQQX ($30.50M)

## Program activity and chain health

Chain clock drift: **+14.4 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 38,233 | 29.60% | 1.3 s |
| Pump.fun | 26,303 | 88.70% | 2.1 s |
| Jupiter v6 | 2,365 | 51.10% | 25.3 s |
| Orca Whirlpools | 750 | 25.50% | 79.6 s |
| Raydium AMM v4 | 684 | 38.40% | 87.6 s |

Median failure rate across the sampled programs: **38.40%** (range 25.50% to 88.70%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.24 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 532.69K USD | DeFiLlama: 614.78K USD | -14.31% | agree (0.87x), *indicative* |
| SOL price | coingecko: 73.63 USD | Jupiter (on-chain DEX): 73.62 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 581.19M SOL | CoinGecko: 581.19M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-07-20

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-03
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-03
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

- **[Marmot Researchers Turn to OnlyFans for Funding—And There Are Meme Coins Too](https://decrypt.co/374874/marmot-researchers-onlyfans-memecoins-solana-onlymarms)** - Decrypt, 2026-08-03
- **[BlackRock Launches Tokenized Money Market Funds on Solana, Ethereum](https://decrypt.co/374865/blackrock-tokenized-money-market-funds-solana-ethereum)** - Decrypt, 2026-08-03
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29
- **[Setting Up Subscriptions and Recurring Payments on Solana](https://www.helius.dev/blog/solana-subscriptions-recurring-payments)** - Helius, 2026-07-24
- **[Solana Changelog: July 23, 2026](https://solana.com/news/solana-changelog-july-23-2026)** - Solana.com, 2026-07-23
- **[Deploying enterprise stablecoin rails on Solana in days with Crossmint](https://solana.com/news/case-study-crossmint)** - Solana.com, 2026-07-23
- **[Rent Reduction on Solana: A Data-Backed Analysis](https://solana.com/news/rent-reduction-deep-dive)** - Solana.com, 2026-07-20

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
