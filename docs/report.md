# Solana Ecosystem Report

*Generated 2026-08-04 18:09 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 7.4 robust standard deviations above its 7-day baseline: a 28.3% move to 1,712,543,782.00 USD from a typical 1,335,113,153.00.
- 🔴 **Network fees (24h)** (critical): Network fees (24h) is 37.6 robust standard deviations above its 7-day baseline: a 45.8% move to 8,405,853.00 USD from a typical 5,767,298.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 2.4K |
| Slot time | 430.1 ms |
| Slot | 437M |
| Block height | 415M |
| Epoch | 1012 (9.07% complete, ~46.9h remaining) |
| Lifetime transactions | 535.1B |
| Circulating supply | 581.3M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,631 lamports (about $0.00042) |
| Transaction fee p90 / p99 | 18,491 / 1,005,000 lamports |
| Paying base fee only | 19.00% of 6,116 sampled transactions |
| AMM write-lock congestion (150-slot window) | 20.70% of slots needed a priority fee (max 2.7M µlam/CU) |
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
| SOL price | $74.02 (+0.50% 24h) |
| Market cap | $43.03B (rank #7) |
| 24h volume | $1.37B |
| ATH | $293.31 (-74.76% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.78B |
| Stablecoin supply | $15.84B |
| DEX volume (24h) | $1.71B (+27.00% 1d) |
| App fees (24h, all protocols) | $8.41M |
| Chain fees (24h) | $614.78K |
| Jito MEV tips (24h) | $149.87K |
| **REV - Real Economic Value (24h)** | **$764.65K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.05B | -10.12% |
| USDT | $3.35B | -0.59% |
| USDGO | $1.11B | -0.00% |
| USD1 | $1.02B | +0.03% |
| BUIDL | $675.72M | +3.30% |
| PYUSD | $675.48M | -2.75% |
| USDG | $654.58M | +2.38% |
| USDe | $533.65M | -0.66% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $731.06M |
| BisonFi | $134.69M |
| Orca DEX | $124.38M |
| Manifest Trade | $96.46M |
| Meteora DLMM | $88.98M |
| GoonFi | $79.60M |
| Raydium AMM | $76.85M |
| pump.fun | $70.54M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.27M |
| pump.fun | $1.26M |
| Axiom | $1.11M |
| Collector Crypt | $341.95K |
| Meteora DLMM | $336.05K |
| fomo Wallet | $303.49K |
| Phantom Wallet | $233.30K |
| Raydium AMM | $195.34K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 276 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $370.21M |
| xStocks 24h DEX volume | $26.18M |
| xStocks holders | 249.1K |
| Total RWA TVL on Solana | $1.79B |

Top tokenized equities: TSLAX ($60.72M), CRCLX ($48.21M), SPYX ($43.98M), MSTRX ($36.17M), QQQX ($31.12M)

## Program activity and chain health

Chain clock drift: **+15.7 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 49,942 (approx.) | 52.20% | 0.4 s |
| Pump.fun | 24,022 | 88.10% | 2.2 s |
| Raydium AMM v4 | 18,494 | 85.20% | 3 s |
| Orca Whirlpools | 9,244 | 83.40% | 6.5 s |
| Jupiter v6 | 7,041 | 81.80% | 8.2 s |

Median failure rate across the sampled programs: **83.40%** (range 52.20% to 88.10%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **484.11 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 602.87K USD | DeFiLlama: 614.78K USD | -1.96% | agree (0.98x), *indicative* |
| SOL price | coingecko: 74.02 USD | Jupiter (on-chain DEX): 73.97 USD | +0.07% | agree |
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
