# Solana Ecosystem Report

*Generated 2026-09-13 12:08 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.9 robust standard deviations above its 7-day baseline: a 750.0% move to 0.41 % from a typical 0.05.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.3K |
| TPS (non-vote) | 1.2K |
| Slot time | 315 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1034 (2.59% complete, ~36.8h remaining) |
| Lifetime transactions | 548.0B |
| Circulating supply | 586.7M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,410 lamports (about $0.00054) |
| Transaction fee p90 / p99 | 34,808 / 805,000 lamports |
| Paying no priority fee | 27.10% of 4,751 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 40.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
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
| SOL price | $99.72 (-2.41% 24h) |
| Market cap | $58.51B (rank #7) |
| 24h volume | $1.87B |
| ATH | $293.31 (-66.00% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.84B |
| Stablecoin supply | $16.16B |
| DEX volume (24h) | $1.69B (-46.88% 1d) |
| App fees (24h, all protocols) | $13.52M |
| Chain fees (24h) | $708.83K |
| Jito MEV tips (24h) | $103.97K |
| **REV - Real Economic Value (24h)** | **$812.80K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.26B | -0.55% |
| USDT | $2.54B | -7.95% |
| USDGO | $1.38B | +2.02% |
| USD1 | $1.31B | +3.93% |
| BUIDL | $992.60M | +1.50% |
| PYUSD | $707.00M | -5.99% |
| USDG | $603.00M | +3.59% |
| USDe | $532.99M | -0.56% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $377.15M |
| Raydium AMM | $284.98M |
| BisonFi | $162.68M |
| Meteora DLMM | $161.06M |
| Orca DEX | $94.63M |
| HumidiFi | $85.03M |
| Tessera V | $81.22M |
| Manifest Trade | $73.74M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.34M |
| pump.fun | $1.40M |
| Axiom | $1.34M |
| fomo Wallet | $1.18M |
| Raydium AMM | $1.18M |
| Meteora DLMM | $1.01M |
| StonkFun | $783.82K |
| Collector Crypt | $381.48K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 329 |
| Persistently-active cohort (capture-recapture est.) | 4.1K |
| Unique payers across sampled blocks | 2.0K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $78.28M |
| xStocks holder positions | 529.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.93B |

## Program activity and chain health

Chain tip lag: **+11.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 40,905 | 19.60% | 1.3 s |
| Pump.fun | 10,431 | 78.50% | 5.4 s |
| Orca Whirlpools | 2,795 | 42.20% | 21.1 s |
| Jupiter v6 | 1,680 | 39.80% | 35 s |
| Raydium AMM v4 | 1,640 | 40.60% | 36.5 s |

Median failure rate across the sampled programs: **40.60%** (range 19.60% to 78.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.18K SOL**.

## Exchange and large-holder balances

11.73M SOL ($1.17B) across 8 publicly-attributed accounts. Net **16K SOL (0.14%) moved off exchanges** over the last 22.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $916.27M | 0.3/h | 1 |
| Binance (2) | 1.88M | $187.64M | 975.6/h | 0 |
| Gate.io | 309.89K | $30.90M | 144.9/h | 0 |
| Bybit | 232.18K | $23.15M | 36.5/h | 0 |
| Bitget | 46.21K | $4.61M | 222.4/h | 0 |
| Kraken | 26.25K | $2.62M | 165.3/h | 0 |
| Coinbase (2) | 23.39K | $2.33M | 170.3/h | 0 |
| Coinbase | 23.35K | $2.33M | 192/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 816 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.225 | 775 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.194 | 782 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.159 | 741 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.157 | 741 | 0.0000 |
| Total TPS moves with Slot time | +0.155 | 782 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.137 | 763 | 0.0002 |
| Total TPS moves with Program failure rate | +0.136 | 763 | 0.0002 |
| Slot time moves with AMM write-lock congestion | +0.116 | 741 | 0.0015 |
| Share paying base fee only moves with Activity index | +0.115 | 805 | 0.0011 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 542.73K USD | DeFiLlama: 708.83K USD | -26.54% | *indicative*: 0.77x, within the order-of-magnitude band |
| SOL price | coingecko: 99.72 USD | Jupiter (on-chain DEX): 99.71 USD | +0.01% | agree |
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
