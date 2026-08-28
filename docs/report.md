# Solana Ecosystem Report

*Generated 2026-08-28 13:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 4.2 robust standard deviations above its 7-day baseline: a 10.4% move to 104.97 USD from a typical 95.12.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 5.9 robust standard deviations above its 7-day baseline: a 6.1% move to 5,916,951,218.00 USD from a typical 5,577,888,789.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.8K |
| TPS (non-vote) | 1.9K |
| Slot time | 365.9 ms |
| Slot | 442M |
| Block height | 420M |
| Epoch | 1023 (95.64% complete, ~1.9h remaining) |
| Lifetime transactions | 542.7B |
| Circulating supply | 584.1M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,620 lamports (about $0.00059) |
| Transaction fee p90 / p99 | 29,391 / 478,737 lamports |
| Paying no priority fee | 17.30% of 6,491 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 3.30% of slots needed a priority fee (max 13.7M µlam/CU) |
| Node version (RPC) | 4.3.0-beta.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 687 |
| Delinquent validators | 10 |
| Delinquent stake | 0.02% |
| Total active stake | 436.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.20% / 24.28% / 35.58% |
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
| SOL price | $104.97 (+0.32% 24h) |
| Market cap | $61.26B (rank #7) |
| 24h volume | $5.99B |
| ATH | $293.31 (-64.21% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.92B |
| Stablecoin supply | $15.97B |
| DEX volume (24h) | $3.70B (+57.34% 1d) |
| App fees (24h, all protocols) | $16.19M |
| Chain fees (24h) | $1.19M |
| Jito MEV tips (24h) | $267.55K |
| **REV - Real Economic Value (24h)** | **$1.46M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.05B | -3.25% |
| USDT | $2.84B | -0.87% |
| USDGO | $1.25B | +7.89% |
| USD1 | $1.14B | +7.41% |
| BUIDL | $886.45M | +19.68% |
| PYUSD | $681.46M | -0.99% |
| USDG | $619.89M | -1.80% |
| USDe | $536.53M | +0.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $1.46B |
| BisonFi | $416.99M |
| Orca DEX | $317.30M |
| Meteora DLMM | $245.52M |
| Axiom | $165.79M |
| Manifest Trade | $160.18M |
| Raydium AMM | $160.12M |
| pump.fun | $144.47M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.66M |
| pump.fun | $2.65M |
| Axiom | $2.54M |
| fomo Wallet | $729.96K |
| Meteora DLMM | $695.76K |
| Jupiter Perpetual Exchange | $521.61K |
| Collector Crypt | $517.75K |
| pump.fun Mobile App | $325.83K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 296 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $437.50M |
| xStocks 24h DEX volume | $37.86M |
| xStocks holder positions | 281.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.08B |

Top tokenized equities: CRCLX ($68.00M), TSLAX ($65.60M), MSTRX ($53.45M), SPYX ($48.93M), GOOGLX ($30.79M)

## Program activity and chain health

Chain tip lag: **+13.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 76,906 (approx.) | 89.60% | 0.4 s |
| SPL Token | 71,659 (approx.) | 46.40% | 0.4 s |
| Jupiter v6 | 31,254 | 79.80% | 1.8 s |
| Orca Whirlpools | 15,596 | 71.80% | 3.3 s |
| Raydium AMM v4 | 2,004 | 25.20% | 29.6 s |

Median failure rate across the sampled programs: **71.80%** (range 25.20% to 89.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.32 SOL**.

## Exchange and large-holder balances

11.82M SOL ($1.24B) across 8 publicly-attributed accounts. Net **637K SOL (5.11%) moved off exchanges** over the last 20.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $964.51M | 1/h | 6 |
| Binance (2) | 1.82M | $190.96M | 949.9/h | 0 |
| Bybit | 377.26K | $39.60M | 33.1/h | 0 |
| Gate.io | 303.97K | $31.91M | 189.8/h | 0 |
| Bitget | 55.02K | $5.78M | 264.9/h | 0 |
| Kraken | 30.59K | $3.21M | 243.6/h | 0 |
| Coinbase | 24.71K | $2.59M | 425.5/h | 0 |
| Coinbase (2) | 23.56K | $2.47M | 435.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 709 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.227 | 668 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.195 | 675 | 0.0000 |
| DEX volume moves with App fees | +0.174 | 668 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 675 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.130 | 634 | 0.0010 |
| Total TPS moves with AMM write-lock congestion | +0.128 | 634 | 0.0012 |
| Slot time moves with AMM write-lock congestion | +0.126 | 634 | 0.0015 |
| Non-vote TPS moves with Activity index | +0.122 | 674 | 0.0015 |
| AMM write-lock congestion moves with Program failure rate | +0.121 | 634 | 0.0023 |
| Total TPS moves with Activity index | +0.113 | 674 | 0.0032 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 656.35K USD | DeFiLlama: 1.19M USD | -57.66% | *indicative*: 0.55x, within the order-of-magnitude band |
| SOL price | coingecko: 104.97 USD | Jupiter (on-chain DEX): 105.26 USD | -0.28% | agree |
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

**Latest Agave release:** [v4.4.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.2) (2026-08-28)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[Morning Minute: Solana Jumps with Network Inflation Set to Drop](https://decrypt.co/376800/morning-minute-solana-jumps-with-network-inflation-set-to-drop)** - Decrypt, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[DeFi Development Corp resumes Solana purchases, acquiring nearly 20,000 SOL](https://www.theblock.co/news/business/2026-08-27-defi-development-resumes-solana-purchases-acquiring-nearly-20000-sol-412932)** - The Block, 2026-08-27
- **[Solana Is Having Its Best Month Since 2024—With a Historic Governance Vote on Deck](https://decrypt.co/376706/solana-best-month-since-2024-historic-governance-vote)** - Decrypt, 2026-08-27
- **[Charles Schwab to add Solana, Avalanche and Chainlink to crypto trading platform](https://www.theblock.co/news/business/2026-08-27-charles-schwab-add-solana-avalanche-chainlink-to-crypto-trading-platform-412923)** - The Block, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[Galaxy Opens Retail Crypto-Backed Credit Lines on Bitcoin, Ethereum and Solana](https://decrypt.co/376646/galaxy-crypto-credit-lines-bitcoin-ethereum-solana)** - Decrypt, 2026-08-26
- **[Solana Treasury Firm Invites Investors to Look 'Beyond the Price of SOL'](https://decrypt.co/376619/solana-treasury-sol-data-beyond-price)** - Decrypt, 2026-08-26
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
