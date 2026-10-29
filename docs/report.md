# Solana Ecosystem Report

*Generated 2026-10-29 00:30 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 7.8 robust standard deviations above its 7-day baseline: a 608.7% move to 0.74 % from a typical 0.10.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.7K |
| TPS (non-vote) | 1.7K |
| Slot time | 215.1 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1071 (1.73% complete, ~25.4h remaining) |
| Lifetime transactions | 564.2B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 7.30% of slots needed a priority fee (max 34.1M µlam/CU) |
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
| SOL price | $102.21 (+1.07% 24h) |
| Market cap | $60.30B (rank #7) |
| 24h volume | $2.68B |
| ATH | $293.31 (-65.15% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.76B |
| Stablecoin supply | $15.43B |
| DEX volume (24h) | $1.58B (-23.57% 1d) |
| App fees (24h, all protocols) | $11.37M |
| Chain fees (24h) | $538.02K |
| Jito MEV tips (24h) | $137.29K |
| **REV - Real Economic Value (24h)** | **$675.31K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.79B | -2.58% |
| USDT | $2.63B | -2.23% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.30B | +0.70% |
| BUIDL | $875.97M | -1.14% |
| PYUSD | $715.97M | +5.99% |
| USDG | $621.28M | -1.49% |
| USDe | $315.41M | -18.96% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $236.40M |
| PumpSwap | $193.28M |
| BisonFi | $191.20M |
| Manifest Trade | $189.21M |
| Raydium AMM | $160.73M |
| Tessera V | $142.35M |
| pump.fun | $140.44M |
| Meteora DLMM | $80.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.00M |
| pump.fun | $1.85M |
| Axiom | $645.78K |
| Collector Crypt | $546.76K |
| Raydium AMM | $359.12K |
| Lunar Lander | $344.50K |
| Meteora DLMM | $323.86K |
| pump.fun Mobile App | $294.01K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $78.94M |
| xStocks holder positions | 856.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $607.18M |

## Program activity and chain health

Chain tip lag: **+1.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 39,769 | 51.20% | 1.5 s |
| Pump.fun | 21,307 | 83.10% | 2.8 s |
| Jupiter v6 | 2,927 | 39.70% | 20.4 s |
| Orca Whirlpools | 1,506 | 33.40% | 39.8 s |
| Raydium AMM v4 | 911 | 21.90% | 65.8 s |

Median failure rate across the sampled programs: **39.70%** (range 21.90% to 83.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **586.11 SOL**.

## Exchange and large-holder balances

13.59M SOL ($1.39B) across 8 publicly-attributed accounts. Net **318K SOL (2.40%) moved onto exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.14B | 0.2/h | 3 |
| Binance (2) | 1.57M | $160.93M | 678/h | 0 |
| Gate.io | 350.49K | $35.82M | 194/h | 0 |
| Bybit | 330.88K | $33.82M | 28.6/h | 0 |
| Bitget | 94.08K | $9.62M | 95.9/h | 0 |
| Kraken | 30.39K | $3.11M | 188/h | 0 |
| Coinbase (2) | 17.43K | $1.78M | 346.2/h | 0 |
| Coinbase | 13.20K | $1.35M | 345.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1070 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.261 | 1029 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 1036 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.222 | 995 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.217 | 995 | 0.0000 |
| SOL price moves with DeFi TVL | +0.208 | 1070 | 0.0000 |
| Total TPS moves with Slot time | +0.197 | 1036 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 1017 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 1017 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 995 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.116 | 995 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 102.21 USD | Jupiter (on-chain DEX): 102.10 USD | +0.11% | agree |
| Circulating supply | getSupply (RPC): 589.98M SOL | CoinGecko: 589.93M SOL | +0.01% | agree |

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
