# Solana Ecosystem Report

*Generated 2026-11-20 08:00 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 6.0 robust standard deviations below its 7-day baseline: a 6.6% move to 13,015,492,116.00 USD from a typical 13,938,030,622.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 214.3 ms |
| Slot | 472M |
| Block height | 450M |
| Epoch | 1091 (81.11% complete, ~4.9h remaining) |
| Lifetime transactions | 567.6B |
| Circulating supply | 591.9M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 8.00% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 659 |
| Delinquent validators | 26 |
| Delinquent stake | 0.03% |
| Total active stake | 428.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.85% / 36.01% |
| Commission (stake-weighted, delegatable validators) | 3.86% |
| Stake on private (100% commission) validators | 23.01% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.82% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.90% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.40% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.29% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.23% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.86% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.58% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $72.58 (-3.11% 24h) |
| Market cap | $42.95B (rank #7) |
| 24h volume | $2.54B |
| ATH | $293.31 (-75.26% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.72B |
| Stablecoin supply | $13.02B |
| DEX volume (24h) | $1.85B (+1.76% 1d) |
| App fees (24h, all protocols) | $9.57M |
| Chain fees (24h) | $469.96K |
| Jito MEV tips (24h) | $122.10K |
| **REV - Real Economic Value (24h)** | **$592.06K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.62B | -8.89% |
| USDT | $2.07B | -3.71% |
| USDGO | $998.94M | -7.41% |
| USD1 | $902.81M | -16.16% |
| PYUSD | $708.73M | -10.72% |
| USDG | $451.70M | -4.00% |
| SOFID | $276.01M | +0.68% |
| USDe | $265.28M | -5.17% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $253.17M |
| Meteora DLMM | $246.17M |
| PumpSwap | $207.82M |
| BisonFi | $153.98M |
| Raydium AMM | $149.09M |
| pump.fun | $127.79M |
| Manifest Trade | $126.96M |
| Scorch | $79.90M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.27M |
| pump.fun | $1.26M |
| Meteora DLMM | $927.79K |
| Axiom | $817.38K |
| Jupiter Perpetual Exchange | $304.28K |
| Raydium AMM | $276.35K |
| fomo Wallet | $265.92K |
| Lunar Lander | $227.41K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $94.69M |
| xStocks holder positions | 944.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $571.57M |

## Program activity and chain health

Chain tip lag: **+0.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 29,647 | 33.70% | 1.9 s |
| Pump.fun | 7,114 | 53.60% | 8.4 s |
| Orca Whirlpools | 3,040 | 35.10% | 19.7 s |
| Jupiter v6 | 2,915 | 61.50% | 20.4 s |
| Raydium AMM v4 | 465 | 14.80% | 129 s |

Median failure rate across the sampled programs: **35.10%** (range 14.80% to 61.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.03K SOL**.

## Exchange and large-holder balances

9.70M SOL ($704.24M) across 7 publicly-attributed accounts. Net **10K SOL (0.10%) moved off exchanges** over the last 22.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $674.99M | 0.3/h | 2 |
| Bybit | 133.49K | $9.69M | 19.3/h | 0 |
| Gate.io | 73.82K | $5.36M | 140/h | 0 |
| Coinbase | 69.63K | $5.05M | 168.3/h | 0 |
| Bitget | 69.54K | $5.05M | 8.0K/h | 0 |
| Kraken | 37.14K | $2.70M | 143.3/h | 0 |
| Coinbase (2) | 19.28K | $1.40M | 178.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1153 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.257 | 1153 | 0.0000 |
| DEX volume moves with App fees | +0.253 | 1112 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.248 | 1080 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.244 | 1080 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.220 | 1121 | 0.0000 |
| Total TPS moves with Slot time | +0.190 | 1121 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.180 | 1102 | 0.0000 |
| Total TPS moves with Program failure rate | +0.179 | 1102 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 1080 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.132 | 1080 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 72.58 USD | Jupiter (on-chain DEX): 72.54 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 591.85M SOL | CoinGecko: 591.85M SOL | -0.00% | agree |

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

- **[Why CoinShares Just Sold All Its Ethereum and Half Its Solana](https://decrypt.co/383570/why-coinshares-just-sold-all-ethereum-half-solana)** - Decrypt, 2026-11-18
- **[AI Will Make the Next 12 Months 'a Slaughterhouse' for Crypto Security: Anchorage Exec](https://decrypt.co/383526/ai-will-make-the-next-12-months-a-slaughterhouse-for-crypto-security-anchorage-exec)** - Decrypt, 2026-11-18
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
