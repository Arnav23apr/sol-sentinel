# Solana Ecosystem Report

*Generated 2026-08-15 21:10 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 2.3K |
| Slot time | 419.6 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1017 (38.19% complete, ~31.1h remaining) |
| Lifetime transactions | 538.5B |
| Circulating supply | 582.7M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,514 lamports (about $0.00042) |
| Transaction fee p90 / p99 | 21,000 / 410,000 lamports |
| Paying base fee only | 15.50% of 5,480 sampled transactions |
| AMM write-lock congestion (150-slot window) | 6.00% of slots needed a priority fee (max 1.5M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 8 |
| Delinquent stake | 0.01% |
| Total active stake | 435.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.40% / 35.73% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.18% |

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
| SOL price | $75.48 (+0.60% 24h) |
| Market cap | $43.98B (rank #7) |
| 24h volume | $674.08M |
| ATH | $293.31 (-74.27% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.82B |
| Stablecoin supply | $15.41B |
| DEX volume (24h) | $1.61B (-16.98% 1d) |
| App fees (24h, all protocols) | $8.05M |
| Chain fees (24h) | $602.88K |
| Jito MEV tips (24h) | $82.79K |
| **REV - Real Economic Value (24h)** | **$685.67K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.70B | -6.29% |
| USDT | $2.90B | -2.03% |
| USDGO | $1.19B | +4.25% |
| USD1 | $1.05B | +1.18% |
| BUIDL | $740.96M | +4.04% |
| PYUSD | $678.40M | -0.90% |
| USDG | $635.20M | -2.14% |
| USDe | $537.69M | -0.27% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $597.50M |
| BisonFi | $156.52M |
| HumidiFi | $118.79M |
| pump.fun | $81.83M |
| Orca DEX | $64.63M |
| Raydium AMM | $61.04M |
| Meteora DLMM | $59.31M |
| Axiom | $58.07M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.14M |
| pump.fun | $1.35M |
| Axiom | $1.02M |
| fomo Wallet | $350.49K |
| Meteora DLMM | $260.73K |
| Collector Crypt | $227.25K |
| Raydium AMM | $186.53K |
| pump.fun Mobile App | $155.19K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 264 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $380.35M |
| xStocks 24h DEX volume | $6.13M |
| xStocks holders | 267.0K |
| Total RWA TVL on Solana | $1.87B |

Top tokenized equities: TSLAX ($62.30M), CRCLX ($51.71M), SPYX ($44.92M), MSTRX ($38.24M), GOOGLX ($31.00M)

## Program activity and chain health

Chain clock drift: **+15.7 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 41,230 | 24.30% | 1.3 s |
| Pump.fun | 26,997 | 90.10% | 2.1 s |
| Jupiter v6 | 1,124 | 17.90% | 52.9 s |
| Raydium AMM v4 | 750 | 18.30% | 79.7 s |
| Orca Whirlpools | 629 | 74.00% | 94 s |

Median failure rate across the sampled programs: **24.30%** (range 17.90% to 90.10%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.28 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 388.95K USD | DeFiLlama: 602.88K USD | -43.14% | agree (0.65x), *indicative* |
| SOL price | coingecko: 75.48 USD | Jupiter (on-chain DEX): 75.45 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 582.73M SOL | CoinGecko: 582.73M SOL | -0.00% | agree |

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
