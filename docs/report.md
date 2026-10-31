# Solana Ecosystem Report

*Generated 2026-10-31 00:15 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **DeFi TVL** (critical): DeFi TVL is 8.2 robust standard deviations below its 7-day baseline: a 5.2% move to 5,437,124,766.00 USD from a typical 5,733,327,776.00.
- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.8 robust standard deviations above its 7-day baseline: a 425.2% move to 0.65 % from a typical 0.12.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.4K |
| TPS (non-vote) | 1.4K |
| Slot time | 214.7 ms |
| Slot | 463M |
| Block height | 442M |
| Epoch | 1072 (87.77% complete, ~3.2h remaining) |
| Lifetime transactions | 564.5B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 26.00% of slots needed a priority fee (max 2.8M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 666 |
| Delinquent validators | 25 |
| Delinquent stake | 0.65% |
| Total active stake | 432.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.43% / 24.79% / 36.02% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.15% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 12.9M | 2.99% | 0% |
| 4 | `8Gbw…F8iD` | 10.5M | 2.43% | 0% |
| 5 | `Catz…Diqb` | 9.7M | 2.23% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.19% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.80% | 7% |
| 9 | `CvSb…wycB` | 7.0M | 1.63% | 5% |
| 10 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $96.28 (+1.05% 24h) |
| Market cap | $56.81B (rank #7) |
| 24h volume | $4.04B |
| ATH | $293.31 (-67.17% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.44B |
| Stablecoin supply | $15.24B |
| DEX volume (24h) | $2.30B (+32.42% 1d) |
| App fees (24h, all protocols) | $12.33M |
| Chain fees (24h) | $564.52K |
| Jito MEV tips (24h) | $115.70K |
| **REV - Real Economic Value (24h)** | **$680.22K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.99B | +2.54% |
| USDT | $2.40B | -12.71% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.26B | -3.64% |
| BUIDL | $812.65M | -8.31% |
| PYUSD | $687.84M | -6.66% |
| USDG | $614.09M | -2.52% |
| USDe | $315.75M | -12.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $353.37M |
| BisonFi | $301.26M |
| Manifest Trade | $217.92M |
| Tessera V | $209.29M |
| Raydium AMM | $200.04M |
| Scorch | $194.06M |
| Meteora DLMM | $130.28M |
| pump.fun | $127.30M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.70M |
| pump.fun | $1.71M |
| Meteora DLMM | $883.32K |
| Collector Crypt | $783.77K |
| Jupiter Perpetual Exchange | $736.57K |
| Axiom | $716.50K |
| Raydium AMM | $363.57K |
| Orca DEX | $295.37K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $91.46M |
| xStocks holder positions | 870.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $615.80M |

## Program activity and chain health

Chain tip lag: **+1.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 61,202 | 51.40% | 0.9 s |
| Pump.fun | 17,867 | 78.30% | 3.2 s |
| Orca Whirlpools | 4,794 | 55.80% | 12.5 s |
| Jupiter v6 | 3,440 | 47.10% | 17.4 s |
| Raydium AMM v4 | 1,148 | 43.50% | 52.2 s |

Median failure rate across the sampled programs: **51.40%** (range 43.50% to 78.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **116.00 SOL**.

## Exchange and large-holder balances

12.88M SOL ($1.24B) across 7 publicly-attributed accounts. Net **142K SOL (1.11%) moved onto exchanges** over the last 21.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.89M | $1.14B | 0.2/h | 6 |
| Gate.io | 350.21K | $33.72M | 207.4/h | 0 |
| Bybit | 339.48K | $32.69M | 37.3/h | 0 |
| Bitget | 135.27K | $13.02M | 131.1/h | 0 |
| Coinbase (2) | 113.91K | $10.97M | 348.2/h | 0 |
| Kraken | 34.16K | $3.29M | 400/h | 0 |
| Coinbase | 21.57K | $2.08M | 264.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1079 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.257 | 1038 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.233 | 1045 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.222 | 1004 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.217 | 1004 | 0.0000 |
| SOL price moves with DeFi TVL | +0.216 | 1079 | 0.0000 |
| Total TPS moves with Slot time | +0.200 | 1045 | 0.0000 |
| Total TPS moves with Program failure rate | +0.168 | 1026 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.168 | 1026 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1004 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.119 | 1004 | 0.0002 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 96.28 USD | Jupiter (on-chain DEX): 96.26 USD | +0.02% | agree |
| Circulating supply | getSupply (RPC): 590.04M SOL | CoinGecko: 590.04M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-10-30
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23

**Recently merged SIMDs:**

- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28
- [Amend SIMD-0607: Derive per-slot decay and increase intermediate precision](https://github.com/solana-foundation/solana-improvement-documents/pull/642) - updated 2026-10-28
- [SIMD-0140: Migrate Config Program to Core BPF](https://github.com/solana-foundation/solana-improvement-documents/pull/140) - updated 2026-10-28
- [SIMD-0133: Syscall: Get Epoch Stake](https://github.com/solana-foundation/solana-improvement-documents/pull/133) - updated 2026-10-28
- [SIMD-0089: Programify Feature Gate Program](https://github.com/solana-foundation/solana-improvement-documents/pull/89) - updated 2026-10-28

**Latest Agave release:** [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28)

**Latest Firedancer release:** [v26.10.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.5) (2026-10-27)

## Ecosystem news

- **[Polygon Extends Its Stablecoin Payments Infrastructure to Solana](https://decrypt.co/381850/polygon-stablecoin-payments-open-money-stack-solana)** - Decrypt, 2026-10-29
- **[Polygon adds Solana to payment stack linking bank accounts, crypto and payouts](https://www.theblock.co/news/defi/2026-10-29-polygon-adds-solana-payment-stack-432115)** - The Block, 2026-10-29
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
