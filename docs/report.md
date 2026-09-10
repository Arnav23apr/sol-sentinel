# Solana Ecosystem Report

*Generated 2026-09-10 18:34 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.0K |
| Slot time | 317.5 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1032 (29.95% complete, ~26.7h remaining) |
| Lifetime transactions | 547.1B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,324 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 34,279 / 410,000 lamports |
| Paying no priority fee | 29.60% of 4,559 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 35.30% of slots needed a priority fee (max 19.4M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 12 |
| Delinquent stake | 0.02% |
| Total active stake | 439.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.31% / 24.22% / 35.49% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.97% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.97% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.18% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.3M | 1.67% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.57% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $99.31 (-4.19% 24h) |
| Market cap | $58.23B (rank #7) |
| 24h volume | $3.31B |
| ATH | $293.31 (-66.14% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.77B |
| Stablecoin supply | $16.02B |
| DEX volume (24h) | $3.00B (+10.69% 1d) |
| App fees (24h, all protocols) | $15.72M |
| Chain fees (24h) | $978.48K |
| Jito MEV tips (24h) | $181.66K |
| **REV - Real Economic Value (24h)** | **$1.16M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.97B | +3.39% |
| USDT | $2.68B | -7.57% |
| USDGO | $1.38B | +10.24% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $992.27M | +11.40% |
| PYUSD | $733.36M | -8.24% |
| USDG | $597.60M | -1.62% |
| USDe | $536.06M | +0.09% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $402.77M |
| Raydium AMM | $347.70M |
| PumpSwap | $340.96M |
| Meteora DLMM | $322.25M |
| HumidiFi | $285.64M |
| Tessera V | $248.02M |
| Orca DEX | $170.35M |
| Manifest Trade | $148.45M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.36M |
| Axiom | $1.88M |
| fomo Wallet | $1.52M |
| pump.fun | $1.41M |
| Raydium AMM | $1.26M |
| Meteora DLMM | $1.19M |
| StonkFun | $968.30K |
| Orca DEX | $543.66K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 290 |
| Persistently-active cohort (capture-recapture est.) | 3.5K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $181.63M |
| xStocks holder positions | 471.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

## Program activity and chain health

Chain tip lag: **+11.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 66,898 (approx.) | 18.60% | 0.6 s |
| Jupiter v6 | 7,385 | 74.80% | 7.9 s |
| Orca Whirlpools | 2,944 | 50.70% | 20.3 s |
| Pump.fun | 2,904 | 27.60% | 20.6 s |
| Raydium AMM v4 | 2,180 | 42.90% | 27.3 s |

Median failure rate across the sampled programs: **42.90%** (range 18.60% to 74.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **235.20 SOL**.

## Exchange and large-holder balances

11.67M SOL ($1.16B) across 8 publicly-attributed accounts. Net **93K SOL (0.80%) moved onto exchanges** over the last 21.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $912.50M | 0.3/h | 1 |
| Binance (2) | 1.84M | $182.52M | 1.6K/h | 0 |
| Gate.io | 290.00K | $28.80M | 191.2/h | 0 |
| Bybit | 211.98K | $21.05M | 34.5/h | 0 |
| Bitget | 61.11K | $6.07M | 211.5/h | 0 |
| Kraken | 34.75K | $3.45M | 196.5/h | 0 |
| Coinbase (2) | 23.48K | $2.33M | 447.8/h | 0 |
| Coinbase | 21.24K | $2.11M | 428.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 796 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.223 | 755 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.196 | 762 | 0.0000 |
| Total TPS moves with Slot time | +0.157 | 762 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.143 | 721 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.142 | 721 | 0.0001 |
| Total TPS moves with Program failure rate | +0.124 | 743 | 0.0007 |
| Non-vote TPS moves with Program failure rate | +0.123 | 743 | 0.0008 |
| Slot time moves with AMM write-lock congestion | +0.114 | 721 | 0.0022 |
| Non-vote TPS moves with Activity index | +0.110 | 761 | 0.0024 |
| Share paying base fee only moves with Activity index | +0.109 | 785 | 0.0022 |
| Total TPS moves with Activity index | +0.103 | 761 | 0.0046 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 492.31K USD | DeFiLlama: 978.48K USD | -66.11% | *indicative*: 0.50x, within the order-of-magnitude band |
| SOL price | coingecko: 99.31 USD | Jupiter (on-chain DEX): 99.27 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 586.34M SOL | CoinGecko: 586.34M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 Amendment: Specify use of sol_get_sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-10
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

**Latest Agave release:** [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) (2026-09-04)

**Latest Firedancer release:** [v26.08.3](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.3) (2026-09-10)

## Ecosystem news

- **[Solana treasury firm SkyAI faces board challenge from would-be acquirer Forward Industries, shareholder group](https://www.theblock.co/news/business/2026-09-09-solana-treasury-firm-skyai-board-challenge-would-be-acquirer-forward-industries-shareholder-group-414061)** - The Block, 2026-09-09
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
