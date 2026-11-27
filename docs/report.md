# Solana Ecosystem Report

*Generated 2026-11-27 00:16 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.7 robust standard deviations above its 7-day baseline: a 233.3% move to 0.06 % from a typical 0.02.
- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 4.0 robust standard deviations below its 7-day baseline: a 5.1% move to 12,429,327,117.00 USD from a typical 13,095,123,390.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 214.7 ms |
| Slot | 474M |
| Block height | 452M |
| Epoch | 1098 (2.25% complete, ~25.2h remaining) |
| Lifetime transactions | 568.6B |
| Circulating supply | 592.2M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 4.00% of slots needed a priority fee (max 1.3M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 654 |
| Delinquent validators | 34 |
| Delinquent stake | 0.06% |
| Total active stake | 424.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.39% / 24.98% / 36.11% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.25% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 15.8M | 3.73% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.93% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.9M | 2.34% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.27% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.19% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.90% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.59% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $70.94 (-0.09% 24h) |
| Market cap | $42.02B (rank #7) |
| 24h volume | $1.78B |
| ATH | $293.31 (-75.81% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.65B |
| Stablecoin supply | $12.43B |
| DEX volume (24h) | $1.51B (+3.72% 1d) |
| App fees (24h, all protocols) | $7.48M |
| Chain fees (24h) | $415.33K |
| Jito MEV tips (24h) | $90.04K |
| **REV - Real Economic Value (24h)** | **$505.37K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.44B | -0.31% |
| USDT | $1.89B | -5.49% |
| USDGO | $923.25M | -9.79% |
| USD1 | $869.31M | -5.73% |
| PYUSD | $735.04M | +4.89% |
| USDG | $374.97M | -12.02% |
| SOFID | $279.80M | +1.27% |
| USDe | $241.47M | -9.76% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $190.65M |
| Orca DEX | $135.13M |
| Meteora DLMM | $119.43M |
| Raydium AMM | $117.21M |
| Scorch | $104.62M |
| PumpSwap | $102.42M |
| pump.fun | $102.41M |
| Jupiterz | $53.10M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.51M |
| pump.fun | $1.27M |
| Axiom | $373.68K |
| Jupiter Perpetual Exchange | $328.25K |
| Meteora DLMM | $286.36K |
| Sanctum Validator LSTs | $243.24K |
| Lunar Lander | $159.66K |
| Raydium AMM | $150.41K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $52.68M |
| xStocks holder positions | 966.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $541.81M |

## Program activity and chain health

Chain tip lag: **+1.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 36,050 | 31.90% | 1.5 s |
| Pump.fun | 8,197 | 35.50% | 7.1 s |
| Jupiter v6 | 1,952 | 32.10% | 30.7 s |
| Orca Whirlpools | 1,729 | 27.30% | 34.4 s |
| Raydium AMM v4 | 811 | 11.00% | 73.6 s |

Median failure rate across the sampled programs: **31.90%** (range 11.00% to 35.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.38K SOL**.

## Exchange and large-holder balances

9.57M SOL ($679.06M) across 6 publicly-attributed accounts. Net **151K SOL (1.55%) moved off exchanges** over the last 18.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $659.74M | 0.2/h | 1 |
| Coinbase (2) | 63.64K | $4.51M | 259.9/h | 0 |
| Bybit | 59.50K | $4.22M | 53.6/h | 0 |
| Bitget | 54.05K | $3.83M | 89.6/h | 0 |
| Coinbase | 53.22K | $3.78M | 217/h | 0 |
| Kraken | 41.92K | $2.97M | 222.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1174 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.269 | 1133 | 0.0000 |
| SOL price moves with DeFi TVL | +0.266 | 1174 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.247 | 1101 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.243 | 1101 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.217 | 1142 | 0.0000 |
| Total TPS moves with Slot time | +0.187 | 1142 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.183 | 1123 | 0.0000 |
| Total TPS moves with Program failure rate | +0.182 | 1123 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 1101 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 1101 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 70.94 USD | Jupiter (on-chain DEX): 71.01 USD | -0.10% | agree |
| Circulating supply | getSupply (RPC): 592.24M SOL | CoinGecko: 592.24M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-24
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-26
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-11-20

**Recently merged SIMDs:**

- [Withdraw SIMD-0506](https://github.com/solana-foundation/solana-improvement-documents/pull/738) - updated 2026-11-26
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-23
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01

**Latest Agave release:** [v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) (2026-11-25)

**Latest Firedancer release:** [v26.11.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.1) (2026-11-25)

## Ecosystem news

- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
