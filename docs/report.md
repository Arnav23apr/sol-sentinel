# Solana Ecosystem Report

*Generated 2026-08-21 09:57 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 11.2 robust standard deviations above its 7-day baseline: a 588.2% move to 0.12 % from a typical 0.02.
- 🔴 **SOL price** (critical): SOL price is 20.6 robust standard deviations above its 7-day baseline: a 21.4% move to 91.90 USD from a typical 75.73.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 11.3 robust standard deviations above its 7-day baseline: a 12.5% move to 5,445,065,419.00 USD from a typical 4,840,167,093.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.3K |
| TPS (non-vote) | 2.5K |
| Slot time | 362.5 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1020 (4.99% complete, ~41.3h remaining) |
| Lifetime transactions | 540.3B |
| Circulating supply | 583.2M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,563 lamports (about $0.00051) |
| Transaction fee p90 / p99 | 29,000 / 410,000 lamports |
| Paying no priority fee | 20.20% of 8,137 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 21.30% of slots needed a priority fee (max 7.1M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 681 |
| Delinquent validators | 13 |
| Delinquent stake | 0.12% |
| Total active stake | 433.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.30% / 24.35% / 35.73% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.25% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.1M | 3.71% | 0% |
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
| SOL price | $91.90 (+8.10% 24h) |
| Market cap | $53.61B (rank #7) |
| 24h volume | $5.65B |
| ATH | $293.31 (-68.67% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.45B |
| Stablecoin supply | $15.76B |
| DEX volume (24h) | $2.78B (-7.60% 1d) |
| App fees (24h, all protocols) | $11.04M |
| Chain fees (24h) | $776.70K |
| Jito MEV tips (24h) | $150.91K |
| **REV - Real Economic Value (24h)** | **$927.61K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.24B | +7.10% |
| USDT | $2.74B | -7.43% |
| USDGO | $1.15B | -1.37% |
| USD1 | $1.06B | +0.86% |
| BUIDL | $740.67M | -0.03% |
| PYUSD | $688.27M | +1.62% |
| USDG | $628.91M | -1.10% |
| USDe | $536.54M | -0.32% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $485.33M |
| BisonFi | $465.64M |
| Orca DEX | $306.56M |
| Raydium AMM | $252.67M |
| Manifest Trade | $210.13M |
| Meteora DLMM | $167.53M |
| Scorch | $137.28M |
| Tessera V | $109.10M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.77M |
| pump.fun | $1.76M |
| Axiom | $1.40M |
| Collector Crypt | $525.87K |
| Raydium AMM | $501.33K |
| fomo Wallet | $500.29K |
| Jupiter Perpetual Exchange | $465.48K |
| Meteora DLMM | $391.65K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 386 |
| Persistently-active cohort (capture-recapture est.) | 3.7K |
| Unique payers across sampled blocks | 2.2K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $417.73M |
| xStocks 24h DEX volume | $26.82M |
| xStocks holder positions | 272.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.91B |

Top tokenized equities: CRCLX ($65.02M), TSLAX ($63.70M), MSTRX ($47.85M), SPYX ($45.89M), GOOGLX ($30.68M)

## Program activity and chain health

Chain tip lag: **+14.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 52,028 | 22.70% | 1.1 s |
| Pump.fun | 13,752 | 77.20% | 4.3 s |
| Jupiter v6 | 10,626 | 74.70% | 5.4 s |
| Orca Whirlpools | 6,086 | 65.30% | 9.4 s |
| Raydium AMM v4 | 1,812 | 47.00% | 33 s |

Median failure rate across the sampled programs: **65.30%** (range 22.70% to 77.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.01K SOL**.

## Exchange and large-holder balances

13.02M SOL ($1.20B) across 8 publicly-attributed accounts. Net **107K SOL (0.83%) moved onto exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.00B | 1.1/h | 0 |
| Binance (2) | 1.22M | $111.96M | 1.1K/h | 0 |
| Gate.io | 382.60K | $35.16M | 217.3/h | 0 |
| Bybit | 369.70K | $33.98M | 108.6/h | 0 |
| Bitget | 50.14K | $4.61M | 352.9/h | 0 |
| Coinbase | 33.67K | $3.09M | 477.5/h | 0 |
| Coinbase (2) | 32.50K | $2.99M | 409.6/h | 0 |
| Kraken | 28.23K | $2.59M | 278.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 515 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.240 | 474 | 0.0000 |
| DEX volume moves with App fees | +0.211 | 474 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.199 | 481 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.168 | 440 | 0.0004 |
| Total TPS moves with Slot time | +0.161 | 481 | 0.0004 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 571.82K USD | DeFiLlama: 776.70K USD | -30.39% | *indicative*: 0.74x, within the order-of-magnitude band |
| SOL price | coingecko: 91.90 USD | Jupiter (on-chain DEX): 91.50 USD | +0.44% | agree |
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

**Latest Agave release:** [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) (2026-08-13)

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
