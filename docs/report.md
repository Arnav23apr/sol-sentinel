# Solana Ecosystem Report

*Generated 2026-11-04 06:45 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 7.2 robust standard deviations below its 7-day baseline: a 4.1% move to 14,562,802,467.00 USD from a typical 15,181,872,435.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.4K |
| TPS (non-vote) | 1.4K |
| Slot time | 214.7 ms |
| Slot | 465M |
| Block height | 443M |
| Epoch | 1076 (86.55% complete, ~3.5h remaining) |
| Lifetime transactions | 565.1B |
| Circulating supply | 590.2M SOL |
| Inflation (annual) | 3.57% |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 15.2M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 666 |
| Delinquent validators | 27 |
| Delinquent stake | 0.42% |
| Total active stake | 432.9M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.42% / 24.77% / 36.15% |
| Commission (stake-weighted, delegatable validators) | 3.73% |
| Stake on private (100% commission) validators | 24.09% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.7M | 3.86% | 0% |
| 3 | `3N7s…iD5g` | 13.0M | 3.01% | 0% |
| 4 | `8Gbw…F8iD` | 10.4M | 2.41% | 0% |
| 5 | `Catz…Diqb` | 9.6M | 2.21% | 5% |
| 6 | `51JB…UNAm` | 9.4M | 2.18% | 10% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `CvSb…wycB` | 7.0M | 1.61% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $92.77 (+1.20% 24h) |
| Market cap | $54.78B (rank #7) |
| 24h volume | $2.63B |
| ATH | $293.31 (-68.37% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.40B |
| Stablecoin supply | $14.56B |
| DEX volume (24h) | $1.87B (+1.13% 1d) |
| App fees (24h, all protocols) | $11.43M |
| Chain fees (24h) | $479.80K |
| Jito MEV tips (24h) | $135.72K |
| **REV - Real Economic Value (24h)** | **$615.52K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.94B | +3.29% |
| USDT | $2.27B | -19.18% |
| USD1 | $1.36B | -1.11% |
| USDGO | $1.18B | -8.92% |
| PYUSD | $675.59M | -2.69% |
| BUIDL | $672.81M | -23.37% |
| USDG | $470.95M | -23.08% |
| USDe | $297.28M | -6.18% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $321.84M |
| BisonFi | $250.54M |
| Orca DEX | $229.97M |
| Raydium AMM | $163.16M |
| Tessera V | $149.85M |
| Manifest Trade | $128.17M |
| pump.fun | $123.08M |
| GoonFi | $110.91M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.82M |
| pump.fun | $1.61M |
| Pyth Pro | $1.04M |
| Axiom | $586.96K |
| Meteora DLMM | $287.28K |
| Raydium AMM | $287.06K |
| Lunar Lander | $273.86K |
| Sanctum Validator LSTs | $263.81K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $56.96M |
| xStocks holder positions | 874.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $569.66M |

## Program activity and chain health

Chain tip lag: **+1.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 40,568 | 41.50% | 1.3 s |
| Pump.fun | 27,418 | 92.80% | 1.9 s |
| Jupiter v6 | 7,716 | 85.60% | 7.7 s |
| Orca Whirlpools | 5,056 | 61.50% | 11.8 s |
| Raydium AMM v4 | 727 | 40.50% | 82.4 s |

Median failure rate across the sampled programs: **61.50%** (range 40.50% to 92.80%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **634.94 SOL**.

## Exchange and large-holder balances

9.86M SOL ($914.45M) across 7 publicly-attributed accounts. Net **542K SOL (5.21%) moved off exchanges** over the last 18.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $862.76M | 0.3/h | 3 |
| Bybit | 339.40K | $31.49M | 45.5/h | 0 |
| Gate.io | 109.92K | $10.20M | 162.3/h | 0 |
| Kraken | 37.06K | $3.44M | 147.8/h | 0 |
| Coinbase | 24.48K | $2.27M | 288/h | 0 |
| Coinbase (2) | 24.27K | $2.25M | 160.4/h | 0 |
| Bitget | 22.04K | $2.04M | 153.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1095 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.255 | 1054 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.230 | 1063 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.226 | 1022 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.222 | 1022 | 0.0000 |
| SOL price moves with DeFi TVL | +0.220 | 1095 | 0.0000 |
| Total TPS moves with Slot time | +0.198 | 1063 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.162 | 1044 | 0.0000 |
| Total TPS moves with Program failure rate | +0.161 | 1044 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.158 | 1022 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.120 | 1022 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 92.77 USD | Jupiter (on-chain DEX): 92.70 USD | +0.08% | agree |
| Circulating supply | getSupply (RPC): 590.21M SOL | CoinGecko: 590.21M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *open*, updated 2026-11-03
- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17

**Open SIMD proposals:**

- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-03
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-10-27
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_` again](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-03
- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-03
- [amend SIMD-0083: Update feature identifier in relax entry constraints proposal](https://github.com/solana-foundation/solana-improvement-documents/pull/691) - updated 2026-10-26

**Recently merged SIMDs:**

- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31
- [docs: align SIMD-0550 with the integer inflation schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/704) - updated 2026-10-29
- [Mark SIMDs as Activated](https://github.com/solana-foundation/solana-improvement-documents/pull/710) - updated 2026-10-28

**Latest Agave release:** [v4.4.0](https://github.com/anza-xyz/agave/releases/tag/v4.4.0) (2026-10-28)

**Latest Firedancer release:** [v26.10.5](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.5) (2026-10-27)

## Ecosystem news

- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
