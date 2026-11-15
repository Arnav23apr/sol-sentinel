# Solana Ecosystem Report

*Generated 2026-11-15 00:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price move** (warning): SOL moved -10.5% in 24h.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 3.8 robust standard deviations below its 7-day baseline: a 8.2% move to 4,633,209,028.00 USD from a typical 5,047,847,280.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.3K |
| TPS (non-vote) | 2.3K |
| Slot time | 215.8 ms |
| Slot | 470M |
| Block height | 448M |
| Epoch | 1086 (87.23% complete, ~3.3h remaining) |
| Lifetime transactions | 566.7B |
| Circulating supply | 591.6M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 18.00% of slots needed a priority fee (max 4.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 37 |
| Delinquent stake | 0.09% |
| Total active stake | 429.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.33% / 24.74% / 35.91% |
| Commission (stake-weighted, delegatable validators) | 3.86% |
| Stake on private (100% commission) validators | 22.94% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.95% | 0% |
| 2 | `CcaH…oTN1` | 16.4M | 3.81% | 7% |
| 3 | `3N7s…iD5g` | 12.6M | 2.94% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.36% | 0% |
| 5 | `51JB…UNAm` | 9.7M | 2.27% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.23% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.9M | 1.84% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $70.08 (-10.49% 24h) |
| Market cap | $41.46B (rank #7) |
| 24h volume | $4.44B |
| ATH | $293.31 (-76.11% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.63B |
| Stablecoin supply | $13.94B |
| DEX volume (24h) | $1.58B (+1.35% 1d) |
| App fees (24h, all protocols) | $8.65M |
| Chain fees (24h) | $448.75K |
| Jito MEV tips (24h) | $106.73K |
| **REV - Real Economic Value (24h)** | **$555.48K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.33B | +4.44% |
| USDT | $2.00B | -18.00% |
| USDGO | $1.06B | -4.90% |
| USD1 | $1.03B | -17.39% |
| PYUSD | $802.98M | +10.16% |
| USDG | $445.13M | -9.89% |
| USDe | $276.94M | -6.30% |
| SOFID | $273.72M | +2.87% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $284.65M |
| BisonFi | $186.88M |
| PumpSwap | $177.25M |
| Meteora DLMM | $164.81M |
| Raydium AMM | $136.33M |
| pump.fun | $108.58M |
| Scorch | $80.26M |
| Manifest Trade | $64.60M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.04M |
| pump.fun | $1.38M |
| Meteora DLMM | $608.79K |
| Jupiter Perpetual Exchange | $577.30K |
| Axiom | $451.15K |
| Raydium AMM | $229.03K |
| Sanctum Validator LSTs | $212.33K |
| Orca DEX | $203.68K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $59.41M |
| xStocks holder positions | 932.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $592.25M |

## Program activity and chain health

Chain tip lag: **+0.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 78,128 | 51.80% | 0.6 s |
| Pump.fun | 48,656 | 83.80% | 1.1 s |
| Orca Whirlpools | 5,646 | 30.20% | 10.6 s |
| Jupiter v6 | 5,561 | 63.20% | 10.6 s |
| Raydium AMM v4 | 2,347 | 7.90% | 25.5 s |

Median failure rate across the sampled programs: **51.80%** (range 7.90% to 83.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.16K SOL**.

## Exchange and large-holder balances

9.45M SOL ($662.60M) across 6 publicly-attributed accounts. Net **27K SOL (0.29%) moved off exchanges** over the last 22.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $651.74M | 0.3/h | 5 |
| Gate.io | 36.90K | $2.59M | 325.2/h | 0 |
| Kraken | 33.57K | $2.35M | 262.6/h | 0 |
| Coinbase | 32.30K | $2.26M | 309/h | 0 |
| Coinbase (2) | 29.29K | $2.05M | 288.9/h | 0 |
| Bitget | 22.85K | $1.60M | 142.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1136 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.252 | 1095 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.245 | 1063 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.241 | 1063 | 0.0000 |
| SOL price moves with DeFi TVL | +0.239 | 1136 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 1104 | 0.0000 |
| Total TPS moves with Slot time | +0.192 | 1104 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.175 | 1085 | 0.0000 |
| Total TPS moves with Program failure rate | +0.174 | 1085 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 1063 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.124 | 1063 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 70.08 USD | Jupiter (on-chain DEX): 69.74 USD | +0.49% | agree |
| Circulating supply | getSupply (RPC): 591.57M SOL | CoinGecko: 591.57M SOL | -0.00% | agree |

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

⚠️ *Sections served from the previous snapshot due to source errors this run: dev.*

<details><summary>Collection errors this run</summary>

- `dev`: `FetchError('https://api.github.com/repos/solana-foundation/solana-improvement-documents/pulls?state=open&per_page=30 -> HTTP 403')`

</details>
