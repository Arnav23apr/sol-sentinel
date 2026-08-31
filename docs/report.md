# Solana Ecosystem Report

*Generated 2026-08-31 23:57 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 14.5 robust standard deviations below its 7-day baseline: a 34.6% move to 1,929,632,645.00 USD from a typical 2,948,787,718.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.8K |
| TPS (non-vote) | 1.7K |
| Slot time | 317.5 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1026 (11.49% complete, ~33.7h remaining) |
| Lifetime transactions | 543.9B |
| Circulating supply | 585.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,877 lamports (about $0.00061) |
| Transaction fee p90 / p99 | 21,145 / 240,224 lamports |
| Paying no priority fee | 19.70% of 4,383 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 445.7K µlam/CU) |
| Node version (RPC) | 4.2.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 679 |
| Delinquent validators | 15 |
| Delinquent stake | 0.03% |
| Total active stake | 438.1M SOL |
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
| SOL price | $102.98 (+1.15% 24h) |
| Market cap | $60.26B (rank #7) |
| 24h volume | $3.27B |
| ATH | $293.31 (-64.89% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.99B |
| Stablecoin supply | $15.76B |
| DEX volume (24h) | $1.93B (+15.50% 1d) |
| App fees (24h, all protocols) | $12.31M |
| Chain fees (24h) | $677.06K |
| Jito MEV tips (24h) | $171.27K |
| **REV - Real Economic Value (24h)** | **$848.34K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.71B | -7.89% |
| USDT | $2.83B | 0.00% |
| USDGO | $1.24B | +4.18% |
| USD1 | $1.21B | +12.99% |
| BUIDL | $886.92M | +14.13% |
| PYUSD | $754.03M | +9.58% |
| USDG | $615.52M | +1.35% |
| USDe | $537.04M | +0.14% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $732.11M |
| Orca DEX | $262.20M |
| BisonFi | $184.51M |
| Meteora DLMM | $142.67M |
| Raydium AMM | $141.22M |
| Manifest Trade | $130.83M |
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
| Raydium AMM | $323.38K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 225 |
| Persistently-active cohort (capture-recapture est.) | 2.1K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $441.84M |
| xStocks 24h DEX volume | $21.95M |
| xStocks holder positions | 296.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: CRCLX ($69.94M), TSLAX ($67.60M), MSTRX ($54.58M), SPYX ($48.95M), GOOGLX ($30.57M)

## Program activity and chain health

Chain tip lag: **+11.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 41,575 | 31.00% | 1.3 s |
| Pump.fun | 25,728 | 91.90% | 2.2 s |
| Raydium AMM v4 | 5,351 | 35.80% | 11.1 s |
| Jupiter v6 | 1,649 | 40.30% | 35.9 s |
| Orca Whirlpools | 470 | 32.80% | 127.3 s |

Median failure rate across the sampled programs: **35.80%** (range 31.00% to 91.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **646.68 SOL**.

## Exchange and large-holder balances

11.80M SOL ($1.21B) across 8 publicly-attributed accounts. Net **33K SOL (0.28%) moved onto exchanges** over the last 23.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $946.23M | 1.2/h | 1 |
| Binance (2) | 1.79M | $184.40M | 1.1K/h | 0 |
| Gate.io | 328.79K | $33.86M | 118.7/h | 0 |
| Bybit | 323.35K | $33.30M | 46.7/h | 0 |
| Bitget | 72.71K | $7.49M | 153.8/h | 0 |
| Kraken | 33.87K | $3.49M | 183/h | 0 |
| Coinbase (2) | 29.65K | $3.05M | 720/h | 0 |
| Coinbase | 29.64K | $3.05M | 432.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 727 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.246 | 686 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.199 | 693 | 0.0000 |
| DEX volume moves with App fees | +0.196 | 686 | 0.0000 |
| Total TPS moves with Slot time | +0.160 | 693 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.136 | 652 | 0.0005 |
| Non-vote TPS moves with AMM write-lock congestion | +0.135 | 652 | 0.0005 |
| Non-vote TPS moves with Activity index | +0.128 | 692 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.126 | 652 | 0.0013 |
| Total TPS moves with Activity index | +0.120 | 692 | 0.0015 |
| Slot time moves with AMM write-lock congestion | +0.120 | 652 | 0.0021 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 540.87K USD | DeFiLlama: 677.06K USD | -22.36% | *indicative*: 0.80x, within the order-of-magnitude band |
| SOL price | coingecko: 102.98 USD | Jupiter (on-chain DEX): 102.99 USD | -0.01% | agree |
| Circulating supply | getSupply (RPC): 585.21M SOL | CoinGecko: 585.21M SOL | -0.00% | agree |

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
