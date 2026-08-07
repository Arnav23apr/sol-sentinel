# Solana Ecosystem Report

*Generated 2026-08-07 00:20 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.8K |
| Slot time | 421.1 ms |
| Slot | 438M |
| Block height | 416M |
| Epoch | 1013 (15.86% complete, ~42.5h remaining) |
| Lifetime transactions | 535.8B |
| Circulating supply | 582.1M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,527 lamports (about $0.00040) |
| Transaction fee p90 / p99 | 20,000 / 605,000 lamports |
| Paying base fee only | 16.70% of 6,063 sampled transactions |
| AMM write-lock congestion (150-slot window) | 15.30% of slots needed a priority fee (max 137.0M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 693 |
| Delinquent validators | 7 |
| Delinquent stake | 0.00% |
| Total active stake | 434.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.36% / 24.36% / 35.67% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.21% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 16.9M | 3.88% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 5 | `26pV…3dJx` | 9.1M | 2.10% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.04% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.82% | 7% |
| 9 | `CvSb…wycB` | 7.6M | 1.76% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $72.63 (-1.70% 24h) |
| Market cap | $42.27B (rank #7) |
| 24h volume | $1.44B |
| ATH | $293.31 (-75.24% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.72B |
| Stablecoin supply | $15.66B |
| DEX volume (24h) | $1.64B (-6.33% 1d) |
| App fees (24h, all protocols) | $7.78M |
| Chain fees (24h) | $589.53K |
| Jito MEV tips (24h) | $109.27K |
| **REV - Real Economic Value (24h)** | **$698.80K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.02B | +1.79% |
| USDT | $3.16B | -8.14% |
| USDGO | $1.13B | +1.90% |
| USD1 | $1.02B | +0.03% |
| BUIDL | $697.09M | +6.67% |
| PYUSD | $672.82M | -1.85% |
| USDG | $643.72M | +1.67% |
| USDe | $538.83M | +0.44% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $606.68M |
| BisonFi | $130.67M |
| Raydium AMM | $93.78M |
| Orca DEX | $89.86M |
| pump.fun | $76.20M |
| Meteora DLMM | $75.94M |
| Manifest Trade | $67.74M |
| SolFi V2 | $66.92M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.00M |
| pump.fun | $1.28M |
| Axiom | $982.24K |
| Raydium AMM | $528.88K |
| fomo Wallet | $435.44K |
| Collector Crypt | $392.53K |
| Meteora DLMM | $330.80K |
| Phantom Wallet | $159.50K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 270 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $366.55M |
| xStocks 24h DEX volume | $29.21M |
| xStocks holders | 254.5K |
| Total RWA TVL on Solana | $1.81B |

Top tokenized equities: TSLAX ($59.53M), CRCLX ($48.70M), SPYX ($43.15M), MSTRX ($36.36M), QQQX ($28.57M)

## Program activity and chain health

Chain clock drift: **+15.6 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 51,508 (approx.) | 40.60% | 0.8 s |
| Pump.fun | 5,283 | 67.40% | 10.9 s |
| Jupiter v6 | 2,983 | 52.30% | 19.8 s |
| Orca Whirlpools | 2,133 | 57.70% | 27.8 s |
| Raydium AMM v4 | 1,310 | 65.20% | 45.5 s |

Median failure rate across the sampled programs: **57.70%** (range 40.60% to 67.40%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **852.07 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 7.24M USD | DeFiLlama: 589.53K USD | +169.87% | **diverge** (12.28x), *indicative* |
| SOL price | coingecko: 72.63 USD | Jupiter (on-chain DEX): 72.52 USD | +0.15% | agree |
| Circulating supply | getSupply (RPC): 582.05M SOL | CoinGecko: 582.05M SOL | -0.00% | agree |

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

- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[JPMorgan says Hyperliquid faces growing competition while HYPE ETF inflows stall](https://www.theblock.co/post/411001/jpmorgan-hyperliquid-competition-hype-etf-inflows-stall?utm_source=rss&utm_medium=rss)** - The Block, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Top 15 Best Solana RPC Providers (2026)](https://www.helius.dev/blog/top-solana-rpcs-helius-vs-other-node-providers)** - Helius, 2026-08-04
- **[Solana Proposal Would Increase Daily SOL Burns More Than 10-Fold](https://decrypt.co/374915/solana-proposal-increase-daily-sol-burns-10-fold)** - Decrypt, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
