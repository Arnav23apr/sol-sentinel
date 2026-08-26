# Solana Ecosystem Report

*Generated 2026-08-26 14:33 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.9K |
| Slot time | 365.9 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1022 (88.75% complete, ~4.9h remaining) |
| Lifetime transactions | 542.1B |
| Circulating supply | 583.4M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,527 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 25,001 / 720,353 lamports |
| Paying no priority fee | 22.50% of 5,026 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 15.30% of slots needed a priority fee (max 1.1M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 10 |
| Delinquent stake | 0.06% |
| Total active stake | 434.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.25% / 24.29% / 35.64% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 24.17% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
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
| SOL price | $96.30 (-1.89% 24h) |
| Market cap | $56.17B (rank #7) |
| 24h volume | $3.06B |
| ATH | $293.31 (-67.17% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.60B |
| Stablecoin supply | $15.89B |
| DEX volume (24h) | $2.93B (-2.04% 1d) |
| App fees (24h, all protocols) | $13.24M |
| Chain fees (24h) | $889.16K |
| Jito MEV tips (24h) | $209.84K |
| **REV - Real Economic Value (24h)** | **$1.10M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.99B | +3.24% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.25B | +5.18% |
| USD1 | $1.11B | +5.95% |
| BUIDL | $876.38M | +18.20% |
| PYUSD | $688.68M | +1.77% |
| USDG | $615.25M | -2.73% |
| USDe | $536.95M | -0.11% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $567.89M |
| BisonFi | $411.40M |
| Orca DEX | $285.77M |
| Meteora DLMM | $246.36M |
| Scorch | $173.07M |
| Raydium AMM | $151.86M |
| Manifest Trade | $132.67M |
| pump.fun | $112.18M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.81M |
| pump.fun | $1.95M |
| Axiom | $1.60M |
| Bags | $1.45M |
| fomo Wallet | $664.84K |
| Jupiter Perpetual Exchange | $631.25K |
| Meteora DLMM | $507.74K |
| Phantom Wallet | $274.91K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 255 |
| Persistently-active cohort (capture-recapture est.) | 2.7K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $427.37M |
| xStocks 24h DEX volume | $20.51M |
| xStocks holder positions | 277.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.06B |

Top tokenized equities: CRCLX ($65.77M), TSLAX ($63.69M), MSTRX ($49.23M), SPYX ($48.19M), GOOGLX ($31.07M)

## Program activity and chain health

Chain tip lag: **+13.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 68,461 (approx.) | 36.50% | 0.7 s |
| Pump.fun | 36,936 | 86.80% | 1.5 s |
| Jupiter v6 | 5,236 | 59.70% | 11 s |
| Raydium AMM v4 | 2,822 | 48.90% | 21.2 s |
| Orca Whirlpools | 2,169 | 53.10% | 27.4 s |

Median failure rate across the sampled programs: **53.10%** (range 36.50% to 86.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.31 SOL**.

## Exchange and large-holder balances

12.41M SOL ($1.19B) across 8 publicly-attributed accounts. Net **388K SOL (3.03%) moved off exchanges** over the last 23.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.41M | $906.05M | 1.1/h | 9 |
| Binance (2) | 2.07M | $199.64M | 1.8K/h | 0 |
| Gate.io | 387.94K | $37.36M | 260.7/h | 0 |
| Bybit | 377.26K | $36.33M | 72.2/h | 0 |
| Bitget | 68.31K | $6.58M | 245.7/h | 0 |
| Kraken | 38.86K | $3.74M | 276.3/h | 0 |
| Coinbase (2) | 27.77K | $2.67M | 462.7/h | 0 |
| Coinbase | 25.67K | $2.47M | 645.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 6 of 117 tested pairs survive, over 701 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.214 | 660 | 0.0000 |
| DEX volume moves with App fees | +0.199 | 660 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.189 | 667 | 0.0000 |
| Total TPS moves with Slot time | +0.152 | 667 | 0.0001 |
| AMM write-lock congestion moves with Program failure rate | +0.121 | 626 | 0.0024 |
| Non-vote TPS moves with Activity index | +0.117 | 666 | 0.0025 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 479.74K USD | DeFiLlama: 889.16K USD | -59.82% | *indicative*: 0.54x, within the order-of-magnitude band |
| SOL price | coingecko: 96.30 USD | Jupiter (on-chain DEX): 95.94 USD | +0.37% | agree |
| Circulating supply | getSupply (RPC): 583.38M SOL | CoinGecko: 583.38M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-08-26
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-08-25
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26
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

- **[SOL treasury firm DeFi Development launches real-time ‘State of Solana’ intelligence platform](https://www.theblock.co/news/markets/2026-08-26-sol-treasury-firm-defi-development-launches-real-time-state-of-solana-intelligence-platform-412798)** - The Block, 2026-08-26
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
