# Solana Ecosystem Report

*Generated 2026-11-04 20:59 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 6.1 robust standard deviations below its 7-day baseline: a 3.6% move to 14,627,302,658.00 USD from a typical 15,172,512,541.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.5K |
| TPS (non-vote) | 2.5K |
| Slot time | 212.8 ms |
| Slot | 465M |
| Block height | 443M |
| Epoch | 1077 (41.81% complete, ~14.9h remaining) |
| Lifetime transactions | 565.2B |
| Circulating supply | 590.3M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 36.70% of slots needed a priority fee (max 4.1M µlam/CU) |
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
| SOL price | $94.68 (+1.30% 24h) |
| Market cap | $55.89B (rank #7) |
| 24h volume | $3.79B |
| ATH | $293.31 (-67.72% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.55B |
| Stablecoin supply | $14.63B |
| DEX volume (24h) | $1.88B (+1.54% 1d) |
| App fees (24h, all protocols) | $11.47M |
| Chain fees (24h) | $479.80K |
| Jito MEV tips (24h) | $148.13K |
| **REV - Real Economic Value (24h)** | **$627.93K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.10B | +5.60% |
| USDT | $2.18B | -22.38% |
| USD1 | $1.33B | -3.66% |
| USDGO | $1.17B | -9.31% |
| BUIDL | $672.88M | -23.37% |
| PYUSD | $671.95M | -3.21% |
| USDG | $508.17M | -16.99% |
| USDe | $297.01M | -6.31% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $321.84M |
| Orca DEX | $309.68M |
| BisonFi | $257.10M |
| Raydium AMM | $226.98M |
| Tessera V | $154.41M |
| Manifest Trade | $151.39M |
| pump.fun | $126.27M |
| Scorch | $99.91M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.82M |
| pump.fun | $1.61M |
| Pyth Pro | $1.04M |
| Axiom | $586.96K |
| Raydium AMM | $357.92K |
| Lunar Lander | $297.62K |
| Meteora DLMM | $287.28K |
| Orca DEX | $281.46K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $88.52M |
| xStocks holder positions | 877.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $569.67M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 115,320 (approx.) | 47.00% | 0.4 s |
| Pump.fun | 24,940 | 80.30% | 2.3 s |
| Orca Whirlpools | 10,213 | 78.00% | 5.7 s |
| Jupiter v6 | 7,590 | 59.00% | 7.9 s |
| Raydium AMM v4 | 1,201 | 6.90% | 49.8 s |

Median failure rate across the sampled programs: **59.00%** (range 6.90% to 80.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **911.66 SOL**.

## Exchange and large-holder balances

9.85M SOL ($932.65M) across 7 publicly-attributed accounts. Net **4K SOL (0.04%) moved onto exchanges** over the last 20.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $880.52M | 0.2/h | 3 |
| Bybit | 346.93K | $32.85M | 43/h | 0 |
| Gate.io | 99.02K | $9.38M | 127.4/h | 0 |
| Kraken | 38.95K | $3.69M | 352.9/h | 0 |
| Coinbase (2) | 26.46K | $2.51M | 274.2/h | 0 |
| Coinbase | 24.82K | $2.35M | 407.2/h | 0 |
| Bitget | 14.41K | $1.36M | 169.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1097 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.251 | 1056 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1065 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.224 | 1024 | 0.0000 |
| SOL price moves with DeFi TVL | +0.220 | 1097 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.219 | 1024 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1065 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.161 | 1046 | 0.0000 |
| Total TPS moves with Program failure rate | +0.160 | 1046 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 1024 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.120 | 1024 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 94.68 USD | Jupiter (on-chain DEX): 94.77 USD | -0.10% | agree |
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
