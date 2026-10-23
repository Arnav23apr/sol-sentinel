# Solana Ecosystem Report

*Generated 2026-10-23 23:37 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 6.7 robust standard deviations above its 7-day baseline: a 1000.0% move to 0.07 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.7K |
| TPS (non-vote) | 1.7K |
| Slot time | 210.5 ms |
| Slot | 461M |
| Block height | 439M |
| Epoch | 1066 (27.89% complete, ~18.2h remaining) |
| Lifetime transactions | 563.5B |
| Circulating supply | 589.7M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 35.30% of slots needed a priority fee (max 20.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 664 |
| Delinquent validators | 14 |
| Delinquent stake | 0.07% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.18% / 24.45% / 35.64% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.92% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.67% | 0% |
| 3 | `3N7s…iD5g` | 12.6M | 2.88% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.49% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.17% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $102.50 (-0.71% 24h) |
| Market cap | $60.45B (rank #7) |
| 24h volume | $2.18B |
| ATH | $293.31 (-65.06% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.83B |
| Stablecoin supply | $15.64B |
| DEX volume (24h) | $2.04B (-10.18% 1d) |
| App fees (24h, all protocols) | $11.47M |
| Chain fees (24h) | $631.02K |
| Jito MEV tips (24h) | $138.59K |
| **REV - Real Economic Value (24h)** | **$769.60K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.77B | -2.92% |
| USDT | $2.83B | -0.35% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.30B | +3.57% |
| BUIDL | $886.39M | +0.10% |
| PYUSD | $687.57M | -1.80% |
| USDG | $641.43M | +1.94% |
| USDe | $327.29M | -25.96% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $312.02M |
| PumpSwap | $259.02M |
| Orca DEX | $197.43M |
| Tessera V | $187.55M |
| pump.fun | $142.23M |
| Raydium AMM | $140.92M |
| Manifest Trade | $135.46M |
| Meteora DLMM | $107.69M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.45M |
| pump.fun | $1.88M |
| Axiom | $792.29K |
| Collector Crypt | $460.15K |
| Meteora DLMM | $387.99K |
| pump.fun Mobile App | $311.09K |
| Sanctum Validator LSTs | $278.92K |
| Raydium AMM | $241.13K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $251.66M |
| xStocks holder positions | 843.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $594.36M |

## Program activity and chain health

Chain tip lag: **+1.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 48,969 | 47.20% | 1.1 s |
| Pump.fun | 21,728 | 77.80% | 2.7 s |
| Jupiter v6 | 6,029 | 67.20% | 9.7 s |
| Orca Whirlpools | 2,063 | 68.10% | 29 s |
| Raydium AMM v4 | 798 | 18.30% | 74.9 s |

Median failure rate across the sampled programs: **67.20%** (range 18.30% to 77.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **581.63 SOL**.

## Exchange and large-holder balances

13.47M SOL ($1.38B) across 6 publicly-attributed accounts. Net **40K SOL (0.30%) moved onto exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.15B | 0.2/h | 4 |
| Binance (2) | 1.50M | $153.49M | 944.9/h | 0 |
| Bybit | 330.96K | $33.92M | 44.7/h | 0 |
| Gate.io | 328.06K | $33.63M | 127.6/h | 0 |
| Bitget | 103.36K | $10.59M | 143/h | 0 |
| Kraken | 31.79K | $3.26M | 297.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1041 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.267 | 1000 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.234 | 1007 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.205 | 966 | 0.0000 |
| SOL price moves with DeFi TVL | +0.202 | 1041 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.200 | 966 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1007 | 0.0000 |
| Total TPS moves with Program failure rate | +0.161 | 988 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.161 | 988 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 966 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.113 | 966 | 0.0004 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 102.50 USD | Jupiter (on-chain DEX): 102.44 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 589.71M SOL | CoinGecko: 589.71M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-23
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23

**Recently merged SIMDs:**

- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-23
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-23
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-21
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-10-20
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-20

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.4) (2026-10-21)

## Ecosystem news

- **[Bitcoin ETFs Bleed $636 Million as October Turns Red Again](https://decrypt.co/381700/bitcoin-etfs-bleed-october-turns-red-again)** - Decrypt, 2026-10-23
- **[Solana Alpenglow Goes Live in 'Most Ambitious' Upgrade Since Ethereum's Merge](https://decrypt.co/381484/solana-alpenglow-goes-live-in-most-ambitious-upgrade-since-ethereums-merge)** - Decrypt, 2026-10-21
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
