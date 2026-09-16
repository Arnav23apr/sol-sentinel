# Solana Ecosystem Report

*Generated 2026-09-16 00:34 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 5.0 robust standard deviations below its 7-day baseline: a 3.4% move to 15,618,886,656.00 USD from a typical 16,174,312,140.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.0K |
| Slot time | 318.3 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1035 (61.89% complete, ~14.6h remaining) |
| Lifetime transactions | 548.9B |
| Circulating supply | 587.1M SOL |
| Inflation (annual) | 3.65% |
| AMM write-lock congestion (150-slot window) | 28.00% of slots needed a priority fee (max 2.5M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 679 |
| Delinquent validators | 10 |
| Delinquent stake | 0.04% |
| Total active stake | 439.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.33% / 35.57% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 23.93% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.73% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.7M | 2.20% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.58% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $97.14 (-5.39% 24h) |
| Market cap | $57.03B (rank #7) |
| 24h volume | $3.88B |
| ATH | $293.31 (-66.88% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.73B |
| Stablecoin supply | $15.62B |
| DEX volume (24h) | $2.44B (-3.00% 1d) |
| App fees (24h, all protocols) | $13.27M |
| Chain fees (24h) | $647.01K |
| Jito MEV tips (24h) | $145.81K |
| **REV - Real Economic Value (24h)** | **$792.83K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.74B | -8.00% |
| USDT | $2.48B | -10.12% |
| USDGO | $1.38B | +0.46% |
| USD1 | $1.32B | +4.45% |
| BUIDL | $993.10M | +1.55% |
| PYUSD | $716.44M | -1.99% |
| USDG | $612.19M | +7.07% |
| USDe | $527.09M | -1.47% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $445.38M |
| BisonFi | $315.80M |
| Raydium AMM | $248.78M |
| Meteora DLMM | $198.81M |
| Orca DEX | $188.09M |
| HumidiFi | $179.41M |
| fomo Wallet | $166.82M |
| Tessera V | $115.58M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.26M |
| pump.fun | $1.71M |
| Axiom | $1.29M |
| Raydium AMM | $1.01M |
| fomo Wallet | $905.21K |
| Meteora DLMM | $827.24K |
| StonkFun | $588.47K |
| Collector Crypt | $540.18K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $82.61M |
| xStocks holder positions | 548.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $551.78M |

## Program activity and chain health

Chain tip lag: **+12.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,954 | 54.40% | 1 s |
| Pump.fun | 3,987 | 43.60% | 15 s |
| Jupiter v6 | 3,678 | 52.50% | 16.2 s |
| Raydium AMM v4 | 2,661 | 18.30% | 22 s |
| Orca Whirlpools | 2,200 | 41.30% | 27.1 s |

Median failure rate across the sampled programs: **43.60%** (range 18.30% to 54.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.37 SOL**.

## Exchange and large-holder balances

11.77M SOL ($1.14B) across 8 publicly-attributed accounts. Net **172K SOL (1.48%) moved onto exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $892.57M | 0.3/h | 1 |
| Binance (2) | 1.97M | $191.20M | 1.2K/h | 0 |
| Gate.io | 263.49K | $25.60M | 142.8/h | 0 |
| Bybit | 232.08K | $22.54M | 26.3/h | 0 |
| Bitget | 52.52K | $5.10M | 149.8/h | 0 |
| Kraken | 34.01K | $3.30M | 208.2/h | 0 |
| Coinbase (2) | 15.29K | $1.49M | 543.8/h | 0 |
| Coinbase | 15.11K | $1.47M | 529.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 832 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.207 | 791 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.199 | 798 | 0.0000 |
| Total TPS moves with Slot time | +0.161 | 798 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.159 | 757 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.158 | 757 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.146 | 779 | 0.0000 |
| Total TPS moves with Program failure rate | +0.145 | 779 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| Slot time moves with AMM write-lock congestion | +0.116 | 757 | 0.0014 |
| AMM write-lock congestion moves with Program failure rate | +0.102 | 757 | 0.0050 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 97.14 USD | Jupiter (on-chain DEX): 97.02 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 587.07M SOL | CoinGecko: 587.07M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-15
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [SIMD-0558 Amendment: Use accountless sysvar instead of new syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-14
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-15
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26

**Recently merged SIMDs:**

- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08

**Latest Agave release:** [v4.3.0-rc.1](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1) (2026-09-11)

**Latest Firedancer release:** [v26.08.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.5) (2026-09-15)

## Ecosystem news

- **[Solana Treasury Firm DeFi Dev Corp Rolls Out $300M CHAD to Buy More SOL](https://decrypt.co/378183/solana-defi-development-corp-chad)** - Decrypt, 2026-09-15
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
