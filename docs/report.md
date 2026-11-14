# Solana Ecosystem Report

*Generated 2026-11-14 02:31 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.4K |
| TPS (non-vote) | 2.4K |
| Slot time | 215.8 ms |
| Slot | 469M |
| Block height | 447M |
| Epoch | 1086 (2.16% complete, ~25.3h remaining) |
| Lifetime transactions | 566.6B |
| Circulating supply | 591.6M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 2.5M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 663 |
| Delinquent validators | 36 |
| Delinquent stake | 0.09% |
| Total active stake | 429.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.33% / 24.74% / 35.91% |
| Commission (stake-weighted, delegatable validators) | 3.86% |
| Stake on private (100% commission) validators | 22.94% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.95% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.81% | 7% |
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
| SOL price | $75.65 (-6.42% 24h) |
| Market cap | $44.71B (rank #7) |
| 24h volume | $3.67B |
| ATH | $293.31 (-74.21% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.90B |
| Stablecoin supply | $13.96B |
| DEX volume (24h) | $1.45B (-3.37% 1d) |
| App fees (24h, all protocols) | $9.35M |
| Chain fees (24h) | $448.75K |
| Jito MEV tips (24h) | $114.57K |
| **REV - Real Economic Value (24h)** | **$563.32K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.31B | +4.19% |
| USDT | $2.05B | -15.95% |
| USDGO | $1.06B | -4.90% |
| USD1 | $1.04B | -16.16% |
| PYUSD | $782.48M | +7.38% |
| USDG | $443.41M | -10.24% |
| USDe | $277.75M | -6.01% |
| SOFID | $271.31M | +1.93% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $241.30M |
| PumpSwap | $177.25M |
| BisonFi | $147.27M |
| Meteora DLMM | $144.66M |
| Raydium AMM | $134.81M |
| pump.fun | $102.29M |
| Manifest Trade | $78.12M |
| Scorch | $68.83M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.04M |
| pump.fun | $1.38M |
| Meteora DLMM | $655.32K |
| Jupiter Perpetual Exchange | $577.30K |
| Axiom | $492.53K |
| Collector Crypt | $348.87K |
| Raydium AMM | $262.92K |
| Jupiter Lend | $244.53K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $97.74M |
| xStocks holder positions | 931.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $605.33M |

## Program activity and chain health

Chain tip lag: **+1.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 67,354 | 42.20% | 0.9 s |
| Pump.fun | 26,163 | 85.60% | 2.2 s |
| Orca Whirlpools | 19,184 | 62.50% | 3 s |
| Jupiter v6 | 11,786 | 65.80% | 5 s |
| Raydium AMM v4 | 1,592 | 32.40% | 37.5 s |

Median failure rate across the sampled programs: **62.50%** (range 32.40% to 85.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.47K SOL**.

## Exchange and large-holder balances

9.48M SOL ($717.31M) across 5 publicly-attributed accounts. Net **115K SOL (1.20%) moved off exchanges** over the last 18.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $703.55M | 0.3/h | 5 |
| Gate.io | 72.57K | $5.49M | 206.5/h | 0 |
| Bybit | 47.55K | $3.60M | 32.9/h | 0 |
| Kraken | 40.94K | $3.10M | 274.8/h | 0 |
| Bitget | 20.95K | $1.58M | 178.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1132 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.261 | 1091 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.242 | 1059 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.237 | 1059 | 0.0000 |
| SOL price moves with DeFi TVL | +0.234 | 1132 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.224 | 1100 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 1100 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.174 | 1081 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1081 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 1059 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.125 | 1059 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 75.65 USD | Jupiter (on-chain DEX): 75.52 USD | +0.17% | agree |
| Circulating supply | getSupply (RPC): 591.57M SOL | CoinGecko: 591.52M SOL | +0.01% | agree |

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
