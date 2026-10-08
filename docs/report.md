# Solana Ecosystem Report

*Generated 2026-10-08 07:38 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 1.4K |
| Slot time | 267.9 ms |
| Slot | 454M |
| Block height | 433M |
| Epoch | 1052 (3.66% complete, ~31.0h remaining) |
| Lifetime transactions | 557.4B |
| Circulating supply | 589.2M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 8 |
| Delinquent stake | 0.01% |
| Total active stake | 439.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.58% / 24.59% / 35.61% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.78% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.63% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.81% | 0% |
| 4 | `8Gbw…F8iD` | 11.2M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.1M | 2.52% | 5% |
| 6 | `51JB…UNAm` | 9.3M | 2.11% | 10% |
| 7 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.5M | 1.71% | 7% |
| 9 | `CvSb…wycB` | 6.8M | 1.55% | 5% |
| 10 | `3JD3…FrXf` | 6.7M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $115.64 (-2.72% 24h) |
| Market cap | $68.11B (rank #7) |
| 24h volume | $2.98B |
| ATH | $293.31 (-60.58% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.43B |
| Stablecoin supply | $16.29B |
| DEX volume (24h) | $2.14B (+4.42% 1d) |
| App fees (24h, all protocols) | $13.75M |
| Chain fees (24h) | $970.30K |
| Jito MEV tips (24h) | $235.92K |
| **REV - Real Economic Value (24h)** | **$1.21M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.90B | -2.40% |
| USDT | $2.93B | +6.92% |
| USD1 | $1.41B | +1.76% |
| USDGO | $1.30B | +9.61% |
| BUIDL | $930.17M | -3.54% |
| PYUSD | $702.13M | -7.19% |
| USDG | $637.25M | -2.23% |
| USDe | $516.13M | +15.88% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $280.51M |
| Orca DEX | $259.78M |
| BisonFi | $220.60M |
| Raydium AMM | $217.67M |
| pump.fun | $184.98M |
| Manifest Trade | $157.89M |
| Meteora DLMM | $153.21M |
| Axiom | $124.01M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.25M |
| pump.fun | $2.38M |
| Axiom | $1.12M |
| Meteora DLMM | $655.55K |
| Raydium AMM | $503.49K |
| fomo Wallet | $457.66K |
| StonkFun | $428.16K |
| Collector Crypt | $387.62K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $68.91M |
| xStocks holder positions | 788.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $598.19M |

## Program activity and chain health

Chain tip lag: **+9.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 29,467 | 22.50% | 1.9 s |
| Pump.fun | 9,155 | 54.70% | 6.4 s |
| Orca Whirlpools | 2,874 | 42.10% | 20.6 s |
| Jupiter v6 | 1,544 | 33.00% | 38.3 s |
| Raydium AMM v4 | 669 | 17.30% | 89.5 s |

Median failure rate across the sampled programs: **33.00%** (range 17.30% to 54.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **679.67 SOL**.

## Exchange and large-holder balances

12.32M SOL ($1.42B) across 8 publicly-attributed accounts. Net **4K SOL (0.03%) moved off exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.22B | 0.3/h | 1 |
| Binance (2) | 1.04M | $120.45M | 1.2K/h | 0 |
| Bybit | 304.37K | $35.20M | 70.4/h | 0 |
| Gate.io | 216.22K | $25.00M | 524.8/h | 3 |
| Bitget | 109.11K | $12.62M | 7.2K/h | 0 |
| Kraken | 31.66K | $3.66M | 869.6/h | 0 |
| Coinbase (2) | 24.78K | $2.87M | 190.6/h | 0 |
| Coinbase | 21.60K | $2.50M | 183.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 955 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.235 | 914 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.220 | 921 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.211 | 880 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.206 | 880 | 0.0000 |
| Total TPS moves with Slot time | +0.182 | 921 | 0.0000 |
| SOL price moves with DeFi TVL | +0.173 | 955 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 902 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 902 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.142 | 880 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 115.64 USD | Jupiter (on-chain DEX): 115.55 USD | +0.08% | agree |
| Circulating supply | getSupply (RPC): 589.17M SOL | CoinGecko: 589.17M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-06

**Open SIMD proposals:**

- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-08
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

- **[Samsung to launch USDC transfers on Solana for US Galaxy users](https://www.theblock.co/news/business/2026-10-07-samsung-to-launch-usdc-transfers-on-solana-for-us-galaxy-users-418004)** - The Block, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana’s Orca merges with Loopscale in push to finance AI, robotics and defense](https://www.theblock.co/news/defi/2026-10-07-solanas-orca-merges-with-loopscale-push-to-finance-ai-robotics-defense-417924)** - The Block, 2026-10-07
- **[Jito’s JTX plans mobile app this fall, eyes perps integration later this winter](https://www.theblock.co/news/defi/2026-10-07-jitos-jtx-plans-mobile-app-this-fall-eyes-perps-integration-later-this-winter-417905)** - The Block, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana treasury DeFi Development authorizes CHAD preferred stock buyback program](https://www.theblock.co/news/markets/2026-10-06-defi-development-chad-preferred-stock-repurchase-program-417819)** - The Block, 2026-10-06
- **[Solana Debuts Institutional Settlement Standard With J.P. Morgan Input](https://decrypt.co/380126/solana-institutional-settlement-standard-jp-morgan)** - Decrypt, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06
- **[DeFi Development Corp Adds $3 Million in Solana as SOL Buys Slow](https://decrypt.co/380125/defi-development-corp-adds-3m-solana)** - Decrypt, 2026-10-05
- **[Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)** - Solana.com, 2026-10-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
