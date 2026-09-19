# Solana Ecosystem Report

*Generated 2026-09-19 06:05 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DeFi TVL** (critical): DeFi TVL is 7.6 robust standard deviations above its 7-day baseline: a 7.4% move to 6,305,117,589.00 USD from a typical 5,873,248,128.00.
- 🟠 **App fees (24h, all protocols)** (warning): App fees (24h, all protocols) is 5.1 robust standard deviations above its 7-day baseline: a 27.2% move to 17,919,631.00 USD from a typical 14,083,156.00.
- 🟠 **SOL price** (warning): SOL price is 5.3 robust standard deviations above its 7-day baseline: a 10.4% move to 111.91 USD from a typical 101.40.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 1.5K |
| Slot time | 267.3 ms |
| Slot | 448M |
| Block height | 426M |
| Epoch | 1037 (78.08% complete, ~7.0h remaining) |
| Lifetime transactions | 550.1B |
| Circulating supply | 587.3M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 56.00% of slots needed a priority fee (max 7.6M µlam/CU) |
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
| SOL price | $111.91 (+6.03% 24h) |
| Market cap | $65.77B (rank #7) |
| 24h volume | $5.88B |
| ATH | $293.31 (-61.85% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.31B |
| Stablecoin supply | $15.54B |
| DEX volume (24h) | $3.26B (+25.68% 1d) |
| App fees (24h, all protocols) | $17.92M |
| Chain fees (24h) | $965.96K |
| Jito MEV tips (24h) | $193.78K |
| **REV - Real Economic Value (24h)** | **$1.16M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.00B | -4.17% |
| USDT | $2.11B | -19.11% |
| USDGO | $1.38B | +0.07% |
| USD1 | $1.33B | +2.07% |
| BUIDL | $993.18M | +0.06% |
| PYUSD | $727.46M | +2.67% |
| USDG | $625.17M | +3.93% |
| USDe | $518.85M | -3.19% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $488.34M |
| Raydium AMM | $403.42M |
| BisonFi | $378.33M |
| Orca DEX | $338.33M |
| HumidiFi | $281.64M |
| Meteora DLMM | $239.38M |
| fomo Wallet | $174.89M |
| Manifest Trade | $168.98M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.75M |
| Axiom | $2.08M |
| pump.fun | $1.67M |
| Raydium AMM | $1.37M |
| StonkFun | $1.16M |
| fomo Wallet | $1.12M |
| Meteora DLMM | $986.14K |
| LaunchLab | $592.47K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $119.60M |
| xStocks holder positions | 554.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $577.31M |

## Program activity and chain health

Chain tip lag: **+9.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,579 | 39.10% | 0.8 s |
| Jupiter v6 | 6,510 | 72.50% | 8.8 s |
| Pump.fun | 6,148 | 64.60% | 9.6 s |
| Orca Whirlpools | 5,744 | 63.60% | 10.4 s |
| Raydium AMM v4 | 1,495 | 29.40% | 40.1 s |

Median failure rate across the sampled programs: **63.60%** (range 29.40% to 72.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.38 SOL**.

## Exchange and large-holder balances

11.81M SOL ($1.32B) across 8 publicly-attributed accounts. Net **19K SOL (0.16%) moved onto exchanges** over the last 18.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $1.03B | 0.2/h | 0 |
| Binance (2) | 2.01M | $224.65M | 1.1K/h | 0 |
| Gate.io | 240.82K | $26.95M | 146.5/h | 0 |
| Bybit | 235.08K | $26.31M | 23.7/h | 0 |
| Kraken | 35.81K | $4.01M | 105.7/h | 0 |
| Bitget | 33.14K | $3.71M | 124.4/h | 0 |
| Coinbase | 32.40K | $3.63M | 297.3/h | 0 |
| Coinbase (2) | 32.35K | $3.62M | 317.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 10 of 117 tested pairs survive, over 853 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.212 | 812 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.203 | 819 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.168 | 778 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.163 | 778 | 0.0000 |
| Total TPS moves with Slot time | +0.162 | 819 | 0.0000 |
| Total TPS moves with Program failure rate | +0.151 | 800 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.148 | 800 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.118 | 778 | 0.0010 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 111.91 USD | Jupiter (on-chain DEX): 111.98 USD | -0.06% | agree |
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
- [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-19
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
