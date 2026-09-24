# Solana Ecosystem Report

*Generated 2026-09-24 23:38 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 1.7K |
| Slot time | 267.3 ms |
| Slot | 450M |
| Block height | 428M |
| Epoch | 1042 (8.23% complete, ~29.4h remaining) |
| Lifetime transactions | 552.3B |
| Circulating supply | 587.6M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 3.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 10 |
| Delinquent stake | 0.03% |
| Total active stake | 440.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.41% / 24.41% / 35.63% |
| Commission (stake-weighted, delegatable validators) | 3.80% |
| Stake on private (100% commission) validators | 23.74% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.59% | 0% |
| 3 | `3N7s…iD5g` | 12.4M | 2.81% | 0% |
| 4 | `Catz…Diqb` | 11.3M | 2.56% | 5% |
| 5 | `8Gbw…F8iD` | 10.6M | 2.41% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.09% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.08% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $117.05 (+1.94% 24h) |
| Market cap | $68.78B (rank #7) |
| 24h volume | $4.31B |
| ATH | $293.31 (-60.09% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.48B |
| Stablecoin supply | $17.27B |
| DEX volume (24h) | $2.55B (-20.10% 1d) |
| App fees (24h, all protocols) | $16.12M |
| Chain fees (24h) | $1.01M |
| Jito MEV tips (24h) | $223.39K |
| **REV - Real Economic Value (24h)** | **$1.23M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $8.11B | +21.08% |
| USDT | $2.66B | +13.64% |
| USDGO | $1.42B | +2.98% |
| USD1 | $1.38B | +4.48% |
| BUIDL | $987.78M | -0.54% |
| PYUSD | $723.23M | +0.55% |
| USDG | $635.63M | +1.76% |
| USDe | $493.60M | -5.74% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Raydium AMM | $347.53M |
| BisonFi | $323.94M |
| Orca DEX | $323.12M |
| PumpSwap | $270.19M |
| Meteora DLMM | $233.66M |
| pump.fun | $115.24M |
| Scorch | $113.00M |
| fomo Wallet | $112.98M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.50M |
| Axiom | $1.82M |
| pump.fun | $1.59M |
| Raydium AMM | $1.25M |
| Meteora DLMM | $978.23K |
| StonkFun | $958.37K |
| LaunchLab | $644.87K |
| Collector Crypt | $534.96K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $142.93M |
| xStocks holder positions | 633.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $542.93M |

## Program activity and chain health

Chain tip lag: **+9.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 70,857 | 27.80% | 0.8 s |
| Pump.fun | 8,988 | 62.70% | 6.4 s |
| Orca Whirlpools | 3,203 | 24.30% | 17.9 s |
| Raydium AMM v4 | 2,797 | 46.10% | 21.4 s |
| Jupiter v6 | 2,548 | 55.90% | 23.5 s |

Median failure rate across the sampled programs: **46.10%** (range 24.30% to 62.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **554.01 SOL**.

## Exchange and large-holder balances

11.68M SOL ($1.37B) across 7 publicly-attributed accounts. Net **78K SOL (0.67%) moved off exchanges** over the last 22.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.16B | 0.2/h | 0 |
| Binance (2) | 1.15M | $135.11M | 997.2/h | 0 |
| Gate.io | 249.75K | $29.23M | 213.6/h | 3 |
| Bybit | 213.29K | $24.97M | 68.2/h | 0 |
| Coinbase (2) | 66.69K | $7.81M | 503.5/h | 0 |
| Kraken | 35.21K | $4.12M | 241.6/h | 0 |
| Coinbase | 20.95K | $2.45M | 518/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 889 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.243 | 848 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.211 | 855 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.194 | 814 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.189 | 814 | 0.0000 |
| Total TPS moves with Slot time | +0.170 | 855 | 0.0000 |
| Total TPS moves with Program failure rate | +0.157 | 836 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.156 | 836 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.134 | 814 | 0.0001 |
| SOL price moves with DeFi TVL | +0.119 | 889 | 0.0004 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 117.05 USD | Jupiter (on-chain DEX): 117.09 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 587.65M SOL | CoinGecko: 587.65M SOL | -0.00% | agree |

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

- **[Solana treasury firm SkyAI keeps board after shareholder protest, loses equity plan vote](https://www.theblock.co/news/business/2026-09-24-solana-treasury-skyai-keeps-board-shareholder-protest-loses-equity-plan-vote-416298)** - The Block, 2026-09-24
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Solana Foundation Hires Binance's Former Global CMO for Institutional Push](https://decrypt.co/379179/solana-foundation-hires-binances-former-global-cmo-for-institutional-push)** - Decrypt, 2026-09-24
- **[Solana Foundation taps Binance, Polygon vets to drive institutional adoption and payments](https://www.theblock.co/news/ecosystems/2026-09-24-solana-foundation-taps-binance-polygon-vets-to-drive-institutional-adoption-and-payments-416254)** - The Block, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
