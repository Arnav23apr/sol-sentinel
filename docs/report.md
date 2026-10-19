# Solana Ecosystem Report

*Generated 2026-10-19 17:04 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.2K |
| TPS (non-vote) | 2.2K |
| Slot time | 217.8 ms |
| Slot | 459M |
| Block height | 437M |
| Epoch | 1062 (29.08% complete, ~18.5h remaining) |
| Lifetime transactions | 562.2B |
| Circulating supply | 589.5M SOL |
| Inflation (annual) | 3.60% |
| AMM write-lock congestion (150-slot window) | 19.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 667 |
| Delinquent validators | 12 |
| Delinquent stake | 0.01% |
| Total active stake | 437.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.08% / 24.27% / 35.51% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.83% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.90% | 7% |
| 2 | `he1i…uBtk` | 15.7M | 3.59% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `8Gbw…F8iD` | 11.0M | 2.51% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.22% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.17% | 10% |
| 7 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.60% | 5% |
| 10 | `Dumi…Zk4a` | 6.7M | 1.54% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $104.44 (+2.19% 24h) |
| Market cap | $61.56B (rank #7) |
| 24h volume | $2.91B |
| ATH | $293.31 (-64.39% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.86B |
| Stablecoin supply | $15.56B |
| DEX volume (24h) | $1.70B (+35.52% 1d) |
| App fees (24h, all protocols) | $9.84M |
| Chain fees (24h) | $641.35K |
| Jito MEV tips (24h) | $145.20K |
| **REV - Real Economic Value (24h)** | **$786.55K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.82B | +0.51% |
| USDT | $2.69B | -6.26% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.27B | -1.63% |
| BUIDL | $885.88M | -4.85% |
| PYUSD | $681.61M | -4.18% |
| USDG | $618.01M | -1.76% |
| USDe | $403.16M | -16.41% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $467.32M |
| Orca DEX | $242.67M |
| BisonFi | $235.99M |
| pump.fun | $140.77M |
| Raydium AMM | $135.62M |
| Tessera V | $99.83M |
| Manifest Trade | $88.89M |
| Meteora DLMM | $78.59M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.91M |
| pump.fun | $1.74M |
| Axiom | $668.31K |
| Meteora DLMM | $369.27K |
| Collector Crypt | $366.35K |
| pump.fun Mobile App | $341.76K |
| Sanctum Validator LSTs | $279.75K |
| Raydium AMM | $274.02K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $45.26M |
| xStocks holder positions | 836.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $612.78M |

## Program activity and chain health

Chain tip lag: **+8.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 81,451 | 44.60% | 0.7 s |
| Pump.fun | 14,180 | 65.30% | 4.1 s |
| Orca Whirlpools | 5,611 | 69.40% | 10.7 s |
| Jupiter v6 | 5,061 | 52.20% | 11.8 s |
| Raydium AMM v4 | 850 | 13.50% | 70.3 s |

Median failure rate across the sampled programs: **52.20%** (range 13.50% to 69.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **112.19 SOL**.

## Exchange and large-holder balances

13.36M SOL ($1.40B) across 8 publicly-attributed accounts. Net **44K SOL (0.33%) moved onto exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.17B | 0.2/h | 4 |
| Binance (2) | 1.40M | $146.29M | 1.3K/h | 0 |
| Bybit | 328.74K | $34.33M | 25.3/h | 0 |
| Gate.io | 312.79K | $32.67M | 136.2/h | 0 |
| Bitget | 86.87K | $9.07M | 178.1/h | 0 |
| Kraken | 29.20K | $3.05M | 342.9/h | 0 |
| Coinbase (2) | 16.49K | $1.72M | 241/h | 0 |
| Coinbase | 13.47K | $1.41M | 329.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 15 of 117 tested pairs survive, over 1016 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.268 | 975 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 982 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.203 | 941 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.194 | 941 | 0.0000 |
| SOL price moves with DeFi TVL | +0.194 | 1016 | 0.0000 |
| Total TPS moves with Slot time | +0.191 | 982 | 0.0000 |
| Total TPS moves with Program failure rate | +0.158 | 963 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.158 | 963 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 941 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.111 | 941 | 0.0006 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 104.44 USD | Jupiter (on-chain DEX): 104.43 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 589.49M SOL | CoinGecko: 589.49M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-16
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15

**Open SIMD proposals:**

- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-17
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14

**Recently merged SIMDs:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.2) (2026-10-14)

## Ecosystem news

- **[SkyAI sells off entire Solana treasury as it launches $201 million buyback](https://www.theblock.co/news/business/2026-10-19-skyai-sells-off-entire-solana-treasury-launches-201-million-buyback-421037)** - The Block, 2026-10-19
- **[GTA 6 Trailer Features Meme Coin—And Solana Copycat Soars 2,900%](https://decrypt.co/381122/gta-6-trailer-features-meme-coin-and-solana-copycat-soars-2900)** - Decrypt, 2026-10-16
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
