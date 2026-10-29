# Solana Ecosystem Report

*Generated 2026-10-29 13:48 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.6 robust standard deviations above its 7-day baseline: a 499.2% move to 0.74 % from a typical 0.12.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.1K |
| TPS (non-vote) | 2.1K |
| Slot time | 213.9 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1071 (53.60% complete, ~11.9h remaining) |
| Lifetime transactions | 564.3B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 19.30% of slots needed a priority fee (max 21.4M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 666 |
| Delinquent validators | 23 |
| Delinquent stake | 0.74% |
| Total active stake | 433.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.46% / 24.71% / 36.07% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.10% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.84% | 0% |
| 3 | `3N7s…iD5g` | 12.9M | 2.97% | 0% |
| 4 | `8Gbw…F8iD` | 10.8M | 2.48% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.24% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |
| 10 | `CvSb…wycB` | 6.6M | 1.53% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $100.36 (-0.71% 24h) |
| Market cap | $59.18B (rank #7) |
| 24h volume | $2.84B |
| ATH | $293.31 (-65.78% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.65B |
| Stablecoin supply | $15.42B |
| DEX volume (24h) | $1.73B (+9.50% 1d) |
| App fees (24h, all protocols) | $10.35M |
| Chain fees (24h) | $527.15K |
| Jito MEV tips (24h) | $140.06K |
| **REV - Real Economic Value (24h)** | **$667.21K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.82B | -3.35% |
| USDT | $2.63B | -3.30% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.28B | -1.72% |
| BUIDL | $875.97M | -1.15% |
| PYUSD | $693.65M | +2.17% |
| USDG | $621.56M | -6.10% |
| USDe | $315.60M | -16.81% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $246.10M |
| BisonFi | $205.55M |
| Manifest Trade | $157.90M |
| Tessera V | $148.18M |
| Raydium AMM | $144.65M |
| PumpSwap | $140.55M |
| pump.fun | $122.74M |
| Scorch | $89.51M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.91M |
| pump.fun | $1.68M |
| Axiom | $709.81K |
| Lunar Lander | $346.67K |
| Collector Crypt | $339.44K |
| Meteora DLMM | $323.86K |
| Raydium AMM | $312.95K |
| pump.fun Mobile App | $257.66K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $87.33M |
| xStocks holder positions | 858.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $596.95M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 47,125 | 36.50% | 1.1 s |
| Jupiter v6 | 12,970 | 76.00% | 4.5 s |
| Pump.fun | 6,984 | 67.40% | 8.3 s |
| Orca Whirlpools | 3,639 | 49.20% | 15.6 s |
| Raydium AMM v4 | 1,243 | 10.70% | 48.1 s |

Median failure rate across the sampled programs: **49.20%** (range 10.70% to 76.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **382.74 SOL**.

## Exchange and large-holder balances

13.61M SOL ($1.37B) across 8 publicly-attributed accounts. Net **95K SOL (0.71%) moved onto exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.73M | $1.18B | 0.2/h | 3 |
| Binance (2) | 1.02M | $102.47M | 1.1K/h | 0 |
| Gate.io | 348.46K | $34.97M | 160.2/h | 0 |
| Bybit | 330.88K | $33.21M | 62/h | 0 |
| Bitget | 105.59K | $10.60M | 142.9/h | 0 |
| Kraken | 33.09K | $3.32M | 327.6/h | 0 |
| Coinbase (2) | 15.92K | $1.60M | 229.4/h | 0 |
| Coinbase | 15.51K | $1.56M | 226.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1072 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.253 | 1031 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1038 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.223 | 997 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.218 | 997 | 0.0000 |
| SOL price moves with DeFi TVL | +0.209 | 1072 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1038 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 1019 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 1019 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 997 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.116 | 997 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 100.36 USD | Jupiter (on-chain DEX): 100.28 USD | +0.08% | agree |
| Circulating supply | getSupply (RPC): 589.98M SOL | CoinGecko: 589.98M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-29

**Recently merged SIMDs:**

- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-28
- [SIMD-0140: Migrate Config Program to Core BPF](https://github.com/solana-foundation/solana-improvement-documents/pull/140) - updated 2026-10-28
- [SIMD-0133: Syscall: Get Epoch Stake](https://github.com/solana-foundation/solana-improvement-documents/pull/133) - updated 2026-10-28
- [SIMD-0089: Programify Feature Gate Program](https://github.com/solana-foundation/solana-improvement-documents/pull/89) - updated 2026-10-28
- [SIMD-0088: Enable Core BPF Programs](https://github.com/solana-foundation/solana-improvement-documents/pull/88) - updated 2026-10-28

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
