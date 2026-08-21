# Solana Ecosystem Report

*Generated 2026-08-21 21:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 15.0 robust standard deviations above its 7-day baseline: a 21.1% move to 91.86 USD from a typical 75.86.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 8.8 robust standard deviations above its 7-day baseline: a 12.2% move to 5,443,083,201.00 USD from a typical 4,849,288,954.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 2.3K |
| Slot time | 364.8 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1020 (30.58% complete, ~30.4h remaining) |
| Lifetime transactions | 540.5B |
| Circulating supply | 583.2M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,438 lamports (about $0.00050) |
| Transaction fee p90 / p99 | 22,000 / 455,000 lamports |
| Paying no priority fee | 17.30% of 6,661 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 15.5M µlam/CU) |
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
| SOL price | $91.86 (+5.20% 24h) |
| Market cap | $53.55B (rank #7) |
| 24h volume | $6.02B |
| ATH | $293.31 (-68.68% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.44B |
| Stablecoin supply | $15.83B |
| DEX volume (24h) | $2.77B (-7.95% 1d) |
| App fees (24h, all protocols) | $11.08M |
| Chain fees (24h) | $776.70K |
| Jito MEV tips (24h) | $148.62K |
| **REV - Real Economic Value (24h)** | **$925.31K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.27B | +7.62% |
| USDT | $2.74B | -7.43% |
| USDGO | $1.19B | +2.18% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $740.74M | -0.02% |
| PYUSD | $681.29M | +0.60% |
| USDG | $612.72M | -3.64% |
| USDe | $536.62M | -0.32% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $485.33M |
| BisonFi | $465.64M |
| Orca DEX | $375.25M |
| Manifest Trade | $236.71M |
| Raydium AMM | $228.33M |
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
| Raydium AMM | $405.09K |
| Meteora DLMM | $391.65K |
| Collector Crypt | $292.63K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 302 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $422.86M |
| xStocks 24h DEX volume | $29.94M |
| xStocks holder positions | 272.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($66.18M), CRCLX ($64.86M), SPYX ($46.98M), MSTRX ($46.50M), GOOGLX ($31.62M)

## Program activity and chain health

Chain tip lag: **+13.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 44,792 | 37.10% | 1.1 s |
| Pump.fun | 34,211 | 88.70% | 1.5 s |
| Jupiter v6 | 10,636 | 72.90% | 5.5 s |
| Orca Whirlpools | 4,184 | 72.60% | 14.2 s |
| Raydium AMM v4 | 1,051 | 48.10% | 55.8 s |

Median failure rate across the sampled programs: **72.60%** (range 37.10% to 88.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **110.96 SOL**.

## Exchange and large-holder balances

13.11M SOL ($1.20B) across 8 publicly-attributed accounts. Net **164K SOL (1.27%) moved onto exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.00B | 1/h | 0 |
| Binance (2) | 1.23M | $112.87M | 1.1K/h | 0 |
| Bybit | 369.67K | $33.96M | 46.2/h | 0 |
| Gate.io | 355.99K | $32.70M | 134.7/h | 0 |
| Coinbase (2) | 119.31K | $10.96M | 527.1/h | 0 |
| Bitget | 57.76K | $5.31M | 222.2/h | 0 |
| Kraken | 36.27K | $3.33M | 336.1/h | 0 |
| Coinbase | 30.95K | $2.84M | 526.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 534 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.219 | 493 | 0.0000 |
| DEX volume moves with App fees | +0.208 | 493 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.200 | 500 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.170 | 459 | 0.0003 |
| Total TPS moves with Slot time | +0.160 | 500 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 552.00K USD | DeFiLlama: 776.70K USD | -33.82% | *indicative*: 0.71x, within the order-of-magnitude band |
| SOL price | coingecko: 91.86 USD | Jupiter (on-chain DEX): 92.14 USD | -0.30% | agree |
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
