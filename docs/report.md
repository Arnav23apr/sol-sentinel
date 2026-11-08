# Solana Ecosystem Report

*Generated 2026-11-08 20:39 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.7K |
| TPS (non-vote) | 1.7K |
| Slot time | 215.4 ms |
| Slot | 467M |
| Block height | 445M |
| Epoch | 1081 (13.94% complete, ~22.2h remaining) |
| Lifetime transactions | 565.8B |
| Circulating supply | 591.1M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 25.30% of slots needed a priority fee (max 8.9M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 36 |
| Delinquent stake | 0.14% |
| Total active stake | 433.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.66% / 36.13% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.07% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.01% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.37% | 0% |
| 5 | `Catz…Diqb` | 9.6M | 2.20% | 5% |
| 6 | `51JB…UNAm` | 9.6M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.55% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $89.32 (-0.11% 24h) |
| Market cap | $52.80B (rank #7) |
| 24h volume | $970.88M |
| ATH | $293.31 (-69.55% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.22B |
| Stablecoin supply | $14.64B |
| DEX volume (24h) | $917.44M (-38.01% 1d) |
| App fees (24h, all protocols) | $8.03M |
| Chain fees (24h) | $392.52K |
| Jito MEV tips (24h) | $115.14K |
| **REV - Real Economic Value (24h)** | **$507.65K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.04B | +1.46% |
| USDT | $2.44B | +0.41% |
| USD1 | $1.21B | -11.91% |
| USDGO | $1.12B | -10.91% |
| PYUSD | $742.17M | +5.45% |
| BUIDL | $540.61M | -33.48% |
| USDG | $494.75M | -18.09% |
| USDe | $289.64M | -7.92% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $217.32M |
| pump.fun | $87.46M |
| BisonFi | $80.20M |
| Meteora DLMM | $79.23M |
| Raydium AMM | $79.08M |
| Orca DEX | $77.44M |
| Tessera V | $48.35M |
| fomo Wallet | $41.49M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.87M |
| pump.fun | $1.10M |
| Axiom | $477.60K |
| Meteora DLMM | $459.79K |
| BONK.fun Launchpad | $257.16K |
| Sanctum Validator LSTs | $247.11K |
| LaunchLab | $235.23K |
| Lunar Lander | $206.71K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $23.89M |
| xStocks holder positions | 891.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $581.50M |

## Program activity and chain health

Chain tip lag: **+1.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 73,352 | 49.50% | 0.6 s |
| Pump.fun | 19,893 | 86.70% | 2.6 s |
| Jupiter v6 | 9,749 | 75.80% | 6 s |
| Orca Whirlpools | 9,222 | 41.50% | 6 s |
| Raydium AMM v4 | 867 | 12.20% | 69.1 s |

Median failure rate across the sampled programs: **49.50%** (range 12.20% to 86.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **2.09K SOL**.

## Exchange and large-holder balances

9.60M SOL ($857.08M) across 7 publicly-attributed accounts. Net **4K SOL (0.04%) moved off exchanges** over the last 21.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $830.68M | 0.3/h | 5 |
| Gate.io | 98.92K | $8.84M | 171.3/h | 0 |
| Bybit | 97.60K | $8.72M | 18.3/h | 0 |
| Coinbase | 28.38K | $2.54M | 299.3/h | 0 |
| Kraken | 25.74K | $2.30M | 256.4/h | 0 |
| Coinbase (2) | 24.99K | $2.23M | 329.4/h | 0 |
| Bitget | 20.02K | $1.79M | 107.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1114 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.255 | 1073 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.234 | 1041 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.230 | 1041 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 1082 | 0.0000 |
| SOL price moves with DeFi TVL | +0.227 | 1114 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1082 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.173 | 1063 | 0.0000 |
| Total TPS moves with Program failure rate | +0.172 | 1063 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1041 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.128 | 1041 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 89.32 USD | Jupiter (on-chain DEX): 89.14 USD | +0.20% | agree |
| Circulating supply | getSupply (RPC): 591.09M SOL | CoinGecko: 591.09M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-06

**Open SIMD proposals:**

- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-06
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

**Recently merged SIMDs:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-06
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31

**Latest Agave release:** [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06)

**Latest Firedancer release:** [v26.10.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.6) (2026-11-05)

## Ecosystem news

- **[Solana Labs’ Leap Launches Mobile App for Trading Tokenized Stocks and Crypto](https://decrypt.co/382609/solana-labs-leap-launches-mobile-app-tokenized-stocks-crypto)** - Decrypt, 2026-11-05
- **[Stablecoins Go Mainstream as Samsung Wallet Adds USDC on Solana](https://decrypt.co/382586/stablecoins-samsung-wallet-adds-usdc-solana)** - Decrypt, 2026-11-05
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
