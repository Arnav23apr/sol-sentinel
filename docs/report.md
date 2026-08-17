# Solana Ecosystem Report

*Generated 2026-08-17 02:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.2K |
| TPS (non-vote) | 1.6K |
| Slot time | 413.8 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1017 (96.41% complete, ~1.8h remaining) |
| Lifetime transactions | 538.8B |
| Circulating supply | 582.8M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,447 lamports (about $0.00041) |
| Transaction fee p90 / p99 | 26,531 / 410,000 lamports |
| Paying no priority fee | 21.30% of 5,130 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 5.5M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 688 |
| Delinquent validators | 9 |
| Delinquent stake | 0.02% |
| Total active stake | 435.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.40% / 35.74% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.19% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.2M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.67% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $75.05 (-0.50% 24h) |
| Market cap | $43.74B (rank #7) |
| 24h volume | $789.96M |
| ATH | $293.31 (-74.41% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.77B |
| Stablecoin supply | $15.41B |
| DEX volume (24h) | $1.05B (-9.86% 1d) |
| App fees (24h, all protocols) | $6.63M |
| Chain fees (24h) | $468.52K |
| Jito MEV tips (24h) | $78.56K |
| **REV - Real Economic Value (24h)** | **$547.08K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.71B | -6.78% |
| USDT | $2.90B | -2.03% |
| USDGO | $1.19B | +4.25% |
| USD1 | $1.05B | +1.18% |
| BUIDL | $740.96M | +4.04% |
| PYUSD | $678.11M | -0.87% |
| USDG | $635.16M | +0.26% |
| USDe | $537.27M | -0.28% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $502.56M |
| BisonFi | $78.50M |
| pump.fun | $65.31M |
| Orca DEX | $54.62M |
| Raydium AMM | $53.25M |
| HumidiFi | $53.10M |
| Axiom | $50.64M |
| Meteora DLMM | $48.30M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.88M |
| pump.fun | $1.15M |
| Axiom | $829.08K |
| Collector Crypt | $469.94K |
| fomo Wallet | $326.13K |
| Meteora DLMM | $181.46K |
| pump.fun Mobile App | $138.88K |
| Kamino Lend | $129.28K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 268 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $383.35M |
| xStocks 24h DEX volume | $4.99M |
| xStocks holder positions | 267.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.87B |

Top tokenized equities: TSLAX ($62.34M), CRCLX ($51.99M), SPYX ($44.93M), MSTRX ($38.04M), GOOGLX ($31.07M)

## Program activity and chain health

Chain tip lag: **+15.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 57,999 (approx.) | 34.00% | 0.8 s |
| Pump.fun | 13,818 | 83.40% | 4.1 s |
| Jupiter v6 | 1,636 | 41.90% | 36.4 s |
| Raydium AMM v4 | 1,201 | 14.70% | 49.7 s |
| Orca Whirlpools | 585 | 40.70% | 102.2 s |

Median failure rate across the sampled programs: **40.70%** (range 14.70% to 83.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.28 SOL**.

## Exchange and large-holder balances

12.42M SOL ($932.48M) across 8 publicly-attributed accounts. Net **6K SOL (0.05%) moved off exchanges** over the last 24.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.75M | $806.79M | 1.2/h | 1 |
| Binance (2) | 777.89K | $58.38M | 853.1/h | 0 |
| Gate.io | 399.21K | $29.96M | 82.2/h | 1 |
| Bybit | 325.52K | $24.43M | 32.2/h | 0 |
| Bitget | 46.87K | $3.52M | 104.3/h | 0 |
| Coinbase | 44.56K | $3.34M | 365.1/h | 0 |
| Kraken | 41.48K | $3.11M | 157.3/h | 0 |
| Coinbase (2) | 39.25K | $2.95M | 666.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 4 of 117 tested pairs survive, over 358 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.246 | 317 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.218 | 314 | 0.0001 |
| Slot time moves with AMM write-lock congestion | +0.184 | 314 | 0.0011 |
| Non-vote TPS moves with Slot time | +0.167 | 355 | 0.0015 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 1.04M USD | DeFiLlama: 468.52K USD | +75.52% | *indicative*: 2.21x, within the order-of-magnitude band |
| SOL price | coingecko: 75.05 USD | Jupiter (on-chain DEX): 74.97 USD | +0.11% | agree |
| Circulating supply | getSupply (RPC): 582.78M SOL | CoinGecko: 582.78M SOL | -0.00% | agree |

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

- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Israel’s largest bank taps Galaxy to offer bitcoin, ether and solana trading](https://www.theblock.co/news/business/2026-08-14-israels-largest-bank-taps-galaxy-to-offer-bitcoin-ether-and-solana-trading-411868)** - The Block, 2026-08-14
- **[Bitwise mulls tokenizing its Solana staking ETF via Superstate partnership](https://www.theblock.co/news/defi/2026-08-14-bitwise-tokenize-sol-staking-etf-411790)** - The Block, 2026-08-14
- **[Solana Can Be the 'Everything Chain' as Crypto Apps Go Mainstream: 6th Man Ventures Co-Founder](https://decrypt.co/375605/solana-everything-chain-crypto-apps-mainstream)** - Decrypt, 2026-08-13
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
