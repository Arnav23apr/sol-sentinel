# Solana Ecosystem Report

*Generated 2026-08-25 21:49 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.7 robust standard deviations above its 7-day baseline: a 445.5% move to 0.18 % from a typical 0.03.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.3K |
| Slot time | 365.9 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1022 (50.56% complete, ~21.7h remaining) |
| Lifetime transactions | 541.8B |
| Circulating supply | 583.4M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,563 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 30,000 / 410,000 lamports |
| Paying no priority fee | 19.00% of 7,106 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 92.00% of slots needed a priority fee (max 1.3M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 10 |
| Delinquent stake | 0.18% |
| Total active stake | 434.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.27% / 24.32% / 35.69% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.20% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.69% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 4 | `Catz…Diqb` | 11.7M | 2.70% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.05% | 10% |
| 7 | `8Gbw…F8iD` | 8.6M | 1.98% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.68% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $97.07 (-0.13% 24h) |
| Market cap | $56.63B (rank #7) |
| 24h volume | $6.11B |
| ATH | $293.31 (-66.91% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.63B |
| Stablecoin supply | $15.93B |
| DEX volume (24h) | $3.00B (+1.96% 1d) |
| App fees (24h, all protocols) | $14.49M |
| Chain fees (24h) | $928.73K |
| Jito MEV tips (24h) | $199.25K |
| **REV - Real Economic Value (24h)** | **$1.13M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.04B | +4.57% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.24B | +4.34% |
| USD1 | $1.11B | +5.61% |
| BUIDL | $876.38M | +18.21% |
| PYUSD | $668.29M | -0.76% |
| USDG | $635.73M | -0.18% |
| USDe | $536.93M | -0.13% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $694.81M |
| Orca DEX | $449.27M |
| BisonFi | $409.15M |
| Meteora DLMM | $278.05M |
| Scorch | $218.92M |
| Manifest Trade | $203.13M |
| Raydium AMM | $195.48M |
| pump.fun | $95.40M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.03M |
| pump.fun | $1.82M |
| Axiom | $1.54M |
| fomo Wallet | $585.96K |
| Meteora DLMM | $575.35K |
| Sanctum Validator LSTs | $430.20K |
| Jupiter Perpetual Exchange | $413.47K |
| Phantom Wallet | $316.76K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 320 |
| Persistently-active cohort (capture-recapture est.) | 3.2K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $431.32M |
| xStocks 24h DEX volume | $24.11M |
| xStocks holder positions | 276.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.06B |

Top tokenized equities: CRCLX ($67.13M), TSLAX ($64.19M), MSTRX ($50.24M), SPYX ($48.06M), GOOGLX ($31.06M)

## Program activity and chain health

Chain tip lag: **+14.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | >163,979 | 42.20% | 0.4 s |
| Pump.fun | 20,333 | 76.80% | 2.9 s |
| Jupiter v6 | 5,099 | 59.20% | 11.7 s |
| Orca Whirlpools | 1,741 | 44.10% | 34.4 s |
| Raydium AMM v4 | 1,555 | 31.30% | 38.4 s |

Median failure rate across the sampled programs: **44.10%** (range 31.30% to 76.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.31 SOL**.

## Exchange and large-holder balances

12.72M SOL ($1.23B) across 8 publicly-attributed accounts. Net **186K SOL (1.44%) moved off exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.41M | $913.30M | 1.2/h | 9 |
| Binance (2) | 2.37M | $230.19M | 888.9/h | 0 |
| Gate.io | 382.20K | $37.10M | 193.5/h | 0 |
| Bybit | 377.27K | $36.62M | 447.8/h | 0 |
| Bitget | 67.88K | $6.59M | 183/h | 0 |
| Coinbase | 39.29K | $3.81M | 481.9/h | 0 |
| Kraken | 35.30K | $3.43M | 292.9/h | 0 |
| Coinbase (2) | 33.87K | $3.29M | 498.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 7 of 117 tested pairs survive, over 680 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.221 | 639 | 0.0000 |
| DEX volume moves with App fees | +0.188 | 639 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.184 | 646 | 0.0000 |
| Total TPS moves with Slot time | +0.146 | 646 | 0.0002 |
| Non-vote TPS moves with AMM write-lock congestion | +0.121 | 605 | 0.0030 |
| Slot time moves with AMM write-lock congestion | +0.121 | 605 | 0.0029 |
| Non-vote TPS moves with Activity index | +0.118 | 645 | 0.0027 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 666.03K USD | DeFiLlama: 928.73K USD | -32.94% | *indicative*: 0.72x, within the order-of-magnitude band |
| SOL price | coingecko: 97.07 USD | Jupiter (on-chain DEX): 97.09 USD | -0.02% | agree |
| Circulating supply | getSupply (RPC): 583.38M SOL | CoinGecko: 583.38M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-08-25
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-08-25
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-25
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-25
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-25
- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-24

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
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
