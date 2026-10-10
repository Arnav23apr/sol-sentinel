# Solana Ecosystem Report

*Generated 2026-10-10 19:02 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 6.3 robust standard deviations above its 7-day baseline: a 572.2% move to 0.12 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.9K |
| TPS (non-vote) | 1.8K |
| Slot time | 219 ms |
| Slot | 455M |
| Block height | 433M |
| Epoch | 1054 (8.20% complete, ~24.1h remaining) |
| Lifetime transactions | 558.4B |
| Circulating supply | 588.8M SOL |
| Inflation (annual) | 3.61% |
| AMM write-lock congestion (150-slot window) | 20.00% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 671 |
| Delinquent validators | 9 |
| Delinquent stake | 0.12% |
| Total active stake | 438.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.51% / 24.50% / 35.60% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.97% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.64% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.81% | 0% |
| 4 | `8Gbw…F8iD` | 11.1M | 2.54% | 0% |
| 5 | `Catz…Diqb` | 10.8M | 2.45% | 5% |
| 6 | `51JB…UNAm` | 9.3M | 2.13% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.6M | 1.74% | 7% |
| 9 | `CvSb…wycB` | 6.8M | 1.55% | 5% |
| 10 | `3JD3…FrXf` | 6.4M | 1.47% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $110.20 (+0.77% 24h) |
| Market cap | $64.89B (rank #7) |
| 24h volume | $1.67B |
| ATH | $293.31 (-62.43% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.22B |
| Stablecoin supply | $16.10B |
| DEX volume (24h) | $1.98B (-25.21% 1d) |
| App fees (24h, all protocols) | $13.91M |
| Chain fees (24h) | $808.72K |
| Jito MEV tips (24h) | $200.51K |
| **REV - Real Economic Value (24h)** | **$1.01M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.80B | -9.13% |
| USDT | $2.90B | +2.11% |
| USD1 | $1.41B | +1.11% |
| USDGO | $1.29B | +7.99% |
| BUIDL | $931.06M | -3.77% |
| PYUSD | $701.80M | -4.48% |
| USDG | $625.30M | -1.24% |
| USDe | $492.05M | +7.62% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $389.88M |
| BisonFi | $258.65M |
| pump.fun | $175.62M |
| Orca DEX | $139.81M |
| Raydium AMM | $110.95M |
| Meteora DLMM | $110.70M |
| Tessera V | $107.27M |
| fomo Wallet | $75.90M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $4.05M |
| pump.fun | $2.20M |
| Collector Crypt | $967.45K |
| Axiom | $891.26K |
| Meteora DLMM | $612.21K |
| pump.fun Mobile App | $392.45K |
| Sanctum Validator LSTs | $351.64K |
| fomo Wallet | $342.12K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $32.86M |
| xStocks holder positions | 797.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $596.35M |

## Program activity and chain health

Chain tip lag: **+8.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 77,717 | 37.80% | 0.7 s |
| Pump.fun | 16,712 | 53.40% | 3.5 s |
| Orca Whirlpools | 3,179 | 19.70% | 18.8 s |
| Jupiter v6 | 2,974 | 23.80% | 19.5 s |
| Raydium AMM v4 | 2,090 | 17.30% | 28.3 s |

Median failure rate across the sampled programs: **23.80%** (range 17.30% to 53.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **585.26 SOL**.

## Exchange and large-holder balances

12.70M SOL ($1.40B) across 8 publicly-attributed accounts. Net **110K SOL (0.87%) moved onto exchanges** over the last 23.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.17B | 0.2/h | 4 |
| Binance (2) | 1.43M | $157.54M | 1.6K/h | 0 |
| Bybit | 307.25K | $33.86M | 15.6/h | 0 |
| Gate.io | 298.96K | $32.95M | 139.3/h | 7 |
| Bitget | 33.73K | $3.72M | 159.3/h | 0 |
| Kraken | 30.72K | $3.39M | 477.5/h | 0 |
| Coinbase | 11.80K | $1.30M | 392.2/h | 0 |
| Coinbase (2) | 11.74K | $1.29M | 339.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 966 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.249 | 925 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.226 | 932 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.207 | 891 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.199 | 891 | 0.0000 |
| Total TPS moves with Slot time | +0.185 | 932 | 0.0000 |
| SOL price moves with DeFi TVL | +0.182 | 966 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 913 | 0.0000 |
| Total TPS moves with Program failure rate | +0.159 | 913 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 891 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 110.20 USD | Jupiter (on-chain DEX): 110.17 USD | +0.03% | agree |
| Circulating supply | getSupply (RPC): 588.85M SOL | CoinGecko: 588.85M SOL | -0.00% | agree |

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
