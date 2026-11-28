# Solana Ecosystem Report

*Generated 2026-11-28 01:43 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.5K |
| TPS (non-vote) | 1.5K |
| Slot time | 214.3 ms |
| Slot | 475M |
| Block height | 453M |
| Epoch | 1099 (1.00% complete, ~25.5h remaining) |
| Lifetime transactions | 568.7B |
| Circulating supply | 592.4M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 0.00% of slots needed a priority fee (max 0 µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 655 |
| Delinquent validators | 10 |
| Delinquent stake | 0.03% |
| Total active stake | 423.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 24.95% / 36.11% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.29% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 15.9M | 3.76% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.94% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.42% | 0% |
| 5 | `51JB…UNAm` | 9.9M | 2.34% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.27% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.20% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.90% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.65% | 0% |
| 10 | `CvSb…wycB` | 6.3M | 1.50% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $71.98 (+0.90% 24h) |
| Market cap | $42.64B (rank #7) |
| 24h volume | $2.64B |
| ATH | $293.31 (-75.46% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.64B |
| Stablecoin supply | $13.13B |
| DEX volume (24h) | $885.19M (+1.68% 1d) |
| App fees (24h, all protocols) | $6.24M |
| Chain fees (24h) | $332.65K |
| Jito MEV tips (24h) | $88.73K |
| **REV - Real Economic Value (24h)** | **$421.38K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.72B | +1.03% |
| USDT | $2.29B | +10.60% |
| USDGO | $932.14M | -5.30% |
| USD1 | $869.94M | -2.24% |
| PYUSD | $736.91M | +2.15% |
| USDG | $384.82M | -13.65% |
| SOFID | $282.75M | +1.31% |
| USDe | $240.99M | -4.78% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $139.53M |
| Raydium AMM | $111.99M |
| pump.fun | $107.98M |
| PumpSwap | $86.72M |
| BisonFi | $81.42M |
| Meteora DLMM | $78.64M |
| Manifest Trade | $52.73M |
| Scorch | $39.54M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.42M |
| pump.fun | $1.23M |
| Axiom | $329.43K |
| Sanctum Validator LSTs | $203.94K |
| Raydium AMM | $173.75K |
| Collector Crypt | $169.71K |
| Jupiter Lend | $139.94K |
| Lunar Lander | $134.25K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $41.23M |
| xStocks holder positions | 971.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $548.57M |

## Program activity and chain health

Chain tip lag: **+0.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 34,718 | 51.20% | 1.7 s |
| Pump.fun | 11,869 | 37.70% | 4.9 s |
| Orca Whirlpools | 2,811 | 41.80% | 21 s |
| Jupiter v6 | 2,467 | 57.20% | 24 s |
| Raydium AMM v4 | 666 | 18.50% | 89.8 s |

Median failure rate across the sampled programs: **41.80%** (range 18.50% to 57.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.58K SOL**.

## Exchange and large-holder balances

9.54M SOL ($686.68M) across 7 publicly-attributed accounts. Net **56K SOL (0.59%) moved off exchanges** over the last 16.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $669.41M | 0.3/h | 2 |
| Bybit | 59.50K | $4.28M | 30.1/h | 0 |
| Bitget | 55.88K | $4.02M | 94.2/h | 0 |
| Gate.io | 41.22K | $2.97M | 12.2/h | 0 |
| Kraken | 32.60K | $2.35M | 150/h | 0 |
| Coinbase (2) | 28.55K | $2.06M | 289.2/h | 0 |
| Coinbase | 22.10K | $1.59M | 271.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1177 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.270 | 1136 | 0.0000 |
| SOL price moves with DeFi TVL | +0.269 | 1177 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.248 | 1104 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.243 | 1104 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.215 | 1145 | 0.0000 |
| Total TPS moves with Slot time | +0.186 | 1145 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.186 | 1126 | 0.0000 |
| Total TPS moves with Program failure rate | +0.185 | 1126 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.145 | 1104 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 1104 | 0.0000 |
| DEX volume moves with REV | +0.121 | 1177 | 0.0000 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 71.98 USD | Jupiter (on-chain DEX): 71.97 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 592.43M SOL | CoinGecko: 592.38M SOL | +0.01% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-26
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20

**Recently merged SIMDs:**

- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-11-27
- [Withdraw SIMD-0506](https://github.com/solana-foundation/solana-improvement-documents/pull/738) - updated 2026-11-26
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-23
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02

**Latest Agave release:** [v4.5.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.1) (2026-11-27)

**Latest Firedancer release:** [v26.11.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.1) (2026-11-25)

## Ecosystem news

- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
