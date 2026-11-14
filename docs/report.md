# Solana Ecosystem Report

*Generated 2026-11-14 09:36 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.2K |
| TPS (non-vote) | 1.2K |
| Slot time | 215.1 ms |
| Slot | 469M |
| Block height | 447M |
| Epoch | 1086 (29.59% complete, ~18.2h remaining) |
| Lifetime transactions | 566.6B |
| Circulating supply | 591.6M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 2.2M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 37 |
| Delinquent stake | 0.11% |
| Total active stake | 429.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.34% / 24.75% / 35.92% |
| Commission (stake-weighted, delegatable validators) | 3.86% |
| Stake on private (100% commission) validators | 22.94% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.95% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.82% | 7% |
| 3 | `3N7s…iD5g` | 12.6M | 2.94% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.36% | 0% |
| 5 | `51JB…UNAm` | 9.7M | 2.27% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.23% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.9M | 1.84% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $75.68 (-5.26% 24h) |
| Market cap | $44.76B (rank #7) |
| 24h volume | $3.33B |
| ATH | $293.31 (-74.20% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.84B |
| Stablecoin supply | $13.94B |
| DEX volume (24h) | $1.45B (-3.34% 1d) |
| App fees (24h, all protocols) | $9.34M |
| Chain fees (24h) | $448.75K |
| Jito MEV tips (24h) | $107.77K |
| **REV - Real Economic Value (24h)** | **$556.52K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.29B | +3.89% |
| USDT | $2.05B | -15.95% |
| USDGO | $1.06B | -4.90% |
| USD1 | $1.04B | -16.16% |
| PYUSD | $782.32M | +7.37% |
| USDG | $443.50M | -10.22% |
| USDe | $277.52M | -6.03% |
| SOFID | $271.17M | +1.93% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $228.27M |
| PumpSwap | $177.25M |
| BisonFi | $147.27M |
| Meteora DLMM | $144.66M |
| Raydium AMM | $122.16M |
| pump.fun | $102.29M |
| Manifest Trade | $78.86M |
| Scorch | $68.83M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.04M |
| pump.fun | $1.38M |
| Meteora DLMM | $655.32K |
| Jupiter Perpetual Exchange | $577.30K |
| Axiom | $492.53K |
| Collector Crypt | $250.52K |
| Jupiter Lend | $244.53K |
| Raydium AMM | $232.36K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $88.74M |
| xStocks holder positions | 933.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $604.87M |

## Program activity and chain health

Chain tip lag: **+1.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 45,914 | 38.90% | 1.1 s |
| Pump.fun | 20,770 | 81.10% | 2.8 s |
| Jupiter v6 | 1,451 | 42.40% | 41.3 s |
| Orca Whirlpools | 1,191 | 42.40% | 50.3 s |
| Raydium AMM v4 | 478 | 16.60% | 125 s |

Median failure rate across the sampled programs: **42.40%** (range 16.60% to 81.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.31K SOL**.

## Exchange and large-holder balances

9.59M SOL ($725.66M) across 7 publicly-attributed accounts. Net **56K SOL (0.59%) moved onto exchanges** over the last 17.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $703.82M | 0.3/h | 5 |
| Coinbase | 102.62K | $7.77M | 164.8/h | 0 |
| Gate.io | 49.40K | $3.74M | 307.2/h | 0 |
| Bybit | 47.55K | $3.60M | 31.9/h | 0 |
| Kraken | 37.92K | $2.87M | 178.9/h | 0 |
| Coinbase (2) | 29.08K | $2.20M | 167.4/h | 0 |
| Bitget | 22.00K | $1.66M | 152.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1133 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.259 | 1092 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.243 | 1060 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.239 | 1060 | 0.0000 |
| SOL price moves with DeFi TVL | +0.233 | 1133 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.224 | 1101 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 1101 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.176 | 1082 | 0.0000 |
| Total TPS moves with Program failure rate | +0.175 | 1082 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 1060 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.127 | 1060 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 75.68 USD | Jupiter (on-chain DEX): 75.55 USD | +0.17% | agree |
| Circulating supply | getSupply (RPC): 591.57M SOL | CoinGecko: 591.57M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-12
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

**Latest Firedancer release:** [v26.11.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.0) (2026-11-11)

## Ecosystem news

- **[SoFi Brings Its Bank-Issued Stablecoin to Polygon’s Payments Stack](https://decrypt.co/383096/sofi-brings-bank-issued-stablecoin-polygon-payments-stack)** - Decrypt, 2026-11-12
- **[DTCC to Bring Tokenized Stocks and Treasuries to Solana in 2027](https://decrypt.co/383132/dtcc-to-bring-tokenized-stocks-and-treasuries-to-solana-in-2027)** - Decrypt, 2026-11-12
- **[What Are Solana Privacy Rings? Inside Helius’ Privacy Protocol for Solana](https://decrypt.co/resources/what-are-solana-privacy-rings-inside-helius-privacy-protocol-for-solana)** - Decrypt, 2026-11-11
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
