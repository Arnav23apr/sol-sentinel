# Solana Ecosystem Report

*Generated 2026-11-19 18:43 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 6.9 robust standard deviations below its 7-day baseline: a 7.1% move to 12,952,472,323.00 USD from a typical 13,939,097,084.00.
- 🟠 **App fees (24h, all protocols)** (warning): App fees (24h, all protocols) is 5.1 robust standard deviations above its 7-day baseline: a 32.4% move to 10,954,886.00 USD from a typical 8,274,171.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.3K |
| TPS (non-vote) | 2.3K |
| Slot time | 214.3 ms |
| Slot | 471M |
| Block height | 449M |
| Epoch | 1091 (29.71% complete, ~18.1h remaining) |
| Lifetime transactions | 567.5B |
| Circulating supply | 591.9M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 13.30% of slots needed a priority fee (max 1,000.0K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 659 |
| Delinquent validators | 26 |
| Delinquent stake | 0.03% |
| Total active stake | 428.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.85% / 36.01% |
| Commission (stake-weighted, delegatable validators) | 3.86% |
| Stake on private (100% commission) validators | 23.01% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.82% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.90% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.40% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.29% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.23% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.86% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.58% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $74.50 (+0.74% 24h) |
| Market cap | $44.09B (rank #7) |
| 24h volume | $2.04B |
| ATH | $293.31 (-74.60% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.76B |
| Stablecoin supply | $12.95B |
| DEX volume (24h) | $1.82B (+20.25% 1d) |
| App fees (24h, all protocols) | $10.95M |
| Chain fees (24h) | $560.49K |
| Jito MEV tips (24h) | $130.95K |
| **REV - Real Economic Value (24h)** | **$691.44K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.71B | -4.52% |
| USDT | $1.94B | -9.75% |
| USDGO | $1.00B | -7.21% |
| USD1 | $902.77M | -20.04% |
| PYUSD | $690.68M | -14.21% |
| USDG | $436.94M | -11.52% |
| SOFID | $276.22M | +2.74% |
| USDe | $265.65M | -5.53% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $330.65M |
| Orca DEX | $248.34M |
| Meteora DLMM | $246.17M |
| Raydium AMM | $208.82M |
| BisonFi | $153.98M |
| Manifest Trade | $128.20M |
| pump.fun | $127.79M |
| Scorch | $79.90M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.01M |
| pump.fun | $1.72M |
| Meteora DLMM | $927.79K |
| Axiom | $817.38K |
| Jupiter Perpetual Exchange | $302.08K |
| Lunar Lander | $273.63K |
| Raydium AMM | $272.40K |
| fomo Wallet | $265.92K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $60.79M |
| xStocks holder positions | 940.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $559.48M |

## Program activity and chain health

Chain tip lag: **+1.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 75,782 | 44.40% | 0.6 s |
| Pump.fun | 23,238 | 74.60% | 2.4 s |
| Jupiter v6 | 5,488 | 63.70% | 10.7 s |
| Orca Whirlpools | 4,943 | 56.80% | 11.8 s |
| Raydium AMM v4 | 1,908 | 8.90% | 31.3 s |

Median failure rate across the sampled programs: **56.80%** (range 8.90% to 74.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **935.75 SOL**.

## Exchange and large-holder balances

9.70M SOL ($722.91M) across 7 publicly-attributed accounts. Net **65K SOL (0.67%) moved off exchanges** over the last 22.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $692.85M | 0.3/h | 2 |
| Bybit | 133.49K | $9.94M | 32.7/h | 0 |
| Coinbase | 86.34K | $6.43M | 287.8/h | 0 |
| Gate.io | 68.75K | $5.12M | 209.1/h | 0 |
| Kraken | 43.91K | $3.27M | 268.5/h | 0 |
| Bitget | 40.87K | $3.04M | 8.0K/h | 0 |
| Coinbase (2) | 30.14K | $2.25M | 340.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1151 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.255 | 1151 | 0.0000 |
| DEX volume moves with App fees | +0.254 | 1110 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.248 | 1078 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.244 | 1078 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.221 | 1119 | 0.0000 |
| Total TPS moves with Slot time | +0.190 | 1119 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.179 | 1100 | 0.0000 |
| Total TPS moves with Program failure rate | +0.178 | 1100 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 1078 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.131 | 1078 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 74.50 USD | Jupiter (on-chain DEX): 74.32 USD | +0.24% | agree |
| Circulating supply | getSupply (RPC): 591.85M SOL | CoinGecko: 591.85M SOL | -0.00% | agree |

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

- **[Why CoinShares Just Sold All Its Ethereum and Half Its Solana](https://decrypt.co/383570/why-coinshares-just-sold-all-ethereum-half-solana)** - Decrypt, 2026-11-18
- **[AI Will Make the Next 12 Months 'a Slaughterhouse' for Crypto Security: Anchorage Exec](https://decrypt.co/383526/ai-will-make-the-next-12-months-a-slaughterhouse-for-crypto-security-anchorage-exec)** - Decrypt, 2026-11-18
- **[Standard Life Chair Wants Tokenized Gilts to Open UK Government Bonds to Retail Savers](https://decrypt.co/383434/standard-life-chair-wants-tokenized-gilts-to-open-uk-government-bonds-to-retail-savers)** - Decrypt, 2026-11-17
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
