# Solana Ecosystem Report

*Generated 2026-09-21 02:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.5K |
| TPS (non-vote) | 2.0K |
| Slot time | 268.5 ms |
| Slot | 449M |
| Block height | 427M |
| Epoch | 1039 (15.83% complete, ~27.1h remaining) |
| Lifetime transactions | 550.8B |
| Circulating supply | 587.4M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 38.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 14 |
| Delinquent stake | 0.04% |
| Total active stake | 439.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.27% / 35.62% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 23.89% |

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
| SOL price | $111.33 (+0.90% 24h) |
| Market cap | $65.36B (rank #7) |
| 24h volume | $3.58B |
| ATH | $293.31 (-62.04% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.19B |
| Stablecoin supply | $15.60B |
| DEX volume (24h) | $2.75B (-4.29% 1d) |
| App fees (24h, all protocols) | $14.41M |
| Chain fees (24h) | $826.27K |
| Jito MEV tips (24h) | $149.20K |
| **REV - Real Economic Value (24h)** | **$975.47K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.06B | -1.97% |
| USDT | $2.11B | -14.88% |
| USDGO | $1.38B | +0.07% |
| USD1 | $1.33B | +1.91% |
| BUIDL | $993.18M | +0.06% |
| PYUSD | $734.93M | +3.86% |
| USDG | $631.01M | +5.23% |
| USDe | $508.95M | -4.48% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $482.79M |
| BisonFi | $386.77M |
| Raydium AMM | $297.81M |
| Orca DEX | $244.13M |
| HumidiFi | $228.88M |
| Meteora DLMM | $191.78M |
| Tessera V | $142.16M |
| fomo Wallet | $116.87M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.25M |
| Axiom | $1.70M |
| pump.fun | $1.44M |
| Meteora DLMM | $991.06K |
| Raydium AMM | $960.98K |
| StonkFun | $819.17K |
| Collector Crypt | $569.99K |
| LaunchLab | $521.93K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $83.09M |
| xStocks holder positions | 576.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $580.25M |

## Program activity and chain health

Chain tip lag: **+9.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 64,134 (approx.) | 20.50% | 0.5 s |
| Pump.fun | 6,201 | 47.70% | 9.7 s |
| Orca Whirlpools | 5,678 | 32.60% | 10.5 s |
| Jupiter v6 | 5,063 | 63.70% | 11.8 s |
| Raydium AMM v4 | 4,756 | 25.30% | 12.4 s |

Median failure rate across the sampled programs: **32.60%** (range 20.50% to 63.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **648.12 SOL**.

## Exchange and large-holder balances

11.89M SOL ($1.32B) across 8 publicly-attributed accounts. Net **5K SOL (0.04%) moved onto exchanges** over the last 18.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.11B | 0.2/h | 0 |
| Binance (2) | 1.23M | $136.88M | 821.9/h | 0 |
| Gate.io | 269.58K | $30.01M | 149.1/h | 7 |
| Bybit | 251.40K | $27.99M | 34.4/h | 0 |
| Coinbase | 94.83K | $10.56M | 373.8/h | 0 |
| Bitget | 54.19K | $6.03M | 154.7/h | 0 |
| Kraken | 32.09K | $3.57M | 196.1/h | 0 |
| Coinbase (2) | 14.76K | $1.64M | 355.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 867 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.221 | 826 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.207 | 833 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.180 | 792 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.176 | 792 | 0.0000 |
| Total TPS moves with Slot time | +0.166 | 833 | 0.0000 |
| Total TPS moves with Program failure rate | +0.154 | 814 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.152 | 814 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.126 | 792 | 0.0004 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with DeFi TVL | +0.103 | 867 | 0.0025 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 111.33 USD | Jupiter (on-chain DEX): 111.46 USD | -0.12% | agree |
| Circulating supply | getSupply (RPC): 587.44M SOL | CoinGecko: 587.44M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-18
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-17
- [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-20
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

- **[ZetaChain votes to shut down Layer 1 network and move ZETA to Solana](https://www.theblock.co/news/defi/2026-09-20-zetachain-votes-to-shut-down-layer-1-network-and-move-zeta-to-solana-415878)** - The Block, 2026-09-20
- **[Solana's Heartbeat Quickens: Block Times Fall 17% in Latest Speed Upgrade](https://decrypt.co/378674/solana-heartbeat-quickens-speed-upgrade)** - Decrypt, 2026-09-19
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Bitcoin reclaims $80,000, Solana and Hyperliquid rally as crypto markets shrug off Clarity setback](https://www.theblock.co/news/markets/2026-09-18-bitcoin-reclaims-80000-solana-hyperliquid-rally-crypto-markets-shrug-off-clarity-setback-415523)** - The Block, 2026-09-18
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)** - Solana.com, 2026-09-10
- **[Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)** - Solana.com, 2026-09-10
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
