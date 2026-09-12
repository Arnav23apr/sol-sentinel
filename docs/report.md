# Solana Ecosystem Report

*Generated 2026-09-12 01:17 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 36.9 robust standard deviations above its 7-day baseline: a 2733.3% move to 0.68 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 1.8K |
| Slot time | 315 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1033 (10.73% complete, ~33.7h remaining) |
| Lifetime transactions | 547.6B |
| Circulating supply | 586.6M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,319 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 15,200 / 248,529 lamports |
| Paying no priority fee | 29.90% of 4,830 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 24.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 13 |
| Delinquent stake | 0.68% |
| Total active stake | 433.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.55% / 24.56% / 35.97% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.25% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.05% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.77% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.88% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.62% | 5% |
| 5 | `8Gbw…F8iD` | 9.7M | 2.23% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.08% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.70% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.60% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $102.17 (+2.91% 24h) |
| Market cap | $59.92B (rank #7) |
| 24h volume | $4.60B |
| ATH | $293.31 (-65.17% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.88B |
| Stablecoin supply | $16.27B |
| DEX volume (24h) | $3.25B (+11.21% 1d) |
| App fees (24h, all protocols) | $16.60M |
| Chain fees (24h) | $709.33K |
| Jito MEV tips (24h) | $147.50K |
| **REV - Real Economic Value (24h)** | **$856.83K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.29B | +2.85% |
| USDT | $2.61B | -11.20% |
| USDGO | $1.38B | +5.12% |
| USD1 | $1.30B | +6.76% |
| BUIDL | $992.60M | +5.84% |
| PYUSD | $708.30M | -17.61% |
| USDG | $601.25M | +6.97% |
| USDe | $536.19M | +0.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $562.91M |
| BisonFi | $395.81M |
| Meteora DLMM | $363.04M |
| HumidiFi | $322.67M |
| PumpSwap | $294.17M |
| Orca DEX | $272.49M |
| Tessera V | $232.00M |
| Manifest Trade | $165.93M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.79M |
| Raydium AMM | $2.18M |
| Axiom | $1.40M |
| fomo Wallet | $1.33M |
| pump.fun | $1.14M |
| Meteora DLMM | $862.62K |
| Orca DEX | $771.26K |
| StonkFun | $759.29K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 292 |
| Persistently-active cohort (capture-recapture est.) | 4.4K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $123.32M |
| xStocks holder positions | 517.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

## Program activity and chain health

Chain tip lag: **+11.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 64,667 (approx.) | 28.10% | 0.6 s |
| Orca Whirlpools | 4,485 | 62.00% | 13.2 s |
| Jupiter v6 | 3,453 | 57.20% | 17.3 s |
| Pump.fun | 2,826 | 52.50% | 21.1 s |
| Raydium AMM v4 | 2,318 | 52.30% | 25.8 s |

Median failure rate across the sampled programs: **52.50%** (range 28.10% to 62.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **970.45 SOL**.

## Exchange and large-holder balances

11.71M SOL ($1.20B) across 8 publicly-attributed accounts. Net **31K SOL (0.26%) moved onto exchanges** over the last 19.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $938.78M | 0.3/h | 1 |
| Binance (2) | 1.89M | $192.86M | 884.5/h | 0 |
| Gate.io | 274.92K | $28.09M | 121/h | 0 |
| Bybit | 232.18K | $23.72M | 39.3/h | 0 |
| Bitget | 42.23K | $4.31M | 143.8/h | 0 |
| Coinbase | 28.55K | $2.92M | 434.3/h | 0 |
| Kraken | 26.13K | $2.67M | 182.2/h | 0 |
| Coinbase (2) | 25.92K | $2.65M | 412.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 806 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.230 | 765 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 772 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 772 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.147 | 731 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.146 | 731 | 0.0001 |
| Total TPS moves with Program failure rate | +0.128 | 753 | 0.0004 |
| Non-vote TPS moves with Program failure rate | +0.128 | 753 | 0.0004 |
| Share paying base fee only moves with Activity index | +0.111 | 795 | 0.0017 |
| Slot time moves with AMM write-lock congestion | +0.107 | 731 | 0.0037 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 368.61K USD | DeFiLlama: 709.33K USD | -63.22% | *indicative*: 0.52x, within the order-of-magnitude band |
| SOL price | coingecko: 102.17 USD | Jupiter (on-chain DEX): 102.17 USD | 0.00% | agree |
| Circulating supply | getSupply (RPC): 586.63M SOL | CoinGecko: 586.63M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-11
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-11
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
