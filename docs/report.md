# Solana Ecosystem Report

*Generated 2026-10-22 01:04 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Transactions per second** (warning): Transactions per second is 5.8 robust standard deviations below its 7-day baseline: a 64.6% move to 1,721.10 tps from a typical 4,860.70.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.7K |
| TPS (non-vote) | 1.7K |
| Slot time | 212.4 ms |
| Slot | 460M |
| Block height | 438M |
| Epoch | 1064 (44.89% complete, ~14.0h remaining) |
| Lifetime transactions | 563.1B |
| Circulating supply | 589.6M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 668 |
| Delinquent validators | 9 |
| Delinquent stake | 0.01% |
| Total active stake | 438.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.11% / 24.35% / 35.56% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.77% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.90% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.64% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.49% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.22% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.16% | 10% |
| 7 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.60% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $107.05 (+0.64% 24h) |
| Market cap | $63.12B (rank #7) |
| 24h volume | $2.59B |
| ATH | $293.31 (-63.50% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.03B |
| Stablecoin supply | $15.89B |
| DEX volume (24h) | $2.28B (-6.52% 1d) |
| App fees (24h, all protocols) | $11.79M |
| Chain fees (24h) | $732.12K |
| Jito MEV tips (24h) | $125.89K |
| **REV - Real Economic Value (24h)** | **$858.01K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.07B | -0.57% |
| USDT | $2.72B | -2.50% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.30B | +2.92% |
| BUIDL | $886.21M | -0.46% |
| PYUSD | $679.11M | -2.88% |
| USDG | $662.56M | +6.16% |
| USDe | $379.70M | -16.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $340.98M |
| PumpSwap | $293.40M |
| Orca DEX | $243.46M |
| Raydium AMM | $190.51M |
| pump.fun | $166.39M |
| Manifest Trade | $140.57M |
| Scorch | $138.56M |
| Tessera V | $133.58M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.46M |
| pump.fun | $2.00M |
| Axiom | $883.44K |
| Meteora DLMM | $547.07K |
| Raydium AMM | $355.57K |
| pump.fun Mobile App | $345.46K |
| Sanctum Validator LSTs | $289.89K |
| Collector Crypt | $289.21K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $63.02M |
| xStocks holder positions | 837.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.78M |

## Program activity and chain health

Chain tip lag: **+1.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 93,079 (approx.) | 51.10% | 0.4 s |
| Pump.fun | 43,879 | 88.50% | 1.3 s |
| Orca Whirlpools | 9,284 | 44.50% | 6.4 s |
| Jupiter v6 | 8,554 | 66.00% | 6.8 s |
| Raydium AMM v4 | 770 | 16.30% | 77.7 s |

Median failure rate across the sampled programs: **51.10%** (range 16.30% to 88.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **113.39 SOL**.

## Exchange and large-holder balances

13.36M SOL ($1.43B) across 8 publicly-attributed accounts. Net **37K SOL (0.28%) moved onto exchanges** over the last 19.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.20B | 0.2/h | 4 |
| Binance (2) | 1.39M | $148.94M | 923.1/h | 0 |
| Bybit | 330.78K | $35.41M | 47.7/h | 0 |
| Gate.io | 311.99K | $33.40M | 236.5/h | 0 |
| Bitget | 85.95K | $9.20M | 93.9/h | 0 |
| Kraken | 32.26K | $3.45M | 298.3/h | 0 |
| Coinbase (2) | 19.84K | $2.12M | 280.2/h | 0 |
| Coinbase | 13.64K | $1.46M | 247.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1030 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.272 | 989 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 996 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.203 | 955 | 0.0000 |
| SOL price moves with DeFi TVL | +0.199 | 1030 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.198 | 955 | 0.0000 |
| Total TPS moves with Slot time | +0.195 | 996 | 0.0000 |
| Total TPS moves with Program failure rate | +0.165 | 977 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.165 | 977 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 955 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.114 | 955 | 0.0004 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 107.05 USD | Jupiter (on-chain DEX): 107.04 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 589.60M SOL | CoinGecko: 589.60M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-21
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-20

**Open SIMD proposals:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-21
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-21
- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12

**Recently merged SIMDs:**

- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-21
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-10-20
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-20
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-20
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.4) (2026-10-21)

## Ecosystem news

- **[Anza’s Alpenglow goes live on Solana, cutting finality to 150 milliseconds](https://www.theblock.co/news/ecosystems/2026-10-21-anzas-alpenglow-goes-live-on-solana-cutting-finality-to-150-milliseconds-421508)** - The Block, 2026-10-21
- **[Solana Alpenglow Goes Live in 'Most Ambitious' Upgrade Since Ethereum's Merge](https://decrypt.co/381484/solana-alpenglow-goes-live-in-most-ambitious-upgrade-since-ethereums-merge)** - Decrypt, 2026-10-21
- **[Ethereum staking hits record as yields fall and Solana activity grows: Bitwise](https://www.theblock.co/news/ecosystems/2026-10-20-ethereum-solana-staking-record-yields-fall-bitwise-q3-421414)** - The Block, 2026-10-20
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
