# Solana Ecosystem Report

*Generated 2026-08-30 22:50 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DEX volume (24h)** (critical): DEX volume (24h) is 22.0 robust standard deviations below its 7-day baseline: a 43.3% move to 1,670,710,752.00 USD from a typical 2,948,781,265.00.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 5.0 robust standard deviations above its 7-day baseline: a 5.3% move to 5,907,245,489.00 USD from a typical 5,607,526,420.00.
- 🟠 **Delinquent validators** (warning): Delinquent validators is 5.4 robust standard deviations above its 7-day baseline: a 80.0% move to 18.00 from a typical 10.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 1.9K |
| Slot time | 315.8 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1025 (45.56% complete, ~20.6h remaining) |
| Lifetime transactions | 543.6B |
| Circulating supply | 585.1M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,612 lamports (about $0.00058) |
| Transaction fee p90 / p99 | 19,555 / 410,000 lamports |
| Paying no priority fee | 20.90% of 4,502 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 2.2M µlam/CU) |
| Node version (RPC) | 4.2.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 679 |
| Delinquent validators | 18 |
| Delinquent stake | 0.01% |
| Total active stake | 437.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.24% / 24.26% / 35.54% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.02% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.2M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.1M | 3.68% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.83% | 0% |
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
| SOL price | $103.69 (-1.55% 24h) |
| Market cap | $60.66B (rank #7) |
| 24h volume | $2.65B |
| ATH | $293.31 (-64.65% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.91B |
| Stablecoin supply | $15.82B |
| DEX volume (24h) | $1.67B (-35.51% 1d) |
| App fees (24h, all protocols) | $11.21M |
| Chain fees (24h) | $826.70K |
| Jito MEV tips (24h) | $143.03K |
| **REV - Real Economic Value (24h)** | **$969.73K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.84B | -5.60% |
| USDT | $2.83B | +1.61% |
| USDGO | $1.25B | +4.60% |
| USD1 | $1.19B | +11.12% |
| BUIDL | $886.54M | +14.08% |
| PYUSD | $692.46M | +0.67% |
| USDG | $612.72M | +1.00% |
| USDe | $537.14M | +0.05% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $584.75M |
| Orca DEX | $174.47M |
| BisonFi | $149.87M |
| Meteora DLMM | $142.97M |
| pump.fun | $110.08M |
| Axiom | $103.65M |
| Raydium AMM | $101.53M |
| Manifest Trade | $93.07M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.44M |
| pump.fun | $1.94M |
| Axiom | $1.56M |
| fomo Wallet | $789.24K |
| Meteora DLMM | $443.15K |
| pump.fun Mobile App | $311.35K |
| Raydium AMM | $263.99K |
| Terminal | $223.10K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 226 |
| Persistently-active cohort (capture-recapture est.) | 2.2K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $435.75M |
| xStocks 24h DEX volume | $10.17M |
| xStocks holder positions | 293.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: CRCLX ($65.63M), TSLAX ($64.84M), MSTRX ($53.17M), SPYX ($49.38M), GOOGLX ($31.06M)

## Program activity and chain health

Chain tip lag: **+12.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 81,127 (approx.) | 53.60% | 0.6 s |
| Pump.fun | 12,743 | 81.60% | 4.4 s |
| Jupiter v6 | 2,459 | 57.00% | 22.7 s |
| Raydium AMM v4 | 1,345 | 13.60% | 44.5 s |
| Orca Whirlpools | 1,034 | 42.10% | 57.8 s |

Median failure rate across the sampled programs: **53.60%** (range 13.60% to 81.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **131.40 SOL**.

## Exchange and large-holder balances

11.76M SOL ($1.22B) across 8 publicly-attributed accounts. Net **87K SOL (0.75%) moved onto exchanges** over the last 23.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $952.75M | 1.4/h | 3 |
| Binance (2) | 1.68M | $174.52M | 845.1/h | 0 |
| Bybit | 377.26K | $39.12M | 80.7/h | 0 |
| Gate.io | 326.94K | $33.90M | 200.2/h | 0 |
| Bitget | 74.06K | $7.68M | 144.8/h | 0 |
| Kraken | 40.20K | $4.17M | 268.3/h | 0 |
| Coinbase | 35.20K | $3.65M | 500.7/h | 0 |
| Coinbase (2) | 32.28K | $3.35M | 412.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 11 of 117 tested pairs survive, over 722 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.237 | 681 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.198 | 688 | 0.0000 |
| DEX volume moves with App fees | +0.193 | 681 | 0.0000 |
| Total TPS moves with Slot time | +0.159 | 688 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.136 | 647 | 0.0005 |
| Non-vote TPS moves with AMM write-lock congestion | +0.136 | 647 | 0.0005 |
| Non-vote TPS moves with Activity index | +0.131 | 687 | 0.0006 |
| AMM write-lock congestion moves with Program failure rate | +0.128 | 647 | 0.0011 |
| Slot time moves with AMM write-lock congestion | +0.124 | 647 | 0.0016 |
| Total TPS moves with Activity index | +0.123 | 687 | 0.0013 |
| Total TPS moves with Program failure rate | +0.111 | 669 | 0.0042 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 358.73K USD | DeFiLlama: 826.70K USD | -78.95% | *indicative*: 0.43x, within the order-of-magnitude band |
| SOL price | coingecko: 103.69 USD | Jupiter (on-chain DEX): 103.69 USD | 0.00% | agree |
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
