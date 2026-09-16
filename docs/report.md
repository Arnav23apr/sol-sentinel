# Solana Ecosystem Report

*Generated 2026-09-16 18:57 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 4.5 robust standard deviations below its 7-day baseline: a 3.9% move to 15,479,262,121.00 USD from a typical 16,105,960,644.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.1K |
| TPS (non-vote) | 3.0K |
| Slot time | 315 ms |
| Slot | 448M |
| Block height | 426M |
| Epoch | 1036 (10.24% complete, ~33.9h remaining) |
| Lifetime transactions | 549.1B |
| Circulating supply | 587.2M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 36.70% of slots needed a priority fee (max 25.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 14 |
| Delinquent stake | 0.04% |
| Total active stake | 439.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.35% / 35.66% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.88% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 16.4M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.7M | 2.22% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $97.74 (-0.32% 24h) |
| Market cap | $57.42B (rank #7) |
| 24h volume | $3.59B |
| ATH | $293.31 (-66.68% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.71B |
| Stablecoin supply | $15.48B |
| DEX volume (24h) | $2.70B (+6.84% 1d) |
| App fees (24h, all protocols) | $14.08M |
| Chain fees (24h) | $693.21K |
| Jito MEV tips (24h) | $162.52K |
| **REV - Real Economic Value (24h)** | **$855.73K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.74B | -6.05% |
| USDT | $2.34B | -15.19% |
| USDGO | $1.38B | +0.83% |
| USD1 | $1.32B | +2.83% |
| BUIDL | $993.19M | +0.57% |
| PYUSD | $704.13M | -6.37% |
| USDG | $612.69M | +3.74% |
| USDe | $523.88M | -2.27% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $519.33M |
| BisonFi | $353.62M |
| HumidiFi | $232.02M |
| fomo Wallet | $226.51M |
| Raydium AMM | $199.75M |
| Orca DEX | $196.98M |
| Tessera V | $171.07M |
| Meteora DLMM | $168.53M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.20M |
| pump.fun | $1.59M |
| Axiom | $1.30M |
| Raydium AMM | $817.75K |
| Meteora DLMM | $811.23K |
| fomo Wallet | $645.93K |
| Collector Crypt | $481.42K |
| Jupiter Perpetual Exchange | $376.58K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $61.92M |
| xStocks holder positions | 534.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $561.51M |

## Program activity and chain health

Chain tip lag: **+11.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 56,571 | 31.80% | 0.9 s |
| Jupiter v6 | 27,079 | 85.80% | 1.9 s |
| Pump.fun | 13,034 | 79.40% | 4.4 s |
| Orca Whirlpools | 6,509 | 59.90% | 9.1 s |
| Raydium AMM v4 | 1,909 | 25.90% | 31.2 s |

Median failure rate across the sampled programs: **59.90%** (range 25.90% to 85.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **467.27 SOL**.

## Exchange and large-holder balances

11.89M SOL ($1.16B) across 8 publicly-attributed accounts. Net **182K SOL (1.56%) moved onto exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $898.08M | 0.3/h | 1 |
| Binance (2) | 1.98M | $193.18M | 1.1K/h | 0 |
| Gate.io | 272.04K | $26.59M | 181.6/h | 0 |
| Bybit | 232.95K | $22.77M | 26.9/h | 0 |
| Coinbase (2) | 93.65K | $9.15M | 404.5/h | 0 |
| Bitget | 72.76K | $7.11M | 214.4/h | 0 |
| Kraken | 30.70K | $3.00M | 271.5/h | 0 |
| Coinbase | 21.42K | $2.09M | 519.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 836 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.205 | 795 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.198 | 802 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.163 | 761 | 0.0000 |
| Total TPS moves with Slot time | +0.161 | 802 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.161 | 761 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.149 | 783 | 0.0000 |
| Total TPS moves with Program failure rate | +0.148 | 783 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| Slot time moves with AMM write-lock congestion | +0.116 | 761 | 0.0014 |
| AMM write-lock congestion moves with Program failure rate | +0.107 | 761 | 0.0033 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 97.74 USD | Jupiter (on-chain DEX): 97.74 USD | 0.00% | agree |
| Circulating supply | getSupply (RPC): 587.15M SOL | CoinGecko: 587.15M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-16
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [Sync SIMD statuses and feature keys with mainnet activations (55 SIMDs)](https://github.com/solana-foundation/solana-improvement-documents/pull/638) - updated 2026-09-14
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-16
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-11
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20

**Recently merged SIMDs:**

- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10

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
