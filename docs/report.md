# Solana Ecosystem Report

*Generated 2026-08-17 19:48 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 14.8 robust standard deviations above its 7-day baseline: a 388.2% move to 0.08 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.6K |
| TPS (non-vote) | 3.0K |
| Slot time | 413.8 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1018 (31.69% complete, ~33.9h remaining) |
| Lifetime transactions | 539.1B |
| Circulating supply | 582.9M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 6,000 lamports (about $0.00046) |
| Transaction fee p90 / p99 | 32,491 / 786,250 lamports |
| Paying no priority fee | 17.60% of 7,840 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 1.3M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 688 |
| Delinquent validators | 7 |
| Delinquent stake | 0.08% |
| Total active stake | 435.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.41% / 35.75% |
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
| SOL price | $75.84 (+0.80% 24h) |
| Market cap | $44.20B (rank #7) |
| 24h volume | $1.33B |
| ATH | $293.31 (-74.15% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.85B |
| Stablecoin supply | $15.38B |
| DEX volume (24h) | $1.06B (-9.71% 1d) |
| App fees (24h, all protocols) | $6.80M |
| Chain fees (24h) | $468.52K |
| Jito MEV tips (24h) | $106.51K |
| **REV - Real Economic Value (24h)** | **$575.03K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.72B | -7.30% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.19B | +4.25% |
| USD1 | $1.05B | +1.18% |
| BUIDL | $741.17M | +4.07% |
| PYUSD | $674.06M | -1.59% |
| USDG | $633.07M | +0.12% |
| USDe | $537.07M | -0.16% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $502.56M |
| Orca DEX | $97.21M |
| Raydium AMM | $78.80M |
| BisonFi | $78.50M |
| Manifest Trade | $77.27M |
| pump.fun | $65.31M |
| HumidiFi | $53.10M |
| Axiom | $48.69M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.88M |
| pump.fun | $1.15M |
| Axiom | $829.08K |
| fomo Wallet | $422.11K |
| Collector Crypt | $327.19K |
| Raydium AMM | $181.50K |
| Meteora DLMM | $181.46K |
| pump.fun Mobile App | $138.88K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 304 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $388.51M |
| xStocks 24h DEX volume | $19.73M |
| xStocks holder positions | 268.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.88B |

Top tokenized equities: TSLAX ($61.86M), CRCLX ($54.48M), SPYX ($44.68M), MSTRX ($39.69M), GOOGLX ($30.78M)

## Program activity and chain health

Chain tip lag: **+14.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 77,139 (approx.) | 32.00% | 0.4 s |
| Pump.fun | 40,986 | 91.00% | 1.2 s |
| Raydium AMM v4 | 4,688 | 39.00% | 12.4 s |
| Jupiter v6 | 1,523 | 22.00% | 39.3 s |
| Orca Whirlpools | 799 | 41.50% | 74.5 s |

Median failure rate across the sampled programs: **39.00%** (range 22.00% to 91.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.28 SOL**.

## Exchange and large-holder balances

12.18M SOL ($923.49M) across 8 publicly-attributed accounts. Net **267K SOL (2.15%) moved off exchanges** over the last 23.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.75M | $815.28M | 31/h | 0 |
| Binance (2) | 534.33K | $40.52M | 1.0K/h | 0 |
| Gate.io | 397.86K | $30.17M | 102.7/h | 0 |
| Bybit | 325.52K | $24.69M | 39.8/h | 0 |
| Coinbase (2) | 54.05K | $4.10M | 522.5/h | 0 |
| Coinbase | 41.94K | $3.18M | 416.2/h | 0 |
| Kraken | 38.99K | $2.96M | 241.8/h | 0 |
| Bitget | 34.18K | $2.59M | 181.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 384 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.257 | 343 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.195 | 334 | 0.0003 |
| AMM write-lock congestion moves with Program failure rate | +0.195 | 334 | 0.0003 |
| DEX volume moves with App fees | +0.178 | 343 | 0.0009 |
| Non-vote TPS moves with Slot time | +0.170 | 375 | 0.0009 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 564.71K USD | DeFiLlama: 468.52K USD | +18.62% | *indicative*: 1.21x, within the order-of-magnitude band |
| SOL price | coingecko: 75.84 USD | Jupiter (on-chain DEX): 75.75 USD | +0.12% | agree |
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
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
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
- **[Israel’s largest bank taps Galaxy to offer bitcoin, ether and solana trading](https://www.theblock.co/news/business/2026-08-14-israels-largest-bank-taps-galaxy-to-offer-bitcoin-ether-and-solana-trading-411868)** - The Block, 2026-08-14
- **[Solana Can Be the 'Everything Chain' as Crypto Apps Go Mainstream: 6th Man Ventures Co-Founder](https://decrypt.co/375605/solana-everything-chain-crypto-apps-mainstream)** - Decrypt, 2026-08-13
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
