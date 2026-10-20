# Solana Ecosystem Report

*Generated 2026-10-20 00:47 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.9K |
| TPS (non-vote) | 1.9K |
| Slot time | 218.2 ms |
| Slot | 459M |
| Block height | 437M |
| Epoch | 1062 (58.54% complete, ~10.9h remaining) |
| Lifetime transactions | 562.4B |
| Circulating supply | 589.5M SOL |
| Inflation (annual) | 3.60% |
| AMM write-lock congestion (150-slot window) | 16.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 668 |
| Delinquent validators | 11 |
| Delinquent stake | 0.00% |
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
| SOL price | $104.70 (+0.27% 24h) |
| Market cap | $61.72B (rank #7) |
| 24h volume | $2.63B |
| ATH | $293.31 (-64.30% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.87B |
| Stablecoin supply | $15.63B |
| DEX volume (24h) | $1.70B (+35.52% 1d) |
| App fees (24h, all protocols) | $9.84M |
| Chain fees (24h) | $641.35K |
| Jito MEV tips (24h) | $166.22K |
| **REV - Real Economic Value (24h)** | **$807.57K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.88B | +1.36% |
| USDT | $2.69B | -6.26% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.27B | -1.63% |
| BUIDL | $886.03M | -4.84% |
| PYUSD | $695.49M | -2.22% |
| USDG | $632.97M | +0.63% |
| USDe | $390.04M | -19.14% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $467.32M |
| Orca DEX | $240.02M |
| BisonFi | $235.99M |
| Raydium AMM | $166.44M |
| pump.fun | $140.77M |
| Manifest Trade | $104.53M |
| Tessera V | $99.83M |
| Meteora DLMM | $78.59M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.91M |
| pump.fun | $1.74M |
| Axiom | $668.31K |
| Collector Crypt | $536.41K |
| Raydium AMM | $407.55K |
| Meteora DLMM | $369.27K |
| pump.fun Mobile App | $341.76K |
| Sanctum Validator LSTs | $279.75K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $46.53M |
| xStocks holder positions | 836.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $613.33M |

## Program activity and chain health

Chain tip lag: **+8.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 43,676 | 26.30% | 1.3 s |
| Pump.fun | 10,301 | 68.40% | 5.7 s |
| Orca Whirlpools | 4,360 | 9.80% | 13.5 s |
| Raydium AMM v4 | 3,789 | 17.00% | 15.7 s |
| Jupiter v6 | 3,611 | 37.40% | 16.6 s |

Median failure rate across the sampled programs: **26.30%** (range 9.80% to 68.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **112.19 SOL**.

## Exchange and large-holder balances

13.31M SOL ($1.39B) across 8 publicly-attributed accounts. Net **66K SOL (0.49%) moved off exchanges** over the last 19.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.17B | 0.2/h | 4 |
| Binance (2) | 1.36M | $142.45M | 949.9/h | 0 |
| Bybit | 330.78K | $34.63M | 16.5/h | 0 |
| Gate.io | 313.16K | $32.79M | 90.2/h | 0 |
| Bitget | 82.25K | $8.61M | 87.9/h | 0 |
| Kraken | 20.51K | $2.15M | 231.4/h | 0 |
| Coinbase | 16.33K | $1.71M | 612.2/h | 0 |
| Coinbase (2) | 14.96K | $1.57M | 214/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 15 of 117 tested pairs survive, over 1018 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.268 | 977 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 984 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.200 | 943 | 0.0000 |
| SOL price moves with DeFi TVL | +0.193 | 1018 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.191 | 943 | 0.0000 |
| Total TPS moves with Slot time | +0.190 | 984 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 965 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 965 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 943 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.107 | 943 | 0.0009 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 104.70 USD | Jupiter (on-chain DEX): 104.57 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 589.49M SOL | CoinGecko: 589.49M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-16
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15

**Open SIMD proposals:**

- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-19
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-19
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

- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[SkyAI sells off entire Solana treasury as it launches $201 million buyback](https://www.theblock.co/news/business/2026-10-19-skyai-sells-off-entire-solana-treasury-launches-201-million-buyback-421037)** - The Block, 2026-10-19
- **[GTA 6 Trailer Features Meme Coin—And Solana Copycat Soars 2,900%](https://decrypt.co/381122/gta-6-trailer-features-meme-coin-and-solana-copycat-soars-2900)** - Decrypt, 2026-10-16
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
