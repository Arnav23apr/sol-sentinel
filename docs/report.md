# Solana Ecosystem Report

*Generated 2026-08-29 04:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 3.6 robust standard deviations above its 7-day baseline: a 8.7% move to 103.64 USD from a typical 95.34.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 5.4 robust standard deviations above its 7-day baseline: a 5.1% move to 5,870,469,439.00 USD from a typical 5,584,178,233.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 1.5K |
| Slot time | 317.5 ms |
| Slot | 443M |
| Block height | 421M |
| Epoch | 1024 (33.49% complete, ~25.3h remaining) |
| Lifetime transactions | 543.0B |
| Circulating supply | 584.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 5,500 lamports (about $0.00057) |
| Transaction fee p90 / p99 | 22,938 / 805,000 lamports |
| Paying no priority fee | 21.30% of 6,040 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 6.00% of slots needed a priority fee (max 13.7M µlam/CU) |
| Node version (RPC) | 4.2.1 |

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
| Stake on private (100% commission) validators | 24.08% |

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
| SOL price | $103.64 (-2.90% 24h) |
| Market cap | $60.54B (rank #7) |
| 24h volume | $5.39B |
| ATH | $293.31 (-64.67% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.87B |
| Stablecoin supply | $15.99B |
| DEX volume (24h) | $2.62B (-29.33% 1d) |
| App fees (24h, all protocols) | $15.45M |
| Chain fees (24h) | $946.01K |
| Jito MEV tips (24h) | $233.55K |
| **REV - Real Economic Value (24h)** | **$1.18M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.03B | -4.43% |
| USDT | $2.84B | +3.47% |
| USDGO | $1.25B | +4.60% |
| USD1 | $1.16B | +9.14% |
| BUIDL | $886.54M | +14.08% |
| PYUSD | $693.62M | +2.75% |
| USDG | $622.88M | +1.65% |
| USDe | $534.51M | -0.42% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $576.29M |
| Orca DEX | $338.68M |
| BisonFi | $331.44M |
| Meteora DLMM | $279.39M |
| Raydium AMM | $172.70M |
| Axiom | $165.79M |
| Manifest Trade | $135.00M |
| pump.fun | $117.62M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.11M |
| pump.fun | $2.16M |
| Axiom | $1.85M |
| fomo Wallet | $729.95K |
| Meteora DLMM | $621.75K |
| Jupiter Perpetual Exchange | $498.13K |
| Collector Crypt | $437.31K |
| Sanctum Validator LSTs | $436.02K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 301 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $431.79M |
| xStocks 24h DEX volume | $35.09M |
| xStocks holder positions | 287.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: TSLAX ($64.58M), CRCLX ($64.46M), MSTRX ($52.26M), SPYX ($49.32M), GOOGLX ($31.10M)

## Program activity and chain health

Chain tip lag: **+11.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 40,819 | 17.40% | 1.3 s |
| Pump.fun | 19,906 | 84.70% | 2.9 s |
| Jupiter v6 | 3,361 | 54.20% | 17.8 s |
| Raydium AMM v4 | 1,585 | 29.20% | 37.8 s |
| Orca Whirlpools | 1,388 | 49.10% | 42.5 s |

Median failure rate across the sampled programs: **49.10%** (range 17.40% to 84.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **917.88 SOL**.

## Exchange and large-holder balances

11.64M SOL ($1.21B) across 8 publicly-attributed accounts. Net **181K SOL (1.53%) moved off exchanges** over the last 14.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $952.29M | 1.2/h | 2 |
| Binance (2) | 1.66M | $172.04M | 1.6K/h | 0 |
| Bybit | 377.26K | $39.10M | 20.1/h | 0 |
| Gate.io | 277.25K | $28.73M | 236.7/h | 0 |
| Bitget | 63.62K | $6.59M | 156.2/h | 0 |
| Kraken | 26.43K | $2.74M | 148.6/h | 0 |
| Coinbase (2) | 24.51K | $2.54M | 562.5/h | 0 |
| Coinbase | 24.14K | $2.50M | 450.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 711 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.232 | 670 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.196 | 677 | 0.0000 |
| DEX volume moves with App fees | +0.182 | 670 | 0.0000 |
| Total TPS moves with Slot time | +0.156 | 677 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.132 | 636 | 0.0009 |
| Non-vote TPS moves with AMM write-lock congestion | +0.131 | 636 | 0.0009 |
| AMM write-lock congestion moves with Program failure rate | +0.126 | 636 | 0.0015 |
| Non-vote TPS moves with Activity index | +0.122 | 676 | 0.0015 |
| Slot time moves with AMM write-lock congestion | +0.121 | 636 | 0.0023 |
| Total TPS moves with Activity index | +0.115 | 676 | 0.0029 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 885.84K USD | DeFiLlama: 946.01K USD | -6.57% | *indicative*: 0.94x, within the order-of-magnitude band |
| SOL price | coingecko: 103.64 USD | Jupiter (on-chain DEX): 103.75 USD | -0.11% | agree |
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
