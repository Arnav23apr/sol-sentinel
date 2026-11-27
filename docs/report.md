# Solana Ecosystem Report

*Generated 2026-11-27 18:33 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.7 robust standard deviations above its 7-day baseline: a 233.3% move to 0.06 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.0K |
| TPS (non-vote) | 2.0K |
| Slot time | 212.8 ms |
| Slot | 475M |
| Block height | 453M |
| Epoch | 1098 (73.17% complete, ~6.9h remaining) |
| Lifetime transactions | 568.7B |
| Circulating supply | 592.2M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 3.30% of slots needed a priority fee (max 489.4K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 654 |
| Delinquent validators | 34 |
| Delinquent stake | 0.06% |
| Total active stake | 424.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.98% / 36.11% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.25% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 15.8M | 3.73% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.93% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.9M | 2.34% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.27% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.19% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.90% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.59% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $71.71 (+0.65% 24h) |
| Market cap | $42.46B (rank #7) |
| 24h volume | $2.59B |
| ATH | $293.31 (-75.55% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.63B |
| Stablecoin supply | $12.77B |
| DEX volume (24h) | $870.58M (-42.38% 1d) |
| App fees (24h, all protocols) | $6.15M |
| Chain fees (24h) | $332.65K |
| Jito MEV tips (24h) | $81.10K |
| **REV - Real Economic Value (24h)** | **$413.74K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.78B | +1.14% |
| USDT | $1.89B | -11.66% |
| USDGO | $932.10M | -7.10% |
| USD1 | $869.78M | -3.80% |
| PYUSD | $720.57M | -0.54% |
| USDG | $384.60M | -14.83% |
| SOFID | $279.99M | +1.41% |
| USDe | $241.16M | -9.15% |

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
| Raydium AMM | $164.24K |
| Lunar Lander | $140.35K |
| Jupiter Lend | $139.94K |
| Orca DEX | $130.93K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $43.41M |
| xStocks holder positions | 970.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $544.05M |

## Program activity and chain health

Chain tip lag: **+1.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 90,883 | 47.60% | 0.6 s |
| Pump.fun | 46,382 | 87.30% | 0.9 s |
| Orca Whirlpools | 4,422 | 68.70% | 13.4 s |
| Jupiter v6 | 2,908 | 49.70% | 20.4 s |
| Raydium AMM v4 | 888 | 18.10% | 67.2 s |

Median failure rate across the sampled programs: **49.70%** (range 18.10% to 87.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **980.31 SOL**.

## Exchange and large-holder balances

9.58M SOL ($687.20M) across 7 publicly-attributed accounts. Net **11K SOL (0.11%) moved onto exchanges** over the last 18.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $666.90M | 0.3/h | 1 |
| Bybit | 59.50K | $4.27M | 28/h | 0 |
| Bitget | 58.52K | $4.20M | 126.8/h | 0 |
| Kraken | 51.31K | $3.68M | 275.2/h | 0 |
| Gate.io | 41.22K | $2.96M | 12.2/h | 0 |
| Coinbase (2) | 40.58K | $2.91M | 268.5/h | 0 |
| Coinbase | 31.92K | $2.29M | 256.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1176 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.269 | 1176 | 0.0000 |
| DEX volume moves with App fees | +0.268 | 1135 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.247 | 1103 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.243 | 1103 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.216 | 1144 | 0.0000 |
| Total TPS moves with Slot time | +0.187 | 1144 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.185 | 1125 | 0.0000 |
| Total TPS moves with Program failure rate | +0.184 | 1125 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 1103 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 1103 | 0.0000 |
| DEX volume moves with REV | +0.119 | 1176 | 0.0000 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 71.71 USD | Jupiter (on-chain DEX): 71.76 USD | -0.07% | agree |
| Circulating supply | getSupply (RPC): 592.24M SOL | CoinGecko: 592.24M SOL | -0.00% | agree |

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

**Latest Agave release:** [v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) (2026-11-25)

**Latest Firedancer release:** [v26.11.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.1) (2026-11-25)

## Ecosystem news

- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
