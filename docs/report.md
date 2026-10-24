# Solana Ecosystem Report

*Generated 2026-10-24 18:53 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent validators** (critical): Delinquent validators is 6.1 robust standard deviations above its 7-day baseline: a 117.4% move to 25.00 from a typical 11.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.6K |
| TPS (non-vote) | 1.6K |
| Slot time | 213.5 ms |
| Slot | 461M |
| Block height | 439M |
| Epoch | 1067 (3.51% complete, ~24.7h remaining) |
| Lifetime transactions | 563.6B |
| Circulating supply | 589.8M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 16.70% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 665 |
| Delinquent validators | 25 |
| Delinquent stake | 0.05% |
| Total active stake | 437.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.32% / 24.59% / 35.78% |
| Commission (stake-weighted, delegatable validators) | 3.75% |
| Stake on private (100% commission) validators | 23.91% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.6M | 3.81% | 0% |
| 3 | `3N7s…iD5g` | 12.6M | 2.88% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.49% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.22% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.17% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.60% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.02 (-2.87% 24h) |
| Market cap | $59.58B (rank #7) |
| 24h volume | $2.60B |
| ATH | $293.31 (-65.56% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.72B |
| Stablecoin supply | $15.61B |
| DEX volume (24h) | $2.00B (-2.07% 1d) |
| App fees (24h, all protocols) | $10.55M |
| Chain fees (24h) | $560.39K |
| Jito MEV tips (24h) | $133.85K |
| **REV - Real Economic Value (24h)** | **$694.24K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.72B | -4.01% |
| USDT | $2.83B | +6.38% |
| USD1 | $1.40B | -0.00% |
| USDGO | $1.30B | +2.60% |
| BUIDL | $886.39M | +0.09% |
| PYUSD | $706.41M | +3.15% |
| USDG | $639.97M | +2.84% |
| USDe | $318.65M | -24.34% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $342.50M |
| PumpSwap | $266.43M |
| Orca DEX | $183.81M |
| Tessera V | $162.38M |
| Manifest Trade | $152.37M |
| pump.fun | $142.80M |
| Raydium AMM | $139.60M |
| Scorch | $119.99M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.92M |
| pump.fun | $1.88M |
| Axiom | $685.23K |
| Collector Crypt | $643.93K |
| pump.fun Mobile App | $330.51K |
| Meteora DLMM | $304.25K |
| Sanctum Validator LSTs | $278.18K |
| fomo Wallet | $233.24K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $220.86M |
| xStocks holder positions | 844.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $594.44M |

## Program activity and chain health

Chain tip lag: **+0.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 40,890 | 32.10% | 1.3 s |
| Pump.fun | 18,749 | 75.90% | 3 s |
| Jupiter v6 | 7,291 | 70.60% | 7.5 s |
| Orca Whirlpools | 5,955 | 50.00% | 10 s |
| Raydium AMM v4 | 868 | 9.10% | 69 s |

Median failure rate across the sampled programs: **50.00%** (range 9.10% to 75.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **730.28 SOL**.

## Exchange and large-holder balances

13.56M SOL ($1.37B) across 8 publicly-attributed accounts. Net **47K SOL (0.35%) moved onto exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.13B | 0.2/h | 4 |
| Binance (2) | 1.55M | $156.41M | 1.2K/h | 0 |
| Gate.io | 344.43K | $34.79M | 161.8/h | 0 |
| Bybit | 330.96K | $33.43M | 38.5/h | 0 |
| Bitget | 102.42K | $10.35M | 176.6/h | 0 |
| Kraken | 35.44K | $3.58M | 461.5/h | 0 |
| Coinbase | 10.36K | $1.05M | 324/h | 0 |
| Coinbase (2) | 10.35K | $1.05M | 455.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1046 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.264 | 1005 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 1012 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 971 | 0.0000 |
| SOL price moves with DeFi TVL | +0.204 | 1046 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.203 | 971 | 0.0000 |
| Total TPS moves with Slot time | +0.196 | 1012 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 993 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 993 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 971 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.114 | 971 | 0.0004 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 101.02 USD | Jupiter (on-chain DEX): 100.99 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 589.76M SOL | CoinGecko: 589.75M SOL | 0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-21
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in program migrations and upgrades](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-24
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0676: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/676) - updated 2026-10-23

**Recently merged SIMDs:**

- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-23
- [[SIMD-0529] Finalize compute unit costs for the SIMD-0529 big_mod_exp syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/699) - updated 2026-10-23
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-10-21
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-20
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-10-20
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-20

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
