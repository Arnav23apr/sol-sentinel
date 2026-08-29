# Solana Ecosystem Report

*Generated 2026-08-29 15:40 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 4.0 robust standard deviations above its 7-day baseline: a 9.5% move to 105.04 USD from a typical 95.92.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 1.6K |
| Slot time | 315 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1024 (63.67% complete, ~13.7h remaining) |
| Lifetime transactions | 543.1B |
| Circulating supply | 584.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,512 lamports (about $0.00058) |
| Transaction fee p90 / p99 | 29,000 / 514,294 lamports |
| Paying no priority fee | 25.60% of 4,056 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 10.70% of slots needed a priority fee (max 2.2M µlam/CU) |
| Node version (RPC) | 4.3.0-beta.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 688 |
| Delinquent validators | 9 |
| Delinquent stake | 0.00% |
| Total active stake | 436.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.17% / 24.15% / 35.47% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.09% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.90% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.5M | 2.63% | 5% |
| 5 | `26pV…3dJx` | 9.3M | 2.13% | 7% |
| 6 | `8Gbw…F8iD` | 9.1M | 2.08% | 0% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `CvSb…wycB` | 7.3M | 1.67% | 5% |
| 9 | `9QU2…29mF` | 7.2M | 1.65% | 7% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $105.04 (-1.29% 24h) |
| Market cap | $61.36B (rank #7) |
| 24h volume | $3.58B |
| ATH | $293.31 (-64.19% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.85B |
| Stablecoin supply | $15.99B |
| DEX volume (24h) | $2.59B (-29.99% 1d) |
| App fees (24h, all protocols) | $15.73M |
| Chain fees (24h) | $946.01K |
| Jito MEV tips (24h) | $214.30K |
| **REV - Real Economic Value (24h)** | **$1.16M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.03B | -4.36% |
| USDT | $2.84B | +3.47% |
| USDGO | $1.25B | +4.60% |
| USD1 | $1.16B | +9.14% |
| BUIDL | $886.54M | +14.08% |
| PYUSD | $696.10M | +3.14% |
| USDG | $618.55M | +0.94% |
| USDe | $531.85M | -0.92% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $576.29M |
| BisonFi | $331.44M |
| Orca DEX | $281.02M |
| Meteora DLMM | $279.39M |
| Raydium AMM | $145.05M |
| Manifest Trade | $126.59M |
| Axiom | $124.30M |
| pump.fun | $117.62M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.11M |
| pump.fun | $2.16M |
| Axiom | $1.85M |
| fomo Wallet | $814.79K |
| Meteora DLMM | $621.75K |
| Jupiter Perpetual Exchange | $498.13K |
| Sanctum Validator LSTs | $436.02K |
| pump.fun Mobile App | $315.98K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 253 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $432.55M |
| xStocks 24h DEX volume | $23.00M |
| xStocks holder positions | 288.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: TSLAX ($64.74M), CRCLX ($64.67M), MSTRX ($52.27M), SPYX ($49.37M), GOOGLX ($31.09M)

## Program activity and chain health

Chain tip lag: **+11.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 55,238 (approx.) | 33.30% | 0.6 s |
| Pump.fun | 26,340 | 84.00% | 2.2 s |
| Jupiter v6 | 1,932 | 44.10% | 30.9 s |
| Orca Whirlpools | 1,620 | 67.60% | 36.2 s |
| Raydium AMM v4 | 1,284 | 29.40% | 46.3 s |

Median failure rate across the sampled programs: **44.10%** (range 29.40% to 84.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **285.79 SOL**.

## Exchange and large-holder balances

11.71M SOL ($1.23B) across 8 publicly-attributed accounts. Net **38K SOL (0.33%) moved onto exchanges** over the last 16.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $965.15M | 1.3/h | 2 |
| Binance (2) | 1.69M | $177.52M | 1.1K/h | 0 |
| Bybit | 377.26K | $39.63M | 19/h | 0 |
| Gate.io | 306.15K | $32.16M | 222.5/h | 0 |
| Bitget | 55.65K | $5.85M | 298.8/h | 0 |
| Kraken | 40.26K | $4.23M | 214.9/h | 0 |
| Coinbase | 26.47K | $2.78M | 358.9/h | 0 |
| Coinbase (2) | 23.93K | $2.51M | 509.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 713 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.226 | 672 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.197 | 679 | 0.0000 |
| DEX volume moves with App fees | +0.173 | 672 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 679 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.132 | 638 | 0.0008 |
| Non-vote TPS moves with AMM write-lock congestion | +0.132 | 638 | 0.0009 |
| Non-vote TPS moves with Activity index | +0.127 | 678 | 0.0010 |
| AMM write-lock congestion moves with Program failure rate | +0.126 | 638 | 0.0014 |
| Slot time moves with AMM write-lock congestion | +0.120 | 638 | 0.0023 |
| Total TPS moves with Activity index | +0.119 | 678 | 0.0019 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 491.99K USD | DeFiLlama: 946.01K USD | -63.15% | *indicative*: 0.52x, within the order-of-magnitude band |
| SOL price | coingecko: 105.04 USD | Jupiter (on-chain DEX): 105.05 USD | -0.01% | agree |
| Circulating supply | getSupply (RPC): 584.16M SOL | CoinGecko: 584.16M SOL | -0.00% | agree |

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
- **[DeFi Development Corp resumes Solana purchases, acquiring nearly 20,000 SOL](https://www.theblock.co/news/business/2026-08-27-defi-development-resumes-solana-purchases-acquiring-nearly-20000-sol-412932)** - The Block, 2026-08-27
- **[Solana Is Having Its Best Month Since 2024—With a Historic Governance Vote on Deck](https://decrypt.co/376706/solana-best-month-since-2024-historic-governance-vote)** - Decrypt, 2026-08-27
- **[Charles Schwab to add Solana, Avalanche and Chainlink to crypto trading platform](https://www.theblock.co/news/business/2026-08-27-charles-schwab-add-solana-avalanche-chainlink-to-crypto-trading-platform-412923)** - The Block, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
