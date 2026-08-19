# Solana Ecosystem Report

*Generated 2026-08-19 10:51 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.1K |
| TPS (non-vote) | 1.4K |
| Slot time | 413.8 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1019 (10.05% complete, ~44.7h remaining) |
| Lifetime transactions | 539.6B |
| Circulating supply | 583.0M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,668 lamports (about $0.00044) |
| Transaction fee p90 / p99 | 31,808 / 410,000 lamports |
| Paying no priority fee | 17.60% of 6,104 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 54.8M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 10 |
| Delinquent stake | 0.03% |
| Total active stake | 435.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.38% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.19% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.4M | 2.85% | 5% |
| 4 | `3N7s…iD5g` | 12.2M | 2.80% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $77.27 (+1.60% 24h) |
| Market cap | $45.06B (rank #7) |
| 24h volume | $1.41B |
| ATH | $293.31 (-73.66% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.90B |
| Stablecoin supply | $15.42B |
| DEX volume (24h) | $1.82B (+23.44% 1d) |
| App fees (24h, all protocols) | $8.71M |
| Chain fees (24h) | $649.17K |
| Jito MEV tips (24h) | $122.72K |
| **REV - Real Economic Value (24h)** | **$771.89K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.77B | -2.80% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.19B | +2.62% |
| USD1 | $1.05B | 0.00% |
| BUIDL | $741.42M | +1.82% |
| PYUSD | $675.34M | -0.84% |
| USDG | $632.53M | -2.89% |
| USDe | $537.46M | -0.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $698.60M |
| BisonFi | $241.78M |
| HumidiFi | $160.54M |
| Orca DEX | $105.60M |
| pump.fun | $85.05M |
| Meteora DLMM | $84.89M |
| Axiom | $77.09M |
| Raydium AMM | $74.69M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.61M |
| pump.fun | $1.51M |
| Axiom | $1.31M |
| fomo Wallet | $479.35K |
| Collector Crypt | $378.68K |
| Meteora DLMM | $346.41K |
| Terminal | $159.23K |
| Phantom Wallet | $157.34K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 293 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $382.73M |
| xStocks 24h DEX volume | $16.13M |
| xStocks holder positions | 269.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.88B |

Top tokenized equities: TSLAX ($61.30M), CRCLX ($51.89M), SPYX ($45.17M), MSTRX ($38.06M), GOOGLX ($30.71M)

## Program activity and chain health

Chain tip lag: **+14.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 69,019 (approx.) | 29.70% | 0.4 s |
| Pump.fun | 8,487 | 72.00% | 7 s |
| Jupiter v6 | 1,954 | 38.20% | 30.2 s |
| Orca Whirlpools | 531 | 13.60% | 112.1 s |
| Raydium AMM v4 | 451 | 14.70% | 132.8 s |

Median failure rate across the sampled programs: **29.70%** (range 13.60% to 72.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **839.60 SOL**.

## Exchange and large-holder balances

12.20M SOL ($943.03M) across 8 publicly-attributed accounts. Net **20K SOL (0.17%) moved onto exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.75M | $753.38M | 2.3/h | 0 |
| Binance (2) | 1.52M | $117.24M | 859.2/h | 0 |
| Gate.io | 401.22K | $31.00M | 180.5/h | 0 |
| Bybit | 325.52K | $25.15M | 50/h | 0 |
| Bitget | 88.17K | $6.81M | 269.7/h | 0 |
| Coinbase | 48.77K | $3.77M | 209.3/h | 0 |
| Coinbase (2) | 45.52K | $3.52M | 183.7/h | 0 |
| Kraken | 27.95K | $2.16M | 288.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 4 of 117 tested pairs survive, over 445 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.233 | 404 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.176 | 372 | 0.0007 |
| Non-vote TPS moves with Slot time | +0.168 | 413 | 0.0006 |
| DEX volume moves with App fees | +0.157 | 404 | 0.0016 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 403.50K USD | DeFiLlama: 649.17K USD | -46.68% | *indicative*: 0.62x, within the order-of-magnitude band |
| SOL price | coingecko: 77.27 USD | Jupiter (on-chain DEX): 77.24 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 583.01M SOL | CoinGecko: 583.01M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-19
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-18

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) (2026-08-13)

**Latest Firedancer release:** [v26.08.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.0) (2026-08-12)

## Ecosystem news

- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Solana Policy Institute CEO says Clarity Act in ‘August recess purgatory,’ gives it 10% odds before midterms](https://www.theblock.co/news/regulation/2026-08-18-solana-policy-institute-ceo-larity-act-august-recess-purgatory-gives-10-odds-midterms-412171)** - The Block, 2026-08-18
- **[Securitize brings Neuberger’s $230 billion fixed-income platform onchain with new tokenized fund](https://www.theblock.co/news/markets/2026-08-18-securitize-neubergers-230-billion-fixed-income-platform-onchain-new-tokenized-fund-412102)** - The Block, 2026-08-18
- **[Solana’s Pump Token Leads Crypto Market Gainers as Chart Paints Golden Cross](https://decrypt.co/375788/solana-pump-price-crypto-market-golden-cross)** - Decrypt, 2026-08-17
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
