# Solana Ecosystem Report

*Generated 2026-09-01 03:24 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.5K |
| TPS (non-vote) | 1.4K |
| Slot time | 315 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1026 (20.52% complete, ~30.0h remaining) |
| Lifetime transactions | 544.0B |
| Circulating supply | 585.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,612 lamports (about $0.00058) |
| Transaction fee p90 / p99 | 22,523 / 617,867 lamports |
| Paying no priority fee | 21.60% of 4,874 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 1.4M µlam/CU) |
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
| SOL price | $103.45 (+1.66% 24h) |
| Market cap | $60.54B (rank #7) |
| 24h volume | $3.09B |
| ATH | $293.31 (-64.73% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.84B |
| Stablecoin supply | $15.79B |
| DEX volume (24h) | $2.46B (+27.37% 1d) |
| App fees (24h, all protocols) | $13.29M |
| Chain fees (24h) | $836.26K |
| Jito MEV tips (24h) | $172.59K |
| **REV - Real Economic Value (24h)** | **$1.01M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.72B | -6.14% |
| USDT | $2.83B | 0.00% |
| USDGO | $1.24B | +4.18% |
| USD1 | $1.21B | +10.10% |
| BUIDL | $886.92M | +7.02% |
| PYUSD | $774.15M | +14.72% |
| USDG | $609.13M | -3.95% |
| USDe | $537.20M | +0.13% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $939.21M |
| BisonFi | $232.85M |
| Orca DEX | $220.81M |
| Meteora DLMM | $149.33M |
| Manifest Trade | $136.17M |
| Raydium AMM | $135.95M |
| pump.fun | $98.91M |
| Axiom | $83.77M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.73M |
| pump.fun | $1.72M |
| Axiom | $1.65M |
| fomo Wallet | $973.16K |
| Meteora DLMM | $403.59K |
| Sanctum Validator LSTs | $377.96K |
| Raydium AMM | $303.92K |
| pump.fun Mobile App | $294.26K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 252 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $440.30M |
| xStocks 24h DEX volume | $20.65M |
| xStocks holder positions | 296.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: CRCLX ($69.18M), TSLAX ($67.49M), MSTRX ($53.58M), SPYX ($48.94M), GOOGLX ($30.54M)

## Program activity and chain health

Chain tip lag: **+11.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 44,143 | 29.70% | 1.3 s |
| Pump.fun | 14,841 | 83.00% | 3.8 s |
| Orca Whirlpools | 1,326 | 45.80% | 43.5 s |
| Jupiter v6 | 1,282 | 33.80% | 46 s |
| Raydium AMM v4 | 1,111 | 15.20% | 53.9 s |

Median failure rate across the sampled programs: **33.80%** (range 15.20% to 83.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **646.68 SOL**.

## Exchange and large-holder balances

11.81M SOL ($1.22B) across 8 publicly-attributed accounts. Net **18K SOL (0.15%) moved onto exchanges** over the last 20.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $950.54M | 1.2/h | 1 |
| Binance (2) | 1.81M | $187.28M | 1.1K/h | 0 |
| Gate.io | 326.94K | $33.82M | 153.9/h | 0 |
| Bybit | 315.19K | $32.61M | 51.9/h | 0 |
| Bitget | 73.79K | $7.63M | 162.2/h | 0 |
| Coinbase | 34.32K | $3.55M | 460.9/h | 0 |
| Kraken | 33.45K | $3.46M | 173.5/h | 0 |
| Coinbase (2) | 31.30K | $3.24M | 466.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 728 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.249 | 687 | 0.0000 |
| DEX volume moves with App fees | +0.203 | 687 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.201 | 694 | 0.0000 |
| Total TPS moves with Slot time | +0.161 | 694 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.137 | 653 | 0.0004 |
| Non-vote TPS moves with AMM write-lock congestion | +0.136 | 653 | 0.0005 |
| Non-vote TPS moves with Activity index | +0.127 | 693 | 0.0008 |
| AMM write-lock congestion moves with Program failure rate | +0.126 | 653 | 0.0012 |
| Slot time moves with AMM write-lock congestion | +0.121 | 653 | 0.0019 |
| Total TPS moves with Activity index | +0.119 | 693 | 0.0017 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 763.21K USD | DeFiLlama: 836.26K USD | -9.13% | *indicative*: 0.91x, within the order-of-magnitude band |
| SOL price | coingecko: 103.45 USD | Jupiter (on-chain DEX): 103.31 USD | +0.14% | agree |
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
