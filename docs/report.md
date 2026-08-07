# Solana Ecosystem Report

*Generated 2026-08-07 08:05 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.9K |
| TPS (non-vote) | 1.3K |
| Slot time | 422.5 ms |
| Slot | 438M |
| Block height | 416M |
| Epoch | 1013 (31.17% complete, ~34.9h remaining) |
| Lifetime transactions | 535.9B |
| Circulating supply | 582.1M SOL |
| Inflation (annual) | 3.71% |
| Median transaction fee | 5,253 lamports (about $0.00038) |
| Transaction fee p90 / p99 | 21,014 / 1,005,000 lamports |
| Paying base fee only | 20.90% of 5,294 sampled transactions |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 6.4M µlam/CU) |
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
| SOL price | $72.90 (-1.40% 24h) |
| Market cap | $42.43B (rank #7) |
| 24h volume | $1.35B |
| ATH | $293.31 (-75.15% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.71B |
| Stablecoin supply | $15.64B |
| DEX volume (24h) | $1.40B (-14.50% 1d) |
| App fees (24h, all protocols) | $8.80M |
| Chain fees (24h) | $516.12K |
| Jito MEV tips (24h) | $106.43K |
| **REV - Real Economic Value (24h)** | **$622.55K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.99B | +0.24% |
| USDT | $3.16B | -6.51% |
| USDGO | $1.14B | +4.30% |
| USD1 | $1.02B | +0.03% |
| BUIDL | $697.09M | +6.61% |
| PYUSD | $673.80M | -1.16% |
| USDG | $651.12M | +2.79% |
| USDe | $538.69M | +0.28% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $560.33M |
| BisonFi | $115.36M |
| Raydium AMM | $99.46M |
| Orca DEX | $92.19M |
| Meteora DLMM | $73.35M |
| pump.fun | $68.21M |
| Manifest Trade | $67.26M |
| Axiom | $56.92M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.87M |
| pump.fun | $1.17M |
| Axiom | $911.99K |
| Raydium AMM | $498.54K |
| fomo Wallet | $435.44K |
| Sanctum Validator LSTs | $351.73K |
| Meteora DLMM | $262.47K |
| Binance Staked SOL | $217.91K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 267 |
| Persistently-active cohort (capture-recapture est.) | 2.7K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $366.68M |
| xStocks 24h DEX volume | $24.94M |
| xStocks holders | 255.4K |
| Total RWA TVL on Solana | $1.81B |

Top tokenized equities: TSLAX ($59.64M), CRCLX ($48.56M), SPYX ($43.15M), MSTRX ($36.32M), QQQX ($28.54M)

## Program activity and chain health

Chain clock drift: **+14.5 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 33,515 | 25.00% | 1.7 s |
| Pump.fun | 20,105 | 90.80% | 3 s |
| Jupiter v6 | 1,673 | 38.90% | 34.2 s |
| Orca Whirlpools | 1,573 | 25.60% | 37.6 s |
| Raydium AMM v4 | 1,333 | 38.60% | 44.8 s |

Median failure rate across the sampled programs: **38.60%** (range 25.00% to 90.80%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **586.67 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 992.07K USD | DeFiLlama: 516.12K USD | +63.12% | agree (1.92x), *indicative* |
| SOL price | coingecko: 72.90 USD | Jupiter (on-chain DEX): 72.88 USD | +0.03% | agree |
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
