# Solana Ecosystem Report

*Generated 2026-08-23 04:07 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 14.4 robust standard deviations above its 7-day baseline: a 1285.0% move to 0.28 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.2K |
| Slot time | 363.6 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1021 (0.78% complete, ~43.3h remaining) |
| Lifetime transactions | 540.9B |
| Circulating supply | 583.3M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,915 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 29,000 / 410,000 lamports |
| Paying no priority fee | 14.60% of 5,984 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 16.00% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 684 |
| Delinquent validators | 11 |
| Delinquent stake | 0.28% |
| Total active stake | 432.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.30% / 24.37% / 35.79% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.29% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.71% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.83% | 0% |
| 4 | `Catz…Diqb` | 11.7M | 2.71% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.05% | 10% |
| 7 | `8Gbw…F8iD` | 8.5M | 1.96% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $93.45 (-2.00% 24h) |
| Market cap | $54.49B (rank #7) |
| 24h volume | $7.38B |
| ATH | $293.31 (-68.14% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.56B |
| Stablecoin supply | $15.89B |
| DEX volume (24h) | $3.65B (+1.31% 1d) |
| App fees (24h, all protocols) | $11.92M |
| Chain fees (24h) | $785.84K |
| Jito MEV tips (24h) | $179.16K |
| **REV - Real Economic Value (24h)** | **$965.00K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.25B | +8.05% |
| USDT | $2.79B | -3.79% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $688.02M | +1.39% |
| USDG | $606.13M | -4.61% |
| USDe | $536.88M | -0.19% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $586.23M |
| BisonFi | $584.36M |
| PumpSwap | $570.01M |
| Meteora DLMM | $377.27M |
| Raydium AMM | $278.73M |
| Scorch | $242.28M |
| Manifest Trade | $182.55M |
| Tessera V | $175.26M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.01M |
| pump.fun | $1.50M |
| Axiom | $1.16M |
| Jupiter Perpetual Exchange | $1.04M |
| Meteora DLMM | $985.54K |
| fomo Wallet | $481.19K |
| Raydium AMM | $477.82K |
| Orca DEX | $455.06K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 247 |
| Persistently-active cohort (capture-recapture est.) | 2.0K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $420.00M |
| xStocks 24h DEX volume | $15.32M |
| xStocks holder positions | 273.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($65.89M), CRCLX ($63.27M), SPYX ($47.12M), MSTRX ($45.41M), GOOGLX ($31.43M)

## Program activity and chain health

Chain tip lag: **+12.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 117,822 (approx.) | 27.90% | 0.4 s |
| Pump.fun | 12,211 | 82.00% | 4.4 s |
| Jupiter v6 | 7,830 | 67.70% | 7.3 s |
| Orca Whirlpools | 3,185 | 38.50% | 18.2 s |
| Raydium AMM v4 | 1,763 | 5.00% | 33.5 s |

Median failure rate across the sampled programs: **38.50%** (range 5.00% to 82.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **807.05 SOL**.

## Exchange and large-holder balances

12.82M SOL ($1.20B) across 8 publicly-attributed accounts. Net **57K SOL (0.44%) moved off exchanges** over the last 23.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.02B | 1.1/h | 0 |
| Binance (2) | 1.04M | $97.26M | 1.1K/h | 0 |
| Bybit | 373.02K | $34.86M | 40/h | 0 |
| Gate.io | 351.94K | $32.89M | 105.3/h | 0 |
| Kraken | 43.45K | $4.06M | 128.1/h | 0 |
| Coinbase (2) | 41.46K | $3.87M | 338/h | 0 |
| Bitget | 35.22K | $3.29M | 105.4/h | 0 |
| Coinbase | 27.60K | $2.58M | 396.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 6 of 117 tested pairs survive, over 584 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DEX volume moves with App fees | +0.223 | 543 | 0.0000 |
| DeFi TVL moves with xStocks AUM | +0.211 | 543 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.195 | 550 | 0.0000 |
| Total TPS moves with Slot time | +0.156 | 550 | 0.0002 |
| Slot time moves with AMM write-lock congestion | +0.144 | 509 | 0.0011 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 509 | 0.0022 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 450.09K USD | DeFiLlama: 785.84K USD | -54.33% | *indicative*: 0.57x, within the order-of-magnitude band |
| SOL price | coingecko: 93.45 USD | Jupiter (on-chain DEX): 93.24 USD | +0.22% | agree |
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
