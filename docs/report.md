# Solana Ecosystem Report

*Generated 2026-10-28 20:39 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 15.0 robust standard deviations above its 7-day baseline: a 994.1% move to 0.93 % from a typical 0.09.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.4K |
| TPS (non-vote) | 2.4K |
| Slot time | 213.9 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1070 (86.71% complete, ~3.4h remaining) |
| Lifetime transactions | 564.2B |
| Circulating supply | 589.9M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 660 |
| Delinquent validators | 31 |
| Delinquent stake | 0.93% |
| Total active stake | 433.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.46% / 24.81% / 36.03% |
| Commission (stake-weighted, delegatable validators) | 3.73% |
| Stake on private (100% commission) validators | 24.13% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.85% | 0% |
| 3 | `3N7s…iD5g` | 12.8M | 2.95% | 0% |
| 4 | `8Gbw…F8iD` | 10.8M | 2.50% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.24% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.63% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $102.13 (+1.26% 24h) |
| Market cap | $60.22B (rank #7) |
| 24h volume | $2.64B |
| ATH | $293.31 (-65.18% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.73B |
| Stablecoin supply | $15.54B |
| DEX volume (24h) | $1.58B (-23.57% 1d) |
| App fees (24h, all protocols) | $10.91M |
| Chain fees (24h) | $538.02K |
| Jito MEV tips (24h) | $134.81K |
| **REV - Real Economic Value (24h)** | **$672.83K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.92B | -0.69% |
| USDT | $2.63B | -2.23% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.30B | +0.70% |
| BUIDL | $875.97M | -1.14% |
| PYUSD | $695.65M | +2.98% |
| USDG | $628.48M | -0.35% |
| USDe | $316.02M | -18.83% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $193.28M |
| BisonFi | $191.20M |
| Manifest Trade | $181.63M |
| Orca DEX | $161.86M |
| Tessera V | $142.35M |
| pump.fun | $140.44M |
| Raydium AMM | $138.09M |
| Meteora DLMM | $80.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.00M |
| pump.fun | $1.85M |
| Axiom | $645.78K |
| Collector Crypt | $582.40K |
| Meteora DLMM | $323.86K |
| pump.fun Mobile App | $294.01K |
| Raydium AMM | $287.84K |
| Sanctum Validator LSTs | $277.75K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $65.11M |
| xStocks holder positions | 855.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $607.24M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 58,976 | 50.90% | 0.9 s |
| Pump.fun | 22,791 | 81.20% | 2.6 s |
| Jupiter v6 | 9,051 | 53.20% | 6.4 s |
| Orca Whirlpools | 3,992 | 43.30% | 14.8 s |
| Raydium AMM v4 | 1,024 | 11.50% | 58.4 s |

Median failure rate across the sampled programs: **50.90%** (range 11.50% to 81.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **117.59 SOL**.

## Exchange and large-holder balances

13.62M SOL ($1.39B) across 8 publicly-attributed accounts. Net **354K SOL (2.67%) moved onto exchanges** over the last 21.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.14B | 0.2/h | 3 |
| Binance (2) | 1.59M | $162.54M | 923.1/h | 0 |
| Gate.io | 349.12K | $35.66M | 276.3/h | 0 |
| Bybit | 330.88K | $33.79M | 35.7/h | 0 |
| Bitget | 96.96K | $9.90M | 160.1/h | 0 |
| Kraken | 46.46K | $4.75M | 437.4/h | 0 |
| Coinbase (2) | 13.31K | $1.36M | 300.5/h | 0 |
| Coinbase | 12.76K | $1.30M | 406.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1069 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.261 | 1028 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1035 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.221 | 994 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.216 | 994 | 0.0000 |
| SOL price moves with DeFi TVL | +0.207 | 1069 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1035 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 1016 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 1016 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 994 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.115 | 994 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 102.13 USD | Jupiter (on-chain DEX): 101.95 USD | +0.18% | agree |
| Circulating supply | getSupply (RPC): 589.93M SOL | CoinGecko: 589.93M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14

**Recently merged SIMDs:**

- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-28
- [SIMD-0140: Migrate Config Program to Core BPF](https://github.com/solana-foundation/solana-improvement-documents/pull/140) - updated 2026-10-28
- [SIMD-0133: Syscall: Get Epoch Stake](https://github.com/solana-foundation/solana-improvement-documents/pull/133) - updated 2026-10-28
- [SIMD-0089: Programify Feature Gate Program](https://github.com/solana-foundation/solana-improvement-documents/pull/89) - updated 2026-10-28
- [SIMD-0088: Enable Core BPF Programs](https://github.com/solana-foundation/solana-improvement-documents/pull/88) - updated 2026-10-28

**Latest Agave release:** [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28)

**Latest Firedancer release:** [v26.10.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.5) (2026-10-27)

## Ecosystem news

- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
