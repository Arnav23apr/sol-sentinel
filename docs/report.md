# Solana Ecosystem Report

*Generated 2026-08-22 08:54 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 21.7 robust standard deviations above its 7-day baseline: a 1700.0% move to 0.31 % from a typical 0.02.
- 🔴 **SOL price** (critical): SOL price is 11.4 robust standard deviations above its 7-day baseline: a 22.7% move to 93.67 USD from a typical 76.33.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 9.0 robust standard deviations above its 7-day baseline: a 14.7% move to 5,579,694,557.00 USD from a typical 4,862,971,825.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.6K |
| Slot time | 364.8 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1020 (57.14% complete, ~18.8h remaining) |
| Lifetime transactions | 540.6B |
| Circulating supply | 583.2M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,830 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 29,000 / 374,693 lamports |
| Paying no priority fee | 16.30% of 7,771 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 5.30% of slots needed a priority fee (max 1.2M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 684 |
| Delinquent validators | 10 |
| Delinquent stake | 0.31% |
| Total active stake | 432.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.33% / 24.40% / 35.80% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.35% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.95% | 7% |
| 2 | `he1i…uBtk` | 16.1M | 3.71% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.82% | 0% |
| 4 | `Catz…Diqb` | 11.8M | 2.73% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.4M | 1.94% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $93.67 (+4.40% 24h) |
| Market cap | $54.63B (rank #7) |
| 24h volume | $8.83B |
| ATH | $293.31 (-68.06% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.58B |
| Stablecoin supply | $15.88B |
| DEX volume (24h) | $3.47B (+25.26% 1d) |
| App fees (24h, all protocols) | $13.20M |
| Chain fees (24h) | $898.90K |
| Jito MEV tips (24h) | $194.31K |
| **REV - Real Economic Value (24h)** | **$1.09M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.28B | +8.41% |
| USDT | $2.74B | -5.52% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $677.17M | -0.22% |
| USDG | $620.25M | -1.55% |
| USDe | $536.80M | -0.29% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $600.74M |
| BisonFi | $562.98M |
| Orca DEX | $441.89M |
| Raydium AMM | $284.68M |
| Manifest Trade | $242.55M |
| Meteora DLMM | $237.06M |
| HumidiFi | $213.79M |
| Scorch | $153.48M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.22M |
| pump.fun | $1.78M |
| Axiom | $1.42M |
| Jupiter Perpetual Exchange | $619.81K |
| Meteora DLMM | $506.71K |
| Raydium AMM | $476.13K |
| Sanctum Validator LSTs | $455.86K |
| fomo Wallet | $450.16K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 300 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $423.94M |
| xStocks 24h DEX volume | $35.08M |
| xStocks holder positions | 273.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($65.59M), CRCLX ($65.55M), MSTRX ($47.30M), SPYX ($47.08M), GOOGLX ($31.37M)

## Program activity and chain health

Chain tip lag: **+13.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 28,816 | 21.30% | 1.8 s |
| Jupiter v6 | 5,184 | 72.40% | 9.1 s |
| Pump.fun | 3,987 | 53.00% | 15 s |
| Orca Whirlpools | 1,708 | 56.70% | 35 s |
| Raydium AMM v4 | 737 | 18.20% | 81 s |

Median failure rate across the sampled programs: **53.00%** (range 18.20% to 72.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **46.42 SOL**.

## Exchange and large-holder balances

12.93M SOL ($1.21B) across 8 publicly-attributed accounts. Net **86K SOL (0.66%) moved off exchanges** over the last 23.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.02B | 0.9/h | 0 |
| Binance (2) | 1.09M | $102.36M | 1.6K/h | 0 |
| Gate.io | 388.71K | $36.41M | 572.3/h | 0 |
| Bybit | 373.02K | $34.94M | 85.2/h | 0 |
| Coinbase (2) | 74.01K | $6.93M | 286.4/h | 0 |
| Bitget | 41.07K | $3.85M | 259.6/h | 0 |
| Coinbase | 29.50K | $2.76M | 232.6/h | 0 |
| Kraken | 24.57K | $2.30M | 261.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 6 of 117 tested pairs survive, over 551 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.204 | 510 | 0.0000 |
| DEX volume moves with App fees | +0.194 | 510 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 517 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 517 | 0.0005 |
| AMM write-lock congestion moves with Program failure rate | +0.151 | 476 | 0.0009 |
| Slot time moves with AMM write-lock congestion | +0.145 | 476 | 0.0015 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 543.38K USD | DeFiLlama: 898.90K USD | -49.30% | *indicative*: 0.60x, within the order-of-magnitude band |
| SOL price | coingecko: 93.67 USD | Jupiter (on-chain DEX): 93.78 USD | -0.12% | agree |
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

- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
- **[South Korea’s Shinhan partners with Solana Foundation, Etherfuse, Orca for tokenized fund issuance](https://www.theblock.co/news/regulation/2026-08-21-south-korea-shinhan-partners-solana-412420)** - The Block, 2026-08-21
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
