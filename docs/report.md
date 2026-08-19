# Solana Ecosystem Report

*Generated 2026-08-19 08:37 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.9K |
| TPS (non-vote) | 1.3K |
| Slot time | 412.4 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1019 (5.57% complete, ~46.7h remaining) |
| Lifetime transactions | 539.5B |
| Circulating supply | 583.0M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,495 lamports (about $0.00042) |
| Transaction fee p90 / p99 | 21,411 / 410,000 lamports |
| Paying no priority fee | 17.80% of 7,514 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 547.9K µlam/CU) |
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
| SOL price | $77.14 (+1.20% 24h) |
| Market cap | $44.98B (rank #7) |
| 24h volume | $1.32B |
| ATH | $293.31 (-73.70% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.89B |
| Stablecoin supply | $15.43B |
| DEX volume (24h) | $1.82B (+23.44% 1d) |
| App fees (24h, all protocols) | $8.71M |
| Chain fees (24h) | $649.17K |
| Jito MEV tips (24h) | $120.73K |
| **REV - Real Economic Value (24h)** | **$769.90K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.78B | -2.64% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.19B | +2.62% |
| USD1 | $1.05B | 0.00% |
| BUIDL | $741.42M | +1.82% |
| PYUSD | $676.33M | -0.69% |
| USDG | $632.67M | -2.87% |
| USDe | $537.37M | -0.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $698.60M |
| BisonFi | $241.78M |
| HumidiFi | $160.54M |
| Orca DEX | $98.25M |
| pump.fun | $85.05M |
| Meteora DLMM | $84.89M |
| Raydium AMM | $77.17M |
| Axiom | $77.09M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.61M |
| pump.fun | $1.51M |
| Axiom | $1.31M |
| fomo Wallet | $479.35K |
| Meteora DLMM | $346.41K |
| Collector Crypt | $233.71K |
| Terminal | $159.23K |
| Phantom Wallet | $157.34K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 316 |
| Persistently-active cohort (capture-recapture est.) | 3.1K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $380.49M |
| xStocks 24h DEX volume | $16.38M |
| xStocks holder positions | 269.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.87B |

Top tokenized equities: TSLAX ($61.00M), CRCLX ($51.29M), SPYX ($44.95M), MSTRX ($37.82M), GOOGLX ($30.74M)

## Program activity and chain health

Chain tip lag: **+14.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 35,099 | 14.40% | 1.6 s |
| Pump.fun | 12,301 | 75.70% | 4.5 s |
| Jupiter v6 | 5,686 | 60.00% | 10.3 s |
| Orca Whirlpools | 2,271 | 45.40% | 26.4 s |
| Raydium AMM v4 | 604 | 31.60% | 99 s |

Median failure rate across the sampled programs: **45.40%** (range 14.40% to 75.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.02K SOL**.

## Exchange and large-holder balances

12.23M SOL ($943.69M) across 8 publicly-attributed accounts. Net **73K SOL (0.60%) moved onto exchanges** over the last 23.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.75M | $752.12M | 2.5/h | 0 |
| Binance (2) | 1.53M | $117.99M | 975.6/h | 0 |
| Gate.io | 402.45K | $31.04M | 1.7K/h | 0 |
| Bybit | 325.52K | $25.11M | 28.4/h | 0 |
| Bitget | 98.77K | $7.62M | 240.2/h | 0 |
| Coinbase (2) | 50.26K | $3.88M | 213/h | 0 |
| Coinbase | 49.26K | $3.80M | 276.9/h | 0 |
| Kraken | 27.75K | $2.14M | 156.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 441 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.229 | 400 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.178 | 370 | 0.0006 |
| Non-vote TPS moves with Slot time | +0.167 | 411 | 0.0007 |
| Slot time moves with AMM write-lock congestion | +0.160 | 370 | 0.0020 |
| DEX volume moves with App fees | +0.158 | 400 | 0.0016 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 472.46K USD | DeFiLlama: 649.17K USD | -31.51% | *indicative*: 0.73x, within the order-of-magnitude band |
| SOL price | coingecko: 77.14 USD | Jupiter (on-chain DEX): 77.27 USD | -0.17% | agree |
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

- **[Solana Policy Institute CEO says Clarity Act in ‘August recess purgatory,’ gives it 10% odds before midterms](https://www.theblock.co/news/regulation/2026-08-18-solana-policy-institute-ceo-larity-act-august-recess-purgatory-gives-10-odds-midterms-412171)** - The Block, 2026-08-18
- **[Securitize brings Neuberger’s $230 billion fixed-income platform onchain with new tokenized fund](https://www.theblock.co/news/markets/2026-08-18-securitize-neubergers-230-billion-fixed-income-platform-onchain-new-tokenized-fund-412102)** - The Block, 2026-08-18
- **[Solana’s Pump Token Leads Crypto Market Gainers as Chart Paints Golden Cross](https://decrypt.co/375788/solana-pump-price-crypto-market-golden-cross)** - Decrypt, 2026-08-17
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
