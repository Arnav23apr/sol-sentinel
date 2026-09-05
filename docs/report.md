# Solana Ecosystem Report

*Generated 2026-09-05 01:51 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.1K |
| Slot time | 312.5 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1028 (69.88% complete, ~11.3h remaining) |
| Lifetime transactions | 545.3B |
| Circulating supply | 585.4M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,164 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 24,637 / 325,124 lamports |
| Paying no priority fee | 29.30% of 4,523 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 4.00% of slots needed a priority fee (max 1.1M µlam/CU) |
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
| SOL price | $102.02 (-1.36% 24h) |
| Market cap | $59.72B (rank #7) |
| 24h volume | $3.27B |
| ATH | $293.31 (-65.22% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.86B |
| Stablecoin supply | $16.30B |
| DEX volume (24h) | $1.85B (-24.83% 1d) |
| App fees (24h, all protocols) | $10.60M |
| Chain fees (24h) | $594.53K |
| Jito MEV tips (24h) | $109.77K |
| **REV - Real Economic Value (24h)** | **$704.29K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.28B | +3.10% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.36B | +8.49% |
| USD1 | $1.25B | +9.61% |
| BUIDL | $977.90M | +10.32% |
| PYUSD | $720.29M | +4.27% |
| USDG | $581.86M | -6.28% |
| USDe | $533.36M | -0.81% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $310.67M |
| Orca DEX | $243.78M |
| BisonFi | $232.51M |
| Meteora DLMM | $180.66M |
| Manifest Trade | $161.55M |
| Raydium AMM | $151.57M |
| Jupiterz | $99.63M |
| Scorch | $77.86M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.84M |
| fomo Wallet | $1.33M |
| pump.fun | $928.13K |
| Axiom | $554.79K |
| Raydium AMM | $407.48K |
| Sanctum Validator LSTs | $377.64K |
| Meteora DLMM | $374.45K |
| Jupiter Perpetual Exchange | $345.18K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 266 |
| Persistently-active cohort (capture-recapture est.) | 3.4K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $448.13M |
| xStocks 24h DEX volume | $25.43M |
| xStocks holder positions | 318.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: CRCLX ($74.80M), TSLAX ($66.50M), MSTRX ($61.88M), SPYX ($46.33M), GOOGLX ($29.79M)

## Program activity and chain health

Chain tip lag: **+12.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 47,616 | 34.80% | 1.2 s |
| Pump.fun | 7,033 | 71.70% | 8.4 s |
| Jupiter v6 | 1,293 | 48.20% | 44.7 s |
| Orca Whirlpools | 1,178 | 27.70% | 50.6 s |
| Raydium AMM v4 | 594 | 37.30% | 100 s |

Median failure rate across the sampled programs: **37.30%** (range 27.70% to 71.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.34 SOL**.

## Exchange and large-holder balances

11.70M SOL ($1.19B) across 8 publicly-attributed accounts. Net **203K SOL (1.71%) moved off exchanges** over the last 20.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $937.41M | 0.6/h | 1 |
| Binance (2) | 1.79M | $182.36M | 689.7/h | 0 |
| Gate.io | 280.43K | $28.61M | 132/h | 0 |
| Bybit | 263.69K | $26.90M | 32.6/h | 0 |
| Bitget | 71.43K | $7.29M | 145.2/h | 0 |
| Coinbase (2) | 58.56K | $5.97M | 466.3/h | 0 |
| Kraken | 26.56K | $2.71M | 152.9/h | 0 |
| Coinbase | 22.42K | $2.29M | 587.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 756 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.272 | 715 | 0.0000 |
| DEX volume moves with App fees | +0.209 | 715 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 722 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 722 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.142 | 681 | 0.0002 |
| Non-vote TPS moves with AMM write-lock congestion | +0.142 | 681 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.128 | 721 | 0.0006 |
| Total TPS moves with Activity index | +0.120 | 721 | 0.0012 |
| Slot time moves with AMM write-lock congestion | +0.116 | 681 | 0.0024 |
| AMM write-lock congestion moves with Program failure rate | +0.115 | 681 | 0.0027 |
| Total TPS moves with Program failure rate | +0.108 | 703 | 0.0042 |
| Non-vote TPS moves with Program failure rate | +0.106 | 703 | 0.0048 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 425.77K USD | DeFiLlama: 594.53K USD | -33.08% | *indicative*: 0.72x, within the order-of-magnitude band |
| SOL price | coingecko: 102.02 USD | Jupiter (on-chain DEX): 102.05 USD | -0.03% | agree |
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
