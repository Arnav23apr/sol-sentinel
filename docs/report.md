# Solana Ecosystem Report

*Generated 2026-08-14 11:35 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.0K |
| TPS (non-vote) | 1.3K |
| Slot time | 415.2 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1016 (70.90% complete, ~14.5h remaining) |
| Lifetime transactions | 538.1B |
| Circulating supply | 582.6M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,473 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 25,994 / 805,000 lamports |
| Paying base fee only | 13.80% of 6,853 sampled transactions |
| AMM write-lock congestion (150-slot window) | 6.70% of slots needed a priority fee (max 2.5M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 688 |
| Delinquent validators | 9 |
| Delinquent stake | 0.01% |
| Total active stake | 434.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.42% / 24.44% / 35.79% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.24% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.4M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $75.46 (-0.80% 24h) |
| Market cap | $43.96B (rank #7) |
| 24h volume | $1.10B |
| ATH | $293.31 (-74.27% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.83B |
| Stablecoin supply | $15.50B |
| DEX volume (24h) | $1.94B (+12.58% 1d) |
| App fees (24h, all protocols) | $10.08M |
| Chain fees (24h) | $709.83K |
| Jito MEV tips (24h) | $118.26K |
| **REV - Real Economic Value (24h)** | **$828.09K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.75B | -4.12% |
| USDT | $2.95B | -6.33% |
| USDGO | $1.18B | +4.74% |
| USD1 | $1.05B | +2.92% |
| BUIDL | $740.89M | +6.28% |
| PYUSD | $676.66M | -0.84% |
| USDG | $635.07M | -1.24% |
| USDe | $537.95M | -0.14% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $866.70M |
| BisonFi | $178.89M |
| HumidiFi | $126.58M |
| Orca DEX | $108.21M |
| pump.fun | $83.54M |
| Raydium AMM | $82.71M |
| Manifest Trade | $81.43M |
| Meteora DLMM | $75.77M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.40M |
| pump.fun | $1.48M |
| Axiom | $1.34M |
| Collector Crypt | $446.19K |
| fomo Wallet | $382.68K |
| Sanctum Validator LSTs | $365.14K |
| Meteora DLMM | $288.23K |
| Binance Staked SOL | $228.50K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 281 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $383.33M |
| xStocks 24h DEX volume | $21.31M |
| xStocks holders | 266.1K |
| Total RWA TVL on Solana | $1.87B |

Top tokenized equities: TSLAX ($62.84M), CRCLX ($54.72M), SPYX ($44.15M), MSTRX ($38.21M), GOOGLX ($30.22M)

## Program activity and chain health

Chain clock drift: **+15.3 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 29,335 | 31.80% | 1.7 s |
| Pump.fun | 20,190 | 86.30% | 2.9 s |
| Jupiter v6 | 2,287 | 52.60% | 26.2 s |
| Orca Whirlpools | 656 | 55.20% | 91.3 s |
| Raydium AMM v4 | 617 | 26.40% | 97.2 s |

Median failure rate across the sampled programs: **52.60%** (range 26.40% to 86.30%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.27 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 583.70K USD | DeFiLlama: 709.83K USD | -19.50% | agree (0.82x), *indicative* |
| SOL price | coingecko: 75.46 USD | Jupiter (on-chain DEX): 75.44 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 582.61M SOL | CoinGecko: 582.61M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
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

**Latest Agave release:** [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) (2026-08-13)

**Latest Firedancer release:** [v26.08.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.0) (2026-08-12)

## Ecosystem news

- **[Bitwise mulls tokenizing its Solana staking ETF via Superstate partnership](https://www.theblock.co/news/defi/2026-08-14-bitwise-tokenize-sol-staking-etf-411790)** - The Block, 2026-08-14
- **[Solana Can Be the 'Everything Chain' as Crypto Apps Go Mainstream: 6th Man Ventures Co-Founder](https://decrypt.co/375605/solana-everything-chain-crypto-apps-mainstream)** - Decrypt, 2026-08-13
- **[A Routing Bug Took Solana 86% of the Way to Losing Finality](https://decrypt.co/375404/a-routing-bug-took-solana-86-of-the-way-to-losing-finality)** - Decrypt, 2026-08-12
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
