# Solana Ecosystem Report

*Generated 2026-11-12 03:56 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 3.8 robust standard deviations below its 7-day baseline: a 6.9% move to 83.16 USD from a typical 89.29.
- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 5.7 robust standard deviations below its 7-day baseline: a 4.6% move to 13,948,400,840.00 USD from a typical 14,620,310,095.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.5K |
| TPS (non-vote) | 1.5K |
| Slot time | 214.7 ms |
| Slot | 468M |
| Block height | 446M |
| Epoch | 1084 (21.86% complete, ~20.1h remaining) |
| Lifetime transactions | 566.3B |
| Circulating supply | 591.5M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 10.6M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 37 |
| Delinquent stake | 0.16% |
| Total active stake | 432.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.19% / 24.52% / 36.07% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 22.77% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.88% | 0% |
| 2 | `CcaH…oTN1` | 16.1M | 3.72% | 7% |
| 3 | `3N7s…iD5g` | 13.0M | 3.01% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.34% | 0% |
| 5 | `51JB…UNAm` | 9.7M | 2.24% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.21% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $83.16 (-0.19% 24h) |
| Market cap | $49.20B (rank #7) |
| 24h volume | $2.13B |
| ATH | $293.31 (-71.65% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.06B |
| Stablecoin supply | $13.95B |
| DEX volume (24h) | $1.64B (+22.25% 1d) |
| App fees (24h, all protocols) | $9.32M |
| Chain fees (24h) | $500.87K |
| Jito MEV tips (24h) | $135.57K |
| **REV - Real Economic Value (24h)** | **$636.44K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.02B | -1.27% |
| USDT | $2.15B | -15.99% |
| USD1 | $1.13B | -14.48% |
| USDGO | $1.08B | -7.83% |
| PYUSD | $804.56M | +17.94% |
| USDG | $493.74M | -1.26% |
| USDe | $281.00M | -5.24% |
| SOFID | $269.15M | +3.58% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $395.67M |
| Orca DEX | $205.10M |
| BisonFi | $152.62M |
| Raydium AMM | $147.15M |
| Meteora DLMM | $129.37M |
| Manifest Trade | $101.95M |
| pump.fun | $92.13M |
| Scorch | $84.04M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.25M |
| pump.fun | $1.29M |
| Meteora DLMM | $494.00K |
| Axiom | $487.11K |
| Collector Crypt | $435.05K |
| Raydium AMM | $326.86K |
| Lunar Lander | $271.93K |
| Jupiter Perpetual Exchange | $232.13K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $90.07M |
| xStocks holder positions | 911.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $582.40M |

## Program activity and chain health

Chain tip lag: **+1.1 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 50,918 | 35.20% | 1.1 s |
| Pump.fun | 10,029 | 70.60% | 5.8 s |
| Jupiter v6 | 1,516 | 25.90% | 39.3 s |
| Orca Whirlpools | 1,098 | 44.30% | 54.5 s |
| Raydium AMM v4 | 940 | 11.70% | 63.8 s |

Median failure rate across the sampled programs: **35.20%** (range 11.70% to 70.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **960.49 SOL**.

## Exchange and large-holder balances

9.56M SOL ($795.19M) across 7 publicly-attributed accounts. Net **13K SOL (0.13%) moved off exchanges** over the last 19.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $773.39M | 0.3/h | 5 |
| Bybit | 97.55K | $8.11M | 28.4/h | 0 |
| Gate.io | 57.16K | $4.75M | 117.5/h | 0 |
| Coinbase | 39.27K | $3.27M | 367/h | 0 |
| Kraken | 26.29K | $2.19M | 138.7/h | 0 |
| Coinbase (2) | 23.85K | $1.98M | 267.9/h | 0 |
| Bitget | 18.01K | $1.50M | 86.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1125 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.262 | 1084 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.240 | 1052 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.235 | 1052 | 0.0000 |
| SOL price moves with DeFi TVL | +0.228 | 1125 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.226 | 1093 | 0.0000 |
| Total TPS moves with Slot time | +0.194 | 1093 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.173 | 1074 | 0.0000 |
| Total TPS moves with Program failure rate | +0.172 | 1074 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 1052 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.124 | 1052 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 83.16 USD | Jupiter (on-chain DEX): 83.22 USD | -0.07% | agree |
| Circulating supply | getSupply (RPC): 591.46M SOL | CoinGecko: 591.46M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
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

- **[‘Milestone quarter’: Solana Company reports Q3 revenue growth driven by staking rewards](https://www.theblock.co/news/business/2026-11-11-solana-company-reports-q3-revenue-growth-438448)** - The Block, 2026-11-12
- **[What Are Solana Privacy Rings? Inside Helius’ Privacy Protocol for Solana](https://decrypt.co/resources/what-are-solana-privacy-rings-inside-helius-privacy-protocol-for-solana)** - Decrypt, 2026-11-11
- **[Decrypt Becomes First News Publisher to Offer Perps Trading, Powered by Solana's Phoenix](https://decrypt.co/382992/decrypt-becomes-first-news-publisher-to-offer-perps-trading-powered-by-solanas-phoenix)** - Decrypt, 2026-11-11
- **[Solana's Jupiter Expands Beyond Trading With Token Baskets, Yield Vaults and New Portfolio](https://decrypt.co/382836/solanas-jupiter-expands-beyond-trading-with-token-baskets-yield-vaults-and-new-portfolio)** - Decrypt, 2026-11-10
- **[Decrypt Money Account Gets Confidential Transfers With Solana Privacy Firm Helius](https://decrypt.co/382806/decrypt-money-account-gets-confidential-transfers-with-solana-privacy-firm-helius)** - Decrypt, 2026-11-10
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
