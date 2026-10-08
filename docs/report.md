# Solana Ecosystem Report

*Generated 2026-10-08 01:25 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.6K |
| TPS (non-vote) | 2.1K |
| Slot time | 270.9 ms |
| Slot | 454M |
| Block height | 432M |
| Epoch | 1051 (84.28% complete, ~5.1h remaining) |
| Lifetime transactions | 557.3B |
| Circulating supply | 589.1M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 20.00% of slots needed a priority fee (max 2.8M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 10 |
| Delinquent stake | 0.01% |
| Total active stake | 439.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.56% / 24.62% / 35.63% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.77% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.7M | 4.02% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.64% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.80% | 0% |
| 4 | `8Gbw…F8iD` | 11.3M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.1M | 2.54% | 5% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.3M | 2.11% | 10% |
| 8 | `9QU2…29mF` | 7.5M | 1.71% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.62% | 5% |
| 10 | `3JD3…FrXf` | 6.7M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $116.24 (-3.19% 24h) |
| Market cap | $68.50B (rank #7) |
| 24h volume | $3.15B |
| ATH | $293.31 (-60.37% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.44B |
| Stablecoin supply | $16.32B |
| DEX volume (24h) | $2.14B (+4.34% 1d) |
| App fees (24h, all protocols) | $14.10M |
| Chain fees (24h) | $970.30K |
| Jito MEV tips (24h) | $241.49K |
| **REV - Real Economic Value (24h)** | **$1.21M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.93B | -1.89% |
| USDT | $2.91B | +6.19% |
| USD1 | $1.41B | +1.76% |
| USDGO | $1.31B | +10.36% |
| BUIDL | $930.17M | -3.54% |
| PYUSD | $703.54M | -7.04% |
| USDG | $631.02M | -3.19% |
| USDe | $516.18M | +15.88% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $300.56M |
| PumpSwap | $280.51M |
| Raydium AMM | $228.88M |
| BisonFi | $220.60M |
| pump.fun | $184.98M |
| Manifest Trade | $154.59M |
| Meteora DLMM | $153.21M |
| Axiom | $124.01M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.25M |
| pump.fun | $2.38M |
| Axiom | $1.12M |
| Meteora DLMM | $655.55K |
| Raydium AMM | $541.72K |
| fomo Wallet | $457.66K |
| StonkFun | $428.16K |
| Collector Crypt | $403.26K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $73.46M |
| xStocks holder positions | 789.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.48M |

## Program activity and chain health

Chain tip lag: **+9.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 89,701 (approx.) | 19.50% | 0.3 s |
| Pump.fun | 20,797 | 77.50% | 2.7 s |
| Orca Whirlpools | 4,187 | 8.60% | 14.1 s |
| Jupiter v6 | 2,361 | 35.90% | 24.7 s |
| Raydium AMM v4 | 1,192 | 11.60% | 50.1 s |

Median failure rate across the sampled programs: **19.50%** (range 8.60% to 77.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.48 SOL**.

## Exchange and large-holder balances

12.38M SOL ($1.44B) across 8 publicly-attributed accounts. Net **98K SOL (0.80%) moved onto exchanges** over the last 22.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.23B | 0.3/h | 1 |
| Binance (2) | 1.11M | $129.46M | 1.6K/h | 0 |
| Bybit | 304.37K | $35.38M | 29.7/h | 0 |
| Gate.io | 220.20K | $25.60M | 250.3/h | 2 |
| Bitget | 99.59K | $11.58M | 6.0K/h | 0 |
| Kraken | 31.44K | $3.65M | 316.6/h | 0 |
| Coinbase | 19.66K | $2.29M | 304.8/h | 0 |
| Coinbase (2) | 19.54K | $2.27M | 446.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 954 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.240 | 913 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.218 | 920 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.210 | 879 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.205 | 879 | 0.0000 |
| Total TPS moves with Slot time | +0.180 | 920 | 0.0000 |
| SOL price moves with DeFi TVL | +0.171 | 954 | 0.0000 |
| Total TPS moves with Program failure rate | +0.167 | 901 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.166 | 901 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.142 | 879 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 116.24 USD | Jupiter (on-chain DEX): 116.29 USD | -0.04% | agree |
| Circulating supply | getSupply (RPC): 589.09M SOL | CoinGecko: 589.09M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-06

**Open SIMD proposals:**

- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-07
- [SIMD-0686: Single Program Runtime Environment](https://github.com/solana-foundation/solana-improvement-documents/pull/688) - updated 2026-10-07
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-10-05
- [SIMD-0684: Loader V3: Allow Prefunded ProgramData](https://github.com/solana-foundation/solana-improvement-documents/pull/684) - updated 2026-10-05
- [SIMD-0683: Pass ABIv1 input metadata via registers r3–r5](https://github.com/solana-foundation/solana-improvement-documents/pull/683) - updated 2026-10-05

**Recently merged SIMDs:**

- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-10-06
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23

**Latest Agave release:** [v4.5.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.1) (2026-10-03)

**Latest Firedancer release:** [v26.10.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.0) (2026-10-07)

## Ecosystem news

- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana’s Orca merges with Loopscale in push to finance AI, robotics and defense](https://www.theblock.co/news/defi/2026-10-07-solanas-orca-merges-with-loopscale-push-to-finance-ai-robotics-defense-417924)** - The Block, 2026-10-07
- **[Jito’s JTX plans mobile app this fall, eyes perps integration later this winter](https://www.theblock.co/news/defi/2026-10-07-jitos-jtx-plans-mobile-app-this-fall-eyes-perps-integration-later-this-winter-417905)** - The Block, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana treasury DeFi Development authorizes CHAD preferred stock buyback program](https://www.theblock.co/news/markets/2026-10-06-defi-development-chad-preferred-stock-repurchase-program-417819)** - The Block, 2026-10-06
- **[Solana Debuts Institutional Settlement Standard With J.P. Morgan Input](https://decrypt.co/380126/solana-institutional-settlement-standard-jp-morgan)** - Decrypt, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06
- **[DeFi Development Corp Adds $3 Million in Solana as SOL Buys Slow](https://decrypt.co/380125/defi-development-corp-adds-3m-solana)** - Decrypt, 2026-10-05
- **[Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)** - Solana.com, 2026-10-05
- **[Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer)** - Solana.com, 2026-10-02

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
