# Solana Ecosystem Report

*Generated 2026-11-17 13:56 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 213.6 ms |
| Slot | 471M |
| Block height | 449M |
| Epoch | 1089 (25.59% complete, ~19.1h remaining) |
| Lifetime transactions | 567.1B |
| Circulating supply | 591.7M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 30.00% of slots needed a priority fee (max 10.0M µlam/CU) |
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
| SOL price | $73.59 (+4.13% 24h) |
| Market cap | $43.55B (rank #7) |
| 24h volume | $3.02B |
| ATH | $293.31 (-74.91% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.80B |
| Stablecoin supply | $13.82B |
| DEX volume (24h) | $1.48B (+9.42% 1d) |
| App fees (24h, all protocols) | $8.33M |
| Chain fees (24h) | $446.30K |
| Jito MEV tips (24h) | $131.70K |
| **REV - Real Economic Value (24h)** | **$578.00K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.45B | +5.20% |
| USDT | $2.00B | -10.69% |
| USDGO | $1.02B | -6.05% |
| USD1 | $964.04M | -16.57% |
| PYUSD | $680.36M | -9.68% |
| USDG | $437.17M | -10.68% |
| SOFID | $280.66M | +4.75% |
| USDe | $276.24M | -4.04% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $219.71M |
| PumpSwap | $157.21M |
| Meteora DLMM | $155.76M |
| BisonFi | $148.83M |
| Raydium AMM | $110.51M |
| pump.fun | $110.25M |
| Manifest Trade | $89.61M |
| Scorch | $88.93M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.70M |
| pump.fun | $1.38M |
| Meteora DLMM | $503.82K |
| Axiom | $477.36K |
| Jupiter Perpetual Exchange | $278.68K |
| Lunar Lander | $215.51K |
| Raydium AMM | $213.88K |
| Sanctum Validator LSTs | $210.86K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $52.97M |
| xStocks holder positions | 934.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $574.64M |

## Program activity and chain health

Chain tip lag: **+1.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 36,918 | 23.40% | 1.5 s |
| Pump.fun | 7,986 | 51.70% | 7.5 s |
| Jupiter v6 | 6,160 | 73.10% | 9 s |
| Orca Whirlpools | 2,017 | 56.20% | 29.5 s |
| Raydium AMM v4 | 670 | 15.60% | 89.3 s |

Median failure rate across the sampled programs: **51.70%** (range 15.60% to 73.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **727.64 SOL**.

## Exchange and large-holder balances

9.61M SOL ($707.15M) across 7 publicly-attributed accounts. Net **16K SOL (0.16%) moved onto exchanges** over the last 15.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $684.39M | 0.3/h | 2 |
| Bybit | 67.80K | $4.99M | 50.9/h | 0 |
| Gate.io | 65.48K | $4.82M | 210.8/h | 0 |
| Bitget | 61.27K | $4.51M | 188.9/h | 0 |
| Coinbase (2) | 41.95K | $3.09M | 218/h | 0 |
| Kraken | 40.02K | $2.94M | 241.8/h | 0 |
| Coinbase | 32.86K | $2.42M | 367.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1144 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.254 | 1103 | 0.0000 |
| SOL price moves with DeFi TVL | +0.249 | 1144 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.246 | 1071 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.242 | 1071 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 1112 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 1112 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.174 | 1093 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1093 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 1071 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.128 | 1071 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 73.59 USD | Jupiter (on-chain DEX): 73.68 USD | -0.12% | agree |
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

- **['The Biggest Opportunity in Crypto Is Already Underway': Solana Bets Big on AI Agents](https://decrypt.co/383417/the-biggest-opportunity-in-crypto-is-already-underway-solana-bets-big-on-ai-agents)** - Decrypt, 2026-11-17
- **[Solana Foundation Backs CoinGecko as Crypto Data Giant Eyes Trading](https://decrypt.co/383401/solana-foundation-backs-coingecko-eyes-trading)** - Decrypt, 2026-11-17
- **[CZ denies Binance sold crypto, Bitwise sees Solana at $1,100 by 2031, and more](https://www.theblock.co/newsletters/the-daily/2026-11-17-cz-binance-bitwise-solana-more-crypto-news-441584)** - The Block, 2026-11-17
- **[Bitwise sees Solana reaching $1,100 by 2031 in bull case as onchain trading grows](https://www.theblock.co/news/markets/2026-11-16-bitwise-solana-price-prediction-1100-2031-441407)** - The Block, 2026-11-16
- **[Privacy on Solana is ‘non-negotiable’ for institutional adoption, Mert Mumtaz says](https://www.theblock.co/news/ecosystems/2026-11-16-privacy-solana-non-negotiable-institutional-adoption-mert-mumtaz-says-441363)** - The Block, 2026-11-16
- **['Tokenization Is Not the Finish Line': Jupiter to Let Users Borrow Against Bullish Shares](https://decrypt.co/383333/tokenization-is-not-the-finish-line-jupiter-to-let-users-borrow-against-bullish-shares)** - Decrypt, 2026-11-16
- **[Boris Johnson backs tokenization months after likening bitcoin to a ‘Ponzi scheme’](https://www.theblock.co/news/regulation/2026-11-16-boris-johnson-backs-tokenization-months-after-bitcoin-to-ponzi-scheme-441368)** - The Block, 2026-11-16
- **[Solana Drops 'Mainnet Beta' After Six Years: Here's What 1.0 Is All About](https://decrypt.co/383322/solana-drops-mainnet-beta-after-six-years)** - Decrypt, 2026-11-16
- **[DTCC, Barclays Say Tokenization's Real Prize Is Unlocking Idle Collateral](https://decrypt.co/383316/dtcc-barclays-say-tokenizations-real-prize-is-unlocking-idle-collateral)** - Decrypt, 2026-11-16
- **['Nobody Knows Who's in Charge': Boris Johnson Stands by Bitcoin Skepticism at Breakpoint](https://decrypt.co/383307/nobody-knows-whos-in-charge-boris-johnson-stands-by-bitcoin-skepticism-at-breakpoint)** - Decrypt, 2026-11-16

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
