# Solana Ecosystem Report

*Generated 2026-09-30 16:00 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 10.8 robust standard deviations above its 7-day baseline: a 600.0% move to 0.06 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.2K |
| Slot time | 267.3 ms |
| Slot | 452M |
| Block height | 430M |
| Epoch | 1046 (32.40% complete, ~21.7h remaining) |
| Lifetime transactions | 554.5B |
| Circulating supply | 588.0M SOL |
| Inflation (annual) | 3.62% |
| AMM write-lock congestion (150-slot window) | 34.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 12 |
| Delinquent stake | 0.06% |
| Total active stake | 440.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.45% / 24.48% / 35.38% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.70% |

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
| SOL price | $119.32 (+1.09% 24h) |
| Market cap | $70.15B (rank #7) |
| 24h volume | $4.06B |
| ATH | $293.31 (-59.32% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.55B |
| Stablecoin supply | $16.38B |
| DEX volume (24h) | $2.53B (-4.80% 1d) |
| App fees (24h, all protocols) | $14.86M |
| Chain fees (24h) | $1.07M |
| Jito MEV tips (24h) | $225.60K |
| **REV - Real Economic Value (24h)** | **$1.29M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.37B | -7.42% |
| USDT | $2.74B | +28.51% |
| USD1 | $1.39B | +1.46% |
| USDGO | $1.19B | -15.47% |
| BUIDL | $964.23M | -2.37% |
| PYUSD | $743.87M | +0.70% |
| USDG | $656.32M | +4.23% |
| USDe | $447.41M | -10.95% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $374.43M |
| BisonFi | $349.04M |
| PumpSwap | $337.46M |
| Raydium AMM | $290.71M |
| Meteora DLMM | $189.70M |
| fomo Wallet | $178.89M |
| pump.fun | $142.82M |
| Manifest Trade | $141.27M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.71M |
| pump.fun | $2.02M |
| Axiom | $1.26M |
| StonkFun | $1.17M |
| Meteora DLMM | $835.44K |
| Collector Crypt | $719.16K |
| Raydium AMM | $712.36K |
| fomo Wallet | $511.31K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $175.77M |
| xStocks holder positions | 739.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $539.00M |

## Program activity and chain health

Chain tip lag: **+11.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 108,642 (approx.) | 34.50% | 0.5 s |
| Pump.fun | 52,189 | 91.20% | 1.1 s |
| Jupiter v6 | 14,905 | 63.70% | 4 s |
| Orca Whirlpools | 4,476 | 64.10% | 13.4 s |
| Raydium AMM v4 | 1,301 | 11.80% | 45.7 s |

Median failure rate across the sampled programs: **63.70%** (range 11.80% to 91.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.46 SOL**.

## Exchange and large-holder balances

12.51M SOL ($1.49B) across 8 publicly-attributed accounts. Net **88K SOL (0.71%) moved onto exchanges** over the last 20.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.77M | $1.29B | 0.3/h | 0 |
| Binance (2) | 994.79K | $118.70M | 1.1K/h | 0 |
| Bybit | 387.52K | $46.24M | 35.8/h | 0 |
| Gate.io | 255.16K | $30.45M | 249.5/h | 3 |
| Kraken | 30.39K | $3.63M | 409.6/h | 0 |
| Coinbase (2) | 25.93K | $3.09M | 377/h | 0 |
| Bitget | 24.65K | $2.94M | 228/h | 0 |
| Coinbase | 19.17K | $2.29M | 446.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 919 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.228 | 878 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.218 | 885 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.207 | 844 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.201 | 844 | 0.0000 |
| Total TPS moves with Slot time | +0.179 | 885 | 0.0000 |
| SOL price moves with DeFi TVL | +0.153 | 919 | 0.0000 |
| Total TPS moves with Program failure rate | +0.152 | 866 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.151 | 866 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.144 | 844 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 119.32 USD | Jupiter (on-chain DEX): 119.15 USD | +0.14% | agree |
| Circulating supply | getSupply (RPC): 588.01M SOL | CoinGecko: 588.01M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-09-30
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16

**Open SIMD proposals:**

- [SIMD-0677: Vote Account Commission History](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-09-30
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-09-30
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

- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1)** - Solana.com, 2026-09-18
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026)** - Solana.com, 2026-09-14
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
