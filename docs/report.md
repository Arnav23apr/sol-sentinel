# Solana Ecosystem Report

*Generated 2026-11-25 15:51 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.7K |
| TPS (non-vote) | 2.7K |
| Slot time | 214.7 ms |
| Slot | 474M |
| Block height | 452M |
| Epoch | 1096 (76.63% complete, ~6.0h remaining) |
| Lifetime transactions | 568.3B |
| Circulating supply | 592.1M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 11.30% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 659 |
| Delinquent validators | 28 |
| Delinquent stake | 0.04% |
| Total active stake | 424.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 25.01% / 36.14% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.21% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 4.00% | 0% |
| 2 | `CcaH…oTN1` | 16.0M | 3.76% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.92% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.9M | 2.33% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.26% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.19% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.89% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.60% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $66.90 (-2.59% 24h) |
| Market cap | $39.61B (rank #7) |
| 24h volume | $2.72B |
| ATH | $293.31 (-77.19% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.45B |
| Stablecoin supply | $12.93B |
| DEX volume (24h) | $1.46B (-19.33% 1d) |
| App fees (24h, all protocols) | $7.15M |
| Chain fees (24h) | $365.96K |
| Jito MEV tips (24h) | $101.87K |
| **REV - Real Economic Value (24h)** | **$467.83K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.87B | -5.54% |
| USDT | $1.88B | -5.99% |
| USDGO | $922.76M | -9.79% |
| USD1 | $867.60M | -8.27% |
| PYUSD | $714.00M | -8.22% |
| USDG | $431.66M | +2.05% |
| SOFID | $278.81M | +0.06% |
| USDe | $242.66M | -9.42% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $190.49M |
| Orca DEX | $184.70M |
| Manifest Trade | $170.96M |
| Raydium AMM | $139.68M |
| Scorch | $134.08M |
| PumpSwap | $114.27M |
| Meteora DLMM | $112.97M |
| pump.fun | $97.42M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.64M |
| pump.fun | $1.24M |
| Axiom | $355.55K |
| Meteora DLMM | $286.36K |
| Jupiter Perpetual Exchange | $285.38K |
| Raydium AMM | $205.65K |
| Sanctum Validator LSTs | $201.71K |
| Lunar Lander | $147.44K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $80.32M |
| xStocks holder positions | 967.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $525.16M |

## Program activity and chain health

Chain tip lag: **+1.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 87,378 | 60.50% | 0.6 s |
| Pump.fun | 47,396 | 84.40% | 1.1 s |
| Jupiter v6 | 13,068 | 74.60% | 4.5 s |
| Orca Whirlpools | 9,905 | 77.10% | 5.8 s |
| Raydium AMM v4 | 1,099 | 18.00% | 54.5 s |

Median failure rate across the sampled programs: **74.60%** (range 18.00% to 84.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **573.37 SOL**.

## Exchange and large-holder balances

9.58M SOL ($640.64M) across 7 publicly-attributed accounts. Net **95K SOL (0.98%) moved off exchanges** over the last 17.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $622.17M | 0.2/h | 3 |
| Gate.io | 98.27K | $6.57M | 323.2/h | 0 |
| Bybit | 59.50K | $3.98M | 187.6/h | 0 |
| Bitget | 42.61K | $2.85M | 153.2/h | 0 |
| Kraken | 39.26K | $2.63M | 383.4/h | 0 |
| Coinbase | 22.62K | $1.51M | 309/h | 0 |
| Coinbase (2) | 13.75K | $919.72K | 286.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1170 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.267 | 1129 | 0.0000 |
| SOL price moves with DeFi TVL | +0.263 | 1170 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.248 | 1097 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.243 | 1097 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.214 | 1138 | 0.0000 |
| Total TPS moves with Slot time | +0.185 | 1138 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.180 | 1119 | 0.0000 |
| Total TPS moves with Program failure rate | +0.179 | 1119 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 1097 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.135 | 1097 | 0.0000 |
| DEX volume moves with REV | +0.120 | 1170 | 0.0000 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 66.90 USD | Jupiter (on-chain DEX): 67.48 USD | -0.86% | agree |
| Circulating supply | getSupply (RPC): 592.13M SOL | CoinGecko: 592.13M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Withdraw SIMD-0506](https://github.com/solana-foundation/solana-improvement-documents/pull/738) - updated 2026-11-25
- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-23

**Recently merged SIMDs:**

- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-23
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01

**Latest Agave release:** [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) (2026-11-19)

**Latest Firedancer release:** [v26.11.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.0) (2026-11-11)

## Ecosystem news

- **[Japan’s SBI, SMFG launch Solana joint venture for stablecoin payments and tokenization](https://www.theblock.co/news/business/2026-11-25-japans-sbi-smfg-tap-solana-stablecoin-tokenization-joint-venture-446131)** - The Block, 2026-11-25
- **[Tom Lee Says Ethereum Is as Scarce as Bitcoin—And Bitmine Just Bought More](https://decrypt.co/383800/tom-lee-ethereum-scarce-bitcoin-bitmine-buys-more)** - Decrypt, 2026-11-23
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
