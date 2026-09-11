# Solana Ecosystem Report

*Generated 2026-09-11 11:35 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 23.9 robust standard deviations above its 7-day baseline: a 1770.8% move to 0.45 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 1.8K |
| Slot time | 317.5 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1032 (74.77% complete, ~9.6h remaining) |
| Lifetime transactions | 547.4B |
| Circulating supply | 586.5M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,377 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 24,107 / 439,926 lamports |
| Paying no priority fee | 25.90% of 4,501 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 37.30% of slots needed a priority fee (max 8.2M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
| Delinquent validators | 16 |
| Delinquent stake | 0.45% |
| Total active stake | 437.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.32% / 35.64% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.08% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.99% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.60% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.19% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.3M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.57% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $98.87 (-2.49% 24h) |
| Market cap | $58.00B (rank #7) |
| 24h volume | $2.94B |
| ATH | $293.31 (-66.29% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.80B |
| Stablecoin supply | $15.99B |
| DEX volume (24h) | $2.95B (-1.73% 1d) |
| App fees (24h, all protocols) | $14.81M |
| Chain fees (24h) | $709.33K |
| Jito MEV tips (24h) | $128.35K |
| **REV - Real Economic Value (24h)** | **$837.67K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.97B | -2.02% |
| USDT | $2.67B | -9.17% |
| USDGO | $1.38B | +5.13% |
| USD1 | $1.28B | +5.17% |
| BUIDL | $992.51M | +5.83% |
| PYUSD | $715.48M | -16.78% |
| USDG | $596.52M | +6.14% |
| USDe | $536.13M | +0.10% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $468.14M |
| BisonFi | $402.77M |
| Raydium AMM | $396.89M |
| HumidiFi | $285.64M |
| Tessera V | $248.02M |
| Meteora DLMM | $220.43M |
| Orca DEX | $198.15M |
| Manifest Trade | $144.87M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.79M |
| fomo Wallet | $1.52M |
| Raydium AMM | $1.44M |
| Axiom | $1.40M |
| pump.fun | $1.14M |
| Meteora DLMM | $862.62K |
| StonkFun | $759.29K |
| BONK.fun Launchpad | $383.82K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 257 |
| Persistently-active cohort (capture-recapture est.) | 2.7K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $107.77M |
| xStocks holder positions | 506.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

## Program activity and chain health

Chain tip lag: **+11.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 93,543 (approx.) | 35.30% | 0.3 s |
| Raydium AMM v4 | 23,197 | 26.30% | 2.5 s |
| Orca Whirlpools | 11,575 | 59.10% | 5.1 s |
| Jupiter v6 | 3,925 | 55.70% | 15.2 s |
| Pump.fun | 1,871 | 49.10% | 31.8 s |

Median failure rate across the sampled programs: **49.10%** (range 26.30% to 59.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **235.20 SOL**.

## Exchange and large-holder balances

11.75M SOL ($1.16B) across 8 publicly-attributed accounts. Net **73K SOL (0.62%) moved onto exchanges** over the last 20.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $908.46M | 0.3/h | 1 |
| Binance (2) | 1.82M | $179.86M | 2.1K/h | 0 |
| Gate.io | 299.53K | $29.61M | 310.6/h | 0 |
| Bybit | 232.17K | $22.96M | 198.2/h | 0 |
| Coinbase (2) | 113.57K | $11.23M | 328.5/h | 0 |
| Bitget | 44.29K | $4.38M | 281.5/h | 0 |
| Kraken | 30.59K | $3.02M | 422/h | 0 |
| Coinbase | 23.94K | $2.37M | 648.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 801 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.220 | 760 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 767 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 767 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.147 | 726 | 0.0001 |
| Non-vote TPS moves with AMM write-lock congestion | +0.147 | 726 | 0.0001 |
| Total TPS moves with Program failure rate | +0.125 | 748 | 0.0006 |
| Non-vote TPS moves with Program failure rate | +0.125 | 748 | 0.0006 |
| Share paying base fee only moves with Activity index | +0.113 | 790 | 0.0015 |
| Slot time moves with AMM write-lock congestion | +0.110 | 726 | 0.0030 |
| Non-vote TPS moves with Activity index | +0.103 | 766 | 0.0043 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 559.50K USD | DeFiLlama: 709.33K USD | -23.62% | *indicative*: 0.79x, within the order-of-magnitude band |
| SOL price | coingecko: 98.87 USD | Jupiter (on-chain DEX): 98.82 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 586.54M SOL | CoinGecko: 586.54M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-11
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-09
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02

**Recently merged SIMDs:**

- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08
- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12

**Latest Agave release:** [v4.4.0-alpha.4](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.4) (2026-09-10)

**Latest Firedancer release:** [v26.08.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.4) (2026-09-10)

## Ecosystem news

- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
