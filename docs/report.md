# Solana Ecosystem Report

*Generated 2026-11-16 22:23 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.2K |
| TPS (non-vote) | 2.2K |
| Slot time | 215.1 ms |
| Slot | 470M |
| Block height | 448M |
| Epoch | 1088 (65.20% complete, ~9.0h remaining) |
| Lifetime transactions | 567.0B |
| Circulating supply | 591.7M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 34.00% of slots needed a priority fee (max 20.3M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 37 |
| Delinquent stake | 0.04% |
| Total active stake | 429.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.34% / 24.77% / 36.00% |
| Commission (stake-weighted, delegatable validators) | 3.87% |
| Stake on private (100% commission) validators | 22.97% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.9M | 3.95% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.83% | 7% |
| 3 | `3N7s…iD5g` | 12.5M | 2.91% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.36% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.28% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.24% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.86% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $71.97 (-0.33% 24h) |
| Market cap | $42.59B (rank #7) |
| 24h volume | $2.66B |
| ATH | $293.31 (-75.46% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.73B |
| Stablecoin supply | $14.02B |
| DEX volume (24h) | $1.35B (-20.09% 1d) |
| App fees (24h, all protocols) | $7.20M |
| Chain fees (24h) | $353.01K |
| Jito MEV tips (24h) | $120.35K |
| **REV - Real Economic Value (24h)** | **$473.36K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.63B | +9.21% |
| USDT | $2.00B | -18.00% |
| USDGO | $1.03B | -7.67% |
| USD1 | $976.48M | -19.75% |
| PYUSD | $674.30M | -9.12% |
| USDG | $446.56M | -9.80% |
| USDe | $276.47M | -4.56% |
| SOFID | $273.64M | +2.87% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $203.31M |
| BisonFi | $158.79M |
| PumpSwap | $142.79M |
| Raydium AMM | $132.60M |
| Meteora DLMM | $119.67M |
| Scorch | $88.68M |
| pump.fun | $87.48M |
| Manifest Trade | $85.85M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.44M |
| pump.fun | $1.13M |
| Jupiter Perpetual Exchange | $599.47K |
| Axiom | $350.35K |
| Meteora DLMM | $274.74K |
| Raydium AMM | $242.67K |
| Sanctum Validator LSTs | $214.03K |
| Lunar Lander | $204.46K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $63.41M |
| xStocks holder positions | 935.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $581.33M |

## Program activity and chain health

Chain tip lag: **+1.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 95,955 (approx.) | 58.60% | 0.4 s |
| Pump.fun | 52,273 | 88.50% | 1.1 s |
| Orca Whirlpools | 19,376 | 47.30% | 2.8 s |
| Jupiter v6 | 13,487 | 84.80% | 4.3 s |
| Raydium AMM v4 | 5,800 | 23.30% | 10.3 s |

Median failure rate across the sampled programs: **58.60%** (range 23.30% to 88.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.55K SOL**.

## Exchange and large-holder balances

9.59M SOL ($690.47M) across 7 publicly-attributed accounts. Net **89K SOL (0.93%) moved onto exchanges** over the last 22.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $669.32M | 0.3/h | 2 |
| Coinbase (2) | 72.55K | $5.22M | 317.7/h | 0 |
| Bybit | 67.81K | $4.88M | 35.1/h | 0 |
| Gate.io | 60.90K | $4.38M | 114.4/h | 0 |
| Kraken | 33.99K | $2.45M | 257/h | 0 |
| Bitget | 32.70K | $2.35M | 358.6/h | 0 |
| Coinbase | 25.83K | $1.86M | 349.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1142 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.249 | 1069 | 0.0000 |
| DEX volume moves with App fees | +0.249 | 1101 | 0.0000 |
| SOL price moves with DeFi TVL | +0.246 | 1142 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.244 | 1069 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 1110 | 0.0000 |
| Total TPS moves with Slot time | +0.192 | 1110 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.175 | 1091 | 0.0000 |
| Total TPS moves with Program failure rate | +0.174 | 1091 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 1069 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.126 | 1069 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 71.97 USD | Jupiter (on-chain DEX): 71.93 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 591.68M SOL | CoinGecko: 591.68M SOL | -0.00% | agree |

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

- **[Bitwise sees Solana reaching $1,100 by 2031 in bull case as onchain trading grows](https://www.theblock.co/news/markets/2026-11-16-bitwise-solana-price-prediction-1100-2031-441407)** - The Block, 2026-11-16
- **[Privacy on Solana is ‘non-negotiable’ for institutional adoption, Mert Mumtaz says](https://www.theblock.co/news/ecosystems/2026-11-16-privacy-solana-non-negotiable-institutional-adoption-mert-mumtaz-says-441363)** - The Block, 2026-11-16
- **['Tokenization Is Not the Finish Line': Jupiter to Let Users Borrow Against Bullish Shares](https://decrypt.co/383333/tokenization-is-not-the-finish-line-jupiter-to-let-users-borrow-against-bullish-shares)** - Decrypt, 2026-11-16
- **[Boris Johnson backs tokenization months after likening bitcoin to a ‘Ponzi scheme’](https://www.theblock.co/news/regulation/2026-11-16-boris-johnson-backs-tokenization-months-after-bitcoin-to-ponzi-scheme-441368)** - The Block, 2026-11-16
- **[DeFi Development Corp. adds 9,482 SOL as CHAD dividend streak hits 31 days](https://www.theblock.co/news/markets/2026-11-16-defi-development-solana-treasury-2-62-million-sol-441361)** - The Block, 2026-11-16
- **[Solana Drops 'Mainnet Beta' After Six Years: Here's What 1.0 Is All About](https://decrypt.co/383322/solana-drops-mainnet-beta-after-six-years)** - Decrypt, 2026-11-16
- **[DTCC, Barclays Say Tokenization's Real Prize Is Unlocking Idle Collateral](https://decrypt.co/383316/dtcc-barclays-say-tokenizations-real-prize-is-unlocking-idle-collateral)** - Decrypt, 2026-11-16
- **['Nobody Knows Who's in Charge': Boris Johnson Stands by Bitcoin Skepticism at Breakpoint](https://decrypt.co/383307/nobody-knows-whos-in-charge-boris-johnson-stands-by-bitcoin-skepticism-at-breakpoint)** - Decrypt, 2026-11-16
- **[Ledger Brings Clear Signing to Solana, Ending 'Blind' Signing for Jupiter Swaps](https://decrypt.co/383302/ledger-brings-clear-signing-to-solana-ending-blind-signing-for-jupiter-swaps)** - Decrypt, 2026-11-16
- **[Solana drops ‘mainnet beta’ label and adopts protocol version 1.0](https://www.theblock.co/news/ecosystems/2026-11-16-solana-drops-mainnet-beta-label-and-adopts-protocol-version-1-0-440885)** - The Block, 2026-11-16

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
