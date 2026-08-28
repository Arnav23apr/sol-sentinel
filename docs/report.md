# Solana Ecosystem Report

*Generated 2026-08-28 01:33 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 6.1 robust standard deviations above its 7-day baseline: a 15.5% move to 109.48 USD from a typical 94.79.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 8.3 robust standard deviations above its 7-day baseline: a 8.0% move to 6,008,382,169.00 USD from a typical 5,564,594,614.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 2.1K |
| Slot time | 365.9 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1023 (68.41% complete, ~13.9h remaining) |
| Lifetime transactions | 542.6B |
| Circulating supply | 584.1M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,612 lamports (about $0.00061) |
| Transaction fee p90 / p99 | 43,626 / 605,000 lamports |
| Paying no priority fee | 17.30% of 7,244 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 840.2K µlam/CU) |
| Node version (RPC) | 4.2.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 689 |
| Delinquent validators | 9 |
| Delinquent stake | 0.01% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.19% / 24.28% / 35.57% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.16% |

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
| SOL price | $109.48 (+7.64% 24h) |
| Market cap | $63.96B (rank #7) |
| 24h volume | $7.04B |
| ATH | $293.31 (-62.67% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.01B |
| Stablecoin supply | $16.00B |
| DEX volume (24h) | $2.94B (+25.02% 1d) |
| App fees (24h, all protocols) | $14.76M |
| Chain fees (24h) | $973.47K |
| Jito MEV tips (24h) | $280.58K |
| **REV - Real Economic Value (24h)** | **$1.25M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.06B | -0.47% |
| USDT | $2.84B | -0.87% |
| USDGO | $1.25B | +5.17% |
| USD1 | $1.14B | +7.41% |
| BUIDL | $886.45M | +19.71% |
| PYUSD | $690.83M | +3.45% |
| USDG | $620.67M | -1.45% |
| USDe | $537.80M | -0.01% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $765.13M |
| BisonFi | $416.99M |
| Orca DEX | $365.65M |
| Meteora DLMM | $245.52M |
| Raydium AMM | $180.41M |
| Manifest Trade | $179.83M |
| pump.fun | $144.47M |
| Axiom | $126.33M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.16M |
| pump.fun | $2.17M |
| Axiom | $1.92M |
| fomo Wallet | $759.04K |
| Meteora DLMM | $695.76K |
| Raydium AMM | $367.81K |
| Collector Crypt | $359.00K |
| pump.fun Mobile App | $337.97K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 327 |
| Persistently-active cohort (capture-recapture est.) | 3.3K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $441.65M |
| xStocks 24h DEX volume | $27.91M |
| xStocks holder positions | 282.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: CRCLX ($69.63M), TSLAX ($65.68M), MSTRX ($55.16M), SPYX ($49.15M), GOOGLX ($30.67M)

## Program activity and chain health

Chain tip lag: **+12.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 60,344 (approx.) | 26.10% | 0.7 s |
| Jupiter v6 | 8,334 | 75.70% | 6.2 s |
| Pump.fun | 8,233 | 66.00% | 7 s |
| Orca Whirlpools | 5,564 | 56.90% | 10.6 s |
| Raydium AMM v4 | 3,558 | 19.30% | 16.8 s |

Median failure rate across the sampled programs: **56.90%** (range 19.30% to 75.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.32 SOL**.

## Exchange and large-holder balances

12.30M SOL ($1.35B) across 8 publicly-attributed accounts. Net **189K SOL (1.51%) moved off exchanges** over the last 20.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.19M | $1.12B | 1/h | 11 |
| Binance (2) | 1.30M | $142.11M | 1.3K/h | 0 |
| Bybit | 377.26K | $41.30M | 82.2/h | 0 |
| Gate.io | 297.91K | $32.62M | 214/h | 0 |
| Bitget | 51.95K | $5.69M | 178.6/h | 0 |
| Coinbase (2) | 36.25K | $3.97M | 1.1K/h | 0 |
| Coinbase | 31.88K | $3.49M | 640.6/h | 0 |
| Kraken | 18.91K | $2.07M | 215.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 708 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.223 | 667 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.195 | 674 | 0.0000 |
| DEX volume moves with App fees | +0.167 | 667 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 674 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.129 | 633 | 0.0011 |
| Total TPS moves with AMM write-lock congestion | +0.127 | 633 | 0.0014 |
| Slot time moves with AMM write-lock congestion | +0.126 | 633 | 0.0015 |
| AMM write-lock congestion moves with Program failure rate | +0.124 | 633 | 0.0018 |
| Non-vote TPS moves with Activity index | +0.121 | 673 | 0.0017 |
| Total TPS moves with Activity index | +0.112 | 673 | 0.0036 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 815.66K USD | DeFiLlama: 973.47K USD | -17.64% | *indicative*: 0.84x, within the order-of-magnitude band |
| SOL price | coingecko: 109.48 USD | Jupiter (on-chain DEX): 109.37 USD | +0.10% | agree |
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
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-27

**Recently merged SIMDs:**

- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29

**Latest Agave release:** [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[DeFi Development Corp resumes Solana purchases, acquiring nearly 20,000 SOL](https://www.theblock.co/news/business/2026-08-27-defi-development-resumes-solana-purchases-acquiring-nearly-20000-sol-412932)** - The Block, 2026-08-27
- **[Solana Is Having Its Best Month Since 2024—With a Historic Governance Vote on Deck](https://decrypt.co/376706/solana-best-month-since-2024-historic-governance-vote)** - Decrypt, 2026-08-27
- **[Charles Schwab to add Solana, Avalanche and Chainlink to crypto trading platform](https://www.theblock.co/news/business/2026-08-27-charles-schwab-add-solana-avalanche-chainlink-to-crypto-trading-platform-412923)** - The Block, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[Galaxy Opens Retail Crypto-Backed Credit Lines on Bitcoin, Ethereum and Solana](https://decrypt.co/376646/galaxy-crypto-credit-lines-bitcoin-ethereum-solana)** - Decrypt, 2026-08-26
- **[Solana Treasury Firm Invites Investors to Look 'Beyond the Price of SOL'](https://decrypt.co/376619/solana-treasury-sol-data-beyond-price)** - Decrypt, 2026-08-26
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
