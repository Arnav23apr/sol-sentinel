# Solana Ecosystem Report

*Generated 2026-10-06 00:27 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.5K |
| TPS (non-vote) | 2.0K |
| Slot time | 265.5 ms |
| Slot | 454M |
| Block height | 432M |
| Epoch | 1050 (32.37% complete, ~21.5h remaining) |
| Lifetime transactions | 556.5B |
| Circulating supply | 588.4M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 30.70% of slots needed a priority fee (max 10.0M µlam/CU) |
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
| Stake on private (100% commission) validators | 23.63% |

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
| SOL price | $120.95 (-0.08% 24h) |
| Market cap | $71.16B (rank #7) |
| 24h volume | $2.64B |
| ATH | $293.31 (-58.76% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.80B |
| Stablecoin supply | $16.75B |
| DEX volume (24h) | $1.95B (+14.41% 1d) |
| App fees (24h, all protocols) | $16.15M |
| Chain fees (24h) | $1.01M |
| Jito MEV tips (24h) | $289.41K |
| **REV - Real Economic Value (24h)** | **$1.30M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.45B | +2.86% |
| USDT | $2.87B | +7.84% |
| USD1 | $1.40B | +0.65% |
| USDGO | $1.28B | -9.32% |
| BUIDL | $967.88M | -2.03% |
| PYUSD | $713.62M | -4.03% |
| USDG | $619.44M | -8.23% |
| USDe | $503.91M | +8.54% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $397.81M |
| Orca DEX | $296.25M |
| BisonFi | $236.72M |
| pump.fun | $184.20M |
| Raydium AMM | $175.83M |
| Manifest Trade | $136.20M |
| fomo Wallet | $134.15M |
| Meteora DLMM | $124.17M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $5.16M |
| pump.fun | $2.40M |
| Axiom | $1.20M |
| Meteora DLMM | $705.97K |
| fomo Wallet | $583.15K |
| StonkFun | $577.37K |
| pump.fun Mobile App | $492.17K |
| Raydium AMM | $455.60K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $78.77M |
| xStocks holder positions | 776.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $599.84M |

## Program activity and chain health

Chain tip lag: **+9.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 86,441 (approx.) | 55.30% | 0.5 s |
| Orca Whirlpools | 6,405 | 35.90% | 9.3 s |
| Pump.fun | 5,064 | 42.20% | 11.7 s |
| Jupiter v6 | 2,496 | 40.20% | 23.6 s |
| Raydium AMM v4 | 1,353 | 5.00% | 44.1 s |

Median failure rate across the sampled programs: **40.20%** (range 5.00% to 55.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **96.09 SOL**.

## Exchange and large-holder balances

12.54M SOL ($1.52B) across 8 publicly-attributed accounts. Net **7K SOL (0.06%) moved off exchanges** over the last 22.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.28B | 0.3/h | 1 |
| Binance (2) | 1.24M | $149.79M | 1.1K/h | 0 |
| Bybit | 303.37K | $36.69M | 23.6/h | 0 |
| Gate.io | 215.48K | $26.06M | 234.5/h | 2 |
| Bitget | 99.40K | $12.02M | 7.7K/h | 0 |
| Coinbase (2) | 78.60K | $9.51M | 479.4/h | 0 |
| Kraken | 23.93K | $2.89M | 371.9/h | 0 |
| Coinbase | 11.54K | $1.40M | 289.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 945 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.247 | 904 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.220 | 911 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 870 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.203 | 870 | 0.0000 |
| Total TPS moves with Slot time | +0.182 | 911 | 0.0000 |
| SOL price moves with DeFi TVL | +0.172 | 945 | 0.0000 |
| Total TPS moves with Program failure rate | +0.159 | 892 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.158 | 892 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 870 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 120.95 USD | Jupiter (on-chain DEX): 120.90 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 588.39M SOL | CoinGecko: 588.38M SOL | 0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-05

**Open SIMD proposals:**

- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-05
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-05
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23

**Latest Agave release:** [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03)

**Latest Firedancer release:** [v26.09.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.5) (2026-09-28)

## Ecosystem news

- **[DeFi Development Corp Adds $3 Million in Solana as SOL Buys Slow](https://decrypt.co/380125/defi-development-corp-adds-3m-solana)** - Decrypt, 2026-10-05
- **[DeFi Development sees NAV per share more than doubling, holds 2.56 million SOL](https://www.theblock.co/news/markets/2026-10-05-defi-development-nav-per-share-doubles-2-56-million-sol-417674)** - The Block, 2026-10-05
- **[Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)** - Solana.com, 2026-10-02
- **[Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana)** - Solana.com, 2026-09-30
- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
