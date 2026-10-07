# Solana Ecosystem Report

*Generated 2026-10-07 02:31 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.2K |
| Slot time | 268.5 ms |
| Slot | 454M |
| Block height | 432M |
| Epoch | 1051 (13.24% complete, ~28.0h remaining) |
| Lifetime transactions | 557.0B |
| Circulating supply | 589.1M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 19.30% of slots needed a priority fee (max 1.4M µlam/CU) |
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
| SOL price | $117.77 (-2.34% 24h) |
| Market cap | $69.37B (rank #7) |
| 24h volume | $2.79B |
| ATH | $293.31 (-59.85% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.62B |
| Stablecoin supply | $16.65B |
| DEX volume (24h) | $2.04B (-0.87% 1d) |
| App fees (24h, all protocols) | $16.05M |
| Chain fees (24h) | $1.05M |
| Jito MEV tips (24h) | $284.29K |
| **REV - Real Economic Value (24h)** | **$1.33M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.25B | +0.52% |
| USDT | $2.87B | +5.47% |
| USD1 | $1.41B | +1.76% |
| USDGO | $1.31B | +10.03% |
| BUIDL | $967.97M | +0.39% |
| PYUSD | $715.21M | -3.12% |
| USDG | $626.23M | -2.38% |
| USDe | $540.01M | +19.01% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $302.95M |
| Orca DEX | $277.80M |
| BisonFi | $234.22M |
| pump.fun | $187.50M |
| Raydium AMM | $182.50M |
| Meteora DLMM | $154.14M |
| Axiom | $122.05M |
| fomo Wallet | $116.20M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.47M |
| pump.fun | $2.52M |
| Axiom | $1.36M |
| Meteora DLMM | $826.08K |
| fomo Wallet | $470.81K |
| Collector Crypt | $461.74K |
| Raydium AMM | $450.87K |
| StonkFun | $428.10K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $86.85M |
| xStocks holder positions | 784.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $596.28M |

## Program activity and chain health

Chain tip lag: **+9.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 57,579 | 32.60% | 0.8 s |
| Jupiter v6 | 8,397 | 72.00% | 7 s |
| Orca Whirlpools | 4,693 | 34.90% | 12.6 s |
| Pump.fun | 4,043 | 22.80% | 14.5 s |
| Raydium AMM v4 | 1,968 | 28.70% | 30.3 s |

Median failure rate across the sampled programs: **32.60%** (range 22.80% to 72.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **724.63 SOL**.

## Exchange and large-holder balances

12.28M SOL ($1.45B) across 8 publicly-attributed accounts. Net **253K SOL (2.02%) moved off exchanges** over the last 19.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.25B | 0.3/h | 1 |
| Binance (2) | 1.04M | $122.31M | 913.7/h | 0 |
| Bybit | 304.34K | $35.84M | 39.3/h | 0 |
| Gate.io | 214.43K | $25.25M | 292.4/h | 2 |
| Bitget | 86.37K | $10.17M | 7.7K/h | 0 |
| Kraken | 31.76K | $3.74M | 343.5/h | 0 |
| Coinbase | 18.36K | $2.16M | 329.1/h | 0 |
| Coinbase (2) | 16.53K | $1.95M | 315/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 950 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.247 | 909 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.215 | 916 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.212 | 875 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.207 | 875 | 0.0000 |
| Total TPS moves with Slot time | +0.177 | 916 | 0.0000 |
| SOL price moves with DeFi TVL | +0.176 | 950 | 0.0000 |
| Total TPS moves with Program failure rate | +0.165 | 897 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 897 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.141 | 875 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 117.77 USD | Jupiter (on-chain DEX): 117.97 USD | -0.17% | agree |
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
- **[DeFi Development sees NAV per share more than doubling, holds 2.56 million SOL](https://www.theblock.co/news/markets/2026-10-05-defi-development-nav-per-share-doubles-2-56-million-sol-417674)** - The Block, 2026-10-05
- **[Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)** - Solana.com, 2026-10-02
- **[Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)** - Solana.com, 2026-09-30
- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
