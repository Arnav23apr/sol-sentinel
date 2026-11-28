# Solana Ecosystem Report

*Generated 2026-11-28 09:34 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Network throughput** (critical): Total TPS at 800, far below normal mainnet levels; possible degradation or an RPC reporting artifact.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 800.2 |
| TPS (non-vote) | 800.2 |
| Slot time | 213.2 ms |
| Slot | 475M |
| Block height | 453M |
| Epoch | 1099 (31.52% complete, ~17.5h remaining) |
| Lifetime transactions | 568.7B |
| Circulating supply | 592.4M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 2.70% of slots needed a priority fee (max 249.1K µlam/CU) |
| Node version (RPC) | 4.4.2 |

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
| SOL price | $71.01 (-3.54% 24h) |
| Market cap | $42.07B (rank #7) |
| 24h volume | $2.24B |
| ATH | $293.31 (-75.79% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.62B |
| Stablecoin supply | $13.07B |
| DEX volume (24h) | $943.00M (+8.32% 1d) |
| App fees (24h, all protocols) | $5.61M |
| Chain fees (24h) | $309.63K |
| Jito MEV tips (24h) | $91.27K |
| **REV - Real Economic Value (24h)** | **$400.90K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.68B | +0.41% |
| USDT | $2.29B | +10.60% |
| USDGO | $931.89M | -5.30% |
| USD1 | $851.58M | -3.46% |
| PYUSD | $737.69M | +2.29% |
| USDG | $383.50M | -13.93% |
| SOFID | $282.84M | +1.31% |
| USDe | $240.90M | -4.78% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $168.61M |
| PumpSwap | $139.67M |
| Raydium AMM | $111.99M |
| pump.fun | $107.98M |
| BisonFi | $81.42M |
| Meteora DLMM | $78.64M |
| Manifest Trade | $54.14M |
| Scorch | $39.54M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.30M |
| pump.fun | $1.20M |
| Axiom | $329.43K |
| Jupiter Perpetual Exchange | $240.69K |
| Collector Crypt | $182.67K |
| Raydium AMM | $180.33K |
| Jupiter Lend | $139.94K |
| Lunar Lander | $137.93K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $37.14M |
| xStocks holder positions | 971.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $527.92M |

## Program activity and chain health

Chain tip lag: **+0.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 17,237 | 12.60% | 3.4 s |
| Pump.fun | 5,711 | 32.80% | 10.2 s |
| Jupiter v6 | 1,367 | 50.70% | 43.7 s |
| Orca Whirlpools | 762 | 29.50% | 78.7 s |
| Raydium AMM v4 | 410 | 19.90% | 146 s |

Median failure rate across the sampled programs: **29.50%** (range 12.60% to 50.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.38K SOL**.

## Exchange and large-holder balances

9.51M SOL ($675.28M) across 6 publicly-attributed accounts. Net **73K SOL (0.77%) moved off exchanges** over the last 15.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $660.39M | 0.3/h | 3 |
| Bitget | 61.75K | $4.38M | 131.6/h | 0 |
| Bybit | 59.50K | $4.23M | 88.4/h | 0 |
| Kraken | 48.34K | $3.43M | 126.3/h | 0 |
| Coinbase (2) | 26.64K | $1.89M | 132.3/h | 0 |
| Coinbase | 13.41K | $952.04K | 346.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 15 of 117 tested pairs survive, over 1178 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.271 | 1178 | 0.0000 |
| DEX volume moves with App fees | +0.267 | 1137 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.247 | 1105 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.242 | 1105 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.215 | 1146 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.187 | 1127 | 0.0000 |
| Total TPS moves with Slot time | +0.186 | 1146 | 0.0000 |
| Total TPS moves with Program failure rate | +0.186 | 1127 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.145 | 1105 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 1105 | 0.0000 |
| DEX volume moves with REV | +0.119 | 1178 | 0.0001 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 71.01 USD | Jupiter (on-chain DEX): 70.87 USD | +0.20% | agree |
| Circulating supply | getSupply (RPC): 592.43M SOL | CoinGecko: 592.43M SOL | -0.00% | agree |

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
