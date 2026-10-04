# Solana Ecosystem Report

*Generated 2026-10-04 23:19 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **DEX volume (24h)** (warning): DEX volume (24h) is 5.7 robust standard deviations below its 7-day baseline: a 38.9% move to 1,553,984,451.00 USD from a typical 2,544,678,620.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.8K |
| TPS (non-vote) | 2.3K |
| Slot time | 266.7 ms |
| Slot | 453M |
| Block height | 431M |
| Epoch | 1049 (54.21% complete, ~14.7h remaining) |
| Lifetime transactions | 556.1B |
| Circulating supply | 588.3M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 15.30% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 15 |
| Delinquent stake | 0.03% |
| Total active stake | 441.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.54% / 24.57% / 35.48% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.63% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.9M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.61% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.80% | 0% |
| 4 | `8Gbw…F8iD` | 11.3M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.1M | 2.52% | 5% |
| 6 | `26pV…3dJx` | 9.3M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.09% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.72% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.60% | 5% |
| 10 | `3JD3…FrXf` | 6.7M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $122.03 (+1.93% 24h) |
| Market cap | $71.80B (rank #7) |
| 24h volume | $2.00B |
| ATH | $293.31 (-58.40% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.73B |
| Stablecoin supply | $16.58B |
| DEX volume (24h) | $1.55B (-43.70% 1d) |
| App fees (24h, all protocols) | $12.93M |
| Chain fees (24h) | $902.91K |
| Jito MEV tips (24h) | $248.12K |
| **REV - Real Economic Value (24h)** | **$1.15M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.41B | +1.46% |
| USDT | $2.87B | +7.84% |
| USD1 | $1.40B | +0.65% |
| USDGO | $1.20B | -14.86% |
| BUIDL | $967.58M | -2.06% |
| PYUSD | $704.90M | -7.33% |
| USDG | $625.98M | -7.97% |
| USDe | $471.59M | +0.91% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $401.98M |
| pump.fun | $183.58M |
| BisonFi | $171.40M |
| Orca DEX | $170.86M |
| fomo Wallet | $155.62M |
| Axiom | $149.54M |
| Raydium AMM | $144.40M |
| Meteora DLMM | $112.43M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.26M |
| pump.fun | $2.31M |
| Axiom | $1.06M |
| Meteora DLMM | $843.39K |
| Collector Crypt | $641.12K |
| fomo Wallet | $444.08K |
| pump.fun Mobile App | $432.17K |
| Raydium AMM | $385.30K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $84.05M |
| xStocks holder positions | 787.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.72M |

## Program activity and chain health

Chain tip lag: **+9.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 64,942 | 39.70% | 0.8 s |
| Pump.fun | 18,898 | 83.60% | 2.9 s |
| Jupiter v6 | 5,098 | 66.60% | 11.7 s |
| Orca Whirlpools | 2,254 | 46.30% | 25.6 s |
| Raydium AMM v4 | 975 | 17.20% | 61.3 s |

Median failure rate across the sampled programs: **46.30%** (range 17.20% to 83.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.47 SOL**.

## Exchange and large-holder balances

12.58M SOL ($1.54B) across 8 publicly-attributed accounts. Net **80K SOL (0.64%) moved onto exchanges** over the last 23.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.29B | 0.3/h | 1 |
| Binance (2) | 1.35M | $164.87M | 845.1/h | 0 |
| Bybit | 301.68K | $36.81M | 17.8/h | 0 |
| Gate.io | 236.07K | $28.81M | 204.7/h | 4 |
| Bitget | 72.20K | $8.81M | 107.1/h | 0 |
| Kraken | 21.92K | $2.67M | 283/h | 0 |
| Coinbase (2) | 12.25K | $1.50M | 321.1/h | 0 |
| Coinbase | 11.50K | $1.40M | 402.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 941 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.235 | 900 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.220 | 907 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.207 | 866 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.202 | 866 | 0.0000 |
| Total TPS moves with Slot time | +0.182 | 907 | 0.0000 |
| SOL price moves with DeFi TVL | +0.168 | 941 | 0.0000 |
| Total TPS moves with Program failure rate | +0.154 | 888 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.154 | 888 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 866 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 122.03 USD | Jupiter (on-chain DEX): 121.97 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 588.31M SOL | CoinGecko: 588.31M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-09-30
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-04
- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-04
- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16

**Latest Agave release:** [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03)

**Latest Firedancer release:** [v26.09.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.5) (2026-09-28)

## Ecosystem news

- **[Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)** - Solana.com, 2026-10-02
- **[Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)** - Solana.com, 2026-09-30
- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1)** - Solana.com, 2026-09-18
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
