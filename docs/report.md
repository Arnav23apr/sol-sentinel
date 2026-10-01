# Solana Ecosystem Report

*Generated 2026-10-01 13:36 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 17.8 robust standard deviations above its 7-day baseline: a 987.5% move to 0.09 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.5K |
| TPS (non-vote) | 3.0K |
| Slot time | 266.7 ms |
| Slot | 452M |
| Block height | 430M |
| Epoch | 1046 (99.76% complete, ~0.1h remaining) |
| Lifetime transactions | 554.8B |
| Circulating supply | 588.0M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 23.30% of slots needed a priority fee (max 1.4M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 12 |
| Delinquent stake | 0.09% |
| Total active stake | 440.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.46% / 24.49% / 35.39% |
| Commission (stake-weighted, delegatable validators) | 3.84% |
| Stake on private (100% commission) validators | 23.71% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.2M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.61% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.80% | 0% |
| 4 | `8Gbw…F8iD` | 11.4M | 2.59% | 0% |
| 5 | `Catz…Diqb` | 11.2M | 2.55% | 5% |
| 6 | `26pV…3dJx` | 9.3M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.10% | 10% |
| 8 | `9QU2…29mF` | 7.7M | 1.74% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.48% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $117.43 (-3.71% 24h) |
| Market cap | $69.01B (rank #7) |
| 24h volume | $3.74B |
| ATH | $293.31 (-59.96% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.53B |
| Stablecoin supply | $16.22B |
| DEX volume (24h) | $2.57B (+1.41% 1d) |
| App fees (24h, all protocols) | $15.88M |
| Chain fees (24h) | $1.05M |
| Jito MEV tips (24h) | $258.85K |
| **REV - Real Economic Value (24h)** | **$1.31M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.15B | -4.37% |
| USDT | $2.78B | +30.39% |
| USD1 | $1.39B | +0.72% |
| USDGO | $1.19B | -16.30% |
| BUIDL | $964.32M | -2.37% |
| PYUSD | $753.10M | +1.17% |
| USDG | $651.75M | +3.21% |
| USDe | $444.60M | -10.62% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $403.39M |
| BisonFi | $285.04M |
| Raydium AMM | $243.35M |
| PumpSwap | $207.00M |
| Meteora DLMM | $205.40M |
| Manifest Trade | $163.55M |
| pump.fun | $155.99M |
| fomo Wallet | $146.05M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.89M |
| pump.fun | $2.14M |
| Axiom | $1.23M |
| StonkFun | $940.36K |
| Meteora DLMM | $747.19K |
| Collector Crypt | $609.87K |
| Raydium AMM | $597.50K |
| fomo Wallet | $470.58K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $113.83M |
| xStocks holder positions | 766.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $539.35M |

## Program activity and chain health

Chain tip lag: **+10.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 125,534 (approx.) | 48.70% | 0.3 s |
| Pump.fun | 14,361 | 66.70% | 3.2 s |
| Jupiter v6 | 11,886 | 83.20% | 4.8 s |
| Orca Whirlpools | 7,750 | 54.90% | 7.7 s |
| Raydium AMM v4 | 1,672 | 3.50% | 35.7 s |

Median failure rate across the sampled programs: **54.90%** (range 3.50% to 83.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.46 SOL**.

## Exchange and large-holder balances

12.39M SOL ($1.45B) across 8 publicly-attributed accounts. Net **124K SOL (0.99%) moved off exchanges** over the last 21.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.24B | 0.3/h | 0 |
| Binance (2) | 1.08M | $126.40M | 1.3K/h | 0 |
| Bybit | 387.52K | $45.51M | 25.2/h | 0 |
| Gate.io | 255.06K | $29.95M | 271.9/h | 3 |
| Bitget | 34.01K | $3.99M | 145.2/h | 0 |
| Kraken | 32.91K | $3.87M | 428.1/h | 0 |
| Coinbase (2) | 14.49K | $1.70M | 262.4/h | 0 |
| Coinbase | 12.87K | $1.51M | 298.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 923 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.227 | 882 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.221 | 889 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.207 | 848 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.202 | 848 | 0.0000 |
| Total TPS moves with Slot time | +0.182 | 889 | 0.0000 |
| SOL price moves with DeFi TVL | +0.160 | 923 | 0.0000 |
| Total TPS moves with Program failure rate | +0.158 | 870 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.157 | 870 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.145 | 848 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 117.43 USD | Jupiter (on-chain DEX): 117.66 USD | -0.20% | agree |
| Circulating supply | getSupply (RPC): 588.00M SOL | CoinGecko: 588.00M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-09-30
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16

**Open SIMD proposals:**

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-01
- [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-30
- [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29
- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16

**Latest Agave release:** [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) (2026-09-28)

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
