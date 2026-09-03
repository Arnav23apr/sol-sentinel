# Solana Ecosystem Report

*Generated 2026-09-03 20:15 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.9K |
| TPS (non-vote) | 2.7K |
| Slot time | 316.6 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1027 (91.65% complete, ~3.2h remaining) |
| Lifetime transactions | 544.9B |
| Circulating supply | 585.3M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,480 lamports (about $0.00058) |
| Transaction fee p90 / p99 | 33,839 / 955,000 lamports |
| Paying no priority fee | 25.30% of 3,727 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 12.70% of slots needed a priority fee (max 6.4M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 19 |
| Delinquent stake | 0.05% |
| Total active stake | 438.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.25% / 35.53% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.96% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.3M | 3.96% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.3M | 2.58% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.18% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.2M | 1.65% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.63% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $105.29 (+5.69% 24h) |
| Market cap | $61.63B (rank #7) |
| 24h volume | $4.05B |
| ATH | $293.31 (-64.10% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.97B |
| Stablecoin supply | $16.04B |
| DEX volume (24h) | $2.29B (+5.42% 1d) |
| App fees (24h, all protocols) | $10.54M |
| Chain fees (24h) | $612.58K |
| Jito MEV tips (24h) | $105.96K |
| **REV - Real Economic Value (24h)** | **$718.54K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.88B | -1.37% |
| USDT | $2.95B | +3.90% |
| USDGO | $1.32B | +5.28% |
| USD1 | $1.22B | +7.68% |
| BUIDL | $890.78M | +0.50% |
| PYUSD | $819.34M | +19.64% |
| USDG | $596.39M | -2.86% |
| USDe | $536.20M | -0.18% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $1.02B |
| Orca DEX | $267.01M |
| BisonFi | $194.35M |
| Manifest Trade | $184.75M |
| Raydium AMM | $147.77M |
| Meteora DLMM | $137.83M |
| pump.fun | $83.17M |
| Axiom | $60.26M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.72M |
| pump.fun | $1.46M |
| Axiom | $893.14K |
| fomo Wallet | $582.97K |
| Raydium AMM | $387.25K |
| Sanctum Validator LSTs | $364.05K |
| pump.fun Mobile App | $317.34K |
| Meteora DLMM | $313.01K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 226 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $462.50M |
| xStocks 24h DEX volume | $36.95M |
| xStocks holder positions | 314.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.11B |

Top tokenized equities: CRCLX ($74.75M), TSLAX ($70.86M), MSTRX ($62.14M), SPYX ($49.14M), GOOGLX ($30.80M)

## Program activity and chain health

Chain tip lag: **+11.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 79,785 (approx.) | 35.80% | 0.6 s |
| Pump.fun | 20,173 | 85.30% | 2.8 s |
| Orca Whirlpools | 6,984 | 53.80% | 8.5 s |
| Raydium AMM v4 | 4,872 | 25.40% | 12 s |
| Jupiter v6 | 4,028 | 60.60% | 14.9 s |

Median failure rate across the sampled programs: **53.80%** (range 25.40% to 85.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.34 SOL**.

## Exchange and large-holder balances

11.98M SOL ($1.26B) across 8 publicly-attributed accounts. Net **187K SOL (1.58%) moved onto exchanges** over the last 21.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $967.45M | 0.7/h | 1 |
| Binance (2) | 2.03M | $213.80M | 1.4K/h | 0 |
| Bybit | 315.40K | $33.21M | 34.6/h | 0 |
| Gate.io | 277.21K | $29.19M | 166.7/h | 0 |
| Bitget | 59.90K | $6.31M | 227.7/h | 0 |
| Coinbase | 44.19K | $4.65M | 655.7/h | 0 |
| Kraken | 33.17K | $3.49M | 321.7/h | 0 |
| Coinbase (2) | 30.44K | $3.21M | 618.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 746 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.264 | 705 | 0.0000 |
| DEX volume moves with App fees | +0.200 | 705 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.195 | 712 | 0.0000 |
| Total TPS moves with Slot time | +0.156 | 712 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.146 | 671 | 0.0001 |
| Non-vote TPS moves with AMM write-lock congestion | +0.146 | 671 | 0.0001 |
| Non-vote TPS moves with Activity index | +0.134 | 711 | 0.0003 |
| Total TPS moves with Activity index | +0.126 | 711 | 0.0008 |
| AMM write-lock congestion moves with Program failure rate | +0.117 | 671 | 0.0024 |
| Slot time moves with AMM write-lock congestion | +0.114 | 671 | 0.0030 |
| Total TPS moves with Program failure rate | +0.109 | 693 | 0.0039 |
| Non-vote TPS moves with Program failure rate | +0.108 | 693 | 0.0044 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (0 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 2.49M USD | DeFiLlama: 612.58K USD | +121.04% | *indicative*: 4.07x, outside the order-of-magnitude band |
| SOL price | coingecko: 105.29 USD | Jupiter (on-chain DEX): 105.27 USD | +0.02% | agree |
| Circulating supply | getSupply (RPC): 585.27M SOL | CoinGecko: 585.27M SOL | -0.00% | agree |

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
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Solana Treasury DeFi Development Corp Eyes $20 Million Raise to Buy More SOL](https://decrypt.co/377068/defi-development-corp-20-million-raise-more-solana)** - Decrypt, 2026-09-01
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
