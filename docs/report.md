# Solana Ecosystem Report

*Generated 2026-10-16 05:15 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.0K |
| TPS (non-vote) | 1.9K |
| Slot time | 216.2 ms |
| Slot | 458M |
| Block height | 436M |
| Epoch | 1059 (6.68% complete, ~24.2h remaining) |
| Lifetime transactions | 560.8B |
| Circulating supply | 589.3M SOL |
| Inflation (annual) | 3.60% |
| AMM write-lock congestion (150-slot window) | 13.30% of slots needed a priority fee (max 3.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 9 |
| Delinquent stake | 0.00% |
| Total active stake | 437.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.23% / 24.31% / 35.42% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 23.79% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.01% | 7% |
| 2 | `he1i…uBtk` | 15.5M | 3.53% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.82% | 0% |
| 4 | `8Gbw…F8iD` | 11.1M | 2.53% | 0% |
| 5 | `Catz…Diqb` | 10.2M | 2.33% | 5% |
| 6 | `51JB…UNAm` | 9.4M | 2.15% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.7M | 1.77% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `Dumi…Zk4a` | 6.4M | 1.47% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $106.16 (+3.15% 24h) |
| Market cap | $62.57B (rank #7) |
| 24h volume | $3.39B |
| ATH | $293.31 (-63.81% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.01B |
| Stablecoin supply | $15.89B |
| DEX volume (24h) | $2.42B (+14.26% 1d) |
| App fees (24h, all protocols) | $12.66M |
| Chain fees (24h) | $811.04K |
| Jito MEV tips (24h) | $219.33K |
| **REV - Real Economic Value (24h)** | **$1.03M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.98B | +3.33% |
| USDT | $2.80B | -3.77% |
| USD1 | $1.41B | 0.00% |
| USDGO | $1.26B | -3.49% |
| BUIDL | $885.52M | -4.22% |
| PYUSD | $678.84M | -3.19% |
| USDG | $629.09M | +0.29% |
| USDe | $441.39M | -10.70% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $381.36M |
| Orca DEX | $381.18M |
| PumpSwap | $252.51M |
| Raydium AMM | $232.61M |
| Meteora DLMM | $166.57M |
| pump.fun | $151.42M |
| Manifest Trade | $114.14M |
| Tessera V | $111.68M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.34M |
| pump.fun | $1.91M |
| Collector Crypt | $864.04K |
| Axiom | $829.89K |
| Meteora DLMM | $587.79K |
| Raydium AMM | $489.69K |
| pump.fun Mobile App | $367.39K |
| Jupiter Perpetual Exchange | $356.56K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $78.39M |
| xStocks holder positions | 822.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $601.62M |

## Program activity and chain health

Chain tip lag: **+8.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 43,062 | 29.70% | 1.3 s |
| Pump.fun | 9,066 | 50.00% | 6.5 s |
| Jupiter v6 | 4,315 | 58.90% | 13.8 s |
| Orca Whirlpools | 2,482 | 29.20% | 23.6 s |
| Raydium AMM v4 | 1,446 | 3.90% | 41.3 s |

Median failure rate across the sampled programs: **29.70%** (range 3.90% to 58.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **446.54 SOL**.

## Exchange and large-holder balances

13.42M SOL ($1.42B) across 8 publicly-attributed accounts. Net **20K SOL (0.15%) moved onto exchanges** over the last 23.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.19B | 0.2/h | 4 |
| Binance (2) | 1.40M | $148.88M | 1.1K/h | 0 |
| Gate.io | 320.64K | $34.04M | 125/h | 0 |
| Bybit | 308.81K | $32.78M | 22.7/h | 0 |
| Bitget | 104.61K | $11.10M | 480/h | 0 |
| Coinbase | 56.11K | $5.96M | 209.9/h | 0 |
| Kraken | 32.06K | $3.40M | 166/h | 0 |
| Coinbase (2) | 16.90K | $1.79M | 219.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 993 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.260 | 952 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.227 | 959 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.209 | 918 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.201 | 918 | 0.0000 |
| SOL price moves with DeFi TVL | +0.192 | 993 | 0.0000 |
| Total TPS moves with Slot time | +0.186 | 959 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 940 | 0.0000 |
| Total TPS moves with Program failure rate | +0.163 | 940 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.149 | 918 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 106.16 USD | Jupiter (on-chain DEX): 106.01 USD | +0.14% | agree |
| Circulating supply | getSupply (RPC): 589.32M SOL | CoinGecko: 589.32M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-14
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15

**Open SIMD proposals:**

- [SIMD-0088 Amendment: Hash validation in Core BPF migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/696) - updated 2026-10-15
- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-14
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

- **[DeFi Development boosts CHAD dividend to 14% amid push to grow Solana holdings](https://www.theblock.co/news/markets/2026-10-15-defi-development-chad-dividend-rate-14-418694)** - The Block, 2026-10-15
- **[Morning Minute: Solana Is About To Get Faster](https://decrypt.co/381018/morning-minute-solana-is-about-to-get-faster)** - Decrypt, 2026-10-15
- **[Ledger unveils Atom Android device with Solana Mobile integration and new tamper protections amid investigation into modified wallets](https://www.theblock.co/news/business/2026-10-15-ledger-atom-solana-mobile-418644)** - The Block, 2026-10-15
- **[Solana Sets a Date for Its Next Major Upgrade](https://decrypt.co/380974/solana-alpenglow-upgrade-date)** - Decrypt, 2026-10-14
- **[Major shareholder presses SkyAI on Solana sales after treasury shrinks 70% in a month](https://www.theblock.co/news/business/2026-10-14-solana-treasury-skyai-bastion-sol-sales-tender-offer-418598)** - The Block, 2026-10-14
- **[Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule)** - Solana.com, 2026-10-14
- **[More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2)** - Solana.com, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
