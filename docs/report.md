# Solana Ecosystem Report

*Generated 2026-09-03 00:49 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 1.8K |
| Slot time | 315.8 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1027 (40.24% complete, ~22.6h remaining) |
| Lifetime transactions | 544.6B |
| Circulating supply | 585.3M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,418 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 21,594 / 410,000 lamports |
| Paying no priority fee | 27.30% of 3,947 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 8.2M µlam/CU) |
| Node version (RPC) | 4.3.0-beta.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 18 |
| Delinquent stake | 0.05% |
| Total active stake | 438.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.25% / 35.53% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.95% |

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
| SOL price | $99.67 (-0.06% 24h) |
| Market cap | $58.31B (rank #7) |
| 24h volume | $2.89B |
| ATH | $293.31 (-66.02% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.68B |
| Stablecoin supply | $15.76B |
| DEX volume (24h) | $2.17B (-13.19% 1d) |
| App fees (24h, all protocols) | $11.83M |
| Chain fees (24h) | $899.77K |
| Jito MEV tips (24h) | $112.85K |
| **REV - Real Economic Value (24h)** | **$1.01M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.73B | -4.41% |
| USDT | $2.90B | +2.49% |
| USDGO | $1.25B | +1.21% |
| USD1 | $1.21B | +8.62% |
| BUIDL | $890.69M | +1.63% |
| PYUSD | $804.06M | +18.44% |
| USDG | $609.02M | -3.22% |
| USDe | $535.74M | -0.17% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $827.37M |
| BisonFi | $204.83M |
| Orca DEX | $201.05M |
| Manifest Trade | $171.65M |
| Meteora DLMM | $139.98M |
| Raydium AMM | $117.02M |
| Axiom | $97.98M |
| Scorch | $64.72M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.44M |
| pump.fun | $1.74M |
| Axiom | $1.37M |
| fomo Wallet | $1.35M |
| Meteora DLMM | $364.50K |
| Raydium AMM | $341.08K |
| pump.fun Mobile App | $318.69K |
| Collector Crypt | $232.45K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 243 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $434.54M |
| xStocks 24h DEX volume | $28.90M |
| xStocks holder positions | 313.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: TSLAX ($66.45M), CRCLX ($65.18M), MSTRX ($53.07M), SPYX ($48.69M), GOOGLX ($30.58M)

## Program activity and chain health

Chain tip lag: **+11.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 34,427 | 20.70% | 1.6 s |
| Pump.fun | 13,042 | 81.40% | 4.4 s |
| Jupiter v6 | 2,590 | 56.30% | 23.1 s |
| Orca Whirlpools | 1,399 | 46.60% | 42.6 s |
| Raydium AMM v4 | 1,112 | 21.80% | 53.4 s |

Median failure rate across the sampled programs: **46.60%** (range 20.70% to 81.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **447.97 SOL**.

## Exchange and large-holder balances

11.88M SOL ($1.18B) across 8 publicly-attributed accounts. Net **101K SOL (0.86%) moved onto exchanges** over the last 19.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $915.81M | 0.8/h | 1 |
| Binance (2) | 1.91M | $189.90M | 857.1/h | 0 |
| Gate.io | 333.86K | $33.28M | 121.4/h | 0 |
| Bybit | 174.00K | $17.34M | 22.9/h | 0 |
| Coinbase (2) | 138.25K | $13.78M | 504.2/h | 0 |
| Bitget | 80.55K | $8.03M | 114.4/h | 0 |
| Kraken | 33.88K | $3.38M | 194.5/h | 0 |
| Coinbase | 25.70K | $2.56M | 442.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 741 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.256 | 700 | 0.0000 |
| DEX volume moves with App fees | +0.203 | 700 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.197 | 707 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 707 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.147 | 666 | 0.0001 |
| Non-vote TPS moves with AMM write-lock congestion | +0.147 | 666 | 0.0001 |
| Non-vote TPS moves with Activity index | +0.134 | 706 | 0.0003 |
| Total TPS moves with Activity index | +0.126 | 706 | 0.0008 |
| AMM write-lock congestion moves with Program failure rate | +0.122 | 666 | 0.0016 |
| Slot time moves with AMM write-lock congestion | +0.114 | 666 | 0.0031 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 317.60K USD | DeFiLlama: 899.77K USD | -95.64% | *indicative*: 0.35x, within the order-of-magnitude band |
| SOL price | coingecko: 99.67 USD | Jupiter (on-chain DEX): 99.55 USD | +0.12% | agree |
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
