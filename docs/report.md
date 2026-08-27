# Solana Ecosystem Report

*Generated 2026-08-27 05:34 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.4K |
| Slot time | 364.8 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1023 (22.95% complete, ~33.7h remaining) |
| Lifetime transactions | 542.3B |
| Circulating supply | 584.1M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,895 lamports (about $0.00060) |
| Transaction fee p90 / p99 | 29,000 / 425,000 lamports |
| Paying no priority fee | 13.80% of 6,938 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 317.3K µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 686 |
| Delinquent validators | 11 |
| Delinquent stake | 0.02% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.20% / 24.28% / 35.58% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.03% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.91% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.67% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 4 | `Catz…Diqb` | 11.8M | 2.69% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `8Gbw…F8iD` | 9.1M | 2.07% | 0% |
| 7 | `51JB…UNAm` | 8.9M | 2.04% | 10% |
| 8 | `9QU2…29mF` | 7.8M | 1.80% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.67% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $100.95 (+4.13% 24h) |
| Market cap | $58.96B (rank #7) |
| 24h volume | $3.86B |
| ATH | $293.31 (-65.58% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.77B |
| Stablecoin supply | $15.93B |
| DEX volume (24h) | $2.48B (-15.46% 1d) |
| App fees (24h, all protocols) | $14.68M |
| Chain fees (24h) | $889.16K |
| Jito MEV tips (24h) | $236.01K |
| **REV - Real Economic Value (24h)** | **$1.13M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.00B | -1.33% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.25B | +5.18% |
| USD1 | $1.13B | +6.94% |
| BUIDL | $886.37M | +19.70% |
| PYUSD | $684.28M | +2.55% |
| USDG | $625.23M | -0.72% |
| USDe | $536.93M | -0.11% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $765.13M |
| Orca DEX | $315.18M |
| BisonFi | $251.44M |
| Meteora DLMM | $184.81M |
| Scorch | $173.07M |
| Raydium AMM | $159.97M |
| Manifest Trade | $121.56M |
| Axiom | $88.92M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.81M |
| pump.fun | $1.95M |
| Axiom | $1.92M |
| fomo Wallet | $664.84K |
| Jupiter Perpetual Exchange | $631.25K |
| Meteora DLMM | $507.74K |
| Sanctum Validator LSTs | $429.89K |
| pump.fun Mobile App | $337.97K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 286 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $428.98M |
| xStocks 24h DEX volume | $37.51M |
| xStocks holder positions | 280.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: CRCLX ($65.37M), TSLAX ($63.77M), MSTRX ($49.20M), SPYX ($48.99M), GOOGLX ($30.75M)

## Program activity and chain health

Chain tip lag: **+13.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 46,601 | 31.40% | 1.1 s |
| Pump.fun | 6,695 | 76.10% | 8.8 s |
| Jupiter v6 | 4,427 | 59.40% | 13.5 s |
| Raydium AMM v4 | 1,528 | 31.00% | 39 s |
| Orca Whirlpools | 1,378 | 56.90% | 43.4 s |

Median failure rate across the sampled programs: **56.90%** (range 31.00% to 76.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **517.61 SOL**.

## Exchange and large-holder balances

12.49M SOL ($1.26B) across 8 publicly-attributed accounts. Net **164K SOL (1.29%) moved off exchanges** over the last 23.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.19M | $1.03B | 1/h | 9 |
| Binance (2) | 1.40M | $140.93M | 970.4/h | 0 |
| Bybit | 377.26K | $38.08M | 26.7/h | 0 |
| Gate.io | 336.20K | $33.94M | 144.2/h | 0 |
| Bitget | 94.53K | $9.54M | 163/h | 0 |
| Kraken | 40.87K | $4.13M | 190/h | 0 |
| Coinbase | 29.34K | $2.96M | 348.5/h | 0 |
| Coinbase (2) | 27.13K | $2.74M | 585.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 706 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.216 | 665 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.189 | 672 | 0.0000 |
| DEX volume moves with App fees | +0.188 | 665 | 0.0000 |
| Total TPS moves with Slot time | +0.152 | 672 | 0.0001 |
| Non-vote TPS moves with AMM write-lock congestion | +0.121 | 631 | 0.0023 |
| Non-vote TPS moves with Activity index | +0.120 | 671 | 0.0019 |
| Total TPS moves with AMM write-lock congestion | +0.119 | 631 | 0.0027 |
| Slot time moves with AMM write-lock congestion | +0.119 | 631 | 0.0027 |
| AMM write-lock congestion moves with Program failure rate | +0.118 | 631 | 0.0029 |
| Total TPS moves with Activity index | +0.111 | 671 | 0.0041 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 687.72K USD | DeFiLlama: 889.16K USD | -25.55% | *indicative*: 0.77x, within the order-of-magnitude band |
| SOL price | coingecko: 100.95 USD | Jupiter (on-chain DEX): 100.86 USD | +0.09% | agree |
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
