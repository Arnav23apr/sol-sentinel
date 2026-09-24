# Solana Ecosystem Report

*Generated 2026-09-24 12:23 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 1.5K |
| Slot time | 264.9 ms |
| Slot | 450M |
| Block height | 428M |
| Epoch | 1041 (73.11% complete, ~8.5h remaining) |
| Lifetime transactions | 552.1B |
| Circulating supply | 587.6M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 22.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 673 |
| Delinquent validators | 13 |
| Delinquent stake | 0.09% |
| Total active stake | 439.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.40% / 35.69% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.79% |

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
| SOL price | $113.51 (-2.85% 24h) |
| Market cap | $66.69B (rank #7) |
| 24h volume | $4.61B |
| ATH | $293.31 (-61.30% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.33B |
| Stablecoin supply | $16.12B |
| DEX volume (24h) | $2.55B (-20.10% 1d) |
| App fees (24h, all protocols) | $16.48M |
| Chain fees (24h) | $1.01M |
| Jito MEV tips (24h) | $217.34K |
| **REV - Real Economic Value (24h)** | **$1.23M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.48B | +11.66% |
| USDT | $2.13B | -8.95% |
| USDGO | $1.42B | +2.98% |
| USD1 | $1.38B | +4.48% |
| BUIDL | $987.68M | -0.55% |
| PYUSD | $734.92M | +2.19% |
| USDG | $632.11M | +1.21% |
| USDe | $496.89M | -5.11% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $347.44M |
| Raydium AMM | $343.50M |
| BisonFi | $323.94M |
| PumpSwap | $270.19M |
| Meteora DLMM | $233.66M |
| fomo Wallet | $118.88M |
| pump.fun | $115.24M |
| Scorch | $113.00M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| Axiom | $1.82M |
| pump.fun | $1.59M |
| Raydium AMM | $1.03M |
| Meteora DLMM | $978.23K |
| StonkFun | $958.37K |
| fomo Wallet | $841.44K |
| LaunchLab | $644.87K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $149.89M |
| xStocks holder positions | 624.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $543.26M |

## Program activity and chain health

Chain tip lag: **+10.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 45,413 | 30.60% | 1.1 s |
| Jupiter v6 | 7,160 | 77.70% | 8.2 s |
| Orca Whirlpools | 5,638 | 73.10% | 9.8 s |
| Pump.fun | 5,595 | 37.60% | 10.6 s |
| Raydium AMM v4 | 1,005 | 20.80% | 59.6 s |

Median failure rate across the sampled programs: **37.60%** (range 20.80% to 77.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.40 SOL**.

## Exchange and large-holder balances

11.79M SOL ($1.34B) across 8 publicly-attributed accounts. Net **13K SOL (0.11%) moved off exchanges** over the last 19.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.13B | 0.3/h | 0 |
| Binance (2) | 1.21M | $137.72M | 1.4K/h | 1 |
| Gate.io | 258.81K | $29.38M | 230.8/h | 3 |
| Bybit | 235.36K | $26.72M | 59.4/h | 0 |
| Kraken | 55.34K | $6.28M | 288.2/h | 0 |
| Coinbase (2) | 40.90K | $4.64M | 305.9/h | 0 |
| Bitget | 20.58K | $2.34M | 274.4/h | 0 |
| Coinbase | 17.88K | $2.03M | 329.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 886 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.244 | 845 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.212 | 852 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.196 | 811 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.191 | 811 | 0.0000 |
| Total TPS moves with Slot time | +0.172 | 852 | 0.0000 |
| Total TPS moves with Program failure rate | +0.157 | 833 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.155 | 833 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.136 | 811 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with DeFi TVL | +0.117 | 886 | 0.0005 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 113.51 USD | Jupiter (on-chain DEX): 113.60 USD | -0.08% | agree |
| Circulating supply | getSupply (RPC): 587.58M SOL | CoinGecko: 587.58M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - *open*, updated 2026-09-23
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-24
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
