# Solana Ecosystem Report

*Generated 2026-11-07 02:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

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
| Epoch | 1079 (48.98% complete, ~13.1h remaining) |
| Lifetime transactions | 565.6B |
| Circulating supply | 591.0M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 21.30% of slots needed a priority fee (max 371.1K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 658 |
| Delinquent validators | 38 |
| Delinquent stake | 0.31% |
| Total active stake | 433.6M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.73% / 36.17% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.06% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.00% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.41% | 0% |
| 5 | `Catz…Diqb` | 9.5M | 2.20% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.7M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $90.53 (+0.54% 24h) |
| Market cap | $53.50B (rank #7) |
| 24h volume | $2.24B |
| ATH | $293.31 (-69.14% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.25B |
| Stablecoin supply | $14.57B |
| DEX volume (24h) | $1.86B (-15.45% 1d) |
| App fees (24h, all protocols) | $9.39M |
| Chain fees (24h) | $466.94K |
| Jito MEV tips (24h) | $125.67K |
| **REV - Real Economic Value (24h)** | **$592.61K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.02B | +0.91% |
| USDT | $2.44B | +1.66% |
| USD1 | $1.24B | -9.75% |
| USDGO | $1.12B | -10.91% |
| PYUSD | $729.07M | +3.98% |
| BUIDL | $540.61M | -33.48% |
| USDG | $494.11M | -19.44% |
| USDe | $295.27M | -6.59% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $231.07M |
| Orca DEX | $229.36M |
| Tessera V | $197.03M |
| Meteora DLMM | $172.58M |
| Raydium AMM | $166.51M |
| Scorch | $147.40M |
| pump.fun | $108.30M |
| PumpSwap | $90.88M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.94M |
| pump.fun | $1.39M |
| Axiom | $532.49K |
| Meteora DLMM | $510.02K |
| Jupiter Perpetual Exchange | $481.93K |
| Raydium AMM | $335.48K |
| Collector Crypt | $281.40K |
| Lunar Lander | $253.89K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $63.66M |
| xStocks holder positions | 886.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $581.63M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 45,863 | 45.60% | 1.3 s |
| Pump.fun | 11,571 | 81.10% | 5.1 s |
| Jupiter v6 | 2,045 | 32.10% | 29.3 s |
| Orca Whirlpools | 2,022 | 55.40% | 29.5 s |
| Raydium AMM v4 | 968 | 45.40% | 61.6 s |

Median failure rate across the sampled programs: **45.60%** (range 32.10% to 81.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.30K SOL**.

## Exchange and large-holder balances

9.60M SOL ($868.86M) across 7 publicly-attributed accounts. Net **246K SOL (2.50%) moved off exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $841.93M | 0.2/h | 3 |
| Gate.io | 104.63K | $9.47M | 77.9/h | 0 |
| Bybit | 97.31K | $8.81M | 35.7/h | 0 |
| Kraken | 31.27K | $2.83M | 183.2/h | 0 |
| Coinbase (2) | 23.56K | $2.13M | 250.9/h | 0 |
| Coinbase | 23.47K | $2.12M | 272.7/h | 0 |
| Bitget | 17.19K | $1.56M | 740.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1106 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.254 | 1065 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1074 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.229 | 1033 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.225 | 1033 | 0.0000 |
| SOL price moves with DeFi TVL | +0.224 | 1106 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1074 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.167 | 1055 | 0.0000 |
| Total TPS moves with Program failure rate | +0.166 | 1055 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1033 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.121 | 1033 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 90.53 USD | Jupiter (on-chain DEX): 90.45 USD | +0.09% | agree |
| Circulating supply | getSupply (RPC): 590.98M SOL | CoinGecko: 590.98M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-06

**Open SIMD proposals:**

- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
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
