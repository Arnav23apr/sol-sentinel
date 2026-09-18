# Solana Ecosystem Report

*Generated 2026-09-18 23:24 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 6.7 robust standard deviations above its 7-day baseline: a 11.6% move to 113.20 USD from a typical 101.40.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 8.3 robust standard deviations above its 7-day baseline: a 7.0% move to 6,286,658,066.00 USD from a typical 5,873,248,128.00.
- 🟠 **SOL price move** (warning): SOL moved +11.5% in 24h.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.1K |
| Slot time | 264.3 ms |
| Slot | 448M |
| Block height | 426M |
| Epoch | 1037 (57.14% complete, ~13.6h remaining) |
| Lifetime transactions | 550.0B |
| Circulating supply | 587.3M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 28.00% of slots needed a priority fee (max 4.4M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 11 |
| Delinquent stake | 0.04% |
| Total active stake | 439.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.32% / 24.28% / 35.59% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 23.86% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.05% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.8M | 2.23% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.1M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.68% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $113.20 (+11.54% 24h) |
| Market cap | $66.49B (rank #7) |
| 24h volume | $6.65B |
| ATH | $293.31 (-61.41% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.29B |
| Stablecoin supply | $15.45B |
| DEX volume (24h) | $2.59B (-7.41% 1d) |
| App fees (24h, all protocols) | $14.68M |
| Chain fees (24h) | $813.11K |
| Jito MEV tips (24h) | $193.72K |
| **REV - Real Economic Value (24h)** | **$1.01M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.02B | +0.46% |
| USDT | $2.11B | -20.93% |
| USDGO | $1.38B | +0.06% |
| USD1 | $1.33B | +3.61% |
| BUIDL | $993.18M | +0.07% |
| PYUSD | $728.12M | -2.50% |
| USDG | $623.14M | +4.00% |
| USDe | $520.39M | -3.02% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $420.24M |
| BisonFi | $378.33M |
| PumpSwap | $329.29M |
| HumidiFi | $281.64M |
| Orca DEX | $235.25M |
| fomo Wallet | $177.97M |
| Meteora DLMM | $177.93M |
| Tessera V | $168.27M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.81M |
| Axiom | $1.70M |
| pump.fun | $1.65M |
| Raydium AMM | $1.50M |
| fomo Wallet | $1.12M |
| Meteora DLMM | $827.23K |
| StonkFun | $625.65K |
| BONK.fun Launchpad | $450.06K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $119.39M |
| xStocks holder positions | 552.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $576.93M |

## Program activity and chain health

Chain tip lag: **+9.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,899 | 48.60% | 0.8 s |
| Orca Whirlpools | 8,653 | 69.20% | 6.9 s |
| Jupiter v6 | 6,853 | 76.10% | 8.5 s |
| Pump.fun | 5,319 | 43.90% | 11.1 s |
| Raydium AMM v4 | 4,820 | 46.30% | 12.4 s |

Median failure rate across the sampled programs: **48.60%** (range 43.90% to 76.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.38 SOL**.

## Exchange and large-holder balances

11.74M SOL ($1.33B) across 7 publicly-attributed accounts. Net **49K SOL (0.41%) moved off exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $1.04B | 0.2/h | 0 |
| Binance (2) | 1.98M | $224.63M | 1.3K/h | 0 |
| Gate.io | 243.85K | $27.60M | 131.6/h | 0 |
| Bybit | 235.08K | $26.61M | 29.3/h | 0 |
| Bitget | 32.39K | $3.67M | 144.8/h | 0 |
| Coinbase | 31.82K | $3.60M | 566.9/h | 0 |
| Kraken | 28.76K | $3.26M | 276.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 851 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.205 | 817 | 0.0000 |
| DEX volume moves with App fees | +0.202 | 810 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.166 | 776 | 0.0000 |
| Total TPS moves with Slot time | +0.164 | 817 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.161 | 776 | 0.0000 |
| Total TPS moves with Program failure rate | +0.152 | 798 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.149 | 798 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.120 | 776 | 0.0008 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 113.20 USD | Jupiter (on-chain DEX): 113.08 USD | +0.11% | agree |
| Circulating supply | getSupply (RPC): 587.30M SOL | CoinGecko: 587.30M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-18
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-18
- [amend SIMD-0558: fix CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/644) - updated 2026-09-18
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-09-18
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - updated 2026-09-16

**Recently merged SIMDs:**

- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10

**Latest Agave release:** [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) (2026-09-18)

**Latest Firedancer release:** [v26.09.3](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.3) (2026-09-16)

## Ecosystem news

- **[Bitcoin reclaims $80,000, Solana and Hyperliquid rally as crypto markets shrug off Clarity setback](https://www.theblock.co/news/markets/2026-09-18-bitcoin-reclaims-80000-solana-hyperliquid-rally-crypto-markets-shrug-off-clarity-setback-415523)** - The Block, 2026-09-18
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)** - Solana.com, 2026-09-10
- **[Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)** - Solana.com, 2026-09-10
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
