# Solana Ecosystem Report

*Generated 2026-10-29 19:19 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 10.1 robust standard deviations above its 7-day baseline: a 897.6% move to 1.23 % from a typical 0.12.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.8K |
| TPS (non-vote) | 1.8K |
| Slot time | 213.5 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1071 (75.07% complete, ~6.4h remaining) |
| Lifetime transactions | 564.3B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 8.00% of slots needed a priority fee (max 996.8K µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 663 |
| Delinquent validators | 26 |
| Delinquent stake | 1.23% |
| Total active stake | 431.4M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.54% / 24.83% / 36.25% |
| Commission (stake-weighted, delegatable validators) | 3.74% |
| Stake on private (100% commission) validators | 24.22% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.95% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 12.9M | 2.99% | 0% |
| 4 | `8Gbw…F8iD` | 10.8M | 2.49% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.25% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.19% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.80% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `CvSb…wycB` | 6.6M | 1.54% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $100.21 (-1.76% 24h) |
| Market cap | $59.12B (rank #7) |
| 24h volume | $2.88B |
| ATH | $293.31 (-65.84% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.70B |
| Stablecoin supply | $15.25B |
| DEX volume (24h) | $1.73B (+9.50% 1d) |
| App fees (24h, all protocols) | $10.35M |
| Chain fees (24h) | $527.15K |
| Jito MEV tips (24h) | $146.10K |
| **REV - Real Economic Value (24h)** | **$673.24K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.89B | -2.25% |
| USDT | $2.40B | -11.74% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.28B | -1.72% |
| BUIDL | $876.06M | -1.14% |
| PYUSD | $679.06M | +0.01% |
| USDG | $622.10M | -6.04% |
| USDe | $315.60M | -16.81% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $264.96M |
| BisonFi | $205.55M |
| Raydium AMM | $165.03M |
| Manifest Trade | $162.62M |
| Tessera V | $148.18M |
| PumpSwap | $140.55M |
| pump.fun | $122.74M |
| Scorch | $89.51M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.91M |
| pump.fun | $1.68M |
| Axiom | $709.81K |
| Raydium AMM | $439.54K |
| Lunar Lander | $344.76K |
| Collector Crypt | $328.07K |
| Meteora DLMM | $323.86K |
| Relay | $261.63K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $81.05M |
| xStocks holder positions | 858.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $597.54M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 63,091 | 42.30% | 0.9 s |
| Pump.fun | 14,732 | 75.80% | 4.1 s |
| Jupiter v6 | 5,808 | 64.00% | 10.2 s |
| Orca Whirlpools | 3,804 | 19.00% | 15.6 s |
| Raydium AMM v4 | 697 | 21.40% | 85.8 s |

Median failure rate across the sampled programs: **42.30%** (range 19.00% to 75.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **116.80 SOL**.

## Exchange and large-holder balances

13.57M SOL ($1.36B) across 8 publicly-attributed accounts. Net **42K SOL (0.31%) moved off exchanges** over the last 22.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.73M | $1.18B | 0.2/h | 3 |
| Binance (2) | 1.02M | $101.85M | 949.9/h | 0 |
| Gate.io | 349.07K | $34.98M | 141/h | 0 |
| Bybit | 330.88K | $33.16M | 25.8/h | 0 |
| Bitget | 98.31K | $9.85M | 135.4/h | 0 |
| Kraken | 19.64K | $1.97M | 245.6/h | 0 |
| Coinbase (2) | 13.20K | $1.32M | 384.6/h | 1 |
| Coinbase | 12.14K | $1.22M | 318.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1073 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.253 | 1032 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 1039 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.224 | 998 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.219 | 998 | 0.0000 |
| SOL price moves with DeFi TVL | +0.208 | 1073 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1039 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 1020 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 1020 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 998 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.117 | 998 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 100.21 USD | Jupiter (on-chain DEX): 100.15 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 589.98M SOL | CoinGecko: 589.98M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-29
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-29

**Recently merged SIMDs:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-28
- [SIMD-0140: Migrate Config Program to Core BPF](https://github.com/solana-foundation/solana-improvement-documents/pull/140) - updated 2026-10-28
- [SIMD-0133: Syscall: Get Epoch Stake](https://github.com/solana-foundation/solana-improvement-documents/pull/133) - updated 2026-10-28
- [SIMD-0089: Programify Feature Gate Program](https://github.com/solana-foundation/solana-improvement-documents/pull/89) - updated 2026-10-28

**Latest Agave release:** [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28)

**Latest Firedancer release:** [v26.10.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.5) (2026-10-27)

## Ecosystem news

- **[Polygon Extends Its Stablecoin Payments Infrastructure to Solana](https://decrypt.co/381850/polygon-stablecoin-payments-open-money-stack-solana)** - Decrypt, 2026-10-29
- **[Polygon adds Solana to payment stack linking bank accounts, crypto and payouts](https://www.theblock.co/news/defi/2026-10-29-polygon-adds-solana-payment-stack-432115)** - The Block, 2026-10-29
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
