# Solana Ecosystem Report

*Generated 2026-11-15 14:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 213.9 ms |
| Slot | 470M |
| Block height | 448M |
| Epoch | 1087 (41.51% complete, ~15.0h remaining) |
| Lifetime transactions | 566.8B |
| Circulating supply | 591.6M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 1.4M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 38 |
| Delinquent stake | 0.08% |
| Total active stake | 429.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.35% / 24.79% / 35.99% |
| Commission (stake-weighted, delegatable validators) | 3.87% |
| Stake on private (100% commission) validators | 22.95% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.9M | 3.95% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.82% | 7% |
| 3 | `3N7s…iD5g` | 12.6M | 2.94% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.36% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.27% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.25% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.15% | 7% |
| 8 | `9QU2…29mF` | 7.9M | 1.85% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $72.07 (-3.14% 24h) |
| Market cap | $42.64B (rank #7) |
| 24h volume | $5.50B |
| ATH | $293.31 (-75.43% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.74B |
| Stablecoin supply | $14.00B |
| DEX volume (24h) | $1.69B (+8.45% 1d) |
| App fees (24h, all protocols) | $7.95M |
| Chain fees (24h) | $357.11K |
| Jito MEV tips (24h) | $100.22K |
| **REV - Real Economic Value (24h)** | **$457.33K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.39B | +4.75% |
| USDT | $2.00B | -18.00% |
| USDGO | $1.06B | -4.90% |
| USD1 | $1.03B | -16.05% |
| PYUSD | $801.62M | +8.05% |
| USDG | $441.60M | -10.64% |
| USDe | $277.06M | -4.90% |
| SOFID | $273.76M | +2.87% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $327.64M |
| BisonFi | $236.69M |
| PumpSwap | $156.41M |
| Meteora DLMM | $154.87M |
| Scorch | $131.54M |
| Raydium AMM | $124.79M |
| pump.fun | $89.40M |
| Manifest Trade | $80.03M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.48M |
| Jupiter Perpetual Exchange | $1.22M |
| pump.fun | $1.05M |
| Meteora DLMM | $404.81K |
| Axiom | $369.07K |
| Orca DEX | $226.73K |
| Raydium AMM | $201.53K |
| Sanctum Validator LSTs | $200.71K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $46.22M |
| xStocks holder positions | 931.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $589.89M |

## Program activity and chain health

Chain tip lag: **+0.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,781 | 34.40% | 0.9 s |
| Pump.fun | 26,676 | 87.50% | 2.1 s |
| Jupiter v6 | 7,194 | 73.70% | 7.3 s |
| Orca Whirlpools | 5,270 | 60.50% | 11.1 s |
| Raydium AMM v4 | 827 | 17.70% | 72.1 s |

Median failure rate across the sampled programs: **60.50%** (range 17.70% to 87.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.55K SOL**.

## Exchange and large-holder balances

9.49M SOL ($684.16M) across 7 publicly-attributed accounts. Net **48K SOL (0.50%) moved off exchanges** over the last 22.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $670.25M | 0.8/h | 0 |
| Gate.io | 58.43K | $4.21M | 180.2/h | 0 |
| Bybit | 34.57K | $2.49M | 19.3/h | 0 |
| Coinbase (2) | 29.92K | $2.16M | 172.6/h | 0 |
| Coinbase | 28.81K | $2.08M | 166.7/h | 0 |
| Kraken | 25.79K | $1.86M | 203.4/h | 0 |
| Bitget | 15.50K | $1.12M | 142.9/h | 1 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1138 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.246 | 1065 | 0.0000 |
| DEX volume moves with App fees | +0.245 | 1097 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.241 | 1065 | 0.0000 |
| SOL price moves with DeFi TVL | +0.241 | 1138 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 1106 | 0.0000 |
| Total TPS moves with Slot time | +0.192 | 1106 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.173 | 1087 | 0.0000 |
| Total TPS moves with Program failure rate | +0.172 | 1087 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 1065 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.123 | 1065 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 72.07 USD | Jupiter (on-chain DEX): 71.76 USD | +0.43% | agree |
| Circulating supply | getSupply (RPC): 591.63M SOL | CoinGecko: 591.63M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
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

- **[SoFi Brings Its Bank-Issued Stablecoin to Polygon’s Payments Stack](https://decrypt.co/383096/sofi-brings-bank-issued-stablecoin-polygon-payments-stack)** - Decrypt, 2026-11-12
- **[DTCC to Bring Tokenized Stocks and Treasuries to Solana in 2027](https://decrypt.co/383132/dtcc-to-bring-tokenized-stocks-and-treasuries-to-solana-in-2027)** - Decrypt, 2026-11-12
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
