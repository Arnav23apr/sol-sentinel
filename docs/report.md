# Solana Ecosystem Report

*Generated 2026-09-15 15:52 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 1.9K |
| Slot time | 316.6 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1035 (39.08% complete, ~23.1h remaining) |
| Lifetime transactions | 548.7B |
| Circulating supply | 587.0M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,300 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 14,750 / 189,091 lamports |
| Paying no priority fee | 31.10% of 328 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 32.00% of slots needed a priority fee (max 10.2M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 11 |
| Delinquent stake | 0.08% |
| Total active stake | 438.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.42% / 24.34% / 35.58% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.93% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.05% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.7M | 2.20% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $99.43 (-2.60% 24h) |
| Market cap | $58.37B (rank #7) |
| 24h volume | $3.50B |
| ATH | $293.31 (-66.10% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.84B |
| Stablecoin supply | $15.99B |
| DEX volume (24h) | $2.53B (+41.27% 1d) |
| App fees (24h, all protocols) | $13.58M |
| Chain fees (24h) | $647.01K |
| Jito MEV tips (24h) | $125.88K |
| **REV - Real Economic Value (24h)** | **$772.89K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.12B | -2.80% |
| USDT | $2.48B | -10.12% |
| USDGO | $1.38B | +0.46% |
| USD1 | $1.32B | +4.45% |
| BUIDL | $992.89M | +1.53% |
| PYUSD | $715.03M | -2.20% |
| USDG | $612.44M | +7.11% |
| USDe | $527.53M | -1.45% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $445.38M |
| BisonFi | $315.80M |
| Raydium AMM | $235.67M |
| Meteora DLMM | $198.81M |
| fomo Wallet | $191.98M |
| HumidiFi | $179.41M |
| Orca DEX | $149.16M |
| Manifest Trade | $132.83M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.26M |
| pump.fun | $1.71M |
| Axiom | $1.29M |
| fomo Wallet | $905.21K |
| Raydium AMM | $835.59K |
| Meteora DLMM | $827.24K |
| StonkFun | $588.47K |
| Collector Crypt | $557.35K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 196 |
| Persistently-active cohort (lower bound) | >=196 |
| Unique payers across sampled blocks | 196 (1 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $84.29M |
| xStocks holder positions | 547.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

## Program activity and chain health

Chain tip lag: **+11.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 57,612 (approx.) | 37.70% | 0.6 s |
| Pump.fun | 37,751 | 88.90% | 1.6 s |
| Jupiter v6 | 9,135 | 79.30% | 6.3 s |
| Orca Whirlpools | 4,075 | 73.00% | 14.6 s |
| Raydium AMM v4 | 1,753 | 39.10% | 34.2 s |

Median failure rate across the sampled programs: **73.00%** (range 37.70% to 88.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.37 SOL**.

## Exchange and large-holder balances

11.61M SOL ($1.15B) across 8 publicly-attributed accounts. Net **33K SOL (0.28%) moved off exchanges** over the last 20.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $913.61M | 0.3/h | 1 |
| Binance (2) | 1.77M | $175.79M | 1.8K/h | 0 |
| Gate.io | 278.38K | $27.68M | 198.3/h | 0 |
| Bybit | 232.08K | $23.08M | 29.7/h | 0 |
| Coinbase | 44.21K | $4.40M | 371.5/h | 0 |
| Kraken | 34.65K | $3.45M | 324.6/h | 0 |
| Bitget | 33.12K | $3.29M | 251.7/h | 0 |
| Coinbase (2) | 31.93K | $3.17M | 378.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 829 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.203 | 788 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.196 | 795 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.162 | 754 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.160 | 754 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 795 | 0.0000 |
| Total TPS moves with Program failure rate | +0.152 | 776 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.152 | 776 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.121 | 754 | 0.0009 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.102 | 754 | 0.0051 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 210.28K USD | DeFiLlama: 647.01K USD | -101.89% | *indicative*: 0.33x, within the order-of-magnitude band |
| SOL price | coingecko: 99.43 USD | Jupiter (on-chain DEX): 99.28 USD | +0.15% | agree |
| Circulating supply | getSupply (RPC): 587.03M SOL | CoinGecko: 587.03M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-15
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-14
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-15
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11

**Recently merged SIMDs:**

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08
- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27

**Latest Agave release:** [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) (2026-09-11)

**Latest Firedancer release:** [v26.08.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.4) (2026-09-10)

## Ecosystem news

- **[Solana Treasury Firm DeFi Dev Corp Rolls Out $300M CHAD to Buy More SOL](https://decrypt.co/378183/solana-defi-development-corp-chad)** - Decrypt, 2026-09-15
- **[DeFi Development Corp expands Solana treasury to 2.39 million SOL, sets up $300 million CHAD ATM](https://www.theblock.co/news/markets/2026-09-14-defi-development-corp-expands-solana-treasury-2-39-million-sol-sets-300-million-chad-atm-414633)** - The Block, 2026-09-14
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
