# Solana Ecosystem Report

*Generated 2026-09-22 20:17 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **App fees (24h, all protocols)** (warning): App fees (24h, all protocols) is 4.8 robust standard deviations above its 7-day baseline: a 27.4% move to 18,642,402.00 USD from a typical 14,631,505.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.8K |
| TPS (non-vote) | 2.2K |
| Slot time | 266.7 ms |
| Slot | 449M |
| Block height | 428M |
| Epoch | 1040 (47.18% complete, ~16.9h remaining) |
| Lifetime transactions | 551.5B |
| Circulating supply | 587.5M SOL |
| Inflation (annual) | 3.64% |
| AMM write-lock congestion (150-slot window) | 50.00% of slots needed a priority fee (max 33.1M µlam/CU) |
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
| Stake on private (100% commission) validators | 23.81% |

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
| SOL price | $117.94 (-0.46% 24h) |
| Market cap | $69.31B (rank #7) |
| 24h volume | $4.89B |
| ATH | $293.31 (-59.79% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.49B |
| Stablecoin supply | $16.04B |
| DEX volume (24h) | $3.43B (+22.67% 1d) |
| App fees (24h, all protocols) | $18.64M |
| Chain fees (24h) | $1.10M |
| Jito MEV tips (24h) | $243.44K |
| **REV - Real Economic Value (24h)** | **$1.34M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.44B | +3.31% |
| USDT | $2.14B | -14.08% |
| USDGO | $1.40B | +0.86% |
| USD1 | $1.37B | +3.72% |
| BUIDL | $993.58M | +0.07% |
| PYUSD | $717.09M | +2.09% |
| USDG | $621.50M | +1.23% |
| USDe | $503.46M | -4.79% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $497.57M |
| BisonFi | $446.78M |
| Orca DEX | $398.84M |
| PumpSwap | $390.12M |
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
| pump.fun | $1.73M |
| Raydium AMM | $1.68M |
| Meteora DLMM | $1.28M |
| fomo Wallet | $936.63K |
| LaunchLab | $833.21K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $199.83M |
| xStocks holder positions | 607.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $536.80M |

## Program activity and chain health

Chain tip lag: **+10.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 89,651 (approx.) | 31.80% | 0.5 s |
| Pump.fun | 8,003 | 49.70% | 7.5 s |
| Orca Whirlpools | 4,994 | 19.30% | 12 s |
| Jupiter v6 | 4,744 | 58.50% | 12.5 s |
| Raydium AMM v4 | 4,215 | 10.50% | 14.1 s |

Median failure rate across the sampled programs: **31.80%** (range 10.50% to 58.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.39 SOL**.

## Exchange and large-holder balances

12.14M SOL ($1.43B) across 8 publicly-attributed accounts. Net **148K SOL (1.23%) moved onto exchanges** over the last 20.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.17B | 0.2/h | 0 |
| Binance (2) | 1.44M | $169.75M | 1.2K/h | 0 |
| Gate.io | 304.42K | $35.90M | 303.3/h | 4 |
| Bybit | 263.05K | $31.02M | 29.3/h | 0 |
| Coinbase (2) | 93.89K | $11.07M | 496.6/h | 0 |
| Kraken | 48.87K | $5.76M | 272.7/h | 0 |
| Bitget | 21.16K | $2.50M | 190/h | 0 |
| Coinbase | 21.15K | $2.49M | 459.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 876 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.240 | 835 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.210 | 842 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.190 | 801 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.186 | 801 | 0.0000 |
| Total TPS moves with Slot time | +0.170 | 842 | 0.0000 |
| Total TPS moves with Program failure rate | +0.158 | 823 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.156 | 823 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.131 | 801 | 0.0002 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with DeFi TVL | +0.110 | 876 | 0.0011 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 117.94 USD | Jupiter (on-chain DEX): 117.93 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 587.51M SOL | CoinGecko: 587.51M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08

**Open SIMD proposals:**

- [Fix rendering in SIMD-0302/0306/0266/0307, rename 0505 file to 0506](https://github.com/solana-foundation/solana-improvement-documents/pull/655) - updated 2026-09-22
- [SIMD-0047 / SIMD-0186: fix syscall hash and signature, union of loaded accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/654) - updated 2026-09-22
- [SIMD-0317 / SIMD-0313: fix FEC set payload size, gate name and shred layout](https://github.com/solana-foundation/solana-improvement-documents/pull/653) - updated 2026-09-22
- [SIMD-0174: fix UREM32 width, SREM operators and SUB_IMM operands](https://github.com/solana-foundation/solana-improvement-documents/pull/652) - updated 2026-09-22
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-22
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-21

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
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14
- **[Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026)** - Solana.com, 2026-09-10
- **[Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026)** - Solana.com, 2026-09-10
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
