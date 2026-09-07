# Solana Ecosystem Report

*Generated 2026-09-07 04:58 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.3K |
| Slot time | 315.8 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1030 (4.63% complete, ~36.1h remaining) |
| Lifetime transactions | 545.9B |
| Circulating supply | 586.2M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,356 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 20,000 / 410,000 lamports |
| Paying no priority fee | 25.80% of 4,125 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 16.00% of slots needed a priority fee (max 65.2M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 11 |
| Delinquent stake | 0.01% |
| Total active stake | 439.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.30% / 24.19% / 35.46% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.94% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.97% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.18% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.09% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.56% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $105.07 (-0.70% 24h) |
| Market cap | $61.58B (rank #7) |
| 24h volume | $3.81B |
| ATH | $293.31 (-64.18% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.92B |
| Stablecoin supply | $16.44B |
| DEX volume (24h) | $1.96B (+4.20% 1d) |
| App fees (24h, all protocols) | $10.48M |
| Chain fees (24h) | $381.12K |
| Jito MEV tips (24h) | $61.04K |
| **REV - Real Economic Value (24h)** | **$442.16K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.38B | +8.52% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.36B | +8.49% |
| USD1 | $1.26B | +5.20% |
| BUIDL | $977.90M | +10.31% |
| PYUSD | $748.31M | +8.02% |
| USDG | $583.25M | -4.49% |
| USDe | $534.96M | -0.41% |

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
| Activity index: unique fee payers per block (24h sampled avg) | 241 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $450.35M |
| xStocks 24h DEX volume | $99.88M |
| xStocks holder positions | 349.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: CRCLX ($74.67M), TSLAX ($67.05M), MSTRX ($62.56M), SPYX ($46.53M), GOOGLX ($29.78M)

## Program activity and chain health

Chain tip lag: **+11.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,733 | 18.30% | 1.6 s |
| Orca Whirlpools | 4,288 | 30.30% | 13.9 s |
| Raydium AMM v4 | 3,666 | 23.00% | 16.1 s |
| Pump.fun | 2,445 | 43.90% | 24.3 s |
| Jupiter v6 | 2,090 | 44.00% | 28.4 s |

Median failure rate across the sampled programs: **30.30%** (range 18.30% to 44.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **580.97 SOL**.

## Exchange and large-holder balances

11.76M SOL ($1.24B) across 8 publicly-attributed accounts. Net **4K SOL (0.03%) moved off exchanges** over the last 20.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $965.43M | 0.5/h | 1 |
| Binance (2) | 1.88M | $198.02M | 1.0K/h | 0 |
| Gate.io | 302.40K | $31.77M | 279.9/h | 0 |
| Bybit | 210.81K | $22.15M | 31.8/h | 0 |
| Bitget | 69.26K | $7.28M | 225.7/h | 0 |
| Kraken | 41.03K | $4.31M | 218.2/h | 0 |
| Coinbase (2) | 35.79K | $3.76M | 326.7/h | 0 |
| Coinbase | 31.58K | $3.32M | 290.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 773 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.282 | 732 | 0.0000 |
| DEX volume moves with App fees | +0.223 | 732 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.188 | 739 | 0.0000 |
| Total TPS moves with Slot time | +0.150 | 739 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.142 | 698 | 0.0002 |
| Total TPS moves with AMM write-lock congestion | +0.141 | 698 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.122 | 738 | 0.0009 |
| Total TPS moves with Program failure rate | +0.118 | 720 | 0.0016 |
| Non-vote TPS moves with Program failure rate | +0.117 | 720 | 0.0017 |
| Slot time moves with AMM write-lock congestion | +0.114 | 698 | 0.0025 |
| Total TPS moves with Activity index | +0.113 | 738 | 0.0021 |
| AMM write-lock congestion moves with Program failure rate | +0.113 | 698 | 0.0027 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 385.54K USD | DeFiLlama: 381.12K USD | +1.15% | *indicative*: 1.01x, within the order-of-magnitude band |
| SOL price | coingecko: 105.07 USD | Jupiter (on-chain DEX): 105.11 USD | -0.04% | agree |
| Circulating supply | getSupply (RPC): 586.17M SOL | CoinGecko: 586.17M SOL | -0.00% | agree |

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

- **[STONK surges 250% to $140 million market cap as stock-paired Solana launchpad StonkFun pulls volume to Raydium and Jupiter](https://www.theblock.co/news/defi/2026-09-06-stonk-surges-250-to-140-million-market-cap-as-stock-paired-solana-launchpad-stonkfun-pulls-volume-to-raydium-and-jupiter-413621)** - The Block, 2026-09-06
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
