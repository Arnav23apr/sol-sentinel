# Solana Ecosystem Report

*Generated 2026-10-30 09:13 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DeFi TVL** (critical): DeFi TVL is 9.4 robust standard deviations below its 7-day baseline: a 5.2% move to 5,445,362,953.00 USD from a typical 5,744,897,574.00.
- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.2 robust standard deviations above its 7-day baseline: a 465.0% move to 0.69 % from a typical 0.12.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.1K |
| TPS (non-vote) | 1.1K |
| Slot time | 212.8 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1072 (29.29% complete, ~18.1h remaining) |
| Lifetime transactions | 564.4B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 1.6M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 665 |
| Delinquent validators | 26 |
| Delinquent stake | 0.69% |
| Total active stake | 432.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 24.81% / 36.04% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.16% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 12.9M | 2.99% | 0% |
| 4 | `8Gbw…F8iD` | 10.5M | 2.43% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.19% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.80% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.63% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $97.03 (-3.36% 24h) |
| Market cap | $57.25B (rank #7) |
| 24h volume | $5.83B |
| ATH | $293.31 (-66.92% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.45B |
| Stablecoin supply | $15.18B |
| DEX volume (24h) | $1.92B (+11.02% 1d) |
| App fees (24h, all protocols) | $12.25M |
| Chain fees (24h) | $564.52K |
| Jito MEV tips (24h) | $150.52K |
| **REV - Real Economic Value (24h)** | **$715.05K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.88B | +1.09% |
| USDT | $2.40B | -12.71% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.26B | -3.10% |
| BUIDL | $837.56M | -5.50% |
| PYUSD | $706.41M | -3.76% |
| USDG | $602.93M | -4.22% |
| USDe | $316.03M | -11.83% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $448.82M |
| Manifest Trade | $241.25M |
| Raydium AMM | $218.87M |
| BisonFi | $205.55M |
| Tessera V | $148.18M |
| Meteora DLMM | $130.28M |
| pump.fun | $122.74M |
| PumpSwap | $118.70M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.70M |
| pump.fun | $1.71M |
| Meteora DLMM | $883.32K |
| Jupiter Perpetual Exchange | $736.57K |
| Axiom | $716.50K |
| Raydium AMM | $494.73K |
| Orca DEX | $400.20K |
| Lunar Lander | $323.43K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $61.34M |
| xStocks holder positions | 858.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $612.41M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 29,198 | 48.00% | 1.9 s |
| Pump.fun | 13,788 | 80.30% | 4.3 s |
| Jupiter v6 | 5,069 | 70.50% | 9.4 s |
| Orca Whirlpools | 2,483 | 50.20% | 24 s |
| Raydium AMM v4 | 665 | 38.30% | 90 s |

Median failure rate across the sampled programs: **50.20%** (range 38.30% to 80.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **382.71 SOL**.

## Exchange and large-holder balances

12.75M SOL ($1.24B) across 7 publicly-attributed accounts. Net **859K SOL (6.32%) moved off exchanges** over the last 19.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.89M | $1.15B | 0.2/h | 3 |
| Gate.io | 352.39K | $34.19M | 203/h | 0 |
| Bybit | 337.73K | $32.77M | 20.2/h | 0 |
| Bitget | 102.40K | $9.94M | 233.5/h | 0 |
| Kraken | 31.98K | $3.10M | 222.9/h | 0 |
| Coinbase | 17.09K | $1.66M | 165.6/h | 0 |
| Coinbase (2) | 14.40K | $1.40M | 219.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1076 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.255 | 1035 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 1042 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.224 | 1001 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.219 | 1001 | 0.0000 |
| SOL price moves with DeFi TVL | +0.214 | 1076 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1042 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 1023 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 1023 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 1001 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.118 | 1001 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 97.03 USD | Jupiter (on-chain DEX): 96.96 USD | +0.07% | agree |
| Circulating supply | getSupply (RPC): 590.04M SOL | CoinGecko: 590.04M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
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
