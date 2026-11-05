# Solana Ecosystem Report

*Generated 2026-11-05 01:19 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.7K |
| TPS (non-vote) | 1.7K |
| Slot time | 213.9 ms |
| Slot | 466M |
| Block height | 444M |
| Epoch | 1077 (58.64% complete, ~10.6h remaining) |
| Lifetime transactions | 565.3B |
| Circulating supply | 590.3M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 607.5K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 31 |
| Delinquent stake | 0.46% |
| Total active stake | 431.0M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.48% / 24.86% / 36.32% |
| Commission (stake-weighted, delegatable validators) | 3.73% |
| Stake on private (100% commission) validators | 24.12% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.95% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.88% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.02% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.42% | 0% |
| 5 | `Catz…Diqb` | 9.5M | 2.21% | 5% |
| 6 | `51JB…UNAm` | 9.4M | 2.19% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.82% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `CvSb…wycB` | 7.0M | 1.62% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $95.46 (+4.05% 24h) |
| Market cap | $56.34B (rank #7) |
| 24h volume | $3.95B |
| ATH | $293.31 (-67.46% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.55B |
| Stablecoin supply | $14.93B |
| DEX volume (24h) | $2.20B (+16.92% 1d) |
| App fees (24h, all protocols) | $10.63M |
| Chain fees (24h) | $479.80K |
| Jito MEV tips (24h) | $147.79K |
| **REV - Real Economic Value (24h)** | **$627.59K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.12B | +5.94% |
| USDT | $2.56B | -8.88% |
| USD1 | $1.32B | -4.48% |
| USDGO | $1.17B | -9.31% |
| PYUSD | $682.43M | -1.72% |
| BUIDL | $584.94M | -33.38% |
| USDG | $500.20M | -18.31% |
| USDe | $296.63M | -6.46% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $326.52M |
| PumpSwap | $321.84M |
| BisonFi | $257.10M |
| Raydium AMM | $235.97M |
| Tessera V | $154.41M |
| Manifest Trade | $151.36M |
| pump.fun | $126.27M |
| Scorch | $99.91M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.82M |
| pump.fun | $1.61M |
| Axiom | $586.96K |
| Raydium AMM | $386.69K |
| Lunar Lander | $306.38K |
| Orca DEX | $287.44K |
| Meteora DLMM | $287.28K |
| Sanctum Validator LSTs | $263.81K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $92.67M |
| xStocks holder positions | 880.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $569.77M |

## Program activity and chain health

Chain tip lag: **+1.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 41,468 | 42.80% | 1.3 s |
| Pump.fun | 20,908 | 86.50% | 2.8 s |
| Jupiter v6 | 10,541 | 67.70% | 5.6 s |
| Orca Whirlpools | 5,950 | 38.40% | 10.1 s |
| Raydium AMM v4 | 924 | 24.80% | 64.8 s |

Median failure rate across the sampled programs: **42.80%** (range 24.80% to 86.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **946.73 SOL**.

## Exchange and large-holder balances

9.81M SOL ($936.12M) across 5 publicly-attributed accounts. Net **51K SOL (0.52%) moved off exchanges** over the last 18.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $887.78M | 0.2/h | 3 |
| Bybit | 346.93K | $33.12M | 61.5/h | 0 |
| Gate.io | 97.87K | $9.34M | 240.2/h | 0 |
| Kraken | 33.30K | $3.18M | 188.5/h | 0 |
| Coinbase | 28.31K | $2.70M | 270.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1098 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.247 | 1057 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 1066 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.226 | 1025 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.222 | 1025 | 0.0000 |
| SOL price moves with DeFi TVL | +0.221 | 1098 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1066 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 1047 | 0.0000 |
| Total TPS moves with Program failure rate | +0.161 | 1047 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.156 | 1025 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.122 | 1025 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 95.46 USD | Jupiter (on-chain DEX): 95.12 USD | +0.36% | agree |
| Circulating supply | getSupply (RPC): 590.26M SOL | CoinGecko: 590.26M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-03
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-03
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

**Recently merged SIMDs:**

- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28

**Latest Agave release:** [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28)

**Latest Firedancer release:** [v26.10.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.5) (2026-10-27)

## Ecosystem news

- **[Schroders launches tokenized emerging markets debt fund on Solana with Centrifuge](https://www.theblock.co/news/business/2026-11-04-schroders-centrifuge-tokenized-emerging-markets-debt-fund-solana-432878)** - The Block, 2026-11-04
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
