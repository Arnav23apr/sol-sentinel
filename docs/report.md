# Solana Ecosystem Report

*Generated 2026-10-20 10:17 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.4 robust standard deviations above its 7-day baseline: a 650.0% move to 0.03 % from a typical 0.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.5K |
| TPS (non-vote) | 1.4K |
| Slot time | 216.6 ms |
| Slot | 459M |
| Block height | 437M |
| Epoch | 1062 (94.92% complete, ~1.3h remaining) |
| Lifetime transactions | 562.5B |
| Circulating supply | 589.5M SOL |
| Inflation (annual) | 3.60% |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 4.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 666 |
| Delinquent validators | 13 |
| Delinquent stake | 0.03% |
| Total active stake | 437.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.09% / 24.28% / 35.52% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.84% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.91% | 7% |
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
| SOL price | $104.09 (-1.19% 24h) |
| Market cap | $61.38B (rank #7) |
| 24h volume | $2.36B |
| ATH | $293.31 (-64.51% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.88B |
| Stablecoin supply | $15.67B |
| DEX volume (24h) | $1.61B (-5.09% 1d) |
| App fees (24h, all protocols) | $11.95M |
| Chain fees (24h) | $781.53K |
| Jito MEV tips (24h) | $173.12K |
| **REV - Real Economic Value (24h)** | **$954.65K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.90B | +2.18% |
| USDT | $2.69B | -4.60% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.29B | -0.70% |
| BUIDL | $886.03M | -4.84% |
| PYUSD | $688.05M | -2.85% |
| USDG | $633.13M | +1.08% |
| USDe | $400.63M | -14.28% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $241.01M |
| BisonFi | $235.99M |
| Raydium AMM | $154.66M |
| PumpSwap | $142.12M |
| pump.fun | $140.77M |
| Manifest Trade | $110.68M |
| Meteora DLMM | $110.61M |
| Tessera V | $99.83M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.13M |
| pump.fun | $2.19M |
| Collector Crypt | $1.39M |
| Axiom | $848.42K |
| Meteora DLMM | $454.28K |
| Raydium AMM | $357.43K |
| pump.fun Mobile App | $317.37K |
| Sanctum Validator LSTs | $283.74K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $45.93M |
| xStocks holder positions | 835.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $592.76M |

## Program activity and chain health

Chain tip lag: **+8.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 65,235 | 34.40% | 0.9 s |
| Pump.fun | 12,138 | 80.90% | 4.8 s |
| Jupiter v6 | 2,661 | 51.00% | 20.4 s |
| Orca Whirlpools | 2,212 | 37.70% | 27.1 s |
| Raydium AMM v4 | 777 | 14.00% | 77.1 s |

Median failure rate across the sampled programs: **37.70%** (range 14.00% to 80.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **112.19 SOL**.

## Exchange and large-holder balances

13.34M SOL ($1.39B) across 8 publicly-attributed accounts. Net **11K SOL (0.08%) moved off exchanges** over the last 23.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.16B | 0.2/h | 4 |
| Binance (2) | 1.35M | $140.62M | 1.1K/h | 0 |
| Bybit | 330.78K | $34.43M | 19.1/h | 0 |
| Gate.io | 311.27K | $32.40M | 187.9/h | 0 |
| Bitget | 85.63K | $8.91M | 267.1/h | 0 |
| Kraken | 50.51K | $5.26M | 202.2/h | 0 |
| Coinbase | 16.61K | $1.73M | 148.1/h | 0 |
| Coinbase (2) | 14.73K | $1.53M | 115.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 15 of 117 tested pairs survive, over 1020 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.263 | 979 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 986 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.200 | 945 | 0.0000 |
| SOL price moves with DeFi TVL | +0.195 | 1020 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.191 | 945 | 0.0000 |
| Total TPS moves with Slot time | +0.190 | 986 | 0.0000 |
| Total TPS moves with Program failure rate | +0.160 | 967 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.160 | 967 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 945 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.107 | 945 | 0.0010 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 104.09 USD | Jupiter (on-chain DEX): 104.08 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 589.49M SOL | CoinGecko: 589.49M SOL | -0.00% | agree |

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
