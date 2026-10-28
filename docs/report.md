# Solana Ecosystem Report

*Generated 2026-10-28 02:27 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 9.7 robust standard deviations above its 7-day baseline: a 1242.4% move to 0.89 % from a typical 0.07.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.6K |
| TPS (non-vote) | 1.6K |
| Slot time | 212.4 ms |
| Slot | 462M |
| Block height | 440M |
| Epoch | 1070 (15.50% complete, ~21.5h remaining) |
| Lifetime transactions | 564.1B |
| Circulating supply | 589.9M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 29 |
| Delinquent stake | 0.89% |
| Total active stake | 433.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.46% / 24.79% / 36.02% |
| Commission (stake-weighted, delegatable validators) | 3.73% |
| Stake on private (100% commission) validators | 24.11% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.84% | 0% |
| 3 | `3N7s…iD5g` | 12.8M | 2.95% | 0% |
| 4 | `8Gbw…F8iD` | 10.8M | 2.50% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.24% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.62% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.58 (+1.18% 24h) |
| Market cap | $59.96B (rank #7) |
| 24h volume | $2.03B |
| ATH | $293.31 (-65.37% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.74B |
| Stablecoin supply | $15.50B |
| DEX volume (24h) | $1.85B (-10.72% 1d) |
| App fees (24h, all protocols) | $11.08M |
| Chain fees (24h) | $568.35K |
| Jito MEV tips (24h) | $134.30K |
| **REV - Real Economic Value (24h)** | **$702.64K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.71B | -3.68% |
| USDT | $2.81B | +4.45% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.29B | +0.23% |
| BUIDL | $878.04M | -0.91% |
| PYUSD | $694.67M | +2.85% |
| USDG | $611.87M | -2.93% |
| USDe | $316.85M | -18.53% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $293.05M |
| Manifest Trade | $214.46M |
| Tessera V | $183.66M |
| PumpSwap | $167.04M |
| Orca DEX | $157.46M |
| pump.fun | $146.85M |
| Raydium AMM | $122.57M |
| Meteora DLMM | $80.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.00M |
| pump.fun | $1.97M |
| Axiom | $645.78K |
| Collector Crypt | $559.31K |
| Meteora DLMM | $323.86K |
| pump.fun Mobile App | $294.01K |
| Sanctum Validator LSTs | $277.75K |
| Raydium AMM | $261.05K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $40.65M |
| xStocks holder positions | 848.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $601.92M |

## Program activity and chain health

Chain tip lag: **+0.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 39,629 | 38.80% | 1.5 s |
| Pump.fun | 9,256 | 70.10% | 6.4 s |
| Jupiter v6 | 5,293 | 66.00% | 11.3 s |
| Orca Whirlpools | 3,471 | 65.60% | 17 s |
| Raydium AMM v4 | 459 | 18.10% | 130.4 s |

Median failure rate across the sampled programs: **65.60%** (range 18.10% to 70.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **523.79 SOL**.

## Exchange and large-holder balances

13.27M SOL ($1.35B) across 8 publicly-attributed accounts. Net **35K SOL (0.26%) moved off exchanges** over the last 18.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.14B | 0.2/h | 4 |
| Binance (2) | 1.24M | $125.58M | 873.8/h | 0 |
| Gate.io | 363.41K | $36.92M | 144.4/h | 0 |
| Bybit | 330.88K | $33.61M | 31.7/h | 0 |
| Bitget | 105.55K | $10.72M | 130.4/h | 0 |
| Kraken | 33.49K | $3.40M | 212.5/h | 0 |
| Coinbase | 11.62K | $1.18M | 271.3/h | 0 |
| Coinbase (2) | 11.58K | $1.18M | 291.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1066 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.257 | 1025 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.233 | 1032 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.221 | 991 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.216 | 991 | 0.0000 |
| SOL price moves with DeFi TVL | +0.207 | 1066 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1032 | 0.0000 |
| Total TPS moves with Program failure rate | +0.160 | 1013 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.160 | 1013 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 991 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.115 | 991 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 101.58 USD | Jupiter (on-chain DEX): 101.37 USD | +0.21% | agree |
| Circulating supply | getSupply (RPC): 589.93M SOL | CoinGecko: 589.93M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-27
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
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

**Latest Firedancer release:** [v26.10.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.5) (2026-10-27)

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
