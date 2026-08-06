# Solana Ecosystem Report

*Generated 2026-08-06 03:57 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.1K |
| TPS (non-vote) | 1.4K |
| Slot time | 421.1 ms |
| Slot | 438M |
| Block height | 416M |
| Epoch | 1012 (75.65% complete, ~12.3h remaining) |
| Lifetime transactions | 535.5B |
| Circulating supply | 581.3M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,308 lamports (about $0.00039) |
| Transaction fee p90 / p99 | 22,101 / 672,838 lamports |
| Paying base fee only | 21.80% of 5,724 sampled transactions |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 2.7M µlam/CU) |
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
| Commission (stake-weighted, delegatable validators) | 3.81% |
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
| SOL price | $73.42 (-0.90% 24h) |
| Market cap | $42.69B (rank #7) |
| 24h volume | $1.59B |
| ATH | $293.31 (-74.97% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.78B |
| Stablecoin supply | $15.62B |
| DEX volume (24h) | $1.65B (-5.31% 1d) |
| App fees (24h, all protocols) | $7.71M |
| Chain fees (24h) | $614.00K |
| Jito MEV tips (24h) | $118.01K |
| **REV - Real Economic Value (24h)** | **$732.01K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.00B | +1.54% |
| USDT | $3.16B | -8.14% |
| USDGO | $1.12B | +0.99% |
| USD1 | $1.02B | +0.03% |
| BUIDL | $685.51M | +4.90% |
| PYUSD | $678.00M | -1.07% |
| USDG | $653.24M | +3.06% |
| USDe | $538.52M | +0.38% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $606.68M |
| Orca DEX | $138.33M |
| BisonFi | $130.67M |
| Raydium AMM | $98.23M |
| Manifest Trade | $92.73M |
| Meteora DLMM | $85.45M |
| GoonFi | $84.28M |
| pump.fun | $76.20M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.00M |
| pump.fun | $1.28M |
| Axiom | $982.24K |
| Raydium AMM | $467.69K |
| fomo Wallet | $466.21K |
| Collector Crypt | $347.00K |
| Meteora DLMM | $330.72K |
| Phantom Wallet | $162.70K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 282 |
| Persistently-active cohort (capture-recapture est.) | 3.1K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $365.90M |
| xStocks 24h DEX volume | $43.36M |
| xStocks holders | 253.1K |
| Total RWA TVL on Solana | $1.79B |

Top tokenized equities: TSLAX ($59.81M), CRCLX ($47.24M), SPYX ($43.54M), MSTRX ($36.84M), QQQX ($28.82M)

## Program activity and chain health

Chain clock drift: **+15.4 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 38,281 | 27.60% | 1.3 s |
| Pump.fun | 12,952 | 88.00% | 4.2 s |
| Raydium AMM v4 | 1,975 | 61.70% | 30.3 s |
| Orca Whirlpools | 1,910 | 48.10% | 31.2 s |
| Jupiter v6 | 1,757 | 47.70% | 33.3 s |

Median failure rate across the sampled programs: **48.10%** (range 27.60% to 88.00%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.24 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 493.07K USD | DeFiLlama: 614.00K USD | -21.85% | agree (0.80x), *indicative* |
| SOL price | coingecko: 73.42 USD | Jupiter (on-chain DEX): 73.38 USD | +0.05% | agree |
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

- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Top 15 Best Solana RPC Providers (2026)](https://www.helius.dev/blog/top-solana-rpcs-helius-vs-other-node-providers)** - Helius, 2026-08-04
- **[Solana Proposal Would Increase Daily SOL Burns More Than 10-Fold](https://decrypt.co/374915/solana-proposal-increase-daily-sol-burns-10-fold)** - Decrypt, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Marmot Researchers Turn to OnlyFans for Funding—And There Are Meme Coins Too](https://decrypt.co/374874/marmot-researchers-onlyfans-memecoins-solana-onlymarms)** - Decrypt, 2026-08-03
- **[BlackRock Launches Tokenized Money Market Funds on Solana, Ethereum](https://decrypt.co/374865/blackrock-tokenized-money-market-funds-solana-ethereum)** - Decrypt, 2026-08-03
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
