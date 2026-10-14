# Solana Ecosystem Report

*Generated 2026-10-14 00:43 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.0K |
| TPS (non-vote) | 1.9K |
| Slot time | 215.8 ms |
| Slot | 457M |
| Block height | 435M |
| Epoch | 1057 (4.56% complete, ~24.7h remaining) |
| Lifetime transactions | 559.8B |
| Circulating supply | 589.2M SOL |
| Inflation (annual) | 3.60% |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 299.9K µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
| Delinquent validators | 5 |
| Delinquent stake | 0.00% |
| Total active stake | 438.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.48% / 24.59% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.77% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.61% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.81% | 0% |
| 4 | `8Gbw…F8iD` | 11.1M | 2.54% | 0% |
| 5 | `Catz…Diqb` | 10.8M | 2.46% | 5% |
| 6 | `51JB…UNAm` | 9.4M | 2.15% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 8 | `9QU2…29mF` | 7.7M | 1.76% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `3JD3…FrXf` | 6.6M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $107.88 (+4.15% 24h) |
| Market cap | $63.56B (rank #7) |
| 24h volume | $3.52B |
| ATH | $293.31 (-63.22% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.06B |
| Stablecoin supply | $16.13B |
| DEX volume (24h) | $2.25B (+0.70% 1d) |
| App fees (24h, all protocols) | $13.08M |
| Chain fees (24h) | $790.54K |
| Jito MEV tips (24h) | $209.20K |
| **REV - Real Economic Value (24h)** | **$999.75K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.04B | -5.57% |
| USDT | $2.79B | -2.78% |
| USD1 | $1.41B | +1.11% |
| USDGO | $1.27B | -0.81% |
| BUIDL | $890.34M | -8.01% |
| PYUSD | $699.31M | -2.02% |
| USDG | $624.21M | +0.77% |
| USDe | $452.19M | -10.20% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $411.88M |
| Orca DEX | $278.66M |
| BisonFi | $274.06M |
| pump.fun | $178.90M |
| Raydium AMM | $178.09M |
| Manifest Trade | $130.78M |
| Meteora DLMM | $124.24M |
| Tessera V | $116.62M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.61M |
| pump.fun | $2.20M |
| Axiom | $955.87K |
| Meteora DLMM | $865.50K |
| Jupiter Perpetual Exchange | $443.48K |
| Raydium AMM | $408.63K |
| Collector Crypt | $399.62K |
| pump.fun Mobile App | $327.45K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $60.47M |
| xStocks holder positions | 811.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $587.36M |

## Program activity and chain health

Chain tip lag: **+8.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 66,103 | 44.60% | 0.9 s |
| Jupiter v6 | 7,469 | 39.70% | 8 s |
| Pump.fun | 5,775 | 44.00% | 10.4 s |
| Orca Whirlpools | 2,975 | 21.50% | 20.1 s |
| Raydium AMM v4 | 1,600 | 3.30% | 37.1 s |

Median failure rate across the sampled programs: **39.70%** (range 3.30% to 44.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **573.20 SOL**.

## Exchange and large-holder balances

13.08M SOL ($1.41B) across 8 publicly-attributed accounts. Net **148K SOL (1.14%) moved onto exchanges** over the last 23.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.57M | $1.14B | 0.2/h | 4 |
| Binance (2) | 1.72M | $185.43M | 1.1K/h | 0 |
| Bybit | 308.80K | $33.31M | 20.8/h | 0 |
| Gate.io | 303.20K | $32.71M | 146.2/h | 0 |
| Bitget | 89.53K | $9.66M | 102.1/h | 0 |
| Kraken | 31.72K | $3.42M | 292.7/h | 0 |
| Coinbase (2) | 29.58K | $3.19M | 264.7/h | 0 |
| Coinbase | 26.21K | $2.83M | 279.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 980 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.252 | 939 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.227 | 946 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.209 | 905 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.201 | 905 | 0.0000 |
| SOL price moves with DeFi TVL | +0.192 | 980 | 0.0000 |
| Total TPS moves with Slot time | +0.187 | 946 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.159 | 927 | 0.0000 |
| Total TPS moves with Program failure rate | +0.158 | 927 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 905 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 107.88 USD | Jupiter (on-chain DEX): 107.75 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 589.22M SOL | CoinGecko: 589.22M SOL | 0.00% | agree |

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

**Latest Agave release:** [v4.4.0-beta.1](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.1) (2026-10-13)

**Latest Firedancer release:** [v26.10.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.1) (2026-10-09)

## Ecosystem news

- **[Solana Treasury Firm DeFi Development Keeps Buying SOL as CHAD Preferred Stock Hits Record](https://decrypt.co/380752/solana-treasury-firm-defi-development-keeps-buying-sol)** - Decrypt, 2026-10-12
- **[StoneX raises Securitize price target 50% as tokenized stock platform opens new revenue stream](https://www.theblock.co/news/markets/2026-10-12-stonex-raises-securitize-price-target-tokenized-stocks-418313)** - The Block, 2026-10-12
- **[Bitcoin, Ethereum and Solana ETFs All in the Red for October](https://decrypt.co/380640/bitcoin-ethereum-solana-etfs-red-october)** - Decrypt, 2026-10-11
- **[Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories)** - Solana.com, 2026-10-09
- **[Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2)** - Solana.com, 2026-10-08
- **[Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026)** - Solana.com, 2026-10-08
- **[Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet)** - Solana.com, 2026-10-07
- **[Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026)** - Solana.com, 2026-10-06
- **[Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions)** - Solana.com, 2026-10-06
- **[Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope)** - Solana.com, 2026-10-05

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
