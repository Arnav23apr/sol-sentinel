# Solana Ecosystem Report

*Generated 2026-09-10 01:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 8.7 robust standard deviations above its 7-day baseline: a 49.5% move to 16,140,710.00 USD from a typical 10,796,465.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.0K |
| Slot time | 315.8 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1031 (84.14% complete, ~6.0h remaining) |
| Lifetime transactions | 546.9B |
| Circulating supply | 586.2M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,570 lamports (about $0.00057) |
| Transaction fee p90 / p99 | 54,417 / 1,005,000 lamports |
| Paying no priority fee | 21.10% of 4,832 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 18.4M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 13 |
| Delinquent stake | 0.05% |
| Total active stake | 438.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.34% / 24.26% / 35.55% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.01% |

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
| 9 | `CvSb…wycB` | 6.9M | 1.56% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.54 (-2.31% 24h) |
| Market cap | $59.61B (rank #7) |
| 24h volume | $3.22B |
| ATH | $293.31 (-65.38% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.79B |
| Stablecoin supply | $16.27B |
| DEX volume (24h) | $2.56B (-5.73% 1d) |
| App fees (24h, all protocols) | $16.14M |
| Chain fees (24h) | $772.73K |
| Jito MEV tips (24h) | $184.16K |
| **REV - Real Economic Value (24h)** | **$956.89K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.10B | +7.13% |
| USDT | $2.76B | -2.45% |
| USDGO | $1.37B | +10.24% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $992.17M | +11.86% |
| PYUSD | $756.66M | +2.52% |
| USDG | $603.10M | -1.68% |
| USDe | $535.57M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $434.28M |
| PumpSwap | $340.96M |
| Meteora DLMM | $322.25M |
| BisonFi | $249.32M |
| Orca DEX | $169.53M |
| Tessera V | $156.31M |
| HumidiFi | $153.40M |
| Manifest Trade | $152.49M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| fomo Wallet | $1.78M |
| Raydium AMM | $1.61M |
| StonkFun | $1.45M |
| Axiom | $1.44M |
| pump.fun | $1.27M |
| Meteora DLMM | $1.08M |
| Orca DEX | $483.99K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 275 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $436.89M |
| xStocks 24h DEX volume | $184.82M |
| xStocks holder positions | 437.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.35B |

Top tokenized equities: TSLAX ($67.65M), CRCLX ($67.11M), MSTRX ($58.63M), SPYX ($46.23M), GOOGLX ($29.61M)

## Program activity and chain health

Chain tip lag: **+11.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 62,191 | 31.00% | 0.9 s |
| Pump.fun | 9,574 | 76.10% | 5.7 s |
| Jupiter v6 | 7,516 | 72.40% | 7.9 s |
| Orca Whirlpools | 3,434 | 55.10% | 17.4 s |
| Raydium AMM v4 | 3,087 | 28.90% | 19.3 s |

Median failure rate across the sampled programs: **55.10%** (range 28.90% to 76.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **159.35 SOL**.

## Exchange and large-holder balances

11.66M SOL ($1.18B) across 8 publicly-attributed accounts. Net **38K SOL (0.33%) moved onto exchanges** over the last 19.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $933.00M | 0.4/h | 1 |
| Binance (2) | 1.82M | $184.85M | 2.4K/h | 0 |
| Gate.io | 276.79K | $28.10M | 193.5/h | 0 |
| Bybit | 211.87K | $21.51M | 45.1/h | 0 |
| Coinbase (2) | 67.49K | $6.85M | 446.1/h | 0 |
| Bitget | 40.24K | $4.09M | 150/h | 0 |
| Kraken | 30.46K | $3.09M | 134.3/h | 0 |
| Coinbase | 26.36K | $2.68M | 398.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 792 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.306 | 751 | 0.0000 |
| DEX volume moves with App fees | +0.239 | 751 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 758 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 758 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.143 | 717 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.142 | 717 | 0.0001 |
| Total TPS moves with Program failure rate | +0.121 | 739 | 0.0010 |
| Non-vote TPS moves with Program failure rate | +0.120 | 739 | 0.0011 |
| Slot time moves with AMM write-lock congestion | +0.115 | 717 | 0.0021 |
| Non-vote TPS moves with Activity index | +0.114 | 757 | 0.0017 |
| Total TPS moves with Activity index | +0.107 | 757 | 0.0032 |
| Share paying base fee only moves with Activity index | +0.102 | 781 | 0.0044 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 1.17M USD | DeFiLlama: 772.73K USD | +40.94% | *indicative*: 1.51x, within the order-of-magnitude band |
| SOL price | coingecko: 101.54 USD | Jupiter (on-chain DEX): 101.20 USD | +0.34% | agree |
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

- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10
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
