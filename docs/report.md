# Solana Ecosystem Report

*Generated 2026-11-20 22:51 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 4.4 robust standard deviations below its 7-day baseline: a 7.8% move to 12,806,969,433.00 USD from a typical 13,894,332,170.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 214.7 ms |
| Slot | 472M |
| Block height | 450M |
| Epoch | 1092 (38.66% complete, ~15.8h remaining) |
| Lifetime transactions | 567.7B |
| Circulating supply | 591.9M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 23 |
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
| SOL price | $68.90 (-5.79% 24h) |
| Market cap | $40.78B (rank #7) |
| 24h volume | $3.56B |
| ATH | $293.31 (-76.51% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.56B |
| Stablecoin supply | $12.81B |
| DEX volume (24h) | $1.90B (+4.89% 1d) |
| App fees (24h, all protocols) | $9.31M |
| Chain fees (24h) | $469.96K |
| Jito MEV tips (24h) | $118.92K |
| **REV - Real Economic Value (24h)** | **$588.88K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.46B | -11.08% |
| USDT | $2.07B | -3.71% |
| USDGO | $984.90M | -8.80% |
| USD1 | $889.91M | -17.25% |
| PYUSD | $720.78M | -9.17% |
| USDG | $441.90M | -6.04% |
| SOFID | $275.83M | +0.68% |
| USDe | $253.03M | -9.44% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $283.44M |
| Meteora DLMM | $237.03M |
| PumpSwap | $207.82M |
| Raydium AMM | $192.05M |
| BisonFi | $179.10M |
| Scorch | $108.88M |
| Manifest Trade | $104.15M |
| pump.fun | $95.60M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.27M |
| pump.fun | $1.26M |
| Meteora DLMM | $885.94K |
| Axiom | $579.50K |
| Raydium AMM | $348.19K |
| Jupiter Perpetual Exchange | $304.28K |
| fomo Wallet | $229.00K |
| Sanctum Validator LSTs | $213.77K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $104.36M |
| xStocks holder positions | 946.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $529.07M |

## Program activity and chain health

Chain tip lag: **+1.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 50,973 | 51.20% | 1.1 s |
| Pump.fun | 29,840 | 74.80% | 1.9 s |
| Orca Whirlpools | 4,125 | 52.80% | 14.4 s |
| Jupiter v6 | 2,139 | 39.70% | 27.9 s |
| Raydium AMM v4 | 678 | 12.30% | 87.8 s |

Median failure rate across the sampled programs: **51.20%** (range 12.30% to 74.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.20K SOL**.

## Exchange and large-holder balances

9.64M SOL ($664.39M) across 7 publicly-attributed accounts. Net **19K SOL (0.20%) moved off exchanges** over the last 21.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $640.77M | 0.3/h | 2 |
| Bybit | 133.49K | $9.20M | 37.5/h | 0 |
| Gate.io | 80.92K | $5.58M | 126.2/h | 0 |
| Coinbase | 40.60K | $2.80M | 358.9/h | 0 |
| Bitget | 33.50K | $2.31M | 2.0K/h | 0 |
| Coinbase (2) | 29.37K | $2.02M | 322.9/h | 0 |
| Kraken | 24.96K | $1.72M | 182.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1155 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.260 | 1155 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.251 | 1082 | 0.0000 |
| DEX volume moves with App fees | +0.250 | 1114 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.247 | 1082 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 1123 | 0.0000 |
| Total TPS moves with Slot time | +0.192 | 1123 | 0.0000 |
| Total TPS moves with Program failure rate | +0.182 | 1104 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.182 | 1104 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.148 | 1082 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.134 | 1082 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 68.90 USD | Jupiter (on-chain DEX): 68.94 USD | -0.06% | agree |
| Circulating supply | getSupply (RPC): 591.91M SOL | CoinGecko: 591.91M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
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
