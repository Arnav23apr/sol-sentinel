# Solana Ecosystem Report

*Generated 2026-09-09 10:01 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 9.2 robust standard deviations above its 7-day baseline: a 52.3% move to 16,439,615.00 USD from a typical 10,796,465.50.
- 🟠 **Activity index (fee payers per block)** (warning): Activity index (fee payers per block) is 3.7 robust standard deviations above its 7-day baseline: a 47.0% move to 344.00 from a typical 234.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.8K |
| TPS (non-vote) | 1.7K |
| Slot time | 317.5 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1031 (44.23% complete, ~21.2h remaining) |
| Lifetime transactions | 546.7B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,151 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 23,333 / 242,126 lamports |
| Paying no priority fee | 36.20% of 5,193 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 7.30% of slots needed a priority fee (max 6.5M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 10 |
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
| SOL price | $103.50 (-0.09% 24h) |
| Market cap | $60.68B (rank #7) |
| 24h volume | $2.81B |
| ATH | $293.31 (-64.71% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.99B |
| Stablecoin supply | $16.25B |
| DEX volume (24h) | $2.58B (-5.25% 1d) |
| App fees (24h, all protocols) | $16.44M |
| Chain fees (24h) | $772.73K |
| Jito MEV tips (24h) | $149.51K |
| **REV - Real Economic Value (24h)** | **$922.25K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.11B | +7.20% |
| USDT | $2.76B | -2.45% |
| USDGO | $1.37B | +10.28% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $987.58M | +11.34% |
| PYUSD | $752.34M | +1.93% |
| USDG | $589.13M | -3.94% |
| USDe | $535.65M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $737.12M |
| Raydium AMM | $328.32M |
| Meteora DLMM | $237.76M |
| BisonFi | $204.07M |
| Tessera V | $149.50M |
| Manifest Trade | $132.18M |
| pump.fun | $100.28M |
| HumidiFi | $96.88M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| fomo Wallet | $1.66M |
| Axiom | $1.44M |
| Raydium AMM | $1.41M |
| pump.fun | $1.27M |
| Meteora DLMM | $1.08M |
| Pyth Pro | $722.90K |
| Sanctum Validator LSTs | $377.06K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 344 |
| Persistently-active cohort (capture-recapture est.) | 4.2K |
| Unique payers across sampled blocks | 2.1K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $443.55M |
| xStocks 24h DEX volume | $86.23M |
| xStocks holder positions | 396.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.35B |

Top tokenized equities: CRCLX ($70.78M), TSLAX ($68.58M), MSTRX ($60.48M), SPYX ($45.64M), GOOGLX ($29.74M)

## Program activity and chain health

Chain tip lag: **+12.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 40,299 | 12.80% | 1.3 s |
| Jupiter v6 | 8,183 | 76.40% | 7.3 s |
| Pump.fun | 8,118 | 66.60% | 7.3 s |
| Orca Whirlpools | 2,064 | 39.60% | 28.6 s |
| Raydium AMM v4 | 729 | 22.10% | 82.2 s |

Median failure rate across the sampled programs: **39.60%** (range 12.80% to 76.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **568.43 SOL**.

## Exchange and large-holder balances

11.62M SOL ($1.20B) across 8 publicly-attributed accounts. Net **44K SOL (0.38%) moved onto exchanges** over the last 20.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $951.00M | 0.4/h | 1 |
| Binance (2) | 1.76M | $182.56M | 1.0K/h | 0 |
| Gate.io | 322.13K | $33.34M | 156.2/h | 0 |
| Bybit | 211.87K | $21.93M | 42.6/h | 0 |
| Bitget | 40.92K | $4.24M | 335.2/h | 0 |
| Coinbase | 31.73K | $3.28M | 222.5/h | 0 |
| Coinbase (2) | 29.58K | $3.06M | 208.5/h | 0 |
| Kraken | 27.46K | $2.84M | 208.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 11 of 117 tested pairs survive, over 787 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.300 | 746 | 0.0000 |
| DEX volume moves with App fees | +0.229 | 746 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.194 | 753 | 0.0000 |
| Total TPS moves with Slot time | +0.155 | 753 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.139 | 712 | 0.0002 |
| Non-vote TPS moves with AMM write-lock congestion | +0.139 | 712 | 0.0002 |
| Total TPS moves with Program failure rate | +0.121 | 734 | 0.0010 |
| Non-vote TPS moves with Activity index | +0.121 | 752 | 0.0009 |
| Non-vote TPS moves with Program failure rate | +0.120 | 734 | 0.0011 |
| Slot time moves with AMM write-lock congestion | +0.113 | 712 | 0.0025 |
| Total TPS moves with Activity index | +0.112 | 752 | 0.0020 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 392.93K USD | DeFiLlama: 772.73K USD | -65.17% | *indicative*: 0.51x, within the order-of-magnitude band |
| SOL price | coingecko: 103.50 USD | Jupiter (on-chain DEX): 103.56 USD | -0.06% | agree |
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
- **[‘The chain is now earnings’: Bernstein sees 31% upside for Robinhood as fees top Solana, BNB Chain](https://www.theblock.co/news/markets/2026-09-08-bernstein-sees-upside-robinhood-413729)** - The Block, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
