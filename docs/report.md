# Solana Ecosystem Report

*Generated 2026-10-21 19:44 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Transactions per second** (warning): Transactions per second is 4.9 robust standard deviations below its 7-day baseline: a 51.6% move to 2,384.30 tps from a typical 4,930.95.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.4K |
| TPS (non-vote) | 2.4K |
| Slot time | 213.6 ms |
| Slot | 460M |
| Block height | 438M |
| Epoch | 1064 (24.07% complete, ~19.5h remaining) |
| Lifetime transactions | 563.1B |
| Circulating supply | 589.6M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 7.5M µlam/CU) |
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
| SOL price | $108.27 (+2.30% 24h) |
| Market cap | $63.82B (rank #7) |
| 24h volume | $2.48B |
| ATH | $293.31 (-63.09% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.06B |
| Stablecoin supply | $15.89B |
| DEX volume (24h) | $2.44B (+33.68% 1d) |
| App fees (24h, all protocols) | $13.17M |
| Chain fees (24h) | $799.59K |
| Jito MEV tips (24h) | $128.14K |
| **REV - Real Economic Value (24h)** | **$927.74K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.10B | -0.17% |
| USDT | $2.72B | -2.50% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.30B | +2.92% |
| BUIDL | $886.21M | -0.46% |
| PYUSD | $672.46M | -3.91% |
| USDG | $632.60M | +1.36% |
| USDe | $387.35M | -14.37% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $396.96M |
| BisonFi | $340.98M |
| Orca DEX | $278.42M |
| Raydium AMM | $192.53M |
| pump.fun | $166.39M |
| Manifest Trade | $139.30M |
| Meteora DLMM | $139.28M |
| Scorch | $138.56M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.29M |
| pump.fun | $2.08M |
| Axiom | $907.80K |
| Meteora DLMM | $473.16K |
| Collector Crypt | $417.42K |
| Raydium AMM | $378.83K |
| pump.fun Mobile App | $302.70K |
| Sanctum Validator LSTs | $287.68K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $60.97M |
| xStocks holder positions | 838.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $593.86M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 92,041 | 55.10% | 0.6 s |
| Pump.fun | 27,747 | 84.80% | 1.9 s |
| Jupiter v6 | 9,841 | 71.50% | 6 s |
| Orca Whirlpools | 2,884 | 36.10% | 20.7 s |
| Raydium AMM v4 | 1,498 | 4.80% | 39.7 s |

Median failure rate across the sampled programs: **55.10%** (range 4.80% to 84.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **113.39 SOL**.

## Exchange and large-holder balances

13.37M SOL ($1.45B) across 8 publicly-attributed accounts. Net **3K SOL (0.02%) moved off exchanges** over the last 21.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.21B | 0.2/h | 4 |
| Binance (2) | 1.38M | $149.49M | 1.2K/h | 0 |
| Bybit | 330.78K | $35.81M | 52/h | 0 |
| Gate.io | 316.62K | $34.28M | 203/h | 0 |
| Bitget | 89.62K | $9.70M | 145.6/h | 0 |
| Kraken | 38.65K | $4.18M | 311.7/h | 0 |
| Coinbase (2) | 22.53K | $2.44M | 290.3/h | 0 |
| Coinbase | 16.50K | $1.79M | 293.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1028 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.269 | 987 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.228 | 994 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.200 | 953 | 0.0000 |
| SOL price moves with DeFi TVL | +0.196 | 1028 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.194 | 953 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 994 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.161 | 975 | 0.0000 |
| Total TPS moves with Program failure rate | +0.160 | 975 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.155 | 953 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.111 | 953 | 0.0006 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 108.27 USD | Jupiter (on-chain DEX): 108.22 USD | +0.05% | agree |
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
