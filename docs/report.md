# Solana Ecosystem Report

*Generated 2026-10-28 15:35 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 14.2 robust standard deviations above its 7-day baseline: a 942.4% move to 0.89 % from a typical 0.09.
- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 6.3 robust standard deviations below its 7-day baseline: a 3.2% move to 15,119,256,353.00 USD from a typical 15,618,778,640.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.1K |
| TPS (non-vote) | 2.1K |
| Slot time | 211.7 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1070 (66.88% complete, ~8.4h remaining) |
| Lifetime transactions | 564.2B |
| Circulating supply | 589.9M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 7.30% of slots needed a priority fee (max 3.7M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 30 |
| Delinquent stake | 0.89% |
| Total active stake | 433.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.46% / 24.79% / 36.02% |
| Commission (stake-weighted, delegatable validators) | 3.73% |
| Stake on private (100% commission) validators | 24.12% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.84% | 0% |
| 3 | `3N7s…iD5g` | 12.8M | 2.95% | 0% |
| 4 | `8Gbw…F8iD` | 10.8M | 2.50% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.24% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.62% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $100.85 (+0.19% 24h) |
| Market cap | $59.48B (rank #7) |
| 24h volume | $2.07B |
| ATH | $293.31 (-65.62% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.75B |
| Stablecoin supply | $15.12B |
| DEX volume (24h) | $1.58B (-23.57% 1d) |
| App fees (24h, all protocols) | $10.91M |
| Chain fees (24h) | $538.02K |
| Jito MEV tips (24h) | $140.37K |
| **REV - Real Economic Value (24h)** | **$678.39K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.51B | -6.53% |
| USDT | $2.63B | -2.23% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.30B | +0.70% |
| BUIDL | $878.04M | -0.91% |
| PYUSD | $694.77M | +2.86% |
| USDG | $618.56M | -1.90% |
| USDe | $316.32M | -18.69% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Manifest Trade | $194.98M |
| PumpSwap | $193.28M |
| BisonFi | $191.20M |
| Orca DEX | $160.48M |
| Tessera V | $142.35M |
| pump.fun | $140.44M |
| Raydium AMM | $121.81M |
| Meteora DLMM | $80.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.00M |
| pump.fun | $1.85M |
| Axiom | $645.78K |
| Meteora DLMM | $323.86K |
| pump.fun Mobile App | $294.01K |
| Sanctum Validator LSTs | $277.75K |
| StonkFun | $268.13K |
| Raydium AMM | $264.37K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $57.98M |
| xStocks holder positions | 855.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $602.20M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 58,172 | 47.40% | 0.8 s |
| Pump.fun | 25,250 | 74.70% | 2.3 s |
| Orca Whirlpools | 7,224 | 51.10% | 8.3 s |
| Jupiter v6 | 4,604 | 56.50% | 12.9 s |
| Raydium AMM v4 | 702 | 12.90% | 85.3 s |

Median failure rate across the sampled programs: **51.10%** (range 12.90% to 74.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **254.41 SOL**.

## Exchange and large-holder balances

13.51M SOL ($1.36B) across 8 publicly-attributed accounts. Net **228K SOL (1.72%) moved onto exchanges** over the last 19.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.13B | 0.2/h | 3 |
| Binance (2) | 1.48M | $148.80M | 1.6K/h | 0 |
| Gate.io | 353.37K | $35.64M | 315.5/h | 0 |
| Bybit | 330.88K | $33.37M | 34.7/h | 0 |
| Bitget | 101.27K | $10.21M | 187.4/h | 0 |
| Kraken | 49.71K | $5.01M | 298.5/h | 0 |
| Coinbase | 11.97K | $1.21M | 312.8/h | 1 |
| Coinbase (2) | 11.39K | $1.15M | 411.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1068 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.261 | 1027 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1034 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.220 | 993 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.215 | 993 | 0.0000 |
| SOL price moves with DeFi TVL | +0.209 | 1068 | 0.0000 |
| Total TPS moves with Slot time | +0.197 | 1034 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 1015 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 1015 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 993 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.115 | 993 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 100.85 USD | Jupiter (on-chain DEX): 100.75 USD | +0.10% | agree |
| Circulating supply | getSupply (RPC): 589.93M SOL | CoinGecko: 589.93M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-27
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

**Recently merged SIMDs:**

- [SIMD-0140: Migrate Config Program to Core BPF](https://github.com/solana-foundation/solana-improvement-documents/pull/140) - updated 2026-10-28
- [SIMD-0133: Syscall: Get Epoch Stake](https://github.com/solana-foundation/solana-improvement-documents/pull/133) - updated 2026-10-28
- [SIMD-0089: Programify Feature Gate Program](https://github.com/solana-foundation/solana-improvement-documents/pull/89) - updated 2026-10-28
- [SIMD-0088: Enable Core BPF Programs](https://github.com/solana-foundation/solana-improvement-documents/pull/88) - updated 2026-10-28
- [SIMD-0688: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-28
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-28

**Latest Agave release:** [v4.5.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.4) (2026-10-26)

**Latest Firedancer release:** [v26.10.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.5) (2026-10-27)

## Ecosystem news

- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
