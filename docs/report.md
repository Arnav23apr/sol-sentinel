# Solana Ecosystem Report

*Generated 2026-09-07 22:08 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 7.7 robust standard deviations above its 7-day baseline: a 37.2% move to 14,655,300.00 USD from a typical 10,682,294.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.0K |
| Slot time | 319.2 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1030 (49.78% complete, ~19.2h remaining) |
| Lifetime transactions | 546.1B |
| Circulating supply | 586.2M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,538 lamports (about $0.00057) |
| Transaction fee p90 / p99 | 24,886 / 410,000 lamports |
| Paying no priority fee | 26.20% of 3,636 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 24.00% of slots needed a priority fee (max 59.9M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 13 |
| Delinquent stake | 0.08% |
| Total active stake | 439.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.32% / 24.21% / 35.48% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.97% |

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
| SOL price | $103.74 (-1.86% 24h) |
| Market cap | $60.84B (rank #7) |
| 24h volume | $3.24B |
| ATH | $293.31 (-64.63% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.91B |
| Stablecoin supply | $16.37B |
| DEX volume (24h) | $2.90B (+55.76% 1d) |
| App fees (24h, all protocols) | $14.66M |
| Chain fees (24h) | $653.15K |
| Jito MEV tips (24h) | $119.50K |
| **REV - Real Economic Value (24h)** | **$772.64K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.32B | +7.51% |
| USDT | $2.77B | -2.45% |
| USDGO | $1.37B | +9.69% |
| USD1 | $1.26B | +5.70% |
| BUIDL | $977.90M | +10.31% |
| PYUSD | $732.96M | +5.80% |
| USDG | $576.64M | -5.60% |
| USDe | $535.59M | -0.30% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $677.89M |
| Raydium AMM | $308.42M |
| Orca DEX | $241.61M |
| BisonFi | $241.45M |
| Meteora DLMM | $223.09M |
| Tessera V | $206.39M |
| HumidiFi | $143.21M |
| Manifest Trade | $133.30M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.14M |
| fomo Wallet | $2.00M |
| Raydium AMM | $1.67M |
| Meteora DLMM | $1.15M |
| Axiom | $959.52K |
| StonkFun | $803.65K |
| pump.fun | $695.15K |
| Collector Crypt | $527.20K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 222 |
| Persistently-active cohort (capture-recapture est.) | 2.2K |
| Unique payers across sampled blocks | 1.3K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $448.00M |
| xStocks 24h DEX volume | $66.70M |
| xStocks holder positions | 361.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.36B |

Top tokenized equities: CRCLX ($74.69M), TSLAX ($66.71M), MSTRX ($61.62M), SPYX ($45.13M), GOOGLX ($29.67M)

## Program activity and chain health

Chain tip lag: **+12.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 57,331 (approx.) | 27.60% | 0.6 s |
| Orca Whirlpools | 10,129 | 35.20% | 5.7 s |
| Pump.fun | 5,839 | 66.80% | 9.9 s |
| Raydium AMM v4 | 4,867 | 30.70% | 11.8 s |
| Jupiter v6 | 3,632 | 51.60% | 16 s |

Median failure rate across the sampled programs: **35.20%** (range 27.60% to 66.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.35 SOL**.

## Exchange and large-holder balances

11.58M SOL ($1.20B) across 8 publicly-attributed accounts. Net **215K SOL (1.82%) moved off exchanges** over the last 24.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $953.21M | 0.4/h | 1 |
| Binance (2) | 1.72M | $178.69M | 1.2K/h | 0 |
| Gate.io | 273.23K | $28.34M | 139.5/h | 0 |
| Bybit | 210.99K | $21.89M | 24.7/h | 0 |
| Bitget | 89.44K | $9.28M | 217.5/h | 0 |
| Kraken | 35.35K | $3.67M | 195.1/h | 0 |
| Coinbase | 29.40K | $3.05M | 466.3/h | 0 |
| Coinbase (2) | 29.29K | $3.04M | 764.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 777 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.286 | 736 | 0.0000 |
| DEX volume moves with App fees | +0.229 | 736 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.189 | 743 | 0.0000 |
| Total TPS moves with Slot time | +0.151 | 743 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.141 | 702 | 0.0002 |
| Total TPS moves with AMM write-lock congestion | +0.140 | 702 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.124 | 742 | 0.0007 |
| Total TPS moves with Program failure rate | +0.118 | 724 | 0.0015 |
| Non-vote TPS moves with Program failure rate | +0.117 | 724 | 0.0016 |
| Total TPS moves with Activity index | +0.115 | 742 | 0.0017 |
| Slot time moves with AMM write-lock congestion | +0.113 | 702 | 0.0026 |
| AMM write-lock congestion moves with Program failure rate | +0.111 | 702 | 0.0033 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 332.09K USD | DeFiLlama: 653.15K USD | -65.17% | *indicative*: 0.51x, within the order-of-magnitude band |
| SOL price | coingecko: 103.74 USD | Jupiter (on-chain DEX): 103.82 USD | -0.08% | agree |
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
