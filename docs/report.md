# Solana Ecosystem Report

*Generated 2026-08-04 20:06 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Network fees (24h)** (critical): Network fees (24h) is 37.6 robust standard deviations above its 7-day baseline: a 45.8% move to 8,405,853.00 USD from a typical 5,767,298.00.
- 🟠 **DEX volume (24h)** (warning): DEX volume (24h) is 6.0 robust standard deviations above its 7-day baseline: a 27.5% move to 1,712,543,782.00 USD from a typical 1,342,682,593.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 2.5K |
| Slot time | 421.1 ms |
| Slot | 437M |
| Block height | 415M |
| Epoch | 1012 (12.88% complete, ~44.0h remaining) |
| Lifetime transactions | 535.1B |
| Circulating supply | 581.4M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,527 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 19,047 / 805,000 lamports |
| Paying base fee only | 18.50% of 6,724 sampled transactions |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 2.3M µlam/CU) |
| Node version (RPC) | 4.1.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 692 |
| Delinquent validators | 7 |
| Delinquent stake | 0.00% |
| Total active stake | 434.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.36% / 24.35% / 35.61% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 24.23% |

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
| SOL price | $74.07 (+0.30% 24h) |
| Market cap | $43.06B (rank #7) |
| 24h volume | $1.35B |
| ATH | $293.31 (-74.75% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.78B |
| Stablecoin supply | $15.87B |
| DEX volume (24h) | $1.71B (+27.00% 1d) |
| App fees (24h, all protocols) | $8.41M |
| Chain fees (24h) | $614.78K |
| Jito MEV tips (24h) | $147.29K |
| **REV - Real Economic Value (24h)** | **$762.08K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.07B | -9.84% |
| USDT | $3.35B | -0.59% |
| USDGO | $1.11B | -0.00% |
| USD1 | $1.02B | +0.03% |
| PYUSD | $676.12M | -2.65% |
| BUIDL | $675.72M | +3.30% |
| USDG | $658.13M | +2.78% |
| USDe | $532.36M | -0.93% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $731.06M |
| BisonFi | $134.69M |
| Orca DEX | $124.38M |
| Manifest Trade | $103.29M |
| Meteora DLMM | $89.37M |
| Raydium AMM | $80.51M |
| GoonFi | $79.60M |
| pump.fun | $70.54M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.27M |
| pump.fun | $1.26M |
| Axiom | $1.11M |
| Collector Crypt | $341.95K |
| Meteora DLMM | $331.82K |
| fomo Wallet | $303.49K |
| Phantom Wallet | $233.30K |
| Raydium AMM | $219.55K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 309 |
| Persistently-active cohort (capture-recapture est.) | 3.2K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $371.03M |
| xStocks 24h DEX volume | $31.87M |
| xStocks holders | 249.8K |
| Total RWA TVL on Solana | $1.79B |

Top tokenized equities: TSLAX ($60.85M), CRCLX ($47.94M), SPYX ($44.12M), MSTRX ($36.31M), QQQX ($31.21M)

## Program activity and chain health

Chain clock drift: **+15.5 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,188 (approx.) | 52.40% | 0.8 s |
| Pump.fun | 21,254 | 90.40% | 2.5 s |
| Jupiter v6 | 8,013 | 77.50% | 7.2 s |
| Orca Whirlpools | 2,089 | 63.90% | 28.6 s |
| Raydium AMM v4 | 694 | 28.10% | 86.3 s |

Median failure rate across the sampled programs: **63.90%** (range 28.10% to 90.40%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **552.03 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 465.48K USD | DeFiLlama: 614.78K USD | -27.64% | agree (0.76x), *indicative* |
| SOL price | coingecko: 74.07 USD | Jupiter (on-chain DEX): 74.07 USD | 0.00% | agree |
| Circulating supply | getSupply (RPC): 581.39M SOL | CoinGecko: 581.31M SOL | +0.01% | agree |

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

**Latest Agave release:** [v4.2.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.0-rc.1) (2026-07-31)

**Latest Firedancer release:** [v1.1.3](https://github.com/firedancer-io/firedancer/releases/tag/v1.1.3) (2026-08-04)

## Ecosystem news

- **[Solana Proposal Would Increase Daily SOL Burns More Than 10-Fold](https://decrypt.co/374915/solana-proposal-increase-daily-sol-burns-10-fold)** - Decrypt, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Marmot Researchers Turn to OnlyFans for Funding—And There Are Meme Coins Too](https://decrypt.co/374874/marmot-researchers-onlyfans-memecoins-solana-onlymarms)** - Decrypt, 2026-08-03
- **[BlackRock Launches Tokenized Money Market Funds on Solana, Ethereum](https://decrypt.co/374865/blackrock-tokenized-money-market-funds-solana-ethereum)** - Decrypt, 2026-08-03
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29
- **[Setting Up Subscriptions and Recurring Payments on Solana](https://www.helius.dev/blog/solana-subscriptions-recurring-payments)** - Helius, 2026-07-24
- **[Solana Changelog: July 23, 2026](https://solana.com/news/solana-changelog-july-23-2026)** - Solana.com, 2026-07-23

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
