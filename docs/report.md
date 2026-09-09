# Solana Ecosystem Report

*Generated 2026-09-09 23:22 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 11.4 robust standard deviations above its 7-day baseline: a 55.0% move to 16,561,493.00 USD from a typical 10,682,294.00.
- 🟠 **Delinquent stake** (warning): Delinquent stake is 5.4 robust standard deviations above its 7-day baseline: a 403.2% move to 0.16 % from a typical 0.03.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 1.8K |
| Slot time | 316.6 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1031 (79.31% complete, ~7.9h remaining) |
| Lifetime transactions | 546.9B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,974 lamports (about $0.00061) |
| Transaction fee p90 / p99 | 50,001 / 713,030 lamports |
| Paying no priority fee | 19.10% of 5,796 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 23.30% of slots needed a priority fee (max 3.6M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 13 |
| Delinquent stake | 0.16% |
| Total active stake | 438.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.36% / 24.29% / 35.58% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.03% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.98% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.86% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.60% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.18% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.3M | 1.67% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.57% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.48 (-1.79% 24h) |
| Market cap | $59.49B (rank #7) |
| 24h volume | $3.12B |
| ATH | $293.31 (-65.40% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.92B |
| Stablecoin supply | $16.26B |
| DEX volume (24h) | $2.71B (-0.36% 1d) |
| App fees (24h, all protocols) | $16.56M |
| Chain fees (24h) | $772.73K |
| Jito MEV tips (24h) | $145.07K |
| **REV - Real Economic Value (24h)** | **$917.80K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.12B | +7.39% |
| USDT | $2.76B | -2.45% |
| USDGO | $1.37B | +10.24% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $992.17M | +11.86% |
| PYUSD | $756.64M | +2.52% |
| USDG | $602.89M | -1.68% |
| USDe | $535.52M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $737.12M |
| Raydium AMM | $433.73M |
| BisonFi | $249.32M |
| Meteora DLMM | $237.76M |
| Orca DEX | $166.62M |
| Tessera V | $156.31M |
| HumidiFi | $153.40M |
| Manifest Trade | $148.56M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| fomo Wallet | $1.78M |
| Raydium AMM | $1.63M |
| StonkFun | $1.45M |
| Axiom | $1.44M |
| pump.fun | $1.27M |
| Meteora DLMM | $1.08M |
| Orca DEX | $468.10K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 295 |
| Persistently-active cohort (capture-recapture est.) | 2.8K |
| Unique payers across sampled blocks | 1.7K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $437.71M |
| xStocks 24h DEX volume | $182.43M |
| xStocks holder positions | 433.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.35B |

Top tokenized equities: TSLAX ($67.80M), CRCLX ($67.27M), MSTRX ($58.86M), SPYX ($46.22M), GOOGLX ($29.62M)

## Program activity and chain health

Chain tip lag: **+11.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 77,606 (approx.) | 43.50% | 0.6 s |
| Pump.fun | 4,989 | 41.20% | 11.7 s |
| Jupiter v6 | 4,902 | 57.70% | 12 s |
| Raydium AMM v4 | 4,217 | 31.40% | 13.9 s |
| Orca Whirlpools | 3,097 | 54.60% | 19.3 s |

Median failure rate across the sampled programs: **43.50%** (range 31.40% to 57.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **159.35 SOL**.

## Exchange and large-holder balances

11.71M SOL ($1.19B) across 8 publicly-attributed accounts. Net **49K SOL (0.42%) moved onto exchanges** over the last 22.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $932.44M | 0.4/h | 1 |
| Binance (2) | 1.82M | $185.00M | 1.7K/h | 1 |
| Gate.io | 277.34K | $28.14M | 272.9/h | 0 |
| Bybit | 211.87K | $21.50M | 74.6/h | 0 |
| Coinbase (2) | 108.35K | $11.00M | 503.5/h | 0 |
| Bitget | 41.94K | $4.26M | 161.8/h | 0 |
| Kraken | 31.16K | $3.16M | 317.2/h | 0 |
| Coinbase | 24.99K | $2.54M | 434.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 791 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.304 | 750 | 0.0000 |
| DEX volume moves with App fees | +0.234 | 750 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 757 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 757 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.144 | 716 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.142 | 716 | 0.0001 |
| Total TPS moves with Program failure rate | +0.121 | 738 | 0.0010 |
| Non-vote TPS moves with Program failure rate | +0.119 | 738 | 0.0012 |
| Non-vote TPS moves with Activity index | +0.115 | 756 | 0.0016 |
| Slot time moves with AMM write-lock congestion | +0.114 | 716 | 0.0022 |
| Total TPS moves with Activity index | +0.107 | 756 | 0.0032 |
| Share paying base fee only moves with Activity index | +0.103 | 780 | 0.0042 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 777.81K USD | DeFiLlama: 772.73K USD | +0.66% | *indicative*: 1.01x, within the order-of-magnitude band |
| SOL price | coingecko: 101.48 USD | Jupiter (on-chain DEX): 101.43 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 586.25M SOL | CoinGecko: 586.25M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-09
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02

**Recently merged SIMDs:**

- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-09
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08
- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31

**Latest Agave release:** [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) (2026-09-04)

**Latest Firedancer release:** [v26.09.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.0) (2026-09-08)

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
