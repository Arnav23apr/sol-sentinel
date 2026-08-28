# Solana Ecosystem Report

*Generated 2026-08-28 23:09 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 3.9 robust standard deviations above its 7-day baseline: a 9.1% move to 104.04 USD from a typical 95.32.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 1.8K |
| Slot time | 317.5 ms |
| Slot | 442M |
| Block height | 421M |
| Epoch | 1024 (20.19% complete, ~30.4h remaining) |
| Lifetime transactions | 542.9B |
| Circulating supply | 584.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,267 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 24,507 / 1,005,000 lamports |
| Paying no priority fee | 28.00% of 5,186 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 24.00% of slots needed a priority fee (max 1.9M µlam/CU) |
| Node version (RPC) | 4.3.0-beta.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 687 |
| Delinquent validators | 10 |
| Delinquent stake | 0.01% |
| Total active stake | 436.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.17% / 24.15% / 35.47% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.07% |

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
| SOL price | $104.04 (-4.65% 24h) |
| Market cap | $60.80B (rank #7) |
| 24h volume | $5.97B |
| ATH | $293.31 (-64.53% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.83B |
| Stablecoin supply | $15.95B |
| DEX volume (24h) | $3.70B (+57.34% 1d) |
| App fees (24h, all protocols) | $16.30M |
| Chain fees (24h) | $1.19M |
| Jito MEV tips (24h) | $255.43K |
| **REV - Real Economic Value (24h)** | **$1.44M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.01B | -3.75% |
| USDT | $2.83B | -0.87% |
| USDGO | $1.25B | +7.89% |
| USD1 | $1.15B | +8.92% |
| BUIDL | $886.54M | +19.69% |
| PYUSD | $682.43M | -0.84% |
| USDG | $624.75M | -0.98% |
| USDe | $534.32M | -0.35% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $1.46B |
| BisonFi | $416.99M |
| Orca DEX | $335.52M |
| Meteora DLMM | $245.52M |
| Raydium AMM | $179.13M |
| Axiom | $165.79M |
| pump.fun | $144.47M |
| Manifest Trade | $143.10M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.66M |
| pump.fun | $2.65M |
| Axiom | $2.54M |
| fomo Wallet | $729.95K |
| Meteora DLMM | $695.76K |
| Jupiter Perpetual Exchange | $521.61K |
| Collector Crypt | $433.30K |
| pump.fun Mobile App | $325.83K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 316 |
| Persistently-active cohort (capture-recapture est.) | 3.5K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $431.54M |
| xStocks 24h DEX volume | $35.89M |
| xStocks holder positions | 286.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: TSLAX ($64.40M), CRCLX ($63.86M), MSTRX ($52.21M), SPYX ($49.29M), GOOGLX ($31.18M)

## Program activity and chain health

Chain tip lag: **+12.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 106,016 (approx.) | 49.60% | 0.3 s |
| Jupiter v6 | 7,677 | 77.50% | 7.6 s |
| Raydium AMM v4 | 7,293 | 76.00% | 7 s |
| Orca Whirlpools | 6,547 | 76.40% | 8.9 s |
| Pump.fun | 4,170 | 33.80% | 14.3 s |

Median failure rate across the sampled programs: **76.00%** (range 33.80% to 77.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **917.88 SOL**.

## Exchange and large-holder balances

11.67M SOL ($1.21B) across 8 publicly-attributed accounts. Net **631K SOL (5.13%) moved off exchanges** over the last 21.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $955.97M | 0.9/h | 4 |
| Binance (2) | 1.68M | $174.92M | 904.5/h | 0 |
| Bybit | 377.26K | $39.25M | 21.4/h | 0 |
| Gate.io | 283.67K | $29.51M | 181.9/h | 0 |
| Bitget | 66.31K | $6.90M | 184.6/h | 0 |
| Kraken | 27.56K | $2.87M | 211.6/h | 0 |
| Coinbase | 22.77K | $2.37M | 939.9/h | 0 |
| Coinbase (2) | 22.75K | $2.37M | 464.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 710 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.230 | 669 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.196 | 676 | 0.0000 |
| DEX volume moves with App fees | +0.174 | 669 | 0.0000 |
| Total TPS moves with Slot time | +0.156 | 676 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.130 | 635 | 0.0011 |
| Non-vote TPS moves with AMM write-lock congestion | +0.129 | 635 | 0.0012 |
| AMM write-lock congestion moves with Program failure rate | +0.122 | 635 | 0.0021 |
| Non-vote TPS moves with Activity index | +0.121 | 675 | 0.0016 |
| Slot time moves with AMM write-lock congestion | +0.121 | 635 | 0.0023 |
| Total TPS moves with Activity index | +0.114 | 675 | 0.0031 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 619.59K USD | DeFiLlama: 1.19M USD | -62.90% | *indicative*: 0.52x, within the order-of-magnitude band |
| SOL price | coingecko: 104.04 USD | Jupiter (on-chain DEX): 104.21 USD | -0.16% | agree |
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
- **[Galaxy Opens Retail Crypto-Backed Credit Lines on Bitcoin, Ethereum and Solana](https://decrypt.co/376646/galaxy-crypto-credit-lines-bitcoin-ethereum-solana)** - Decrypt, 2026-08-26

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
