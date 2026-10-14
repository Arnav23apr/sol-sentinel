# Solana Ecosystem Report

*Generated 2026-10-14 22:48 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.9K |
| TPS (non-vote) | 1.7K |
| Slot time | 213.5 ms |
| Slot | 457M |
| Block height | 435M |
| Epoch | 1057 (89.35% complete, ~2.7h remaining) |
| Lifetime transactions | 560.2B |
| Circulating supply | 589.2M SOL |
| Inflation (annual) | 3.60% |
| AMM write-lock congestion (150-slot window) | 20.00% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
| Delinquent validators | 5 |
| Delinquent stake | 0.00% |
| Total active stake | 438.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.48% / 24.59% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.78% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.61% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.81% | 0% |
| 4 | `8Gbw…F8iD` | 11.1M | 2.54% | 0% |
| 5 | `Catz…Diqb` | 10.8M | 2.46% | 5% |
| 6 | `51JB…UNAm` | 9.4M | 2.15% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.7M | 1.76% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `3JD3…FrXf` | 6.6M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $104.13 (-2.48% 24h) |
| Market cap | $61.36B (rank #7) |
| 24h volume | $3.25B |
| ATH | $293.31 (-64.50% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.98B |
| Stablecoin supply | $15.81B |
| DEX volume (24h) | $2.50B (+11.80% 1d) |
| App fees (24h, all protocols) | $11.78M |
| Chain fees (24h) | $790.54K |
| Jito MEV tips (24h) | $199.16K |
| **REV - Real Economic Value (24h)** | **$989.70K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.94B | -3.85% |
| USDT | $2.78B | -3.13% |
| USD1 | $1.41B | 0.00% |
| USDGO | $1.26B | -3.62% |
| BUIDL | $885.43M | -8.53% |
| PYUSD | $677.98M | -5.22% |
| USDG | $600.59M | -4.14% |
| USDe | $464.33M | -14.02% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $451.80M |
| BisonFi | $411.45M |
| Orca DEX | $283.35M |
| Raydium AMM | $168.93M |
| pump.fun | $164.38M |
| Tessera V | $141.37M |
| Meteora DLMM | $114.45M |
| GoonFi | $98.65M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.29M |
| pump.fun | $2.07M |
| Axiom | $845.27K |
| Meteora DLMM | $462.06K |
| Raydium AMM | $325.44K |
| pump.fun Mobile App | $321.33K |
| Collector Crypt | $290.78K |
| Sanctum Validator LSTs | $280.47K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $56.90M |
| xStocks holder positions | 813.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $590.16M |

## Program activity and chain health

Chain tip lag: **+8.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 89,180 | 45.70% | 0.6 s |
| Pump.fun | 42,061 | 83.50% | 1.3 s |
| Orca Whirlpools | 9,061 | 42.90% | 6.2 s |
| Jupiter v6 | 6,444 | 67.10% | 9.2 s |
| Raydium AMM v4 | 3,042 | 23.90% | 19.4 s |

Median failure rate across the sampled programs: **45.70%** (range 23.90% to 83.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **90.42 SOL**.

## Exchange and large-holder balances

13.17M SOL ($1.37B) across 6 publicly-attributed accounts. Net **94K SOL (0.72%) moved onto exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.18M | $1.16B | 0.2/h | 4 |
| Binance (2) | 1.25M | $129.83M | 973/h | 0 |
| Gate.io | 316.82K | $32.99M | 181.4/h | 0 |
| Bybit | 308.80K | $32.16M | 17.7/h | 0 |
| Bitget | 98.63K | $10.27M | 102/h | 0 |
| Kraken | 27.23K | $2.84M | 269.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 985 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.244 | 944 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 951 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 910 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.200 | 910 | 0.0000 |
| SOL price moves with DeFi TVL | +0.195 | 985 | 0.0000 |
| Total TPS moves with Slot time | +0.188 | 951 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.160 | 932 | 0.0000 |
| Total TPS moves with Program failure rate | +0.159 | 932 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.149 | 910 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 104.13 USD | Jupiter (on-chain DEX): 104.36 USD | -0.22% | agree |
| Circulating supply | getSupply (RPC): 589.21M SOL | CoinGecko: 589.21M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-14
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15

**Open SIMD proposals:**

- [[SIMD-0565] Specify compute unit costs for the SIMD-0565 secp256r1 syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/695) - updated 2026-10-14
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-14
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-14
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-14

**Recently merged SIMDs:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15

**Latest Agave release:** [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) (2026-10-13)

**Latest Firedancer release:** [v26.10.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.2) (2026-10-14)

## Ecosystem news

- **[Solana Sets a Date for Its Next Major Upgrade](https://decrypt.co/380974/solana-alpenglow-upgrade-date)** - Decrypt, 2026-10-14
- **[Major shareholder presses SkyAI on Solana sales after treasury shrinks 70% in a month](https://www.theblock.co/news/business/2026-10-14-solana-treasury-skyai-bastion-sol-sales-tender-offer-418598)** - The Block, 2026-10-14
- **[Solana Treasury Firm DeFi Development Keeps Buying SOL as CHAD Preferred Stock Hits Record](https://decrypt.co/380752/solana-treasury-firm-defi-development-keeps-buying-sol)** - Decrypt, 2026-10-12
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06
- **[Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)** - Solana.com, 2026-10-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
