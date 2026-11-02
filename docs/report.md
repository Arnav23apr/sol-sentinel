# Solana Ecosystem Report

*Generated 2026-11-02 06:30 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.1K |
| TPS (non-vote) | 1.1K |
| Slot time | 212.8 ms |
| Slot | 464M |
| Block height | 442M |
| Epoch | 1074 (98.84% complete, ~0.3h remaining) |
| Lifetime transactions | 564.8B |
| Circulating supply | 590.2M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 364.0K µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 34 |
| Delinquent stake | 1.05% |
| Total active stake | 429.4M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.53% / 24.95% / 36.25% |
| Commission (stake-weighted, delegatable validators) | 3.73% |
| Stake on private (100% commission) validators | 24.33% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.97% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.89% | 0% |
| 3 | `3N7s…iD5g` | 12.9M | 3.01% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.43% | 0% |
| 5 | `Catz…Diqb` | 9.6M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 7.0M | 1.62% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $94.34 (-1.31% 24h) |
| Market cap | $55.67B (rank #7) |
| 24h volume | $1.97B |
| ATH | $293.31 (-67.84% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.51B |
| Stablecoin supply | $15.07B |
| DEX volume (24h) | $832.67M (-12.68% 1d) |
| App fees (24h, all protocols) | $8.43M |
| Chain fees (24h) | $367.71K |
| Jito MEV tips (24h) | $92.31K |
| **REV - Real Economic Value (24h)** | **$460.02K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.82B | +1.81% |
| USDT | $2.41B | -15.71% |
| USD1 | $1.38B | -0.94% |
| USDGO | $1.25B | -4.40% |
| BUIDL | $812.65M | -8.32% |
| PYUSD | $696.41M | -0.70% |
| USDG | $592.59M | -4.82% |
| USDe | $313.36M | -1.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $122.94M |
| Orca DEX | $112.24M |
| pump.fun | $103.80M |
| GoonFi | $73.87M |
| Raydium AMM | $72.58M |
| Tessera V | $70.33M |
| BisonFi | $60.33M |
| Meteora DLMM | $47.62M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.16M |
| pump.fun | $1.38M |
| Axiom | $482.58K |
| Collector Crypt | $327.90K |
| Sanctum Validator LSTs | $265.28K |
| pump.fun Mobile App | $260.57K |
| Lunar Lander | $218.06K |
| fomo Wallet | $179.24K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $18.26M |
| xStocks holder positions | 872.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.65M |

## Program activity and chain health

Chain tip lag: **+1.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 33,069 | 35.60% | 1.5 s |
| Pump.fun | 10,025 | 77.90% | 5.7 s |
| Jupiter v6 | 1,948 | 50.60% | 30.6 s |
| Orca Whirlpools | 1,167 | 41.00% | 50.6 s |
| Raydium AMM v4 | 461 | 11.30% | 129.8 s |

Median failure rate across the sampled programs: **41.00%** (range 11.30% to 77.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **114.40 SOL**.

## Exchange and large-holder balances

10.76M SOL ($1.01B) across 7 publicly-attributed accounts. Net **2M SOL (15.96%) moved off exchanges** over the last 19.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.89M | $933.02M | 0.2/h | 6 |
| Gate.io | 379.63K | $35.81M | 137.8/h | 0 |
| Bybit | 339.50K | $32.03M | 37.5/h | 0 |
| Coinbase | 44.96K | $4.24M | 145.7/h | 1 |
| Coinbase (2) | 37.44K | $3.53M | 189.1/h | 0 |
| Kraken | 35.17K | $3.32M | 130.3/h | 0 |
| Bitget | 30.28K | $2.86M | 183.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 15 of 117 tested pairs survive, over 1090 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.254 | 1049 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1056 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.221 | 1015 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.216 | 1015 | 0.0000 |
| SOL price moves with DeFi TVL | +0.216 | 1090 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1056 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 1037 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 1037 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 1015 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.119 | 1015 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 94.34 USD | Jupiter (on-chain DEX): 94.32 USD | +0.02% | agree |
| Circulating supply | getSupply (RPC): 590.15M SOL | CoinGecko: 590.15M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-02

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-02
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

**Recently merged SIMDs:**

- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-28

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
