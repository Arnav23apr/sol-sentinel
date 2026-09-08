# Solana Ecosystem Report

*Generated 2026-09-08 09:53 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 54.6 robust standard deviations above its 7-day baseline: a 3543.7% move to 1.17 % from a typical 0.03.
- 🔴 **App fees (24h, all protocols)** (critical): App fees (24h, all protocols) is 10.3 robust standard deviations above its 7-day baseline: a 49.8% move to 15,999,657.00 USD from a typical 10,682,294.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.3K |
| Slot time | 315.8 ms |
| Slot | 445M |
| Block height | 423M |
| Epoch | 1030 (80.78% complete, ~7.3h remaining) |
| Lifetime transactions | 546.3B |
| Circulating supply | 586.2M SOL |
| Inflation (annual) | 3.66% |
| Median transaction fee | 5,400 lamports (about $0.00056) |
| Transaction fee p90 / p99 | 24,201 / 410,000 lamports |
| Paying no priority fee | 23.50% of 4,180 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
| Delinquent validators | 15 |
| Delinquent stake | 1.17% |
| Total active stake | 434.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.48% / 24.48% / 35.87% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.18% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 4.01% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.76% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.88% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.62% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.20% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.08% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.70% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $103.71 (-1.14% 24h) |
| Market cap | $60.79B (rank #7) |
| 24h volume | $2.90B |
| ATH | $293.31 (-64.64% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.87B |
| Stablecoin supply | $16.32B |
| DEX volume (24h) | $2.87B (-1.12% 1d) |
| App fees (24h, all protocols) | $16.00M |
| Chain fees (24h) | $750.65K |
| Jito MEV tips (24h) | $118.60K |
| **REV - Real Economic Value (24h)** | **$869.25K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.27B | +8.10% |
| USDT | $2.76B | -2.45% |
| USDGO | $1.37B | +9.73% |
| USD1 | $1.26B | +4.83% |
| BUIDL | $977.90M | +10.26% |
| PYUSD | $731.71M | -5.47% |
| USDG | $578.20M | -5.47% |
| USDe | $536.16M | -0.19% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $873.43M |
| Raydium AMM | $291.98M |
| BisonFi | $241.45M |
| Orca DEX | $226.62M |
| Tessera V | $206.39M |
| Meteora DLMM | $195.35M |
| HumidiFi | $143.21M |
| Manifest Trade | $143.09M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.76M |
| fomo Wallet | $2.00M |
| Raydium AMM | $1.45M |
| Axiom | $1.27M |
| pump.fun | $1.23M |
| Meteora DLMM | $876.51K |
| Orca DEX | $454.58K |
| Collector Crypt | $386.58K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 246 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $441.65M |
| xStocks 24h DEX volume | $71.02M |
| xStocks holder positions | 373.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.35B |

Top tokenized equities: CRCLX ($72.70M), TSLAX ($66.53M), MSTRX ($60.24M), SPYX ($45.00M), GOOGLX ($29.56M)

## Program activity and chain health

Chain tip lag: **+11.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 33,325 | 26.70% | 1.6 s |
| Jupiter v6 | 3,823 | 64.20% | 15.5 s |
| Pump.fun | 2,870 | 54.40% | 20.8 s |
| Raydium AMM v4 | 2,023 | 27.40% | 29.4 s |
| Orca Whirlpools | 1,467 | 44.00% | 40.4 s |

Median failure rate across the sampled programs: **44.00%** (range 26.70% to 64.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.35 SOL**.

## Exchange and large-holder balances

11.63M SOL ($1.21B) across 8 publicly-attributed accounts. Net **96K SOL (0.82%) moved off exchanges** over the last 24.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $952.93M | 0.4/h | 1 |
| Binance (2) | 1.75M | $181.42M | 1.1K/h | 0 |
| Gate.io | 298.53K | $30.96M | 176.4/h | 0 |
| Bybit | 210.99K | $21.88M | 31.7/h | 0 |
| Bitget | 79.92K | $8.29M | 241.9/h | 0 |
| Coinbase | 34.38K | $3.57M | 202.6/h | 0 |
| Coinbase (2) | 33.27K | $3.45M | 202/h | 0 |
| Kraken | 32.27K | $3.35M | 186/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 11 of 117 tested pairs survive, over 780 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.292 | 739 | 0.0000 |
| DEX volume moves with App fees | +0.240 | 739 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.192 | 746 | 0.0000 |
| Total TPS moves with Slot time | +0.154 | 746 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.141 | 705 | 0.0002 |
| Total TPS moves with AMM write-lock congestion | +0.140 | 705 | 0.0002 |
| Non-vote TPS moves with Activity index | +0.123 | 745 | 0.0008 |
| Total TPS moves with Program failure rate | +0.117 | 727 | 0.0015 |
| Non-vote TPS moves with Program failure rate | +0.116 | 727 | 0.0017 |
| Slot time moves with AMM write-lock congestion | +0.115 | 705 | 0.0022 |
| Total TPS moves with Activity index | +0.114 | 745 | 0.0018 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 381.48K USD | DeFiLlama: 750.65K USD | -65.22% | *indicative*: 0.51x, within the order-of-magnitude band |
| SOL price | coingecko: 103.71 USD | Jupiter (on-chain DEX): 103.64 USD | +0.07% | agree |
| Circulating supply | getSupply (RPC): 586.17M SOL | CoinGecko: 586.17M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-05
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-08
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-02

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

- **[‘The chain is now earnings’: Bernstein sees 31% upside for Robinhood as fees top Solana, BNB Chain](https://www.theblock.co/news/markets/2026-09-08-bernstein-sees-upside-robinhood-413729)** - The Block, 2026-09-08
- **[# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[STONK surges 250% to $140 million market cap as stock-paired Solana launchpad StonkFun pulls volume to Raydium and Jupiter](https://www.theblock.co/news/defi/2026-09-06-stonk-surges-250-to-140-million-market-cap-as-stock-paired-solana-launchpad-stonkfun-pulls-volume-to-raydium-and-jupiter-413621)** - The Block, 2026-09-06
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01
- **[Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026)** - Solana.com, 2026-08-28

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
