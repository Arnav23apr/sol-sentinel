# Solana Ecosystem Report

*Generated 2026-09-18 01:20 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Activity index (fee payers per block)** (warning): Activity index (fee payers per block) is 5.3 robust standard deviations below its 7-day baseline: a 72.5% move to 71.00 from a typical 258.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 1.9K |
| Slot time | 317.5 ms |
| Slot | 448M |
| Block height | 426M |
| Epoch | 1036 (90.09% complete, ~3.8h remaining) |
| Lifetime transactions | 549.6B |
| Circulating supply | 587.2M SOL |
| Inflation (annual) | 3.64% |
| Median transaction fee | 5,057 lamports (about $0.00051) |
| Transaction fee p90 / p99 | 15,000 / 1,005,000 lamports |
| Paying no priority fee | 24.50% of 110 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 30.00% of slots needed a priority fee (max 21.7M µlam/CU) |
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
| SOL price | $101.50 (+2.82% 24h) |
| Market cap | $59.59B (rank #7) |
| 24h volume | $3.24B |
| ATH | $293.31 (-65.40% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.88B |
| Stablecoin supply | $15.40B |
| DEX volume (24h) | $2.56B (-8.72% 1d) |
| App fees (24h, all protocols) | $14.21M |
| Chain fees (24h) | $750.61K |
| Jito MEV tips (24h) | $172.18K |
| **REV - Real Economic Value (24h)** | **$922.79K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.69B | -4.17% |
| USDT | $2.27B | -14.95% |
| USDGO | $1.38B | -0.08% |
| USD1 | $1.32B | +2.83% |
| BUIDL | $993.29M | +0.08% |
| PYUSD | $732.97M | -1.62% |
| USDG | $624.05M | +4.16% |
| USDe | $523.14M | -2.40% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $440.07M |
| PumpSwap | $329.29M |
| HumidiFi | $301.79M |
| Raydium AMM | $283.25M |
| fomo Wallet | $218.37M |
| Meteora DLMM | $177.93M |
| Orca DEX | $170.36M |
| Tessera V | $125.24M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.44M |
| pump.fun | $1.47M |
| Axiom | $1.38M |
| Raydium AMM | $976.54K |
| Meteora DLMM | $878.37K |
| StonkFun | $665.33K |
| fomo Wallet | $433.08K |
| Sanctum Validator LSTs | $362.23K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 71 |
| Persistently-active cohort (lower bound) | >=71 |
| Unique payers across sampled blocks | 71 (1 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $76.85M |
| xStocks holder positions | 546.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $572.95M |

## Program activity and chain health

Chain tip lag: **+11.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 62,488 | 32.60% | 1 s |
| Orca Whirlpools | 10,436 | 43.20% | 5.7 s |
| Jupiter v6 | 7,136 | 73.30% | 7.9 s |
| Raydium AMM v4 | 6,915 | 29.60% | 8.6 s |
| Pump.fun | 5,024 | 48.70% | 11.4 s |

Median failure rate across the sampled programs: **43.20%** (range 29.60% to 73.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.37 SOL**.

## Exchange and large-holder balances

11.79M SOL ($1.20B) across 8 publicly-attributed accounts. Net **89K SOL (0.75%) moved off exchanges** over the last 22.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $932.63M | 0.2/h | 1 |
| Binance (2) | 1.98M | $200.70M | 843.1/h | 0 |
| Gate.io | 265.93K | $26.99M | 182.2/h | 0 |
| Bybit | 235.08K | $23.86M | 20.3/h | 0 |
| Bitget | 42.51K | $4.32M | 154.7/h | 0 |
| Coinbase | 28.70K | $2.91M | 393.9/h | 0 |
| Coinbase (2) | 27.95K | $2.84M | 352.3/h | 0 |
| Kraken | 27.35K | $2.78M | 193.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 845 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.200 | 811 | 0.0000 |
| DEX volume moves with App fees | +0.194 | 804 | 0.0000 |
| Total TPS moves with Slot time | +0.164 | 811 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.160 | 770 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.158 | 770 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.151 | 792 | 0.0000 |
| Total TPS moves with Program failure rate | +0.150 | 792 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| Slot time moves with AMM write-lock congestion | +0.116 | 770 | 0.0013 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 230.64K USD | DeFiLlama: 750.61K USD | -105.98% | *indicative*: 0.31x, within the order-of-magnitude band |
| SOL price | coingecko: 101.50 USD | Jupiter (on-chain DEX): 101.63 USD | -0.13% | agree |
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
- [amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
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
- **[Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)** - Solana.com, 2026-09-10
- **[Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)** - Solana.com, 2026-09-10
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
