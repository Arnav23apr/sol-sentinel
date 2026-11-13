# Solana Ecosystem Report

*Generated 2026-11-13 22:16 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 3.9 robust standard deviations below its 7-day baseline: a 4.3% move to 13,926,264,631.00 USD from a typical 14,548,278,012.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.6K |
| TPS (non-vote) | 2.6K |
| Slot time | 215.8 ms |
| Slot | 469M |
| Block height | 447M |
| Epoch | 1085 (85.67% complete, ~3.7h remaining) |
| Lifetime transactions | 566.6B |
| Circulating supply | 591.5M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 15.30% of slots needed a priority fee (max 12.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 38 |
| Delinquent stake | 0.13% |
| Total active stake | 431.8M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.23% / 24.58% / 35.96% |
| Commission (stake-weighted, delegatable validators) | 3.82% |
| Stake on private (100% commission) validators | 22.79% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.89% | 0% |
| 2 | `CcaH…oTN1` | 16.1M | 3.74% | 7% |
| 3 | `3N7s…iD5g` | 13.0M | 3.00% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.34% | 0% |
| 5 | `51JB…UNAm` | 9.7M | 2.25% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.22% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.9M | 1.82% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.55% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $78.20 (-3.94% 24h) |
| Market cap | $46.23B (rank #7) |
| 24h volume | $3.09B |
| ATH | $293.31 (-73.34% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.97B |
| Stablecoin supply | $13.93B |
| DEX volume (24h) | $1.50B (-7.06% 1d) |
| App fees (24h, all protocols) | $8.07M |
| Chain fees (24h) | $447.43K |
| Jito MEV tips (24h) | $111.79K |
| **REV - Real Economic Value (24h)** | **$559.22K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.30B | +3.59% |
| USDT | $2.05B | -19.88% |
| USDGO | $1.06B | -8.03% |
| USD1 | $1.04B | -17.26% |
| PYUSD | $746.44M | +9.12% |
| USDG | $461.80M | -7.43% |
| USDe | $277.63M | -6.70% |
| SOFID | $268.32M | +1.60% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $290.16M |
| Orca DEX | $226.84M |
| BisonFi | $147.27M |
| Meteora DLMM | $144.66M |
| Raydium AMM | $135.21M |
| pump.fun | $102.29M |
| Manifest Trade | $81.59M |
| Scorch | $68.83M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.87M |
| pump.fun | $1.36M |
| Meteora DLMM | $655.32K |
| Axiom | $492.53K |
| Jupiter Perpetual Exchange | $407.76K |
| Collector Crypt | $287.48K |
| Raydium AMM | $263.52K |
| Jupiter Lend | $244.53K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $101.37M |
| xStocks holder positions | 928.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $605.84M |

## Program activity and chain health

Chain tip lag: **+0.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 86,191 (approx.) | 53.40% | 0.4 s |
| Pump.fun | 32,982 | 76.70% | 1.7 s |
| Jupiter v6 | 11,168 | 78.00% | 5.2 s |
| Orca Whirlpools | 7,936 | 59.80% | 7.6 s |
| Raydium AMM v4 | 2,308 | 16.20% | 25.7 s |

Median failure rate across the sampled programs: **59.80%** (range 16.20% to 78.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **900.62 SOL**.

## Exchange and large-holder balances

9.51M SOL ($743.60M) across 7 publicly-attributed accounts. Net **27K SOL (0.28%) moved off exchanges** over the last 21.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $727.26M | 0.3/h | 5 |
| Gate.io | 58.76K | $4.60M | 130.2/h | 0 |
| Bybit | 47.55K | $3.72M | 19.3/h | 0 |
| Kraken | 38.42K | $3.00M | 248.4/h | 0 |
| Bitget | 22.67K | $1.77M | 128.4/h | 0 |
| Coinbase (2) | 22.49K | $1.76M | 321.4/h | 0 |
| Coinbase | 19.09K | $1.49M | 376.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1131 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.265 | 1090 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.242 | 1058 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.238 | 1058 | 0.0000 |
| SOL price moves with DeFi TVL | +0.232 | 1131 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.224 | 1099 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 1099 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.174 | 1080 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1080 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.152 | 1058 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.125 | 1058 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 78.20 USD | Jupiter (on-chain DEX): 78.04 USD | +0.20% | agree |
| Circulating supply | getSupply (RPC): 591.51M SOL | CoinGecko: 591.51M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-12
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

- **[SoFi Brings Its Bank-Issued Stablecoin to Polygon’s Payments Stack](https://decrypt.co/383096/sofi-brings-bank-issued-stablecoin-polygon-payments-stack)** - Decrypt, 2026-11-12
- **[DTCC to Bring Tokenized Stocks and Treasuries to Solana in 2027](https://decrypt.co/383132/dtcc-to-bring-tokenized-stocks-and-treasuries-to-solana-in-2027)** - Decrypt, 2026-11-12
- **[What Are Solana Privacy Rings? Inside Helius’ Privacy Protocol for Solana](https://decrypt.co/resources/what-are-solana-privacy-rings-inside-helius-privacy-protocol-for-solana)** - Decrypt, 2026-11-11
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
