# Solana Ecosystem Report

*Generated 2026-10-09 00:46 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 6.3 robust standard deviations below its 7-day baseline: a 8.9% move to 109.17 USD from a typical 119.78.
- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 4.9 robust standard deviations below its 7-day baseline: a 3.0% move to 16,082,247,003.00 USD from a typical 16,584,155,228.00.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 4.6 robust standard deviations below its 7-day baseline: a 6.6% move to 6,210,773,694.00 USD from a typical 6,652,453,936.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 1.7K |
| Slot time | 267.9 ms |
| Slot | 455M |
| Block height | 433M |
| Epoch | 1052 (56.75% complete, ~13.9h remaining) |
| Lifetime transactions | 557.7B |
| Circulating supply | 588.7M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 80.00% of slots needed a priority fee (max 4.1M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
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
| SOL price | $109.17 (-5.98% 24h) |
| Market cap | $64.27B (rank #7) |
| 24h volume | $4.96B |
| ATH | $293.31 (-62.78% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.21B |
| Stablecoin supply | $16.08B |
| DEX volume (24h) | $2.37B (+7.45% 1d) |
| App fees (24h, all protocols) | $13.78M |
| Chain fees (24h) | $970.30K |
| Jito MEV tips (24h) | $248.83K |
| **REV - Real Economic Value (24h)** | **$1.22M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.75B | -4.42% |
| USDT | $2.91B | +6.19% |
| USD1 | $1.41B | +1.76% |
| USDGO | $1.30B | +9.88% |
| BUIDL | $924.57M | -4.12% |
| PYUSD | $700.95M | -7.41% |
| USDG | $627.09M | -3.79% |
| USDe | $494.43M | +11.01% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $364.57M |
| Orca DEX | $350.68M |
| Raydium AMM | $233.18M |
| BisonFi | $230.56M |
| Manifest Trade | $172.33M |
| pump.fun | $160.98M |
| Meteora DLMM | $153.21M |
| Tessera V | $105.71M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.25M |
| pump.fun | $2.38M |
| Axiom | $1.12M |
| Meteora DLMM | $655.55K |
| Raydium AMM | $518.86K |
| Collector Crypt | $498.01K |
| fomo Wallet | $385.85K |
| pump.fun Mobile App | $370.73K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $74.76M |
| xStocks holder positions | 793.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $597.60M |

## Program activity and chain health

Chain tip lag: **+9.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 57,409 | 32.40% | 0.8 s |
| Pump.fun | 24,138 | 69.80% | 2.4 s |
| Jupiter v6 | 6,416 | 67.10% | 9.1 s |
| Orca Whirlpools | 4,027 | 70.80% | 14.7 s |
| Raydium AMM v4 | 1,823 | 46.90% | 32.7 s |

Median failure rate across the sampled programs: **67.10%** (range 32.40% to 70.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.49 SOL**.

## Exchange and large-holder balances

12.53M SOL ($1.37B) across 8 publicly-attributed accounts. Net **148K SOL (1.19%) moved onto exchanges** over the last 23.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.15B | 0.3/h | 1 |
| Binance (2) | 1.22M | $133.63M | 1.1K/h | 0 |
| Bybit | 304.37K | $33.23M | 22/h | 0 |
| Gate.io | 238.84K | $26.07M | 191.2/h | 3 |
| Bitget | 92.99K | $10.15M | 116.7/h | 0 |
| Coinbase (2) | 47.83K | $5.22M | 251.4/h | 0 |
| Kraken | 32.48K | $3.55M | 180.5/h | 0 |
| Coinbase | 15.75K | $1.72M | 303.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 958 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.233 | 917 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.222 | 924 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.208 | 883 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.203 | 883 | 0.0000 |
| Total TPS moves with Slot time | +0.184 | 924 | 0.0000 |
| SOL price moves with DeFi TVL | +0.179 | 958 | 0.0000 |
| Total TPS moves with Program failure rate | +0.164 | 905 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.164 | 905 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.141 | 883 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 109.17 USD | Jupiter (on-chain DEX): 109.37 USD | -0.18% | agree |
| Circulating supply | getSupply (RPC): 588.70M SOL | CoinGecko: 588.70M SOL | -0.00% | agree |

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
- **[Jito’s JTX plans mobile app this fall, eyes perps integration later this winter](https://www.theblock.co/news/defi/2026-10-07-jitos-jtx-plans-mobile-app-this-fall-eyes-perps-integration-later-this-winter-417905)** - The Block, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
