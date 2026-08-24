# Solana Ecosystem Report

*Generated 2026-08-24 18:23 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 6.3 robust standard deviations above its 7-day baseline: a 671.9% move to 0.22 % from a typical 0.03.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.4K |
| TPS (non-vote) | 2.6K |
| Slot time | 367 ms |
| Slot | 441M |
| Block height | 420M |
| Epoch | 1021 (88.05% complete, ~5.3h remaining) |
| Lifetime transactions | 541.4B |
| Circulating supply | 583.3M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,450 lamports (about $0.00052) |
| Transaction fee p90 / p99 | 29,000 / 410,000 lamports |
| Paying no priority fee | 22.90% of 7,033 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 26.00% of slots needed a priority fee (max 3.5M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 684 |
| Delinquent validators | 11 |
| Delinquent stake | 0.22% |
| Total active stake | 432.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.36% / 35.77% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 24.29% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.71% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.82% | 0% |
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
| SOL price | $96.19 (+1.04% 24h) |
| Market cap | $56.10B (rank #7) |
| 24h volume | $5.10B |
| ATH | $293.31 (-67.21% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.62B |
| Stablecoin supply | $15.78B |
| DEX volume (24h) | $2.94B (-21.27% 1d) |
| App fees (24h, all protocols) | $12.65M |
| Chain fees (24h) | $696.89K |
| Jito MEV tips (24h) | $139.28K |
| **REV - Real Economic Value (24h)** | **$836.17K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.09B | +5.67% |
| USDT | $2.83B | -2.24% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.09B | +3.23% |
| BUIDL | $777.36M | +4.91% |
| PYUSD | $673.78M | -0.62% |
| USDG | $622.74M | -1.97% |
| USDe | $536.54M | -0.16% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $712.73M |
| BisonFi | $438.48M |
| Orca DEX | $392.12M |
| Scorch | $270.62M |
| Meteora DLMM | $269.04M |
| Raydium AMM | $192.60M |
| Manifest Trade | $160.05M |
| Tessera V | $87.16M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.25M |
| pump.fun | $1.42M |
| Axiom | $1.13M |
| Jupiter Perpetual Exchange | $651.76K |
| Meteora DLMM | $631.90K |
| fomo Wallet | $605.37K |
| Sanctum Validator LSTs | $403.69K |
| Raydium AMM | $336.89K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 304 |
| Persistently-active cohort (capture-recapture est.) | 2.7K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $422.56M |
| xStocks 24h DEX volume | $28.92M |
| xStocks holder positions | 274.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.96B |

Top tokenized equities: TSLAX ($64.31M), CRCLX ($64.08M), SPYX ($47.71M), MSTRX ($47.27M), GOOGLX ($31.49M)

## Program activity and chain health

Chain tip lag: **+14.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 67,193 (approx.) | 49.20% | 0.4 s |
| Pump.fun | 21,814 | 86.60% | 2.6 s |
| Jupiter v6 | 5,542 | 59.30% | 10.6 s |
| Orca Whirlpools | 4,075 | 51.50% | 14.3 s |
| Raydium AMM v4 | 2,248 | 40.80% | 26.4 s |

Median failure rate across the sampled programs: **51.50%** (range 40.80% to 86.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.30 SOL**.

## Exchange and large-holder balances

12.94M SOL ($1.24B) across 8 publicly-attributed accounts. Net **67K SOL (0.51%) moved off exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.05B | 1.3/h | 8 |
| Binance (2) | 1.09M | $105.05M | 2.0K/h | 0 |
| Gate.io | 405.11K | $38.97M | 260.9/h | 0 |
| Bybit | 373.02K | $35.88M | 44.9/h | 0 |
| Bitget | 70.48K | $6.78M | 250.2/h | 0 |
| Kraken | 39.46K | $3.80M | 363.3/h | 0 |
| Coinbase | 27.59K | $2.65M | 634.9/h | 0 |
| Coinbase (2) | 25.38K | $2.44M | 566/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 641 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.223 | 600 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.183 | 607 | 0.0000 |
| DEX volume moves with App fees | +0.183 | 600 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 566 | 0.0004 |
| Total TPS moves with Slot time | +0.145 | 607 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 645.05K USD | DeFiLlama: 696.89K USD | -7.73% | *indicative*: 0.93x, within the order-of-magnitude band |
| SOL price | coingecko: 96.19 USD | Jupiter (on-chain DEX): 96.10 USD | +0.09% | agree |
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

- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
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
