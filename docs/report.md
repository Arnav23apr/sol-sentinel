# Solana Ecosystem Report

*Generated 2026-11-01 16:56 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.1K |
| TPS (non-vote) | 2.1K |
| Slot time | 213.2 ms |
| Slot | 464M |
| Block height | 442M |
| Epoch | 1074 (46.10% complete, ~13.8h remaining) |
| Lifetime transactions | 564.7B |
| Circulating supply | 590.2M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 4.6M µlam/CU) |
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
| Stake on private (100% commission) validators | 24.32% |

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
| SOL price | $94.63 (-1.33% 24h) |
| Market cap | $55.84B (rank #7) |
| 24h volume | $1.35B |
| ATH | $293.31 (-67.74% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.43B |
| Stablecoin supply | $15.15B |
| DEX volume (24h) | $953.37M (-54.97% 1d) |
| App fees (24h, all protocols) | $8.27M |
| Chain fees (24h) | $364.24K |
| Jito MEV tips (24h) | $81.60K |
| **REV - Real Economic Value (24h)** | **$445.85K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.88B | +1.62% |
| USDT | $2.41B | -14.82% |
| USD1 | $1.38B | -0.94% |
| USDGO | $1.26B | -3.64% |
| BUIDL | $812.65M | -8.32% |
| PYUSD | $704.80M | -0.20% |
| USDG | $600.35M | -5.75% |
| USDe | $313.75M | -1.31% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $130.68M |
| pump.fun | $103.80M |
| Orca DEX | $86.53M |
| GoonFi | $73.87M |
| Tessera V | $70.33M |
| Raydium AMM | $61.93M |
| Meteora DLMM | $60.72M |
| BisonFi | $60.33M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.42M |
| pump.fun | $1.42M |
| Collector Crypt | $546.45K |
| Axiom | $408.90K |
| pump.fun Mobile App | $303.53K |
| Sanctum Validator LSTs | $262.56K |
| Meteora DLMM | $244.58K |
| Lunar Lander | $185.47K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $13.88M |
| xStocks holder positions | 871.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $597.42M |

## Program activity and chain health

Chain tip lag: **+0.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 47,280 | 50.00% | 1.1 s |
| Pump.fun | 28,330 | 91.90% | 1.9 s |
| Jupiter v6 | 1,575 | 20.10% | 37.9 s |
| Orca Whirlpools | 1,196 | 28.00% | 50.1 s |
| Raydium AMM v4 | 876 | 15.20% | 68.4 s |

Median failure rate across the sampled programs: **28.00%** (range 15.20% to 91.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **114.40 SOL**.

## Exchange and large-holder balances

10.80M SOL ($1.02B) across 7 publicly-attributed accounts. Net **2M SOL (15.69%) moved off exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.89M | $935.89M | 0.2/h | 6 |
| Gate.io | 354.22K | $33.52M | 139.5/h | 0 |
| Bybit | 339.50K | $32.13M | 23.2/h | 0 |
| Coinbase (2) | 74.98K | $7.10M | 218.4/h | 0 |
| Coinbase | 54.97K | $5.20M | 217.5/h | 0 |
| Kraken | 45.11K | $4.27M | 272.9/h | 0 |
| Bitget | 36.24K | $3.43M | 187.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1087 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.257 | 1046 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1053 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.222 | 1012 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.217 | 1012 | 0.0000 |
| SOL price moves with DeFi TVL | +0.215 | 1087 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1053 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 1034 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 1034 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1012 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.117 | 1012 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 94.63 USD | Jupiter (on-chain DEX): 94.64 USD | -0.01% | agree |
| Circulating supply | getSupply (RPC): 590.15M SOL | CoinGecko: 590.15M SOL | -0.00% | agree |

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

- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-28
- [SIMD-0140: Migrate Config Program to Core BPF](https://github.com/solana-foundation/solana-improvement-documents/pull/140) - updated 2026-10-28

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
