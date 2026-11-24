# Solana Ecosystem Report

*Generated 2026-11-24 22:49 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.8K |
| TPS (non-vote) | 1.8K |
| Slot time | 213.5 ms |
| Slot | 474M |
| Block height | 452M |
| Epoch | 1096 (10.61% complete, ~22.9h remaining) |
| Lifetime transactions | 568.2B |
| Circulating supply | 592.1M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 22.00% of slots needed a priority fee (max 3.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 660 |
| Delinquent validators | 27 |
| Delinquent stake | 0.02% |
| Total active stake | 424.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 25.00% / 36.13% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.20% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 4.00% | 0% |
| 2 | `CcaH…oTN1` | 16.0M | 3.76% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.92% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.9M | 2.33% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.26% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.19% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.89% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.60% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $69.89 (-2.50% 24h) |
| Market cap | $41.38B (rank #7) |
| 24h volume | $2.46B |
| ATH | $293.31 (-76.17% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.54B |
| Stablecoin supply | $13.22B |
| DEX volume (24h) | $1.81B (+85.09% 1d) |
| App fees (24h, all protocols) | $8.46M |
| Chain fees (24h) | $424.09K |
| Jito MEV tips (24h) | $106.94K |
| **REV - Real Economic Value (24h)** | **$531.03K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.18B | -6.45% |
| USDT | $1.86B | -6.73% |
| USDGO | $922.93M | -10.67% |
| USD1 | $867.97M | -11.32% |
| PYUSD | $713.55M | +2.99% |
| USDG | $434.52M | -0.92% |
| SOFID | $277.14M | +1.28% |
| USDe | $242.33M | -12.35% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $216.91M |
| BisonFi | $204.07M |
| Meteora DLMM | $166.92M |
| Scorch | $159.21M |
| Raydium AMM | $153.39M |
| Manifest Trade | $121.31M |
| pump.fun | $107.91M |
| PumpSwap | $99.47M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.43M |
| pump.fun | $1.40M |
| Jupiter Perpetual Exchange | $568.69K |
| Axiom | $431.18K |
| Meteora DLMM | $403.77K |
| Collector Crypt | $319.00K |
| Raydium AMM | $223.90K |
| Sanctum Validator LSTs | $209.74K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $88.76M |
| xStocks holder positions | 967.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $541.87M |

## Program activity and chain health

Chain tip lag: **+1.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,335 | 63.20% | 0.9 s |
| Pump.fun | 37,497 | 81.30% | 1.5 s |
| Orca Whirlpools | 4,598 | 9.80% | 13 s |
| Jupiter v6 | 4,447 | 75.40% | 13.5 s |
| Raydium AMM v4 | 795 | 5.50% | 75.4 s |

Median failure rate across the sampled programs: **63.20%** (range 5.50% to 81.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **906.10 SOL**.

## Exchange and large-holder balances

9.67M SOL ($675.90M) across 7 publicly-attributed accounts. Net **67K SOL (0.70%) moved onto exchanges** over the last 20.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $649.98M | 0.2/h | 3 |
| Gate.io | 100.16K | $7.00M | 74.1/h | 0 |
| Bybit | 88.91K | $6.21M | 45.1/h | 0 |
| Coinbase (2) | 73.43K | $5.13M | 292.7/h | 0 |
| Kraken | 51.21K | $3.58M | 440.6/h | 0 |
| Coinbase | 34.80K | $2.43M | 292/h | 0 |
| Bitget | 22.42K | $1.57M | 85.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1168 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.263 | 1127 | 0.0000 |
| SOL price moves with DeFi TVL | +0.260 | 1168 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.248 | 1095 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.244 | 1095 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.216 | 1136 | 0.0000 |
| Total TPS moves with Slot time | +0.186 | 1136 | 0.0000 |
| Total TPS moves with Program failure rate | +0.178 | 1117 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.178 | 1117 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.148 | 1095 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.135 | 1095 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 69.89 USD | Jupiter (on-chain DEX): 69.86 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 592.13M SOL | CoinGecko: 592.13M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-11-17
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20

**Recently merged SIMDs:**

- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-23
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01

**Latest Agave release:** [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) (2026-11-19)

**Latest Firedancer release:** [v26.11.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.0) (2026-11-11)

## Ecosystem news

- **[Tom Lee Says Ethereum Is as Scarce as Bitcoin—And Bitmine Just Bought More](https://decrypt.co/383800/tom-lee-ethereum-scarce-bitcoin-bitmine-buys-more)** - Decrypt, 2026-11-23
- **[Solana Meme Coin for Fiona the Hippo Raises $100K for Cincinnati Zoo Charity](https://decrypt.co/383762/solana-meme-coin-for-fiona-the-hippo-sends-100k-to-cincinnati-zoo-charity)** - Decrypt, 2026-11-23
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
