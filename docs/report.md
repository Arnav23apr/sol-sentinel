# Solana Ecosystem Report

*Generated 2026-08-25 11:27 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.6K |
| Slot time | 363.6 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1022 (26.94% complete, ~31.9h remaining) |
| Lifetime transactions | 541.7B |
| Circulating supply | 583.4M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,731 lamports (about $0.00057) |
| Transaction fee p90 / p99 | 38,147 / 410,000 lamports |
| Paying no priority fee | 20.20% of 5,539 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 19.2M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 10 |
| Delinquent stake | 0.04% |
| Total active stake | 435.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.25% / 24.29% / 35.64% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 24.15% |

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
| SOL price | $98.98 (+4.43% 24h) |
| Market cap | $57.75B (rank #7) |
| 24h volume | $7.26B |
| ATH | $293.31 (-66.25% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.78B |
| Stablecoin supply | $15.88B |
| DEX volume (24h) | $3.00B (+1.96% 1d) |
| App fees (24h, all protocols) | $14.39M |
| Chain fees (24h) | $928.73K |
| Jito MEV tips (24h) | $200.68K |
| **REV - Real Economic Value (24h)** | **$1.13M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.06B | +4.79% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.21B | +2.06% |
| USD1 | $1.10B | +4.18% |
| BUIDL | $828.75M | +11.79% |
| PYUSD | $679.22M | +0.91% |
| USDG | $633.58M | -0.52% |
| USDe | $536.80M | -0.13% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $694.81M |
| Orca DEX | $519.35M |
| BisonFi | $409.15M |
| Meteora DLMM | $278.05M |
| Manifest Trade | $221.67M |
| Scorch | $218.92M |
| Raydium AMM | $194.80M |
| pump.fun | $95.40M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.03M |
| pump.fun | $1.82M |
| Axiom | $1.54M |
| fomo Wallet | $585.96K |
| Meteora DLMM | $575.35K |
| Sanctum Validator LSTs | $430.20K |
| Jupiter Perpetual Exchange | $413.47K |
| Phantom Wallet | $320.72K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 259 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $422.07M |
| xStocks 24h DEX volume | $31.38M |
| xStocks holder positions | 275.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.01B |

Top tokenized equities: TSLAX ($64.19M), CRCLX ($62.17M), SPYX ($48.20M), MSTRX ($47.89M), GOOGLX ($31.28M)

## Program activity and chain health

Chain tip lag: **+13.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 44,829 | 24.70% | 1.1 s |
| Pump.fun | 26,485 | 81.50% | 2.2 s |
| Jupiter v6 | 14,686 | 79.20% | 2.5 s |
| Orca Whirlpools | 9,115 | 71.80% | 6.2 s |
| Raydium AMM v4 | 929 | 24.40% | 64.4 s |

Median failure rate across the sampled programs: **71.80%** (range 24.40% to 81.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **516.94 SOL**.

## Exchange and large-holder balances

12.97M SOL ($1.28B) across 8 publicly-attributed accounts. Net **290K SOL (2.19%) moved off exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.08B | 1.2/h | 9 |
| Binance (2) | 1.04M | $103.23M | 1.3K/h | 0 |
| Gate.io | 431.98K | $42.76M | 264.7/h | 0 |
| Bybit | 377.27K | $37.34M | 77.3/h | 0 |
| Coinbase (2) | 80.90K | $8.01M | 240/h | 0 |
| Bitget | 58.93K | $5.83M | 230.9/h | 0 |
| Kraken | 38.38K | $3.80M | 257.7/h | 0 |
| Coinbase | 30.77K | $3.05M | 354.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 7 of 117 tested pairs survive, over 665 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.228 | 624 | 0.0000 |
| DEX volume moves with App fees | +0.189 | 624 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.184 | 631 | 0.0000 |
| Total TPS moves with Slot time | +0.145 | 631 | 0.0003 |
| Non-vote TPS moves with Activity index | +0.130 | 630 | 0.0011 |
| Slot time moves with AMM write-lock congestion | +0.129 | 590 | 0.0017 |
| Total TPS moves with Activity index | +0.121 | 630 | 0.0024 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 486.50K USD | DeFiLlama: 928.73K USD | -62.49% | *indicative*: 0.52x, within the order-of-magnitude band |
| SOL price | coingecko: 98.98 USD | Jupiter (on-chain DEX): 98.60 USD | +0.38% | agree |
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
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-24

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21)

**Latest Firedancer release:** [v26.08.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.1) (2026-08-21)

## Ecosystem news

- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
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
