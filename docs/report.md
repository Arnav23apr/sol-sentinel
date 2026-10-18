# Solana Ecosystem Report

*Generated 2026-10-18 11:26 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 215.4 ms |
| Slot | 458M |
| Block height | 436M |
| Epoch | 1061 (15.23% complete, ~21.9h remaining) |
| Lifetime transactions | 561.7B |
| Circulating supply | 589.4M SOL |
| Inflation (annual) | 3.60% |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 5.1M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 669 |
| Delinquent validators | 11 |
| Delinquent stake | 0.00% |
| Total active stake | 437.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.11% / 24.30% / 35.54% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.82% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `8Gbw…F8iD` | 11.0M | 2.51% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.22% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.16% | 10% |
| 7 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.78% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.60% | 5% |
| 10 | `Dumi…Zk4a` | 6.7M | 1.54% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $104.05 (-0.51% 24h) |
| Market cap | $61.33B (rank #7) |
| 24h volume | $1.92B |
| ATH | $293.31 (-64.53% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.94B |
| Stablecoin supply | $15.56B |
| DEX volume (24h) | $1.25B (-42.23% 1d) |
| App fees (24h, all protocols) | $9.25M |
| Chain fees (24h) | $622.77K |
| Jito MEV tips (24h) | $124.89K |
| **REV - Real Economic Value (24h)** | **$747.66K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.80B | +0.04% |
| USDT | $2.69B | -7.23% |
| USD1 | $1.40B | -1.20% |
| USDGO | $1.27B | -1.86% |
| BUIDL | $885.61M | -4.88% |
| PYUSD | $675.67M | -4.31% |
| USDG | $624.14M | -0.35% |
| USDe | $406.89M | -17.07% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $194.51M |
| BisonFi | $182.29M |
| Orca DEX | $145.39M |
| pump.fun | $127.77M |
| Tessera V | $93.95M |
| Raydium AMM | $84.49M |
| Meteora DLMM | $59.29M |
| Manifest Trade | $53.95M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.63M |
| pump.fun | $1.58M |
| Collector Crypt | $685.93K |
| Axiom | $629.65K |
| Meteora DLMM | $376.86K |
| pump.fun Mobile App | $299.01K |
| Sanctum Validator LSTs | $272.67K |
| fomo Wallet | $225.28K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $30.22M |
| xStocks holder positions | 834.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $619.82M |

## Program activity and chain health

Chain tip lag: **+8.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 53,203 | 32.70% | 1.1 s |
| Pump.fun | 11,481 | 82.00% | 5 s |
| Orca Whirlpools | 1,745 | 23.20% | 34.2 s |
| Jupiter v6 | 1,366 | 40.80% | 42.2 s |
| Raydium AMM v4 | 697 | 13.40% | 85.5 s |

Median failure rate across the sampled programs: **32.70%** (range 13.40% to 82.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **591.18 SOL**.

## Exchange and large-holder balances

13.34M SOL ($1.39B) across 8 publicly-attributed accounts. Net **39K SOL (0.29%) moved off exchanges** over the last 22.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.16B | 0.2/h | 4 |
| Binance (2) | 1.35M | $140.34M | 1.1K/h | 0 |
| Bybit | 328.74K | $34.21M | 10.4/h | 0 |
| Gate.io | 323.27K | $33.64M | 133.4/h | 0 |
| Bitget | 97.61K | $10.16M | 190/h | 0 |
| Kraken | 34.34K | $3.57M | 144.5/h | 0 |
| Coinbase | 18.36K | $1.91M | 123.2/h | 0 |
| Coinbase (2) | 16.60K | $1.73M | 102.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 15 of 117 tested pairs survive, over 1008 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.263 | 967 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.228 | 974 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.207 | 933 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.198 | 933 | 0.0000 |
| SOL price moves with DeFi TVL | +0.193 | 1008 | 0.0000 |
| Total TPS moves with Slot time | +0.188 | 974 | 0.0000 |
| Total TPS moves with Program failure rate | +0.161 | 955 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.161 | 955 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 933 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.108 | 933 | 0.0010 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 104.05 USD | Jupiter (on-chain DEX): 103.99 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 589.44M SOL | CoinGecko: 589.44M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-16
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15

**Open SIMD proposals:**

- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-17
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14

**Recently merged SIMDs:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15

**Latest Agave release:** [v4.3.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.2) (2026-10-15)

**Latest Firedancer release:** [v26.10.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.2) (2026-10-14)

## Ecosystem news

- **[GTA 6 Trailer Features Meme Coin—And Solana Copycat Soars 2,900%](https://decrypt.co/381122/gta-6-trailer-features-meme-coin-and-solana-copycat-soars-2900)** - Decrypt, 2026-10-16
- **[DeFi Development boosts CHAD dividend to 14% amid push to grow Solana holdings](https://www.theblock.co/news/markets/2026-10-15-defi-development-chad-dividend-rate-14-418694)** - The Block, 2026-10-15
- **[Morning Minute: Solana Is About To Get Faster](https://decrypt.co/381018/morning-minute-solana-is-about-to-get-faster)** - Decrypt, 2026-10-15
- **[Solana Sets a Date for Its Next Major Upgrade](https://decrypt.co/380974/solana-alpenglow-upgrade-date)** - Decrypt, 2026-10-14
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
