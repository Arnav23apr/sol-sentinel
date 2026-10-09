# Solana Ecosystem Report

*Generated 2026-10-09 06:55 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 5.0 robust standard deviations below its 7-day baseline: a 7.6% move to 110.62 USD from a typical 119.70.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 4.3 robust standard deviations below its 7-day baseline: a 6.1% move to 6,246,153,795.00 USD from a typical 6,652,453,936.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.5K |
| TPS (non-vote) | 2.0K |
| Slot time | 268.5 ms |
| Slot | 455M |
| Block height | 433M |
| Epoch | 1052 (75.85% complete, ~7.8h remaining) |
| Lifetime transactions | 557.8B |
| Circulating supply | 588.7M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 300.0K µlam/CU) |
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
| SOL price | $110.62 (-4.02% 24h) |
| Market cap | $65.12B (rank #7) |
| 24h volume | $5.03B |
| ATH | $293.31 (-62.29% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.25B |
| Stablecoin supply | $16.13B |
| DEX volume (24h) | $2.44B (+10.65% 1d) |
| App fees (24h, all protocols) | $14.30M |
| Chain fees (24h) | $940.13K |
| Jito MEV tips (24h) | $251.78K |
| **REV - Real Economic Value (24h)** | **$1.19M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.78B | -5.16% |
| USDT | $2.91B | +4.67% |
| USD1 | $1.41B | +1.76% |
| USDGO | $1.30B | +9.42% |
| BUIDL | $924.57M | -4.44% |
| PYUSD | $721.79M | -3.16% |
| USDG | $627.82M | -4.51% |
| USDe | $493.73M | +6.41% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $364.57M |
| Orca DEX | $357.66M |
| BisonFi | $230.56M |
| Meteora DLMM | $215.94M |
| Raydium AMM | $213.83M |
| Manifest Trade | $164.66M |
| pump.fun | $160.98M |
| Tessera V | $105.71M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.64M |
| pump.fun | $2.24M |
| Axiom | $1.05M |
| Meteora DLMM | $655.55K |
| Jupiter Perpetual Exchange | $611.60K |
| Raydium AMM | $458.36K |
| Collector Crypt | $435.86K |
| fomo Wallet | $385.85K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $76.63M |
| xStocks holder positions | 795.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $597.67M |

## Program activity and chain health

Chain tip lag: **+10.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 51,844 | 38.50% | 1.1 s |
| Pump.fun | 13,132 | 51.70% | 4.6 s |
| Jupiter v6 | 1,997 | 32.70% | 29.8 s |
| Orca Whirlpools | 1,720 | 24.30% | 34.6 s |
| Raydium AMM v4 | 875 | 6.30% | 68.2 s |

Median failure rate across the sampled programs: **32.70%** (range 6.30% to 51.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.49 SOL**.

## Exchange and large-holder balances

12.54M SOL ($1.39B) across 8 publicly-attributed accounts. Net **219K SOL (1.78%) moved onto exchanges** over the last 23.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.17B | 0.2/h | 1 |
| Binance (2) | 1.29M | $142.31M | 1.2K/h | 0 |
| Bybit | 307.25K | $33.99M | 18.5/h | 0 |
| Gate.io | 255.45K | $28.26M | 240.3/h | 2 |
| Bitget | 44.77K | $4.95M | 138.7/h | 0 |
| Kraken | 32.18K | $3.56M | 451.7/h | 0 |
| Coinbase (2) | 26.29K | $2.91M | 206.1/h | 0 |
| Coinbase | 16.30K | $1.80M | 202.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 959 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.237 | 918 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.222 | 925 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.205 | 884 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.200 | 884 | 0.0000 |
| Total TPS moves with Slot time | +0.185 | 925 | 0.0000 |
| SOL price moves with DeFi TVL | +0.181 | 959 | 0.0000 |
| Total TPS moves with Program failure rate | +0.162 | 906 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 906 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.141 | 884 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 110.62 USD | Jupiter (on-chain DEX): 110.63 USD | -0.01% | agree |
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
