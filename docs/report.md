# Solana Ecosystem Report

*Generated 2026-10-05 09:17 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **DEX volume (24h)** (warning): DEX volume (24h) is 5.1 robust standard deviations below its 7-day baseline: a 35.2% move to 1,649,284,606.00 USD from a typical 2,544,678,620.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 1.4K |
| Slot time | 267.3 ms |
| Slot | 454M |
| Block height | 432M |
| Epoch | 1049 (85.26% complete, ~4.7h remaining) |
| Lifetime transactions | 556.3B |
| Circulating supply | 588.3M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 4.1M µlam/CU) |
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
| SOL price | $120.84 (-0.06% 24h) |
| Market cap | $71.09B (rank #7) |
| 24h volume | $2.48B |
| ATH | $293.31 (-58.80% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.72B |
| Stablecoin supply | $16.51B |
| DEX volume (24h) | $1.65B (+6.13% 1d) |
| App fees (24h, all protocols) | $15.99M |
| Chain fees (24h) | $1.01M |
| Jito MEV tips (24h) | $267.57K |
| **REV - Real Economic Value (24h)** | **$1.28M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.30B | +0.76% |
| USDT | $2.87B | +7.84% |
| USD1 | $1.40B | +0.65% |
| USDGO | $1.24B | -12.02% |
| BUIDL | $967.58M | -2.06% |
| PYUSD | $701.90M | -5.59% |
| USDG | $635.38M | -5.91% |
| USDe | $461.14M | -0.63% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $397.81M |
| Orca DEX | $246.33M |
| pump.fun | $183.58M |
| BisonFi | $171.40M |
| fomo Wallet | $152.15M |
| Raydium AMM | $150.90M |
| Axiom | $149.54M |
| Meteora DLMM | $124.17M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $5.16M |
| pump.fun | $2.40M |
| Axiom | $1.20M |
| Meteora DLMM | $705.97K |
| Collector Crypt | $496.42K |
| pump.fun Mobile App | $492.17K |
| fomo Wallet | $444.08K |
| Sanctum Validator LSTs | $385.86K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $86.39M |
| xStocks holder positions | 770.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.09M |

## Program activity and chain health

Chain tip lag: **+10.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 34,523 | 24.10% | 1.3 s |
| Pump.fun | 4,489 | 21.60% | 13.1 s |
| Jupiter v6 | 2,875 | 57.00% | 20.8 s |
| Raydium AMM v4 | 1,307 | 44.80% | 45.7 s |
| Orca Whirlpools | 1,125 | 30.40% | 53.2 s |

Median failure rate across the sampled programs: **30.40%** (range 21.60% to 57.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.47 SOL**.

## Exchange and large-holder balances

12.44M SOL ($1.50B) across 7 publicly-attributed accounts. Net **197K SOL (1.56%) moved off exchanges** over the last 20.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.28B | 0.3/h | 1 |
| Binance (2) | 1.22M | $147.77M | 1.1K/h | 0 |
| Bybit | 303.37K | $36.66M | 20/h | 0 |
| Gate.io | 225.92K | $27.30M | 225.7/h | 2 |
| Bitget | 71.56K | $8.65M | 194.7/h | 0 |
| Kraken | 23.05K | $2.79M | 219.2/h | 0 |
| Coinbase (2) | 19.15K | $2.31M | 122.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 943 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.241 | 902 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.219 | 909 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.205 | 868 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.201 | 868 | 0.0000 |
| Total TPS moves with Slot time | +0.181 | 909 | 0.0000 |
| SOL price moves with DeFi TVL | +0.167 | 943 | 0.0000 |
| Total TPS moves with Program failure rate | +0.156 | 890 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.155 | 890 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 868 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 120.84 USD | Jupiter (on-chain DEX): 120.70 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 588.31M SOL | CoinGecko: 588.31M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-05
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-04
- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-05
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-10-02
- [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-10-05

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23

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
