# Solana Ecosystem Report

*Generated 2026-09-02 22:43 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 1.5K |
| Slot time | 315 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1027 (34.68% complete, ~24.7h remaining) |
| Lifetime transactions | 544.6B |
| Circulating supply | 585.3M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,502 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 67,600 / 605,000 lamports |
| Paying no priority fee | 28.10% of 4,048 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 3.30% of slots needed a priority fee (max 356.8K µlam/CU) |
| Node version (RPC) | 4.2.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 19 |
| Delinquent stake | 0.09% |
| Total active stake | 438.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.30% / 24.26% / 35.54% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.96% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.3M | 3.96% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
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
| SOL price | $99.61 (+0.22% 24h) |
| Market cap | $58.29B (rank #7) |
| 24h volume | $2.90B |
| ATH | $293.31 (-66.04% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.69B |
| Stablecoin supply | $15.72B |
| DEX volume (24h) | $2.17B (-13.19% 1d) |
| App fees (24h, all protocols) | $12.65M |
| Chain fees (24h) | $899.77K |
| Jito MEV tips (24h) | $118.37K |
| **REV - Real Economic Value (24h)** | **$1.02M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.71B | -4.68% |
| USDT | $2.90B | +2.49% |
| USDGO | $1.25B | +1.21% |
| USD1 | $1.21B | +8.62% |
| BUIDL | $890.69M | +1.63% |
| PYUSD | $785.61M | +15.71% |
| USDG | $611.06M | -2.87% |
| USDe | $535.76M | -0.17% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $827.37M |
| BisonFi | $204.83M |
| Orca DEX | $200.27M |
| Manifest Trade | $163.16M |
| Meteora DLMM | $139.98M |
| Raydium AMM | $123.83M |
| Axiom | $97.98M |
| Scorch | $64.72M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.44M |
| pump.fun | $1.74M |
| Axiom | $1.37M |
| fomo Wallet | $1.35M |
| Raydium AMM | $366.72K |
| Meteora DLMM | $364.50K |
| pump.fun Mobile App | $318.69K |
| Collector Crypt | $244.66K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 260 |
| Persistently-active cohort (capture-recapture est.) | 3.4K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $433.88M |
| xStocks 24h DEX volume | $27.44M |
| xStocks holder positions | 311.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: TSLAX ($66.24M), CRCLX ($65.29M), MSTRX ($53.11M), SPYX ($48.67M), GOOGLX ($30.49M)

## Program activity and chain health

Chain tip lag: **+12.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 30,984 | 87.90% | 1.9 s |
| SPL Token | 28,159 | 11.90% | 1.9 s |
| Jupiter v6 | 3,572 | 38.70% | 16.7 s |
| Raydium AMM v4 | 1,228 | 17.80% | 48.8 s |
| Orca Whirlpools | 805 | 30.40% | 74.3 s |

Median failure rate across the sampled programs: **30.40%** (range 11.90% to 87.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **447.97 SOL**.

## Exchange and large-holder balances

11.79M SOL ($1.17B) across 8 publicly-attributed accounts. Net **70K SOL (0.59%) moved onto exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $915.26M | 0.8/h | 1 |
| Binance (2) | 1.90M | $189.59M | 1.1K/h | 0 |
| Gate.io | 337.10K | $33.58M | 96.2/h | 0 |
| Bybit | 174.76K | $17.41M | 24.2/h | 0 |
| Bitget | 76.73K | $7.64M | 160.8/h | 0 |
| Coinbase (2) | 51.61K | $5.14M | 435.8/h | 0 |
| Kraken | 36.00K | $3.59M | 235.4/h | 0 |
| Coinbase | 24.86K | $2.48M | 465.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 740 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.258 | 699 | 0.0000 |
| DEX volume moves with App fees | +0.204 | 699 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.196 | 706 | 0.0000 |
| Total TPS moves with Slot time | +0.157 | 706 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.146 | 665 | 0.0002 |
| Total TPS moves with AMM write-lock congestion | +0.145 | 665 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.135 | 705 | 0.0003 |
| Total TPS moves with Activity index | +0.127 | 705 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.120 | 665 | 0.0019 |
| Slot time moves with AMM write-lock congestion | +0.114 | 665 | 0.0032 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 488.14K USD | DeFiLlama: 899.77K USD | -59.32% | *indicative*: 0.54x, within the order-of-magnitude band |
| SOL price | coingecko: 99.61 USD | Jupiter (on-chain DEX): 99.68 USD | -0.07% | agree |
| Circulating supply | getSupply (RPC): 585.28M SOL | CoinGecko: 585.28M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02
- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20

**Recently merged SIMDs:**

- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29

**Latest Agave release:** [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) (2026-08-28)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Solana Treasury DeFi Development Corp Eyes $20 Million Raise to Buy More SOL](https://decrypt.co/377068/defi-development-corp-20-million-raise-more-solana)** - Decrypt, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[v1 Transactions and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
