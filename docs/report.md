# Solana Ecosystem Report

*Generated 2026-10-27 19:44 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.3K |
| TPS (non-vote) | 2.3K |
| Slot time | 213.9 ms |
| Slot | 462M |
| Block height | 440M |
| Epoch | 1069 (89.22% complete, ~2.8h remaining) |
| Lifetime transactions | 564.0B |
| Circulating supply | 589.9M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 3.3M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 665 |
| Delinquent validators | 20 |
| Delinquent stake | 0.09% |
| Total active stake | 436.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.32% / 24.60% / 35.70% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.95% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.6M | 3.81% | 0% |
| 3 | `3N7s…iD5g` | 12.7M | 2.90% | 0% |
| 4 | `8Gbw…F8iD` | 10.8M | 2.48% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.08 (+0.67% 24h) |
| Market cap | $59.63B (rank #7) |
| 24h volume | $2.04B |
| ATH | $293.31 (-65.54% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.72B |
| Stablecoin supply | $15.42B |
| DEX volume (24h) | $2.07B (+42.91% 1d) |
| App fees (24h, all protocols) | $11.67M |
| Chain fees (24h) | $568.35K |
| Jito MEV tips (24h) | $134.30K |
| **REV - Real Economic Value (24h)** | **$702.64K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.67B | -2.97% |
| USDT | $2.81B | +4.45% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.29B | +1.57% |
| BUIDL | $878.76M | -0.82% |
| PYUSD | $663.52M | -4.57% |
| USDG | $612.81M | -3.13% |
| USDe | $317.23M | -18.59% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $293.05M |
| Manifest Trade | $264.36M |
| Tessera V | $183.66M |
| Orca DEX | $171.26M |
| PumpSwap | $167.04M |
| pump.fun | $146.85M |
| Raydium AMM | $128.98M |
| Meteora DLMM | $113.45M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.08M |
| pump.fun | $1.97M |
| Axiom | $745.11K |
| Collector Crypt | $559.31K |
| Meteora DLMM | $419.10K |
| pump.fun Mobile App | $275.38K |
| Sanctum Validator LSTs | $273.74K |
| Meteora DAMM V2 | $266.87K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $52.36M |
| xStocks holder positions | 849.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $601.33M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 75,456 | 41.60% | 0.6 s |
| Pump.fun | 10,336 | 61.60% | 5.6 s |
| Jupiter v6 | 5,944 | 55.70% | 10.1 s |
| Orca Whirlpools | 3,873 | 49.30% | 15.4 s |
| Raydium AMM v4 | 773 | 10.40% | 77.4 s |

Median failure rate across the sampled programs: **49.30%** (range 10.40% to 61.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **118.39 SOL**.

## Exchange and large-holder balances

13.28M SOL ($1.34B) across 8 publicly-attributed accounts. Net **32K SOL (0.24%) moved onto exchanges** over the last 20.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.13B | 0.2/h | 4 |
| Binance (2) | 1.25M | $126.52M | 1.6K/h | 0 |
| Gate.io | 363.94K | $36.79M | 127.8/h | 0 |
| Bybit | 330.88K | $33.44M | 25.9/h | 0 |
| Bitget | 103.30K | $10.44M | 133.2/h | 0 |
| Kraken | 28.71K | $2.90M | 299/h | 0 |
| Coinbase (2) | 14.82K | $1.50M | 277.1/h | 0 |
| Coinbase | 12.37K | $1.25M | 255.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1064 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.254 | 1023 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 1030 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.221 | 989 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.216 | 989 | 0.0000 |
| SOL price moves with DeFi TVL | +0.205 | 1064 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1030 | 0.0000 |
| Total TPS moves with Program failure rate | +0.160 | 1011 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.160 | 1011 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 989 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.112 | 989 | 0.0004 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 101.08 USD | Jupiter (on-chain DEX): 101.16 USD | -0.08% | agree |
| Circulating supply | getSupply (RPC): 589.87M SOL | CoinGecko: 589.87M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-27
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-27
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-27
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

**Recently merged SIMDs:**

- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-10-27
- [SIMD-0688: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-27
- [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-26
- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-24
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-23
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-23

**Latest Agave release:** [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) (2026-10-26)

**Latest Firedancer release:** [v26.10.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.4) (2026-10-21)

## Ecosystem news

- **[Solana Breakpoint 2026 Adds Revolut Chair, Former Prime Minister, Former Chancellor and City Leaders to London Lineup](https://solana.com/news/breakpoint-london-lineup)** - Solana.com, 2026-10-26
- **[Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026)** - Solana.com, 2026-10-23
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026)** - Solana.com, 2026-10-16
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
