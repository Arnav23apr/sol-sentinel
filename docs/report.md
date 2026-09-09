# Solana Ecosystem Report

*Generated 2026-09-09 14:40 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 14.6 robust standard deviations above its 7-day baseline: a 1112.5% move to 0.39 % from a typical 0.03.
- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 9.4 robust standard deviations above its 7-day baseline: a 53.4% move to 16,561,493.00 USD from a typical 10,796,465.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.4K |
| TPS (non-vote) | 2.2K |
| Slot time | 315.8 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1031 (56.49% complete, ~16.5h remaining) |
| Lifetime transactions | 546.7B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,612 lamports (about $0.00058) |
| Transaction fee p90 / p99 | 35,030 / 305,000 lamports |
| Paying no priority fee | 20.20% of 4,771 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 28.00% of slots needed a priority fee (max 4.1M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 12 |
| Delinquent stake | 0.39% |
| Total active stake | 437.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.34% / 35.67% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.09% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.99% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.74% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.87% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.61% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.19% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.13% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.3M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.57% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $103.97 (+0.94% 24h) |
| Market cap | $60.95B (rank #7) |
| 24h volume | $2.86B |
| ATH | $293.31 (-64.55% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.98B |
| Stablecoin supply | $16.27B |
| DEX volume (24h) | $2.71B (-0.36% 1d) |
| App fees (24h, all protocols) | $16.56M |
| Chain fees (24h) | $772.73K |
| Jito MEV tips (24h) | $147.24K |
| **REV - Real Economic Value (24h)** | **$919.97K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.11B | +7.26% |
| USDT | $2.76B | -2.45% |
| USDGO | $1.37B | +10.28% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $987.58M | +11.34% |
| PYUSD | $752.29M | +1.93% |
| USDG | $605.24M | -1.32% |
| USDe | $534.08M | -0.58% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $737.12M |
| Raydium AMM | $309.63M |
| BisonFi | $249.32M |
| Meteora DLMM | $237.76M |
| Tessera V | $156.31M |
| HumidiFi | $153.40M |
| Manifest Trade | $144.19M |
| pump.fun | $102.04M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| fomo Wallet | $1.78M |
| StonkFun | $1.45M |
| Axiom | $1.44M |
| Raydium AMM | $1.28M |
| pump.fun | $1.27M |
| Meteora DLMM | $1.08M |
| Pyth Pro | $722.90K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 267 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $441.60M |
| xStocks 24h DEX volume | $89.17M |
| xStocks holder positions | 396.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.35B |

Top tokenized equities: CRCLX ($70.64M), TSLAX ($67.85M), MSTRX ($60.86M), SPYX ($45.57M), GOOGLX ($29.03M)

## Program activity and chain health

Chain tip lag: **+12.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 76,282 (approx.) | 21.70% | 0.6 s |
| Pump.fun | 13,665 | 72.50% | 4.1 s |
| Orca Whirlpools | 8,230 | 42.90% | 6.9 s |
| Jupiter v6 | 7,327 | 66.40% | 7.3 s |
| Raydium AMM v4 | 6,012 | 23.10% | 9.8 s |

Median failure rate across the sampled programs: **42.90%** (range 21.70% to 72.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **568.43 SOL**.

## Exchange and large-holder balances

11.63M SOL ($1.21B) across 8 publicly-attributed accounts. Net **14K SOL (0.12%) moved onto exchanges** over the last 21.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $955.32M | 0.4/h | 1 |
| Binance (2) | 1.77M | $184.00M | 1.4K/h | 1 |
| Gate.io | 300.78K | $31.27M | 246.1/h | 0 |
| Bybit | 211.87K | $22.03M | 40.1/h | 0 |
| Coinbase (2) | 55.17K | $5.74M | 373.8/h | 0 |
| Bitget | 42.39K | $4.41M | 250/h | 0 |
| Coinbase | 33.47K | $3.48M | 468.1/h | 0 |
| Kraken | 27.49K | $2.86M | 254.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 11 of 117 tested pairs survive, over 788 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.302 | 747 | 0.0000 |
| DEX volume moves with App fees | +0.234 | 747 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 754 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 754 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.142 | 713 | 0.0001 |
| Non-vote TPS moves with AMM write-lock congestion | +0.142 | 713 | 0.0001 |
| Total TPS moves with Program failure rate | +0.121 | 735 | 0.0010 |
| Non-vote TPS moves with Program failure rate | +0.121 | 735 | 0.0011 |
| Non-vote TPS moves with Activity index | +0.117 | 753 | 0.0013 |
| Slot time moves with AMM write-lock congestion | +0.111 | 713 | 0.0030 |
| Total TPS moves with Activity index | +0.109 | 753 | 0.0028 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 407.05K USD | DeFiLlama: 772.73K USD | -61.99% | *indicative*: 0.53x, within the order-of-magnitude band |
| SOL price | coingecko: 103.97 USD | Jupiter (on-chain DEX): 103.83 USD | +0.13% | agree |
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
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
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

- **[DeFi Development closes Strategy-style $11 million CHAD offering to grow Solana treasury](https://www.theblock.co/news/markets/2026-09-08-defi-development-closes-strategy-style-11-million-chad-offering-grow-solana-treasury-413892)** - The Block, 2026-09-08
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
