# Solana Ecosystem Report

*Generated 2026-09-11 15:26 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 23.9 robust standard deviations above its 7-day baseline: a 1770.8% move to 0.45 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.4K |
| TPS (non-vote) | 2.3K |
| Slot time | 318.3 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1032 (84.90% complete, ~5.8h remaining) |
| Lifetime transactions | 547.4B |
| Circulating supply | 586.5M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,415 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 25,469 / 505,000 lamports |
| Paying no priority fee | 26.20% of 3,755 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 33.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 674 |
| Delinquent validators | 16 |
| Delinquent stake | 0.45% |
| Total active stake | 437.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.32% / 35.64% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.08% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.99% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.60% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.19% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.3M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.57% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $103.31 (+3.65% 24h) |
| Market cap | $60.60B (rank #7) |
| 24h volume | $4.00B |
| ATH | $293.31 (-64.78% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.83B |
| Stablecoin supply | $16.04B |
| DEX volume (24h) | $2.92B (-2.61% 1d) |
| App fees (24h, all protocols) | $14.61M |
| Chain fees (24h) | $709.33K |
| Jito MEV tips (24h) | $129.30K |
| **REV - Real Economic Value (24h)** | **$838.63K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.03B | -1.15% |
| USDT | $2.67B | -9.17% |
| USDGO | $1.38B | +5.13% |
| USD1 | $1.28B | +5.17% |
| BUIDL | $992.51M | +5.83% |
| PYUSD | $693.22M | -19.35% |
| USDG | $605.01M | +7.63% |
| USDe | $536.07M | +0.09% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $468.14M |
| Raydium AMM | $432.33M |
| BisonFi | $395.81M |
| HumidiFi | $322.67M |
| Tessera V | $232.00M |
| Meteora DLMM | $220.43M |
| Orca DEX | $201.48M |
| Manifest Trade | $138.50M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.79M |
| Raydium AMM | $1.46M |
| Axiom | $1.40M |
| fomo Wallet | $1.33M |
| pump.fun | $1.14M |
| Meteora DLMM | $862.62K |
| StonkFun | $759.29K |
| Orca DEX | $595.02K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 224 |
| Persistently-active cohort (capture-recapture est.) | 2.4K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $119.16M |
| xStocks holder positions | 508.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.90B |

## Program activity and chain health

Chain tip lag: **+12.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 50,016 | 24.90% | 1 s |
| Raydium AMM v4 | 18,473 | 41.50% | 3.2 s |
| Orca Whirlpools | 17,512 | 51.70% | 3.2 s |
| Jupiter v6 | 15,166 | 74.40% | 3.5 s |
| Pump.fun | 11,983 | 76.60% | 4.5 s |

Median failure rate across the sampled programs: **51.70%** (range 24.90% to 76.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **235.20 SOL**.

## Exchange and large-holder balances

11.72M SOL ($1.21B) across 8 publicly-attributed accounts. Net **54K SOL (0.46%) moved onto exchanges** over the last 20.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $949.26M | 0.3/h | 1 |
| Binance (2) | 1.81M | $186.95M | 1.3K/h | 0 |
| Gate.io | 283.15K | $29.25M | 319.1/h | 0 |
| Bybit | 232.18K | $23.99M | 73.4/h | 0 |
| Coinbase (2) | 106.19K | $10.97M | 559/h | 0 |
| Bitget | 55.45K | $5.73M | 299/h | 0 |
| Kraken | 28.60K | $2.96M | 252.3/h | 0 |
| Coinbase | 18.98K | $1.96M | 564.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 802 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.225 | 761 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.193 | 768 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 768 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.146 | 727 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.145 | 727 | 0.0001 |
| Total TPS moves with Program failure rate | +0.126 | 749 | 0.0006 |
| Non-vote TPS moves with Program failure rate | +0.125 | 749 | 0.0006 |
| Share paying base fee only moves with Activity index | +0.113 | 791 | 0.0015 |
| Slot time moves with AMM write-lock congestion | +0.109 | 727 | 0.0031 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 391.28K USD | DeFiLlama: 709.33K USD | -57.79% | *indicative*: 0.55x, within the order-of-magnitude band |
| SOL price | coingecko: 103.31 USD | Jupiter (on-chain DEX): 103.43 USD | -0.12% | agree |
| Circulating supply | getSupply (RPC): 586.54M SOL | CoinGecko: 586.54M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-11
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-09
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02

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
