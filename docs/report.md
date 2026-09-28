# Solana Ecosystem Report

*Generated 2026-09-28 16:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 5.2K |
| TPS (non-vote) | 2.7K |
| Slot time | 270.3 ms |
| Slot | 451M |
| Block height | 429M |
| Epoch | 1044 (83.56% complete, ~5.3h remaining) |
| Lifetime transactions | 553.7B |
| Circulating supply | 587.8M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 22.00% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 7 |
| Delinquent stake | 0.01% |
| Total active stake | 440.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.46% / 24.46% / 35.37% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.69% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.9M | 4.06% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.80% | 0% |
| 4 | `Catz…Diqb` | 11.2M | 2.55% | 5% |
| 5 | `8Gbw…F8iD` | 10.8M | 2.46% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.09% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.48% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $118.56 (-2.85% 24h) |
| Market cap | $69.72B (rank #7) |
| 24h volume | $4.00B |
| ATH | $293.31 (-59.58% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.55B |
| Stablecoin supply | $16.56B |
| DEX volume (24h) | $1.93B (-10.61% 1d) |
| App fees (24h, all protocols) | $15.42M |
| Chain fees (24h) | $949.15K |
| Jito MEV tips (24h) | $231.27K |
| **REV - Real Economic Value (24h)** | **$1.18M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.24B | +2.62% |
| USDT | $2.68B | +26.94% |
| USDGO | $1.41B | +1.59% |
| USD1 | $1.39B | +4.45% |
| BUIDL | $988.19M | -0.50% |
| PYUSD | $732.03M | -0.35% |
| USDG | $692.50M | +9.73% |
| USDe | $463.66M | -8.89% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $338.50M |
| PumpSwap | $297.07M |
| BisonFi | $270.02M |
| Raydium AMM | $234.17M |
| Meteora DLMM | $158.26M |
| pump.fun | $152.04M |
| fomo Wallet | $148.47M |
| Manifest Trade | $112.58M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $5.07M |
| pump.fun | $2.11M |
| Axiom | $1.00M |
| Meteora DLMM | $698.73K |
| Raydium AMM | $559.39K |
| StonkFun | $529.09K |
| fomo Wallet | $477.88K |
| pump.fun Mobile App | $420.88K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $93.34M |
| xStocks holder positions | 655.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $545.70M |

## Program activity and chain health

Chain tip lag: **+10.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 81,354 (approx.) | 41.30% | 0.5 s |
| Pump.fun | 17,558 | 75.60% | 2.7 s |
| Orca Whirlpools | 13,665 | 50.10% | 4.3 s |
| Jupiter v6 | 7,904 | 73.70% | 7.6 s |
| Raydium AMM v4 | 1,151 | 20.70% | 51.9 s |

Median failure rate across the sampled programs: **50.10%** (range 20.70% to 75.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **88.10 SOL**.

## Exchange and large-holder balances

12.54M SOL ($1.49B) across 7 publicly-attributed accounts. Net **145K SOL (1.14%) moved off exchanges** over the last 22.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.77M | $1.28B | 0.3/h | 0 |
| Binance (2) | 1.07M | $126.76M | 1.7K/h | 0 |
| Bybit | 387.38K | $45.93M | 40.8/h | 0 |
| Gate.io | 243.65K | $28.89M | 226/h | 4 |
| Kraken | 29.53K | $3.50M | 428.6/h | 0 |
| Coinbase | 21.59K | $2.56M | 262/h | 0 |
| Coinbase (2) | 12.68K | $1.50M | 534.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 910 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.225 | 869 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.215 | 876 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.196 | 835 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.191 | 835 | 0.0000 |
| Total TPS moves with Slot time | +0.176 | 876 | 0.0000 |
| Total TPS moves with Program failure rate | +0.158 | 857 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.157 | 857 | 0.0000 |
| SOL price moves with DeFi TVL | +0.146 | 910 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.139 | 835 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 118.56 USD | Jupiter (on-chain DEX): 118.62 USD | -0.05% | agree |
| Circulating supply | getSupply (RPC): 587.78M SOL | CoinGecko: 587.78M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-25

**Open SIMD proposals:**

- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - updated 2026-09-17

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15

**Latest Agave release:** [v4.4.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-beta.0) (2026-09-28)

**Latest Firedancer release:** [v26.09.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.4) (2026-09-22)

## Ecosystem news

- **[Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects)** - Solana.com, 2026-09-28
- **[Bitcoin Rally Slows as $15.6 Billion Options Expiry Hits—XRP and Solana Keep Climbing](https://decrypt.co/379319/bitcoin-slows-billion-options-expiry-xrp-solana)** - Decrypt, 2026-09-25
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16
- **[Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026)** - Solana.com, 2026-09-14
- **[Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public)** - Solana.com, 2026-09-14

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
