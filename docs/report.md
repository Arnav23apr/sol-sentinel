# Solana Ecosystem Report

*Generated 2026-10-25 23:23 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.9K |
| TPS (non-vote) | 1.9K |
| Slot time | 212 ms |
| Slot | 461M |
| Block height | 439M |
| Epoch | 1068 (15.36% complete, ~21.5h remaining) |
| Lifetime transactions | 563.7B |
| Circulating supply | 589.8M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 665 |
| Delinquent validators | 25 |
| Delinquent stake | 0.12% |
| Total active stake | 437.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.31% / 24.57% / 35.78% |
| Commission (stake-weighted, delegatable validators) | 3.75% |
| Stake on private (100% commission) validators | 23.90% |

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
| SOL price | $101.45 (-0.05% 24h) |
| Market cap | $59.82B (rank #7) |
| 24h volume | $1.45B |
| ATH | $293.31 (-65.41% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.76B |
| Stablecoin supply | $15.62B |
| DEX volume (24h) | $1.42B (-28.74% 1d) |
| App fees (24h, all protocols) | $10.05M |
| Chain fees (24h) | $477.32K |
| Jito MEV tips (24h) | $102.59K |
| **REV - Real Economic Value (24h)** | **$579.92K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.72B | -2.36% |
| USDT | $2.86B | +7.51% |
| USD1 | $1.40B | -0.00% |
| USDGO | $1.30B | +2.60% |
| BUIDL | $886.39M | +0.09% |
| PYUSD | $701.62M | +3.80% |
| USDG | $622.81M | -0.28% |
| USDe | $318.47M | -21.95% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $219.28M |
| Manifest Trade | $137.39M |
| Tessera V | $135.53M |
| Orca DEX | $123.01M |
| pump.fun | $119.13M |
| PumpSwap | $112.73M |
| Raydium AMM | $95.85M |
| Meteora DLMM | $84.64M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.95M |
| pump.fun | $1.58M |
| Collector Crypt | $749.50K |
| Axiom | $525.60K |
| Meteora DLMM | $339.81K |
| pump.fun Mobile App | $317.57K |
| Jupiter Perpetual Exchange | $298.66K |
| Sanctum Validator LSTs | $280.25K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $31.34M |
| xStocks holder positions | 848.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $593.80M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 68,703 | 49.70% | 0.8 s |
| Pump.fun | 13,656 | 79.90% | 4.2 s |
| Jupiter v6 | 3,407 | 42.70% | 17.2 s |
| Raydium AMM v4 | 896 | 17.10% | 66.6 s |
| Orca Whirlpools | 821 | 43.50% | 70 s |

Median failure rate across the sampled programs: **43.50%** (range 17.10% to 79.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **521.86 SOL**.

## Exchange and large-holder balances

13.50M SOL ($1.37B) across 8 publicly-attributed accounts. Net **43K SOL (0.32%) moved off exchanges** over the last 24.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.13B | 0.2/h | 4 |
| Binance (2) | 1.50M | $151.99M | 1.1K/h | 0 |
| Bybit | 330.96K | $33.58M | 17.5/h | 0 |
| Gate.io | 326.94K | $33.17M | 94.6/h | 0 |
| Bitget | 99.53K | $10.10M | 121/h | 0 |
| Kraken | 38.49K | $3.90M | 201.3/h | 0 |
| Coinbase (2) | 13.45K | $1.36M | 245.7/h | 0 |
| Coinbase | 12.63K | $1.28M | 225/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1055 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.259 | 1014 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 1021 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.211 | 980 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.206 | 980 | 0.0000 |
| SOL price moves with DeFi TVL | +0.203 | 1055 | 0.0000 |
| Total TPS moves with Slot time | +0.195 | 1021 | 0.0000 |
| Total TPS moves with Program failure rate | +0.159 | 1002 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.159 | 1002 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.154 | 980 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.112 | 980 | 0.0005 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 101.45 USD | Jupiter (on-chain DEX): 101.40 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 589.82M SOL | CoinGecko: 589.82M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-24
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23

**Recently merged SIMDs:**

- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-10-24
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-23
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-23
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-21
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-10-20

**Latest Agave release:** [v4.4.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-rc.0) (2026-10-24)

**Latest Firedancer release:** [v26.10.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.4) (2026-10-21)

## Ecosystem news

- **[Bitcoin ETFs Bleed $636 Million as October Turns Red Again](https://decrypt.co/381700/bitcoin-etfs-bleed-october-turns-red-again)** - Decrypt, 2026-10-23
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026)** - Solana.com, 2026-10-16
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
