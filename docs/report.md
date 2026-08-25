# Solana Ecosystem Report

*Generated 2026-08-25 04:05 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 2.1K |
| Slot time | 365.9 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1022 (10.14% complete, ~39.5h remaining) |
| Lifetime transactions | 541.6B |
| Circulating supply | 583.4M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,316 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 29,000 / 410,000 lamports |
| Paying no priority fee | 22.10% of 7,036 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 686 |
| Delinquent validators | 8 |
| Delinquent stake | 0.02% |
| Total active stake | 435.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.24% / 24.28% / 35.63% |
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
| SOL price | $101.57 (+8.20% 24h) |
| Market cap | $59.28B (rank #7) |
| 24h volume | $7.18B |
| ATH | $293.31 (-65.37% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.77B |
| Stablecoin supply | $15.92B |
| DEX volume (24h) | $2.99B (+1.68% 1d) |
| App fees (24h, all protocols) | $13.05M |
| Chain fees (24h) | $696.89K |
| Jito MEV tips (24h) | $167.75K |
| **REV - Real Economic Value (24h)** | **$864.64K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.14B | +6.02% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.10B | +4.18% |
| BUIDL | $828.75M | +11.79% |
| PYUSD | $674.46M | +0.16% |
| USDG | $634.83M | -0.33% |
| USDe | $536.54M | -0.19% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $694.81M |
| Orca DEX | $453.98M |
| BisonFi | $409.15M |
| Meteora DLMM | $278.05M |
| Scorch | $270.62M |
| Manifest Trade | $205.31M |
| Raydium AMM | $199.80M |
| pump.fun | $95.40M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.25M |
| Axiom | $1.54M |
| pump.fun | $1.42M |
| Jupiter Perpetual Exchange | $651.76K |
| fomo Wallet | $605.37K |
| Meteora DLMM | $575.35K |
| Sanctum Validator LSTs | $430.20K |
| Raydium AMM | $325.50K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 323 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $425.41M |
| xStocks 24h DEX volume | $30.92M |
| xStocks holder positions | 274.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.01B |

Top tokenized equities: CRCLX ($64.72M), TSLAX ($63.68M), MSTRX ($49.43M), SPYX ($47.98M), GOOGLX ($31.18M)

## Program activity and chain health

Chain tip lag: **+13.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 45,750 | 30.70% | 1.1 s |
| Pump.fun | 19,841 | 75.20% | 2.9 s |
| Jupiter v6 | 12,572 | 82.50% | 4.4 s |
| Orca Whirlpools | 2,814 | 61.60% | 20.9 s |
| Raydium AMM v4 | 1,638 | 38.10% | 36.6 s |

Median failure rate across the sampled programs: **61.60%** (range 30.70% to 82.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **667.55 SOL**.

## Exchange and large-holder balances

13.05M SOL ($1.33B) across 8 publicly-attributed accounts. Net **30K SOL (0.23%) moved onto exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.11B | 1.2/h | 9 |
| Binance (2) | 1.23M | $125.28M | 1.3K/h | 0 |
| Bybit | 377.27K | $38.32M | 65/h | 0 |
| Gate.io | 372.95K | $37.88M | 153.5/h | 0 |
| Bitget | 53.93K | $5.48M | 159.4/h | 0 |
| Kraken | 39.74K | $4.04M | 216.1/h | 1 |
| Coinbase (2) | 34.26K | $3.48M | 831.4/h | 0 |
| Coinbase | 33.62K | $3.41M | 419.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 8 of 117 tested pairs survive, over 655 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.222 | 614 | 0.0000 |
| DEX volume moves with App fees | +0.203 | 614 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.182 | 621 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 580 | 0.0004 |
| Total TPS moves with Slot time | +0.143 | 621 | 0.0003 |
| Non-vote TPS moves with AMM write-lock congestion | +0.127 | 580 | 0.0022 |
| Non-vote TPS moves with Activity index | +0.124 | 620 | 0.0019 |
| Total TPS moves with AMM write-lock congestion | +0.123 | 580 | 0.0029 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 551.98K USD | DeFiLlama: 696.89K USD | -23.21% | *indicative*: 0.79x, within the order-of-magnitude band |
| SOL price | coingecko: 101.57 USD | Jupiter (on-chain DEX): 101.23 USD | +0.34% | agree |
| Circulating supply | getSupply (RPC): 583.38M SOL | CoinGecko: 583.38M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-24
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-24
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27

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
- **[Solana cuts mainnet slot time to 350 milliseconds in first step toward 200ms goal](https://www.theblock.co/news/ecosystems/2026-08-22-solana-cuts-mainnet-slot-time-to-350-milliseconds-in-first-step-toward-200ms-goal-412521)** - The Block, 2026-08-22
- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
