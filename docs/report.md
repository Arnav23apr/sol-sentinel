# Solana Ecosystem Report

*Generated 2026-09-12 13:39 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 26.2 robust standard deviations above its 7-day baseline: a 1852.4% move to 0.41 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.3K |
| Slot time | 316.6 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1033 (43.28% complete, ~21.6h remaining) |
| Lifetime transactions | 547.7B |
| Circulating supply | 586.6M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,410 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 34,400 / 658,378 lamports |
| Paying no priority fee | 28.70% of 3,304 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 32.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 13 |
| Delinquent stake | 0.41% |
| Total active stake | 435.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.51% / 24.50% / 35.87% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.19% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.6M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.76% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.88% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.61% | 5% |
| 5 | `8Gbw…F8iD` | 9.7M | 2.22% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.69% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.60% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $101.87 (+0.81% 24h) |
| Market cap | $59.76B (rank #7) |
| 24h volume | $3.65B |
| ATH | $293.31 (-65.27% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.90B |
| Stablecoin supply | $16.19B |
| DEX volume (24h) | $3.18B (+8.96% 1d) |
| App fees (24h, all protocols) | $17.78M |
| Chain fees (24h) | $835.74K |
| Jito MEV tips (24h) | $132.60K |
| **REV - Real Economic Value (24h)** | **$968.35K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.24B | -0.33% |
| USDT | $2.59B | -6.15% |
| USDGO | $1.38B | +2.02% |
| USD1 | $1.30B | +4.41% |
| BUIDL | $992.60M | +1.50% |
| PYUSD | $706.71M | -1.79% |
| USDG | $596.12M | +2.90% |
| USDe | $535.63M | +0.47% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $471.70M |
| Raydium AMM | $399.36M |
| Meteora DLMM | $363.04M |
| PumpSwap | $294.17M |
| Orca DEX | $213.61M |
| Tessera V | $202.03M |
| Manifest Trade | $167.01M |
| HumidiFi | $155.95M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.85M |
| StonkFun | $1.84M |
| Axiom | $1.60M |
| fomo Wallet | $1.56M |
| Raydium AMM | $1.52M |
| Meteora DLMM | $1.22M |
| pump.fun | $950.51K |
| Orca DEX | $535.67K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 242 |
| Persistently-active cohort (capture-recapture est.) | 2.9K |
| Unique payers across sampled blocks | 1.5K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $103.73M |
| xStocks holder positions | 521.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.92B |

## Program activity and chain health

Chain tip lag: **+12.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 39,040 | 30.20% | 1.3 s |
| Jupiter v6 | 11,229 | 92.50% | 5.1 s |
| Orca Whirlpools | 5,662 | 81.60% | 10.1 s |
| Pump.fun | 1,889 | 30.20% | 31.7 s |
| Raydium AMM v4 | 1,657 | 48.70% | 36.1 s |

Median failure rate across the sampled programs: **48.70%** (range 30.20% to 92.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **571.34 SOL**.

## Exchange and large-holder balances

11.75M SOL ($1.20B) across 8 publicly-attributed accounts. Net **25K SOL (0.21%) moved onto exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $936.03M | 0.3/h | 1 |
| Binance (2) | 1.91M | $194.50M | 900/h | 0 |
| Gate.io | 302.33K | $30.80M | 122.9/h | 0 |
| Bybit | 232.18K | $23.65M | 25.2/h | 0 |
| Bitget | 33.93K | $3.46M | 279.3/h | 1 |
| Kraken | 29.16K | $2.97M | 220.6/h | 0 |
| Coinbase (2) | 26.33K | $2.68M | 281.9/h | 0 |
| Coinbase | 25.74K | $2.62M | 376.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 809 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.215 | 768 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.190 | 775 | 0.0000 |
| Total TPS moves with Slot time | +0.151 | 775 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.150 | 734 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.148 | 734 | 0.0001 |
| Total TPS moves with Program failure rate | +0.133 | 756 | 0.0003 |
| Non-vote TPS moves with Program failure rate | +0.133 | 756 | 0.0003 |
| Share paying base fee only moves with Activity index | +0.110 | 798 | 0.0019 |
| Slot time moves with AMM write-lock congestion | +0.108 | 734 | 0.0034 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 422.88K USD | DeFiLlama: 835.74K USD | -65.60% | *indicative*: 0.51x, within the order-of-magnitude band |
| SOL price | coingecko: 101.87 USD | Jupiter (on-chain DEX): 101.87 USD | 0.00% | agree |
| Circulating supply | getSupply (RPC): 586.63M SOL | CoinGecko: 586.63M SOL | -0.00% | agree |

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
