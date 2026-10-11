# Solana Ecosystem Report

*Generated 2026-10-11 07:25 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.3K |
| TPS (non-vote) | 1.2K |
| Slot time | 217 ms |
| Slot | 456M |
| Block height | 434M |
| Epoch | 1054 (55.55% complete, ~11.6h remaining) |
| Lifetime transactions | 558.6B |
| Circulating supply | 589.1M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 6.00% of slots needed a priority fee (max 999.9K µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 674 |
| Delinquent validators | 6 |
| Delinquent stake | 0.00% |
| Total active stake | 438.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.49% / 24.47% / 35.56% |
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
| SOL price | $109.40 (-0.35% 24h) |
| Market cap | $64.44B (rank #7) |
| 24h volume | $1.53B |
| ATH | $293.31 (-62.70% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.20B |
| Stablecoin supply | $16.09B |
| DEX volume (24h) | $1.58B (-20.13% 1d) |
| App fees (24h, all protocols) | $11.84M |
| Chain fees (24h) | $740.67K |
| Jito MEV tips (24h) | $177.09K |
| **REV - Real Economic Value (24h)** | **$917.76K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.78B | -8.67% |
| USDT | $2.90B | +2.11% |
| USD1 | $1.41B | +1.11% |
| USDGO | $1.29B | +7.99% |
| BUIDL | $931.06M | -3.77% |
| PYUSD | $705.99M | -0.82% |
| USDG | $626.27M | -0.14% |
| USDe | $490.47M | +4.12% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $258.65M |
| PumpSwap | $235.28M |
| pump.fun | $175.62M |
| Tessera V | $107.27M |
| Raydium AMM | $105.22M |
| Orca DEX | $102.26M |
| Meteora DLMM | $78.90M |
| GoonFi | $75.15M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.61M |
| pump.fun | $1.93M |
| Axiom | $836.00K |
| Meteora DLMM | $642.87K |
| Collector Crypt | $629.28K |
| pump.fun Mobile App | $387.70K |
| fomo Wallet | $342.12K |
| Sanctum Validator LSTs | $284.37K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $23.32M |
| xStocks holder positions | 796.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $595.64M |

## Program activity and chain health

Chain tip lag: **+7.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 27,066 | 24.60% | 2 s |
| Pump.fun | 7,837 | 70.40% | 7.6 s |
| Jupiter v6 | 2,859 | 58.00% | 20.4 s |
| Raydium AMM v4 | 2,683 | 63.90% | 21.3 s |
| Orca Whirlpools | 2,678 | 28.00% | 21.3 s |

Median failure rate across the sampled programs: **58.00%** (range 24.60% to 70.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **365.86 SOL**.

## Exchange and large-holder balances

12.67M SOL ($1.39B) across 6 publicly-attributed accounts. Net **48K SOL (0.38%) moved onto exchanges** over the last 22.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.16B | 0.2/h | 4 |
| Binance (2) | 1.41M | $154.56M | 947.4/h | 0 |
| Bybit | 307.25K | $33.61M | 23.3/h | 0 |
| Gate.io | 302.38K | $33.08M | 141/h | 2 |
| Bitget | 46.32K | $5.07M | 198.9/h | 0 |
| Kraken | 30.24K | $3.31M | 147.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 969 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.248 | 928 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.225 | 935 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.205 | 894 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.197 | 894 | 0.0000 |
| SOL price moves with DeFi TVL | +0.186 | 969 | 0.0000 |
| Total TPS moves with Slot time | +0.184 | 935 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.158 | 916 | 0.0000 |
| Total TPS moves with Program failure rate | +0.156 | 916 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 894 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 109.40 USD | Jupiter (on-chain DEX): 109.35 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 589.05M SOL | CoinGecko: 589.05M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0677: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/677) - *open*, updated 2026-10-11

**Open SIMD proposals:**

- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-07
- [SIMD-0690: Hash validation in v2 program migrations](https://github.com/solana-foundation/solana-improvement-documents/pull/690) - updated 2026-10-11
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

- **[Ether ETFs extend outflow streak to nine days as Solana funds snap record 14-week inflow run](https://www.theblock.co/news/markets/2026-10-10-ether-etfs-extend-outflow-streak-to-nine-days-as-solana-funds-snap-record-14-week-inflow-run-418215)** - The Block, 2026-10-10
- **[Solana DeFi Firms Orca and Loopscale Merge Under New Formation Brand](https://decrypt.co/380522/solana-defi-firms-orca-and-loopscale-merge-under-new-formation-brand)** - Decrypt, 2026-10-08
- **[Decrypt Money Accounts on Solana to Power The Information Exchange](https://decrypt.co/380436/decrypt-money-accounts-on-solana-to-power-the-information-exchange)** - Decrypt, 2026-10-08
- **[Securitize Brings Nvidia, Apple and Amazon Onchain With Tokenized Stocks on Solana](https://decrypt.co/380458/securitize-nvidia-apple-amazon-tokenized-stocks-solana)** - Decrypt, 2026-10-08
- **[Securitize launches 1:1-backed tokenized stocks, starting with Apple, Nvidia, Strategy and more](https://www.theblock.co/news/markets/2026-10-08-securitize-launches-tokenized-us-stocks-solana-418043)** - The Block, 2026-10-08
- **[Samsung Wallet Taps Solana for USDC Transfers on 82M US Galaxy Devices](https://decrypt.co/380377/samsung-wallet-taps-solana-for-usdc-transfers-on-82m-us-galaxy-devices)** - Decrypt, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06
- **[Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)** - Solana.com, 2026-10-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
