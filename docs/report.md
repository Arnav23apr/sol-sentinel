# Solana Ecosystem Report

*Generated 2026-08-31 14:33 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 17.6 robust standard deviations below its 7-day baseline: a 34.6% move to 1,929,632,645.00 USD from a typical 2,948,781,265.00.
- 🔴 **Delinquent validators** (critical): Delinquent validators is 6.1 robust standard deviations above its 7-day baseline: a 90.0% move to 19.00 from a typical 10.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.5K |
| TPS (non-vote) | 2.4K |
| Slot time | 320 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1025 (86.80% complete, ~5.1h remaining) |
| Lifetime transactions | 543.8B |
| Circulating supply | 585.1M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,900 lamports (about $0.00061) |
| Transaction fee p90 / p99 | 26,236 / 410,000 lamports |
| Paying no priority fee | 17.40% of 5,711 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 18.70% of slots needed a priority fee (max 3.4M µlam/CU) |
| Node version (RPC) | 4.3.0-beta.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 19 |
| Delinquent stake | 0.07% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.25% / 24.27% / 35.57% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.04% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.2M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.1M | 3.68% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.5M | 2.63% | 5% |
| 5 | `8Gbw…F8iD` | 9.5M | 2.16% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.13% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `CvSb…wycB` | 7.3M | 1.67% | 5% |
| 9 | `9QU2…29mF` | 7.2M | 1.65% | 7% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $102.62 (-4.09% 24h) |
| Market cap | $60.00B (rank #7) |
| 24h volume | $3.69B |
| ATH | $293.31 (-65.01% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.80B |
| Stablecoin supply | $15.77B |
| DEX volume (24h) | $1.93B (+15.50% 1d) |
| App fees (24h, all protocols) | $12.31M |
| Chain fees (24h) | $677.06K |
| Jito MEV tips (24h) | $158.09K |
| **REV - Real Economic Value (24h)** | **$835.15K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.78B | -6.85% |
| USDT | $2.83B | 0.00% |
| USDGO | $1.24B | +4.18% |
| USD1 | $1.21B | +12.99% |
| BUIDL | $886.54M | +14.08% |
| PYUSD | $693.75M | +0.85% |
| USDG | $605.81M | -0.26% |
| USDe | $537.15M | +0.16% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $732.11M |
| Orca DEX | $258.15M |
| BisonFi | $184.51M |
| Meteora DLMM | $142.67M |
| Manifest Trade | $131.61M |
| Raydium AMM | $111.76M |
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
| pump.fun Mobile App | $273.16K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 244 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $430.47M |
| xStocks 24h DEX volume | $16.41M |
| xStocks holder positions | 294.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: CRCLX ($64.05M), TSLAX ($63.95M), MSTRX ($52.21M), SPYX ($49.08M), GOOGLX ($30.86M)

## Program activity and chain health

Chain tip lag: **+12.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 54,750 (approx.) | 29.60% | 0.6 s |
| Pump.fun | 51,562 | 90.60% | 1 s |
| Jupiter v6 | 6,208 | 65.60% | 8.6 s |
| Raydium AMM v4 | 3,739 | 23.70% | 16 s |
| Orca Whirlpools | 1,901 | 30.70% | 30.1 s |

Median failure rate across the sampled programs: **30.70%** (range 23.70% to 90.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **26.33 SOL**.

## Exchange and large-holder balances

11.76M SOL ($1.21B) across 8 publicly-attributed accounts. Net **26K SOL (0.22%) moved onto exchanges** over the last 20.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $942.92M | 1.3/h | 1 |
| Binance (2) | 1.70M | $174.95M | 1.4K/h | 0 |
| Bybit | 339.12K | $34.80M | 269.1/h | 0 |
| Gate.io | 337.42K | $34.63M | 566/h | 0 |
| Bitget | 100.46K | $10.31M | 255.7/h | 0 |
| Kraken | 35.77K | $3.67M | 265.1/h | 0 |
| Coinbase | 29.96K | $3.07M | 372.7/h | 0 |
| Coinbase (2) | 28.93K | $2.97M | 559/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 11 of 117 tested pairs survive, over 725 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.240 | 684 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.198 | 691 | 0.0000 |
| DEX volume moves with App fees | +0.196 | 684 | 0.0000 |
| Total TPS moves with Slot time | +0.159 | 691 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.138 | 650 | 0.0004 |
| Non-vote TPS moves with AMM write-lock congestion | +0.137 | 650 | 0.0005 |
| Non-vote TPS moves with Activity index | +0.128 | 690 | 0.0008 |
| Slot time moves with AMM write-lock congestion | +0.126 | 650 | 0.0012 |
| AMM write-lock congestion moves with Program failure rate | +0.125 | 650 | 0.0014 |
| Total TPS moves with Activity index | +0.120 | 690 | 0.0016 |
| Total TPS moves with Program failure rate | +0.109 | 672 | 0.0047 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 530.27K USD | DeFiLlama: 677.06K USD | -24.32% | *indicative*: 0.78x, within the order-of-magnitude band |
| SOL price | coingecko: 102.62 USD | Jupiter (on-chain DEX): 102.48 USD | +0.14% | agree |
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
