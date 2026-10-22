# Solana Ecosystem Report

*Generated 2026-10-22 23:45 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 49.1 robust standard deviations above its 7-day baseline: a 7275.0% move to 0.29 % from a typical 0.00.
- 🔴 **Delinquent validators** (critical): Delinquent validators is 6.1 robust standard deviations above its 7-day baseline: a 81.8% move to 20.00 from a typical 11.00.
- 🟠 **Transactions per second** (warning): Transactions per second is 5.2 robust standard deviations below its 7-day baseline: a 69.6% move to 1,437.50 tps from a typical 4,721.20.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.4K |
| TPS (non-vote) | 1.4K |
| Slot time | 212.8 ms |
| Slot | 460M |
| Block height | 438M |
| Epoch | 1065 (33.95% complete, ~16.9h remaining) |
| Lifetime transactions | 563.3B |
| Circulating supply | 589.7M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 19.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 656 |
| Delinquent validators | 20 |
| Delinquent stake | 0.29% |
| Total active stake | 437.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.18% / 24.46% / 35.66% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.90% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.65% | 0% |
| 3 | `3N7s…iD5g` | 12.6M | 2.87% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.50% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.17% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $103.34 (-3.34% 24h) |
| Market cap | $60.93B (rank #7) |
| 24h volume | $2.46B |
| ATH | $293.31 (-64.77% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.88B |
| Stablecoin supply | $15.69B |
| DEX volume (24h) | $2.27B (-6.87% 1d) |
| App fees (24h, all protocols) | $11.96M |
| Chain fees (24h) | $732.12K |
| Jito MEV tips (24h) | $156.44K |
| **REV - Real Economic Value (24h)** | **$888.56K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.81B | -0.87% |
| USDT | $2.75B | -1.08% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.30B | +3.57% |
| BUIDL | $886.30M | +0.10% |
| PYUSD | $729.79M | +6.22% |
| USDG | $629.24M | +4.98% |
| USDe | $366.27M | -21.09% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $380.46M |
| PumpSwap | $293.40M |
| Orca DEX | $236.19M |
| Tessera V | $191.53M |
| Raydium AMM | $157.26M |
| pump.fun | $152.91M |
| Meteora DLMM | $131.39M |
| Manifest Trade | $112.43M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.46M |
| pump.fun | $2.07M |
| Axiom | $883.44K |
| Meteora DLMM | $547.07K |
| Collector Crypt | $506.82K |
| pump.fun Mobile App | $345.46K |
| Raydium AMM | $292.96K |
| Sanctum Validator LSTs | $289.89K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $68.86M |
| xStocks holder positions | 840.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $600.00M |

## Program activity and chain health

Chain tip lag: **+1.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 36,292 | 21.50% | 1.5 s |
| Pump.fun | 13,346 | 76.70% | 4.5 s |
| Jupiter v6 | 3,136 | 41.60% | 18.9 s |
| Orca Whirlpools | 1,741 | 46.50% | 33.8 s |
| Raydium AMM v4 | 1,159 | 29.60% | 51.7 s |

Median failure rate across the sampled programs: **41.60%** (range 21.50% to 76.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **379.30 SOL**.

## Exchange and large-holder balances

13.43M SOL ($1.39B) across 6 publicly-attributed accounts. Net **66K SOL (0.49%) moved onto exchanges** over the last 22.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.15B | 0.2/h | 4 |
| Binance (2) | 1.47M | $151.43M | 944.9/h | 0 |
| Bybit | 330.78K | $34.18M | 31.1/h | 0 |
| Gate.io | 317.57K | $32.82M | 164.3/h | 0 |
| Bitget | 104.81K | $10.83M | 89.1/h | 0 |
| Kraken | 33.00K | $3.41M | 202.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 1035 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.266 | 994 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.232 | 1001 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 960 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.203 | 960 | 0.0000 |
| SOL price moves with DeFi TVL | +0.201 | 1035 | 0.0000 |
| Total TPS moves with Slot time | +0.197 | 1001 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.165 | 982 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 982 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.159 | 960 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.111 | 960 | 0.0006 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 103.34 USD | Jupiter (on-chain DEX): 103.41 USD | -0.07% | agree |
| Circulating supply | getSupply (RPC): 589.65M SOL | CoinGecko: 589.65M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-22
- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-20

**Open SIMD proposals:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-22
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-21
- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-22

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
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
