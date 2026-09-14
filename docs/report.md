# Solana Ecosystem Report

*Generated 2026-09-14 02:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **DEX volume (24h)** (warning): DEX volume (24h) is 3.8 robust standard deviations below its 7-day baseline: a 41.5% move to 1,637,064,258.00 USD from a typical 2,796,332,495.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 1.9K |
| Slot time | 316.6 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1034 (39.61% complete, ~22.9h remaining) |
| Lifetime transactions | 548.2B |
| Circulating supply | 586.9M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,499 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 25,000 / 441,195 lamports |
| Paying no priority fee | 22.50% of 4,030 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 47.30% of slots needed a priority fee (max 47.5M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 12 |
| Delinquent stake | 0.44% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 24.40% / 35.67% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.09% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.02% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.75% | 0% |
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
| SOL price | $100.21 (-1.87% 24h) |
| Market cap | $58.80B (rank #7) |
| 24h volume | $2.17B |
| ATH | $293.31 (-65.84% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.82B |
| Stablecoin supply | $16.04B |
| DEX volume (24h) | $1.64B (-6.11% 1d) |
| App fees (24h, all protocols) | $14.05M |
| Chain fees (24h) | $608.10K |
| Jito MEV tips (24h) | $95.85K |
| **REV - Real Economic Value (24h)** | **$703.95K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.20B | -2.16% |
| USDT | $2.48B | -10.12% |
| USDGO | $1.38B | +2.02% |
| USD1 | $1.31B | +3.76% |
| BUIDL | $992.60M | +1.50% |
| PYUSD | $707.25M | -5.47% |
| USDG | $599.69M | +2.15% |
| USDe | $532.41M | -0.44% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $315.70M |
| Raydium AMM | $264.96M |
| fomo Wallet | $169.82M |
| BisonFi | $162.68M |
| Meteora DLMM | $157.73M |
| Orca DEX | $105.15M |
| HumidiFi | $85.03M |
| Tessera V | $81.22M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.19M |
| pump.fun | $1.55M |
| fomo Wallet | $1.18M |
| Axiom | $1.17M |
| Raydium AMM | $963.65K |
| Meteora DLMM | $838.46K |
| StonkFun | $662.72K |
| Collector Crypt | $538.38K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 245 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $76.30M |
| xStocks holder positions | 535.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.93B |

## Program activity and chain health

Chain tip lag: **+10.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 83,386 (approx.) | 51.90% | 0.6 s |
| Raydium AMM v4 | 13,076 | 50.90% | 4.4 s |
| Pump.fun | 9,286 | 76.30% | 6.3 s |
| Jupiter v6 | 7,005 | 71.40% | 8.5 s |
| Orca Whirlpools | 5,810 | 54.20% | 10.1 s |

Median failure rate across the sampled programs: **54.20%** (range 50.90% to 76.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.19K SOL**.

## Exchange and large-holder balances

11.71M SOL ($1.17B) across 8 publicly-attributed accounts. Net **46K SOL (0.39%) moved onto exchanges** over the last 19.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $920.77M | 0.3/h | 1 |
| Binance (2) | 1.89M | $189.63M | 736.2/h | 0 |
| Gate.io | 298.05K | $29.87M | 209.7/h | 1 |
| Bybit | 232.08K | $23.26M | 44.4/h | 0 |
| Bitget | 28.60K | $2.87M | 170.3/h | 0 |
| Kraken | 27.31K | $2.74M | 272.3/h | 0 |
| Coinbase (2) | 23.27K | $2.33M | 361.4/h | 0 |
| Coinbase | 23.20K | $2.32M | 328.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 821 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.216 | 780 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.190 | 787 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.155 | 746 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.153 | 746 | 0.0000 |
| Total TPS moves with Slot time | +0.152 | 787 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.140 | 768 | 0.0001 |
| Total TPS moves with Program failure rate | +0.139 | 768 | 0.0001 |
| Slot time moves with AMM write-lock congestion | +0.121 | 746 | 0.0009 |
| Share paying base fee only moves with Activity index | +0.119 | 810 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 437.10K USD | DeFiLlama: 608.10K USD | -32.72% | *indicative*: 0.72x, within the order-of-magnitude band |
| SOL price | coingecko: 100.21 USD | Jupiter (on-chain DEX): 100.48 USD | -0.27% | agree |
| Circulating supply | getSupply (RPC): 586.89M SOL | CoinGecko: 586.89M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-11
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11

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
