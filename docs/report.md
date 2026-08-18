# Solana Ecosystem Report

*Generated 2026-08-18 10:52 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 9.9 robust standard deviations above its 7-day baseline: a 258.8% move to 0.06 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.8K |
| TPS (non-vote) | 1.2K |
| Slot time | 416.7 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1018 (61.96% complete, ~19.0h remaining) |
| Lifetime transactions | 539.2B |
| Circulating supply | 582.9M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,412 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 29,000 / 842,500 lamports |
| Paying no priority fee | 21.50% of 6,834 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 4.00% of slots needed a priority fee (max 1.3M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 688 |
| Delinquent validators | 7 |
| Delinquent stake | 0.06% |
| Total active stake | 435.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.41% / 35.74% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.19% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $75.81 (+0.90% 24h) |
| Market cap | $44.19B (rank #7) |
| 24h volume | $1.28B |
| ATH | $293.31 (-74.16% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.85B |
| Stablecoin supply | $15.39B |
| DEX volume (24h) | $1.43B (+35.03% 1d) |
| App fees (24h, all protocols) | $10.78M |
| Chain fees (24h) | $732.76K |
| Jito MEV tips (24h) | $123.89K |
| **REV - Real Economic Value (24h)** | **$856.64K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.74B | -4.05% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.19B | +4.24% |
| USD1 | $1.05B | +0.85% |
| BUIDL | $741.35M | +4.00% |
| PYUSD | $671.41M | -2.59% |
| USDG | $634.16M | -2.00% |
| USDe | $537.66M | +0.05% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $372.89M |
| BisonFi | $208.44M |
| HumidiFi | $137.88M |
| Meteora DLMM | $93.85M |
| Orca DEX | $90.74M |
| Manifest Trade | $87.11M |
| pump.fun | $80.16M |
| Raydium AMM | $74.37M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.19M |
| Axiom | $1.41M |
| pump.fun | $1.15M |
| Meteora DLMM | $476.23K |
| fomo Wallet | $422.11K |
| Sanctum Validator LSTs | $369.77K |
| Binance Staked SOL | $228.45K |
| Jito Liquid Staking | $216.59K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 343 |
| Persistently-active cohort (capture-recapture est.) | 3.9K |
| Unique payers across sampled blocks | 2.1K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $384.38M |
| xStocks 24h DEX volume | $19.50M |
| xStocks holder positions | 268.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.88B |

Top tokenized equities: TSLAX ($60.95M), CRCLX ($52.56M), SPYX ($44.43M), MSTRX ($39.22M), GOOGLX ($30.69M)

## Program activity and chain health

Chain tip lag: **+14.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 31,425 | 39.10% | 1.7 s |
| Pump.fun | 8,603 | 72.90% | 6.7 s |
| Jupiter v6 | 3,785 | 59.60% | 15.8 s |
| Raydium AMM v4 | 888 | 10.40% | 67.1 s |
| Orca Whirlpools | 807 | 12.50% | 74.2 s |

Median failure rate across the sampled programs: **39.10%** (range 10.40% to 72.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.28 SOL**.

## Exchange and large-holder balances

12.18M SOL ($923.63M) across 8 publicly-attributed accounts. Net **94K SOL (0.76%) moved off exchanges** over the last 24.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.75M | $739.15M | 5.6/h | 0 |
| Binance (2) | 1.56M | $118.00M | 937.5/h | 0 |
| Gate.io | 398.70K | $30.23M | 129.7/h | 0 |
| Bybit | 325.52K | $24.68M | 36.4/h | 0 |
| Coinbase | 43.40K | $3.29M | 172.8/h | 0 |
| Coinbase (2) | 41.63K | $3.16M | 204.7/h | 0 |
| Bitget | 34.57K | $2.62M | 204.9/h | 0 |
| Kraken | 33.10K | $2.51M | 325.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 407 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.258 | 366 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.190 | 347 | 0.0004 |
| Slot time moves with AMM write-lock congestion | +0.189 | 347 | 0.0004 |
| DEX volume moves with App fees | +0.182 | 366 | 0.0005 |
| Non-vote TPS moves with Slot time | +0.165 | 388 | 0.0011 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 612.29K USD | DeFiLlama: 732.76K USD | -17.91% | *indicative*: 0.84x, within the order-of-magnitude band |
| SOL price | coingecko: 75.81 USD | Jupiter (on-chain DEX): 75.77 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 582.90M SOL | CoinGecko: 582.90M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-17
- [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-06-24

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

- **[Solana’s Pump Token Leads Crypto Market Gainers as Chart Paints Golden Cross](https://decrypt.co/375788/solana-pump-price-crypto-market-golden-cross)** - Decrypt, 2026-08-17
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
