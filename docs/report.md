# Solana Ecosystem Report

*Generated 2026-09-23 17:18 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.6K |
| TPS (non-vote) | 2.1K |
| Slot time | 265.5 ms |
| Slot | 450M |
| Block height | 428M |
| Epoch | 1041 (13.14% complete, ~27.7h remaining) |
| Lifetime transactions | 551.8B |
| Circulating supply | 587.6M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 38.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 12 |
| Delinquent stake | 0.05% |
| Total active stake | 439.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.40% / 35.68% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.77% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.81% | 0% |
| 4 | `Catz…Diqb` | 11.3M | 2.56% | 5% |
| 5 | `8Gbw…F8iD` | 10.3M | 2.35% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.08% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $113.72 (-3.20% 24h) |
| Market cap | $66.80B (rank #7) |
| 24h volume | $5.31B |
| ATH | $293.31 (-61.23% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.40B |
| Stablecoin supply | $15.93B |
| DEX volume (24h) | $3.20B (-6.82% 1d) |
| App fees (24h, all protocols) | $17.87M |
| Chain fees (24h) | $1.10M |
| Jito MEV tips (24h) | $255.89K |
| **REV - Real Economic Value (24h)** | **$1.35M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.29B | +7.69% |
| USDT | $2.14B | -14.08% |
| USDGO | $1.42B | +2.98% |
| USD1 | $1.37B | +3.72% |
| BUIDL | $987.68M | -0.54% |
| PYUSD | $734.48M | +2.60% |
| USDG | $630.91M | +3.05% |
| USDe | $498.31M | -5.61% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $634.15M |
| Raydium AMM | $396.04M |
| BisonFi | $368.17M |
| Orca DEX | $365.06M |
| Meteora DLMM | $266.83M |
| fomo Wallet | $156.29M |
| Scorch | $129.41M |
| Manifest Trade | $129.19M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.40M |
| Axiom | $2.00M |
| pump.fun | $1.75M |
| Raydium AMM | $1.29M |
| StonkFun | $1.27M |
| Meteora DLMM | $982.20K |
| fomo Wallet | $864.67K |
| LaunchLab | $764.56K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $136.91M |
| xStocks holder positions | 615.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $544.64M |

## Program activity and chain health

Chain tip lag: **+10.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 75,367 (approx.) | 36.70% | 0.5 s |
| Pump.fun | 13,254 | 67.90% | 4.5 s |
| Jupiter v6 | 12,354 | 77.30% | 4.8 s |
| Raydium AMM v4 | 7,504 | 49.40% | 7.7 s |
| Orca Whirlpools | 7,367 | 48.90% | 8 s |

Median failure rate across the sampled programs: **49.40%** (range 36.70% to 77.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.40 SOL**.

## Exchange and large-holder balances

11.80M SOL ($1.34B) across 8 publicly-attributed accounts. Net **336K SOL (2.77%) moved off exchanges** over the last 21.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.13B | 0.2/h | 0 |
| Binance (2) | 1.23M | $139.99M | 1.2K/h | 0 |
| Gate.io | 259.22K | $29.48M | 245.7/h | 3 |
| Bybit | 241.12K | $27.42M | 65.8/h | 0 |
| Bitget | 43.78K | $4.98M | 284.6/h | 0 |
| Kraken | 38.67K | $4.40M | 255/h | 0 |
| Coinbase (2) | 26.50K | $3.01M | 459.8/h | 0 |
| Coinbase | 15.02K | $1.71M | 796.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 881 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.231 | 840 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.210 | 847 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.195 | 806 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.191 | 806 | 0.0000 |
| Total TPS moves with Slot time | +0.171 | 847 | 0.0000 |
| Total TPS moves with Program failure rate | +0.158 | 828 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.156 | 828 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.130 | 806 | 0.0002 |
| SOL price moves with DeFi TVL | +0.120 | 881 | 0.0004 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.102 | 806 | 0.0039 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 113.72 USD | Jupiter (on-chain DEX): 114.21 USD | -0.43% | agree |
| Circulating supply | getSupply (RPC): 587.58M SOL | CoinGecko: 587.58M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - *open*, updated 2026-09-23
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-23
- [Fix broken markdown, stale references and typos across several SIMDs](https://github.com/solana-foundation/solana-improvement-documents/pull/668) - updated 2026-09-22
- [SIMD-0385 / 0388 / 0204: fix inconsistent field and constant names](https://github.com/solana-foundation/solana-improvement-documents/pull/666) - updated 2026-09-22
- [Fix dead links in SIMD-0118, 0153, 0183, 0204, 0266, 0553](https://github.com/solana-foundation/solana-improvement-documents/pull/665) - updated 2026-09-22
- [SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23

**Recently merged SIMDs:**

- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10

**Latest Agave release:** [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) (2026-09-18)

**Latest Firedancer release:** [v26.09.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.4) (2026-09-22)

## Ecosystem news

- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)** - Solana.com, 2026-09-10
- **[Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)** - Solana.com, 2026-09-10
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
