# Solana Ecosystem Report

*Generated 2026-11-03 04:27 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.4K |
| TPS (non-vote) | 1.4K |
| Slot time | 211.7 ms |
| Slot | 465M |
| Block height | 443M |
| Epoch | 1075 (84.25% complete, ~4.0h remaining) |
| Lifetime transactions | 565.0B |
| Circulating supply | 590.2M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 3.7M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 665 |
| Delinquent validators | 28 |
| Delinquent stake | 1.01% |
| Total active stake | 429.8M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.54% / 24.96% / 36.32% |
| Commission (stake-weighted, delegatable validators) | 3.74% |
| Stake on private (100% commission) validators | 24.27% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.96% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.89% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.03% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.43% | 0% |
| 5 | `Catz…Diqb` | 9.6M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.82% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 7.0M | 1.62% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $92.12 (-3.39% 24h) |
| Market cap | $54.37B (rank #7) |
| 24h volume | $2.57B |
| ATH | $293.31 (-68.59% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.36B |
| Stablecoin supply | $15.12B |
| DEX volume (24h) | $905.60M (-5.03% 1d) |
| App fees (24h, all protocols) | $8.39M |
| Chain fees (24h) | $367.71K |
| Jito MEV tips (24h) | $107.64K |
| **REV - Real Economic Value (24h)** | **$475.35K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.95B | +3.69% |
| USDT | $2.41B | -15.71% |
| USD1 | $1.38B | -0.93% |
| USDGO | $1.23B | -5.79% |
| BUIDL | $804.90M | -9.19% |
| PYUSD | $672.85M | -3.97% |
| USDG | $560.88M | -9.89% |
| USDe | $313.57M | -1.20% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $210.23M |
| Raydium AMM | $137.40M |
| PumpSwap | $122.94M |
| Manifest Trade | $108.64M |
| pump.fun | $104.82M |
| Tessera V | $96.43M |
| BisonFi | $86.05M |
| GoonFi | $75.34M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.16M |
| pump.fun | $1.38M |
| Axiom | $482.58K |
| Sanctum Validator LSTs | $265.28K |
| pump.fun Mobile App | $260.57K |
| Raydium AMM | $238.88K |
| Lunar Lander | $231.54K |
| ORE Protocol | $170.95K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $61.51M |
| xStocks holder positions | 874.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | - |

## Program activity and chain health

Chain tip lag: **+1.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,034 | 37.30% | 1.3 s |
| Pump.fun | 21,322 | 89.60% | 2.8 s |
| Jupiter v6 | 3,655 | 62.20% | 16.3 s |
| Orca Whirlpools | 2,464 | 56.80% | 24.1 s |
| Raydium AMM v4 | 516 | 11.70% | 116.2 s |

Median failure rate across the sampled programs: **56.80%** (range 11.70% to 89.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **390.96 SOL**.

## Exchange and large-holder balances

10.69M SOL ($984.94M) across 7 publicly-attributed accounts. Net **65K SOL (0.60%) moved off exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.89M | $911.07M | 0.2/h | 4 |
| Gate.io | 380.30K | $35.03M | 331.8/h | 0 |
| Bybit | 339.50K | $31.27M | 26/h | 0 |
| Kraken | 31.41K | $2.89M | 104.8/h | 0 |
| Bitget | 18.55K | $1.71M | 123.1/h | 0 |
| Coinbase (2) | 16.25K | $1.50M | 297/h | 0 |
| Coinbase | 15.91K | $1.47M | 212.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1092 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.250 | 1051 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 1059 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.224 | 1018 | 0.0000 |
| SOL price moves with DeFi TVL | +0.220 | 1092 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.219 | 1018 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1059 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.165 | 1040 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 1040 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 1018 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.119 | 1018 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 92.12 USD | Jupiter (on-chain DEX): 92.23 USD | -0.12% | agree |
| Circulating supply | getSupply (RPC): 590.21M SOL | CoinGecko: 590.21M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-02
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-02
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-02
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-02
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

⚠️ *Sections served from the previous snapshot due to source errors this run: defi.*

<details><summary>Collection errors this run</summary>

- `defi`: `FetchError('every DeFiLlama endpoint failed: {\'tvl\': \'FetchError("https://api.llama.fi/v2/chains failed after 3 attempts: TimeoutError(\\\'The read operation timed out\\\')")\', \'dex\': \'FetchError("https://api.llama.fi/overview/dexs/solana?excludeTotalDataChartBreakdown=true failed after 3 attempts: TimeoutError(\\\'The read operation timed out\\\')")\', \'fees\': \'FetchError("https://api.llama.fi/overview/fees/solana?dataType=dailyFees&excludeTotalDataChartBreakdown=true failed after 3 attempts: TimeoutError(\\\'The read operation timed out\\\')")\'}')`

</details>
