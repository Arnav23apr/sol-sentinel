# Solana Ecosystem Report

*Generated 2026-09-15 19:20 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.9K |
| TPS (non-vote) | 2.8K |
| Slot time | 316.6 ms |
| Slot | 447M |
| Block height | 425M |
| Epoch | 1035 (48.18% complete, ~19.7h remaining) |
| Lifetime transactions | 548.8B |
| Circulating supply | 587.0M SOL |
| Inflation (annual) | 3.65% |
| AMM write-lock congestion (150-slot window) | 38.00% of slots needed a priority fee (max 18.0M µlam/CU) |
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
| Stake on private (100% commission) validators | 23.92% |

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
| SOL price | $98.45 (-4.84% 24h) |
| Market cap | $57.73B (rank #7) |
| 24h volume | $3.87B |
| ATH | $293.31 (-66.44% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.79B |
| Stablecoin supply | $15.72B |
| DEX volume (24h) | $2.53B (+41.27% 1d) |
| App fees (24h, all protocols) | $13.58M |
| Chain fees (24h) | $647.01K |
| Jito MEV tips (24h) | $131.09K |
| **REV - Real Economic Value (24h)** | **$778.10K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.86B | -6.39% |
| USDT | $2.48B | -10.12% |
| USDGO | $1.38B | +0.46% |
| USD1 | $1.32B | +4.45% |
| BUIDL | $992.98M | +1.54% |
| PYUSD | $711.66M | -2.67% |
| USDG | $612.56M | +7.12% |
| USDe | $527.25M | -1.47% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $445.38M |
| BisonFi | $315.80M |
| Raydium AMM | $237.31M |
| Meteora DLMM | $198.81M |
| fomo Wallet | $187.20M |
| HumidiFi | $179.41M |
| Orca DEX | $154.63M |
| Tessera V | $115.58M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.26M |
| pump.fun | $1.71M |
| Axiom | $1.29M |
| Raydium AMM | $906.27K |
| fomo Wallet | $905.21K |
| Meteora DLMM | $827.24K |
| StonkFun | $588.47K |
| Collector Crypt | $513.46K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $89.43M |
| xStocks holder positions | 547.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $546.49M |

## Program activity and chain health

Chain tip lag: **+12.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 66,709 (approx.) | 33.90% | 0.6 s |
| Pump.fun | 8,564 | 59.60% | 6.6 s |
| Jupiter v6 | 8,100 | 77.70% | 7.3 s |
| Orca Whirlpools | 5,756 | 50.90% | 10.1 s |
| Raydium AMM v4 | 2,875 | 21.90% | 20.6 s |

Median failure rate across the sampled programs: **50.90%** (range 21.90% to 77.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.37 SOL**.

## Exchange and large-holder balances

11.71M SOL ($1.15B) across 8 publicly-attributed accounts. Net **63K SOL (0.54%) moved onto exchanges** over the last 23.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $904.60M | 0.3/h | 1 |
| Binance (2) | 1.90M | $186.88M | 1.1K/h | 0 |
| Gate.io | 271.03K | $26.68M | 193.9/h | 0 |
| Bybit | 232.08K | $22.85M | 41.6/h | 0 |
| Kraken | 39.00K | $3.84M | 297.5/h | 0 |
| Bitget | 38.03K | $3.74M | 246.6/h | 0 |
| Coinbase (2) | 24.45K | $2.41M | 481.9/h | 0 |
| Coinbase | 14.89K | $1.47M | 935.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 830 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.203 | 789 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.196 | 796 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.164 | 755 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.162 | 755 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 796 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.149 | 777 | 0.0000 |
| Total TPS moves with Program failure rate | +0.148 | 777 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.120 | 755 | 0.0009 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 98.45 USD | Jupiter (on-chain DEX): 98.03 USD | +0.43% | agree |
| Circulating supply | getSupply (RPC): 587.03M SOL | CoinGecko: 587.03M SOL | -0.00% | agree |

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

**Latest Firedancer release:** [v26.08.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.4) (2026-09-10)

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
