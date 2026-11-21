# Solana Ecosystem Report

*Generated 2026-11-21 18:24 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.0K |
| TPS (non-vote) | 2.0K |
| Slot time | 215.8 ms |
| Slot | 472M |
| Block height | 450M |
| Epoch | 1093 (14.46% complete, ~22.2h remaining) |
| Lifetime transactions | 567.8B |
| Circulating supply | 592.0M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 1.30% of slots needed a priority fee (max 200.0K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 24 |
| Delinquent stake | 0.02% |
| Total active stake | 428.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.86% / 35.93% |
| Commission (stake-weighted, delegatable validators) | 3.85% |
| Stake on private (100% commission) validators | 23.01% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.98% | 0% |
| 2 | `CcaH…oTN1` | 16.3M | 3.81% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.90% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.39% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.29% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.25% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.16% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.86% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.58% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $70.54 (+1.68% 24h) |
| Market cap | $41.76B (rank #7) |
| 24h volume | $4.39B |
| ATH | $293.31 (-75.95% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.63B |
| Stablecoin supply | $13.08B |
| DEX volume (24h) | $1.88B (-1.02% 1d) |
| App fees (24h, all protocols) | $8.30M |
| Chain fees (24h) | $395.05K |
| Jito MEV tips (24h) | $101.35K |
| **REV - Real Economic Value (24h)** | **$496.41K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.75B | -7.61% |
| USDT | $2.07B | +0.97% |
| USDGO | $984.36M | -7.52% |
| USD1 | $875.20M | -16.29% |
| PYUSD | $722.29M | -7.74% |
| USDG | $444.03M | +0.14% |
| SOFID | $279.06M | +2.95% |
| USDe | $253.05M | -8.84% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $283.30M |
| BisonFi | $206.37M |
| Meteora DLMM | $177.91M |
| PumpSwap | $166.14M |
| Raydium AMM | $159.41M |
| Scorch | $147.30M |
| pump.fun | $89.06M |
| Manifest Trade | $85.10M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.51M |
| pump.fun | $1.12M |
| Jupiter Perpetual Exchange | $1.12M |
| Meteora DLMM | $488.67K |
| Axiom | $396.98K |
| Raydium AMM | $275.19K |
| Sanctum Validator LSTs | $203.66K |
| Orca DEX | $200.27K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $66.13M |
| xStocks holder positions | 947.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $521.61M |

## Program activity and chain health

Chain tip lag: **+1.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 67,702 | 56.70% | 0.9 s |
| Pump.fun | 31,453 | 83.70% | 1.7 s |
| Jupiter v6 | 3,264 | 58.40% | 18.3 s |
| Orca Whirlpools | 2,922 | 45.90% | 20.3 s |
| Raydium AMM v4 | 2,114 | 48.70% | 28.3 s |

Median failure rate across the sampled programs: **56.70%** (range 45.90% to 83.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.36K SOL**.

## Exchange and large-holder balances

9.62M SOL ($678.69M) across 7 publicly-attributed accounts. Net **21K SOL (0.22%) moved off exchanges** over the last 19.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $656.02M | 0.3/h | 2 |
| Bybit | 120.74K | $8.52M | 24/h | 0 |
| Gate.io | 70.80K | $4.99M | 144.5/h | 0 |
| Kraken | 55.11K | $3.89M | 239.2/h | 0 |
| Bitget | 31.28K | $2.21M | 100/h | 0 |
| Coinbase | 21.77K | $1.54M | 267.3/h | 0 |
| Coinbase (2) | 21.68K | $1.53M | 283.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1158 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.257 | 1158 | 0.0000 |
| DEX volume moves with App fees | +0.250 | 1117 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.249 | 1085 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.245 | 1085 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.221 | 1126 | 0.0000 |
| Total TPS moves with Slot time | +0.191 | 1126 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.177 | 1107 | 0.0000 |
| Total TPS moves with Program failure rate | +0.176 | 1107 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.148 | 1085 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.134 | 1085 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 70.54 USD | Jupiter (on-chain DEX): 70.63 USD | -0.13% | agree |
| Circulating supply | getSupply (RPC): 591.96M SOL | CoinGecko: 591.96M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-20
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19

**Recently merged SIMDs:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31

**Latest Agave release:** [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) (2026-11-19)

**Latest Firedancer release:** [v26.11.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.0) (2026-11-11)

## Ecosystem news

- **[Cathie Wood Bets $91M on Anthropic IPO While Paring Crypto Exposure](https://decrypt.co/383737/cathie-wood-bets-91m-anthropic-ipo-paring-crypto-exposure)** - Decrypt, 2026-11-20
- **[Ark buys $90 million worth of Anthropic shares on debut, trims Ethereum and Solana staking ETF holdings](https://www.theblock.co/news/markets/2026-11-20-ark-buys-90-million-worth-of-anthropic-shares-on-debut-trims-ethereum-and-solana-staking-etf-holdings-444226)** - The Block, 2026-11-20
- **[Why CoinShares Just Sold All Its Ethereum and Half Its Solana](https://decrypt.co/383570/why-coinshares-just-sold-all-ethereum-half-solana)** - Decrypt, 2026-11-18
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
