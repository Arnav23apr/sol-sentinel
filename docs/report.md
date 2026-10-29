# Solana Ecosystem Report

*Generated 2026-10-29 06:36 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.6 robust standard deviations above its 7-day baseline: a 499.2% move to 0.74 % from a typical 0.12.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.2K |
| TPS (non-vote) | 1.2K |
| Slot time | 213.5 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1071 (25.48% complete, ~19.1h remaining) |
| Lifetime transactions | 564.3B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 1,000.0K µlam/CU) |
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
| Stake on private (100% commission) validators | 24.09% |

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
| SOL price | $100.00 (-1.91% 24h) |
| Market cap | $59.01B (rank #7) |
| 24h volume | $2.94B |
| ATH | $293.31 (-65.91% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.65B |
| Stablecoin supply | $15.41B |
| DEX volume (24h) | $1.62B (+2.63% 1d) |
| App fees (24h, all protocols) | $10.35M |
| Chain fees (24h) | $527.15K |
| Jito MEV tips (24h) | $132.03K |
| **REV - Real Economic Value (24h)** | **$659.18K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.79B | -3.65% |
| USDT | $2.63B | -3.30% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.28B | -1.72% |
| BUIDL | $875.97M | -1.15% |
| PYUSD | $716.21M | +5.49% |
| USDG | $621.40M | -6.13% |
| USDe | $315.33M | -16.88% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $249.05M |
| BisonFi | $191.20M |
| Manifest Trade | $174.52M |
| Raydium AMM | $165.67M |
| Tessera V | $142.35M |
| PumpSwap | $140.55M |
| pump.fun | $140.44M |
| Meteora DLMM | $88.30M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.91M |
| pump.fun | $1.68M |
| Axiom | $709.81K |
| Collector Crypt | $557.65K |
| Raydium AMM | $366.82K |
| Lunar Lander | $349.45K |
| Meteora DLMM | $323.86K |
| StonkFun | $268.13K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $79.44M |
| xStocks holder positions | 859.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $596.21M |

## Program activity and chain health

Chain tip lag: **+0.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,979 | 33.60% | 1.5 s |
| Pump.fun | 15,572 | 86.40% | 3.6 s |
| Orca Whirlpools | 3,151 | 79.10% | 19 s |
| Jupiter v6 | 2,843 | 50.70% | 20.1 s |
| Raydium AMM v4 | 601 | 20.60% | 96.3 s |

Median failure rate across the sampled programs: **50.70%** (range 20.60% to 86.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **452.56 SOL**.

## Exchange and large-holder balances

13.59M SOL ($1.36B) across 8 publicly-attributed accounts. Net **253K SOL (1.90%) moved onto exchanges** over the last 21.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.73M | $1.17B | 0.2/h | 3 |
| Binance (2) | 1.01M | $100.91M | 1.1K/h | 0 |
| Gate.io | 350.30K | $35.03M | 130.4/h | 0 |
| Bybit | 330.88K | $33.09M | 26.9/h | 0 |
| Bitget | 104.60K | $10.46M | 133.3/h | 0 |
| Kraken | 30.44K | $3.04M | 153.8/h | 0 |
| Coinbase (2) | 15.94K | $1.59M | 202.6/h | 0 |
| Coinbase | 15.27K | $1.53M | 200.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1071 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.257 | 1030 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1037 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.221 | 996 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.216 | 996 | 0.0000 |
| SOL price moves with DeFi TVL | +0.210 | 1071 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1037 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 1018 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 1018 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 996 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.116 | 996 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 100 USD | Jupiter (on-chain DEX): 99.96 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 589.98M SOL | CoinGecko: 589.98M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14

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

- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
