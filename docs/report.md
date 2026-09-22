# Solana Ecosystem Report

*Generated 2026-09-22 01:39 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 7.0 robust standard deviations above its 7-day baseline: a 8.5% move to 16,873,785,216.00 USD from a typical 15,556,207,419.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.2K |
| Slot time | 266.1 ms |
| Slot | 449M |
| Block height | 427M |
| Epoch | 1039 (89.09% complete, ~3.5h remaining) |
| Lifetime transactions | 551.2B |
| Circulating supply | 587.4M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 26.70% of slots needed a priority fee (max 3.5M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 14 |
| Delinquent stake | 0.04% |
| Total active stake | 439.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.27% / 35.62% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 23.90% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.9M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.3M | 2.56% | 5% |
| 5 | `8Gbw…F8iD` | 9.8M | 2.23% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.1M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.69% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $117.90 (+5.18% 24h) |
| Market cap | $69.26B (rank #7) |
| 24h volume | $6.70B |
| ATH | $293.31 (-59.80% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.52B |
| Stablecoin supply | $16.87B |
| DEX volume (24h) | $3.37B (+20.57% 1d) |
| App fees (24h, all protocols) | $17.59M |
| Chain fees (24h) | $1.10M |
| Jito MEV tips (24h) | $235.55K |
| **REV - Real Economic Value (24h)** | **$1.33M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $8.29B | +15.04% |
| USDT | $2.13B | -14.08% |
| USDGO | $1.40B | +0.86% |
| USD1 | $1.35B | +2.27% |
| BUIDL | $993.48M | +0.06% |
| PYUSD | $731.52M | +4.13% |
| USDG | $620.69M | +1.10% |
| USDe | $502.03M | -5.05% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $577.99M |
| Orca DEX | $444.69M |
| BisonFi | $424.26M |
| PumpSwap | $390.12M |
| Meteora DLMM | $259.61M |
| HumidiFi | $253.12M |
| fomo Wallet | $156.81M |
| Manifest Trade | $141.18M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.36M |
| Axiom | $2.30M |
| Raydium AMM | $2.00M |
| pump.fun | $1.73M |
| Meteora DLMM | $1.28M |
| StonkFun | $1.11M |
| LaunchLab | $833.21K |
| Orca DEX | $677.98K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $223.58M |
| xStocks holder positions | 600.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $553.43M |

## Program activity and chain health

Chain tip lag: **+10.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 45,490 | 28.60% | 1.1 s |
| Orca Whirlpools | 11,535 | 41.00% | 5.1 s |
| Jupiter v6 | 6,346 | 71.90% | 9.3 s |
| Pump.fun | 5,677 | 57.40% | 10.4 s |
| Raydium AMM v4 | 1,777 | 25.00% | 33.5 s |

Median failure rate across the sampled programs: **41.00%** (range 25.00% to 71.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **137.39 SOL**.

## Exchange and large-holder balances

11.98M SOL ($1.41B) across 8 publicly-attributed accounts. Net **87K SOL (0.73%) moved onto exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.17B | 0.2/h | 0 |
| Binance (2) | 1.33M | $156.47M | 823.8/h | 0 |
| Gate.io | 299.92K | $35.36M | 558.1/h | 3 |
| Bybit | 258.25K | $30.45M | 108.6/h | 0 |
| Coinbase | 45.04K | $5.31M | 410.5/h | 0 |
| Kraken | 35.44K | $4.18M | 263.7/h | 0 |
| Coinbase (2) | 33.80K | $3.99M | 399.1/h | 0 |
| Bitget | 33.56K | $3.96M | 215.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 872 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.232 | 831 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.210 | 838 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.187 | 797 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.183 | 797 | 0.0000 |
| Total TPS moves with Slot time | +0.170 | 838 | 0.0000 |
| Total TPS moves with Program failure rate | +0.157 | 819 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.155 | 819 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.130 | 797 | 0.0002 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with DeFi TVL | +0.105 | 872 | 0.0018 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 117.90 USD | Jupiter (on-chain DEX): 117.68 USD | +0.19% | agree |
| Circulating supply | getSupply (RPC): 587.44M SOL | CoinGecko: 587.44M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-21
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-22
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-21
- [SIMD-0649: Priority Ordering Within Entry Batches](https://github.com/solana-foundation/solana-improvement-documents/pull/649) - updated 2026-09-21
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-21
- [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-20

**Recently merged SIMDs:**

- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10

**Latest Agave release:** [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) (2026-09-18)

**Latest Firedancer release:** [v0.1204.40300](https://github.com/firedancer-io/firedancer/releases/tag/v0.1204.40300) (2026-09-21)

## Ecosystem news

- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[ZetaChain votes to shut down Layer 1 network and move ZETA to Solana](https://www.theblock.co/news/defi/2026-09-20-zetachain-votes-to-shut-down-layer-1-network-and-move-zeta-to-solana-415878)** - The Block, 2026-09-20
- **[Solana's Heartbeat Quickens: Block Times Fall 17% in Latest Speed Upgrade](https://decrypt.co/378674/solana-heartbeat-quickens-speed-upgrade)** - Decrypt, 2026-09-19
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Bitcoin reclaims $80,000, Solana and Hyperliquid rally as crypto markets shrug off Clarity setback](https://www.theblock.co/news/markets/2026-09-18-bitcoin-reclaims-80000-solana-hyperliquid-rally-crypto-markets-shrug-off-clarity-setback-415523)** - The Block, 2026-09-18
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)** - Solana.com, 2026-09-10
- **[Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)** - Solana.com, 2026-09-10

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
