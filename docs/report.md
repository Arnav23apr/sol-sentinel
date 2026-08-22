# Solana Ecosystem Report

*Generated 2026-08-22 20:45 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 6.2 robust standard deviations above its 7-day baseline: a 22.6% move to 94.50 USD from a typical 77.10.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 4.6 robust standard deviations above its 7-day baseline: a 13.0% move to 5,536,174,037.00 USD from a typical 4,897,292,666.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.3K |
| TPS (non-vote) | 2.5K |
| Slot time | 364.8 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1020 (84.05% complete, ~7.0h remaining) |
| Lifetime transactions | 540.8B |
| Circulating supply | 583.2M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,353 lamports (about $0.00051) |
| Transaction fee p90 / p99 | 29,000 / 410,000 lamports |
| Paying no priority fee | 26.90% of 5,029 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 2.6M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 686 |
| Delinquent validators | 9 |
| Delinquent stake | 0.02% |
| Total active stake | 433.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.33% / 35.70% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.28% |

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
| SOL price | $94.50 (+3.80% 24h) |
| Market cap | $55.12B (rank #7) |
| 24h volume | $8.10B |
| ATH | $293.31 (-67.78% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.54B |
| Stablecoin supply | $15.86B |
| DEX volume (24h) | $3.60B (+30.15% 1d) |
| App fees (24h, all protocols) | $13.34M |
| Chain fees (24h) | $898.90K |
| Jito MEV tips (24h) | $177.49K |
| **REV - Real Economic Value (24h)** | **$1.08M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.23B | +7.53% |
| USDT | $2.79B | -3.79% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $679.29M | +0.09% |
| USDG | $607.15M | -3.65% |
| USDe | $536.95M | -0.29% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $635.95M |
| PumpSwap | $600.74M |
| BisonFi | $562.98M |
| Raydium AMM | $279.28M |
| Scorch | $242.28M |
| Meteora DLMM | $237.06M |
| HumidiFi | $213.79M |
| Manifest Trade | $190.37M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.22M |
| pump.fun | $1.78M |
| Axiom | $1.42M |
| Jupiter Perpetual Exchange | $619.81K |
| Meteora DLMM | $506.71K |
| fomo Wallet | $481.19K |
| Raydium AMM | $470.12K |
| Orca DEX | $469.94K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 268 |
| Persistently-active cohort (capture-recapture est.) | 2.7K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $417.98M |
| xStocks 24h DEX volume | $16.46M |
| xStocks holder positions | 273.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($65.65M), CRCLX ($62.73M), SPYX ($47.11M), MSTRX ($45.27M), GOOGLX ($31.44M)

## Program activity and chain health

Chain tip lag: **+13.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 78,125 (approx.) | 40.00% | 0.7 s |
| Pump.fun | 15,938 | 79.60% | 3.6 s |
| Raydium AMM v4 | 3,333 | 28.60% | 17.9 s |
| Jupiter v6 | 3,243 | 44.60% | 18.2 s |
| Orca Whirlpools | 1,437 | 53.80% | 41.6 s |

Median failure rate across the sampled programs: **44.60%** (range 28.60% to 79.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **37.86 SOL**.

## Exchange and large-holder balances

12.93M SOL ($1.22B) across 8 publicly-attributed accounts. Net **179K SOL (1.36%) moved off exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.03B | 1.1/h | 0 |
| Binance (2) | 1.08M | $102.52M | 1.3K/h | 0 |
| Bybit | 373.02K | $35.25M | 33.9/h | 1 |
| Gate.io | 356.94K | $33.73M | 176.2/h | 0 |
| Bitget | 84.93K | $8.03M | 184.6/h | 0 |
| Coinbase (2) | 51.76K | $4.89M | 457.4/h | 0 |
| Kraken | 42.58K | $4.02M | 179/h | 0 |
| Coinbase | 25.69K | $2.43M | 665.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 6 of 117 tested pairs survive, over 574 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.210 | 533 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.199 | 540 | 0.0000 |
| DEX volume moves with App fees | +0.198 | 533 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.161 | 499 | 0.0003 |
| Total TPS moves with Slot time | +0.160 | 540 | 0.0002 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 499 | 0.0023 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 414.61K USD | DeFiLlama: 898.90K USD | -73.74% | *indicative*: 0.46x, within the order-of-magnitude band |
| SOL price | coingecko: 94.50 USD | Jupiter (on-chain DEX): 94.49 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 583.18M SOL | CoinGecko: 583.18M SOL | -0.00% | agree |

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
