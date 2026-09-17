# Solana Ecosystem Report

*Generated 2026-09-17 20:42 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 1.9K |
| Slot time | 315.8 ms |
| Slot | 448M |
| Block height | 426M |
| Epoch | 1036 (77.90% complete, ~8.4h remaining) |
| Lifetime transactions | 549.5B |
| Circulating supply | 587.2M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 43.30% of slots needed a priority fee (max 18.8M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 13 |
| Delinquent stake | 0.04% |
| Total active stake | 439.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.35% / 35.66% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.89% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.7M | 2.22% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.08 (+2.87% 24h) |
| Market cap | $59.36B (rank #7) |
| 24h volume | $3.24B |
| ATH | $293.31 (-65.54% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.86B |
| Stablecoin supply | $15.33B |
| DEX volume (24h) | $2.80B (+3.59% 1d) |
| App fees (24h, all protocols) | $14.07M |
| Chain fees (24h) | $750.61K |
| Jito MEV tips (24h) | $182.19K |
| **REV - Real Economic Value (24h)** | **$932.80K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.66B | -6.60% |
| USDT | $2.27B | -17.72% |
| USDGO | $1.38B | +0.64% |
| USD1 | $1.32B | +2.83% |
| BUIDL | $993.29M | +0.11% |
| PYUSD | $702.41M | -7.07% |
| USDG | $620.07M | +3.05% |
| USDe | $523.56M | -2.19% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $441.42M |
| BisonFi | $440.07M |
| HumidiFi | $301.79M |
| Orca DEX | $300.14M |
| Raydium AMM | $258.81M |
| fomo Wallet | $215.36M |
| Meteora DLMM | $174.16M |
| Manifest Trade | $129.44M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.44M |
| pump.fun | $1.47M |
| Axiom | $1.38M |
| Raydium AMM | $954.15K |
| Meteora DLMM | $878.37K |
| StonkFun | $665.33K |
| fomo Wallet | $433.08K |
| Sanctum Validator LSTs | $362.23K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $84.74M |
| xStocks holder positions | 545.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $576.38M |

## Program activity and chain health

Chain tip lag: **+12.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 59,341 | 32.70% | 0.9 s |
| Jupiter v6 | 5,532 | 69.70% | 10.7 s |
| Pump.fun | 4,735 | 50.10% | 12.3 s |
| Raydium AMM v4 | 2,562 | 16.20% | 23.4 s |
| Orca Whirlpools | 2,550 | 60.10% | 23.4 s |

Median failure rate across the sampled programs: **50.10%** (range 16.20% to 69.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.37 SOL**.

## Exchange and large-holder balances

11.81M SOL ($1.19B) across 8 publicly-attributed accounts. Net **84K SOL (0.71%) moved off exchanges** over the last 22.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $928.77M | 0.2/h | 1 |
| Binance (2) | 1.98M | $199.65M | 1.5K/h | 0 |
| Gate.io | 269.14K | $27.20M | 112/h | 0 |
| Bybit | 235.08K | $23.76M | 16.5/h | 0 |
| Bitget | 46.41K | $4.69M | 204.3/h | 0 |
| Kraken | 34.53K | $3.49M | 251/h | 0 |
| Coinbase (2) | 30.68K | $3.10M | 524/h | 0 |
| Coinbase | 26.85K | $2.71M | 612.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 843 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.201 | 802 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.199 | 809 | 0.0000 |
| Total TPS moves with Slot time | +0.162 | 809 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.161 | 768 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.159 | 768 | 0.0000 |
| Total TPS moves with Program failure rate | +0.146 | 790 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.146 | 790 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| Slot time moves with AMM write-lock congestion | +0.117 | 768 | 0.0012 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 101.08 USD | Jupiter (on-chain DEX): 100.93 USD | +0.15% | agree |
| Circulating supply | getSupply (RPC): 587.21M SOL | CoinGecko: 587.21M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-16
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-17
- [amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-17
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-09-16

**Recently merged SIMDs:**

- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10

**Latest Agave release:** [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) (2026-09-11)

**Latest Firedancer release:** [v26.09.3](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.3) (2026-09-16)

## Ecosystem news

- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
