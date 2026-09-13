# Solana Ecosystem Report

*Generated 2026-09-13 01:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 7.4 robust standard deviations above its 7-day baseline: a 831.1% move to 0.42 % from a typical 0.04.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.6K |
| TPS (non-vote) | 1.4K |
| Slot time | 317.5 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1033 (73.68% complete, ~10.0h remaining) |
| Lifetime transactions | 547.9B |
| Circulating supply | 586.6M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,514 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 31,334 / 524,514 lamports |
| Paying no priority fee | 22.40% of 3,754 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 51.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 13 |
| Delinquent stake | 0.42% |
| Total active stake | 435.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.51% / 24.50% / 35.87% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.20% |

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
| SOL price | $101.86 (-0.26% 24h) |
| Market cap | $59.76B (rank #7) |
| 24h volume | $1.83B |
| ATH | $293.31 (-65.27% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.90B |
| Stablecoin supply | $16.22B |
| DEX volume (24h) | $2.64B (-17.16% 1d) |
| App fees (24h, all protocols) | $17.88M |
| Chain fees (24h) | $835.74K |
| Jito MEV tips (24h) | $106.07K |
| **REV - Real Economic Value (24h)** | **$941.82K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.31B | +0.06% |
| USDT | $2.55B | -7.95% |
| USDGO | $1.38B | +2.02% |
| USD1 | $1.31B | +3.93% |
| BUIDL | $992.60M | +1.50% |
| PYUSD | $705.88M | -6.16% |
| USDG | $603.56M | +3.66% |
| USDe | $535.34M | -0.16% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $471.70M |
| Meteora DLMM | $363.04M |
| Raydium AMM | $326.15M |
| PumpSwap | $294.17M |
| Tessera V | $202.03M |
| HumidiFi | $155.95M |
| GoonFi | $111.18M |
| Scorch | $108.66M |

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
| LaunchLab | $494.31K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 227 |
| Persistently-active cohort (capture-recapture est.) | 2.5K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $78.95M |
| xStocks holder positions | 527.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.93B |

## Program activity and chain health

Chain tip lag: **+11.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 35,641 | 26.50% | 1.6 s |
| Pump.fun | 7,843 | 69.50% | 7.6 s |
| Jupiter v6 | 4,252 | 66.10% | 13.3 s |
| Raydium AMM v4 | 3,203 | 41.40% | 18.4 s |
| Orca Whirlpools | 2,986 | 54.40% | 19.4 s |

Median failure rate across the sampled programs: **54.40%** (range 26.50% to 69.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **571.34 SOL**.

## Exchange and large-holder balances

11.72M SOL ($1.19B) across 8 publicly-attributed accounts. Net **13K SOL (0.11%) moved onto exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $935.94M | 0.3/h | 1 |
| Binance (2) | 1.92M | $195.41M | 1.1K/h | 0 |
| Gate.io | 274.93K | $28.00M | 80.7/h | 0 |
| Bybit | 232.18K | $23.65M | 50.1/h | 0 |
| Bitget | 29.13K | $2.97M | 112.7/h | 0 |
| Kraken | 27.16K | $2.77M | 100.4/h | 0 |
| Coinbase (2) | 24.68K | $2.51M | 369.6/h | 0 |
| Coinbase | 23.67K | $2.41M | 422.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 814 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.215 | 773 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.193 | 780 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.158 | 739 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.156 | 739 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 780 | 0.0000 |
| Total TPS moves with Program failure rate | +0.135 | 761 | 0.0002 |
| Non-vote TPS moves with Program failure rate | +0.135 | 761 | 0.0002 |
| Slot time moves with AMM write-lock congestion | +0.115 | 739 | 0.0017 |
| Share paying base fee only moves with Activity index | +0.113 | 803 | 0.0013 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 465.48K USD | DeFiLlama: 835.74K USD | -56.91% | *indicative*: 0.56x, within the order-of-magnitude band |
| SOL price | coingecko: 101.86 USD | Jupiter (on-chain DEX): 101.85 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 586.64M SOL | CoinGecko: 586.64M SOL | -0.00% | agree |

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
