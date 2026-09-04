# Solana Ecosystem Report

*Generated 2026-09-04 19:42 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 3.5 robust standard deviations above its 7-day baseline: a 4.2% move to 16,531,135,896.00 USD from a typical 15,862,059,629.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.3K |
| Slot time | 314.1 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1028 (53.62% complete, ~17.5h remaining) |
| Lifetime transactions | 545.2B |
| Circulating supply | 585.4M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,324 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 22,500 / 776,965 lamports |
| Paying no priority fee | 30.00% of 3,234 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 4.00% of slots needed a priority fee (max 1.3M µlam/CU) |
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
| SOL price | $101.67 (-3.56% 24h) |
| Market cap | $59.51B (rank #7) |
| 24h volume | $3.73B |
| ATH | $293.31 (-65.34% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.81B |
| Stablecoin supply | $16.53B |
| DEX volume (24h) | $2.46B (+7.44% 1d) |
| App fees (24h, all protocols) | $11.82M |
| Chain fees (24h) | $594.53K |
| Jito MEV tips (24h) | $120.58K |
| **REV - Real Economic Value (24h)** | **$715.10K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.24B | +2.50% |
| USDT | $2.95B | +3.90% |
| USDGO | $1.36B | +8.49% |
| USD1 | $1.25B | +9.61% |
| BUIDL | $937.90M | +5.80% |
| PYUSD | $857.77M | +24.16% |
| USDG | $582.10M | -6.23% |
| USDe | $534.03M | -0.69% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $838.66M |
| Orca DEX | $279.89M |
| BisonFi | $232.51M |
| Meteora DLMM | $186.49M |
| Raydium AMM | $166.72M |
| Manifest Trade | $158.06M |
| Jupiterz | $99.63M |
| Scorch | $77.86M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.09M |
| fomo Wallet | $1.33M |
| pump.fun | $1.31M |
| Axiom | $781.93K |
| Raydium AMM | $424.45K |
| Sanctum Validator LSTs | $377.64K |
| Meteora DLMM | $374.45K |
| Jupiter Perpetual Exchange | $313.98K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 202 |
| Persistently-active cohort (capture-recapture est.) | 1.9K |
| Unique payers across sampled blocks | 1.1K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $447.28M |
| xStocks 24h DEX volume | $25.19M |
| xStocks holder positions | 314.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.33B |

Top tokenized equities: CRCLX ($74.39M), TSLAX ($66.22M), MSTRX ($61.83M), SPYX ($46.28M), GOOGLX ($29.72M)

## Program activity and chain health

Chain tip lag: **+11.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 58,580 | 43.90% | 0.9 s |
| Pump.fun | 19,556 | 78.60% | 2.5 s |
| Jupiter v6 | 9,328 | 65.90% | 5.7 s |
| Orca Whirlpools | 1,853 | 41.60% | 32.4 s |
| Raydium AMM v4 | 600 | 17.20% | 99.9 s |

Median failure rate across the sampled programs: **43.90%** (range 17.20% to 78.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.34 SOL**.

## Exchange and large-holder balances

11.97M SOL ($1.22B) across 8 publicly-attributed accounts. Net **12K SOL (0.10%) moved off exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $934.19M | 0.6/h | 1 |
| Binance (2) | 1.98M | $200.97M | 1.1K/h | 0 |
| Gate.io | 293.84K | $29.87M | 119.1/h | 0 |
| Bybit | 274.77K | $27.94M | 42.3/h | 0 |
| Bitget | 94.90K | $9.65M | 165.1/h | 0 |
| Coinbase (2) | 91.89K | $9.34M | 418.1/h | 0 |
| Kraken | 24.04K | $2.44M | 202.6/h | 0 |
| Coinbase | 22.75K | $2.31M | 442.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 753 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.266 | 712 | 0.0000 |
| DEX volume moves with App fees | +0.203 | 712 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.193 | 719 | 0.0000 |
| Total TPS moves with Slot time | +0.155 | 719 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.142 | 678 | 0.0002 |
| Total TPS moves with AMM write-lock congestion | +0.141 | 678 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.129 | 718 | 0.0006 |
| Total TPS moves with Activity index | +0.120 | 718 | 0.0012 |
| Slot time moves with AMM write-lock congestion | +0.116 | 678 | 0.0025 |
| AMM write-lock congestion moves with Program failure rate | +0.116 | 678 | 0.0026 |
| Total TPS moves with Program failure rate | +0.110 | 700 | 0.0035 |
| Non-vote TPS moves with Program failure rate | +0.109 | 700 | 0.0039 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 317.13K USD | DeFiLlama: 594.53K USD | -60.85% | *indicative*: 0.53x, within the order-of-magnitude band |
| SOL price | coingecko: 101.67 USD | Jupiter (on-chain DEX): 101.72 USD | -0.05% | agree |
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
