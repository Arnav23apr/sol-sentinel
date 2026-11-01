# Solana Ecosystem Report

*Generated 2026-11-01 03:01 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 213.9 ms |
| Slot | 464M |
| Block height | 442M |
| Epoch | 1073 (91.93% complete, ~2.1h remaining) |
| Lifetime transactions | 564.7B |
| Circulating supply | 590.1M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 5.30% of slots needed a priority fee (max 334.4K µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 665 |
| Delinquent validators | 27 |
| Delinquent stake | 0.85% |
| Total active stake | 430.0M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.52% / 24.92% / 36.20% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.29% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.96% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.88% | 0% |
| 3 | `3N7s…iD5g` | 12.9M | 3.01% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.42% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.24% | 5% |
| 6 | `51JB…UNAm` | 9.4M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 7.0M | 1.62% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $95.38 (-1.44% 24h) |
| Market cap | $56.28B (rank #7) |
| 24h volume | $1.54B |
| ATH | $293.31 (-67.48% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.44B |
| Stablecoin supply | $15.24B |
| DEX volume (24h) | $1.44B (-31.85% 1d) |
| App fees (24h, all protocols) | $8.58M |
| Chain fees (24h) | $364.24K |
| Jito MEV tips (24h) | $78.61K |
| **REV - Real Economic Value (24h)** | **$442.85K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.94B | +2.50% |
| USDT | $2.43B | -14.11% |
| USD1 | $1.38B | -0.94% |
| USDGO | $1.26B | -3.64% |
| BUIDL | $812.65M | -8.32% |
| PYUSD | $704.64M | -0.27% |
| USDG | $604.28M | -5.13% |
| USDe | $314.84M | -1.05% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $182.87M |
| Tessera V | $181.44M |
| PumpSwap | $130.68M |
| Orca DEX | $117.74M |
| pump.fun | $113.64M |
| GoonFi | $108.02M |
| Scorch | $83.07M |
| ZeroFi | $75.67M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.42M |
| pump.fun | $1.42M |
| Axiom | $408.90K |
| pump.fun Mobile App | $303.53K |
| Jupiter Lend | $300.09K |
| Sanctum Validator LSTs | $262.56K |
| Kamino Lend | $255.07K |
| Collector Crypt | $248.16K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $22.01M |
| xStocks holder positions | 871.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.44M |

## Program activity and chain health

Chain tip lag: **+1.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 44,226 | 23.80% | 1.3 s |
| Orca Whirlpools | 3,252 | 45.20% | 18.4 s |
| Pump.fun | 2,774 | 20.40% | 21.6 s |
| Jupiter v6 | 1,584 | 32.40% | 37.6 s |
| Raydium AMM v4 | 521 | 8.80% | 114.7 s |

Median failure rate across the sampled programs: **23.80%** (range 8.80% to 45.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **115.20 SOL**.

## Exchange and large-holder balances

12.78M SOL ($1.22B) across 6 publicly-attributed accounts. Net **72K SOL (0.56%) moved off exchanges** over the last 21.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.89M | $1.13B | 0.2/h | 6 |
| Gate.io | 343.93K | $32.80M | 106/h | 0 |
| Bybit | 339.50K | $32.38M | 27.4/h | 0 |
| Coinbase | 88.76K | $8.47M | 192.9/h | 0 |
| Coinbase (2) | 85.41K | $8.15M | 206.7/h | 0 |
| Kraken | 28.04K | $2.67M | 157.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1085 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.252 | 1044 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.233 | 1051 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.222 | 1010 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.217 | 1010 | 0.0000 |
| SOL price moves with DeFi TVL | +0.214 | 1085 | 0.0000 |
| Total TPS moves with Slot time | +0.200 | 1051 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.168 | 1032 | 0.0000 |
| Total TPS moves with Program failure rate | +0.167 | 1032 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1010 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.116 | 1010 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 95.38 USD | Jupiter (on-chain DEX): 95.35 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 590.09M SOL | CoinGecko: 590.09M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-10-31
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23

**Recently merged SIMDs:**

- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-28
- [SIMD-0140: Migrate Config Program to Core BPF](https://github.com/solana-foundation/solana-improvement-documents/pull/140) - updated 2026-10-28
- [SIMD-0133: Syscall: Get Epoch Stake](https://github.com/solana-foundation/solana-improvement-documents/pull/133) - updated 2026-10-28

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
