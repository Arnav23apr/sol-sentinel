# Solana Ecosystem Report

*Generated 2026-09-12 10:10 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 20.0 robust standard deviations above its 7-day baseline: a 1608.3% move to 0.41 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.2K |
| TPS (non-vote) | 1.1K |
| Slot time | 318.3 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1033 (34.11% complete, ~25.2h remaining) |
| Lifetime transactions | 547.7B |
| Circulating supply | 586.6M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,350 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 32,000 / 445,483 lamports |
| Paying no priority fee | 26.20% of 3,569 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 18.1M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 13 |
| Delinquent stake | 0.41% |
| Total active stake | 435.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.51% / 24.50% / 35.87% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.19% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.76% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.88% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.61% | 5% |
| 5 | `8Gbw…F8iD` | 9.7M | 2.22% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.69% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.60% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $102.13 (+2.51% 24h) |
| Market cap | $59.92B (rank #7) |
| 24h volume | $4.51B |
| ATH | $293.31 (-65.18% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.89B |
| Stablecoin supply | $16.21B |
| DEX volume (24h) | $3.25B (+11.15% 1d) |
| App fees (24h, all protocols) | $17.54M |
| Chain fees (24h) | $835.74K |
| Jito MEV tips (24h) | $134.40K |
| **REV - Real Economic Value (24h)** | **$970.14K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.26B | -0.07% |
| USDT | $2.59B | -6.15% |
| USDGO | $1.38B | +2.02% |
| USD1 | $1.30B | +4.41% |
| BUIDL | $992.60M | +1.50% |
| PYUSD | $706.72M | -1.79% |
| USDG | $598.03M | +3.23% |
| USDe | $535.47M | +0.43% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $446.42M |
| BisonFi | $395.81M |
| Meteora DLMM | $363.04M |
| HumidiFi | $322.67M |
| PumpSwap | $294.17M |
| Tessera V | $232.00M |
| Orca DEX | $231.78M |
| Manifest Trade | $172.46M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.85M |
| StonkFun | $1.84M |
| Raydium AMM | $1.71M |
| Axiom | $1.60M |
| fomo Wallet | $1.33M |
| Meteora DLMM | $1.22M |
| pump.fun | $950.51K |
| Orca DEX | $535.67K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 242 |
| Persistently-active cohort (capture-recapture est.) | 2.9K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $110.38M |
| xStocks holder positions | 519.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

## Program activity and chain health

Chain tip lag: **+11.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 42,177 | 18.30% | 1.3 s |
| Orca Whirlpools | 3,888 | 64.90% | 15.3 s |
| Jupiter v6 | 2,507 | 54.50% | 23.2 s |
| Pump.fun | 1,964 | 23.30% | 30.2 s |
| Raydium AMM v4 | 1,391 | 23.70% | 43 s |

Median failure rate across the sampled programs: **23.70%** (range 18.30% to 64.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **571.34 SOL**.

## Exchange and large-holder balances

11.75M SOL ($1.20B) across 8 publicly-attributed accounts. Net **1K SOL (0.01%) moved onto exchanges** over the last 22.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $938.42M | 0.3/h | 1 |
| Binance (2) | 1.89M | $193.32M | 1.1K/h | 0 |
| Gate.io | 304.04K | $31.05M | 149.9/h | 0 |
| Bybit | 232.18K | $23.71M | 29.2/h | 0 |
| Bitget | 52.54K | $5.37M | 248.3/h | 0 |
| Kraken | 28.62K | $2.92M | 194.7/h | 0 |
| Coinbase | 27.44K | $2.80M | 188.9/h | 0 |
| Coinbase (2) | 26.94K | $2.75M | 193.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 808 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.223 | 767 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.191 | 774 | 0.0000 |
| Total TPS moves with Slot time | +0.152 | 774 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.148 | 733 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.147 | 733 | 0.0001 |
| Total TPS moves with Program failure rate | +0.131 | 755 | 0.0003 |
| Non-vote TPS moves with Program failure rate | +0.131 | 755 | 0.0003 |
| Slot time moves with AMM write-lock congestion | +0.110 | 733 | 0.0029 |
| Share paying base fee only moves with Activity index | +0.110 | 797 | 0.0019 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 348.10K USD | DeFiLlama: 835.74K USD | -82.38% | *indicative*: 0.42x, within the order-of-magnitude band |
| SOL price | coingecko: 102.13 USD | Jupiter (on-chain DEX): 102.12 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 586.63M SOL | CoinGecko: 586.63M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-11
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-12
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-11

**Recently merged SIMDs:**

- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08
- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12

**Latest Agave release:** [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) (2026-09-11)

**Latest Firedancer release:** [v26.08.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.4) (2026-09-10)

## Ecosystem news

- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
