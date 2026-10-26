# Solana Ecosystem Report

*Generated 2026-10-26 19:38 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.3K |
| TPS (non-vote) | 2.3K |
| Slot time | 212.4 ms |
| Slot | 462M |
| Block height | 440M |
| Epoch | 1068 (94.77% complete, ~1.3h remaining) |
| Lifetime transactions | 563.9B |
| Circulating supply | 589.8M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 18.70% of slots needed a priority fee (max 1.2M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 664 |
| Delinquent validators | 26 |
| Delinquent stake | 0.14% |
| Total active stake | 437.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.31% / 24.58% / 35.79% |
| Commission (stake-weighted, delegatable validators) | 3.75% |
| Stake on private (100% commission) validators | 23.92% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.6M | 3.81% | 0% |
| 3 | `3N7s…iD5g` | 12.6M | 2.88% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.49% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.22% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.17% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $100.40 (-1.26% 24h) |
| Market cap | $59.22B (rank #7) |
| 24h volume | $2.45B |
| ATH | $293.31 (-65.77% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.73B |
| Stablecoin supply | $15.58B |
| DEX volume (24h) | $1.45B (+1.84% 1d) |
| App fees (24h, all protocols) | $9.29M |
| Chain fees (24h) | $434.09K |
| Jito MEV tips (24h) | $134.18K |
| **REV - Real Economic Value (24h)** | **$568.27K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.79B | -0.08% |
| USDT | $2.81B | +4.45% |
| USD1 | $1.39B | -0.21% |
| USDGO | $1.29B | +1.97% |
| BUIDL | $886.66M | +0.12% |
| PYUSD | $688.52M | +1.87% |
| USDG | $624.10M | -0.02% |
| USDe | $317.34M | -21.81% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $310.94M |
| Manifest Trade | $235.81M |
| Orca DEX | $227.59M |
| BisonFi | $184.76M |
| Raydium AMM | $142.61M |
| Tessera V | $107.22M |
| pump.fun | $101.11M |
| Meteora DLMM | $67.38M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.48M |
| pump.fun | $1.40M |
| Collector Crypt | $1.18M |
| Axiom | $545.10K |
| Meteora DLMM | $350.68K |
| Sanctum Validator LSTs | $274.49K |
| StonkFun | $272.76K |
| Raydium AMM | $261.53K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $53.61M |
| xStocks holder positions | 851.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $593.61M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 106,497 (approx.) | 62.80% | 0.4 s |
| Pump.fun | 47,966 | 86.60% | 1.1 s |
| Jupiter v6 | 6,152 | 58.30% | 9.6 s |
| Orca Whirlpools | 2,154 | 30.20% | 27.8 s |
| Raydium AMM v4 | 932 | 35.90% | 64.1 s |

Median failure rate across the sampled programs: **58.30%** (range 30.20% to 86.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **119.19 SOL**.

## Exchange and large-holder balances

13.19M SOL ($1.32B) across 8 publicly-attributed accounts. Net **343K SOL (2.53%) moved off exchanges** over the last 22.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.12B | 0.2/h | 4 |
| Binance (2) | 1.15M | $115.28M | 1.0K/h | 0 |
| Gate.io | 355.56K | $35.70M | 107.5/h | 0 |
| Bybit | 330.87K | $33.22M | 25.6/h | 0 |
| Bitget | 107.03K | $10.75M | 131/h | 0 |
| Kraken | 36.63K | $3.68M | 305.3/h | 0 |
| Coinbase (2) | 17.34K | $1.74M | 262.6/h | 0 |
| Coinbase | 13.62K | $1.37M | 274.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1059 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.247 | 1018 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 1025 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.216 | 984 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.211 | 984 | 0.0000 |
| SOL price moves with DeFi TVL | +0.208 | 1059 | 0.0000 |
| Total TPS moves with Slot time | +0.196 | 1025 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.160 | 1006 | 0.0000 |
| Total TPS moves with Program failure rate | +0.159 | 1006 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.154 | 984 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.112 | 984 | 0.0004 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 100.40 USD | Jupiter (on-chain DEX): 100.32 USD | +0.08% | agree |
| Circulating supply | getSupply (RPC): 589.82M SOL | CoinGecko: 589.82M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-26
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-26

**Recently merged SIMDs:**

- [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-26
- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-24
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-23
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-23
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-21
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.4) (2026-10-21)

## Ecosystem news

- **[Bitcoin ETFs Bleed $636 Million as October Turns Red Again](https://decrypt.co/381700/bitcoin-etfs-bleed-october-turns-red-again)** - Decrypt, 2026-10-23
- **[Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026)** - Solana.com, 2026-10-23
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026)** - Solana.com, 2026-10-16
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
