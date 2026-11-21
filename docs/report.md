# Solana Ecosystem Report

*Generated 2026-11-21 23:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.8K |
| TPS (non-vote) | 1.8K |
| Slot time | 213.9 ms |
| Slot | 472M |
| Block height | 450M |
| Epoch | 1093 (34.15% complete, ~16.9h remaining) |
| Lifetime transactions | 567.8B |
| Circulating supply | 592.0M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 7.30% of slots needed a priority fee (max 2.0M µlam/CU) |
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
| SOL price | $70.14 (+1.47% 24h) |
| Market cap | $41.52B (rank #7) |
| 24h volume | $3.71B |
| ATH | $293.31 (-76.09% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.63B |
| Stablecoin supply | $13.10B |
| DEX volume (24h) | $1.88B (-1.02% 1d) |
| App fees (24h, all protocols) | $8.30M |
| Chain fees (24h) | $395.05K |
| Jito MEV tips (24h) | $94.62K |
| **REV - Real Economic Value (24h)** | **$489.68K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.80B | -6.95% |
| USDT | $2.04B | -0.49% |
| USDGO | $984.98M | -7.52% |
| USD1 | $875.20M | -16.29% |
| PYUSD | $722.14M | -7.74% |
| USDG | $444.31M | +0.15% |
| SOFID | $279.22M | +2.95% |
| USDe | $253.04M | -8.84% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $209.15M |
| BisonFi | $206.37M |
| Meteora DLMM | $177.91M |
| PumpSwap | $166.14M |
| Scorch | $147.30M |
| Raydium AMM | $143.95M |
| pump.fun | $89.06M |
| ZeroFi | $73.26M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.51M |
| pump.fun | $1.12M |
| Jupiter Perpetual Exchange | $1.12M |
| Meteora DLMM | $488.67K |
| Axiom | $396.98K |
| Raydium AMM | $249.69K |
| Collector Crypt | $234.60K |
| Sanctum Validator LSTs | $203.66K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $44.30M |
| xStocks holder positions | 945.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $521.68M |

## Program activity and chain health

Chain tip lag: **+1.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 89,949 | 53.90% | 0.6 s |
| Pump.fun | 62,366 | 91.90% | 0.6 s |
| Jupiter v6 | 5,576 | 77.20% | 10.7 s |
| Orca Whirlpools | 4,037 | 34.30% | 14.8 s |
| Raydium AMM v4 | 915 | 11.40% | 65.5 s |

Median failure rate across the sampled programs: **53.90%** (range 11.40% to 91.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.39K SOL**.

## Exchange and large-holder balances

9.57M SOL ($671.53M) across 7 publicly-attributed accounts. Net **94K SOL (0.98%) moved off exchanges** over the last 19.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $652.30M | 0.3/h | 2 |
| Bybit | 120.74K | $8.47M | 14/h | 0 |
| Gate.io | 63.83K | $4.48M | 101.7/h | 0 |
| Kraken | 37.02K | $2.60M | 211.3/h | 0 |
| Bitget | 24.42K | $1.71M | 81.8/h | 0 |
| Coinbase (2) | 14.99K | $1.05M | 241.9/h | 0 |
| Coinbase | 13.15K | $922.49K | 228/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1159 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.256 | 1159 | 0.0000 |
| DEX volume moves with App fees | +0.250 | 1118 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.249 | 1086 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.244 | 1086 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.221 | 1127 | 0.0000 |
| Total TPS moves with Slot time | +0.191 | 1127 | 0.0000 |
| Total TPS moves with Program failure rate | +0.177 | 1108 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.177 | 1108 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 1086 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.134 | 1086 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 70.14 USD | Jupiter (on-chain DEX): 70.12 USD | +0.03% | agree |
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
