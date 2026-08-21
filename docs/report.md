# Solana Ecosystem Report

*Generated 2026-08-21 07:15 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 21.0 robust standard deviations above its 7-day baseline: a 19.8% move to 90.63 USD from a typical 75.68.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 11.1 robust standard deviations above its 7-day baseline: a 11.2% move to 5,379,119,247.00 USD from a typical 4,836,900,037.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.2K |
| TPS (non-vote) | 1.5K |
| Slot time | 411 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1019 (98.97% complete, ~0.5h remaining) |
| Lifetime transactions | 540.2B |
| Circulating supply | 583.1M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,389 lamports (about $0.00049) |
| Transaction fee p90 / p99 | 21,199 / 338,120 lamports |
| Paying no priority fee | 18.70% of 6,466 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 13.30% of slots needed a priority fee (max 3.2M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 7 |
| Delinquent stake | 0.02% |
| Total active stake | 435.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.38% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.21% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.4M | 2.85% | 5% |
| 4 | `3N7s…iD5g` | 12.2M | 2.80% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $90.63 (+6.20% 24h) |
| Market cap | $52.84B (rank #7) |
| 24h volume | $5.07B |
| ATH | $293.31 (-69.10% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.38B |
| Stablecoin supply | $15.87B |
| DEX volume (24h) | $2.78B (-7.60% 1d) |
| App fees (24h, all protocols) | $11.03M |
| Chain fees (24h) | $776.70K |
| Jito MEV tips (24h) | $150.26K |
| **REV - Real Economic Value (24h)** | **$926.96K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.22B | +6.83% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.15B | -1.37% |
| USD1 | $1.06B | +0.86% |
| BUIDL | $740.67M | -0.03% |
| PYUSD | $685.21M | +1.20% |
| USDG | $628.92M | -1.10% |
| USDe | $536.50M | -0.32% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $485.33M |
| BisonFi | $465.64M |
| Orca DEX | $277.61M |
| Raydium AMM | $259.80M |
| Manifest Trade | $202.40M |
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
| Raydium AMM | $525.60K |
| fomo Wallet | $500.29K |
| Jupiter Perpetual Exchange | $465.48K |
| Meteora DLMM | $391.65K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 321 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $412.11M |
| xStocks 24h DEX volume | $26.33M |
| xStocks holder positions | 272.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.91B |

Top tokenized equities: TSLAX ($63.53M), CRCLX ($62.65M), MSTRX ($46.17M), SPYX ($45.84M), GOOGLX ($30.53M)

## Program activity and chain health

Chain tip lag: **+16.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,387 (approx.) | 32.60% | 0.8 s |
| Jupiter v6 | 26,277 | 87.40% | 2.1 s |
| Pump.fun | 15,312 | 80.60% | 3.7 s |
| Orca Whirlpools | 10,994 | 72.00% | 5.3 s |
| Raydium AMM v4 | 1,694 | 48.40% | 35.3 s |

Median failure rate across the sampled programs: **72.00%** (range 32.60% to 87.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **37.35 SOL**.

## Exchange and large-holder balances

13.10M SOL ($1.19B) across 8 publicly-attributed accounts. Net **184K SOL (1.42%) moved onto exchanges** over the last 23.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $988.65M | 1.2/h | 0 |
| Binance (2) | 1.34M | $121.48M | 1.0K/h | 0 |
| Gate.io | 356.81K | $32.34M | 153.9/h | 0 |
| Bybit | 325.52K | $29.50M | 53.6/h | 0 |
| Bitget | 49.31K | $4.47M | 206.9/h | 0 |
| Coinbase (2) | 44.22K | $4.01M | 401.3/h | 0 |
| Coinbase | 41.64K | $3.77M | 574.2/h | 0 |
| Kraken | 36.66K | $3.32M | 190.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 512 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.232 | 471 | 0.0000 |
| DEX volume moves with App fees | +0.212 | 471 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.203 | 478 | 0.0000 |
| Total TPS moves with Slot time | +0.165 | 478 | 0.0003 |
| AMM write-lock congestion moves with Program failure rate | +0.159 | 437 | 0.0009 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 544.54K USD | DeFiLlama: 776.70K USD | -35.14% | *indicative*: 0.70x, within the order-of-magnitude band |
| SOL price | coingecko: 90.63 USD | Jupiter (on-chain DEX): 90.74 USD | -0.12% | agree |
| Circulating supply | getSupply (RPC): 583.06M SOL | CoinGecko: 583.06M SOL | -0.00% | agree |

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
