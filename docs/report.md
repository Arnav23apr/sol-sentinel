# Solana Ecosystem Report

*Generated 2026-08-26 20:19 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 6.4 robust standard deviations above its 7-day baseline: a 602.6% move to 0.27 % from a typical 0.04.
- 🟠 **Delinquent validators** (warning): Delinquent validators is 4.0 robust standard deviations above its 7-day baseline: a 66.7% move to 15.00 from a typical 9.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.9K |
| Slot time | 369.2 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1023 (1.88% complete, ~43.5h remaining) |
| Lifetime transactions | 542.1B |
| Circulating supply | 584.1M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,500 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 30,923 / 419,171 lamports |
| Paying no priority fee | 21.50% of 7,034 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 38.70% of slots needed a priority fee (max 25.4M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 681 |
| Delinquent validators | 15 |
| Delinquent stake | 0.27% |
| Total active stake | 435.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.23% / 24.34% / 35.67% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.09% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.83% | 0% |
| 4 | `Catz…Diqb` | 11.8M | 2.70% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `8Gbw…F8iD` | 9.1M | 2.08% | 0% |
| 7 | `51JB…UNAm` | 8.9M | 2.04% | 10% |
| 8 | `9QU2…29mF` | 7.8M | 1.80% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.68% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $96.82 (-1.20% 24h) |
| Market cap | $56.55B (rank #7) |
| 24h volume | $3.01B |
| ATH | $293.31 (-66.99% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.57B |
| Stablecoin supply | $15.89B |
| DEX volume (24h) | $2.93B (-2.04% 1d) |
| App fees (24h, all protocols) | $13.24M |
| Chain fees (24h) | $889.16K |
| Jito MEV tips (24h) | $221.95K |
| **REV - Real Economic Value (24h)** | **$1.11M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.98B | +3.02% |
| USDT | $2.84B | -0.87% |
| USDGO | $1.25B | +5.18% |
| USD1 | $1.12B | +6.90% |
| BUIDL | $876.47M | +18.21% |
| PYUSD | $678.42M | +0.28% |
| USDG | $614.48M | -2.86% |
| USDe | $537.00M | -0.11% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $567.89M |
| BisonFi | $411.40M |
| Orca DEX | $278.45M |
| Meteora DLMM | $246.36M |
| Scorch | $173.07M |
| Raydium AMM | $162.18M |
| Manifest Trade | $115.89M |
| pump.fun | $112.18M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.81M |
| pump.fun | $1.95M |
| Axiom | $1.60M |
| Bags | $1.45M |
| fomo Wallet | $664.84K |
| Jupiter Perpetual Exchange | $631.25K |
| Meteora DLMM | $507.74K |
| Raydium AMM | $285.49K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 323 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $427.04M |
| xStocks 24h DEX volume | $29.85M |
| xStocks holder positions | 279.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: CRCLX ($65.43M), TSLAX ($63.52M), SPYX ($48.79M), MSTRX ($48.55M), GOOGLX ($30.70M)

## Program activity and chain health

Chain tip lag: **+13.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 84,670 (approx.) | 49.20% | 0.4 s |
| Pump.fun | 32,421 | 87.90% | 1.5 s |
| Jupiter v6 | 8,384 | 73.60% | 6.3 s |
| Orca Whirlpools | 4,311 | 54.90% | 12.6 s |
| Raydium AMM v4 | 2,025 | 31.90% | 29.5 s |

Median failure rate across the sampled programs: **54.90%** (range 31.90% to 87.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.03K SOL**.

## Exchange and large-holder balances

12.39M SOL ($1.20B) across 8 publicly-attributed accounts. Net **335K SOL (2.64%) moved off exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.41M | $910.95M | 1.1/h | 9 |
| Binance (2) | 2.08M | $201.41M | 1.0K/h | 0 |
| Bybit | 377.26K | $36.53M | 21/h | 0 |
| Gate.io | 356.45K | $34.51M | 144.3/h | 0 |
| Bitget | 77.60K | $7.51M | 184.6/h | 0 |
| Kraken | 40.09K | $3.88M | 277.3/h | 0 |
| Coinbase (2) | 28.65K | $2.77M | 557.3/h | 0 |
| Coinbase | 23.37K | $2.26M | 1.1K/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 9 of 117 tested pairs survive, over 704 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.216 | 663 | 0.0000 |
| DEX volume moves with App fees | +0.199 | 663 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.187 | 670 | 0.0000 |
| Total TPS moves with Slot time | +0.150 | 670 | 0.0001 |
| AMM write-lock congestion moves with Program failure rate | +0.120 | 629 | 0.0025 |
| Non-vote TPS moves with AMM write-lock congestion | +0.118 | 629 | 0.0031 |
| Non-vote TPS moves with Activity index | +0.117 | 669 | 0.0024 |
| Total TPS moves with AMM write-lock congestion | +0.116 | 629 | 0.0036 |
| Slot time moves with AMM write-lock congestion | +0.116 | 629 | 0.0036 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 608.62K USD | DeFiLlama: 889.16K USD | -37.46% | *indicative*: 0.68x, within the order-of-magnitude band |
| SOL price | coingecko: 96.82 USD | Jupiter (on-chain DEX): 96.70 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 584.06M SOL | CoinGecko: 584.06M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-08-26
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-08-26
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-26
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-26
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-26
- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-25

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

- **[Galaxy Opens Retail Crypto-Backed Credit Lines on Bitcoin, Ethereum and Solana](https://decrypt.co/376646/galaxy-crypto-credit-lines-bitcoin-ethereum-solana)** - Decrypt, 2026-08-26
- **[Solana Treasury Firm Invites Investors to Look 'Beyond the Price of SOL'](https://decrypt.co/376619/solana-treasury-sol-data-beyond-price)** - Decrypt, 2026-08-26
- **[SOL treasury firm DeFi Development launches real-time ‘State of Solana’ intelligence platform](https://www.theblock.co/news/markets/2026-08-26-sol-treasury-firm-defi-development-launches-real-time-state-of-solana-intelligence-platform-412798)** - The Block, 2026-08-26
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
