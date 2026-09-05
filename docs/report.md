# Solana Ecosystem Report

*Generated 2026-09-05 10:48 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.0K |
| TPS (non-vote) | 881.5 |
| Slot time | 314.1 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1028 (93.60% complete, ~2.4h remaining) |
| Lifetime transactions | 545.4B |
| Circulating supply | 585.4M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,239 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 31,750 / 290,464 lamports |
| Paying no priority fee | 22.40% of 4,010 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.00% of slots needed a priority fee (max 784.6K µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 18 |
| Delinquent stake | 0.03% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.37% / 24.39% / 35.71% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 24.10% |

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
| SOL price | $102.60 (-1.36% 24h) |
| Market cap | $60.06B (rank #7) |
| 24h volume | $2.80B |
| ATH | $293.31 (-65.02% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.87B |
| Stablecoin supply | $16.34B |
| DEX volume (24h) | $1.85B (-24.89% 1d) |
| App fees (24h, all protocols) | $9.54M |
| Chain fees (24h) | $531.25K |
| Jito MEV tips (24h) | $100.04K |
| **REV - Real Economic Value (24h)** | **$631.28K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.31B | +3.62% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.36B | +8.49% |
| USD1 | $1.26B | +7.84% |
| BUIDL | $977.90M | +10.31% |
| PYUSD | $718.70M | +3.63% |
| USDG | $589.67M | -5.34% |
| USDe | $533.15M | -0.22% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $310.67M |
| BisonFi | $232.51M |
| Orca DEX | $210.00M |
| Meteora DLMM | $180.66M |
| Manifest Trade | $145.24M |
| Raydium AMM | $128.66M |
| Jupiterz | $99.63M |
| Scorch | $77.86M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.84M |
| fomo Wallet | $1.33M |
| pump.fun | $928.13K |
| Axiom | $554.79K |
| Meteora DLMM | $444.50K |
| Raydium AMM | $394.71K |
| Jupiter Perpetual Exchange | $345.18K |
| DEX Screener | $204.37K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 208 |
| Persistently-active cohort (capture-recapture est.) | 2.2K |
| Unique payers across sampled blocks | 1.2K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $447.87M |
| xStocks 24h DEX volume | $24.57M |
| xStocks holder positions | 319.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: CRCLX ($74.60M), TSLAX ($66.75M), MSTRX ($61.74M), SPYX ($46.40M), GOOGLX ($29.81M)

## Program activity and chain health

Chain tip lag: **+11.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 26,552 | 20.10% | 2.2 s |
| Pump.fun | 1,362 | 38.90% | 44 s |
| Jupiter v6 | 1,144 | 46.80% | 52.1 s |
| Orca Whirlpools | 516 | 35.50% | 115.9 s |
| Raydium AMM v4 | 413 | 30.40% | 145.1 s |

Median failure rate across the sampled programs: **35.50%** (range 20.10% to 46.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.34 SOL**.

## Exchange and large-holder balances

11.69M SOL ($1.20B) across 8 publicly-attributed accounts. Net **308K SOL (2.57%) moved off exchanges** over the last 21.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $942.73M | 0.6/h | 1 |
| Binance (2) | 1.80M | $184.33M | 867.5/h | 0 |
| Gate.io | 292.67K | $30.03M | 146.2/h | 0 |
| Bybit | 231.22K | $23.72M | 28.6/h | 0 |
| Bitget | 76.28K | $7.83M | 192.2/h | 0 |
| Coinbase (2) | 53.72K | $5.51M | 210.5/h | 0 |
| Kraken | 34.40K | $3.53M | 158.3/h | 0 |
| Coinbase | 21.06K | $2.16M | 465.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 758 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.274 | 717 | 0.0000 |
| DEX volume moves with App fees | +0.214 | 717 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 724 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 724 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.141 | 683 | 0.0002 |
| Non-vote TPS moves with AMM write-lock congestion | +0.141 | 683 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.130 | 723 | 0.0004 |
| Total TPS moves with Activity index | +0.122 | 723 | 0.0010 |
| Slot time moves with AMM write-lock congestion | +0.116 | 683 | 0.0023 |
| AMM write-lock congestion moves with Program failure rate | +0.114 | 683 | 0.0028 |
| Total TPS moves with Program failure rate | +0.109 | 705 | 0.0038 |
| Non-vote TPS moves with Program failure rate | +0.108 | 705 | 0.0042 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 369.01K USD | DeFiLlama: 531.25K USD | -36.04% | *indicative*: 0.69x, within the order-of-magnitude band |
| SOL price | coingecko: 102.60 USD | Jupiter (on-chain DEX): 102.60 USD | 0.00% | agree |
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

**Latest Agave release:** [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) (2026-09-04)

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
