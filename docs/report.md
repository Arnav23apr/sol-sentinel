# Solana Ecosystem Report

*Generated 2026-09-09 18:07 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 11.4 robust standard deviations above its 7-day baseline: a 55.0% move to 16,561,493.00 USD from a typical 10,682,294.00.
- 🟠 **Activity index (fee payers per block)** (warning): Activity index (fee payers per block) is 5.0 robust standard deviations above its 7-day baseline: a 65.9% move to 394.00 from a typical 237.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.3K |
| TPS (non-vote) | 2.1K |
| Slot time | 315.8 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1031 (65.55% complete, ~13.1h remaining) |
| Lifetime transactions | 546.8B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,319 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 35,168 / 230,000 lamports |
| Paying no priority fee | 30.60% of 5,714 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 12.0M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 679 |
| Delinquent validators | 9 |
| Delinquent stake | 0.01% |
| Total active stake | 438.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.34% / 24.25% / 35.53% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.00% |

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
| SOL price | $103.59 (-0.29% 24h) |
| Market cap | $60.72B (rank #7) |
| 24h volume | $2.92B |
| ATH | $293.31 (-64.68% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.95B |
| Stablecoin supply | $16.18B |
| DEX volume (24h) | $2.71B (-0.36% 1d) |
| App fees (24h, all protocols) | $16.56M |
| Chain fees (24h) | $772.73K |
| Jito MEV tips (24h) | $148.87K |
| **REV - Real Economic Value (24h)** | **$921.60K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.02B | +5.90% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.37B | +10.24% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $987.67M | +11.35% |
| PYUSD | $743.81M | +0.76% |
| USDG | $604.95M | -1.38% |
| USDe | $535.60M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $737.12M |
| Raydium AMM | $345.95M |
| BisonFi | $249.32M |
| Meteora DLMM | $237.76M |
| Tessera V | $156.31M |
| Orca DEX | $155.18M |
| HumidiFi | $153.40M |
| Manifest Trade | $145.21M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| fomo Wallet | $1.78M |
| StonkFun | $1.45M |
| Axiom | $1.44M |
| Raydium AMM | $1.34M |
| pump.fun | $1.27M |
| Meteora DLMM | $1.08M |
| Pyth Pro | $722.90K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 394 |
| Persistently-active cohort (capture-recapture est.) | 4.9K |
| Unique payers across sampled blocks | 2.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $438.64M |
| xStocks 24h DEX volume | $95.10M |
| xStocks holder positions | 398.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.35B |

Top tokenized equities: TSLAX ($68.63M), CRCLX ($68.20M), MSTRX ($58.83M), SPYX ($45.48M), GOOGLX ($29.41M)

## Program activity and chain health

Chain tip lag: **+11.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 62,635 | 33.10% | 0.9 s |
| Pump.fun | 21,422 | 82.80% | 2.5 s |
| Jupiter v6 | 15,437 | 76.40% | 3.8 s |
| Orca Whirlpools | 9,800 | 55.40% | 6 s |
| Raydium AMM v4 | 7,962 | 40.40% | 6.9 s |

Median failure rate across the sampled programs: **55.40%** (range 33.10% to 82.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **159.35 SOL**.

## Exchange and large-holder balances

11.66M SOL ($1.21B) across 8 publicly-attributed accounts. Net **69K SOL (0.58%) moved off exchanges** over the last 21.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $951.83M | 0.4/h | 1 |
| Binance (2) | 1.81M | $187.34M | 1.5K/h | 0 |
| Gate.io | 293.19K | $30.37M | 164.8/h | 0 |
| Bybit | 211.87K | $21.95M | 25.6/h | 0 |
| Coinbase (2) | 53.31K | $5.52M | 439/h | 0 |
| Bitget | 41.76K | $4.33M | 246.7/h | 0 |
| Coinbase | 31.53K | $3.27M | 370/h | 0 |
| Kraken | 30.37K | $3.15M | 246.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 789 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.304 | 748 | 0.0000 |
| DEX volume moves with App fees | +0.234 | 748 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 755 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 755 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.143 | 714 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.142 | 714 | 0.0001 |
| Total TPS moves with Program failure rate | +0.120 | 736 | 0.0011 |
| Non-vote TPS moves with Program failure rate | +0.119 | 736 | 0.0012 |
| Non-vote TPS moves with Activity index | +0.116 | 754 | 0.0015 |
| Slot time moves with AMM write-lock congestion | +0.111 | 714 | 0.0031 |
| Total TPS moves with Activity index | +0.107 | 754 | 0.0032 |
| Share paying base fee only moves with Activity index | +0.101 | 778 | 0.0046 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 934.03K USD | DeFiLlama: 772.73K USD | +18.90% | *indicative*: 1.21x, within the order-of-magnitude band |
| SOL price | coingecko: 103.59 USD | Jupiter (on-chain DEX): 103.45 USD | +0.14% | agree |
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

- **[Solana treasury firm SkyAI faces board challenge from would-be acquirer Forward Industries, shareholder group](https://www.theblock.co/news/business/2026-09-09-solana-treasury-firm-skyai-board-challenge-would-be-acquirer-forward-industries-shareholder-group-414061)** - The Block, 2026-09-09
- **[DeFi Development closes Strategy-style $11 million CHAD offering to grow Solana treasury](https://www.theblock.co/news/markets/2026-09-08-defi-development-closes-strategy-style-11-million-chad-offering-grow-solana-treasury-413892)** - The Block, 2026-09-08
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
