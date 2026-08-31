# Solana Ecosystem Report

*Generated 2026-08-31 20:27 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 14.5 robust standard deviations below its 7-day baseline: a 34.6% move to 1,929,632,645.00 USD from a typical 2,948,781,265.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 1.9K |
| Slot time | 315 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1026 (2.29% complete, ~36.9h remaining) |
| Lifetime transactions | 543.9B |
| Circulating supply | 585.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,699 lamports (about $0.00059) |
| Transaction fee p90 / p99 | 29,260 / 503,058 lamports |
| Paying no priority fee | 24.50% of 4,150 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 31.30% of slots needed a priority fee (max 26.0M µlam/CU) |
| Node version (RPC) | 4.2.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 680 |
| Delinquent validators | 14 |
| Delinquent stake | 0.01% |
| Total active stake | 438.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.25% / 24.17% / 35.44% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.94% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.2M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.5M | 2.62% | 5% |
| 5 | `8Gbw…F8iD` | 9.5M | 2.16% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.2M | 1.65% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $104.11 (-1.45% 24h) |
| Market cap | $60.92B (rank #7) |
| 24h volume | $3.80B |
| ATH | $293.31 (-64.51% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.85B |
| Stablecoin supply | $15.73B |
| DEX volume (24h) | $1.93B (+15.50% 1d) |
| App fees (24h, all protocols) | $12.31M |
| Chain fees (24h) | $677.06K |
| Jito MEV tips (24h) | $169.22K |
| **REV - Real Economic Value (24h)** | **$846.28K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.73B | -7.59% |
| USDT | $2.83B | 0.00% |
| USDGO | $1.24B | +4.18% |
| USD1 | $1.21B | +12.99% |
| BUIDL | $886.79M | +14.11% |
| PYUSD | $694.10M | +0.88% |
| USDG | $615.92M | +1.36% |
| USDe | $537.05M | +0.14% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $732.11M |
| Orca DEX | $274.30M |
| BisonFi | $184.51M |
| Meteora DLMM | $142.67M |
| Raydium AMM | $136.83M |
| Manifest Trade | $132.89M |
| pump.fun | $91.65M |
| Axiom | $83.77M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.97M |
| pump.fun | $1.61M |
| Axiom | $1.20M |
| fomo Wallet | $973.16K |
| Jupiter Aggregator | $721.02K |
| Meteora DLMM | $377.42K |
| Sanctum Validator LSTs | $369.63K |
| Raydium AMM | $300.83K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 244 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $441.04M |
| xStocks 24h DEX volume | $23.08M |
| xStocks holder positions | 295.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: CRCLX ($69.31M), TSLAX ($67.51M), MSTRX ($54.29M), SPYX ($48.70M), GOOGLX ($30.34M)

## Program activity and chain health

Chain tip lag: **+11.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 59,683 | 90.60% | 0.9 s |
| SPL Token | 44,714 | 28.60% | 1.3 s |
| Raydium AMM v4 | 2,789 | 31.70% | 21.1 s |
| Jupiter v6 | 2,099 | 37.30% | 28.4 s |
| Orca Whirlpools | 2,014 | 35.80% | 29 s |

Median failure rate across the sampled programs: **35.80%** (range 28.60% to 90.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **872.77 SOL**.

## Exchange and large-holder balances

11.82M SOL ($1.23B) across 8 publicly-attributed accounts. Net **64K SOL (0.54%) moved onto exchanges** over the last 21.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $956.61M | 1.2/h | 1 |
| Binance (2) | 1.78M | $185.40M | 1.3K/h | 1 |
| Gate.io | 333.41K | $34.71M | 291.7/h | 0 |
| Bybit | 329.62K | $34.32M | 87.7/h | 1 |
| Bitget | 83.54K | $8.70M | 203.4/h | 0 |
| Coinbase (2) | 36.53K | $3.80M | 556.4/h | 0 |
| Kraken | 35.40K | $3.69M | 248.3/h | 0 |
| Coinbase | 33.39K | $3.48M | 467.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 726 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.243 | 685 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.201 | 692 | 0.0000 |
| DEX volume moves with App fees | +0.196 | 685 | 0.0000 |
| Total TPS moves with Slot time | +0.161 | 692 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.134 | 651 | 0.0006 |
| Non-vote TPS moves with AMM write-lock congestion | +0.133 | 651 | 0.0007 |
| Non-vote TPS moves with Activity index | +0.127 | 691 | 0.0008 |
| AMM write-lock congestion moves with Program failure rate | +0.126 | 651 | 0.0013 |
| Slot time moves with AMM write-lock congestion | +0.123 | 651 | 0.0017 |
| Total TPS moves with Activity index | +0.120 | 691 | 0.0016 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 450.31K USD | DeFiLlama: 677.06K USD | -40.23% | *indicative*: 0.67x, within the order-of-magnitude band |
| SOL price | coingecko: 104.11 USD | Jupiter (on-chain DEX): 104.07 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 585.21M SOL | CoinGecko: 585.12M SOL | +0.01% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-08-31
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-08-31
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-31
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-31
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-08-31
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

- **[Solana fees hit record as validators double pace of inflation cuts](https://www.theblock.co/news/ecosystems/2026-08-31-solana-fees-hit-record-as-validators-double-pace-of-inflation-cuts-413135)** - The Block, 2026-08-31
- **[OpenSea adds Solana NFT trading more than four years after initial beta](https://www.theblock.co/news/markets/2026-08-31-opensea-solana-nft-trading-413128)** - The Block, 2026-08-31
- **[Solana Will Now Print Less SOL as Disinflation Vote Passes in Dramatic Fashion](https://decrypt.co/376825/solana-sol-disinflation-vote-passes)** - Decrypt, 2026-08-28
- **[Charles Schwab Expands Crypto Trading Beyond Bitcoin and Ethereum](https://decrypt.co/376819/charles-schwab-crypto-trading-bitcoin-ethereum-solana)** - Decrypt, 2026-08-28
- **[Bitwise fund is first Solana ETF to hit $1 billion AUM](https://www.theblock.co/news/markets/2026-08-28-bitwise-fund-is-first-solana-etf-to-hit-1-billion-aum-413035)** - The Block, 2026-08-28
- **[Morning Minute: Solana Jumps with Network Inflation Set to Drop](https://decrypt.co/376800/morning-minute-solana-jumps-with-network-inflation-set-to-drop)** - Decrypt, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
