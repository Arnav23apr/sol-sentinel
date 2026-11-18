# Solana Ecosystem Report

*Generated 2026-11-18 03:18 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.9K |
| TPS (non-vote) | 1.9K |
| Slot time | 217 ms |
| Slot | 471M |
| Block height | 449M |
| Epoch | 1089 (77.22% complete, ~5.9h remaining) |
| Lifetime transactions | 567.2B |
| Circulating supply | 591.7M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 6.00% of slots needed a priority fee (max 1.5M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 5 |
| Delinquent stake | 0.01% |
| Total active stake | 428.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.31% / 24.77% / 35.97% |
| Commission (stake-weighted, delegatable validators) | 3.87% |
| Stake on private (100% commission) validators | 22.99% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.93% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.84% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.90% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.37% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.29% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.24% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.86% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.57% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $74.68 (+3.64% 24h) |
| Market cap | $44.19B (rank #7) |
| 24h volume | $3.12B |
| ATH | $293.31 (-74.54% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.81B |
| Stablecoin supply | $13.72B |
| DEX volume (24h) | $1.50B (+1.24% 1d) |
| App fees (24h, all protocols) | $8.22M |
| Chain fees (24h) | $445.21K |
| Jito MEV tips (24h) | $118.88K |
| **REV - Real Economic Value (24h)** | **$564.10K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.29B | +2.33% |
| USDT | $2.00B | -6.96% |
| USDGO | $1.02B | -5.36% |
| USD1 | $944.31M | -16.36% |
| PYUSD | $778.08M | -2.23% |
| USDG | $423.09M | -10.95% |
| SOFID | $278.52M | +3.91% |
| USDe | $267.65M | -6.20% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $233.52M |
| Meteora DLMM | $155.76M |
| PumpSwap | $155.29M |
| BisonFi | $148.83M |
| Raydium AMM | $136.30M |
| pump.fun | $110.25M |
| Manifest Trade | $92.84M |
| Scorch | $88.93M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.87M |
| pump.fun | $1.40M |
| Meteora DLMM | $503.82K |
| Axiom | $477.36K |
| Jupiter Perpetual Exchange | $349.86K |
| Raydium AMM | $250.09K |
| Sanctum Validator LSTs | $226.22K |
| Lunar Lander | $200.24K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $86.62M |
| xStocks holder positions | 938.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $562.47M |

## Program activity and chain health

Chain tip lag: **+1.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 54,263 | 46.00% | 0.9 s |
| Pump.fun | 44,931 | 74.10% | 1.3 s |
| Orca Whirlpools | 5,259 | 50.90% | 11.3 s |
| Jupiter v6 | 3,063 | 48.80% | 19.3 s |
| Raydium AMM v4 | 1,125 | 12.90% | 52.9 s |

Median failure rate across the sampled programs: **48.80%** (range 12.90% to 74.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **438.40 SOL**.

## Exchange and large-holder balances

9.61M SOL ($717.37M) across 7 publicly-attributed accounts. Net **16K SOL (0.17%) moved onto exchanges** over the last 22.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $694.52M | 0.3/h | 2 |
| Gate.io | 68.43K | $5.11M | 104/h | 0 |
| Bybit | 67.80K | $5.06M | 22/h | 0 |
| Bitget | 55.60K | $4.15M | 102.3/h | 0 |
| Coinbase (2) | 40.66K | $3.04M | 268.7/h | 0 |
| Kraken | 39.91K | $2.98M | 232.1/h | 0 |
| Coinbase | 33.56K | $2.51M | 271.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1146 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.252 | 1105 | 0.0000 |
| SOL price moves with DeFi TVL | +0.251 | 1146 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.245 | 1073 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.240 | 1073 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 1114 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 1114 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.174 | 1095 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1095 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.148 | 1073 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.128 | 1073 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 74.68 USD | Jupiter (on-chain DEX): 74.63 USD | +0.07% | agree |
| Circulating supply | getSupply (RPC): 591.74M SOL | CoinGecko: 591.74M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-14
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-07
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-09
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04

**Recently merged SIMDs:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31

**Latest Agave release:** [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06)

**Latest Firedancer release:** [v26.11.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.0) (2026-11-11)

## Ecosystem news

- **[Standard Life Chair Wants Tokenized Gilts to Open UK Government Bonds to Retail Savers](https://decrypt.co/383434/standard-life-chair-wants-tokenized-gilts-to-open-uk-government-bonds-to-retail-savers)** - Decrypt, 2026-11-17
- **[Solana’s Trump memecoin launch tested infrastructure ahead of institutional push, Lily Liu says](https://www.theblock.co/news/ecosystems/2026-11-17-solana-trump-memecoin-launch-tested-infrastructure-institutional-push-lily-liu-says-442132)** - The Block, 2026-11-17
- **['The Biggest Opportunity in Crypto Is Already Underway': Solana Bets Big on AI Agents](https://decrypt.co/383417/the-biggest-opportunity-in-crypto-is-already-underway-solana-bets-big-on-ai-agents)** - Decrypt, 2026-11-17
- **[Solana Foundation Backs CoinGecko as Crypto Data Giant Eyes Trading](https://decrypt.co/383401/solana-foundation-backs-coingecko-eyes-trading)** - Decrypt, 2026-11-17
- **['Tokenization Is Not the Finish Line': Jupiter to Let Users Borrow Against Bullish Shares](https://decrypt.co/383333/tokenization-is-not-the-finish-line-jupiter-to-let-users-borrow-against-bullish-shares)** - Decrypt, 2026-11-16
- **[Solana Drops 'Mainnet Beta' After Six Years: Here's What 1.0 Is All About](https://decrypt.co/383322/solana-drops-mainnet-beta-after-six-years)** - Decrypt, 2026-11-16
- **[DTCC, Barclays Say Tokenization's Real Prize Is Unlocking Idle Collateral](https://decrypt.co/383316/dtcc-barclays-say-tokenizations-real-prize-is-unlocking-idle-collateral)** - Decrypt, 2026-11-16
- **['Nobody Knows Who's in Charge': Boris Johnson Stands by Bitcoin Skepticism at Breakpoint](https://decrypt.co/383307/nobody-knows-whos-in-charge-boris-johnson-stands-by-bitcoin-skepticism-at-breakpoint)** - Decrypt, 2026-11-16
- **[Ledger Brings Clear Signing to Solana, Ending 'Blind' Signing for Jupiter Swaps](https://decrypt.co/383302/ledger-brings-clear-signing-to-solana-ending-blind-signing-for-jupiter-swaps)** - Decrypt, 2026-11-16
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
