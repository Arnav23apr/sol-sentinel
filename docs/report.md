# Solana Ecosystem Report

*Generated 2026-10-23 12:56 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 46.0 robust standard deviations above its 7-day baseline: a 6820.0% move to 0.35 % from a typical 0.01.
- 🔴 **Delinquent validators** (critical): Delinquent validators is 6.7 robust standard deviations above its 7-day baseline: a 90.9% move to 21.00 from a typical 11.00.
- 🟠 **Transactions per second** (warning): Transactions per second is 3.5 robust standard deviations below its 7-day baseline: a 66.7% move to 1,552.60 tps from a typical 4,669.10.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.6K |
| TPS (non-vote) | 1.6K |
| Slot time | 211.3 ms |
| Slot | 460M |
| Block height | 438M |
| Epoch | 1065 (85.86% complete, ~3.6h remaining) |
| Lifetime transactions | 563.4B |
| Circulating supply | 589.7M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 655 |
| Delinquent validators | 21 |
| Delinquent stake | 0.35% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.18% / 24.47% / 35.67% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.92% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.66% | 0% |
| 3 | `3N7s…iD5g` | 12.6M | 2.87% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.50% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.17% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $104.22 (-0.01% 24h) |
| Market cap | $61.45B (rank #7) |
| 24h volume | $2.08B |
| ATH | $293.31 (-64.47% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.86B |
| Stablecoin supply | $15.67B |
| DEX volume (24h) | $2.04B (-10.18% 1d) |
| App fees (24h, all protocols) | $11.29M |
| Chain fees (24h) | $631.02K |
| Jito MEV tips (24h) | $138.32K |
| **REV - Real Economic Value (24h)** | **$769.34K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.83B | -1.98% |
| USDT | $2.75B | -3.16% |
| USD1 | $1.39B | -1.20% |
| USDGO | $1.30B | +3.57% |
| BUIDL | $886.30M | +0.09% |
| PYUSD | $731.09M | +4.43% |
| USDG | $628.10M | -0.15% |
| USDe | $334.28M | -24.36% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $312.02M |
| PumpSwap | $259.02M |
| Orca DEX | $200.70M |
| Tessera V | $187.55M |
| pump.fun | $142.23M |
| Raydium AMM | $125.86M |
| Manifest Trade | $114.04M |
| Meteora DLMM | $107.69M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.45M |
| pump.fun | $1.88M |
| Axiom | $792.29K |
| Meteora DLMM | $387.99K |
| Collector Crypt | $366.96K |
| pump.fun Mobile App | $311.09K |
| Sanctum Validator LSTs | $278.92K |
| fomo Wallet | $237.28K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $63.94M |
| xStocks holder positions | 842.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $593.54M |

## Program activity and chain health

Chain tip lag: **+0.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 62,399 | 38.00% | 0.8 s |
| Pump.fun | 23,878 | 82.80% | 2.3 s |
| Jupiter v6 | 4,723 | 49.20% | 12.7 s |
| Orca Whirlpools | 1,760 | 47.50% | 34 s |
| Raydium AMM v4 | 1,103 | 18.60% | 53 s |

Median failure rate across the sampled programs: **47.50%** (range 18.60% to 82.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **377.94 SOL**.

## Exchange and large-holder balances

13.47M SOL ($1.40B) across 6 publicly-attributed accounts. Net **120K SOL (0.90%) moved onto exchanges** over the last 19.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.16B | 0.2/h | 4 |
| Binance (2) | 1.49M | $155.32M | 1.2K/h | 0 |
| Bybit | 330.78K | $34.47M | 67.5/h | 0 |
| Gate.io | 324.04K | $33.77M | 146.6/h | 0 |
| Bitget | 100.04K | $10.43M | 161.2/h | 0 |
| Kraken | 47.50K | $4.95M | 221.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1038 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.268 | 997 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1004 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 963 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.203 | 963 | 0.0000 |
| SOL price moves with DeFi TVL | +0.198 | 1038 | 0.0000 |
| Total TPS moves with Slot time | +0.197 | 1004 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 985 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 985 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 963 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.112 | 963 | 0.0005 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 104.22 USD | Jupiter (on-chain DEX): 104.39 USD | -0.16% | agree |
| Circulating supply | getSupply (RPC): 589.65M SOL | CoinGecko: 589.65M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-20

**Open SIMD proposals:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-23
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - updated 2026-10-20

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

- **[Solana Alpenglow Goes Live in 'Most Ambitious' Upgrade Since Ethereum's Merge](https://decrypt.co/381484/solana-alpenglow-goes-live-in-most-ambitious-upgrade-since-ethereums-merge)** - Decrypt, 2026-10-21
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
