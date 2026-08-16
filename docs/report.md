# Solana Ecosystem Report

*Generated 2026-08-16 22:09 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.6K |
| TPS (non-vote) | 1.9K |
| Slot time | 413.8 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1017 (87.31% complete, ~6.3h remaining) |
| Lifetime transactions | 538.8B |
| Circulating supply | 582.8M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,266 lamports (about $0.00039) |
| Transaction fee p90 / p99 | 30,000 / 853,021 lamports |
| Paying no priority fee | 24.60% of 7,738 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 16.70% of slots needed a priority fee (max 5.5M µlam/CU) |
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
| SOL price | $74.37 (-1.50% 24h) |
| Market cap | $43.34B (rank #7) |
| 24h volume | $694.30M |
| ATH | $293.31 (-74.64% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.79B |
| Stablecoin supply | $15.40B |
| DEX volume (24h) | $1.17B (-27.18% 1d) |
| App fees (24h, all protocols) | $8.15M |
| Chain fees (24h) | $593.84K |
| Jito MEV tips (24h) | $80.23K |
| **REV - Real Economic Value (24h)** | **$674.06K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.69B | -7.05% |
| USDT | $2.90B | -2.03% |
| USDGO | $1.19B | +4.25% |
| USD1 | $1.05B | +1.18% |
| BUIDL | $740.96M | +4.04% |
| PYUSD | $678.28M | -0.87% |
| USDG | $635.52M | +0.32% |
| USDe | $537.17M | -0.31% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $554.66M |
| BisonFi | $89.68M |
| pump.fun | $71.85M |
| HumidiFi | $65.45M |
| Meteora DLMM | $59.31M |
| Axiom | $50.64M |
| Raydium AMM | $50.05M |
| Orca DEX | $40.86M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.98M |
| pump.fun | $1.24M |
| Axiom | $852.64K |
| Collector Crypt | $397.74K |
| Sanctum Validator LSTs | $362.02K |
| fomo Wallet | $326.13K |
| Meteora DLMM | $260.73K |
| Binance Staked SOL | $231.64K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 395 |
| Persistently-active cohort (capture-recapture est.) | 4.5K |
| Unique payers across sampled blocks | 2.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $383.94M |
| xStocks 24h DEX volume | $4.83M |
| xStocks holder positions | 267.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.87B |

Top tokenized equities: TSLAX ($62.25M), CRCLX ($52.31M), SPYX ($44.95M), MSTRX ($38.20M), GOOGLX ($31.02M)

## Program activity and chain health

Chain tip lag: **+14.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 30,993 | 21.60% | 1.7 s |
| Pump.fun | 13,137 | 83.90% | 4.1 s |
| Orca Whirlpools | 5,023 | 28.40% | 11.6 s |
| Jupiter v6 | 2,003 | 37.10% | 29.4 s |
| Raydium AMM v4 | 1,156 | 26.80% | 49.2 s |

Median failure rate across the sampled programs: **28.40%** (range 21.60% to 83.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.28 SOL**.

## Exchange and large-holder balances

12.40M SOL ($922.00M) across 8 publicly-attributed accounts. Net **28K SOL (0.23%) moved off exchanges** over the last 21.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.75M | $799.48M | 1.3/h | 0 |
| Binance (2) | 755.29K | $56.17M | 847.1/h | 0 |
| Gate.io | 399.55K | $29.71M | 100.1/h | 0 |
| Bybit | 325.52K | $24.21M | 17.3/h | 0 |
| Bitget | 42.94K | $3.19M | 149.5/h | 0 |
| Kraken | 42.20K | $3.14M | 197.9/h | 0 |
| Coinbase | 41.88K | $3.11M | 530.2/h | 0 |
| Coinbase (2) | 40.01K | $2.98M | 516.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 4 of 117 tested pairs survive, over 353 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.239 | 312 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.221 | 311 | 0.0001 |
| Slot time moves with AMM write-lock congestion | +0.187 | 311 | 0.0009 |
| Non-vote TPS moves with Slot time | +0.169 | 352 | 0.0015 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 656.21K USD | DeFiLlama: 593.84K USD | +9.98% | *indicative*: 1.11x, within the order-of-magnitude band |
| SOL price | coingecko: 74.37 USD | Jupiter (on-chain DEX): 74.37 USD | 0.00% | agree |
| Circulating supply | getSupply (RPC): 582.78M SOL | CoinGecko: 582.78M SOL | 0.00% | agree |

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

- **[Israel’s largest bank taps Galaxy to offer bitcoin, ether and solana trading](https://www.theblock.co/news/business/2026-08-14-israels-largest-bank-taps-galaxy-to-offer-bitcoin-ether-and-solana-trading-411868)** - The Block, 2026-08-14
- **[Bitwise mulls tokenizing its Solana staking ETF via Superstate partnership](https://www.theblock.co/news/defi/2026-08-14-bitwise-tokenize-sol-staking-etf-411790)** - The Block, 2026-08-14
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

⚠️ *Sections served from the previous snapshot due to source errors this run: network.*

<details><summary>Collection errors this run</summary>

- `network`: `FetchError("getSupply failed on all RPC endpoints: https://api.mainnet-beta.solana.com failed after 2 attempts: TimeoutError('The read operation timed out')")`

</details>
