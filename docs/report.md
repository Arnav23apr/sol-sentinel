# Solana Ecosystem Report

*Generated 2026-09-14 14:46 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.0K |
| Slot time | 316.6 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1034 (72.85% complete, ~10.3h remaining) |
| Lifetime transactions | 548.4B |
| Circulating supply | 586.9M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,493 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 25,108 / 410,000 lamports |
| Paying no priority fee | 25.80% of 4,081 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 23.30% of slots needed a priority fee (max 61.6M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 679 |
| Delinquent validators | 11 |
| Delinquent stake | 0.40% |
| Total active stake | 437.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 24.39% / 35.66% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.09% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.02% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.74% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.60% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.20% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.69% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.59% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.40 (+0.65% 24h) |
| Market cap | $59.53B (rank #7) |
| 24h volume | $2.62B |
| ATH | $293.31 (-65.43% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.89B |
| Stablecoin supply | $16.02B |
| DEX volume (24h) | $1.79B (+2.72% 1d) |
| App fees (24h, all protocols) | $14.04M |
| Chain fees (24h) | $608.10K |
| Jito MEV tips (24h) | $95.14K |
| **REV - Real Economic Value (24h)** | **$703.23K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.19B | -2.24% |
| USDT | $2.48B | -10.12% |
| USDGO | $1.39B | +2.68% |
| USD1 | $1.31B | +3.76% |
| BUIDL | $992.60M | +1.50% |
| PYUSD | $685.92M | -8.32% |
| USDG | $603.79M | +2.89% |
| USDe | $532.62M | -0.40% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $315.70M |
| Raydium AMM | $241.96M |
| BisonFi | $201.48M |
| Meteora DLMM | $157.73M |
| fomo Wallet | $155.28M |
| Orca DEX | $136.37M |
| HumidiFi | $108.44M |
| Tessera V | $107.00M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.19M |
| pump.fun | $1.55M |
| Axiom | $1.17M |
| fomo Wallet | $962.09K |
| Raydium AMM | $849.20K |
| Meteora DLMM | $838.46K |
| StonkFun | $662.72K |
| Collector Crypt | $397.76K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 257 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $93.34M |
| xStocks holder positions | 538.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.93B |

## Program activity and chain health

Chain tip lag: **+11.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 63,582 (approx.) | 45.20% | 0.6 s |
| Jupiter v6 | 14,150 | 80.70% | 3.8 s |
| Pump.fun | 11,158 | 79.70% | 5.1 s |
| Orca Whirlpools | 4,231 | 63.60% | 13.6 s |
| Raydium AMM v4 | 1,329 | 42.50% | 45 s |

Median failure rate across the sampled programs: **63.60%** (range 42.50% to 80.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **986.24 SOL**.

## Exchange and large-holder balances

11.63M SOL ($1.18B) across 8 publicly-attributed accounts. Net **100K SOL (0.86%) moved off exchanges** over the last 22.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $931.71M | 0.3/h | 1 |
| Binance (2) | 1.82M | $184.18M | 1.4K/h | 0 |
| Gate.io | 293.48K | $29.76M | 206.9/h | 0 |
| Bybit | 232.08K | $23.53M | 32.8/h | 0 |
| Kraken | 32.52K | $3.30M | 257.7/h | 0 |
| Bitget | 27.20K | $2.76M | 228.7/h | 0 |
| Coinbase (2) | 24.08K | $2.44M | 364/h | 0 |
| Coinbase | 15.51K | $1.57M | 412.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 823 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.213 | 782 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 789 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.160 | 748 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.158 | 748 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 789 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.146 | 770 | 0.0001 |
| Total TPS moves with Program failure rate | +0.145 | 770 | 0.0001 |
| Slot time moves with AMM write-lock congestion | +0.124 | 748 | 0.0007 |
| Share paying base fee only moves with Activity index | +0.119 | 812 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 899.32K USD | DeFiLlama: 608.10K USD | +38.64% | *indicative*: 1.48x, within the order-of-magnitude band |
| SOL price | coingecko: 101.40 USD | Jupiter (on-chain DEX): 101.59 USD | -0.19% | agree |
| Circulating supply | getSupply (RPC): 586.89M SOL | CoinGecko: 586.89M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-11
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-14
- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11

**Recently merged SIMDs:**

- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08
- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12

**Latest Agave release:** [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) (2026-09-11)

**Latest Firedancer release:** [v26.08.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.4) (2026-09-10)

## Ecosystem news

- **[DeFi Development Corp expands Solana treasury to 2.39 million SOL, sets up $300 million CHAD ATM](https://www.theblock.co/news/markets/2026-09-14-defi-development-corp-expands-solana-treasury-2-39-million-sol-sets-300-million-chad-atm-414633)** - The Block, 2026-09-14
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
