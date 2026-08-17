# Solana Ecosystem Report

*Generated 2026-08-17 20:49 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 14.8 robust standard deviations above its 7-day baseline: a 388.2% move to 0.08 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.3K |
| TPS (non-vote) | 2.6K |
| Slot time | 415.2 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1018 (33.75% complete, ~33.0h remaining) |
| Lifetime transactions | 539.1B |
| Circulating supply | 582.9M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,415 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 29,000 / 410,000 lamports |
| Paying no priority fee | 19.80% of 5,992 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 6.70% of slots needed a priority fee (max 273.9K µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 6 |
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
| SOL price | $75.93 (+0.70% 24h) |
| Market cap | $44.26B (rank #7) |
| 24h volume | $1.35B |
| ATH | $293.31 (-74.11% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.85B |
| Stablecoin supply | $15.37B |
| DEX volume (24h) | $1.06B (-9.71% 1d) |
| App fees (24h, all protocols) | $6.80M |
| Chain fees (24h) | $468.52K |
| Jito MEV tips (24h) | $110.59K |
| **REV - Real Economic Value (24h)** | **$579.11K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.72B | -7.37% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.19B | +4.25% |
| USD1 | $1.05B | +1.18% |
| BUIDL | $741.17M | +4.07% |
| PYUSD | $673.85M | -1.63% |
| USDG | $632.81M | +0.08% |
| USDe | $537.05M | -0.16% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $502.56M |
| Orca DEX | $97.21M |
| Raydium AMM | $80.34M |
| Manifest Trade | $78.91M |
| BisonFi | $78.50M |
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
| Raydium AMM | $184.72K |
| Meteora DLMM | $181.46K |
| pump.fun Mobile App | $138.88K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 274 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $388.57M |
| xStocks 24h DEX volume | $20.03M |
| xStocks holder positions | 268.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.88B |

Top tokenized equities: TSLAX ($61.70M), CRCLX ($54.65M), SPYX ($44.66M), MSTRX ($39.71M), GOOGLX ($30.79M)

## Program activity and chain health

Chain tip lag: **+15.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 69,870 (approx.) | 26.00% | 0.8 s |
| Pump.fun | 67,341 (approx.) | 92.60% | 0.8 s |
| Jupiter v6 | 2,474 | 46.30% | 23.7 s |
| Orca Whirlpools | 1,203 | 65.90% | 46.9 s |
| Raydium AMM v4 | 720 | 17.80% | 82.6 s |

Median failure rate across the sampled programs: **46.30%** (range 17.80% to 92.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.28 SOL**.

## Exchange and large-holder balances

12.22M SOL ($928.02M) across 8 publicly-attributed accounts. Net **220K SOL (1.77%) moved off exchanges** over the last 23.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.75M | $816.25M | 23.4/h | 0 |
| Binance (2) | 579.44K | $44.00M | 841.1/h | 0 |
| Gate.io | 397.72K | $30.20M | 122.6/h | 0 |
| Bybit | 325.52K | $24.72M | 43.2/h | 0 |
| Coinbase (2) | 53.60K | $4.07M | 579.7/h | 0 |
| Coinbase | 40.93K | $3.11M | 468.8/h | 0 |
| Kraken | 38.87K | $2.95M | 221/h | 0 |
| Bitget | 36.01K | $2.73M | 153.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 386 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.255 | 345 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.195 | 336 | 0.0003 |
| AMM write-lock congestion moves with Program failure rate | +0.191 | 336 | 0.0004 |
| DEX volume moves with App fees | +0.177 | 345 | 0.0009 |
| Non-vote TPS moves with Slot time | +0.169 | 377 | 0.0010 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 357.95K USD | DeFiLlama: 468.52K USD | -26.76% | *indicative*: 0.76x, within the order-of-magnitude band |
| SOL price | coingecko: 75.93 USD | Jupiter (on-chain DEX): 75.84 USD | +0.12% | agree |
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
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
