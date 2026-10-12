# Solana Ecosystem Report

*Generated 2026-10-12 19:32 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.7K |
| TPS (non-vote) | 2.6K |
| Slot time | 219 ms |
| Slot | 456M |
| Block height | 434M |
| Epoch | 1055 (93.23% complete, ~1.8h remaining) |
| Lifetime transactions | 559.3B |
| Circulating supply | 589.1M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 46.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
| Delinquent validators | 8 |
| Delinquent stake | 0.02% |
| Total active stake | 438.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.49% / 24.48% / 35.58% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.95% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.05% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.64% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.81% | 0% |
| 4 | `8Gbw…F8iD` | 11.1M | 2.54% | 0% |
| 5 | `Catz…Diqb` | 10.8M | 2.45% | 5% |
| 6 | `51JB…UNAm` | 9.3M | 2.13% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 6.8M | 1.55% | 5% |
| 10 | `3JD3…FrXf` | 6.4M | 1.46% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $108.04 (-2.95% 24h) |
| Market cap | $63.65B (rank #7) |
| 24h volume | $2.81B |
| ATH | $293.31 (-63.17% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.14B |
| Stablecoin supply | $15.97B |
| DEX volume (24h) | $1.28B (-0.72% 1d) |
| App fees (24h, all protocols) | $11.30M |
| Chain fees (24h) | $753.34K |
| Jito MEV tips (24h) | $194.25K |
| **REV - Real Economic Value (24h)** | **$947.59K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.78B | -8.34% |
| USDT | $2.82B | -1.74% |
| USD1 | $1.41B | +1.11% |
| USDGO | $1.29B | +7.99% |
| BUIDL | $931.06M | -3.77% |
| PYUSD | $687.19M | -3.86% |
| USDG | $626.26M | +0.12% |
| USDe | $468.39M | -0.13% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $250.95M |
| BisonFi | $163.16M |
| Raydium AMM | $160.84M |
| pump.fun | $160.84M |
| PumpSwap | $135.49M |
| Manifest Trade | $114.36M |
| Meteora DLMM | $82.88M |
| Tessera V | $72.81M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.07M |
| pump.fun | $2.01M |
| Meteora DLMM | $822.28K |
| Axiom | $821.21K |
| Raydium AMM | $387.89K |
| pump.fun Mobile App | $372.67K |
| fomo Wallet | $290.30K |
| Sanctum Validator LSTs | $287.10K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $61.41M |
| xStocks holder positions | 807.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $594.92M |

## Program activity and chain health

Chain tip lag: **+7.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 109,315 (approx.) | 40.70% | 0.4 s |
| Pump.fun | 28,767 | 82.20% | 2 s |
| Jupiter v6 | 11,404 | 78.90% | 5.3 s |
| Orca Whirlpools | 8,696 | 39.40% | 6.8 s |
| Raydium AMM v4 | 2,098 | 10.20% | 28.3 s |

Median failure rate across the sampled programs: **40.70%** (range 10.20% to 82.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **361.46 SOL**.

## Exchange and large-holder balances

12.96M SOL ($1.40B) across 8 publicly-attributed accounts. Net **185K SOL (1.45%) moved onto exchanges** over the last 20.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.14B | 0.2/h | 4 |
| Binance (2) | 1.61M | $173.83M | 1.6K/h | 0 |
| Bybit | 307.25K | $33.20M | 24.8/h | 0 |
| Gate.io | 287.14K | $31.02M | 168.9/h | 2 |
| Bitget | 68.14K | $7.36M | 137.4/h | 0 |
| Coinbase (2) | 42.75K | $4.62M | 284.1/h | 0 |
| Coinbase | 38.86K | $4.20M | 302/h | 0 |
| Kraken | 35.43K | $3.83M | 441.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 975 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.245 | 934 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.226 | 941 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.207 | 900 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.198 | 900 | 0.0000 |
| SOL price moves with DeFi TVL | +0.188 | 975 | 0.0000 |
| Total TPS moves with Slot time | +0.186 | 941 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.157 | 922 | 0.0000 |
| Total TPS moves with Program failure rate | +0.156 | 922 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 900 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 108.04 USD | Jupiter (on-chain DEX): 108.09 USD | -0.05% | agree |
| Circulating supply | getSupply (RPC): 589.11M SOL | CoinGecko: 589.11M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-12

**Open SIMD proposals:**

- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-12
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-07
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-11

**Recently merged SIMDs:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23

**Latest Agave release:** [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) (2026-10-08)

**Latest Firedancer release:** [v26.10.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.1) (2026-10-09)

## Ecosystem news

- **[Solana Treasury Firm DeFi Development Keeps Buying SOL as CHAD Preferred Stock Hits Record](https://decrypt.co/380752/solana-treasury-firm-defi-development-keeps-buying-sol)** - Decrypt, 2026-10-12
- **[StoneX raises Securitize price target 50% as tokenized stock platform opens new revenue stream](https://www.theblock.co/news/markets/2026-10-12-stonex-raises-securitize-price-target-tokenized-stocks-418313)** - The Block, 2026-10-12
- **[Bitcoin, Ethereum and Solana ETFs All in the Red for October](https://decrypt.co/380640/bitcoin-ethereum-solana-etfs-red-october)** - Decrypt, 2026-10-11
- **[Ether ETFs extend outflow streak to nine days as Solana funds snap record 14-week inflow run](https://www.theblock.co/news/markets/2026-10-10-ether-etfs-extend-outflow-streak-to-nine-days-as-solana-funds-snap-record-14-week-inflow-run-418215)** - The Block, 2026-10-10
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana DeFi Firms Orca and Loopscale Merge Under New Formation Brand](https://decrypt.co/380522/solana-defi-firms-orca-and-loopscale-merge-under-new-formation-brand)** - Decrypt, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
