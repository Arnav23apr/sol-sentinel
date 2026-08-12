# Solana Ecosystem Report

*Generated 2026-08-12 12:41 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.8 robust standard deviations above its 7-day baseline: a 714.3% move to 0.06 % from a typical 0.01.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 2.0K |
| Slot time | 418.1 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1015 (77.23% complete, ~11.4h remaining) |
| Lifetime transactions | 537.4B |
| Circulating supply | 582.5M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,479 lamports (about $0.00042) |
| Transaction fee p90 / p99 | 31,854 / 1,004,905 lamports |
| Paying base fee only | 16.30% of 9,057 sampled transactions |
| AMM write-lock congestion (150-slot window) | 25.30% of slots needed a priority fee (max 1.6M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 10 |
| Delinquent stake | 0.06% |
| Total active stake | 434.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.38% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.24% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.87% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $76.72 (+0.90% 24h) |
| Market cap | $44.69B (rank #7) |
| 24h volume | $1.39B |
| ATH | $293.31 (-73.84% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.85B |
| Stablecoin supply | $15.67B |
| DEX volume (24h) | $1.65B (+4.35% 1d) |
| App fees (24h, all protocols) | $9.90M |
| Chain fees (24h) | $727.62K |
| Jito MEV tips (24h) | $149.16K |
| **REV - Real Economic Value (24h)** | **$876.78K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.91B | -3.50% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.17B | +5.54% |
| USD1 | $1.05B | +2.92% |
| BUIDL | $728.16M | +7.64% |
| PYUSD | $680.94M | +0.22% |
| USDG | $650.85M | -1.20% |
| USDe | $537.62M | -0.88% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $585.32M |
| BisonFi | $151.36M |
| Orca DEX | $105.80M |
| HumidiFi | $90.06M |
| Meteora DLMM | $88.94M |
| Raydium AMM | $85.69M |
| pump.fun | $79.16M |
| Axiom | $68.61M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.61M |
| pump.fun | $1.43M |
| Axiom | $1.36M |
| Collector Crypt | $729.41K |
| fomo Wallet | $458.80K |
| Meteora DLMM | $378.59K |
| Raydium AMM | $249.42K |
| Phantom Wallet | $205.71K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 372 |
| Persistently-active cohort (capture-recapture est.) | 3.7K |
| Unique payers across sampled blocks | 2.2K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $377.17M |
| xStocks 24h DEX volume | $28.60M |
| xStocks holders | 262.6K |
| Total RWA TVL on Solana | $1.85B |

Top tokenized equities: TSLAX ($61.58M), CRCLX ($52.79M), SPYX ($44.23M), MSTRX ($37.91M), QQQX ($28.76M)

## Program activity and chain health

Chain clock drift: **+15.7 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 93,136 (approx.) | 55.40% | 0.4 s |
| Pump.fun | 26,118 | 84.60% | 2.1 s |
| Jupiter v6 | 6,622 | 65.70% | 8.8 s |
| Orca Whirlpools | 4,573 | 74.70% | 12.5 s |
| Raydium AMM v4 | 924 | 34.40% | 64.8 s |

Median failure rate across the sampled programs: **65.70%** (range 34.40% to 84.60%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.26 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 3 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 684.17K USD | DeFiLlama: 727.62K USD | -6.16% | agree (0.94x), *indicative* |
| SOL price | coingecko: 76.72 USD | Jupiter (on-chain DEX): 76.51 USD | +0.27% | agree |
| Circulating supply | getSupply (RPC): 582.50M SOL | CoinGecko: 582.50M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
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

**Latest Agave release:** [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07)

**Latest Firedancer release:** [v26.08.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.0) (2026-08-12)

## Ecosystem news

- **[The Bull and Bear Case for Solana’s Next Price Move](https://decrypt.co/375364/solana-price-death-cross-bull-bear-case-next-move)** - Decrypt, 2026-08-11
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05
- **[Solana Ecosystem Roundup: July 2026](https://solana.com/news/solana-ecosystem-roundup-july-2026)** - Solana.com, 2026-08-05
- **[Breakpoint 2026: The Token Supercycle](https://solana.com/news/the-token-supercycle)** - Solana.com, 2026-08-04
- **[Inside Solana’s Growing Market for Tokenized Cards and Physical Collectibles](https://solana.com/news/tokenized-cards-and-physical-collectibles)** - Solana.com, 2026-07-31
- **[Overview of Institutional Real World Assets on Solana](https://solana.com/news/overview-of-institutional-real-world-assets-on-solana)** - Solana.com, 2026-07-30
- **[Solana Changelog: Mainnet raises block limits to 100M CUs](https://solana.com/news/solana-changelog-july-30-2026)** - Solana.com, 2026-07-30

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
