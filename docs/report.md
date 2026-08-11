# Solana Ecosystem Report

*Generated 2026-08-11 23:28 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 7.9 robust standard deviations above its 7-day baseline: a 1171.4% move to 0.09 % from a typical 0.01.
- 🟠 **Activity index (fee payers per block)** (warning): Activity index (fee payers per block) is 3.9 robust standard deviations above its 7-day baseline: a 43.0% move to 406.00 from a typical 284.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 2.0K |
| Slot time | 416.7 ms |
| Slot | 439M |
| Block height | 417M |
| Epoch | 1015 (51.03% complete, ~24.5h remaining) |
| Lifetime transactions | 537.3B |
| Circulating supply | 582.5M SOL |
| Inflation (annual) | 3.70% |
| Median transaction fee | 5,612 lamports (about $0.00043) |
| Transaction fee p90 / p99 | 33,870 / 816,373 lamports |
| Paying base fee only | 16.50% of 9,111 sampled transactions |
| AMM write-lock congestion (150-slot window) | 21.30% of slots needed a priority fee (max 5.5M µlam/CU) |
| Node version (RPC) | 4.2.0-rc.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 10 |
| Delinquent stake | 0.09% |
| Total active stake | 434.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.39% / 35.73% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.18% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.5M | 2.88% | 5% |
| 4 | `3N7s…iD5g` | 12.3M | 2.84% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.2M | 1.88% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $76.26 (+0.10% 24h) |
| Market cap | $44.41B (rank #7) |
| 24h volume | $1.37B |
| ATH | $293.31 (-74.00% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.84B |
| Stablecoin supply | $15.71B |
| DEX volume (24h) | $1.58B (+17.41% 1d) |
| App fees (24h, all protocols) | $10.49M |
| Chain fees (24h) | $680.55K |
| Jito MEV tips (24h) | $143.31K |
| **REV - Real Economic Value (24h)** | **$823.86K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.98B | -0.43% |
| USDT | $2.96B | -11.90% |
| USDGO | $1.16B | +4.04% |
| USD1 | $1.05B | +2.92% |
| BUIDL | $728.16M | +7.77% |
| PYUSD | $668.36M | -2.96% |
| USDG | $651.33M | +1.14% |
| USDe | $537.58M | -0.28% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $335.38M |
| BisonFi | $216.14M |
| HumidiFi | $161.21M |
| Orca DEX | $109.95M |
| Raydium AMM | $107.98M |
| Meteora DLMM | $89.35M |
| pump.fun | $86.05M |
| Manifest Trade | $70.56M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.49M |
| pump.fun | $1.43M |
| Axiom | $1.18M |
| Collector Crypt | $563.60K |
| fomo Wallet | $406.80K |
| Meteora DLMM | $390.44K |
| Sanctum Validator LSTs | $365.15K |
| Raydium AMM | $358.57K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 406 |
| Persistently-active cohort (capture-recapture est.) | 4.4K |
| Unique payers across sampled blocks | 2.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $377.02M |
| xStocks 24h DEX volume | $27.48M |
| xStocks holders | 262.2K |
| Total RWA TVL on Solana | $1.85B |

Top tokenized equities: TSLAX ($61.36M), CRCLX ($53.21M), SPYX ($44.18M), MSTRX ($37.64M), QQQX ($28.79M)

## Program activity and chain health

Chain clock drift: **+15.6 s** against wall clock (slots run slightly longer than the nominal 400 ms, so chain time falls behind real time).

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 51,980 (approx.) | 28.20% | 0.8 s |
| Pump.fun | 14,927 | 85.40% | 3.8 s |
| Jupiter v6 | 4,087 | 72.50% | 14.2 s |
| Orca Whirlpools | 622 | 64.50% | 95.4 s |
| Raydium AMM v4 | 587 | 16.90% | 102.1 s |

Median failure rate across the sampled programs: **64.50%** (range 16.90% to 85.40%). This is a consistent trend signal across these five programs, not a chain-wide rate.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.26 SOL**.

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 3 agree this run. Rows marked *indicative* are reported for corroboration but never raise an alert, because their own measurement noise is wider than any threshold worth acting on.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 6.26M USD | DeFiLlama: 680.55K USD | +160.78% | **diverge** (9.20x), *indicative* |
| SOL price | coingecko: 76.26 USD | Jupiter (on-chain DEX): 76.19 USD | +0.09% | agree |
| Circulating supply | getSupply (RPC): 582.48M SOL | CoinGecko: 582.48M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-07-20

**Open SIMD proposals:**

- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0511: On-Chain Epoch Stakes](https://github.com/solana-foundation/solana-improvement-documents/pull/586) - updated 2026-07-22
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-07-17
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-04
- [SIMD-0568: Deprecate Precompiles](https://github.com/solana-foundation/solana-improvement-documents/pull/568) - updated 2026-06-24

**Recently merged SIMDs:**

- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-07-23
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-07-20
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.2.0](https://github.com/anza-xyz/agave/releases/tag/v4.2.0) (2026-08-07)

**Latest Firedancer release:** [v0.1105.40200](https://github.com/firedancer-io/firedancer/releases/tag/v0.1105.40200) (2026-08-11)

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
