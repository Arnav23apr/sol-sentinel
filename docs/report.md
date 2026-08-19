# Solana Ecosystem Report

*Generated 2026-08-19 14:03 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 17.5 robust standard deviations above its 7-day baseline: a 458.8% move to 0.10 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 3.1K |
| Slot time | 424 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1019 (16.44% complete, ~42.5h remaining) |
| Lifetime transactions | 539.6B |
| Circulating supply | 583.0M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,410 lamports (about $0.00042) |
| Transaction fee p90 / p99 | 25,000 / 577,522 lamports |
| Paying no priority fee | 20.10% of 5,654 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 15.30% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 686 |
| Delinquent validators | 9 |
| Delinquent stake | 0.10% |
| Total active stake | 434.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.40% / 35.75% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 24.21% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.4M | 2.85% | 5% |
| 4 | `3N7s…iD5g` | 12.2M | 2.81% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $78.35 (+3.00% 24h) |
| Market cap | $45.69B (rank #7) |
| 24h volume | $1.69B |
| ATH | $293.31 (-73.29% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.92B |
| Stablecoin supply | $15.43B |
| DEX volume (24h) | $1.84B (+24.62% 1d) |
| App fees (24h, all protocols) | $8.77M |
| Chain fees (24h) | $649.17K |
| Jito MEV tips (24h) | $120.36K |
| **REV - Real Economic Value (24h)** | **$769.53K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.78B | -2.60% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.19B | +2.62% |
| USD1 | $1.05B | 0.00% |
| BUIDL | $741.42M | +1.82% |
| PYUSD | $675.15M | -0.86% |
| USDG | $632.20M | -2.93% |
| USDe | $537.35M | -0.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $698.60M |
| BisonFi | $241.78M |
| HumidiFi | $160.54M |
| Orca DEX | $109.96M |
| pump.fun | $85.05M |
| Meteora DLMM | $84.89M |
| Manifest Trade | $73.28M |
| Raydium AMM | $72.91M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.61M |
| pump.fun | $1.51M |
| Axiom | $1.31M |
| Phantom Wallet | $544.74K |
| fomo Wallet | $449.17K |
| Collector Crypt | $362.58K |
| Meteora DLMM | $346.41K |
| Terminal | $159.23K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 310 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $383.12M |
| xStocks 24h DEX volume | $18.09M |
| xStocks holder positions | 269.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.88B |

Top tokenized equities: TSLAX ($61.12M), CRCLX ($52.20M), SPYX ($45.03M), MSTRX ($38.22M), GOOGLX ($30.57M)

## Program activity and chain health

Chain tip lag: **+15.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 60,566 (approx.) | 26.60% | 0.8 s |
| Pump.fun | 57,241 (approx.) | 93.70% | 0.8 s |
| Jupiter v6 | 9,274 | 62.50% | 6.4 s |
| Orca Whirlpools | 2,660 | 63.10% | 21.2 s |
| Raydium AMM v4 | 709 | 14.70% | 84 s |

Median failure rate across the sampled programs: **62.50%** (range 14.70% to 93.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **839.60 SOL**.

## Exchange and large-holder balances

12.29M SOL ($963.22M) across 8 publicly-attributed accounts. Net **82K SOL (0.67%) moved onto exchanges** over the last 23.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.75M | $763.91M | 2.3/h | 0 |
| Binance (2) | 1.62M | $126.63M | 1.6K/h | 0 |
| Gate.io | 395.97K | $31.02M | 439.6/h | 0 |
| Bybit | 325.52K | $25.50M | 279.7/h | 0 |
| Bitget | 80.12K | $6.28M | 272.7/h | 0 |
| Coinbase | 45.64K | $3.58M | 356.4/h | 0 |
| Coinbase (2) | 44.65K | $3.50M | 571.4/h | 0 |
| Kraken | 35.61K | $2.79M | 381.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 450 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.231 | 409 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.180 | 375 | 0.0004 |
| Non-vote TPS moves with Slot time | +0.164 | 416 | 0.0008 |
| Slot time moves with AMM write-lock congestion | +0.164 | 375 | 0.0014 |
| DEX volume moves with App fees | +0.164 | 409 | 0.0009 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 383.38K USD | DeFiLlama: 649.17K USD | -51.48% | *indicative*: 0.59x, within the order-of-magnitude band |
| SOL price | coingecko: 78.35 USD | Jupiter (on-chain DEX): 78.45 USD | -0.13% | agree |
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
