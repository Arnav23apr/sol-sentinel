# Solana Ecosystem Report

*Generated 2026-11-15 23:37 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.6K |
| TPS (non-vote) | 1.6K |
| Slot time | 216.2 ms |
| Slot | 470M |
| Block height | 448M |
| Epoch | 1087 (76.95% complete, ~6.0h remaining) |
| Lifetime transactions | 566.9B |
| Circulating supply | 591.6M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 18.00% of slots needed a priority fee (max 2.7M µlam/CU) |
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
| Stake on private (100% commission) validators | 22.96% |

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
| SOL price | $72.23 (+4.53% 24h) |
| Market cap | $42.73B (rank #7) |
| 24h volume | $4.25B |
| ATH | $293.31 (-75.37% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.72B |
| Stablecoin supply | $14.06B |
| DEX volume (24h) | $1.68B (+7.52% 1d) |
| App fees (24h, all protocols) | $7.95M |
| Chain fees (24h) | $357.11K |
| Jito MEV tips (24h) | $96.94K |
| **REV - Real Economic Value (24h)** | **$454.05K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.47B | +5.85% |
| USDT | $2.00B | -18.00% |
| USDGO | $1.06B | -4.90% |
| USD1 | $1.02B | -16.89% |
| PYUSD | $802.39M | +8.08% |
| USDG | $441.85M | -10.60% |
| USDe | $277.05M | -4.92% |
| SOFID | $273.89M | +2.87% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $236.69M |
| Orca DEX | $233.21M |
| PumpSwap | $156.41M |
| Meteora DLMM | $154.87M |
| Scorch | $131.54M |
| Raydium AMM | $120.23M |
| pump.fun | $89.40M |
| Manifest Trade | $65.87M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.48M |
| Jupiter Perpetual Exchange | $1.22M |
| pump.fun | $1.05M |
| Meteora DLMM | $404.81K |
| Axiom | $369.07K |
| Sanctum Validator LSTs | $200.71K |
| Raydium AMM | $198.86K |
| Collector Crypt | $180.32K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $36.26M |
| xStocks holder positions | 932.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $587.41M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 75,856 | 58.90% | 0.6 s |
| Pump.fun | 63,344 | 68.10% | 0.9 s |
| Jupiter v6 | 4,699 | 66.60% | 12.5 s |
| Orca Whirlpools | 3,901 | 65.40% | 15.4 s |
| Raydium AMM v4 | 741 | 13.10% | 80.9 s |

Median failure rate across the sampled programs: **65.40%** (range 13.10% to 68.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.36K SOL**.

## Exchange and large-holder balances

9.51M SOL ($686.55M) across 6 publicly-attributed accounts. Net **50K SOL (0.53%) moved onto exchanges** over the last 23.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $671.74M | 0.3/h | 5 |
| Gate.io | 64.91K | $4.69M | 183.7/h | 0 |
| Kraken | 36.38K | $2.63M | 195.8/h | 0 |
| Coinbase (2) | 35.31K | $2.55M | 240.3/h | 0 |
| Bybit | 34.57K | $2.50M | 15.3/h | 0 |
| Coinbase | 33.85K | $2.45M | 341.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1140 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.247 | 1067 | 0.0000 |
| DEX volume moves with App fees | +0.245 | 1099 | 0.0000 |
| SOL price moves with DeFi TVL | +0.243 | 1140 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.242 | 1067 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.223 | 1108 | 0.0000 |
| Total TPS moves with Slot time | +0.192 | 1108 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.173 | 1089 | 0.0000 |
| Total TPS moves with Program failure rate | +0.172 | 1089 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.151 | 1067 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.123 | 1067 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 72.23 USD | Jupiter (on-chain DEX): 72.56 USD | -0.46% | agree |
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
