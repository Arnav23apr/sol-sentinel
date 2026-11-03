# Solana Ecosystem Report

*Generated 2026-11-03 12:10 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.5K |
| TPS (non-vote) | 1.5K |
| Slot time | 214.3 ms |
| Slot | 465M |
| Block height | 443M |
| Epoch | 1076 (14.31% complete, ~22.0h remaining) |
| Lifetime transactions | 565.0B |
| Circulating supply | 590.3M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 22.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 665 |
| Delinquent validators | 28 |
| Delinquent stake | 0.50% |
| Total active stake | 432.5M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.44% / 24.79% / 36.18% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.11% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.02% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.41% | 0% |
| 5 | `Catz…Diqb` | 9.6M | 2.21% | 5% |
| 6 | `51JB…UNAm` | 9.4M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `CvSb…wycB` | 7.0M | 1.61% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $92.36 (-2.08% 24h) |
| Market cap | $54.52B (rank #7) |
| 24h volume | $2.45B |
| ATH | $293.31 (-68.51% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.40B |
| Stablecoin supply | $14.96B |
| DEX volume (24h) | $1.83B (+102.16% 1d) |
| App fees (24h, all protocols) | $11.04M |
| Chain fees (24h) | $482.24K |
| Jito MEV tips (24h) | $118.77K |
| **REV - Real Economic Value (24h)** | **$601.01K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.91B | +3.09% |
| USDT | $2.44B | -13.14% |
| USD1 | $1.37B | -1.34% |
| USDGO | $1.20B | -7.13% |
| BUIDL | $804.90M | -8.39% |
| PYUSD | $672.25M | -3.84% |
| USDG | $566.84M | -7.72% |
| USDe | $298.00M | -6.01% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $261.06M |
| BisonFi | $250.54M |
| Orca DEX | $204.01M |
| Tessera V | $149.85M |
| pump.fun | $123.08M |
| Raydium AMM | $113.85M |
| GoonFi | $110.91M |
| Manifest Trade | $101.80M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.53M |
| pump.fun | $1.65M |
| Meteora DAMM V2 | $1.26M |
| Axiom | $546.81K |
| Jupiter Perpetual Exchange | $346.05K |
| Collector Crypt | $282.70K |
| ORE Protocol | $261.50K |
| Sanctum Validator LSTs | $256.56K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $63.27M |
| xStocks holder positions | 874.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $559.20M |

## Program activity and chain health

Chain tip lag: **+1.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 52,524 | 61.30% | 1.1 s |
| Pump.fun | 24,358 | 90.10% | 2.4 s |
| Jupiter v6 | 4,726 | 71.50% | 12.6 s |
| Orca Whirlpools | 3,233 | 51.50% | 18.4 s |
| Raydium AMM v4 | 642 | 6.70% | 93.4 s |

Median failure rate across the sampled programs: **61.30%** (range 6.70% to 90.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **998.64 SOL**.

## Exchange and large-holder balances

10.40M SOL ($960.43M) across 7 publicly-attributed accounts. Net **310K SOL (2.90%) moved off exchanges** over the last 19.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.89M | $913.44M | 0.2/h | 4 |
| Bybit | 339.40K | $31.35M | 33.6/h | 0 |
| Gate.io | 100.27K | $9.26M | 216.1/h | 0 |
| Kraken | 31.16K | $2.88M | 174.6/h | 0 |
| Coinbase (2) | 13.23K | $1.22M | 338/h | 0 |
| Bitget | 12.62K | $1.17M | 193.4/h | 0 |
| Coinbase | 12.12K | $1.12M | 213.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1092 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.250 | 1051 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 1060 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.224 | 1019 | 0.0000 |
| SOL price moves with DeFi TVL | +0.220 | 1092 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.219 | 1019 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1060 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.165 | 1041 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 1041 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1019 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.120 | 1019 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 92.36 USD | Jupiter (on-chain DEX): 92.39 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 590.26M SOL | CoinGecko: 590.26M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-03
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-02
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
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

- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
