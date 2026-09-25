# Solana Ecosystem Report

*Generated 2026-09-25 13:58 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.0K |
| TPS (non-vote) | 2.4K |
| Slot time | 268.5 ms |
| Slot | 450M |
| Block height | 428M |
| Epoch | 1042 (52.97% complete, ~15.2h remaining) |
| Lifetime transactions | 552.5B |
| Circulating supply | 587.6M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 16.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 10 |
| Delinquent stake | 0.01% |
| Total active stake | 440.6M SOL |
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
| 5 | `8Gbw…F8iD` | 10.6M | 2.40% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.09% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.08% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.72% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $119.70 (+4.35% 24h) |
| Market cap | $70.32B (rank #7) |
| 24h volume | $5.34B |
| ATH | $293.31 (-59.19% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.54B |
| Stablecoin supply | $16.59B |
| DEX volume (24h) | $2.45B (-4.00% 1d) |
| App fees (24h, all protocols) | $15.98M |
| Chain fees (24h) | $952.67K |
| Jito MEV tips (24h) | $226.59K |
| **REV - Real Economic Value (24h)** | **$1.18M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.44B | +11.07% |
| USDT | $2.66B | +17.14% |
| USDGO | $1.41B | +1.88% |
| USD1 | $1.38B | +4.48% |
| BUIDL | $987.78M | -0.55% |
| PYUSD | $723.31M | -1.50% |
| USDG | $653.00M | +4.64% |
| USDe | $487.89M | -6.83% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $395.08M |
| Orca DEX | $344.60M |
| Raydium AMM | $277.29M |
| Meteora DLMM | $191.04M |
| HumidiFi | $190.33M |
| PumpSwap | $133.76M |
| Manifest Trade | $132.50M |
| pump.fun | $123.23M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.39M |
| Axiom | $1.66M |
| pump.fun | $1.65M |
| StonkFun | $929.73K |
| Raydium AMM | $850.81K |
| Meteora DLMM | $758.62K |
| LaunchLab | $656.41K |
| BONK.fun Launchpad | $527.14K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $111.58M |
| xStocks holder positions | 636.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $543.76M |

## Program activity and chain health

Chain tip lag: **+10.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 49,330 | 34.50% | 1.1 s |
| Pump.fun | 31,700 | 82.20% | 1.9 s |
| Jupiter v6 | 7,210 | 69.70% | 8.1 s |
| Orca Whirlpools | 2,326 | 37.50% | 25.5 s |
| Raydium AMM v4 | 763 | 20.90% | 78.1 s |

Median failure rate across the sampled programs: **37.50%** (range 20.90% to 82.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **385.03 SOL**.

## Exchange and large-holder balances

12.04M SOL ($1.44B) across 7 publicly-attributed accounts. Net **259K SOL (2.20%) moved onto exchanges** over the last 20.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.19B | 0.2/h | 0 |
| Binance (2) | 1.36M | $162.49M | 1.2K/h | 0 |
| Bybit | 387.36K | $46.37M | 48.4/h | 0 |
| Gate.io | 269.99K | $32.32M | 278.6/h | 3 |
| Coinbase (2) | 34.64K | $4.15M | 473.1/h | 0 |
| Kraken | 30.30K | $3.63M | 233/h | 0 |
| Coinbase | 16.82K | $2.01M | 432.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 892 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.245 | 851 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.212 | 858 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.193 | 817 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.189 | 817 | 0.0000 |
| Total TPS moves with Slot time | +0.171 | 858 | 0.0000 |
| Total TPS moves with Program failure rate | +0.156 | 839 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.154 | 839 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.134 | 817 | 0.0001 |
| SOL price moves with DeFi TVL | +0.126 | 892 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 119.70 USD | Jupiter (on-chain DEX): 119.46 USD | +0.20% | agree |
| Circulating supply | getSupply (RPC): 587.65M SOL | CoinGecko: 587.65M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0138: point feature at deprecate_legacy_vote_ixs, status Implemented](https://github.com/solana-foundation/solana-improvement-documents/pull/657) - *open*, updated 2026-09-23
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15

**Open SIMD proposals:**

- [Fix broken markdown, stale references and typos across several SIMDs](https://github.com/solana-foundation/solana-improvement-documents/pull/668) - updated 2026-09-22
- [SIMD-0385 / 0388 / 0204: fix inconsistent field and constant names](https://github.com/solana-foundation/solana-improvement-documents/pull/666) - updated 2026-09-22
- [Fix dead links in SIMD-0118, 0153, 0183, 0204, 0266, 0553](https://github.com/solana-foundation/solana-improvement-documents/pull/665) - updated 2026-09-22
- [SIMD-0249: fix direction of the lifted commission-increase restriction](https://github.com/solana-foundation/solana-improvement-documents/pull/662) - updated 2026-09-23
- [sBPF SIMDs: clarify SBPF version scope (0166/0173/0174), fix 0166 drawbacks and 0460 stack table](https://github.com/solana-foundation/solana-improvement-documents/pull/661) - updated 2026-09-23
- [Fix supersedes / superseded-by links for SIMD-0048, 0219 and 0458](https://github.com/solana-foundation/solana-improvement-documents/pull/660) - updated 2026-09-22

**Recently merged SIMDs:**

- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-15

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
