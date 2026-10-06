# Solana Ecosystem Report

*Generated 2026-10-06 19:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.2K |
| TPS (non-vote) | 2.7K |
| Slot time | 272.1 ms |
| Slot | 454M |
| Block height | 432M |
| Epoch | 1050 (90.65% complete, ~3.1h remaining) |
| Lifetime transactions | 556.8B |
| Circulating supply | 588.4M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 22.00% of slots needed a priority fee (max 11.2M µlam/CU) |
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
| SOL price | $120.62 (+0.45% 24h) |
| Market cap | $70.98B (rank #7) |
| 24h volume | $2.54B |
| ATH | $293.31 (-58.88% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.63B |
| Stablecoin supply | $16.67B |
| DEX volume (24h) | $2.06B (+20.43% 1d) |
| App fees (24h, all protocols) | $15.99M |
| Chain fees (24h) | $1.04M |
| Jito MEV tips (24h) | $286.25K |
| **REV - Real Economic Value (24h)** | **$1.33M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.28B | +1.53% |
| USDT | $2.87B | +6.25% |
| USD1 | $1.41B | +1.22% |
| USDGO | $1.31B | -7.12% |
| BUIDL | $967.97M | +0.40% |
| PYUSD | $739.94M | +2.48% |
| USDG | $628.78M | -9.15% |
| USDe | $513.13M | +11.83% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $306.60M |
| Orca DEX | $282.42M |
| BisonFi | $234.22M |
| Raydium AMM | $193.75M |
| pump.fun | $187.50M |
| Meteora DLMM | $144.38M |
| Manifest Trade | $128.56M |
| fomo Wallet | $122.19M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.45M |
| pump.fun | $2.59M |
| Axiom | $1.28M |
| Meteora DLMM | $678.40K |
| GMX Solana | $529.43K |
| fomo Wallet | $470.81K |
| pump.fun Mobile App | $441.86K |
| Collector Crypt | $428.28K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $81.76M |
| xStocks holder positions | 782.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $597.67M |

## Program activity and chain health

Chain tip lag: **+10.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 70,783 | 29.70% | 0.8 s |
| Pump.fun | 26,929 | 70.30% | 2.2 s |
| Jupiter v6 | 7,474 | 74.40% | 7.9 s |
| Orca Whirlpools | 2,834 | 33.00% | 20.4 s |
| Raydium AMM v4 | 1,457 | 38.20% | 41.1 s |

Median failure rate across the sampled programs: **38.20%** (range 29.70% to 74.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **86.81 SOL**.

## Exchange and large-holder balances

12.37M SOL ($1.49B) across 8 publicly-attributed accounts. Net **171K SOL (1.37%) moved off exchanges** over the last 18.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.28B | 0.3/h | 1 |
| Binance (2) | 1.14M | $136.96M | 1.6K/h | 0 |
| Bybit | 295.81K | $35.68M | 40.5/h | 0 |
| Gate.io | 211.72K | $25.54M | 173.4/h | 2 |
| Bitget | 82.65K | $9.97M | 6.3K/h | 0 |
| Kraken | 33.65K | $4.06M | 394.3/h | 0 |
| Coinbase | 21.34K | $2.57M | 358.9/h | 0 |
| Coinbase (2) | 18.72K | $2.26M | 355.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 948 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.244 | 907 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.214 | 914 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.212 | 873 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.207 | 873 | 0.0000 |
| Total TPS moves with Slot time | +0.175 | 914 | 0.0000 |
| SOL price moves with DeFi TVL | +0.174 | 948 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 895 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 895 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.141 | 873 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 120.62 USD | Jupiter (on-chain DEX): 120.59 USD | +0.02% | agree |
| Circulating supply | getSupply (RPC): 588.39M SOL | CoinGecko: 588.39M SOL | -0.00% | agree |

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
