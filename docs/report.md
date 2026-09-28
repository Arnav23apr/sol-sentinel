# Solana Ecosystem Report

*Generated 2026-09-28 22:10 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Median program failure rate** (warning): Median program failure rate is 5.6 robust standard deviations above its 7-day baseline: a 108.3% move to 85.80 % from a typical 41.20.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.7K |
| TPS (non-vote) | 2.2K |
| Slot time | 269.1 ms |
| Slot | 451M |
| Block height | 429M |
| Epoch | 1045 (2.14% complete, ~31.6h remaining) |
| Lifetime transactions | 553.8B |
| Circulating supply | 587.9M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 20.70% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 7 |
| Delinquent stake | 0.01% |
| Total active stake | 441.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.54% / 24.45% / 35.34% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.64% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.8M | 4.04% | 7% |
| 2 | `he1i…uBtk` | 15.9M | 3.60% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.80% | 0% |
| 4 | `8Gbw…F8iD` | 11.3M | 2.56% | 0% |
| 5 | `Catz…Diqb` | 11.2M | 2.54% | 5% |
| 6 | `26pV…3dJx` | 9.2M | 2.10% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.09% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.73% | 7% |
| 9 | `CvSb…wycB` | 6.7M | 1.52% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.48% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $117.46 (-3.63% 24h) |
| Market cap | $69.01B (rank #7) |
| 24h volume | $4.08B |
| ATH | $293.31 (-59.95% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.55B |
| Stablecoin supply | $16.42B |
| DEX volume (24h) | $1.90B (-11.69% 1d) |
| App fees (24h, all protocols) | $15.42M |
| Chain fees (24h) | $949.15K |
| Jito MEV tips (24h) | $241.65K |
| **REV - Real Economic Value (24h)** | **$1.19M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.26B | +2.92% |
| USDT | $2.70B | +27.89% |
| USDGO | $1.41B | +1.59% |
| USD1 | $1.39B | +4.45% |
| BUIDL | $964.13M | -2.93% |
| PYUSD | $722.52M | -1.71% |
| USDG | $691.65M | +9.57% |
| USDe | $459.73M | -9.62% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $426.72M |
| PumpSwap | $297.07M |
| BisonFi | $270.02M |
| Raydium AMM | $269.47M |
| Meteora DLMM | $158.26M |
| pump.fun | $152.04M |
| fomo Wallet | $140.82M |
| Manifest Trade | $137.89M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $5.07M |
| pump.fun | $2.11M |
| Axiom | $1.00M |
| Raydium AMM | $826.96K |
| Meteora DLMM | $698.73K |
| StonkFun | $529.09K |
| fomo Wallet | $477.88K |
| pump.fun Mobile App | $420.88K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $106.02M |
| xStocks holder positions | 664.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $544.01M |

## Program activity and chain health

Chain tip lag: **+10.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 67,187 | 37.30% | 0.8 s |
| Jupiter v6 | 19,216 | 92.10% | 3 s |
| Orca Whirlpools | 15,862 | 90.00% | 3.8 s |
| Raydium AMM v4 | 14,732 | 85.80% | 3.8 s |
| Pump.fun | 5,972 | 39.80% | 10 s |

Median failure rate across the sampled programs: **85.80%** (range 37.30% to 92.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **787.47 SOL**.

## Exchange and large-holder balances

12.50M SOL ($1.47B) across 6 publicly-attributed accounts. Net **132K SOL (1.05%) moved off exchanges** over the last 22.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.77M | $1.27B | 0.3/h | 0 |
| Binance (2) | 1.05M | $123.42M | 965.1/h | 0 |
| Bybit | 387.38K | $45.50M | 26.9/h | 0 |
| Gate.io | 241.95K | $28.42M | 206.8/h | 3 |
| Kraken | 26.48K | $3.11M | 419.6/h | 0 |
| Coinbase (2) | 17.80K | $2.09M | 445.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 911 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.225 | 870 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.216 | 877 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.196 | 836 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.191 | 836 | 0.0000 |
| Total TPS moves with Slot time | +0.177 | 877 | 0.0000 |
| Total TPS moves with Program failure rate | +0.155 | 858 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.153 | 858 | 0.0000 |
| SOL price moves with DeFi TVL | +0.146 | 911 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.139 | 836 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 117.46 USD | Jupiter (on-chain DEX): 117.36 USD | +0.09% | agree |
| Circulating supply | getSupply (RPC): 587.85M SOL | CoinGecko: 587.85M SOL | -0.00% | agree |

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

**Latest Firedancer release:** [v26.09.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.5) (2026-09-28)

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
