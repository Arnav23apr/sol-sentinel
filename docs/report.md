# Solana Ecosystem Report

*Generated 2026-09-02 05:13 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.3K |
| Slot time | 313.4 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1026 (88.36% complete, ~4.4h remaining) |
| Lifetime transactions | 544.4B |
| Circulating supply | 585.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,881 lamports (about $0.00059) |
| Transaction fee p90 / p99 | 43,271 / 516,814 lamports |
| Paying no priority fee | 23.20% of 4,890 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.3.0-beta.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 16 |
| Delinquent stake | 0.04% |
| Total active stake | 438.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.26% / 24.18% / 35.45% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.95% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.2M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.5M | 2.62% | 5% |
| 5 | `8Gbw…F8iD` | 9.5M | 2.16% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.2M | 1.65% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $99.84 (-3.95% 24h) |
| Market cap | $58.42B (rank #7) |
| 24h volume | $3.58B |
| ATH | $293.31 (-65.96% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.69B |
| Stablecoin supply | $15.56B |
| DEX volume (24h) | $2.25B (-10.19% 1d) |
| App fees (24h, all protocols) | $12.27M |
| Chain fees (24h) | $899.77K |
| Jito MEV tips (24h) | $190.43K |
| **REV - Real Economic Value (24h)** | **$1.09M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.68B | -5.11% |
| USDT | $2.83B | 0.00% |
| USDGO | $1.25B | +0.48% |
| USD1 | $1.21B | +8.62% |
| BUIDL | $887.01M | +1.21% |
| PYUSD | $737.82M | +8.73% |
| USDG | $609.97M | -3.00% |
| USDe | $536.82M | +0.05% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $827.37M |
| Orca DEX | $218.89M |
| BisonFi | $204.83M |
| Raydium AMM | $143.16M |
| Manifest Trade | $141.37M |
| Meteora DLMM | $139.98M |
| Axiom | $113.58M |
| Jupiterz | $101.70M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.44M |
| pump.fun | $1.74M |
| Axiom | $1.37M |
| fomo Wallet | $1.08M |
| Raydium AMM | $771.45K |
| Meteora DLMM | $364.50K |
| pump.fun Mobile App | $318.69K |
| Collector Crypt | $276.91K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 248 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $431.60M |
| xStocks 24h DEX volume | $25.97M |
| xStocks holder positions | 308.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: TSLAX ($65.88M), CRCLX ($65.02M), MSTRX ($52.02M), SPYX ($48.21M), GOOGLX ($30.64M)

## Program activity and chain health

Chain tip lag: **+12.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 37,332 | 21.90% | 1.6 s |
| Pump.fun | 5,237 | 62.00% | 9.7 s |
| Jupiter v6 | 1,780 | 47.00% | 33.5 s |
| Orca Whirlpools | 1,704 | 31.50% | 35.1 s |
| Raydium AMM v4 | 814 | 16.60% | 73.6 s |

Median failure rate across the sampled programs: **31.50%** (range 16.60% to 62.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.33 SOL**.

## Exchange and large-holder balances

11.78M SOL ($1.18B) across 8 publicly-attributed accounts. Net **14K SOL (0.12%) moved off exchanges** over the last 20.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $917.37M | 1/h | 1 |
| Binance (2) | 1.86M | $185.40M | 957.4/h | 0 |
| Gate.io | 329.09K | $32.86M | 103.5/h | 0 |
| Bybit | 180.28K | $18.00M | 42.3/h | 0 |
| Bitget | 95.71K | $9.56M | 157.5/h | 0 |
| Coinbase (2) | 72.87K | $7.28M | 343.2/h | 0 |
| Kraken | 32.28K | $3.22M | 153/h | 0 |
| Coinbase | 23.23K | $2.32M | 448.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 11 of 117 tested pairs survive, over 735 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.257 | 694 | 0.0000 |
| DEX volume moves with App fees | +0.213 | 694 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.204 | 701 | 0.0000 |
| Total TPS moves with Slot time | +0.164 | 701 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.138 | 660 | 0.0004 |
| Total TPS moves with AMM write-lock congestion | +0.137 | 660 | 0.0004 |
| Non-vote TPS moves with Activity index | +0.133 | 700 | 0.0004 |
| Total TPS moves with Activity index | +0.125 | 700 | 0.0009 |
| AMM write-lock congestion moves with Program failure rate | +0.125 | 660 | 0.0013 |
| Slot time moves with AMM write-lock congestion | +0.119 | 660 | 0.0022 |
| Total TPS moves with Program failure rate | +0.108 | 682 | 0.0047 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 563.48K USD | DeFiLlama: 899.77K USD | -45.97% | *indicative*: 0.63x, within the order-of-magnitude band |
| SOL price | coingecko: 99.84 USD | Jupiter (on-chain DEX): 100.04 USD | -0.20% | agree |
| Circulating supply | getSupply (RPC): 585.21M SOL | CoinGecko: 585.21M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-08-31
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-09-01
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-31
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-31
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-01
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

- **[Solana Treasury DeFi Development Corp Eyes $20 Million Raise to Buy More SOL](https://decrypt.co/377068/defi-development-corp-20-million-raise-more-solana)** - Decrypt, 2026-09-01
- **[DeFi Development Corp proposes $20 million preferred stock offering to buy more SOL](https://www.theblock.co/news/business/2026-08-31-solana-defi-development-preferred-stock-offering-413190)** - The Block, 2026-09-01
- **[Solana fees hit record as validators double pace of inflation cuts](https://www.theblock.co/news/ecosystems/2026-08-31-solana-fees-hit-record-as-validators-double-pace-of-inflation-cuts-413135)** - The Block, 2026-08-31
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
