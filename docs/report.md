# Solana Ecosystem Report

*Generated 2026-10-20 15:13 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.9K |
| TPS (non-vote) | 2.7K |
| Slot time | 219.4 ms |
| Slot | 459M |
| Block height | 437M |
| Epoch | 1063 (13.80% complete, ~22.7h remaining) |
| Lifetime transactions | 562.6B |
| Circulating supply | 589.5M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 25.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 669 |
| Delinquent validators | 10 |
| Delinquent stake | 0.00% |
| Total active stake | 438.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.10% / 24.35% / 35.56% |
| Commission (stake-weighted, delegatable validators) | 3.75% |
| Stake on private (100% commission) validators | 23.79% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.90% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.63% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.49% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.22% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.16% | 10% |
| 7 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.60% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $106.92 (+2.20% 24h) |
| Market cap | $63.02B (rank #7) |
| 24h volume | $2.51B |
| ATH | $293.31 (-63.55% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.88B |
| Stablecoin supply | $15.68B |
| DEX volume (24h) | $1.82B (+7.44% 1d) |
| App fees (24h, all protocols) | $11.99M |
| Chain fees (24h) | $781.53K |
| Jito MEV tips (24h) | $166.32K |
| **REV - Real Economic Value (24h)** | **$947.85K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.94B | +2.81% |
| USDT | $2.69B | -4.60% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.29B | -0.32% |
| BUIDL | $886.03M | -4.84% |
| PYUSD | $671.85M | -5.15% |
| USDG | $632.63M | +1.00% |
| USDe | $400.31M | -14.33% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $249.62M |
| Orca DEX | $241.80M |
| pump.fun | $168.22M |
| Raydium AMM | $159.22M |
| PumpSwap | $142.12M |
| Tessera V | $141.42M |
| Manifest Trade | $115.60M |
| Meteora DLMM | $110.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.13M |
| pump.fun | $2.19M |
| Collector Crypt | $1.64M |
| Axiom | $848.42K |
| Meteora DLMM | $454.28K |
| Raydium AMM | $334.09K |
| pump.fun Mobile App | $317.37K |
| Sanctum Validator LSTs | $283.74K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $52.42M |
| xStocks holder positions | 837.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $592.61M |

## Program activity and chain health

Chain tip lag: **+7.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 123,473 (approx.) | 63.30% | 0.4 s |
| Pump.fun | 42,662 | 92.10% | 1.3 s |
| Jupiter v6 | 36,841 | 87.10% | 1.5 s |
| Orca Whirlpools | 29,125 | 54.90% | 1.8 s |
| Raydium AMM v4 | 2,841 | 37.80% | 20.8 s |

Median failure rate across the sampled programs: **63.30%** (range 37.80% to 92.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **257.44 SOL**.

## Exchange and large-holder balances

13.44M SOL ($1.44B) across 8 publicly-attributed accounts. Net **79K SOL (0.59%) moved onto exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.19B | 0.2/h | 4 |
| Binance (2) | 1.42M | $152.23M | 1.8K/h | 0 |
| Bybit | 330.78K | $35.37M | 24.9/h | 0 |
| Gate.io | 311.34K | $33.29M | 278/h | 0 |
| Bitget | 87.44K | $9.35M | 245.1/h | 0 |
| Kraken | 46.22K | $4.94M | 357.9/h | 0 |
| Coinbase | 34.88K | $3.73M | 278/h | 0 |
| Coinbase (2) | 33.16K | $3.55M | 228.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1021 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.265 | 980 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 987 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.202 | 946 | 0.0000 |
| SOL price moves with DeFi TVL | +0.196 | 1021 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.193 | 946 | 0.0000 |
| Total TPS moves with Slot time | +0.191 | 987 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 968 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 968 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.152 | 946 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.109 | 946 | 0.0008 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 106.92 USD | Jupiter (on-chain DEX): 105.29 USD | +1.54% | agree |
| Circulating supply | getSupply (RPC): 589.55M SOL | CoinGecko: 589.55M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-16

**Open SIMD proposals:**

- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-20
- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-19
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14

**Recently merged SIMDs:**

- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-20
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-20
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.3](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.3) (2026-10-20)

## Ecosystem news

- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[SkyAI sells off entire Solana treasury as it launches $201 million buyback](https://www.theblock.co/news/business/2026-10-19-skyai-sells-off-entire-solana-treasury-launches-201-million-buyback-421037)** - The Block, 2026-10-19
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
