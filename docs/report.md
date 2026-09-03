# Solana Ecosystem Report

*Generated 2026-09-03 09:57 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.1K |
| Slot time | 315 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1027 (64.46% complete, ~13.4h remaining) |
| Lifetime transactions | 544.7B |
| Circulating supply | 585.3M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,410 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 19,762 / 159,000 lamports |
| Paying no priority fee | 25.50% of 3,331 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 27.4M µlam/CU) |
| Node version (RPC) | 4.2.2 |

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
| Stake on private (100% commission) validators | 23.96% |

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
| SOL price | $100.21 (+1.60% 24h) |
| Market cap | $58.65B (rank #7) |
| 24h volume | $3.15B |
| ATH | $293.31 (-65.84% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.75B |
| Stablecoin supply | $15.76B |
| DEX volume (24h) | $2.33B (+7.16% 1d) |
| App fees (24h, all protocols) | $11.21M |
| Chain fees (24h) | $612.58K |
| Jito MEV tips (24h) | $97.37K |
| **REV - Real Economic Value (24h)** | **$709.95K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.70B | -4.01% |
| USDT | $2.90B | +2.49% |
| USDGO | $1.28B | +2.08% |
| USD1 | $1.21B | +6.36% |
| BUIDL | $890.69M | +0.49% |
| PYUSD | $811.88M | +18.60% |
| USDG | $598.70M | -2.47% |
| USDe | $535.56M | -0.18% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $1.02B |
| Orca DEX | $218.27M |
| BisonFi | $194.35M |
| Manifest Trade | $164.29M |
| Meteora DLMM | $137.83M |
| Raydium AMM | $111.69M |
| Axiom | $97.98M |
| pump.fun | $83.17M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.72M |
| pump.fun | $1.46M |
| fomo Wallet | $1.35M |
| Axiom | $893.14K |
| Sanctum Validator LSTs | $364.05K |
| pump.fun Mobile App | $317.34K |
| Meteora DLMM | $313.01K |
| Raydium AMM | $303.14K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 220 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $436.72M |
| xStocks 24h DEX volume | $28.93M |
| xStocks holder positions | 314.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: TSLAX ($67.10M), CRCLX ($65.78M), MSTRX ($53.73M), SPYX ($48.72M), GOOGLX ($30.58M)

## Program activity and chain health

Chain tip lag: **+11.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 33,943 | 9.80% | 1.6 s |
| Pump.fun | 23,762 | 87.40% | 2.5 s |
| Jupiter v6 | 2,640 | 33.00% | 22.7 s |
| Raydium AMM v4 | 1,010 | 10.30% | 59.2 s |
| Orca Whirlpools | 860 | 23.80% | 68.7 s |

Median failure rate across the sampled programs: **23.80%** (range 9.80% to 87.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **444.52 SOL**.

## Exchange and large-holder balances

12.03M SOL ($1.21B) across 8 publicly-attributed accounts. Net **175K SOL (1.48%) moved onto exchanges** over the last 20.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $920.77M | 0.8/h | 1 |
| Binance (2) | 1.94M | $194.88M | 1.1K/h | 0 |
| Gate.io | 352.62K | $35.34M | 149.6/h | 0 |
| Bybit | 315.40K | $31.61M | 81.6/h | 0 |
| Coinbase | 79.53K | $7.97M | 180.7/h | 0 |
| Bitget | 78.98K | $7.91M | 187.7/h | 0 |
| Coinbase (2) | 47.36K | $4.75M | 204.2/h | 0 |
| Kraken | 25.87K | $2.59M | 179.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 743 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.261 | 702 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.197 | 709 | 0.0000 |
| DEX volume moves with App fees | +0.194 | 702 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 709 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.148 | 668 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.147 | 668 | 0.0001 |
| Non-vote TPS moves with Activity index | +0.135 | 708 | 0.0003 |
| Total TPS moves with Activity index | +0.127 | 708 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.118 | 668 | 0.0022 |
| Slot time moves with AMM write-lock congestion | +0.114 | 668 | 0.0032 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 308.48K USD | DeFiLlama: 612.58K USD | -66.03% | *indicative*: 0.50x, within the order-of-magnitude band |
| SOL price | coingecko: 100.21 USD | Jupiter (on-chain DEX): 100.09 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 585.27M SOL | CoinGecko: 585.27M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-02

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
