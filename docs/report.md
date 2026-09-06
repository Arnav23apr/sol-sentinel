# Solana Ecosystem Report

*Generated 2026-09-06 09:01 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.2K |
| Slot time | 316.6 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1029 (52.19% complete, ~18.2h remaining) |
| Lifetime transactions | 545.6B |
| Circulating supply | 585.4M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,350 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 30,323 / 204,500 lamports |
| Paying no priority fee | 30.30% of 2,777 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 1.7M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 17 |
| Delinquent stake | 0.03% |
| Total active stake | 439.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.30% / 24.27% / 35.54% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.97% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.97% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.18% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.67% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.62% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $105.22 (+2.55% 24h) |
| Market cap | $61.60B (rank #7) |
| 24h volume | $3.25B |
| ATH | $293.31 (-64.13% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.92B |
| Stablecoin supply | $16.41B |
| DEX volume (24h) | $1.96B (+4.20% 1d) |
| App fees (24h, all protocols) | $10.48M |
| Chain fees (24h) | $381.12K |
| Jito MEV tips (24h) | $61.04K |
| **REV - Real Economic Value (24h)** | **$442.16K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.35B | +4.97% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.36B | +8.49% |
| USD1 | $1.26B | +6.82% |
| BUIDL | $977.90M | +10.31% |
| PYUSD | $752.12M | +8.30% |
| USDG | $579.74M | -5.64% |
| USDe | $536.19M | +0.32% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $693.23M |
| BisonFi | $251.95M |
| Orca DEX | $129.40M |
| Raydium AMM | $125.28M |
| Manifest Trade | $123.28M |
| Meteora DLMM | $122.38M |
| Jupiterz | $64.61M |
| Scorch | $63.08M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.68M |
| fomo Wallet | $2.13M |
| pump.fun | $679.81K |
| Raydium AMM | $580.46K |
| Meteora DLMM | $458.55K |
| Sanctum Validator LSTs | $380.86K |
| Axiom | $380.52K |
| Collector Crypt | $362.33K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 206 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.2K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $450.35M |
| xStocks 24h DEX volume | $51.03M |
| xStocks holder positions | 324.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: CRCLX ($74.67M), TSLAX ($67.05M), MSTRX ($62.56M), SPYX ($46.53M), GOOGLX ($29.78M)

## Program activity and chain health

Chain tip lag: **+11.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 89,735 (approx.) | 34.70% | 0.6 s |
| Orca Whirlpools | 2,688 | 52.80% | 22.2 s |
| Jupiter v6 | 2,667 | 48.70% | 22.2 s |
| Raydium AMM v4 | 1,645 | 44.00% | 36.4 s |
| Pump.fun | 861 | 10.60% | 69 s |

Median failure rate across the sampled programs: **44.00%** (range 10.60% to 52.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **162.74 SOL**.

## Exchange and large-holder balances

11.77M SOL ($1.24B) across 8 publicly-attributed accounts. Net **73K SOL (0.63%) moved onto exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $966.81M | 0.5/h | 1 |
| Binance (2) | 1.85M | $194.17M | 833.3/h | 0 |
| Gate.io | 319.81K | $33.65M | 435.8/h | 0 |
| Bybit | 227.99K | $23.99M | 24.3/h | 0 |
| Bitget | 99.89K | $10.51M | 236.7/h | 0 |
| Kraken | 30.90K | $3.25M | 191.9/h | 0 |
| Coinbase (2) | 29.13K | $3.07M | 334/h | 0 |
| Coinbase | 26.36K | $2.77M | 169.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 766 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.282 | 725 | 0.0000 |
| DEX volume moves with App fees | +0.223 | 725 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.190 | 732 | 0.0000 |
| Total TPS moves with Slot time | +0.151 | 732 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.140 | 691 | 0.0002 |
| Total TPS moves with AMM write-lock congestion | +0.139 | 691 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.121 | 731 | 0.0010 |
| Slot time moves with AMM write-lock congestion | +0.117 | 691 | 0.0022 |
| Total TPS moves with Program failure rate | +0.115 | 713 | 0.0021 |
| AMM write-lock congestion moves with Program failure rate | +0.115 | 691 | 0.0024 |
| Non-vote TPS moves with Program failure rate | +0.114 | 713 | 0.0023 |
| Total TPS moves with Activity index | +0.112 | 731 | 0.0023 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 252.06K USD | DeFiLlama: 381.12K USD | -40.77% | *indicative*: 0.66x, within the order-of-magnitude band |
| SOL price | coingecko: 105.22 USD | Jupiter (on-chain DEX): 105.21 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 585.45M SOL | CoinGecko: 585.45M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
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
