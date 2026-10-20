# Solana Ecosystem Report

*Generated 2026-10-20 22:27 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 98.0 robust standard deviations above its 7-day baseline: a 14533.3% move to 0.44 % from a typical 0.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.3K |
| TPS (non-vote) | 2.3K |
| Slot time | 216.6 ms |
| Slot | 459M |
| Block height | 437M |
| Epoch | 1063 (41.58% complete, ~15.2h remaining) |
| Lifetime transactions | 562.8B |
| Circulating supply | 589.5M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 20.70% of slots needed a priority fee (max 4.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 667 |
| Delinquent validators | 12 |
| Delinquent stake | 0.44% |
| Total active stake | 436.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.17% / 24.46% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.89% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.65% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.87% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.50% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.17% | 10% |
| 7 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $106.91 (+1.66% 24h) |
| Market cap | $63.03B (rank #7) |
| 24h volume | $2.70B |
| ATH | $293.31 (-63.55% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.98B |
| Stablecoin supply | $15.62B |
| DEX volume (24h) | $1.82B (+7.44% 1d) |
| App fees (24h, all protocols) | $12.01M |
| Chain fees (24h) | $781.53K |
| Jito MEV tips (24h) | $164.70K |
| **REV - Real Economic Value (24h)** | **$946.23K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.92B | +2.52% |
| USDT | $2.69B | -4.60% |
| USD1 | $1.39B | -1.20% |
| USDGO | $1.29B | -0.32% |
| BUIDL | $886.12M | -4.83% |
| PYUSD | $670.35M | -5.35% |
| USDG | $631.69M | +0.86% |
| USDe | $395.97M | -15.26% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $291.28M |
| BisonFi | $249.62M |
| Raydium AMM | $198.86M |
| pump.fun | $168.22M |
| PumpSwap | $142.12M |
| Tessera V | $141.42M |
| Meteora DLMM | $110.61M |
| Manifest Trade | $103.66M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.13M |
| pump.fun | $2.19M |
| Collector Crypt | $2.15M |
| Axiom | $848.42K |
| Meteora DLMM | $454.28K |
| Raydium AMM | $417.67K |
| pump.fun Mobile App | $317.37K |
| Sanctum Validator LSTs | $283.74K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $56.87M |
| xStocks holder positions | 837.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $592.72M |

## Program activity and chain health

Chain tip lag: **+8.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 86,796 | 53.70% | 0.6 s |
| Pump.fun | 49,197 | 85.80% | 1.1 s |
| Jupiter v6 | 3,428 | 52.70% | 17.3 s |
| Orca Whirlpools | 1,618 | 34.20% | 37 s |
| Raydium AMM v4 | 1,262 | 34.70% | 47.4 s |

Median failure rate across the sampled programs: **52.70%** (range 34.20% to 85.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **112.20 SOL**.

## Exchange and large-holder balances

13.37M SOL ($1.43B) across 8 publicly-attributed accounts. Net **60K SOL (0.45%) moved onto exchanges** over the last 21.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.19B | 0.2/h | 4 |
| Binance (2) | 1.38M | $148.01M | 1.0K/h | 0 |
| Bybit | 330.78K | $35.36M | 22.4/h | 0 |
| Gate.io | 309.36K | $33.07M | 265.3/h | 0 |
| Bitget | 85.72K | $9.16M | 137.1/h | 0 |
| Kraken | 40.37K | $4.32M | 396.5/h | 0 |
| Coinbase (2) | 28.60K | $3.06M | 305.6/h | 0 |
| Coinbase | 19.15K | $2.05M | 341.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1023 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.265 | 982 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 989 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.202 | 948 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.194 | 948 | 0.0000 |
| SOL price moves with DeFi TVL | +0.194 | 1023 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 989 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 970 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.163 | 970 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 948 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.111 | 948 | 0.0006 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 106.91 USD | Jupiter (on-chain DEX): 106.85 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 589.55M SOL | CoinGecko: 589.55M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-20
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-20

**Open SIMD proposals:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-20
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-20
- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12

**Recently merged SIMDs:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-10-20
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-20
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-20
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.3](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.3) (2026-10-20)

## Ecosystem news

- **[Ethereum staking hits record as yields fall and Solana activity grows: Bitwise](https://www.theblock.co/news/ecosystems/2026-10-20-ethereum-solana-staking-record-yields-fall-bitwise-q3-421414)** - The Block, 2026-10-20
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[SkyAI sells off entire Solana treasury as it launches $201 million buyback](https://www.theblock.co/news/business/2026-10-19-skyai-sells-off-entire-solana-treasury-launches-201-million-buyback-421037)** - The Block, 2026-10-19
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
