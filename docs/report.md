# Solana Ecosystem Report

*Generated 2026-11-07 08:58 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Network throughput** (critical): Total TPS at 962, far below normal mainnet levels; possible degradation or an RPC reporting artifact.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 962.2 |
| TPS (non-vote) | 962.2 |
| Slot time | 215.1 ms |
| Slot | 466M |
| Block height | 444M |
| Epoch | 1079 (75.37% complete, ~6.4h remaining) |
| Lifetime transactions | 565.6B |
| Circulating supply | 591.0M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 2.70% of slots needed a priority fee (max 3.3M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 659 |
| Delinquent validators | 37 |
| Delinquent stake | 0.28% |
| Total active stake | 433.7M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.72% / 36.16% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.05% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.00% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.41% | 0% |
| 5 | `Catz…Diqb` | 9.5M | 2.20% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.7M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $90.21 (+0.71% 24h) |
| Market cap | $53.31B (rank #7) |
| 24h volume | $1.87B |
| ATH | $293.31 (-69.24% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.25B |
| Stablecoin supply | $14.52B |
| DEX volume (24h) | $1.86B (-15.59% 1d) |
| App fees (24h, all protocols) | $9.38M |
| Chain fees (24h) | $466.94K |
| Jito MEV tips (24h) | $129.51K |
| **REV - Real Economic Value (24h)** | **$596.46K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.99B | +0.53% |
| USDT | $2.44B | +1.66% |
| USD1 | $1.22B | -11.19% |
| USDGO | $1.12B | -10.91% |
| PYUSD | $731.28M | +4.36% |
| BUIDL | $540.61M | -33.48% |
| USDG | $494.48M | -19.37% |
| USDe | $291.11M | -7.85% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $231.07M |
| Orca DEX | $209.87M |
| Tessera V | $197.03M |
| Meteora DLMM | $172.58M |
| Scorch | $147.40M |
| Raydium AMM | $139.41M |
| pump.fun | $108.30M |
| PumpSwap | $90.88M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.94M |
| pump.fun | $1.39M |
| Axiom | $532.49K |
| Meteora DLMM | $510.02K |
| Jupiter Perpetual Exchange | $481.93K |
| Raydium AMM | $276.92K |
| Lunar Lander | $251.37K |
| Sanctum Validator LSTs | $249.01K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $64.01M |
| xStocks holder positions | 888.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $581.63M |

## Program activity and chain health

Chain tip lag: **+1.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 22,269 | 19.90% | 2.6 s |
| Pump.fun | 7,476 | 75.00% | 7.5 s |
| Jupiter v6 | 1,842 | 41.40% | 32.5 s |
| Orca Whirlpools | 648 | 26.90% | 92.3 s |
| Raydium AMM v4 | 465 | 27.50% | 128.6 s |

Median failure rate across the sampled programs: **27.50%** (range 19.90% to 75.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.33K SOL**.

## Exchange and large-holder balances

9.60M SOL ($866.14M) across 7 publicly-attributed accounts. Net **8K SOL (0.09%) moved onto exchanges** over the last 22.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $838.95M | 0.2/h | 3 |
| Gate.io | 106.10K | $9.57M | 128.9/h | 0 |
| Bybit | 97.32K | $8.78M | 42.6/h | 0 |
| Kraken | 32.59K | $2.94M | 197/h | 0 |
| Coinbase | 23.63K | $2.13M | 144.7/h | 0 |
| Coinbase (2) | 21.66K | $1.95M | 140.1/h | 0 |
| Bitget | 20.09K | $1.81M | 160/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1107 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.256 | 1066 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.231 | 1034 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 1075 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.227 | 1034 | 0.0000 |
| SOL price moves with DeFi TVL | +0.225 | 1107 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1075 | 0.0000 |
| Total TPS moves with Program failure rate | +0.168 | 1056 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.168 | 1056 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 1034 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.123 | 1034 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 90.21 USD | Jupiter (on-chain DEX): 90.22 USD | -0.01% | agree |
| Circulating supply | getSupply (RPC): 590.98M SOL | CoinGecko: 590.98M SOL | -0.00% | agree |

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
