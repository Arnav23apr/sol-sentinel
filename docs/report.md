# Solana Ecosystem Report

*Generated 2026-11-05 16:35 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.9K |
| TPS (non-vote) | 2.9K |
| Slot time | 214.3 ms |
| Slot | 466M |
| Block height | 444M |
| Epoch | 1078 (18.26% complete, ~21.0h remaining) |
| Lifetime transactions | 565.4B |
| Circulating supply | 590.3M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 16.00% of slots needed a priority fee (max 18.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 663 |
| Delinquent validators | 31 |
| Delinquent stake | 0.13% |
| Total active stake | 430.3M SOL |
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
| 5 | `Catz…Diqb` | 9.5M | 2.21% | 5% |
| 6 | `51JB…UNAm` | 9.5M | 2.20% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.9M | 1.83% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `3JD3…FrXf` | 6.3M | 1.46% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $90.95 (-5.82% 24h) |
| Market cap | $53.69B (rank #7) |
| 24h volume | $4.42B |
| ATH | $293.31 (-68.99% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.48B |
| Stablecoin supply | $14.96B |
| DEX volume (24h) | $2.39B (+26.82% 1d) |
| App fees (24h, all protocols) | $11.23M |
| Chain fees (24h) | $579.75K |
| Jito MEV tips (24h) | $139.20K |
| **REV - Real Economic Value (24h)** | **$718.95K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.19B | +6.08% |
| USDT | $2.56B | -2.66% |
| USD1 | $1.29B | -6.44% |
| USDGO | $1.16B | -10.96% |
| PYUSD | $685.46M | -2.48% |
| BUIDL | $584.94M | -33.22% |
| USDG | $498.57M | -19.75% |
| USDe | $296.92M | -5.74% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $315.41M |
| Orca DEX | $269.12M |
| BisonFi | $241.30M |
| Meteora DLMM | $198.54M |
| Raydium AMM | $188.37M |
| Tessera V | $185.30M |
| pump.fun | $136.47M |
| Manifest Trade | $124.68M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.77M |
| pump.fun | $1.73M |
| Axiom | $715.24K |
| Meteora DLMM | $653.35K |
| Jupiter Perpetual Exchange | $391.42K |
| Raydium AMM | $374.72K |
| Lunar Lander | $303.26K |
| Collector Crypt | $272.11K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $104.69M |
| xStocks holder positions | 883.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $567.57M |

## Program activity and chain health

Chain tip lag: **+0.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 118,432 (approx.) | 95.90% | 0.4 s |
| SPL Token | 65,516 | 64.30% | 0.9 s |
| Jupiter v6 | 16,008 | 63.50% | 3.6 s |
| Orca Whirlpools | 9,577 | 68.90% | 6.2 s |
| Raydium AMM v4 | 2,109 | 36.30% | 27 s |

Median failure rate across the sampled programs: **64.30%** (range 36.30% to 95.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.23K SOL**.

## Exchange and large-holder balances

9.84M SOL ($895.06M) across 7 publicly-attributed accounts. Net **9K SOL (0.10%) moved off exchanges** over the last 19.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $845.84M | 0.2/h | 3 |
| Bybit | 346.93K | $31.55M | 83.7/h | 0 |
| Gate.io | 85.61K | $7.79M | 361.4/h | 0 |
| Coinbase (2) | 37.59K | $3.42M | 294.4/h | 0 |
| Kraken | 32.98K | $3.00M | 310.1/h | 0 |
| Coinbase | 19.85K | $1.81M | 306.1/h | 0 |
| Bitget | 18.29K | $1.66M | 262.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1100 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.251 | 1059 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 1068 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.228 | 1027 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.224 | 1027 | 0.0000 |
| SOL price moves with DeFi TVL | +0.224 | 1100 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1068 | 0.0000 |
| Total TPS moves with Program failure rate | +0.165 | 1049 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.165 | 1049 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.156 | 1027 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.124 | 1027 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 90.95 USD | Jupiter (on-chain DEX): 90.89 USD | +0.07% | agree |
| Circulating supply | getSupply (RPC): 590.32M SOL | CoinGecko: 590.32M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-05

**Open SIMD proposals:**

- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-05
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-04
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-05

**Recently merged SIMDs:**

- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28

**Latest Agave release:** [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28)

**Latest Firedancer release:** [v26.10.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.6) (2026-11-05)

## Ecosystem news

- **[Samsung Wallet launches USDC accounts on Solana for US Galaxy users](https://www.theblock.co/news/business/2026-11-05-samsung-wallet-launches-usdc-accounts-solana-us-galaxy-users-434523)** - The Block, 2026-11-05
- **[Stablecoins Go Mainstream as Samsung Wallet Adds USDC on Solana](https://decrypt.co/382586/stablecoins-samsung-wallet-adds-usdc-solana)** - Decrypt, 2026-11-05
- **[Schroders launches tokenized emerging markets debt fund on Solana with Centrifuge](https://www.theblock.co/news/business/2026-11-04-schroders-centrifuge-tokenized-emerging-markets-debt-fund-solana-432878)** - The Block, 2026-11-04
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
