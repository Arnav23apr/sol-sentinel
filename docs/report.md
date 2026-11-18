# Solana Ecosystem Report

*Generated 2026-11-18 11:59 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 5.1 robust standard deviations below its 7-day baseline: a 3.2% move to 13,493,604,130.00 USD from a typical 13,945,080,999.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.4K |
| TPS (non-vote) | 2.4K |
| Slot time | 215.8 ms |
| Slot | 471M |
| Block height | 449M |
| Epoch | 1090 (10.80% complete, ~23.1h remaining) |
| Lifetime transactions | 567.2B |
| Circulating supply | 591.8M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 32.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 660 |
| Delinquent validators | 25 |
| Delinquent stake | 0.01% |
| Total active stake | 426.7M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.48% / 24.98% / 36.21% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.11% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.99% | 0% |
| 2 | `CcaH…oTN1` | 16.5M | 3.86% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.91% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.30% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.24% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.16% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.87% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.59% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $74.47 (+1.54% 24h) |
| Market cap | $44.08B (rank #7) |
| 24h volume | $2.79B |
| ATH | $293.31 (-74.61% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.80B |
| Stablecoin supply | $13.49B |
| DEX volume (24h) | $1.51B (+2.01% 1d) |
| App fees (24h, all protocols) | $8.19M |
| Chain fees (24h) | $445.21K |
| Jito MEV tips (24h) | $121.05K |
| **REV - Real Economic Value (24h)** | **$566.26K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.08B | -0.62% |
| USDT | $2.00B | -6.96% |
| USDGO | $1.02B | -5.36% |
| USD1 | $932.60M | -17.38% |
| PYUSD | $777.43M | -2.30% |
| USDG | $423.42M | -10.87% |
| SOFID | $278.54M | +3.91% |
| USDe | $267.53M | -6.20% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $231.64M |
| Meteora DLMM | $172.72M |
| PumpSwap | $155.29M |
| BisonFi | $149.60M |
| Raydium AMM | $124.09M |
| pump.fun | $114.24M |
| Manifest Trade | $90.80M |
| Scorch | $80.34M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.87M |
| pump.fun | $1.40M |
| Meteora DLMM | $451.91K |
| Axiom | $433.46K |
| Jupiter Perpetual Exchange | $349.86K |
| Raydium AMM | $235.54K |
| Sanctum Validator LSTs | $226.22K |
| Lunar Lander | $210.53K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $86.95M |
| xStocks holder positions | 938.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $562.67M |

## Program activity and chain health

Chain tip lag: **+1.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 107,044 (approx.) | 56.90% | 0.4 s |
| Pump.fun | 59,291 | 78.60% | 0.9 s |
| Orca Whirlpools | 13,471 | 63.90% | 4.3 s |
| Jupiter v6 | 6,243 | 60.70% | 9.5 s |
| Raydium AMM v4 | 2,610 | 15.00% | 22.9 s |

Median failure rate across the sampled programs: **60.70%** (range 15.00% to 78.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.05K SOL**.

## Exchange and large-holder balances

9.50M SOL ($707.60M) across 6 publicly-attributed accounts. Net **108K SOL (1.12%) moved off exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $692.57M | 0.3/h | 2 |
| Gate.io | 59.04K | $4.40M | 154.2/h | 0 |
| Bitget | 55.69K | $4.15M | 1.1K/h | 0 |
| Kraken | 39.93K | $2.97M | 219.8/h | 0 |
| Coinbase (2) | 33.04K | $2.46M | 201/h | 0 |
| Coinbase | 14.07K | $1.05M | 235.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1147 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.252 | 1147 | 0.0000 |
| DEX volume moves with App fees | +0.249 | 1106 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.246 | 1074 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.242 | 1074 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.222 | 1115 | 0.0000 |
| Total TPS moves with Slot time | +0.192 | 1115 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.175 | 1096 | 0.0000 |
| Total TPS moves with Program failure rate | +0.174 | 1096 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 1074 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.129 | 1074 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 74.47 USD | Jupiter (on-chain DEX): 74.40 USD | +0.09% | agree |
| Circulating supply | getSupply (RPC): 591.79M SOL | CoinGecko: 591.79M SOL | -0.00% | agree |

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
