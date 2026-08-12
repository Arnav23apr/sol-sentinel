# Solana Ecosystem Report

*Generated 2026-08-12 20:31 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.3 robust standard deviations above its 7-day baseline: a 785.7% move to 0.06 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 3.1K |
| Slot time | 418.1 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1015 (92.77% complete, ~3.6h remaining) |
| Lifetime transactions | 537.6B |
| Circulating supply | 582.5M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,412 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 29,000 / 788,327 lamports |
| Paying base fee only | 15.40% of 6,338 sampled transactions |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 19.2M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 687 |
| Delinquent validators | 12 |
| Delinquent stake | 0.06% |
| Total active stake | 434.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.38% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.24% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $75.82 (+0.70% 24h) |
| Market cap | $44.16B (rank #7) |
| 24h volume | $1.29B |
| ATH | $293.31 (-74.15% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.82B |
| Stablecoin supply | $15.54B |
| DEX volume (24h) | $1.65B (+4.35% 1d) |
| App fees (24h, all protocols) | $9.98M |
| Chain fees (24h) | $727.62K |
| Jito MEV tips (24h) | $148.38K |
| **REV - Real Economic Value (24h)** | **$876.00K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.80B | -5.08% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.17B | +5.54% |
| USD1 | $1.05B | +2.92% |
| BUIDL | $728.23M | +7.65% |
| PYUSD | $670.88M | -1.27% |
| USDG | $641.80M | -2.51% |
| USDe | $537.53M | -0.88% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $585.32M |
| BisonFi | $151.36M |
| Orca DEX | $118.68M |
| Raydium AMM | $90.13M |
| HumidiFi | $90.06M |
| Meteora DLMM | $88.95M |
| pump.fun | $79.16M |
| Axiom | $68.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.61M |
| pump.fun | $1.43M |
| Axiom | $1.36M |
| Collector Crypt | $787.16K |
| fomo Wallet | $458.79K |
| Meteora DLMM | $378.98K |
| Raydium AMM | $255.88K |
| Phantom Wallet | $205.71K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 287 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $376.21M |
| xStocks 24h DEX volume | $20.83M |
| xStocks holders | 263.0K |
| Total RWA TVL on Solana | $1.86B |

Top tokenized equities: TSLAX ($60.47M), CRCLX ($52.26M), SPYX ($44.27M), MSTRX ($37.21M), GOOGLX ($29.86M)

## Program activity and chain health

Chain clock drift: **+15.8 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 100,741 (approx.) | 93.40% | 0.4 s |
| SPL Token | 47,142 (approx.) | 37.60% | 0.8 s |
| Jupiter v6 | 2,380 | 45.90% | 25.1 s |
| Orca Whirlpools | 2,051 | 37.90% | 28.8 s |
| Raydium AMM v4 | 1,311 | 17.10% | 45.6 s |

Median failure rate across the sampled programs: **37.90%** (range 17.10% to 93.40%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.26 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 688.55K USD | DeFiLlama: 727.62K USD | -5.52% | agree (0.95x), *indicative* |
| SOL price | coingecko: 75.82 USD | Jupiter (on-chain DEX): 75.81 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 582.50M SOL | CoinGecko: 582.50M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-06-24

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07)

**Latest Firedancer release:** [v26.08.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.0) (2026-08-12)

## Ecosystem news

- **[A Routing Bug Took Solana 86% of the Way to Losing Finality](https://decrypt.co/375404/a-routing-bug-took-solana-86-of-the-way-to-losing-finality)** - Decrypt, 2026-08-12
- **[The Bull and Bear Case for Solana’s Next Price Move](https://decrypt.co/375364/solana-price-death-cross-bull-bear-case-next-move)** - Decrypt, 2026-08-11
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
