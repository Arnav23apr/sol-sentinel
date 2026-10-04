# Solana Ecosystem Report

*Generated 2026-10-04 12:36 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **DEX volume (24h)** (warning): DEX volume (24h) is 5.4 robust standard deviations below its 7-day baseline: a 38.8% move to 1,553,984,451.00 USD from a typical 2,539,433,046.00.
- 🟠 **App fees (24h, all protocols)** (warning): App fees (24h, all protocols) is 4.8 robust standard deviations below its 7-day baseline: a 25.1% move to 12,836,095.00 USD from a typical 17,134,432.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 1.5K |
| Slot time | 267.3 ms |
| Slot | 453M |
| Block height | 431M |
| Epoch | 1049 (20.90% complete, ~25.4h remaining) |
| Lifetime transactions | 556.0B |
| Circulating supply | 588.2M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 26.00% of slots needed a priority fee (max 2.1M µlam/CU) |
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
| Commission (stake-weighted, delegatable validators) | 3.82% |
| Stake on private (100% commission) validators | 23.62% |

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
| SOL price | $121.47 (+1.77% 24h) |
| Market cap | $71.44B (rank #7) |
| 24h volume | $1.73B |
| ATH | $293.31 (-58.59% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.72B |
| Stablecoin supply | $16.54B |
| DEX volume (24h) | $1.55B (-43.70% 1d) |
| App fees (24h, all protocols) | $12.84M |
| Chain fees (24h) | $902.91K |
| Jito MEV tips (24h) | $231.81K |
| **REV - Real Economic Value (24h)** | **$1.13M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.39B | +1.28% |
| USDT | $2.84B | +6.71% |
| USD1 | $1.40B | +0.65% |
| USDGO | $1.20B | -14.86% |
| BUIDL | $967.58M | -2.06% |
| PYUSD | $707.05M | -7.06% |
| USDG | $631.24M | -7.19% |
| USDe | $473.23M | +1.25% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $401.98M |
| pump.fun | $183.58M |
| BisonFi | $171.40M |
| Axiom | $149.54M |
| fomo Wallet | $139.26M |
| Raydium AMM | $121.31M |
| Orca DEX | $115.38M |
| Meteora DLMM | $112.43M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.26M |
| pump.fun | $2.31M |
| Axiom | $1.06M |
| Meteora DLMM | $843.39K |
| Collector Crypt | $641.12K |
| fomo Wallet | $444.10K |
| pump.fun Mobile App | $432.17K |
| Raydium AMM | $299.37K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $58.54M |
| xStocks holder positions | 785.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.97M |

## Program activity and chain health

Chain tip lag: **+10.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 83,726 (approx.) | 37.80% | 0.5 s |
| Pump.fun | 10,572 | 51.90% | 5.3 s |
| Raydium AMM v4 | 8,616 | 2.90% | 6.9 s |
| Orca Whirlpools | 3,588 | 15.00% | 16.6 s |
| Jupiter v6 | 2,022 | 27.20% | 29.1 s |

Median failure rate across the sampled programs: **27.20%** (range 2.90% to 51.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **597.90 SOL**.

## Exchange and large-holder balances

12.64M SOL ($1.53B) across 8 publicly-attributed accounts. Net **17K SOL (0.14%) moved onto exchanges** over the last 22.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.28B | 0.3/h | 1 |
| Binance (2) | 1.39M | $168.48M | 1.1K/h | 0 |
| Bybit | 301.68K | $36.64M | 20.5/h | 0 |
| Gate.io | 218.96K | $26.60M | 284.8/h | 1 |
| Bitget | 100.00K | $12.15M | 238.3/h | 1 |
| Kraken | 28.61K | $3.48M | 420.1/h | 0 |
| Coinbase | 13.33K | $1.62M | 153.1/h | 0 |
| Coinbase (2) | 13.19K | $1.60M | 192.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 938 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.235 | 897 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.217 | 904 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.209 | 863 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.204 | 863 | 0.0000 |
| Total TPS moves with Slot time | +0.178 | 904 | 0.0000 |
| SOL price moves with DeFi TVL | +0.164 | 938 | 0.0000 |
| Total TPS moves with Program failure rate | +0.157 | 885 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.157 | 885 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.145 | 863 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 121.47 USD | Jupiter (on-chain DEX): 121.53 USD | -0.05% | agree |
| Circulating supply | getSupply (RPC): 588.22M SOL | CoinGecko: 588.22M SOL | -0.00% | agree |

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

- **[Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)** - Solana.com, 2026-10-02
- **[Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)** - Solana.com, 2026-09-30
- **[Introducing The Information Exchange on Solana, Powered by Decrypt and MYR](https://decrypt.co/379655/introducing-the-information-exchange-powered-by-decrypt-and-myr)** - Decrypt, 2026-09-30
- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1)** - Solana.com, 2026-09-18

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
