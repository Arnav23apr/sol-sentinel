# Solana Ecosystem Report

*Generated 2026-11-09 06:56 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 215.8 ms |
| Slot | 467M |
| Block height | 445M |
| Epoch | 1081 (53.89% complete, ~11.9h remaining) |
| Lifetime transactions | 565.9B |
| Circulating supply | 591.1M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 281.4K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 35 |
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
| SOL price | $86.17 (-3.12% 24h) |
| Market cap | $50.93B (rank #7) |
| 24h volume | $2.32B |
| ATH | $293.31 (-70.62% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.13B |
| Stablecoin supply | $14.83B |
| DEX volume (24h) | $997.09M (+8.68% 1d) |
| App fees (24h, all protocols) | $8.29M |
| Chain fees (24h) | $408.02K |
| Jito MEV tips (24h) | $113.31K |
| **REV - Real Economic Value (24h)** | **$521.33K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.05B | +2.23% |
| USDT | $2.44B | +1.24% |
| USD1 | $1.20B | -12.63% |
| USDGO | $1.10B | -12.10% |
| PYUSD | $741.32M | +4.74% |
| BUIDL | $540.61M | -33.48% |
| USDG | $495.12M | -18.20% |
| USDe | $289.16M | -7.82% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $189.90M |
| PumpSwap | $165.32M |
| Raydium AMM | $126.33M |
| pump.fun | $87.46M |
| BisonFi | $80.20M |
| Meteora DLMM | $79.23M |
| Manifest Trade | $55.52M |
| Tessera V | $48.35M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.68M |
| pump.fun | $1.02M |
| Axiom | $477.60K |
| Jupiter Perpetual Exchange | $464.27K |
| Meteora DLMM | $459.79K |
| LaunchLab | $297.26K |
| Raydium AMM | $260.82K |
| Sanctum Validator LSTs | $239.84K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $86.01M |
| xStocks holder positions | 901.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $581.43M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 32,843 | 34.10% | 1.7 s |
| Pump.fun | 16,821 | 80.80% | 3.5 s |
| Jupiter v6 | 2,697 | 59.10% | 22.2 s |
| Orca Whirlpools | 1,564 | 38.20% | 37.5 s |
| Raydium AMM v4 | 393 | 8.80% | 152.1 s |

Median failure rate across the sampled programs: **38.20%** (range 8.80% to 80.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **2.02K SOL**.

## Exchange and large-holder balances

9.54M SOL ($822.44M) across 7 publicly-attributed accounts. Net **51K SOL (0.53%) moved off exchanges** over the last 21.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $801.38M | 0.4/h | 5 |
| Bybit | 97.60K | $8.41M | 41.6/h | 0 |
| Gate.io | 67.78K | $5.84M | 170.1/h | 0 |
| Coinbase (2) | 26.07K | $2.25M | 170.9/h | 0 |
| Kraken | 25.12K | $2.16M | 204.4/h | 0 |
| Coinbase | 14.16K | $1.22M | 364/h | 0 |
| Bitget | 13.65K | $1.18M | 142.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1116 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.257 | 1075 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.235 | 1043 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.230 | 1043 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 1084 | 0.0000 |
| SOL price moves with DeFi TVL | +0.228 | 1116 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1084 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.174 | 1065 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1065 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1043 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.128 | 1043 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 86.17 USD | Jupiter (on-chain DEX): 86 USD | +0.20% | agree |
| Circulating supply | getSupply (RPC): 591.09M SOL | CoinGecko: 591.09M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-06

**Open SIMD proposals:**

- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
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
