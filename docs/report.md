# Solana Ecosystem Report

*Generated 2026-10-03 08:40 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 1.6K |
| Slot time | 266.7 ms |
| Slot | 453M |
| Block height | 431M |
| Epoch | 1048 (33.87% complete, ~21.2h remaining) |
| Lifetime transactions | 555.5B |
| Circulating supply | 588.1M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 6.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 672 |
| Delinquent validators | 12 |
| Delinquent stake | 0.01% |
| Total active stake | 442.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.52% / 24.53% / 35.45% |
| Commission (stake-weighted, delegatable validators) | 3.82% |
| Stake on private (100% commission) validators | 23.61% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.9M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.79% | 0% |
| 4 | `8Gbw…F8iD` | 11.3M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.1M | 2.52% | 5% |
| 6 | `26pV…3dJx` | 9.2M | 2.09% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.09% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.72% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.60% | 5% |
| 10 | `3JD3…FrXf` | 6.7M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $119.14 (-2.75% 24h) |
| Market cap | $70.07B (rank #7) |
| 24h volume | $3.29B |
| ATH | $293.31 (-59.38% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.65B |
| Stablecoin supply | $16.63B |
| DEX volume (24h) | $2.57B (+3.26% 1d) |
| App fees (24h, all protocols) | $17.26M |
| Chain fees (24h) | $1.09M |
| Jito MEV tips (24h) | $265.81K |
| **REV - Real Economic Value (24h)** | **$1.36M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.47B | +0.06% |
| USDT | $2.84B | +6.71% |
| USD1 | $1.40B | +0.65% |
| USDGO | $1.20B | -14.86% |
| BUIDL | $967.58M | -2.06% |
| PYUSD | $735.93M | -5.44% |
| USDG | $628.16M | -5.89% |
| USDe | $456.68M | -5.46% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $381.91M |
| PumpSwap | $321.13M |
| Raydium AMM | $235.73M |
| BisonFi | $216.86M |
| Meteora DLMM | $180.66M |
| pump.fun | $177.46M |
| fomo Wallet | $153.95M |
| Manifest Trade | $152.05M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.74M |
| pump.fun | $2.37M |
| Axiom | $1.33M |
| StonkFun | $909.66K |
| Meteora DLMM | $660.93K |
| Raydium AMM | $655.90K |
| Collector Crypt | $589.88K |
| fomo Wallet | $544.45K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $80.06M |
| xStocks holder positions | 780.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.88M |

## Program activity and chain health

Chain tip lag: **+9.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 50,225 | 22.70% | 1.1 s |
| Pump.fun | 3,693 | 22.20% | 16 s |
| Jupiter v6 | 1,186 | 37.10% | 50.4 s |
| Orca Whirlpools | 946 | 37.50% | 63.2 s |
| Raydium AMM v4 | 646 | 9.10% | 92.8 s |

Median failure rate across the sampled programs: **22.70%** (range 9.10% to 37.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **540.99 SOL**.

## Exchange and large-holder balances

12.50M SOL ($1.49B) across 8 publicly-attributed accounts. Net **113K SOL (0.90%) moved off exchanges** over the last 17.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.26B | 0.3/h | 0 |
| Binance (2) | 1.28M | $152.62M | 823.8/h | 0 |
| Bybit | 330.75K | $39.41M | 24.5/h | 0 |
| Gate.io | 204.83K | $24.40M | 184.3/h | 4 |
| Bitget | 55.81K | $6.65M | 163.7/h | 0 |
| Kraken | 26.26K | $3.13M | 281.2/h | 0 |
| Coinbase (2) | 14.60K | $1.74M | 176.8/h | 0 |
| Coinbase | 14.09K | $1.68M | 438.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 932 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.224 | 891 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.214 | 898 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 857 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.203 | 857 | 0.0000 |
| Total TPS moves with Slot time | +0.176 | 898 | 0.0000 |
| Total TPS moves with Program failure rate | +0.159 | 879 | 0.0000 |
| SOL price moves with DeFi TVL | +0.159 | 932 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.157 | 879 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.145 | 857 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 119.14 USD | Jupiter (on-chain DEX): 119.19 USD | -0.04% | agree |
| Circulating supply | getSupply (RPC): 588.15M SOL | CoinGecko: 588.15M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-09-30
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16

**Open SIMD proposals:**

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29
- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16

**Latest Agave release:** [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03)

**Latest Firedancer release:** [v26.09.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.5) (2026-09-28)

## Ecosystem news

- **[Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)** - Solana.com, 2026-09-30
- **[Introducing The Information Exchange on Solana, Powered by Decrypt and MYR](https://decrypt.co/379655/introducing-the-information-exchange-powered-by-decrypt-and-myr)** - Decrypt, 2026-09-30
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
