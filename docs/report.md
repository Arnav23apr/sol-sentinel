# Solana Ecosystem Report

*Generated 2026-11-06 10:03 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.1K |
| TPS (non-vote) | 1.1K |
| Slot time | 214.7 ms |
| Slot | 466M |
| Block height | 444M |
| Epoch | 1078 (86.32% complete, ~3.5h remaining) |
| Lifetime transactions | 565.5B |
| Circulating supply | 590.3M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 12.70% of slots needed a priority fee (max 3.9M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 32 |
| Delinquent stake | 0.15% |
| Total active stake | 430.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.52% / 24.78% / 36.04% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.24% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.97% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.89% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.03% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.43% | 0% |
| 5 | `Catz…Diqb` | 9.5M | 2.22% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.9M | 1.83% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.63% | 0% |
| 10 | `3JD3…FrXf` | 6.3M | 1.46% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $90.03 (-6.88% 24h) |
| Market cap | $53.14B (rank #7) |
| 24h volume | $3.70B |
| ATH | $293.31 (-69.31% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.29B |
| Stablecoin supply | $14.54B |
| DEX volume (24h) | $2.18B (-8.51% 1d) |
| App fees (24h, all protocols) | $9.80M |
| Chain fees (24h) | $499.44K |
| Jito MEV tips (24h) | $124.97K |
| **REV - Real Economic Value (24h)** | **$624.41K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.98B | +2.29% |
| USDT | $2.44B | +1.66% |
| USD1 | $1.26B | -8.53% |
| USDGO | $1.13B | -12.02% |
| PYUSD | $669.19M | -6.04% |
| BUIDL | $568.60M | -32.11% |
| USDG | $498.49M | -19.51% |
| USDe | $297.14M | -6.13% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $311.46M |
| BisonFi | $241.30M |
| Meteora DLMM | $198.54M |
| PumpSwap | $188.58M |
| Tessera V | $185.30M |
| Raydium AMM | $177.16M |
| pump.fun | $136.47M |
| Scorch | $109.72M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.94M |
| pump.fun | $1.39M |
| Meteora DLMM | $653.35K |
| Axiom | $534.39K |
| Jupiter Perpetual Exchange | $414.10K |
| Raydium AMM | $367.15K |
| Collector Crypt | $319.88K |
| Orca DEX | $277.68K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $108.79M |
| xStocks holder positions | 885.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $593.33M |

## Program activity and chain health

Chain tip lag: **+0.8 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 33,186 | 41.20% | 1.7 s |
| Pump.fun | 18,644 | 78.70% | 3 s |
| Jupiter v6 | 3,258 | 63.30% | 18.2 s |
| Orca Whirlpools | 1,417 | 49.10% | 42.3 s |
| Raydium AMM v4 | 461 | 10.40% | 129.9 s |

Median failure rate across the sampled programs: **49.10%** (range 10.40% to 78.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.34K SOL**.

## Exchange and large-holder balances

9.59M SOL ($863.68M) across 7 publicly-attributed accounts. Net **248K SOL (2.52%) moved off exchanges** over the last 17.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $837.28M | 0.2/h | 3 |
| Gate.io | 107.80K | $9.71M | 137.4/h | 0 |
| Bybit | 96.93K | $8.73M | 45.1/h | 0 |
| Kraken | 36.61K | $3.30M | 197.4/h | 0 |
| Coinbase | 20.90K | $1.88M | 140.4/h | 0 |
| Coinbase (2) | 20.73K | $1.87M | 168.1/h | 0 |
| Bitget | 10.23K | $921.23K | 111.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1103 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.255 | 1062 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.229 | 1071 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.227 | 1030 | 0.0000 |
| SOL price moves with DeFi TVL | +0.224 | 1103 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.222 | 1030 | 0.0000 |
| Total TPS moves with Slot time | +0.197 | 1071 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.167 | 1052 | 0.0000 |
| Total TPS moves with Program failure rate | +0.166 | 1052 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.157 | 1030 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.123 | 1030 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 90.03 USD | Jupiter (on-chain DEX): 89.98 USD | +0.06% | agree |
| Circulating supply | getSupply (RPC): 590.29M SOL | CoinGecko: 590.29M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-06

**Open SIMD proposals:**

- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-05
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-06

**Recently merged SIMDs:**

- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28

**Latest Agave release:** [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06)

**Latest Firedancer release:** [v26.10.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.6) (2026-11-05)

## Ecosystem news

- **[Solana Labs’ Leap Launches Mobile App for Trading Tokenized Stocks and Crypto](https://decrypt.co/382609/solana-labs-leap-launches-mobile-app-tokenized-stocks-crypto)** - Decrypt, 2026-11-05
- **[Samsung Wallet launches USDC accounts on Solana for US Galaxy users](https://www.theblock.co/news/business/2026-11-05-samsung-wallet-launches-usdc-accounts-solana-us-galaxy-users-434523)** - The Block, 2026-11-05
- **[Stablecoins Go Mainstream as Samsung Wallet Adds USDC on Solana](https://decrypt.co/382586/stablecoins-samsung-wallet-adds-usdc-solana)** - Decrypt, 2026-11-05
- **[Schroders launches tokenized emerging markets debt fund on Solana with Centrifuge](https://www.theblock.co/news/business/2026-11-04-schroders-centrifuge-tokenized-emerging-markets-debt-fund-solana-432878)** - The Block, 2026-11-04
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
