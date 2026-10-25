# Solana Ecosystem Report

*Generated 2026-10-25 06:22 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 22.6 robust standard deviations above its 7-day baseline: a 3350.0% move to 0.62 % from a typical 0.02.
- 🟠 **Delinquent validators** (warning): Delinquent validators is 4.7 robust standard deviations above its 7-day baseline: a 116.7% move to 26.00 from a typical 12.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.6K |
| TPS (non-vote) | 1.6K |
| Slot time | 212.4 ms |
| Slot | 461M |
| Block height | 439M |
| Epoch | 1067 (48.61% complete, ~13.1h remaining) |
| Lifetime transactions | 563.7B |
| Circulating supply | 589.8M SOL |
| Inflation (annual) | 3.59% |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 1.3M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 664 |
| Delinquent validators | 26 |
| Delinquent stake | 0.62% |
| Total active stake | 434.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.73% / 35.99% |
| Commission (stake-weighted, delegatable validators) | 3.75% |
| Stake on private (100% commission) validators | 23.47% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.6M | 3.83% | 0% |
| 3 | `3N7s…iD5g` | 12.6M | 2.90% | 0% |
| 4 | `8Gbw…F8iD` | 10.9M | 2.50% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.24% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.62% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.79 (-0.35% 24h) |
| Market cap | $60.04B (rank #7) |
| 24h volume | $2.24B |
| ATH | $293.31 (-65.30% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.80B |
| Stablecoin supply | $15.60B |
| DEX volume (24h) | $1.73B (-13.25% 1d) |
| App fees (24h, all protocols) | $9.95M |
| Chain fees (24h) | $477.32K |
| Jito MEV tips (24h) | $113.77K |
| **REV - Real Economic Value (24h)** | **$591.09K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.71B | -2.47% |
| USDT | $2.83B | +6.38% |
| USD1 | $1.40B | -0.00% |
| USDGO | $1.30B | +2.60% |
| BUIDL | $886.39M | +0.09% |
| PYUSD | $711.79M | +5.31% |
| USDG | $636.69M | +1.95% |
| USDe | $318.36M | -21.95% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $342.50M |
| Tessera V | $162.38M |
| pump.fun | $142.80M |
| Orca DEX | $141.95M |
| Manifest Trade | $125.78M |
| Scorch | $119.99M |
| Raydium AMM | $116.32M |
| PumpSwap | $112.73M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.95M |
| pump.fun | $1.58M |
| Axiom | $525.60K |
| Collector Crypt | $489.11K |
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
| xStocks 24h DEX volume | $17.29M |
| xStocks holder positions | 843.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $593.79M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,994 | 13.10% | 1.3 s |
| Pump.fun | 6,438 | 45.70% | 9.1 s |
| Jupiter v6 | 1,931 | 16.30% | 30.8 s |
| Orca Whirlpools | 1,195 | 35.30% | 50.1 s |
| Raydium AMM v4 | 533 | 14.80% | 111.5 s |

Median failure rate across the sampled programs: **16.30%** (range 13.10% to 45.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **385.13 SOL**.

## Exchange and large-holder balances

13.54M SOL ($1.38B) across 8 publicly-attributed accounts. Net **54K SOL (0.40%) moved onto exchanges** over the last 22.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.14B | 0.2/h | 4 |
| Binance (2) | 1.54M | $156.49M | 851.1/h | 0 |
| Gate.io | 341.31K | $34.74M | 121.2/h | 0 |
| Bybit | 330.96K | $33.69M | 35.4/h | 0 |
| Bitget | 100.90K | $10.27M | 96.2/h | 0 |
| Kraken | 30.94K | $3.15M | 228.4/h | 0 |
| Coinbase (2) | 12.74K | $1.30M | 285/h | 0 |
| Coinbase | 12.55K | $1.28M | 184.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1050 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.263 | 1009 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 1016 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 975 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.203 | 975 | 0.0000 |
| SOL price moves with DeFi TVL | +0.201 | 1050 | 0.0000 |
| Total TPS moves with Slot time | +0.195 | 1016 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 997 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 997 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 975 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.115 | 975 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 101.79 USD | Jupiter (on-chain DEX): 101.79 USD | 0.00% | agree |
| Circulating supply | getSupply (RPC): 589.76M SOL | CoinGecko: 589.76M SOL | -0.00% | agree |

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
