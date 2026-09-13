# Solana Ecosystem Report

*Generated 2026-09-13 16:30 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.1 robust standard deviations above its 7-day baseline: a 655.6% move to 0.41 % from a typical 0.05.
- 🟠 **DEX volume (24h)** (warning): DEX volume (24h) is 4.9 robust standard deviations below its 7-day baseline: a 41.1% move to 1,691,135,695.00 USD from a typical 2,872,025,885.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.4K |
| TPS (non-vote) | 2.3K |
| Slot time | 314.1 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1034 (14.10% complete, ~32.4h remaining) |
| Lifetime transactions | 548.1B |
| Circulating supply | 586.7M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,500 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 21,016 / 502,586 lamports |
| Paying no priority fee | 24.40% of 3,294 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 27.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 12 |
| Delinquent stake | 0.41% |
| Total active stake | 436.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 24.39% / 35.66% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.08% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.02% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.74% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.60% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.20% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.69% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.59% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $100.72 (-1.26% 24h) |
| Market cap | $59.09B (rank #7) |
| 24h volume | $1.83B |
| ATH | $293.31 (-65.66% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.85B |
| Stablecoin supply | $16.11B |
| DEX volume (24h) | $1.69B (-46.88% 1d) |
| App fees (24h, all protocols) | $13.52M |
| Chain fees (24h) | $708.83K |
| Jito MEV tips (24h) | $105.54K |
| **REV - Real Economic Value (24h)** | **$814.37K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.27B | -0.43% |
| USDT | $2.48B | -10.12% |
| USDGO | $1.38B | +2.02% |
| USD1 | $1.31B | +3.93% |
| BUIDL | $992.60M | +1.50% |
| PYUSD | $706.90M | -6.02% |
| USDG | $601.63M | +3.33% |
| USDe | $532.99M | -0.56% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $377.15M |
| Raydium AMM | $261.84M |
| fomo Wallet | $201.17M |
| BisonFi | $162.68M |
| Meteora DLMM | $161.06M |
| Orca DEX | $99.65M |
| HumidiFi | $85.03M |
| Tessera V | $81.22M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.34M |
| pump.fun | $1.40M |
| Axiom | $1.34M |
| fomo Wallet | $1.18M |
| Raydium AMM | $1.01M |
| Meteora DLMM | $1.01M |
| StonkFun | $783.82K |
| Collector Crypt | $494.92K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 214 |
| Persistently-active cohort (capture-recapture est.) | 2.1K |
| Unique payers across sampled blocks | 1.2K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $76.00M |
| xStocks holder positions | 529.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.93B |

## Program activity and chain health

Chain tip lag: **+11.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 86,246 (approx.) | 32.10% | 0.6 s |
| Pump.fun | 16,984 | 75.00% | 3.5 s |
| Jupiter v6 | 11,124 | 74.10% | 5.3 s |
| Orca Whirlpools | 6,063 | 56.80% | 9.7 s |
| Raydium AMM v4 | 1,089 | 17.00% | 54.7 s |

Median failure rate across the sampled programs: **56.80%** (range 17.00% to 75.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.19K SOL**.

## Exchange and large-holder balances

11.73M SOL ($1.18B) across 8 publicly-attributed accounts. Net **12K SOL (0.11%) moved off exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $925.46M | 0.3/h | 1 |
| Binance (2) | 1.89M | $190.21M | 863.3/h | 0 |
| Gate.io | 304.41K | $30.66M | 118.5/h | 0 |
| Bybit | 232.18K | $23.39M | 30.9/h | 0 |
| Bitget | 35.99K | $3.63M | 170.9/h | 0 |
| Kraken | 28.44K | $2.86M | 225/h | 0 |
| Coinbase (2) | 26.13K | $2.63M | 353.6/h | 0 |
| Coinbase | 26.04K | $2.62M | 384.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 817 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.225 | 776 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.193 | 783 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.155 | 742 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 783 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.153 | 742 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.139 | 764 | 0.0001 |
| Total TPS moves with Program failure rate | +0.138 | 764 | 0.0001 |
| Slot time moves with AMM write-lock congestion | +0.117 | 742 | 0.0014 |
| Share paying base fee only moves with Activity index | +0.117 | 806 | 0.0009 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 345.14K USD | DeFiLlama: 708.83K USD | -69.01% | *indicative*: 0.49x, within the order-of-magnitude band |
| SOL price | coingecko: 100.72 USD | Jupiter (on-chain DEX): 100.69 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 586.73M SOL | CoinGecko: 586.73M SOL | -0.00% | agree |

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
