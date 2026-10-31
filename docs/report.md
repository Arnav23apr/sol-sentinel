# Solana Ecosystem Report

*Generated 2026-10-31 06:00 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 6.7 robust standard deviations above its 7-day baseline: a 598.4% move to 0.86 % from a typical 0.12.
- 🟠 **SOL price** (warning): SOL price is 5.2 robust standard deviations below its 7-day baseline: a 5.1% move to 95.86 USD from a typical 101.06.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.0K |
| TPS (non-vote) | 1.0K |
| Slot time | 214.3 ms |
| Slot | 464M |
| Block height | 442M |
| Epoch | 1073 (10.10% complete, ~23.1h remaining) |
| Lifetime transactions | 564.6B |
| Circulating supply | 590.1M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 6.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 664 |
| Delinquent validators | 28 |
| Delinquent stake | 0.86% |
| Total active stake | 429.9M SOL |
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
| SOL price | $95.86 (-2.05% 24h) |
| Market cap | $56.56B (rank #7) |
| 24h volume | $3.12B |
| ATH | $293.31 (-67.32% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.47B |
| Stablecoin supply | $15.23B |
| DEX volume (24h) | $2.40B (+4.50% 1d) |
| App fees (24h, all protocols) | $11.03M |
| Chain fees (24h) | $491.89K |
| Jito MEV tips (24h) | $98.59K |
| **REV - Real Economic Value (24h)** | **$590.48K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.94B | +2.68% |
| USDT | $2.43B | -14.11% |
| USD1 | $1.38B | -0.94% |
| USDGO | $1.26B | -3.64% |
| BUIDL | $812.65M | -8.32% |
| PYUSD | $693.25M | -0.86% |
| USDG | $613.51M | -4.37% |
| USDe | $315.86M | -3.39% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $301.26M |
| Orca DEX | $266.24M |
| PumpSwap | $221.74M |
| Tessera V | $209.29M |
| Scorch | $194.06M |
| Raydium AMM | $175.69M |
| Manifest Trade | $156.60M |
| Meteora DLMM | $131.86M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.59M |
| pump.fun | $1.59M |
| Collector Crypt | $771.10K |
| Jupiter Perpetual Exchange | $651.73K |
| Axiom | $526.63K |
| Meteora DLMM | $304.81K |
| Raydium AMM | $303.15K |
| pump.fun Mobile App | $277.32K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $97.49M |
| xStocks holder positions | 872.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $609.95M |

## Program activity and chain health

Chain tip lag: **+1.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 23,854 | 36.50% | 2.1 s |
| Pump.fun | 6,795 | 62.10% | 8.8 s |
| Jupiter v6 | 6,361 | 71.50% | 9.2 s |
| Orca Whirlpools | 2,249 | 48.30% | 26.6 s |
| Raydium AMM v4 | 474 | 15.30% | 126.4 s |

Median failure rate across the sampled programs: **48.30%** (range 15.30% to 71.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **463.06 SOL**.

## Exchange and large-holder balances

12.85M SOL ($1.23B) across 7 publicly-attributed accounts. Net **102K SOL (0.80%) moved onto exchanges** over the last 20.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.89M | $1.14B | 0.2/h | 6 |
| Gate.io | 343.43K | $32.92M | 159.6/h | 0 |
| Bybit | 339.50K | $32.54M | 51.7/h | 0 |
| Bitget | 116.67K | $11.18M | 115.3/h | 0 |
| Coinbase (2) | 112.08K | $10.74M | 177.6/h | 0 |
| Kraken | 26.72K | $2.56M | 148.6/h | 0 |
| Coinbase | 19.62K | $1.88M | 177.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1080 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.253 | 1039 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.233 | 1046 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.223 | 1005 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.218 | 1005 | 0.0000 |
| SOL price moves with DeFi TVL | +0.214 | 1080 | 0.0000 |
| Total TPS moves with Slot time | +0.200 | 1046 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.169 | 1027 | 0.0000 |
| Total TPS moves with Program failure rate | +0.168 | 1027 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1005 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.119 | 1005 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 95.86 USD | Jupiter (on-chain DEX): 95.89 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 590.10M SOL | CoinGecko: 590.10M SOL | -0.00% | agree |

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
