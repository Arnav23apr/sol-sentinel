# Solana Ecosystem Report

*Generated 2026-09-15 06:15 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.3K |
| Slot time | 315 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1035 (13.68% complete, ~32.6h remaining) |
| Lifetime transactions | 548.6B |
| Circulating supply | 587.0M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,410 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 28,363 / 505,000 lamports |
| Paying no priority fee | 26.80% of 2,735 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 2.3M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 680 |
| Delinquent validators | 9 |
| Delinquent stake | 0.03% |
| Total active stake | 439.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.33% / 35.57% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.96% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.84% | 0% |
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
| SOL price | $101.35 (-0.32% 24h) |
| Market cap | $59.50B (rank #7) |
| 24h volume | $3.16B |
| ATH | $293.31 (-65.45% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.89B |
| Stablecoin supply | $16.06B |
| DEX volume (24h) | $2.21B (+23.55% 1d) |
| App fees (24h, all protocols) | $13.55M |
| Chain fees (24h) | $647.01K |
| Jito MEV tips (24h) | $114.76K |
| **REV - Real Economic Value (24h)** | **$761.77K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.16B | -2.27% |
| USDT | $2.48B | -10.12% |
| USDGO | $1.39B | +1.56% |
| USD1 | $1.32B | +4.45% |
| BUIDL | $992.89M | +1.53% |
| PYUSD | $712.72M | -2.58% |
| USDG | $610.59M | +6.76% |
| USDe | $528.66M | -1.29% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $445.38M |
| Raydium AMM | $295.80M |
| BisonFi | $201.48M |
| Meteora DLMM | $198.81M |
| fomo Wallet | $183.79M |
| Orca DEX | $163.67M |
| Manifest Trade | $124.79M |
| HumidiFi | $108.44M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.26M |
| pump.fun | $1.71M |
| Axiom | $1.29M |
| Raydium AMM | $1.19M |
| fomo Wallet | $962.09K |
| Meteora DLMM | $827.24K |
| StonkFun | $588.47K |
| Collector Crypt | $482.57K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 260 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.1K (5 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $93.18M |
| xStocks holder positions | 542.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

## Program activity and chain health

Chain tip lag: **+11.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 36,686 | 13.90% | 1.6 s |
| Pump.fun | 6,424 | 65.00% | 9.1 s |
| Jupiter v6 | 1,884 | 47.00% | 31.8 s |
| Orca Whirlpools | 1,361 | 15.10% | 43.5 s |
| Raydium AMM v4 | 1,128 | 21.20% | 52.9 s |

Median failure rate across the sampled programs: **21.20%** (range 13.90% to 65.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.53K SOL**.

## Exchange and large-holder balances

11.62M SOL ($1.18B) across 8 publicly-attributed accounts. Net **113K SOL (0.97%) moved off exchanges** over the last 22.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $931.25M | 0.3/h | 1 |
| Binance (2) | 1.79M | $181.36M | 754.7/h | 0 |
| Gate.io | 277.80K | $28.16M | 166.7/h | 0 |
| Bybit | 232.08K | $23.52M | 24.2/h | 0 |
| Coinbase | 39.30K | $3.98M | 218.6/h | 0 |
| Bitget | 32.26K | $3.27M | 239.5/h | 0 |
| Coinbase (2) | 30.44K | $3.09M | 243.7/h | 0 |
| Kraken | 26.87K | $2.72M | 150.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 827 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.210 | 786 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.198 | 793 | 0.0000 |
| Total TPS moves with Slot time | +0.160 | 793 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.160 | 752 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.158 | 752 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.150 | 774 | 0.0000 |
| Total TPS moves with Program failure rate | +0.149 | 774 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.120 | 752 | 0.0009 |
| Share paying base fee only moves with Activity index | +0.119 | 816 | 0.0006 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 480.37K USD | DeFiLlama: 647.01K USD | -29.56% | *indicative*: 0.74x, within the order-of-magnitude band |
| SOL price | coingecko: 101.35 USD | Jupiter (on-chain DEX): 101.31 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 587.03M SOL | CoinGecko: 587.03M SOL | -0.00% | agree |

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
