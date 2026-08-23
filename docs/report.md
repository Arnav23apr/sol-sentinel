# Solana Ecosystem Report

*Generated 2026-08-23 13:08 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 55.4 robust standard deviations above its 7-day baseline: a 4930.0% move to 1.01 % from a typical 0.02.
- 🟠 **Delinquent validators** (warning): Delinquent validators is 4.0 robust standard deviations above its 7-day baseline: a 75.0% move to 14.00 from a typical 8.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.5K |
| Slot time | 361.4 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1021 (21.33% complete, ~34.1h remaining) |
| Lifetime transactions | 541.0B |
| Circulating supply | 583.3M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,447 lamports (about $0.00052) |
| Transaction fee p90 / p99 | 21,000 / 410,000 lamports |
| Paying no priority fee | 21.10% of 5,362 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 18.70% of slots needed a priority fee (max 6.3M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 681 |
| Delinquent validators | 14 |
| Delinquent stake | 1.01% |
| Total active stake | 429.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.55% / 36.05% |
| Commission (stake-weighted, delegatable validators) | 3.84% |
| Stake on private (100% commission) validators | 24.47% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.96% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.74% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.7M | 2.73% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.5M | 1.98% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.85% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.72% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.53% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $94.67 (+1.40% 24h) |
| Market cap | $55.22B (rank #7) |
| 24h volume | $4.41B |
| ATH | $293.31 (-67.72% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.55B |
| Stablecoin supply | $15.89B |
| DEX volume (24h) | $3.73B (+3.65% 1d) |
| App fees (24h, all protocols) | $11.92M |
| Chain fees (24h) | $785.84K |
| Jito MEV tips (24h) | $147.79K |
| **REV - Real Economic Value (24h)** | **$933.63K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.21B | +7.47% |
| USDT | $2.83B | -2.24% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $687.95M | +1.39% |
| USDG | $608.87M | -4.18% |
| USDe | $536.62M | -0.21% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $584.36M |
| PumpSwap | $570.01M |
| Orca DEX | $430.84M |
| Meteora DLMM | $377.27M |
| Scorch | $363.43M |
| Raydium AMM | $243.78M |
| Tessera V | $175.26M |
| Manifest Trade | $142.42M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.01M |
| pump.fun | $1.50M |
| Axiom | $1.16M |
| Jupiter Perpetual Exchange | $1.04M |
| Meteora DLMM | $985.54K |
| fomo Wallet | $476.50K |
| Raydium AMM | $413.20K |
| Orca DEX | $287.65K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 240 |
| Persistently-active cohort (capture-recapture est.) | 2.1K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $419.56M |
| xStocks 24h DEX volume | $7.46M |
| xStocks holder positions | 273.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($65.79M), CRCLX ($63.54M), SPYX ($47.15M), MSTRX ($45.03M), GOOGLX ($31.34M)

## Program activity and chain health

Chain tip lag: **+13.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 47,316 | 17.70% | 1.1 s |
| Pump.fun | 10,636 | 76.60% | 5.4 s |
| Jupiter v6 | 3,082 | 38.30% | 19.2 s |
| Orca Whirlpools | 2,470 | 30.20% | 24.2 s |
| Raydium AMM v4 | 889 | 9.50% | 67.2 s |

Median failure rate across the sampled programs: **30.20%** (range 9.50% to 76.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **522.68 SOL**.

## Exchange and large-holder balances

13.09M SOL ($1.24B) across 8 publicly-attributed accounts. Net **86K SOL (0.66%) moved onto exchanges** over the last 23.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.03B | 1.1/h | 0 |
| Binance (2) | 1.24M | $117.66M | 1.0K/h | 0 |
| Gate.io | 434.02K | $41.09M | 119.8/h | 0 |
| Bybit | 373.02K | $35.31M | 33.1/h | 0 |
| Kraken | 39.32K | $3.72M | 206.4/h | 0 |
| Coinbase (2) | 36.87K | $3.49M | 293.9/h | 0 |
| Bitget | 31.79K | $3.01M | 186.3/h | 0 |
| Coinbase | 23.36K | $2.21M | 233.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 8 of 117 tested pairs survive, over 600 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.222 | 559 | 0.0000 |
| DEX volume moves with App fees | +0.211 | 559 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.186 | 566 | 0.0000 |
| Total TPS moves with Slot time | +0.148 | 566 | 0.0004 |
| Slot time moves with AMM write-lock congestion | +0.141 | 525 | 0.0012 |
| Non-vote TPS moves with AMM write-lock congestion | +0.137 | 525 | 0.0016 |
| Total TPS moves with AMM write-lock congestion | +0.135 | 525 | 0.0019 |
| AMM write-lock congestion moves with Program failure rate | +0.129 | 525 | 0.0031 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 377.79K USD | DeFiLlama: 785.84K USD | -70.13% | *indicative*: 0.48x, within the order-of-magnitude band |
| SOL price | coingecko: 94.67 USD | Jupiter (on-chain DEX): 94.70 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 583.28M SOL | CoinGecko: 583.28M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-21
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

- **[Solana cuts mainnet slot time to 350 milliseconds in first step toward 200ms goal](https://www.theblock.co/news/ecosystems/2026-08-22-solana-cuts-mainnet-slot-time-to-350-milliseconds-in-first-step-toward-200ms-goal-412521)** - The Block, 2026-08-22
- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
- **[South Korea’s Shinhan partners with Solana Foundation, Etherfuse, Orca for tokenized fund issuance](https://www.theblock.co/news/regulation/2026-08-21-south-korea-shinhan-partners-solana-412420)** - The Block, 2026-08-21
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
