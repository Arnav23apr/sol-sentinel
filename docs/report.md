# Solana Ecosystem Report

*Generated 2026-08-21 16:58 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 16.7 robust standard deviations above its 7-day baseline: a 20.9% move to 91.65 USD from a typical 75.81.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 9.2 robust standard deviations above its 7-day baseline: a 12.2% move to 5,439,785,185.00 USD from a typical 4,847,040,662.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.6K |
| TPS (non-vote) | 2.7K |
| Slot time | 363.6 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1020 (20.92% complete, ~34.5h remaining) |
| Lifetime transactions | 540.4B |
| Circulating supply | 583.2M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,410 lamports (about $0.00050) |
| Transaction fee p90 / p99 | 24,493 / 410,000 lamports |
| Paying no priority fee | 19.90% of 8,472 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 13.7M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 9 |
| Delinquent stake | 0.02% |
| Total active stake | 433.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.33% / 35.70% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.27% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.1M | 3.70% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.81% | 0% |
| 4 | `Catz…Diqb` | 11.8M | 2.72% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.4M | 1.94% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $91.65 (+5.20% 24h) |
| Market cap | $53.45B (rank #7) |
| 24h volume | $5.97B |
| ATH | $293.31 (-68.75% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.44B |
| Stablecoin supply | $15.74B |
| DEX volume (24h) | $2.77B (-7.95% 1d) |
| App fees (24h, all protocols) | $11.08M |
| Chain fees (24h) | $776.70K |
| Jito MEV tips (24h) | $148.55K |
| **REV - Real Economic Value (24h)** | **$925.25K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.20B | +6.54% |
| USDT | $2.74B | -7.43% |
| USDGO | $1.19B | +1.62% |
| USD1 | $1.06B | +0.86% |
| BUIDL | $740.74M | -0.02% |
| PYUSD | $687.15M | +1.47% |
| USDG | $618.39M | -2.72% |
| USDe | $536.65M | -0.32% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $485.33M |
| BisonFi | $465.64M |
| Orca DEX | $356.49M |
| Raydium AMM | $246.95M |
| Manifest Trade | $232.59M |
| Meteora DLMM | $167.53M |
| Scorch | $153.48M |
| Tessera V | $109.10M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.77M |
| pump.fun | $1.76M |
| Axiom | $1.40M |
| Jupiter Perpetual Exchange | $465.48K |
| fomo Wallet | $450.16K |
| Raydium AMM | $447.39K |
| Meteora DLMM | $391.65K |
| Collector Crypt | $350.21K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 304 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $423.65M |
| xStocks 24h DEX volume | $29.41M |
| xStocks holder positions | 272.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

Top tokenized equities: TSLAX ($66.00M), CRCLX ($65.75M), SPYX ($46.80M), MSTRX ($46.55M), GOOGLX ($31.55M)

## Program activity and chain health

Chain tip lag: **+14.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 42,492 (approx.) | 91.90% | 0.7 s |
| SPL Token | 37,239 | 29.40% | 1.1 s |
| Jupiter v6 | 4,970 | 55.70% | 12 s |
| Orca Whirlpools | 2,083 | 31.60% | 28.7 s |
| Raydium AMM v4 | 803 | 16.20% | 74.5 s |

Median failure rate across the sampled programs: **31.60%** (range 16.20% to 91.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **577.72 SOL**.

## Exchange and large-holder balances

13.10M SOL ($1.20B) across 8 publicly-attributed accounts. Net **147K SOL (1.13%) moved onto exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $999.78M | 1/h | 0 |
| Binance (2) | 1.17M | $107.07M | 1.0K/h | 0 |
| Bybit | 369.70K | $33.88M | 59/h | 0 |
| Gate.io | 369.08K | $33.83M | 219/h | 0 |
| Coinbase (2) | 135.95K | $12.46M | 816.3/h | 0 |
| Coinbase | 62.67K | $5.74M | 685.7/h | 0 |
| Bitget | 49.47K | $4.53M | 263.4/h | 0 |
| Kraken | 36.63K | $3.36M | 368.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 526 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.222 | 485 | 0.0000 |
| DEX volume moves with App fees | +0.209 | 485 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.189 | 492 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.179 | 451 | 0.0001 |
| Total TPS moves with Slot time | +0.149 | 492 | 0.0009 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 681.22K USD | DeFiLlama: 776.70K USD | -13.10% | *indicative*: 0.88x, within the order-of-magnitude band |
| SOL price | coingecko: 91.65 USD | Jupiter (on-chain DEX): 91.57 USD | +0.09% | agree |
| Circulating supply | getSupply (RPC): 583.18M SOL | CoinGecko: 583.18M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-20
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21)

**Latest Firedancer release:** [v0.1106.40201](https://github.com/firedancer-io/firedancer/releases/tag/v0.1106.40201) (2026-08-19)

## Ecosystem news

- **[South Korea’s Shinhan partners with Solana Foundation, Etherfuse, Orca for tokenized fund issuance](https://www.theblock.co/news/regulation/2026-08-21-south-korea-shinhan-partners-solana-412420)** - The Block, 2026-08-21
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06
- **[Webinar Recap: Giving AI agents a native way to pay with x402](https://solana.com/news/webinar-recap-agentic-payments)** - Solana.com, 2026-08-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
