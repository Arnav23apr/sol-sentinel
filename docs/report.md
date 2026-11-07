# Solana Ecosystem Report

*Generated 2026-11-07 19:30 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.9K |
| TPS (non-vote) | 1.9K |
| Slot time | 214.7 ms |
| Slot | 467M |
| Block height | 445M |
| Epoch | 1080 (16.29% complete, ~21.6h remaining) |
| Lifetime transactions | 565.7B |
| Circulating supply | 591.0M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 10.70% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 663 |
| Delinquent validators | 34 |
| Delinquent stake | 0.15% |
| Total active stake | 434.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.35% / 24.67% / 36.11% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.02% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.85% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.00% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.37% | 0% |
| 5 | `Catz…Diqb` | 9.6M | 2.20% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.19% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $89.60 (-0.41% 24h) |
| Market cap | $52.96B (rank #7) |
| 24h volume | $948.77M |
| ATH | $293.31 (-69.45% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.23B |
| Stablecoin supply | $14.66B |
| DEX volume (24h) | $1.48B (-32.68% 1d) |
| App fees (24h, all protocols) | $9.27M |
| Chain fees (24h) | $466.94K |
| Jito MEV tips (24h) | $111.47K |
| **REV - Real Economic Value (24h)** | **$578.41K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.07B | +1.62% |
| USDT | $2.44B | +1.66% |
| USD1 | $1.22B | -11.19% |
| USDGO | $1.12B | -10.91% |
| PYUSD | $731.59M | +4.36% |
| BUIDL | $540.61M | -33.48% |
| USDG | $493.82M | -19.47% |
| USDe | $291.00M | -7.85% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $170.16M |
| Tessera V | $153.42M |
| Meteora DLMM | $128.65M |
| pump.fun | $108.28M |
| Orca DEX | $100.58M |
| Raydium AMM | $94.12M |
| PumpSwap | $90.88M |
| Scorch | $73.26M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.94M |
| pump.fun | $1.39M |
| Axiom | $532.49K |
| Jupiter Perpetual Exchange | $481.93K |
| Meteora DLMM | $439.30K |
| Sanctum Validator LSTs | $249.01K |
| Lunar Lander | $244.35K |
| Raydium AMM | $198.59K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $30.87M |
| xStocks holder positions | 890.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $581.61M |

## Program activity and chain health

Chain tip lag: **+1.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,947 | 46.90% | 0.6 s |
| Pump.fun | 38,891 | 89.00% | 1.3 s |
| Jupiter v6 | 4,994 | 52.60% | 11.6 s |
| Orca Whirlpools | 4,620 | 51.30% | 12.9 s |
| Raydium AMM v4 | 1,485 | 24.50% | 40.4 s |

Median failure rate across the sampled programs: **51.30%** (range 24.50% to 89.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.70K SOL**.

## Exchange and large-holder balances

9.59M SOL ($859.65M) across 7 publicly-attributed accounts. Net **2K SOL (0.02%) moved off exchanges** over the last 21.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $833.28M | 0.3/h | 5 |
| Gate.io | 102.46K | $9.18M | 144.6/h | 0 |
| Bybit | 97.32K | $8.72M | 64/h | 0 |
| Kraken | 29.89K | $2.68M | 219.5/h | 0 |
| Coinbase (2) | 22.12K | $1.98M | 283/h | 0 |
| Bitget | 21.28K | $1.91M | 118.2/h | 0 |
| Coinbase | 21.27K | $1.91M | 516.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1109 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.259 | 1068 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.232 | 1036 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 1077 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.227 | 1036 | 0.0000 |
| SOL price moves with DeFi TVL | +0.227 | 1109 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1077 | 0.0000 |
| Total TPS moves with Program failure rate | +0.170 | 1058 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.170 | 1058 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 1036 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.124 | 1036 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 89.60 USD | Jupiter (on-chain DEX): 89.57 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 591.04M SOL | CoinGecko: 591.04M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-06

**Open SIMD proposals:**

- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-06
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

**Recently merged SIMDs:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-06
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31

**Latest Agave release:** [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06)

**Latest Firedancer release:** [v26.10.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.6) (2026-11-05)

## Ecosystem news

- **[Solana Labs’ Leap Launches Mobile App for Trading Tokenized Stocks and Crypto](https://decrypt.co/382609/solana-labs-leap-launches-mobile-app-tokenized-stocks-crypto)** - Decrypt, 2026-11-05
- **[Stablecoins Go Mainstream as Samsung Wallet Adds USDC on Solana](https://decrypt.co/382586/stablecoins-samsung-wallet-adds-usdc-solana)** - Decrypt, 2026-11-05
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
