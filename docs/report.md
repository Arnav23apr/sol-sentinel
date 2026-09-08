# Solana Ecosystem Report

*Generated 2026-09-08 17:43 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 9.6 robust standard deviations above its 7-day baseline: a 46.5% move to 15,653,179.00 USD from a typical 10,682,294.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.9K |
| TPS (non-vote) | 2.8K |
| Slot time | 315.8 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1031 (1.38% complete, ~37.4h remaining) |
| Lifetime transactions | 546.4B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,324 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 33,907 / 410,000 lamports |
| Paying no priority fee | 27.30% of 4,060 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 22.70% of slots needed a priority fee (max 71.4M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 11 |
| Delinquent stake | 0.01% |
| Total active stake | 438.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.34% / 24.25% / 35.53% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.99% |

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
| SOL price | $103.83 (-0.23% 24h) |
| Market cap | $60.87B (rank #7) |
| 24h volume | $2.94B |
| ATH | $293.31 (-64.60% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.91B |
| Stablecoin supply | $16.18B |
| DEX volume (24h) | $2.72B (-6.33% 1d) |
| App fees (24h, all protocols) | $15.65M |
| Chain fees (24h) | $750.65K |
| Jito MEV tips (24h) | $124.05K |
| **REV - Real Economic Value (24h)** | **$874.71K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.13B | +5.98% |
| USDT | $2.76B | -2.45% |
| USDGO | $1.37B | +9.73% |
| USD1 | $1.26B | +4.82% |
| BUIDL | $978.28M | +10.30% |
| PYUSD | $733.31M | -5.30% |
| USDG | $578.75M | -5.38% |
| USDe | $536.80M | -0.10% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $873.43M |
| Raydium AMM | $302.38M |
| Orca DEX | $218.84M |
| BisonFi | $204.07M |
| Meteora DLMM | $195.35M |
| Tessera V | $149.50M |
| Manifest Trade | $126.38M |
| pump.fun | $100.28M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.76M |
| fomo Wallet | $1.66M |
| Raydium AMM | $1.46M |
| Axiom | $1.27M |
| pump.fun | $1.23M |
| Meteora DLMM | $876.51K |
| Orca DEX | $435.30K |
| Sanctum Validator LSTs | $378.86K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 272 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $444.56M |
| xStocks 24h DEX volume | $86.65M |
| xStocks holder positions | 378.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.34B |

Top tokenized equities: CRCLX ($71.36M), TSLAX ($68.42M), MSTRX ($60.41M), SPYX ($45.22M), GOOGLX ($29.64M)

## Program activity and chain health

Chain tip lag: **+12.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 97,467 (approx.) | 22.30% | 0.3 s |
| Raydium AMM v4 | 22,063 | 31.80% | 2.5 s |
| Pump.fun | 11,768 | 78.50% | 5.1 s |
| Orca Whirlpools | 8,806 | 45.90% | 6.3 s |
| Jupiter v6 | 6,875 | 72.60% | 8.5 s |

Median failure rate across the sampled programs: **45.90%** (range 22.30% to 78.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **873.57 SOL**.

## Exchange and large-holder balances

11.62M SOL ($1.21B) across 8 publicly-attributed accounts. Net **13K SOL (0.11%) moved onto exchanges** over the last 22.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $954.04M | 0.4/h | 1 |
| Binance (2) | 1.75M | $181.43M | 1.4K/h | 0 |
| Gate.io | 294.47K | $30.57M | 174.5/h | 0 |
| Bybit | 210.99K | $21.91M | 44.8/h | 0 |
| Bitget | 77.18K | $8.01M | 298.5/h | 0 |
| Coinbase (2) | 34.26K | $3.56M | 436.4/h | 0 |
| Kraken | 32.08K | $3.33M | 287.8/h | 0 |
| Coinbase | 30.53K | $3.17M | 548.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 782 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.296 | 741 | 0.0000 |
| DEX volume moves with App fees | +0.246 | 741 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 748 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 748 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.144 | 707 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.143 | 707 | 0.0001 |
| Non-vote TPS moves with Activity index | +0.124 | 747 | 0.0007 |
| Total TPS moves with Program failure rate | +0.118 | 729 | 0.0015 |
| Non-vote TPS moves with Program failure rate | +0.117 | 729 | 0.0016 |
| Total TPS moves with Activity index | +0.115 | 747 | 0.0016 |
| Slot time moves with AMM write-lock congestion | +0.115 | 707 | 0.0022 |
| AMM write-lock congestion moves with Program failure rate | +0.105 | 707 | 0.0050 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 421.81K USD | DeFiLlama: 750.65K USD | -56.09% | *indicative*: 0.56x, within the order-of-magnitude band |
| SOL price | coingecko: 103.83 USD | Jupiter (on-chain DEX): 103.81 USD | +0.02% | agree |
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
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02

**Recently merged SIMDs:**

- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08
- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31

**Latest Agave release:** [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) (2026-09-04)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[‘The chain is now earnings’: Bernstein sees 31% upside for Robinhood as fees top Solana, BNB Chain](https://www.theblock.co/news/markets/2026-09-08-bernstein-sees-upside-robinhood-413729)** - The Block, 2026-09-08
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
