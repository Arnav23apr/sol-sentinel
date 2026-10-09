# Solana Ecosystem Report

*Generated 2026-10-09 19:14 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 4.7 robust standard deviations below its 7-day baseline: a 8.5% move to 109.41 USD from a typical 119.51.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 4.1 robust standard deviations below its 7-day baseline: a 6.6% move to 6,207,275,980.00 USD from a typical 6,646,643,395.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.1K |
| TPS (non-vote) | 2.0K |
| Slot time | 216.6 ms |
| Slot | 455M |
| Block height | 433M |
| Epoch | 1053 (17.35% complete, ~21.5h remaining) |
| Lifetime transactions | 558.0B |
| Circulating supply | 588.8M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 820.0K µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 674 |
| Delinquent validators | 6 |
| Delinquent stake | 0.00% |
| Total active stake | 437.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.57% / 24.63% / 35.73% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.96% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.64% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.81% | 0% |
| 4 | `8Gbw…F8iD` | 11.2M | 2.55% | 0% |
| 5 | `Catz…Diqb` | 11.0M | 2.51% | 5% |
| 6 | `51JB…UNAm` | 9.3M | 2.13% | 10% |
| 7 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 6.8M | 1.56% | 5% |
| 10 | `3JD3…FrXf` | 6.7M | 1.53% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $109.41 (+0.71% 24h) |
| Market cap | $64.49B (rank #7) |
| 24h volume | $3.15B |
| ATH | $293.31 (-62.70% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.21B |
| Stablecoin supply | $16.17B |
| DEX volume (24h) | $2.64B (+19.91% 1d) |
| App fees (24h, all protocols) | $15.07M |
| Chain fees (24h) | $940.13K |
| Jito MEV tips (24h) | $248.59K |
| **REV - Real Economic Value (24h)** | **$1.19M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.79B | -5.03% |
| USDT | $2.94B | +5.75% |
| USD1 | $1.41B | +1.76% |
| USDGO | $1.29B | +9.09% |
| BUIDL | $924.66M | -4.43% |
| PYUSD | $735.56M | -1.30% |
| USDG | $628.04M | -4.50% |
| USDe | $495.81M | +6.80% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $364.57M |
| BisonFi | $297.21M |
| Orca DEX | $284.75M |
| Meteora DLMM | $215.94M |
| Raydium AMM | $173.85M |
| pump.fun | $158.81M |
| Tessera V | $143.44M |
| Manifest Trade | $118.25M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.64M |
| pump.fun | $2.24M |
| Meteora DLMM | $1.32M |
| Axiom | $1.05M |
| Jupiter Perpetual Exchange | $611.60K |
| Collector Crypt | $468.58K |
| fomo Wallet | $385.09K |
| pump.fun Mobile App | $384.79K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $62.91M |
| xStocks holder positions | 793.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $596.94M |

## Program activity and chain health

Chain tip lag: **+8.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 46,094 | 16.30% | 1.1 s |
| Pump.fun | 9,058 | 47.40% | 6.5 s |
| Orca Whirlpools | 3,668 | 22.20% | 16.2 s |
| Jupiter v6 | 2,516 | 32.60% | 23.8 s |
| Raydium AMM v4 | 2,227 | 13.70% | 26.9 s |

Median failure rate across the sampled programs: **22.20%** (range 13.70% to 47.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **277.40 SOL**.

## Exchange and large-holder balances

12.59M SOL ($1.38B) across 8 publicly-attributed accounts. Net **106K SOL (0.85%) moved onto exchanges** over the last 22.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.16B | 0.2/h | 1 |
| Binance (2) | 1.33M | $145.10M | 1.5K/h | 0 |
| Bybit | 307.25K | $33.62M | 26/h | 0 |
| Gate.io | 283.49K | $31.02M | 185.2/h | 1 |
| Bitget | 35.87K | $3.92M | 157.5/h | 1 |
| Kraken | 35.06K | $3.84M | 509.9/h | 0 |
| Coinbase | 13.20K | $1.44M | 395.2/h | 0 |
| Coinbase (2) | 12.99K | $1.42M | 381.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 961 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.240 | 920 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 927 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.207 | 886 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.198 | 886 | 0.0000 |
| SOL price moves with DeFi TVL | +0.182 | 961 | 0.0000 |
| Total TPS moves with Slot time | +0.181 | 927 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 908 | 0.0000 |
| Total TPS moves with Program failure rate | +0.161 | 908 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.143 | 886 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.102 | 886 | 0.0024 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 109.41 USD | Jupiter (on-chain DEX): 109.25 USD | +0.15% | agree |
| Circulating supply | getSupply (RPC): 588.77M SOL | CoinGecko: 588.77M SOL | -0.00% | agree |

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

**Latest Agave release:** [v4.5.0-alpha.2](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-alpha.2) (2026-10-08)

**Latest Firedancer release:** [v26.10.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.0) (2026-10-07)

## Ecosystem news

- **[Solana DeFi Firms Orca and Loopscale Merge Under New Formation Brand](https://decrypt.co/380522/solana-defi-firms-orca-and-loopscale-merge-under-new-formation-brand)** - Decrypt, 2026-10-08
- **[Decrypt Money Accounts on Solana to Power The Information Exchange](https://decrypt.co/380436/decrypt-money-accounts-on-solana-to-power-the-information-exchange)** - Decrypt, 2026-10-08
- **[Securitize Brings Nvidia, Apple and Amazon Onchain With Tokenized Stocks on Solana](https://decrypt.co/380458/securitize-nvidia-apple-amazon-tokenized-stocks-solana)** - Decrypt, 2026-10-08
- **[Securitize launches 1:1-backed tokenized stocks, starting with Apple, Nvidia, Strategy and more](https://www.theblock.co/news/markets/2026-10-08-securitize-launches-tokenized-us-stocks-solana-418043)** - The Block, 2026-10-08
- **[Samsung Wallet Taps Solana for USDC Transfers on 82M US Galaxy Devices](https://decrypt.co/380377/samsung-wallet-taps-solana-for-usdc-transfers-on-82m-us-galaxy-devices)** - Decrypt, 2026-10-08
- **[Samsung to launch USDC transfers on Solana for US Galaxy users](https://www.theblock.co/news/business/2026-10-07-samsung-to-launch-usdc-transfers-on-solana-for-us-galaxy-users-418004)** - The Block, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana’s Orca merges with Loopscale in push to finance AI, robotics and defense](https://www.theblock.co/news/defi/2026-10-07-solanas-orca-merges-with-loopscale-push-to-finance-ai-robotics-defense-417924)** - The Block, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
