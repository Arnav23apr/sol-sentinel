# Solana Ecosystem Report

*Generated 2026-08-25 03:24 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.0 robust standard deviations above its 7-day baseline: a 413.2% move to 0.14 % from a typical 0.03.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.2K |
| Slot time | 365.9 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1022 (8.56% complete, ~40.1h remaining) |
| Lifetime transactions | 541.6B |
| Circulating supply | 583.4M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,500 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 35,505 / 505,069 lamports |
| Paying no priority fee | 20.20% of 5,398 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 9 |
| Delinquent stake | 0.14% |
| Total active stake | 434.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.26% / 24.31% / 35.67% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.18% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.69% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 4 | `Catz…Diqb` | 11.7M | 2.70% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.05% | 10% |
| 7 | `8Gbw…F8iD` | 8.6M | 1.97% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.68% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.53 (+8.15% 24h) |
| Market cap | $59.21B (rank #7) |
| 24h volume | $7.02B |
| ATH | $293.31 (-65.39% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.77B |
| Stablecoin supply | $15.92B |
| DEX volume (24h) | $2.99B (+1.68% 1d) |
| App fees (24h, all protocols) | $13.11M |
| Chain fees (24h) | $696.89K |
| Jito MEV tips (24h) | $167.75K |
| **REV - Real Economic Value (24h)** | **$864.64K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.14B | +6.02% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.10B | +4.18% |
| BUIDL | $828.75M | +11.79% |
| PYUSD | $674.46M | +0.16% |
| USDG | $634.83M | -0.33% |
| USDe | $536.54M | -0.19% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $694.81M |
| Orca DEX | $453.98M |
| BisonFi | $409.15M |
| Meteora DLMM | $278.05M |
| Scorch | $270.62M |
| Manifest Trade | $203.57M |
| Raydium AMM | $199.60M |
| pump.fun | $95.40M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.25M |
| Axiom | $1.54M |
| pump.fun | $1.42M |
| Jupiter Perpetual Exchange | $651.76K |
| Meteora DLMM | $631.90K |
| fomo Wallet | $605.37K |
| Sanctum Validator LSTs | $430.20K |
| Raydium AMM | $325.50K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 287 |
| Persistently-active cohort (capture-recapture est.) | 3.2K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $423.77M |
| xStocks 24h DEX volume | $30.76M |
| xStocks holder positions | 274.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.01B |

Top tokenized equities: CRCLX ($63.84M), TSLAX ($63.72M), MSTRX ($49.02M), SPYX ($47.99M), GOOGLX ($31.24M)

## Program activity and chain health

Chain tip lag: **+14.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 67,068 (approx.) | 35.30% | 0.7 s |
| Pump.fun | 9,921 | 71.60% | 5.9 s |
| Jupiter v6 | 7,087 | 64.10% | 8.4 s |
| Orca Whirlpools | 3,266 | 62.20% | 18.3 s |
| Raydium AMM v4 | 901 | 17.30% | 66.2 s |

Median failure rate across the sampled programs: **62.20%** (range 17.30% to 71.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **900.50 SOL**.

## Exchange and large-holder balances

13.04M SOL ($1.32B) across 8 publicly-attributed accounts. Net **21K SOL (0.16%) moved onto exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.11B | 1.2/h | 9 |
| Binance (2) | 1.23M | $124.59M | 1.8K/h | 0 |
| Bybit | 377.27K | $38.30M | 58.9/h | 0 |
| Gate.io | 373.98K | $37.97M | 157.8/h | 0 |
| Bitget | 50.64K | $5.14M | 155.2/h | 0 |
| Kraken | 40.08K | $4.07M | 230.9/h | 0 |
| Coinbase (2) | 33.39K | $3.39M | 408.2/h | 0 |
| Coinbase | 32.37K | $3.29M | 422.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 8 of 117 tested pairs survive, over 654 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.221 | 613 | 0.0000 |
| DEX volume moves with App fees | +0.203 | 613 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.182 | 620 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 579 | 0.0004 |
| Total TPS moves with Slot time | +0.144 | 620 | 0.0003 |
| Non-vote TPS moves with AMM write-lock congestion | +0.126 | 579 | 0.0024 |
| Non-vote TPS moves with Activity index | +0.125 | 619 | 0.0018 |
| Total TPS moves with AMM write-lock congestion | +0.123 | 579 | 0.0030 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 612.64K USD | DeFiLlama: 696.89K USD | -12.87% | *indicative*: 0.88x, within the order-of-magnitude band |
| SOL price | coingecko: 101.53 USD | Jupiter (on-chain DEX): 101.40 USD | +0.13% | agree |
| Circulating supply | getSupply (RPC): 583.38M SOL | CoinGecko: 583.38M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-24
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-24
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21)

**Latest Firedancer release:** [v26.08.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.1) (2026-08-21)

## Ecosystem news

- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Solana cuts mainnet slot time to 350 milliseconds in first step toward 200ms goal](https://www.theblock.co/news/ecosystems/2026-08-22-solana-cuts-mainnet-slot-time-to-350-milliseconds-in-first-step-toward-200ms-goal-412521)** - The Block, 2026-08-22
- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
