# Solana Ecosystem Report

*Generated 2026-10-30 02:44 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DeFi TVL** (critical): DeFi TVL is 11.5 robust standard deviations below its 7-day baseline: a 6.4% move to 5,381,352,589.00 USD from a typical 5,747,941,850.50.
- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.9 robust standard deviations above its 7-day baseline: a 527.6% move to 0.77 % from a typical 0.12.
- 🟠 **SOL price** (warning): SOL price is 4.9 robust standard deviations below its 7-day baseline: a 6.0% move to 95.23 USD from a typical 101.25.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.8K |
| TPS (non-vote) | 1.8K |
| Slot time | 213.9 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1072 (3.97% complete, ~24.6h remaining) |
| Lifetime transactions | 564.4B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 12.70% of slots needed a priority fee (max 5.5M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 666 |
| Delinquent validators | 25 |
| Delinquent stake | 0.77% |
| Total active stake | 432.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.45% / 24.83% / 36.07% |
| Commission (stake-weighted, delegatable validators) | 3.73% |
| Stake on private (100% commission) validators | 24.18% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 12.9M | 2.99% | 0% |
| 4 | `8Gbw…F8iD` | 10.5M | 2.43% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.24% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.19% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.80% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.63% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $95.23 (-4.18% 24h) |
| Market cap | $56.17B (rank #7) |
| 24h volume | $5.16B |
| ATH | $293.31 (-67.53% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.38B |
| Stablecoin supply | $15.16B |
| DEX volume (24h) | $1.92B (+11.02% 1d) |
| App fees (24h, all protocols) | $11.37M |
| Chain fees (24h) | $564.52K |
| Jito MEV tips (24h) | $151.84K |
| **REV - Real Economic Value (24h)** | **$716.36K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.81B | +0.12% |
| USDT | $2.40B | -12.71% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.28B | -1.72% |
| BUIDL | $837.56M | -5.50% |
| PYUSD | $709.46M | -3.11% |
| USDG | $619.59M | -1.51% |
| USDe | $315.79M | -11.80% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $382.62M |
| Raydium AMM | $232.44M |
| BisonFi | $205.55M |
| Manifest Trade | $181.06M |
| Tessera V | $148.18M |
| Meteora DLMM | $130.28M |
| pump.fun | $122.74M |
| PumpSwap | $118.70M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.70M |
| pump.fun | $1.71M |
| Jupiter Perpetual Exchange | $736.57K |
| Axiom | $716.50K |
| Raydium AMM | $570.98K |
| Orca DEX | $349.36K |
| Lunar Lander | $340.25K |
| pump.fun Mobile App | $273.82K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $69.16M |
| xStocks holder positions | 858.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $596.08M |

## Program activity and chain health

Chain tip lag: **+2.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 76,484 | 57.90% | 0.6 s |
| Pump.fun | 15,890 | 87.70% | 3.6 s |
| Orca Whirlpools | 6,228 | 47.40% | 9.4 s |
| Jupiter v6 | 5,090 | 62.20% | 11.8 s |
| Raydium AMM v4 | 995 | 6.00% | 59.9 s |

Median failure rate across the sampled programs: **57.90%** (range 6.00% to 87.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **655.47 SOL**.

## Exchange and large-holder balances

12.74M SOL ($1.21B) across 7 publicly-attributed accounts. Net **849K SOL (6.25%) moved off exchanges** over the last 20.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.89M | $1.13B | 0.2/h | 3 |
| Gate.io | 357.28K | $34.02M | 306.9/h | 0 |
| Bybit | 332.36K | $31.65M | 61.4/h | 0 |
| Bitget | 114.89K | $10.94M | 170.9/h | 0 |
| Kraken | 26.24K | $2.50M | 141.2/h | 0 |
| Coinbase | 11.11K | $1.06M | 325.2/h | 0 |
| Coinbase (2) | 10.90K | $1.04M | 326.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1075 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.256 | 1034 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 1041 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.225 | 1000 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.220 | 1000 | 0.0000 |
| SOL price moves with DeFi TVL | +0.212 | 1075 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1041 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 1022 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 1022 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 1000 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.118 | 1000 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 95.23 USD | Jupiter (on-chain DEX): 95.04 USD | +0.20% | agree |
| Circulating supply | getSupply (RPC): 590.04M SOL | CoinGecko: 590.04M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-29
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

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
