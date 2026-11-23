# Solana Ecosystem Report

*Generated 2026-11-23 15:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.9K |
| TPS (non-vote) | 2.9K |
| Slot time | 213.9 ms |
| Slot | 473M |
| Block height | 451M |
| Epoch | 1094 (89.18% complete, ~2.8h remaining) |
| Lifetime transactions | 568.0B |
| Circulating supply | 592.0M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 22.70% of slots needed a priority fee (max 36.9M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 660 |
| Delinquent validators | 25 |
| Delinquent stake | 0.04% |
| Total active stake | 425.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.45% / 25.00% / 36.04% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.16% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.9M | 3.98% | 0% |
| 2 | `CcaH…oTN1` | 16.3M | 3.84% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.91% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.31% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.26% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.18% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.88% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.59% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $76.59 (+9.04% 24h) |
| Market cap | $45.34B (rank #7) |
| 24h volume | $3.09B |
| ATH | $293.31 (-73.89% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.79B |
| Stablecoin supply | $13.44B |
| DEX volume (24h) | $975.74M (-27.50% 1d) |
| App fees (24h, all protocols) | $5.92M |
| Chain fees (24h) | $287.12K |
| Jito MEV tips (24h) | $82.70K |
| **REV - Real Economic Value (24h)** | **$369.82K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.25B | -3.19% |
| USDT | $1.99B | -0.50% |
| USDGO | $943.10M | -11.39% |
| USD1 | $867.61M | -15.07% |
| PYUSD | $714.58M | -10.90% |
| USDG | $442.98M | +0.23% |
| SOFID | $282.29M | +3.11% |
| USDe | $251.30M | -9.32% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $161.31M |
| Orca DEX | $133.98M |
| BisonFi | $115.02M |
| PumpSwap | $109.84M |
| Scorch | $93.17M |
| pump.fun | $80.56M |
| Meteora DLMM | $72.86M |
| AlphaQ | $46.94M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.10M |
| pump.fun | $955.78K |
| Jupiter Perpetual Exchange | $507.42K |
| Axiom | $300.92K |
| Raydium AMM | $278.14K |
| Meteora DLMM | $208.25K |
| Sanctum Validator LSTs | $207.21K |
| Lunar Lander | $144.85K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $124.88M |
| xStocks holder positions | 957.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $521.91M |

## Program activity and chain health

Chain tip lag: **+0.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 72,931 | 36.10% | 0.6 s |
| Pump.fun | 23,562 | 68.80% | 2.4 s |
| Jupiter v6 | 22,581 | 81.80% | 2.6 s |
| Orca Whirlpools | 15,642 | 48.00% | 3.6 s |
| Raydium AMM v4 | 2,213 | 16.90% | 27 s |

Median failure rate across the sampled programs: **48.00%** (range 16.90% to 81.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.64K SOL**.

## Exchange and large-holder balances

9.63M SOL ($737.41M) across 7 publicly-attributed accounts. Net **4K SOL (0.04%) moved off exchanges** over the last 20.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $712.29M | 0.2/h | 2 |
| Bybit | 120.74K | $9.25M | 73.3/h | 0 |
| Gate.io | 82.72K | $6.34M | 427.6/h | 0 |
| Bitget | 37.52K | $2.87M | 223.9/h | 0 |
| Kraken | 36.82K | $2.82M | 325.2/h | 0 |
| Coinbase (2) | 27.39K | $2.10M | 228.3/h | 0 |
| Coinbase | 22.79K | $1.75M | 266.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1165 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.258 | 1124 | 0.0000 |
| SOL price moves with DeFi TVL | +0.255 | 1165 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.247 | 1092 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.243 | 1092 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.219 | 1133 | 0.0000 |
| Total TPS moves with Slot time | +0.190 | 1133 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.175 | 1114 | 0.0000 |
| Total TPS moves with Program failure rate | +0.174 | 1114 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.150 | 1092 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.133 | 1092 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 76.59 USD | Jupiter (on-chain DEX): 76.31 USD | +0.37% | agree |
| Circulating supply | getSupply (RPC): 592.02M SOL | CoinGecko: 592.02M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-11-17
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-20
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
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

- **[Solana Meme Coin for Fiona the Hippo Raises $100K for Cincinnati Zoo Charity](https://decrypt.co/383762/solana-meme-coin-for-fiona-the-hippo-sends-100k-to-cincinnati-zoo-charity)** - Decrypt, 2026-11-23
- **[Ark buys $146 million in Anthropic shares last week, trims Ethereum and Solana Staking ETF holdings](https://www.theblock.co/news/business/2026-11-23-ark-buys-146-million-worth-anthropic-since-debut-444866)** - The Block, 2026-11-23
- **[Cathie Wood Bets $91M on Anthropic IPO While Paring Crypto Exposure](https://decrypt.co/383737/cathie-wood-bets-91m-anthropic-ipo-paring-crypto-exposure)** - Decrypt, 2026-11-20
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
