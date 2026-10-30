# Solana Ecosystem Report

*Generated 2026-10-30 16:04 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 6.1 robust standard deviations below its 7-day baseline: a 6.6% move to 94.50 USD from a typical 101.15.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 10.9 robust standard deviations below its 7-day baseline: a 6.9% move to 5,347,716,175.00 USD from a typical 5,741,345,754.50.
- 🟠 **Delinquent stake** (warning): Delinquent stake is 4.6 robust standard deviations above its 7-day baseline: a 406.5% move to 0.62 % from a typical 0.12.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.1K |
| TPS (non-vote) | 2.1K |
| Slot time | 214.3 ms |
| Slot | 463M |
| Block height | 441M |
| Epoch | 1072 (56.01% complete, ~11.3h remaining) |
| Lifetime transactions | 564.5B |
| Circulating supply | 590.0M SOL |
| Inflation (annual) | 3.58% |
| AMM write-lock congestion (150-slot window) | 10.00% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 667 |
| Delinquent validators | 24 |
| Delinquent stake | 0.62% |
| Total active stake | 432.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.42% / 24.79% / 36.02% |
| Commission (stake-weighted, delegatable validators) | 3.72% |
| Stake on private (100% commission) validators | 24.15% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.85% | 0% |
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
| SOL price | $94.50 (-7.83% 24h) |
| Market cap | $55.77B (rank #7) |
| 24h volume | $5.86B |
| ATH | $293.31 (-67.78% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.35B |
| Stablecoin supply | $15.15B |
| DEX volume (24h) | $2.30B (+32.42% 1d) |
| App fees (24h, all protocols) | $12.33M |
| Chain fees (24h) | $564.52K |
| Jito MEV tips (24h) | $134.75K |
| **REV - Real Economic Value (24h)** | **$699.28K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.87B | +0.83% |
| USDT | $2.40B | -12.71% |
| USD1 | $1.38B | -0.95% |
| USDGO | $1.26B | -3.64% |
| BUIDL | $837.56M | -5.50% |
| PYUSD | $684.42M | -7.08% |
| USDG | $619.25M | -1.61% |
| USDe | $316.06M | -11.90% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $456.29M |
| BisonFi | $301.26M |
| Manifest Trade | $266.14M |
| Tessera V | $209.29M |
| Raydium AMM | $202.35M |
| Scorch | $194.06M |
| Meteora DLMM | $130.28M |
| pump.fun | $127.30M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.70M |
| pump.fun | $1.71M |
| Meteora DLMM | $883.32K |
| Collector Crypt | $740.67K |
| Jupiter Perpetual Exchange | $736.57K |
| Axiom | $716.50K |
| Raydium AMM | $421.51K |
| Orca DEX | $399.67K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $56.67M |
| xStocks holder positions | 859.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $612.57M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 91,134 (approx.) | 69.30% | 0.4 s |
| Pump.fun | 51,293 | 94.60% | 1.1 s |
| Orca Whirlpools | 13,279 | 55.60% | 4.5 s |
| Jupiter v6 | 7,476 | 69.30% | 7.9 s |
| Raydium AMM v4 | 1,190 | 16.00% | 50.4 s |

Median failure rate across the sampled programs: **69.30%** (range 16.00% to 94.60%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **116.00 SOL**.

## Exchange and large-holder balances

12.87M SOL ($1.22B) across 7 publicly-attributed accounts. Net **704K SOL (5.19%) moved off exchanges** over the last 20.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 11.89M | $1.12B | 0.2/h | 6 |
| Gate.io | 354.18K | $33.47M | 302.8/h | 0 |
| Bybit | 339.48K | $32.08M | 208.5/h | 0 |
| Coinbase (2) | 116.30K | $10.99M | 334.9/h | 0 |
| Bitget | 104.72K | $9.90M | 361.4/h | 0 |
| Kraken | 51.47K | $4.86M | 314.1/h | 0 |
| Coinbase | 14.18K | $1.34M | 323.7/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1077 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.258 | 1036 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.233 | 1043 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.221 | 1002 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.216 | 1002 | 0.0000 |
| SOL price moves with DeFi TVL | +0.216 | 1077 | 0.0000 |
| Total TPS moves with Slot time | +0.200 | 1043 | 0.0000 |
| Total TPS moves with Program failure rate | +0.166 | 1024 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.166 | 1024 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1002 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| AMM write-lock congestion moves with Program failure rate | +0.116 | 1002 | 0.0002 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 94.50 USD | Jupiter (on-chain DEX): 94.50 USD | 0.00% | agree |
| Circulating supply | getSupply (RPC): 590.04M SOL | CoinGecko: 590.04M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-10-23

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-10-30
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-10-30
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: disable `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-10-28
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-10-23
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

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
