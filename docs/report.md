# Solana Ecosystem Report

*Generated 2026-11-06 22:29 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.8K |
| TPS (non-vote) | 1.8K |
| Slot time | 214.3 ms |
| Slot | 466M |
| Block height | 444M |
| Epoch | 1079 (34.59% complete, ~16.8h remaining) |
| Lifetime transactions | 565.6B |
| Circulating supply | 590.3M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 13.30% of slots needed a priority fee (max 696.2K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 659 |
| Delinquent validators | 37 |
| Delinquent stake | 0.32% |
| Total active stake | 433.5M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 24.73% / 36.18% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.06% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.00% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.41% | 0% |
| 5 | `Catz…Diqb` | 9.5M | 2.20% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.7M | 1.79% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.61% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $90.19 (+0.50% 24h) |
| Market cap | $53.24B (rank #7) |
| 24h volume | $2.54B |
| ATH | $293.31 (-69.25% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.24B |
| Stablecoin supply | $14.51B |
| DEX volume (24h) | $2.20B (-7.85% 1d) |
| App fees (24h, all protocols) | $9.71M |
| Chain fees (24h) | $499.44K |
| Jito MEV tips (24h) | $128.53K |
| **REV - Real Economic Value (24h)** | **$627.97K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.01B | +2.61% |
| USDT | $2.44B | +1.66% |
| USD1 | $1.24B | -9.74% |
| USDGO | $1.12B | -12.65% |
| PYUSD | $672.99M | -5.56% |
| BUIDL | $540.61M | -35.45% |
| USDG | $496.62M | -19.85% |
| USDe | $297.46M | -6.13% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $259.46M |
| BisonFi | $231.07M |
| Tessera V | $197.03M |
| PumpSwap | $188.58M |
| Raydium AMM | $173.43M |
| Meteora DLMM | $172.58M |
| Scorch | $147.40M |
| pump.fun | $108.30M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.94M |
| pump.fun | $1.39M |
| Axiom | $534.39K |
| Meteora DLMM | $510.02K |
| Jupiter Perpetual Exchange | $481.93K |
| Raydium AMM | $349.18K |
| Collector Crypt | $290.70K |
| Sanctum Validator LSTs | $249.85K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $71.38M |
| xStocks holder positions | 886.4K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $601.36M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 87,448 | 64.20% | 0.6 s |
| Pump.fun | 72,982 | 93.40% | 0.6 s |
| Orca Whirlpools | 4,137 | 64.30% | 14.4 s |
| Jupiter v6 | 4,000 | 60.10% | 14.1 s |
| Raydium AMM v4 | 694 | 11.40% | 86.4 s |

Median failure rate across the sampled programs: **64.20%** (range 11.40% to 93.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.22K SOL**.

## Exchange and large-holder balances

9.60M SOL ($865.46M) across 7 publicly-attributed accounts. Net **248K SOL (2.52%) moved off exchanges** over the last 19.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $838.77M | 0.2/h | 3 |
| Gate.io | 100.64K | $9.08M | 111.2/h | 0 |
| Bybit | 97.31K | $8.78M | 36.3/h | 0 |
| Kraken | 30.75K | $2.77M | 232.6/h | 0 |
| Coinbase | 23.18K | $2.09M | 310.6/h | 0 |
| Coinbase (2) | 22.90K | $2.07M | 351.2/h | 0 |
| Bitget | 21.12K | $1.90M | 121.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1105 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.252 | 1064 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.231 | 1073 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.230 | 1032 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.225 | 1032 | 0.0000 |
| SOL price moves with DeFi TVL | +0.224 | 1105 | 0.0000 |
| Total TPS moves with Slot time | +0.199 | 1073 | 0.0000 |
| Total TPS moves with Program failure rate | +0.166 | 1054 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.166 | 1054 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1032 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.123 | 1032 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 90.19 USD | Jupiter (on-chain DEX): 90.15 USD | +0.04% | agree |
| Circulating supply | getSupply (RPC): 590.34M SOL | CoinGecko: 590.34M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-06

**Open SIMD proposals:**

- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-06
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-06

**Recently merged SIMDs:**

- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29

**Latest Agave release:** [v4.5.0-beta.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-beta.0) (2026-11-06)

**Latest Firedancer release:** [v26.10.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.6) (2026-11-05)

## Ecosystem news

- **[Solana Labs’ Leap Launches Mobile App for Trading Tokenized Stocks and Crypto](https://decrypt.co/382609/solana-labs-leap-launches-mobile-app-tokenized-stocks-crypto)** - Decrypt, 2026-11-05
- **[Stablecoins Go Mainstream as Samsung Wallet Adds USDC on Solana](https://decrypt.co/382586/stablecoins-samsung-wallet-adds-usdc-solana)** - Decrypt, 2026-11-05
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
