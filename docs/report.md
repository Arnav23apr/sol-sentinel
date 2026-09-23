# Solana Ecosystem Report

*Generated 2026-09-23 06:54 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

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
| Epoch | 1040 (80.48% complete, ~6.2h remaining) |
| Lifetime transactions | 551.6B |
| Circulating supply | 587.5M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 16.00% of slots needed a priority fee (max 1.4M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 12 |
| Delinquent stake | 0.04% |
| Total active stake | 439.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.35% / 24.33% / 35.64% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.82% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.05% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.81% | 0% |
| 4 | `Catz…Diqb` | 11.3M | 2.56% | 5% |
| 5 | `8Gbw…F8iD` | 10.2M | 2.32% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.1M | 2.08% | 10% |
| 8 | `9QU2…29mF` | 7.5M | 1.70% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $118.96 (+1.96% 24h) |
| Market cap | $69.89B (rank #7) |
| 24h volume | $4.28B |
| ATH | $293.31 (-59.44% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.55B |
| Stablecoin supply | $16.14B |
| DEX volume (24h) | $3.45B (+0.59% 1d) |
| App fees (24h, all protocols) | $17.84M |
| Chain fees (24h) | $1.10M |
| Jito MEV tips (24h) | $259.30K |
| **REV - Real Economic Value (24h)** | **$1.36M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.51B | +10.88% |
| USDT | $2.14B | -14.08% |
| USDGO | $1.41B | +2.69% |
| USD1 | $1.37B | +3.72% |
| BUIDL | $987.58M | -0.55% |
| PYUSD | $738.95M | +3.24% |
| USDG | $630.52M | +2.98% |
| USDe | $500.46M | -5.17% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $634.15M |
| BisonFi | $446.78M |
| Raydium AMM | $431.07M |
| Orca DEX | $347.01M |
| Meteora DLMM | $266.83M |
| GoonFi | $159.53M |
| Tessera V | $155.45M |
| Scorch | $150.64M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.40M |
| Axiom | $2.00M |
| pump.fun | $1.75M |
| Raydium AMM | $1.52M |
| StonkFun | $1.27M |
| Meteora DLMM | $982.20K |
| fomo Wallet | $936.63K |
| LaunchLab | $764.56K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $150.88M |
| xStocks holder positions | 612.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $536.52M |

## Program activity and chain health

Chain tip lag: **+10.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 70,517 | 19.40% | 0.8 s |
| Pump.fun | 5,668 | 62.80% | 10.3 s |
| Orca Whirlpools | 4,114 | 44.90% | 14.6 s |
| Jupiter v6 | 2,477 | 46.00% | 24.1 s |
| Raydium AMM v4 | 1,042 | 38.50% | 57.2 s |

Median failure rate across the sampled programs: **44.90%** (range 19.40% to 62.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.39 SOL**.

## Exchange and large-holder balances

12.10M SOL ($1.44B) across 8 publicly-attributed accounts. Net **64K SOL (0.52%) moved off exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.18B | 0.2/h | 0 |
| Binance (2) | 1.45M | $172.29M | 1.4K/h | 0 |
| Bybit | 263.05K | $31.29M | 34.7/h | 0 |
| Gate.io | 256.50K | $30.51M | 292.7/h | 3 |
| Coinbase (2) | 83.69K | $9.96M | 264.5/h | 0 |
| Bitget | 46.86K | $5.57M | 227.3/h | 0 |
| Kraken | 31.70K | $3.77M | 160.7/h | 0 |
| Coinbase | 25.97K | $3.09M | 254.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 879 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.228 | 838 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.210 | 845 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.192 | 804 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.188 | 804 | 0.0000 |
| Total TPS moves with Slot time | +0.170 | 845 | 0.0000 |
| Total TPS moves with Program failure rate | +0.157 | 826 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.156 | 826 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.130 | 804 | 0.0002 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with DeFi TVL | +0.114 | 879 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 118.96 USD | Jupiter (on-chain DEX): 118.89 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 587.51M SOL | CoinGecko: 587.51M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [Vote/commission SIMDs: fix 0249 commission rule direction, 0133 param name, 0387/0185 details](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - *open*, updated 2026-09-22
- [SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - *open*, updated 2026-09-22
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [Fix broken markdown, stale references and typos across several SIMDs](https://github.com/solana-foundation/solana-improvement-documents/pull/668) - updated 2026-09-22
- [SIMD-0385 / 0388 / 0204: fix inconsistent field and constant names](https://github.com/solana-foundation/solana-improvement-documents/pull/666) - updated 2026-09-22
- [Fix dead links in SIMD-0118, 0153, 0183, 0204, 0266, 0553](https://github.com/solana-foundation/solana-improvement-documents/pull/665) - updated 2026-09-22
- [Vote/commission SIMDs: fix 0249 commission rule direction, 0133 param name, 0387/0185 details](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-22
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-22
- [Fix supersedes / superseded-by links for SIMD-0048, 0219 and 0458](https://github.com/solana-foundation/solana-improvement-documents/pull/660) - updated 2026-09-22

**Recently merged SIMDs:**

- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15
- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10

**Latest Agave release:** [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) (2026-09-18)

**Latest Firedancer release:** [v26.09.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.4) (2026-09-22)

## Ecosystem news

- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana's Heartbeat Quickens: Block Times Fall 17% in Latest Speed Upgrade](https://decrypt.co/378674/solana-heartbeat-quickens-speed-upgrade)** - Decrypt, 2026-09-19
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
