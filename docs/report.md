# Solana Ecosystem Report

*Generated 2026-09-23 01:34 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 4.7 robust standard deviations above its 7-day baseline: a 6.6% move to 16,584,963,210.00 USD from a typical 15,556,207,419.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 1.7K |
| Slot time | 265.5 ms |
| Slot | 450M |
| Block height | 428M |
| Epoch | 1040 (63.72% complete, ~11.6h remaining) |
| Lifetime transactions | 551.5B |
| Circulating supply | 587.5M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 12.70% of slots needed a priority fee (max 1.9M µlam/CU) |
| Node version (RPC) | 4.3.0-rc.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 12 |
| Delinquent stake | 0.04% |
| Total active stake | 439.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.35% / 24.33% / 35.64% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
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
| SOL price | $118.90 (+0.68% 24h) |
| Market cap | $69.85B (rank #7) |
| 24h volume | $4.48B |
| ATH | $293.31 (-59.46% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.51B |
| Stablecoin supply | $16.58B |
| DEX volume (24h) | $3.46B (+0.86% 1d) |
| App fees (24h, all protocols) | $17.58M |
| Chain fees (24h) | $1.10M |
| Jito MEV tips (24h) | $258.14K |
| **REV - Real Economic Value (24h)** | **$1.35M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.96B | +17.57% |
| USDT | $2.14B | -14.08% |
| USDGO | $1.40B | +1.96% |
| USD1 | $1.37B | +3.72% |
| BUIDL | $987.58M | -0.55% |
| PYUSD | $738.86M | +3.23% |
| USDG | $629.61M | +2.82% |
| USDe | $502.57M | -4.78% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $634.15M |
| Raydium AMM | $475.88M |
| BisonFi | $446.78M |
| Orca DEX | $367.61M |
| Meteora DLMM | $259.61M |
| GoonFi | $159.53M |
| Tessera V | $155.45M |
| Scorch | $150.64M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.36M |
| Axiom | $2.30M |
| StonkFun | $1.81M |
| Raydium AMM | $1.76M |
| pump.fun | $1.73M |
| Meteora DLMM | $1.28M |
| fomo Wallet | $936.63K |
| LaunchLab | $833.21K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $156.35M |
| xStocks holder positions | 608.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $536.82M |

## Program activity and chain health

Chain tip lag: **+9.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 35,066 | 21.60% | 1.6 s |
| Pump.fun | 9,397 | 79.70% | 6.4 s |
| Jupiter v6 | 3,528 | 54.20% | 17 s |
| Orca Whirlpools | 2,396 | 38.20% | 24.7 s |
| Raydium AMM v4 | 1,821 | 31.20% | 32.9 s |

Median failure rate across the sampled programs: **38.20%** (range 21.60% to 79.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.39 SOL**.

## Exchange and large-holder balances

12.13M SOL ($1.44B) across 8 publicly-attributed accounts. Net **156K SOL (1.30%) moved onto exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.18B | 0.2/h | 0 |
| Binance (2) | 1.47M | $174.32M | 1.2K/h | 0 |
| Gate.io | 289.36K | $34.40M | 460.9/h | 3 |
| Bybit | 263.05K | $31.28M | 35.2/h | 0 |
| Coinbase (2) | 86.64K | $10.30M | 471.2/h | 0 |
| Kraken | 31.72K | $3.77M | 150.1/h | 0 |
| Coinbase | 29.54K | $3.51M | 475.6/h | 0 |
| Bitget | 22.90K | $2.72M | 285.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 878 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.233 | 837 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.210 | 844 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.193 | 803 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.189 | 803 | 0.0000 |
| Total TPS moves with Slot time | +0.170 | 844 | 0.0000 |
| Total TPS moves with Program failure rate | +0.158 | 825 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.157 | 825 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.130 | 803 | 0.0002 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with DeFi TVL | +0.113 | 878 | 0.0008 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 118.90 USD | Jupiter (on-chain DEX): 118.60 USD | +0.25% | agree |
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
