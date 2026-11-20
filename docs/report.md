# Solana Ecosystem Report

*Generated 2026-11-20 16:46 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 5.9 robust standard deviations below its 7-day baseline: a 6.9% move to 12,966,259,627.00 USD from a typical 13,926,264,631.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.4K |
| TPS (non-vote) | 2.4K |
| Slot time | 216.6 ms |
| Slot | 472M |
| Block height | 450M |
| Epoch | 1092 (15.15% complete, ~22.1h remaining) |
| Lifetime transactions | 567.6B |
| Circulating supply | 591.9M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 19.30% of slots needed a priority fee (max 6.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 24 |
| Delinquent stake | 0.02% |
| Total active stake | 428.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.37% / 24.82% / 35.97% |
| Commission (stake-weighted, delegatable validators) | 3.86% |
| Stake on private (100% commission) validators | 22.98% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.81% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.90% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.40% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.28% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.23% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.86% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.58% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $69.29 (-6.02% 24h) |
| Market cap | $41.02B (rank #7) |
| 24h volume | $3.09B |
| ATH | $293.31 (-76.38% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.65B |
| Stablecoin supply | $12.97B |
| DEX volume (24h) | $1.90B (+4.89% 1d) |
| App fees (24h, all protocols) | $9.31M |
| Chain fees (24h) | $469.96K |
| Jito MEV tips (24h) | $122.12K |
| **REV - Real Economic Value (24h)** | **$592.08K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.59B | -9.24% |
| USDT | $2.07B | -3.71% |
| USDGO | $984.03M | -8.80% |
| USD1 | $896.76M | -16.73% |
| PYUSD | $720.42M | -9.24% |
| USDG | $451.88M | -3.92% |
| SOFID | $276.09M | +0.68% |
| USDe | $252.08M | -9.89% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $271.83M |
| Meteora DLMM | $237.03M |
| PumpSwap | $207.82M |
| BisonFi | $179.10M |
| Raydium AMM | $157.06M |
| Manifest Trade | $118.68M |
| Scorch | $108.88M |
| pump.fun | $95.60M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.27M |
| pump.fun | $1.26M |
| Meteora DLMM | $885.94K |
| Axiom | $579.50K |
| Jupiter Perpetual Exchange | $304.28K |
| Raydium AMM | $267.49K |
| Orca DEX | $230.46K |
| fomo Wallet | $229.00K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $103.58M |
| xStocks holder positions | 944.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $570.98M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 81,256 | 55.00% | 0.6 s |
| Pump.fun | 39,520 | 82.40% | 1.3 s |
| Orca Whirlpools | 9,428 | 56.70% | 6.3 s |
| Jupiter v6 | 7,664 | 62.00% | 7.8 s |
| Raydium AMM v4 | 1,690 | 33.30% | 34.7 s |

Median failure rate across the sampled programs: **56.70%** (range 33.30% to 82.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.14K SOL**.

## Exchange and large-holder balances

9.65M SOL ($668.57M) across 7 publicly-attributed accounts. Net **55K SOL (0.56%) moved off exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $644.40M | 0.3/h | 2 |
| Bybit | 133.49K | $9.25M | 69.9/h | 0 |
| Gate.io | 78.79K | $5.46M | 267.3/h | 0 |
| Coinbase | 53.03K | $3.67M | 370/h | 0 |
| Kraken | 34.73K | $2.41M | 330.6/h | 0 |
| Bitget | 32.61K | $2.26M | 4.7K/h | 0 |
| Coinbase (2) | 16.16K | $1.12M | 293.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1154 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.259 | 1154 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.250 | 1081 | 0.0000 |
| DEX volume moves with App fees | +0.250 | 1113 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.246 | 1081 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.221 | 1122 | 0.0000 |
| Total TPS moves with Slot time | +0.191 | 1122 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.182 | 1103 | 0.0000 |
| Total TPS moves with Program failure rate | +0.181 | 1103 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.148 | 1081 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.133 | 1081 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 69.29 USD | Jupiter (on-chain DEX): 69.25 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 591.91M SOL | CoinGecko: 591.91M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
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

- **[Ark buys $90 million worth of Anthropic shares on debut, trims Ethereum and Solana staking ETF holdings](https://www.theblock.co/news/markets/2026-11-20-ark-buys-90-million-worth-of-anthropic-shares-on-debut-trims-ethereum-and-solana-staking-etf-holdings-444226)** - The Block, 2026-11-20
- **[Why CoinShares Just Sold All Its Ethereum and Half Its Solana](https://decrypt.co/383570/why-coinshares-just-sold-all-ethereum-half-solana)** - Decrypt, 2026-11-18
- **[AI Will Make the Next 12 Months 'a Slaughterhouse' for Crypto Security: Anchorage Exec](https://decrypt.co/383526/ai-will-make-the-next-12-months-a-slaughterhouse-for-crypto-security-anchorage-exec)** - Decrypt, 2026-11-18
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
