# Solana Ecosystem Report

*Generated 2026-08-17 14:50 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 2.3K |
| Slot time | 415.2 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1018 (21.81% complete, ~39.0h remaining) |
| Lifetime transactions | 539.0B |
| Circulating supply | 582.9M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,402 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 26,089 / 605,000 lamports |
| Paying no priority fee | 24.30% of 4,511 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 16.00% of slots needed a priority fee (max 13.7M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 6 |
| Delinquent stake | 0.01% |
| Total active stake | 435.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.39% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.17% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.67% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.81% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $75.67 (+0.50% 24h) |
| Market cap | $44.09B (rank #7) |
| 24h volume | $1.23B |
| ATH | $293.31 (-74.20% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.83B |
| Stablecoin supply | $15.36B |
| DEX volume (24h) | $1.06B (-9.71% 1d) |
| App fees (24h, all protocols) | $6.80M |
| Chain fees (24h) | $468.52K |
| Jito MEV tips (24h) | $83.69K |
| **REV - Real Economic Value (24h)** | **$552.21K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.70B | -7.52% |
| USDT | $2.85B | -3.38% |
| USDGO | $1.19B | +4.25% |
| USD1 | $1.05B | +1.18% |
| BUIDL | $740.96M | +4.04% |
| PYUSD | $672.43M | -1.81% |
| USDG | $634.64M | +0.37% |
| USDe | $537.25M | -0.11% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $502.56M |
| Orca DEX | $84.11M |
| BisonFi | $78.50M |
| pump.fun | $65.31M |
| Raydium AMM | $59.16M |
| Manifest Trade | $57.59M |
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
| Meteora DLMM | $181.46K |
| pump.fun Mobile App | $138.88K |
| Kamino Lend | $128.69K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 258 |
| Persistently-active cohort (capture-recapture est.) | 2.7K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $388.96M |
| xStocks 24h DEX volume | $14.61M |
| xStocks holder positions | 268.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.87B |

Top tokenized equities: TSLAX ($62.21M), CRCLX ($54.45M), SPYX ($44.76M), MSTRX ($38.93M), GOOGLX ($30.81M)

## Program activity and chain health

Chain tip lag: **+15.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 51,951 (approx.) | 25.60% | 0.8 s |
| Pump.fun | 35,164 | 91.60% | 1.2 s |
| Jupiter v6 | 3,878 | 51.90% | 15.4 s |
| Raydium AMM v4 | 2,815 | 43.00% | 20.8 s |
| Orca Whirlpools | 2,326 | 64.30% | 25.7 s |

Median failure rate across the sampled programs: **51.90%** (range 25.60% to 91.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **584.49 SOL**.

## Exchange and large-holder balances

12.24M SOL ($925.98M) across 8 publicly-attributed accounts. Net **193K SOL (1.55%) moved off exchanges** over the last 23.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.75M | $813.45M | 1.2/h | 0 |
| Binance (2) | 605.92K | $45.85M | 1.8K/h | 0 |
| Gate.io | 399.65K | $30.24M | 184.7/h | 0 |
| Bybit | 325.52K | $24.63M | 52/h | 0 |
| Kraken | 41.66K | $3.15M | 288/h | 0 |
| Coinbase | 39.02K | $2.95M | 419.1/h | 0 |
| Bitget | 38.05K | $2.88M | 227.1/h | 0 |
| Coinbase (2) | 37.25K | $2.82M | 602/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 375 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.254 | 334 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.195 | 327 | 0.0004 |
| AMM write-lock congestion moves with Program failure rate | +0.191 | 327 | 0.0005 |
| DEX volume moves with App fees | +0.178 | 334 | 0.0011 |
| Non-vote TPS moves with Slot time | +0.164 | 368 | 0.0016 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 388.20K USD | DeFiLlama: 468.52K USD | -18.75% | *indicative*: 0.83x, within the order-of-magnitude band |
| SOL price | coingecko: 75.67 USD | Jupiter (on-chain DEX): 75.76 USD | -0.12% | agree |
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

## Ecosystem news

- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Israel’s largest bank taps Galaxy to offer bitcoin, ether and solana trading](https://www.theblock.co/news/business/2026-08-14-israels-largest-bank-taps-galaxy-to-offer-bitcoin-ether-and-solana-trading-411868)** - The Block, 2026-08-14
- **[Solana Can Be the 'Everything Chain' as Crypto Apps Go Mainstream: 6th Man Ventures Co-Founder](https://decrypt.co/375605/solana-everything-chain-crypto-apps-mainstream)** - Decrypt, 2026-08-13
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
