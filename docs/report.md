# Solana Ecosystem Report

*Generated 2026-09-29 15:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 18.9 robust standard deviations above its 7-day baseline: a 1050.0% move to 0.09 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.8K |
| TPS (non-vote) | 2.3K |
| Slot time | 266.7 ms |
| Slot | 452M |
| Block height | 430M |
| Epoch | 1045 (55.20% complete, ~14.3h remaining) |
| Lifetime transactions | 554.1B |
| Circulating supply | 587.9M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 26.70% of slots needed a priority fee (max 20.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 11 |
| Delinquent stake | 0.09% |
| Total active stake | 440.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.55% / 24.47% / 35.37% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.67% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.80% | 0% |
| 4 | `8Gbw…F8iD` | 11.3M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.2M | 2.54% | 5% |
| 6 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.09% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 6.7M | 1.52% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.48% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $119.62 (+1.53% 24h) |
| Market cap | $70.32B (est.) |
| 24h volume | - |
| Price source | jupiter |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.55B |
| Stablecoin supply | $16.15B |
| DEX volume (24h) | $2.66B (+38.18% 1d) |
| App fees (24h, all protocols) | $17.51M |
| Chain fees (24h) | $1.06M |
| Jito MEV tips (24h) | $225.01K |
| **REV - Real Economic Value (24h)** | **$1.29M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.22B | -12.86% |
| USDT | $2.72B | +27.62% |
| USD1 | $1.39B | +2.90% |
| USDGO | $1.19B | -15.47% |
| BUIDL | $964.13M | -2.95% |
| PYUSD | $708.54M | -3.09% |
| USDG | $641.48M | +3.31% |
| USDe | $454.49M | -9.48% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $381.95M |
| Orca DEX | $381.64M |
| PumpSwap | $268.39M |
| Raydium AMM | $223.20M |
| Meteora DLMM | $205.60M |
| pump.fun | $162.03M |
| Tessera V | $142.20M |
| fomo Wallet | $138.21M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $5.50M |
| pump.fun | $2.23M |
| Axiom | $1.13M |
| Meteora DLMM | $813.07K |
| Collector Crypt | $632.69K |
| StonkFun | $601.02K |
| Raydium AMM | $586.25K |
| GMX Solana | $424.66K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $90.31M |
| xStocks holder positions | 678.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $542.14M |

## Program activity and chain health

Chain tip lag: **+10.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 31,459 | 24.10% | 1.6 s |
| Jupiter v6 | 8,981 | 69.60% | 6.7 s |
| Pump.fun | 6,180 | 55.70% | 9.6 s |
| Orca Whirlpools | 5,465 | 56.70% | 10.9 s |
| Raydium AMM v4 | 937 | 20.70% | 63.7 s |

Median failure rate across the sampled programs: **55.70%** (range 20.70% to 69.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.46 SOL**.

## Exchange and large-holder balances

12.53M SOL ($1.50B) across 8 publicly-attributed accounts. Net **11K SOL (0.09%) moved off exchanges** over the last 23.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.77M | $1.29B | 0.2/h | 0 |
| Binance (2) | 1.04M | $124.45M | 1.3K/h | 0 |
| Bybit | 387.39K | $46.34M | 101.2/h | 0 |
| Gate.io | 241.88K | $28.93M | 308.7/h | 1 |
| Kraken | 35.31K | $4.22M | 375.4/h | 0 |
| Bitget | 19.34K | $2.31M | 40.3/h | 0 |
| Coinbase | 15.58K | $1.86M | 301.3/h | 0 |
| Coinbase (2) | 13.33K | $1.59M | 515/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 914 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.228 | 873 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.215 | 880 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.199 | 839 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.194 | 839 | 0.0000 |
| Total TPS moves with Slot time | +0.176 | 880 | 0.0000 |
| Total TPS moves with Program failure rate | +0.151 | 861 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.150 | 861 | 0.0000 |
| SOL price moves with DeFi TVL | +0.142 | 914 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.139 | 839 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16

**Open SIMD proposals:**

- [SIMD-0675: Geo-Aware Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/675) - updated 2026-09-29
- [SIMD-0674: Validator Location Registration](https://github.com/solana-foundation/solana-improvement-documents/pull/674) - updated 2026-09-29
- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15

**Latest Agave release:** [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) (2026-09-28)

**Latest Firedancer release:** [v26.09.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.5) (2026-09-28)

## Ecosystem news

- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Bitcoin Rally Slows as $15.6 Billion Options Expiry Hits—XRP and Solana Keep Climbing](https://decrypt.co/379319/bitcoin-slows-billion-options-expiry-xrp-solana)** - Decrypt, 2026-09-25
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1)** - Solana.com, 2026-09-18
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026)** - Solana.com, 2026-09-14

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
