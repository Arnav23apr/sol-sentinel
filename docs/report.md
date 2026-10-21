# Solana Ecosystem Report

*Generated 2026-10-21 10:46 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 1.6K |
| Slot time | 215.1 ms |
| Slot | 460M |
| Block height | 438M |
| Epoch | 1063 (89.05% complete, ~2.8h remaining) |
| Lifetime transactions | 563.0B |
| Circulating supply | 589.5M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 10.70% of slots needed a priority fee (max 18.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 668 |
| Delinquent validators | 11 |
| Delinquent stake | 0.00% |
| Total active stake | 438.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.10% / 24.35% / 35.56% |
| Commission (stake-weighted, delegatable validators) | 3.75% |
| Stake on private (100% commission) validators | 23.79% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.90% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.63% | 0% |
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
| SOL price | $106.47 (+2.50% 24h) |
| Market cap | $62.79B (rank #7) |
| 24h volume | $2.68B |
| ATH | $293.31 (-63.70% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.00B |
| Stablecoin supply | $15.71B |
| DEX volume (24h) | $2.46B (+34.78% 1d) |
| App fees (24h, all protocols) | $13.20M |
| Chain fees (24h) | $799.59K |
| Jito MEV tips (24h) | $156.42K |
| **REV - Real Economic Value (24h)** | **$956.01K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.94B | -2.39% |
| USDT | $2.69B | -3.58% |
| USD1 | $1.39B | -1.20% |
| USDGO | $1.29B | +1.89% |
| BUIDL | $886.12M | -0.47% |
| PYUSD | $681.79M | -2.50% |
| USDG | $645.01M | +3.39% |
| USDe | $388.11M | -14.12% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $396.96M |
| BisonFi | $340.98M |
| Orca DEX | $278.42M |
| Raydium AMM | $180.92M |
| pump.fun | $166.39M |
| Tessera V | $141.42M |
| Meteora DLMM | $139.28M |
| Scorch | $138.56M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.29M |
| pump.fun | $2.08M |
| Axiom | $907.80K |
| Collector Crypt | $670.14K |
| Meteora DLMM | $473.16K |
| Raydium AMM | $390.73K |
| pump.fun Mobile App | $302.70K |
| Sanctum Validator LSTs | $287.68K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $59.34M |
| xStocks holder positions | 837.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $593.15M |

## Program activity and chain health

Chain tip lag: **+8.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 50,600 | 47.10% | 1.1 s |
| Pump.fun | 27,699 | 91.70% | 2.2 s |
| Jupiter v6 | 5,207 | 68.20% | 11 s |
| Orca Whirlpools | 1,580 | 35.40% | 37.9 s |
| Raydium AMM v4 | 631 | 22.60% | 94.9 s |

Median failure rate across the sampled programs: **47.10%** (range 22.60% to 91.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **112.20 SOL**.

## Exchange and large-holder balances

13.32M SOL ($1.42B) across 8 publicly-attributed accounts. Net **120K SOL (0.89%) moved off exchanges** over the last 19.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.19B | 0.2/h | 4 |
| Binance (2) | 1.34M | $142.58M | 1.2K/h | 0 |
| Bybit | 330.78K | $35.22M | 32.2/h | 0 |
| Gate.io | 316.35K | $33.68M | 169/h | 0 |
| Bitget | 91.17K | $9.71M | 343.2/h | 0 |
| Kraken | 32.44K | $3.45M | 199.4/h | 0 |
| Coinbase (2) | 20.33K | $2.16M | 145.3/h | 0 |
| Coinbase | 17.77K | $1.89M | 122.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1026 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.266 | 985 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 992 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.203 | 951 | 0.0000 |
| SOL price moves with DeFi TVL | +0.196 | 1026 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.195 | 951 | 0.0000 |
| Total TPS moves with Slot time | +0.192 | 992 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 973 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 973 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 951 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.110 | 951 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 106.47 USD | Jupiter (on-chain DEX): 106.46 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 589.55M SOL | CoinGecko: 589.55M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-21
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-20

**Open SIMD proposals:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-21
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-20
- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14

**Recently merged SIMDs:**

- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-21
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-10-20
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-20
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-20
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.3](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.3) (2026-10-20)

## Ecosystem news

- **[Ethereum staking hits record as yields fall and Solana activity grows: Bitwise](https://www.theblock.co/news/ecosystems/2026-10-20-ethereum-solana-staking-record-yields-fall-bitwise-q3-421414)** - The Block, 2026-10-20
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
