# Solana Ecosystem Report

*Generated 2026-09-05 18:26 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.3K |
| Slot time | 315 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1029 (13.77% complete, ~32.6h remaining) |
| Lifetime transactions | 545.5B |
| Circulating supply | 585.4M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,351 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 18,800 / 125,000 lamports |
| Paying no priority fee | 31.10% of 3,146 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 13.30% of slots needed a priority fee (max 8.1M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 17 |
| Delinquent stake | 0.02% |
| Total active stake | 439.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.30% / 24.27% / 35.53% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.96% |

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
| SOL price | $104.05 (+2.51% 24h) |
| Market cap | $60.90B (rank #7) |
| 24h volume | $2.31B |
| ATH | $293.31 (-64.53% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.90B |
| Stablecoin supply | $16.37B |
| DEX volume (24h) | $1.88B (-23.50% 1d) |
| App fees (24h, all protocols) | $10.44M |
| Chain fees (24h) | $531.25K |
| Jito MEV tips (24h) | $64.82K |
| **REV - Real Economic Value (24h)** | **$596.07K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.30B | +3.59% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.36B | +8.49% |
| USD1 | $1.26B | +7.84% |
| BUIDL | $977.90M | +10.31% |
| PYUSD | $754.41M | +8.78% |
| USDG | $586.20M | -5.90% |
| USDe | $536.48M | +0.37% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $310.67M |
| BisonFi | $251.95M |
| Meteora DLMM | $180.66M |
| Manifest Trade | $123.44M |
| Orca DEX | $114.75M |
| Raydium AMM | $113.08M |
| Jupiterz | $64.61M |
| Scorch | $63.08M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.84M |
| fomo Wallet | $2.13M |
| pump.fun | $928.13K |
| Axiom | $554.79K |
| Meteora DLMM | $444.50K |
| Raydium AMM | $427.56K |
| Jupiter Perpetual Exchange | $345.18K |
| Collector Crypt | $300.67K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 227 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $450.01M |
| xStocks 24h DEX volume | $15.81M |
| xStocks holder positions | 319.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: CRCLX ($74.80M), TSLAX ($66.88M), MSTRX ($62.81M), SPYX ($46.45M), GOOGLX ($29.86M)

## Program activity and chain health

Chain tip lag: **+11.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 41,714 | 22.00% | 1.3 s |
| Pump.fun | 6,503 | 69.70% | 8.8 s |
| Jupiter v6 | 3,158 | 59.60% | 18 s |
| Orca Whirlpools | 1,876 | 36.50% | 31.8 s |
| Raydium AMM v4 | 1,803 | 22.70% | 33.1 s |

Median failure rate across the sampled programs: **36.50%** (range 22.00% to 69.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **172.42 SOL**.

## Exchange and large-holder balances

11.83M SOL ($1.23B) across 8 publicly-attributed accounts. Net **139K SOL (1.16%) moved off exchanges** over the last 22.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $956.06M | 0.5/h | 1 |
| Binance (2) | 1.91M | $199.05M | 1.3K/h | 0 |
| Gate.io | 288.09K | $29.98M | 141/h | 0 |
| Bybit | 227.99K | $23.72M | 17.1/h | 0 |
| Bitget | 94.00K | $9.78M | 193/h | 0 |
| Kraken | 50.61K | $5.27M | 289.2/h | 0 |
| Coinbase (2) | 39.77K | $4.14M | 482.6/h | 0 |
| Coinbase | 26.33K | $2.74M | 533.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 761 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.279 | 720 | 0.0000 |
| DEX volume moves with App fees | +0.219 | 720 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 727 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 727 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.139 | 686 | 0.0003 |
| Total TPS moves with AMM write-lock congestion | +0.138 | 686 | 0.0003 |
| Non-vote TPS moves with Activity index | +0.130 | 726 | 0.0005 |
| Total TPS moves with Activity index | +0.121 | 726 | 0.0011 |
| Slot time moves with AMM write-lock congestion | +0.116 | 686 | 0.0022 |
| AMM write-lock congestion moves with Program failure rate | +0.115 | 686 | 0.0025 |
| Total TPS moves with Program failure rate | +0.108 | 708 | 0.0039 |
| Non-vote TPS moves with Program failure rate | +0.108 | 708 | 0.0042 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 211.85K USD | DeFiLlama: 531.25K USD | -85.96% | *indicative*: 0.40x, within the order-of-magnitude band |
| SOL price | coingecko: 104.05 USD | Jupiter (on-chain DEX): 103.95 USD | +0.10% | agree |
| Circulating supply | getSupply (RPC): 585.45M SOL | CoinGecko: 585.45M SOL | -0.00% | agree |

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
