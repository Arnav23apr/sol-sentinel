# Solana Ecosystem Report

*Generated 2026-11-10 00:45 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.4K |
| TPS (non-vote) | 1.4K |
| Slot time | 214.7 ms |
| Slot | 468M |
| Block height | 446M |
| Epoch | 1082 (23.04% complete, ~19.8h remaining) |
| Lifetime transactions | 566.0B |
| Circulating supply | 591.1M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 10.70% of slots needed a priority fee (max 3.1M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 657 |
| Delinquent validators | 41 |
| Delinquent stake | 0.22% |
| Total active stake | 434.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.34% / 24.62% / 36.08% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 22.81% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 16.9M | 3.89% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.00% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.37% | 0% |
| 5 | `51JB…UNAm` | 9.6M | 2.21% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.20% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.80% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.55% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $86.41 (-0.54% 24h) |
| Market cap | $51.08B (rank #7) |
| 24h volume | $2.43B |
| ATH | $293.31 (-70.54% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.09B |
| Stablecoin supply | $14.55B |
| DEX volume (24h) | $1.20B (+15.41% 1d) |
| App fees (24h, all protocols) | $8.68M |
| Chain fees (24h) | $408.02K |
| Jito MEV tips (24h) | $107.44K |
| **REV - Real Economic Value (24h)** | **$515.47K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.09B | +2.87% |
| USDT | $2.24B | -7.04% |
| USD1 | $1.15B | -16.33% |
| USDGO | $1.09B | -13.30% |
| PYUSD | $738.70M | +4.39% |
| BUIDL | $490.78M | -39.61% |
| USDG | $489.63M | -19.12% |
| USDe | $287.63M | -8.33% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $242.14M |
| PumpSwap | $165.32M |
| Raydium AMM | $160.61M |
| BisonFi | $103.44M |
| Meteora DLMM | $97.96M |
| pump.fun | $78.78M |
| Scorch | $63.55M |
| Manifest Trade | $48.06M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.68M |
| pump.fun | $1.02M |
| Meteora DLMM | $527.12K |
| Axiom | $485.59K |
| Jupiter Perpetual Exchange | $464.27K |
| Raydium AMM | $336.43K |
| LaunchLab | $297.26K |
| BONK.fun Launchpad | $276.74K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $112.54M |
| xStocks holder positions | 904.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $581.48M |

## Program activity and chain health

Chain tip lag: **+1.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 31,055 | 31.20% | 1.7 s |
| Pump.fun | 10,523 | 70.70% | 5.6 s |
| Jupiter v6 | 2,451 | 44.70% | 24.3 s |
| Orca Whirlpools | 1,450 | 52.40% | 41.2 s |
| Raydium AMM v4 | 718 | 19.60% | 83.5 s |

Median failure rate across the sampled programs: **44.70%** (range 19.60% to 70.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **497.68 SOL**.

## Exchange and large-holder balances

9.64M SOL ($833.41M) across 7 publicly-attributed accounts.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $803.61M | 0.4/h | 5 |
| Coinbase | 100.96K | $8.72M | 280.2/h | 0 |
| Bybit | 97.64K | $8.44M | 28.4/h | 0 |
| Gate.io | 80.79K | $6.98M | 118.9/h | 0 |
| Kraken | 31.02K | $2.68M | 146.9/h | 0 |
| Coinbase (2) | 19.63K | $1.70M | 292.9/h | 0 |
| Bitget | 14.84K | $1.28M | 102.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1117 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.260 | 1076 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.235 | 1044 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.230 | 1044 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 1085 | 0.0000 |
| SOL price moves with DeFi TVL | +0.227 | 1117 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1085 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.174 | 1066 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1066 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 1044 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.128 | 1044 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 86.41 USD | Jupiter (on-chain DEX): 86.39 USD | +0.02% | agree |
| Circulating supply | getSupply (RPC): 591.15M SOL | CoinGecko: 591.15M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS validator ranks](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-09
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04

**Recently merged SIMDs:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31

**Latest Agave release:** [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06)

**Latest Firedancer release:** [v26.10.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.6) (2026-11-05)

## Ecosystem news

- **[Solana Set for Another Tokenized Stock Venue as Formation Notifies the SEC](https://decrypt.co/382859/solana-tokenized-stock-venue-formation-sec)** - Decrypt, 2026-11-09
- **[Formation notifies SEC to operate first tokenized securities venue on Solana](https://www.theblock.co/news/defi/2026-11-09-formation-tokenized-securities-solana-436060)** - The Block, 2026-11-09
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
