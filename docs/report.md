# Solana Ecosystem Report

*Generated 2026-09-02 00:38 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.6K |
| TPS (non-vote) | 1.5K |
| Slot time | 316.6 ms |
| Slot | 444M |
| Block height | 422M |
| Epoch | 1026 (76.28% complete, ~9.0h remaining) |
| Lifetime transactions | 544.3B |
| Circulating supply | 585.2M SOL |
| Inflation (annual) | 3.67% |
| Median transaction fee | 6,488 lamports (about $0.00065) |
| Transaction fee p90 / p99 | 35,270 / 435,471 lamports |
| Paying no priority fee | 17.80% of 5,023 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 5.6M µlam/CU) |
| Node version (RPC) | 4.2.1 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 16 |
| Delinquent stake | 0.04% |
| Total active stake | 438.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.26% / 24.18% / 35.45% |
| Commission (stake-weighted, delegatable validators) | 3.76% |
| Stake on private (100% commission) validators | 23.95% |

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
| SOL price | $99.77 (-3.45% 24h) |
| Market cap | $58.41B (rank #7) |
| 24h volume | $3.43B |
| ATH | $293.31 (-65.98% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.70B |
| Stablecoin supply | $15.54B |
| DEX volume (24h) | $2.50B (+29.63% 1d) |
| App fees (24h, all protocols) | $14.36M |
| Chain fees (24h) | $836.26K |
| Jito MEV tips (24h) | $192.41K |
| **REV - Real Economic Value (24h)** | **$1.03M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.64B | -7.25% |
| USDT | $2.83B | 0.00% |
| USDGO | $1.25B | +4.27% |
| USD1 | $1.21B | +10.10% |
| BUIDL | $887.01M | +7.03% |
| PYUSD | $737.66M | +9.37% |
| USDG | $614.82M | -3.06% |
| USDe | $536.89M | +0.12% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $939.21M |
| BisonFi | $232.85M |
| Orca DEX | $218.49M |
| Raydium AMM | $152.53M |
| Meteora DLMM | $149.33M |
| Manifest Trade | $147.07M |
| Axiom | $113.58M |
| Jupiterz | $101.70M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.73M |
| pump.fun | $1.72M |
| Axiom | $1.65M |
| fomo Wallet | $1.08M |
| Raydium AMM | $851.21K |
| Meteora DLMM | $403.59K |
| Sanctum Validator LSTs | $377.96K |
| Collector Crypt | $329.81K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 246 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $431.96M |
| xStocks 24h DEX volume | $27.07M |
| xStocks holder positions | 308.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.07B |

Top tokenized equities: TSLAX ($65.81M), CRCLX ($65.09M), MSTRX ($51.95M), SPYX ($48.29M), GOOGLX ($30.67M)

## Program activity and chain health

Chain tip lag: **+10.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 49,337 | 35.80% | 0.9 s |
| Pump.fun | 16,195 | 82.10% | 3.5 s |
| Jupiter v6 | 6,208 | 73.90% | 9.2 s |
| Orca Whirlpools | 3,097 | 60.10% | 19.3 s |
| Raydium AMM v4 | 1,729 | 56.90% | 30.4 s |

Median failure rate across the sampled programs: **60.10%** (range 35.80% to 82.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.33 SOL**.

## Exchange and large-holder balances

11.72M SOL ($1.17B) across 8 publicly-attributed accounts. Net **90K SOL (0.77%) moved off exchanges** over the last 21.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $916.73M | 1/h | 1 |
| Binance (2) | 1.84M | $183.97M | 935.1/h | 0 |
| Gate.io | 329.83K | $32.91M | 150/h | 0 |
| Bybit | 183.00K | $18.26M | 65.4/h | 0 |
| Bitget | 97.51K | $9.73M | 174.7/h | 0 |
| Kraken | 35.38K | $3.53M | 238.4/h | 0 |
| Coinbase (2) | 22.97K | $2.29M | 364/h | 0 |
| Coinbase | 22.17K | $2.21M | 341.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 734 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.255 | 693 | 0.0000 |
| DEX volume moves with App fees | +0.207 | 693 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.202 | 700 | 0.0000 |
| Total TPS moves with Slot time | +0.163 | 700 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.138 | 659 | 0.0004 |
| Total TPS moves with AMM write-lock congestion | +0.137 | 659 | 0.0004 |
| Non-vote TPS moves with Activity index | +0.134 | 699 | 0.0004 |
| AMM write-lock congestion moves with Program failure rate | +0.126 | 659 | 0.0012 |
| Total TPS moves with Activity index | +0.125 | 699 | 0.0009 |
| Slot time moves with AMM write-lock congestion | +0.119 | 659 | 0.0021 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 563.56K USD | DeFiLlama: 836.26K USD | -38.96% | *indicative*: 0.67x, within the order-of-magnitude band |
| SOL price | coingecko: 99.77 USD | Jupiter (on-chain DEX): 99.67 USD | +0.10% | agree |
| Circulating supply | getSupply (RPC): 585.21M SOL | CoinGecko: 585.21M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-08-31
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-09-01
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-08-31
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-08-31
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-01
- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20

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

- **[Solana Treasury DeFi Development Corp Eyes $20 Million Raise to Buy More SOL](https://decrypt.co/377068/defi-development-corp-20-million-raise-more-solana)** - Decrypt, 2026-09-01
- **[DeFi Development Corp proposes $20 million preferred stock offering to buy more SOL](https://www.theblock.co/news/business/2026-08-31-solana-defi-development-preferred-stock-offering-413190)** - The Block, 2026-09-01
- **[Solana fees hit record as validators double pace of inflation cuts](https://www.theblock.co/news/ecosystems/2026-08-31-solana-fees-hit-record-as-validators-double-pace-of-inflation-cuts-413135)** - The Block, 2026-08-31
- **[OpenSea adds Solana NFT trading more than four years after initial beta](https://www.theblock.co/news/markets/2026-08-31-opensea-solana-nft-trading-413128)** - The Block, 2026-08-31
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27
- **[The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers)** - Solana.com, 2026-08-27
- **[What is an LSM Tree? The Log-Structured Merge Tree Explained](https://www.helius.dev/blog/lsm-tree-explained)** - Helius, 2026-08-25
- **[Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026)** - Solana.com, 2026-08-24
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
