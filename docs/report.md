# Solana Ecosystem Report

*Generated 2026-08-26 04:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.4K |
| Slot time | 363.6 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1022 (65.75% complete, ~14.9h remaining) |
| Lifetime transactions | 541.9B |
| Circulating supply | 583.4M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,730 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 22,614 / 505,000 lamports |
| Paying no priority fee | 17.50% of 7,705 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 6.00% of slots needed a priority fee (max 769.5K µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 684 |
| Delinquent validators | 11 |
| Delinquent stake | 0.12% |
| Total active stake | 434.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.26% / 24.31% / 35.67% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 24.18% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.69% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 4 | `Catz…Diqb` | 11.7M | 2.70% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.05% | 10% |
| 7 | `8Gbw…F8iD` | 8.6M | 1.97% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.68% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $97.10 (-4.32% 24h) |
| Market cap | $56.64B (rank #7) |
| 24h volume | $4.31B |
| ATH | $293.31 (-66.90% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.60B |
| Stablecoin supply | $15.96B |
| DEX volume (24h) | $2.95B (-1.58% 1d) |
| App fees (24h, all protocols) | $13.01M |
| Chain fees (24h) | $889.16K |
| Jito MEV tips (24h) | $210.36K |
| **REV - Real Economic Value (24h)** | **$1.10M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.07B | +4.40% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.24B | +4.34% |
| USD1 | $1.11B | +5.61% |
| BUIDL | $876.38M | +18.20% |
| PYUSD | $678.97M | +0.32% |
| USDG | $628.74M | -0.59% |
| USDe | $536.91M | -0.11% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $567.89M |
| Orca DEX | $424.69M |
| BisonFi | $411.40M |
| Meteora DLMM | $246.36M |
| Scorch | $218.92M |
| Raydium AMM | $181.86M |
| Manifest Trade | $157.26M |
| pump.fun | $112.18M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.81M |
| pump.fun | $1.95M |
| Axiom | $1.60M |
| Jupiter Perpetual Exchange | $631.25K |
| fomo Wallet | $585.96K |
| Meteora DLMM | $507.74K |
| Raydium AMM | $296.78K |
| Phantom Wallet | $295.72K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 308 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $429.38M |
| xStocks 24h DEX volume | $22.43M |
| xStocks holder positions | 276.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.06B |

Top tokenized equities: CRCLX ($66.62M), TSLAX ($63.93M), MSTRX ($49.83M), SPYX ($48.15M), GOOGLX ($31.01M)

## Program activity and chain health

Chain tip lag: **+13.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 36,840 | 30.50% | 1.5 s |
| Pump.fun | 12,404 | 61.90% | 4.4 s |
| Raydium AMM v4 | 4,845 | 52.40% | 12 s |
| Orca Whirlpools | 3,972 | 59.40% | 14.9 s |
| Jupiter v6 | 3,098 | 43.30% | 19.3 s |

Median failure rate across the sampled programs: **52.40%** (range 30.50% to 61.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.31 SOL**.

## Exchange and large-holder balances

12.66M SOL ($1.23B) across 8 publicly-attributed accounts. Net **407K SOL (3.12%) moved off exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.41M | $913.58M | 1.1/h | 9 |
| Binance (2) | 2.35M | $228.29M | 827.6/h | 0 |
| Bybit | 377.26K | $36.63M | 53.9/h | 0 |
| Gate.io | 357.38K | $34.70M | 187.3/h | 0 |
| Bitget | 66.06K | $6.41M | 176.5/h | 0 |
| Kraken | 43.30K | $4.20M | 174.6/h | 0 |
| Coinbase | 35.99K | $3.49M | 355.4/h | 0 |
| Coinbase (2) | 18.74K | $1.82M | 769.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 9 of 117 tested pairs survive, over 688 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.216 | 647 | 0.0000 |
| DEX volume moves with App fees | +0.201 | 647 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.188 | 654 | 0.0000 |
| Total TPS moves with Slot time | +0.151 | 654 | 0.0001 |
| AMM write-lock congestion moves with Program failure rate | +0.124 | 613 | 0.0021 |
| Non-vote TPS moves with AMM write-lock congestion | +0.122 | 613 | 0.0025 |
| Total TPS moves with AMM write-lock congestion | +0.120 | 613 | 0.0030 |
| Non-vote TPS moves with Activity index | +0.120 | 653 | 0.0021 |
| Slot time moves with AMM write-lock congestion | +0.117 | 613 | 0.0038 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 750.92K USD | DeFiLlama: 889.16K USD | -16.86% | *indicative*: 0.84x, within the order-of-magnitude band |
| SOL price | coingecko: 97.10 USD | Jupiter (on-chain DEX): 97.11 USD | -0.01% | agree |
| Circulating supply | getSupply (RPC): 583.38M SOL | CoinGecko: 583.38M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-08-25
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-08-25
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-25
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-25
- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-25
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-24

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
