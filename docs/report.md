# Solana Ecosystem Report

*Generated 2026-10-07 09:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 1.4K |
| Slot time | 265.5 ms |
| Slot | 454M |
| Block height | 432M |
| Epoch | 1051 (34.93% complete, ~20.7h remaining) |
| Lifetime transactions | 557.1B |
| Circulating supply | 589.1M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 24.00% of slots needed a priority fee (max 2.8M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
| Delinquent validators | 8 |
| Delinquent stake | 0.00% |
| Total active stake | 439.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.56% / 24.62% / 35.63% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.76% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.7M | 4.02% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.63% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.80% | 0% |
| 4 | `8Gbw…F8iD` | 11.3M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.1M | 2.54% | 5% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.3M | 2.11% | 10% |
| 8 | `9QU2…29mF` | 7.5M | 1.71% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.62% | 5% |
| 10 | `3JD3…FrXf` | 6.7M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $118.08 (-0.86% 24h) |
| Market cap | $69.56B (rank #7) |
| 24h volume | $2.93B |
| ATH | $293.31 (-59.74% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.54B |
| Stablecoin supply | $16.65B |
| DEX volume (24h) | $2.04B (-0.87% 1d) |
| App fees (24h, all protocols) | $16.06M |
| Chain fees (24h) | $1.05M |
| Jito MEV tips (24h) | $281.05K |
| **REV - Real Economic Value (24h)** | **$1.33M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.21B | +0.05% |
| USDT | $2.91B | +6.93% |
| USD1 | $1.41B | +1.76% |
| USDGO | $1.31B | +10.36% |
| BUIDL | $967.97M | +0.39% |
| PYUSD | $703.31M | -4.69% |
| USDG | $626.49M | -2.34% |
| USDe | $538.70M | +18.77% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $316.48M |
| PumpSwap | $302.95M |
| BisonFi | $234.22M |
| pump.fun | $187.50M |
| Raydium AMM | $183.90M |
| Meteora DLMM | $154.14M |
| Axiom | $122.05M |
| Manifest Trade | $117.85M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.47M |
| pump.fun | $2.52M |
| Axiom | $1.36M |
| Meteora DLMM | $826.08K |
| fomo Wallet | $470.81K |
| Raydium AMM | $445.79K |
| StonkFun | $428.10K |
| Sanctum Validator LSTs | $383.93K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $87.16M |
| xStocks holder positions | 782.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $596.32M |

## Program activity and chain health

Chain tip lag: **+9.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 42,305 | 20.60% | 1.3 s |
| Pump.fun | 14,096 | 69.40% | 4.2 s |
| Orca Whirlpools | 3,177 | 11.10% | 18.9 s |
| Raydium AMM v4 | 1,940 | 21.10% | 30.8 s |
| Jupiter v6 | 1,786 | 36.80% | 33.2 s |

Median failure rate across the sampled programs: **21.10%** (range 11.10% to 69.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **603.82 SOL**.

## Exchange and large-holder balances

12.33M SOL ($1.46B) across 8 publicly-attributed accounts. Net **49K SOL (0.39%) moved off exchanges** over the last 19.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.25B | 0.3/h | 1 |
| Binance (2) | 1.07M | $126.80M | 1.1K/h | 0 |
| Bybit | 304.34K | $35.94M | 16.6/h | 0 |
| Gate.io | 212.25K | $25.06M | 623.9/h | 2 |
| Bitget | 94.47K | $11.16M | 3.7K/h | 0 |
| Kraken | 35.83K | $4.23M | 869.6/h | 0 |
| Coinbase | 16.34K | $1.93M | 138.7/h | 0 |
| Coinbase (2) | 15.79K | $1.86M | 491.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 951 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.244 | 910 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.217 | 917 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.210 | 876 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.205 | 876 | 0.0000 |
| Total TPS moves with Slot time | +0.179 | 917 | 0.0000 |
| SOL price moves with DeFi TVL | +0.174 | 951 | 0.0000 |
| Total TPS moves with Program failure rate | +0.166 | 898 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.166 | 898 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.140 | 876 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 118.08 USD | Jupiter (on-chain DEX): 118.12 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 589.09M SOL | CoinGecko: 589.09M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-06

**Open SIMD proposals:**

- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-05
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-06
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01

**Recently merged SIMDs:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23

**Latest Agave release:** [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03)

**Latest Firedancer release:** [v26.09.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.6) (2026-10-06)

## Ecosystem news

- **[Solana treasury DeFi Development authorizes CHAD preferred stock buyback program](https://www.theblock.co/news/markets/2026-10-06-defi-development-chad-preferred-stock-repurchase-program-417819)** - The Block, 2026-10-06
- **[Solana Debuts Institutional Settlement Standard With J.P. Morgan Input](https://decrypt.co/380126/solana-institutional-settlement-standard-jp-morgan)** - Decrypt, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06
- **[DeFi Development Corp Adds $3 Million in Solana as SOL Buys Slow](https://decrypt.co/380125/defi-development-corp-adds-3m-solana)** - Decrypt, 2026-10-05
- **[Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)** - Solana.com, 2026-10-02
- **[Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026)** - Solana.com, 2026-10-01
- **[Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)** - Solana.com, 2026-09-30
- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Solana Changelog: September 24, 2026](https://solana.com/news/solana-changelog-september-24-2026)** - Solana.com, 2026-09-24
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
