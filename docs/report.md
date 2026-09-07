# Solana Ecosystem Report

*Generated 2026-09-07 19:16 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 6.3 robust standard deviations above its 7-day baseline: a 35.7% move to 14,655,300.00 USD from a typical 10,796,465.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.3K |
| TPS (non-vote) | 2.2K |
| Slot time | 315.8 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1030 (42.28% complete, ~21.9h remaining) |
| Lifetime transactions | 546.1B |
| Circulating supply | 586.2M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,412 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 25,200 / 605,000 lamports |
| Paying no priority fee | 30.20% of 3,853 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 20.00% of slots needed a priority fee (max 27.4M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 674 |
| Delinquent validators | 14 |
| Delinquent stake | 0.10% |
| Total active stake | 439.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.32% / 24.21% / 35.49% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.96% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.97% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.60% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.18% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.09% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.56% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $103.94 (-1.74% 24h) |
| Market cap | $60.92B (rank #7) |
| 24h volume | $3.20B |
| ATH | $293.31 (-64.56% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.90B |
| Stablecoin supply | $16.37B |
| DEX volume (24h) | $2.90B (+55.76% 1d) |
| App fees (24h, all protocols) | $14.66M |
| Chain fees (24h) | $653.15K |
| Jito MEV tips (24h) | $110.90K |
| **REV - Real Economic Value (24h)** | **$764.05K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.33B | +7.67% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.37B | +9.69% |
| USD1 | $1.26B | +5.20% |
| BUIDL | $977.90M | +10.31% |
| PYUSD | $733.13M | +5.80% |
| USDG | $577.43M | -5.47% |
| USDe | $535.60M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $677.89M |
| Raydium AMM | $315.48M |
| Orca DEX | $267.46M |
| BisonFi | $241.45M |
| Meteora DLMM | $223.09M |
| Tessera V | $206.39M |
| HumidiFi | $143.21M |
| Manifest Trade | $139.63M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.14M |
| fomo Wallet | $2.00M |
| Raydium AMM | $1.78M |
| Meteora DLMM | $1.15M |
| Axiom | $959.52K |
| StonkFun | $803.65K |
| pump.fun | $695.15K |
| Collector Crypt | $541.54K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 232 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $446.77M |
| xStocks 24h DEX volume | $61.31M |
| xStocks holder positions | 356.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: CRCLX ($74.17M), TSLAX ($66.83M), MSTRX ($61.03M), SPYX ($45.11M), GOOGLX ($29.65M)

## Program activity and chain health

Chain tip lag: **+12.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 70,583 (approx.) | 29.50% | 0.6 s |
| Pump.fun | 9,234 | 70.40% | 6.3 s |
| Raydium AMM v4 | 5,723 | 42.40% | 10.4 s |
| Jupiter v6 | 4,383 | 47.90% | 13.6 s |
| Orca Whirlpools | 4,338 | 43.70% | 13.3 s |

Median failure rate across the sampled programs: **43.70%** (range 29.50% to 70.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.35 SOL**.

## Exchange and large-holder balances

11.60M SOL ($1.21B) across 8 publicly-attributed accounts. Net **63K SOL (0.54%) moved off exchanges** over the last 23.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $955.05M | 0.4/h | 1 |
| Binance (2) | 1.73M | $179.33M | 1.2K/h | 0 |
| Gate.io | 287.82K | $29.92M | 129.3/h | 0 |
| Bybit | 210.99K | $21.93M | 28.8/h | 0 |
| Bitget | 93.61K | $9.73M | 228.6/h | 0 |
| Kraken | 35.57K | $3.70M | 276.9/h | 0 |
| Coinbase | 30.89K | $3.21M | 740.7/h | 0 |
| Coinbase (2) | 29.49K | $3.07M | 466.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 776 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.284 | 735 | 0.0000 |
| DEX volume moves with App fees | +0.229 | 735 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.191 | 742 | 0.0000 |
| Total TPS moves with Slot time | +0.152 | 742 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.142 | 701 | 0.0002 |
| Total TPS moves with AMM write-lock congestion | +0.141 | 701 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.124 | 741 | 0.0008 |
| Total TPS moves with Program failure rate | +0.117 | 723 | 0.0016 |
| Non-vote TPS moves with Program failure rate | +0.116 | 723 | 0.0018 |
| Total TPS moves with Activity index | +0.115 | 741 | 0.0018 |
| Slot time moves with AMM write-lock congestion | +0.112 | 701 | 0.0029 |
| AMM write-lock congestion moves with Program failure rate | +0.112 | 701 | 0.0030 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 529.39K USD | DeFiLlama: 653.15K USD | -20.93% | *indicative*: 0.81x, within the order-of-magnitude band |
| SOL price | coingecko: 103.94 USD | Jupiter (on-chain DEX): 103.97 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 586.17M SOL | CoinGecko: 586.17M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-01
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02

**Recently merged SIMDs:**

- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29

**Latest Agave release:** [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) (2026-09-04)

**Latest Firedancer release:** [v26.08.2](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.2) (2026-08-25)

## Ecosystem news

- **[# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[STONK surges 250% to $140 million market cap as stock-paired Solana launchpad StonkFun pulls volume to Raydium and Jupiter](https://www.theblock.co/news/defi/2026-09-06-stonk-surges-250-to-140-million-market-cap-as-stock-paired-solana-launchpad-stonkfun-pulls-volume-to-raydium-and-jupiter-413621)** - The Block, 2026-09-06
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28
- **[Agave 4.2: The Migration Checklist](https://www.helius.dev/blog/agave-4-2-migration-checklist)** - Helius, 2026-08-27

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
