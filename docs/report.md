# Solana Ecosystem Report

*Generated 2026-09-20 07:49 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.8K |
| TPS (non-vote) | 1.3K |
| Slot time | 264.9 ms |
| Slot | 449M |
| Block height | 427M |
| Epoch | 1038 (58.50% complete, ~13.2h remaining) |
| Lifetime transactions | 550.5B |
| Circulating supply | 587.4M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 16.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 678 |
| Delinquent validators | 12 |
| Delinquent stake | 0.01% |
| Total active stake | 440.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.27% / 35.65% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 23.92% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.05% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.59% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.84% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.58% | 5% |
| 5 | `8Gbw…F8iD` | 9.8M | 2.22% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.1M | 2.07% | 10% |
| 8 | `9QU2…29mF` | 7.4M | 1.69% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `HZKo…SpEc` | 6.6M | 1.51% | 100% |

## Market

| Metric | Value |
|---|---|
| SOL price | $108.55 (-2.78% 24h) |
| Market cap | $63.75B (rank #7) |
| 24h volume | $2.96B |
| ATH | $293.31 (-62.99% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.13B |
| Stablecoin supply | $15.51B |
| DEX volume (24h) | $3.23B (-8.58% 1d) |
| App fees (24h, all protocols) | $15.22M |
| Chain fees (24h) | $826.27K |
| Jito MEV tips (24h) | $145.18K |
| **REV - Real Economic Value (24h)** | **$971.45K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.97B | -4.47% |
| USDT | $2.11B | -16.89% |
| USDGO | $1.38B | +0.07% |
| USD1 | $1.33B | +1.91% |
| BUIDL | $993.18M | +0.06% |
| PYUSD | $733.13M | +3.87% |
| USDG | $629.64M | +4.36% |
| USDe | $510.62M | -4.59% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $606.41M |
| BisonFi | $532.67M |
| HumidiFi | $334.93M |
| Raydium AMM | $304.14M |
| Orca DEX | $213.53M |
| Tessera V | $205.65M |
| Meteora DLMM | $167.03M |
| QuantumAMM | $143.62M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.45M |
| Axiom | $2.15M |
| pump.fun | $1.48M |
| Raydium AMM | $1.02M |
| StonkFun | $883.06K |
| Meteora DLMM | $734.76K |
| fomo Wallet | $539.22K |
| LaunchLab | $521.92K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $96.90M |
| xStocks holder positions | 569.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $580.48M |

## Program activity and chain health

Chain tip lag: **+9.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 40,815 | 9.60% | 1.3 s |
| Pump.fun | 10,234 | 71.70% | 5.8 s |
| Jupiter v6 | 3,279 | 55.30% | 17.2 s |
| Orca Whirlpools | 1,748 | 25.00% | 32.1 s |
| Raydium AMM v4 | 1,190 | 36.20% | 50.3 s |

Median failure rate across the sampled programs: **36.20%** (range 9.60% to 71.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **208.09 SOL**.

## Exchange and large-holder balances

11.88M SOL ($1.29B) across 8 publicly-attributed accounts. Net **15K SOL (0.13%) moved onto exchanges** over the last 20.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.08B | 0.2/h | 0 |
| Binance (2) | 1.33M | $144.63M | 835.3/h | 0 |
| Gate.io | 258.82K | $28.09M | 176.2/h | 5 |
| Bybit | 243.90K | $26.48M | 21/h | 0 |
| Kraken | 34.03K | $3.69M | 146.1/h | 0 |
| Bitget | 31.56K | $3.43M | 214.4/h | 0 |
| Coinbase | 20.29K | $2.20M | 400.4/h | 0 |
| Coinbase (2) | 20.07K | $2.18M | 183.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 861 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.214 | 820 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.207 | 827 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.177 | 786 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.172 | 786 | 0.0000 |
| Total TPS moves with Slot time | +0.167 | 827 | 0.0000 |
| Total TPS moves with Program failure rate | +0.149 | 808 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.146 | 808 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.122 | 786 | 0.0006 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with DeFi TVL | +0.103 | 861 | 0.0025 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 108.55 USD | Jupiter (on-chain DEX): 108.42 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 587.37M SOL | CoinGecko: 587.37M SOL | -0.00% | agree |

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

- **[Solana's Heartbeat Quickens: Block Times Fall 17% in Latest Speed Upgrade](https://decrypt.co/378674/solana-heartbeat-quickens-speed-upgrade)** - Decrypt, 2026-09-19
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Bitcoin reclaims $80,000, Solana and Hyperliquid rally as crypto markets shrug off Clarity setback](https://www.theblock.co/news/markets/2026-09-18-bitcoin-reclaims-80000-solana-hyperliquid-rally-crypto-markets-shrug-off-clarity-setback-415523)** - The Block, 2026-09-18
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)** - Solana.com, 2026-09-10
- **[Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)** - Solana.com, 2026-09-10
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
