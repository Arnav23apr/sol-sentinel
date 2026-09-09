# Solana Ecosystem Report

*Generated 2026-09-09 21:01 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 11.4 robust standard deviations above its 7-day baseline: a 55.0% move to 16,561,493.00 USD from a typical 10,682,294.00.
- 🟠 **Delinquent stake** (warning): Delinquent stake is 6.0 robust standard deviations above its 7-day baseline: a 441.9% move to 0.17 % from a typical 0.03.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 2.1K |
| Slot time | 318.3 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1031 (73.16% complete, ~10.3h remaining) |
| Lifetime transactions | 546.8B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,500 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 44,761 / 1,005,000 lamports |
| Paying no priority fee | 23.60% of 3,575 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 82.00% of slots needed a priority fee (max 54.3M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 674 |
| Delinquent validators | 14 |
| Delinquent stake | 0.17% |
| Total active stake | 437.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.36% / 24.29% / 35.59% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 24.04% |

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
| SOL price | $102.52 (-0.56% 24h) |
| Market cap | $60.09B (rank #7) |
| 24h volume | $2.97B |
| ATH | $293.31 (-65.05% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.94B |
| Stablecoin supply | $16.21B |
| DEX volume (24h) | $2.71B (-0.36% 1d) |
| App fees (24h, all protocols) | $16.56M |
| Chain fees (24h) | $772.73K |
| Jito MEV tips (24h) | $148.32K |
| **REV - Real Economic Value (24h)** | **$921.05K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.06B | +6.51% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.37B | +10.24% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $987.67M | +11.35% |
| PYUSD | $743.79M | +0.78% |
| USDG | $604.30M | -1.47% |
| USDe | $535.65M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $737.12M |
| Raydium AMM | $401.83M |
| BisonFi | $249.32M |
| Meteora DLMM | $237.76M |
| Tessera V | $156.31M |
| Orca DEX | $155.18M |
| HumidiFi | $153.40M |
| Manifest Trade | $142.50M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| fomo Wallet | $1.78M |
| Raydium AMM | $1.47M |
| StonkFun | $1.45M |
| Axiom | $1.44M |
| pump.fun | $1.27M |
| Meteora DLMM | $1.08M |
| Pyth Pro | $722.90K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 262 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.4K (7 blocks over 24h) |
| xStocks tokenized-equity AUM | $439.98M |
| xStocks 24h DEX volume | $177.14M |
| xStocks holder positions | 428.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: TSLAX ($68.62M), CRCLX ($67.85M), MSTRX ($58.96M), SPYX ($46.24M), GOOGLX ($29.58M)

## Program activity and chain health

Chain tip lag: **+12.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 88,690 (approx.) | 35.80% | 0.6 s |
| Jupiter v6 | 7,246 | 52.80% | 8 s |
| Raydium AMM v4 | 6,598 | 39.10% | 8.9 s |
| Orca Whirlpools | 5,578 | 46.60% | 10.2 s |
| Pump.fun | 4,683 | 35.20% | 12.1 s |

Median failure rate across the sampled programs: **39.10%** (range 35.20% to 52.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **159.35 SOL**.

## Exchange and large-holder balances

11.58M SOL ($1.19B) across 8 publicly-attributed accounts. Net **92K SOL (0.79%) moved off exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $942.00M | 0.4/h | 1 |
| Binance (2) | 1.74M | $178.61M | 1.3K/h | 0 |
| Gate.io | 285.36K | $29.26M | 214/h | 0 |
| Bybit | 211.87K | $21.72M | 40.3/h | 0 |
| Coinbase (2) | 52.27K | $5.36M | 520.2/h | 0 |
| Bitget | 41.42K | $4.25M | 232.7/h | 0 |
| Kraken | 31.18K | $3.20M | 251.6/h | 0 |
| Coinbase | 23.57K | $2.42M | 454.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 790 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.301 | 749 | 0.0000 |
| DEX volume moves with App fees | +0.234 | 749 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.191 | 756 | 0.0000 |
| Total TPS moves with Slot time | +0.153 | 756 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.142 | 715 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.141 | 715 | 0.0001 |
| Total TPS moves with Program failure rate | +0.121 | 737 | 0.0010 |
| Non-vote TPS moves with Program failure rate | +0.120 | 737 | 0.0011 |
| Non-vote TPS moves with Activity index | +0.116 | 755 | 0.0014 |
| Slot time moves with AMM write-lock congestion | +0.113 | 715 | 0.0026 |
| Total TPS moves with Activity index | +0.108 | 755 | 0.0029 |
| Share paying base fee only moves with Activity index | +0.105 | 779 | 0.0034 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 553.84K USD | DeFiLlama: 772.73K USD | -33.00% | *indicative*: 0.72x, within the order-of-magnitude band |
| SOL price | coingecko: 102.52 USD | Jupiter (on-chain DEX): 102.40 USD | +0.12% | agree |
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
