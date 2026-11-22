# Solana Ecosystem Report

*Generated 2026-11-22 03:22 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.4K |
| TPS (non-vote) | 1.4K |
| Slot time | 216.6 ms |
| Slot | 472M |
| Block height | 450M |
| Epoch | 1093 (49.17% complete, ~13.2h remaining) |
| Lifetime transactions | 567.8B |
| Circulating supply | 592.0M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 4.00% of slots needed a priority fee (max 231.2K µlam/CU) |
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
| Commission (stake-weighted, delegatable validators) | 3.86% |
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
| SOL price | $69.32 (+2.19% 24h) |
| Market cap | $41.03B (rank #7) |
| 24h volume | $3.44B |
| ATH | $293.31 (-76.37% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.62B |
| Stablecoin supply | $13.13B |
| DEX volume (24h) | $1.56B (-17.20% 1d) |
| App fees (24h, all protocols) | $7.89M |
| Chain fees (24h) | $317.05K |
| Jito MEV tips (24h) | $94.97K |
| **REV - Real Economic Value (24h)** | **$412.02K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.83B | -7.10% |
| USDT | $2.04B | +2.00% |
| USDGO | $984.83M | -7.52% |
| USD1 | $875.59M | -15.04% |
| PYUSD | $722.08M | -10.08% |
| USDG | $444.30M | -0.20% |
| SOFID | $279.17M | +2.02% |
| USDe | $253.00M | -8.53% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $206.37M |
| Orca DEX | $193.29M |
| Meteora DLMM | $177.91M |
| Scorch | $147.30M |
| Raydium AMM | $129.41M |
| PumpSwap | $124.04M |
| pump.fun | $89.06M |
| ZeroFi | $73.26M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| Jupiter Perpetual Exchange | $1.51M |
| PumpSwap | $1.30M |
| pump.fun | $1.03M |
| Meteora DLMM | $488.67K |
| Axiom | $396.98K |
| Raydium AMM | $233.07K |
| Sanctum Validator LSTs | $203.39K |
| Collector Crypt | $173.53K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $40.95M |
| xStocks holder positions | 946.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $521.23M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 26,648 | 32.10% | 2.2 s |
| Pump.fun | 8,457 | 66.80% | 6.9 s |
| Jupiter v6 | 5,908 | 77.60% | 10 s |
| Orca Whirlpools | 5,591 | 86.70% | 10.6 s |
| Raydium AMM v4 | 715 | 12.90% | 83.6 s |

Median failure rate across the sampled programs: **66.80%** (range 12.90% to 86.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.41K SOL**.

## Exchange and large-holder balances

9.70M SOL ($672.48M) across 7 publicly-attributed accounts. Net **32K SOL (0.34%) moved onto exchanges** over the last 23.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $644.68M | 0.3/h | 2 |
| Coinbase | 138.27K | $9.58M | 200.4/h | 0 |
| Bybit | 120.74K | $8.37M | 19.7/h | 0 |
| Gate.io | 65.14K | $4.52M | 100.9/h | 0 |
| Kraken | 35.51K | $2.46M | 141.2/h | 0 |
| Bitget | 27.35K | $1.90M | 68.6/h | 0 |
| Coinbase (2) | 14.04K | $973.34K | 274.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1160 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.257 | 1160 | 0.0000 |
| DEX volume moves with App fees | +0.252 | 1119 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.249 | 1087 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.245 | 1087 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.220 | 1128 | 0.0000 |
| Total TPS moves with Slot time | +0.190 | 1128 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.176 | 1109 | 0.0000 |
| Total TPS moves with Program failure rate | +0.175 | 1109 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 1087 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.133 | 1087 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 69.32 USD | Jupiter (on-chain DEX): 69.41 USD | -0.13% | agree |
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
