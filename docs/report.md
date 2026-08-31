# Solana Ecosystem Report

*Generated 2026-08-31 06:39 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 18.6 robust standard deviations below its 7-day baseline: a 36.6% move to 1,869,646,571.00 USD from a typical 2,948,781,265.00.
- 🔴 **Delinquent validators** (critical): Delinquent validators is 6.1 robust standard deviations above its 7-day baseline: a 90.0% move to 19.00 from a typical 10.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.0K |
| Slot time | 317.5 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1025 (66.05% complete, ~12.9h remaining) |
| Lifetime transactions | 543.7B |
| Circulating supply | 585.1M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,415 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 40,000 / 305,001 lamports |
| Paying no priority fee | 25.00% of 5,916 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 3.2M µlam/CU) |
| Node version (RPC) | 4.2.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 19 |
| Delinquent stake | 0.03% |
| Total active stake | 437.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.24% / 24.26% / 35.55% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.03% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.2M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.1M | 3.68% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.5M | 2.63% | 5% |
| 5 | `8Gbw…F8iD` | 9.5M | 2.16% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.13% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `CvSb…wycB` | 7.3M | 1.67% | 5% |
| 9 | `9QU2…29mF` | 7.2M | 1.65% | 7% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $102.55 (-2.29% 24h) |
| Market cap | $60.00B (rank #7) |
| 24h volume | $3.49B |
| ATH | $293.31 (-65.04% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.78B |
| Stablecoin supply | $15.87B |
| DEX volume (24h) | $1.87B (+11.91% 1d) |
| App fees (24h, all protocols) | $12.01M |
| Chain fees (24h) | $677.06K |
| Jito MEV tips (24h) | $145.07K |
| **REV - Real Economic Value (24h)** | **$822.14K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.87B | -5.57% |
| USDT | $2.83B | 0.00% |
| USDGO | $1.25B | +4.60% |
| USD1 | $1.21B | +12.99% |
| BUIDL | $886.54M | +14.08% |
| PYUSD | $692.89M | +0.72% |
| USDG | $609.65M | +0.34% |
| USDe | $537.27M | +0.16% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $732.11M |
| Orca DEX | $230.12M |
| BisonFi | $184.51M |
| Meteora DLMM | $142.67M |
| Raydium AMM | $116.71M |
| Manifest Trade | $112.76M |
| Axiom | $103.65M |
| pump.fun | $91.65M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.97M |
| pump.fun | $1.61M |
| Axiom | $1.20M |
| fomo Wallet | $789.24K |
| Jupiter Aggregator | $721.02K |
| Meteora DLMM | $377.42K |
| Sanctum Validator LSTs | $369.63K |
| Raydium AMM | $286.03K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 274 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $431.43M |
| xStocks 24h DEX volume | $13.09M |
| xStocks holder positions | 294.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: TSLAX ($64.47M), CRCLX ($64.05M), MSTRX ($52.34M), SPYX ($49.14M), GOOGLX ($30.99M)

## Program activity and chain health

Chain tip lag: **+13.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 48,945 | 33.20% | 1 s |
| Raydium AMM v4 | 5,087 | 31.90% | 11.7 s |
| Jupiter v6 | 4,432 | 72.00% | 13.3 s |
| Pump.fun | 2,795 | 45.30% | 21 s |
| Orca Whirlpools | 2,094 | 41.70% | 27.9 s |

Median failure rate across the sampled programs: **41.70%** (range 31.90% to 72.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **131.40 SOL**.

## Exchange and large-holder balances

11.80M SOL ($1.21B) across 8 publicly-attributed accounts. Net **73K SOL (0.62%) moved onto exchanges** over the last 22.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $942.28M | 1.3/h | 1 |
| Binance (2) | 1.65M | $169.26M | 805.4/h | 0 |
| Bybit | 377.26K | $38.69M | 67.4/h | 0 |
| Gate.io | 320.69K | $32.89M | 199.9/h | 0 |
| Bitget | 102.25K | $10.49M | 198.5/h | 0 |
| Coinbase | 86.85K | $8.91M | 236.1/h | 0 |
| Kraken | 38.15K | $3.91M | 225.3/h | 0 |
| Coinbase (2) | 31.51K | $3.23M | 250.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 724 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.244 | 683 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.197 | 690 | 0.0000 |
| DEX volume moves with App fees | +0.190 | 683 | 0.0000 |
| Total TPS moves with Slot time | +0.157 | 690 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.135 | 649 | 0.0006 |
| Non-vote TPS moves with AMM write-lock congestion | +0.134 | 649 | 0.0006 |
| Non-vote TPS moves with Activity index | +0.130 | 689 | 0.0006 |
| AMM write-lock congestion moves with Program failure rate | +0.127 | 649 | 0.0012 |
| Slot time moves with AMM write-lock congestion | +0.125 | 649 | 0.0014 |
| Total TPS moves with Activity index | +0.122 | 689 | 0.0013 |
| Total TPS moves with Program failure rate | +0.111 | 671 | 0.0040 |
| Non-vote TPS moves with Program failure rate | +0.108 | 671 | 0.0050 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 525.13K USD | DeFiLlama: 677.06K USD | -25.28% | *indicative*: 0.78x, within the order-of-magnitude band |
| SOL price | coingecko: 102.55 USD | Jupiter (on-chain DEX): 102.80 USD | -0.24% | agree |
| Circulating supply | getSupply (RPC): 585.12M SOL | CoinGecko: 585.12M SOL | -0.00% | agree |

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

**Latest Agave release:** [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) (2026-08-28)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[Solana Will Now Print Less SOL as Disinflation Vote Passes in Dramatic Fashion](https://decrypt.co/376825/solana-sol-disinflation-vote-passes)** - Decrypt, 2026-08-28
- **[Charles Schwab Expands Crypto Trading Beyond Bitcoin and Ethereum](https://decrypt.co/376819/charles-schwab-crypto-trading-bitcoin-ethereum-solana)** - Decrypt, 2026-08-28
- **[Bitwise fund is first Solana ETF to hit $1 billion AUM](https://www.theblock.co/news/markets/2026-08-28-bitwise-fund-is-first-solana-etf-to-hit-1-billion-aum-413035)** - The Block, 2026-08-28
- **[Morning Minute: Solana Jumps with Network Inflation Set to Drop](https://decrypt.co/376800/morning-minute-solana-jumps-with-network-inflation-set-to-drop)** - Decrypt, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[Solana Is Having Its Best Month Since 2024—With a Historic Governance Vote on Deck](https://decrypt.co/376706/solana-best-month-since-2024-historic-governance-vote)** - Decrypt, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
