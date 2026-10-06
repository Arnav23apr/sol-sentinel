# Solana Ecosystem Report

*Generated 2026-10-06 06:39 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **DEX volume (24h)** (warning): DEX volume (24h) is 3.7 robust standard deviations below its 7-day baseline: a 25.1% move to 1,904,732,430.00 USD from a typical 2,544,678,620.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 1.4K |
| Slot time | 269.1 ms |
| Slot | 454M |
| Block height | 432M |
| Epoch | 1050 (51.65% complete, ~15.6h remaining) |
| Lifetime transactions | 556.6B |
| Circulating supply | 588.4M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 8.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 672 |
| Delinquent validators | 13 |
| Delinquent stake | 0.02% |
| Total active stake | 441.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.53% / 24.57% / 35.48% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.64% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.9M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.61% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.78% | 0% |
| 4 | `8Gbw…F8iD` | 11.3M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.1M | 2.52% | 5% |
| 6 | `26pV…3dJx` | 9.3M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.3M | 2.10% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.60% | 5% |
| 10 | `3JD3…FrXf` | 6.7M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $119.69 (-1.07% 24h) |
| Market cap | $70.39B (rank #7) |
| 24h volume | $2.38B |
| ATH | $293.31 (-59.19% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.79B |
| Stablecoin supply | $16.71B |
| DEX volume (24h) | $1.90B (+11.51% 1d) |
| App fees (24h, all protocols) | $16.11M |
| Chain fees (24h) | $1.04M |
| Jito MEV tips (24h) | $299.62K |
| **REV - Real Economic Value (24h)** | **$1.34M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.41B | +3.34% |
| USDT | $2.87B | +6.25% |
| USD1 | $1.40B | +0.65% |
| USDGO | $1.28B | -9.19% |
| BUIDL | $967.88M | +0.39% |
| PYUSD | $711.62M | -1.41% |
| USDG | $619.34M | -10.50% |
| USDe | $502.13M | +9.45% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $306.60M |
| Orca DEX | $282.07M |
| BisonFi | $236.72M |
| pump.fun | $184.20M |
| Raydium AMM | $170.58M |
| Meteora DLMM | $144.38M |
| fomo Wallet | $132.75M |
| Manifest Trade | $130.14M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.45M |
| pump.fun | $2.59M |
| Axiom | $1.28M |
| Meteora DLMM | $678.40K |
| fomo Wallet | $583.15K |
| StonkFun | $577.37K |
| GMX Solana | $529.43K |
| Collector Crypt | $499.74K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $76.71M |
| xStocks holder positions | 776.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $599.50M |

## Program activity and chain health

Chain tip lag: **+9.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 35,050 | 22.70% | 1.3 s |
| Pump.fun | 4,532 | 40.90% | 13.2 s |
| Jupiter v6 | 1,871 | 40.00% | 31.8 s |
| Orca Whirlpools | 1,379 | 28.30% | 42.5 s |
| Raydium AMM v4 | 706 | 11.90% | 84.8 s |

Median failure rate across the sampled programs: **28.30%** (range 11.90% to 40.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **93.22 SOL**.

## Exchange and large-holder balances

12.54M SOL ($1.50B) across 8 publicly-attributed accounts. Net **97K SOL (0.78%) moved onto exchanges** over the last 21.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.27B | 0.3/h | 1 |
| Binance (2) | 1.19M | $142.18M | 875.9/h | 0 |
| Bybit | 303.27K | $36.30M | 15/h | 0 |
| Gate.io | 215.03K | $25.74M | 193.3/h | 3 |
| Bitget | 101.81K | $12.19M | 7.3K/h | 0 |
| Coinbase (2) | 77.33K | $9.26M | 182.6/h | 0 |
| Kraken | 63.55K | $7.61M | 342.9/h | 0 |
| Coinbase | 13.98K | $1.67M | 518.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 946 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.250 | 905 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.217 | 912 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.210 | 871 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.205 | 871 | 0.0000 |
| Total TPS moves with Slot time | +0.179 | 912 | 0.0000 |
| SOL price moves with DeFi TVL | +0.174 | 946 | 0.0000 |
| Total TPS moves with Program failure rate | +0.160 | 893 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.160 | 893 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.144 | 871 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 119.69 USD | Jupiter (on-chain DEX): 119.71 USD | -0.02% | agree |
| Circulating supply | getSupply (RPC): 588.39M SOL | CoinGecko: 588.39M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-06

**Open SIMD proposals:**

- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-05
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-06
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02

**Recently merged SIMDs:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23

**Latest Agave release:** [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03)

**Latest Firedancer release:** [v26.09.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.6) (2026-10-06)

## Ecosystem news

- **[Solana Debuts Institutional Settlement Standard With J.P. Morgan Input](https://decrypt.co/380126/solana-institutional-settlement-standard-jp-morgan)** - Decrypt, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06
- **[DeFi Development Corp Adds $3 Million in Solana as SOL Buys Slow](https://decrypt.co/380125/defi-development-corp-adds-3m-solana)** - Decrypt, 2026-10-05
- **[DeFi Development sees NAV per share more than doubling, holds 2.56 million SOL](https://www.theblock.co/news/markets/2026-10-05-defi-development-nav-per-share-doubles-2-56-million-sol-417674)** - The Block, 2026-10-05
- **[Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)** - Solana.com, 2026-10-02
- **[Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)** - Solana.com, 2026-09-30
- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
