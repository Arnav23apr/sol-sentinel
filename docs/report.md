# Solana Ecosystem Report

*Generated 2026-09-04 05:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.2K |
| Slot time | 314.1 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1028 (15.33% complete, ~31.9h remaining) |
| Lifetime transactions | 545.0B |
| Circulating supply | 585.4M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,592 lamports (about $0.00058) |
| Transaction fee p90 / p99 | 31,251 / 262,904 lamports |
| Paying no priority fee | 18.70% of 4,427 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 2.70% of slots needed a priority fee (max 547.9K µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 18 |
| Delinquent stake | 0.03% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.37% / 24.39% / 35.71% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.04% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.98% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.74% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.61% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.19% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.69% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.63% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $103.84 (+3.24% 24h) |
| Market cap | $60.79B (rank #7) |
| 24h volume | $4.10B |
| ATH | $293.31 (-64.60% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.91B |
| Stablecoin supply | $16.26B |
| DEX volume (24h) | $2.37B (+3.68% 1d) |
| App fees (24h, all protocols) | $10.91M |
| Chain fees (24h) | $612.58K |
| Jito MEV tips (24h) | $103.50K |
| **REV - Real Economic Value (24h)** | **$716.08K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.04B | -0.28% |
| USDT | $2.95B | +3.90% |
| USDGO | $1.32B | +5.28% |
| USD1 | $1.23B | +7.86% |
| BUIDL | $937.81M | +5.79% |
| PYUSD | $860.18M | +24.52% |
| USDG | $560.03M | -9.77% |
| USDe | $535.61M | -0.36% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $838.66M |
| Orca DEX | $289.05M |
| BisonFi | $232.51M |
| Meteora DLMM | $186.49M |
| Manifest Trade | $172.58M |
| Raydium AMM | $146.98M |
| pump.fun | $75.20M |
| Axiom | $60.26M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.09M |
| pump.fun | $1.31M |
| Axiom | $781.93K |
| fomo Wallet | $582.97K |
| Raydium AMM | $387.53K |
| Sanctum Validator LSTs | $377.64K |
| Jupiter Perpetual Exchange | $313.98K |
| Meteora DLMM | $313.01K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 218 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $458.62M |
| xStocks 24h DEX volume | $31.87M |
| xStocks holder positions | 314.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.16B |

Top tokenized equities: CRCLX ($74.16M), TSLAX ($68.51M), MSTRX ($61.47M), SPYX ($49.15M), GOOGLX ($30.89M)

## Program activity and chain health

Chain tip lag: **+11.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 41,261 | 92.30% | 1.3 s |
| SPL Token | 17,001 | 18.00% | 3.1 s |
| Jupiter v6 | 2,337 | 52.70% | 25.4 s |
| Orca Whirlpools | 1,473 | 34.50% | 40.2 s |
| Raydium AMM v4 | 1,040 | 49.40% | 56.9 s |

Median failure rate across the sampled programs: **49.40%** (range 18.00% to 92.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **568.03 SOL**.

## Exchange and large-holder balances

11.90M SOL ($1.24B) across 8 publicly-attributed accounts. Net **49K SOL (0.41%) moved onto exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $954.13M | 0.7/h | 1 |
| Binance (2) | 1.98M | $205.97M | 821.9/h | 0 |
| Bybit | 316.84K | $32.90M | 27.7/h | 0 |
| Gate.io | 267.93K | $27.82M | 164.7/h | 0 |
| Bitget | 66.31K | $6.89M | 152.5/h | 0 |
| Coinbase | 26.64K | $2.77M | 410.5/h | 0 |
| Coinbase (2) | 26.63K | $2.76M | 485.8/h | 0 |
| Kraken | 25.81K | $2.68M | 152/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 749 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.269 | 708 | 0.0000 |
| DEX volume moves with App fees | +0.197 | 708 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.193 | 715 | 0.0000 |
| Total TPS moves with Slot time | +0.155 | 715 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.144 | 674 | 0.0002 |
| Non-vote TPS moves with AMM write-lock congestion | +0.144 | 674 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.134 | 714 | 0.0003 |
| Total TPS moves with Activity index | +0.126 | 714 | 0.0008 |
| AMM write-lock congestion moves with Program failure rate | +0.119 | 674 | 0.0020 |
| Slot time moves with AMM write-lock congestion | +0.116 | 674 | 0.0025 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 362.88K USD | DeFiLlama: 612.58K USD | -51.19% | *indicative*: 0.59x, within the order-of-magnitude band |
| SOL price | coingecko: 103.84 USD | Jupiter (on-chain DEX): 103.81 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 585.36M SOL | CoinGecko: 585.36M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 - Current Leader Sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-03
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02

**Recently merged SIMDs:**

- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29

**Latest Agave release:** [v4.4.0-alpha.3](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.3) (2026-09-03)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
