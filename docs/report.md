# Solana Ecosystem Report

*Generated 2026-08-11 15:48 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.4K |
| TPS (non-vote) | 2.8K |
| Slot time | 419.6 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1015 (35.85% complete, ~32.3h remaining) |
| Lifetime transactions | 537.2B |
| Circulating supply | 582.5M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,415 lamports (about $0.00040) |
| Transaction fee p90 / p99 | 26,803 / 816,173 lamports |
| Paying base fee only | 20.30% of 6,216 sampled transactions |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 32.9M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 690 |
| Delinquent validators | 9 |
| Delinquent stake | 0.01% |
| Total active stake | 434.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.37% / 35.70% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.22% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.67% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $74.78 (-1.80% 24h) |
| Market cap | $43.55B (rank #7) |
| 24h volume | $1.34B |
| ATH | $293.31 (-74.50% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.83B |
| Stablecoin supply | $15.69B |
| DEX volume (24h) | $1.58B (+17.41% 1d) |
| App fees (24h, all protocols) | $10.49M |
| Chain fees (24h) | $680.55K |
| Jito MEV tips (24h) | $140.59K |
| **REV - Real Economic Value (24h)** | **$821.14K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.99B | -0.31% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.16B | +4.04% |
| USD1 | $1.04B | +2.05% |
| BUIDL | $712.85M | +5.50% |
| PYUSD | $668.37M | -2.96% |
| USDG | $646.20M | +0.35% |
| USDe | $537.70M | -0.28% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $335.38M |
| BisonFi | $216.14M |
| HumidiFi | $161.21M |
| Orca DEX | $120.89M |
| Raydium AMM | $97.97M |
| Meteora DLMM | $91.95M |
| pump.fun | $86.05M |
| Manifest Trade | $76.12M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.49M |
| pump.fun | $1.43M |
| Axiom | $1.18M |
| Collector Crypt | $424.16K |
| fomo Wallet | $406.80K |
| Sanctum Validator LSTs | $365.15K |
| Meteora DLMM | $359.67K |
| Raydium AMM | $312.39K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 324 |
| Persistently-active cohort (capture-recapture est.) | 3.2K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $375.89M |
| xStocks 24h DEX volume | $25.30M |
| xStocks holders | 260.6K |
| Total RWA TVL on Solana | $1.84B |

Top tokenized equities: TSLAX ($61.49M), CRCLX ($54.12M), SPYX ($43.79M), MSTRX ($37.92M), QQQX ($28.79M)

## Program activity and chain health

Chain clock drift: **+14.5 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 69,995 (approx.) | 94.00% | 0.8 s |
| SPL Token | 49,547 (approx.) | 37.00% | 0.8 s |
| Jupiter v6 | 3,971 | 55.60% | 14.7 s |
| Orca Whirlpools | 1,918 | 56.30% | 30.6 s |
| Raydium AMM v4 | 716 | 28.90% | 74.7 s |

Median failure rate across the sampled programs: **55.60%** (range 28.90% to 94.00%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **303.30 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 503.16K USD | DeFiLlama: 680.55K USD | -29.97% | agree (0.74x), *indicative* |
| SOL price | coingecko: 74.78 USD | Jupiter (on-chain DEX): 74.70 USD | +0.11% | agree |
| Circulating supply | getSupply (RPC): 582.48M SOL | CoinGecko: 582.48M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-07-20

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
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

**Latest Agave release:** [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07)

**Latest Firedancer release:** [v1.1.4](https://github.com/firedancer-io/firedancer/releases/tag/v1.1.4) (2026-08-10)

## Ecosystem news

- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Top 15 Best Solana RPC Providers (2026)](https://www.helius.dev/blog/top-solana-rpcs-helius-vs-other-node-providers)** - Helius, 2026-08-04
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30
- **[What are Preconfirmations (Preconfs) on Solana?](https://www.helius.dev/blog/solana-preconfirmations)** - Helius, 2026-07-29

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
