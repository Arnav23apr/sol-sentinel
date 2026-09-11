# Solana Ecosystem Report

*Generated 2026-09-11 21:25 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 20.5 robust standard deviations above its 7-day baseline: a 1520.8% move to 0.39 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.6K |
| Slot time | 317.5 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1033 (0.56% complete, ~37.9h remaining) |
| Lifetime transactions | 547.5B |
| Circulating supply | 586.6M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,410 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 25,100 / 410,000 lamports |
| Paying no priority fee | 27.50% of 4,826 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 24.70% of slots needed a priority fee (max 6.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 12 |
| Delinquent stake | 0.39% |
| Total active stake | 435.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.51% / 24.49% / 35.86% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.18% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.03% | 7% |
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
| SOL price | $102.92 (+2.98% 24h) |
| Market cap | $60.36B (rank #7) |
| 24h volume | $4.44B |
| ATH | $293.31 (-64.91% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.87B |
| Stablecoin supply | $16.20B |
| DEX volume (24h) | $2.92B (-2.61% 1d) |
| App fees (24h, all protocols) | $14.61M |
| Chain fees (24h) | $709.33K |
| Jito MEV tips (24h) | $146.00K |
| **REV - Real Economic Value (24h)** | **$855.33K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.23B | +2.01% |
| USDT | $2.61B | -11.20% |
| USDGO | $1.38B | +5.12% |
| USD1 | $1.30B | +6.76% |
| BUIDL | $992.60M | +5.84% |
| PYUSD | $694.54M | -19.24% |
| USDG | $600.63M | +6.86% |
| USDe | $536.35M | +0.09% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $505.05M |
| PumpSwap | $468.14M |
| BisonFi | $395.81M |
| HumidiFi | $322.67M |
| Tessera V | $232.00M |
| Meteora DLMM | $220.43M |
| Orca DEX | $201.48M |
| Manifest Trade | $151.47M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.79M |
| Raydium AMM | $2.07M |
| Axiom | $1.40M |
| fomo Wallet | $1.33M |
| pump.fun | $1.14M |
| Meteora DLMM | $862.62K |
| StonkFun | $759.29K |
| Orca DEX | $595.02K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 285 |
| Persistently-active cohort (capture-recapture est.) | 3.5K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $125.15M |
| xStocks holder positions | 513.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.91B |

## Program activity and chain health

Chain tip lag: **+11.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 186,142 (approx.) | 47.80% | 0.3 s |
| Jupiter v6 | 16,166 | 89.30% | 3.5 s |
| Raydium AMM v4 | 10,058 | 40.60% | 5.7 s |
| Orca Whirlpools | 9,420 | 60.80% | 6.3 s |
| Pump.fun | 8,461 | 55.90% | 7 s |

Median failure rate across the sampled programs: **55.90%** (range 40.60% to 89.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.07K SOL**.

## Exchange and large-holder balances

11.72M SOL ($1.21B) across 8 publicly-attributed accounts. Net **68K SOL (0.58%) moved onto exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $945.68M | 0.3/h | 1 |
| Binance (2) | 1.82M | $187.66M | 1.3K/h | 0 |
| Gate.io | 279.80K | $28.80M | 129.1/h | 0 |
| Bybit | 232.18K | $23.90M | 33.7/h | 0 |
| Coinbase (2) | 92.16K | $9.48M | 554.7/h | 0 |
| Bitget | 50.96K | $5.24M | 208/h | 0 |
| Coinbase | 28.91K | $2.98M | 531/h | 0 |
| Kraken | 27.93K | $2.87M | 267.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 804 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.225 | 763 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.191 | 770 | 0.0000 |
| Total TPS moves with Slot time | +0.152 | 770 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.147 | 729 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.146 | 729 | 0.0001 |
| Total TPS moves with Program failure rate | +0.128 | 751 | 0.0005 |
| Non-vote TPS moves with Program failure rate | +0.128 | 751 | 0.0004 |
| Share paying base fee only moves with Activity index | +0.111 | 793 | 0.0017 |
| Slot time moves with AMM write-lock congestion | +0.107 | 729 | 0.0037 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 569.18K USD | DeFiLlama: 709.33K USD | -21.92% | *indicative*: 0.80x, within the order-of-magnitude band |
| SOL price | coingecko: 102.92 USD | Jupiter (on-chain DEX): 102.86 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 586.62M SOL | CoinGecko: 586.54M SOL | +0.01% | agree |

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
