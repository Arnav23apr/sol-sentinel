# Solana Ecosystem Report

*Generated 2026-11-25 23:52 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 13.5 robust standard deviations above its 7-day baseline: a 235.3% move to 0.06 % from a typical 0.02.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.3K |
| TPS (non-vote) | 1.3K |
| Slot time | 213.6 ms |
| Slot | 474M |
| Block height | 452M |
| Epoch | 1097 (7.66% complete, ~23.7h remaining) |
| Lifetime transactions | 568.4B |
| Circulating supply | 592.2M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 8.00% of slots needed a priority fee (max 4.7M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 655 |
| Delinquent validators | 33 |
| Delinquent stake | 0.06% |
| Total active stake | 423.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.40% / 25.00% / 36.15% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.28% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 15.8M | 3.73% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.94% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.42% | 0% |
| 5 | `51JB…UNAm` | 9.9M | 2.34% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.27% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.19% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.90% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.65% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.59% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $70.30 (+1.00% 24h) |
| Market cap | $41.63B (rank #7) |
| 24h volume | $3.41B |
| ATH | $293.31 (-76.03% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.59B |
| Stablecoin supply | $12.92B |
| DEX volume (24h) | $1.46B (-19.33% 1d) |
| App fees (24h, all protocols) | $7.15M |
| Chain fees (24h) | $365.96K |
| Jito MEV tips (24h) | $106.12K |
| **REV - Real Economic Value (24h)** | **$472.08K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.94B | -4.61% |
| USDT | $1.89B | -5.49% |
| USDGO | $922.90M | -9.79% |
| USD1 | $868.01M | -8.27% |
| PYUSD | $712.56M | -8.43% |
| USDG | $388.10M | -8.27% |
| SOFID | $278.49M | -0.00% |
| USDe | $242.51M | -9.44% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $211.87M |
| BisonFi | $190.49M |
| Raydium AMM | $182.44M |
| Manifest Trade | $139.75M |
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
| Raydium AMM | $284.53K |
| Sanctum Validator LSTs | $201.71K |
| Lunar Lander | $157.07K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $80.42M |
| xStocks holder positions | 968.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $525.96M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 40,496 | 42.90% | 1.3 s |
| Pump.fun | 22,753 | 75.50% | 2.6 s |
| Jupiter v6 | 6,914 | 74.00% | 8.3 s |
| Orca Whirlpools | 5,120 | 42.00% | 11.3 s |
| Raydium AMM v4 | 900 | 25.30% | 66.4 s |

Median failure rate across the sampled programs: **42.90%** (range 25.30% to 75.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.20K SOL**.

## Exchange and large-holder balances

9.68M SOL ($680.25M) across 7 publicly-attributed accounts. Net **55K SOL (0.57%) moved onto exchanges** over the last 18.8 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $653.79M | 0.2/h | 3 |
| Coinbase (2) | 115.24K | $8.10M | 259.4/h | 0 |
| Gate.io | 103.17K | $7.25M | 97.5/h | 0 |
| Bybit | 59.50K | $4.18M | 19.7/h | 0 |
| Bitget | 43.87K | $3.08M | 79.6/h | 0 |
| Kraken | 38.94K | $2.74M | 195.1/h | 0 |
| Coinbase | 15.59K | $1.10M | 281.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1171 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.269 | 1130 | 0.0000 |
| SOL price moves with DeFi TVL | +0.265 | 1171 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.248 | 1098 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.244 | 1098 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.215 | 1139 | 0.0000 |
| Total TPS moves with Slot time | +0.185 | 1139 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.182 | 1120 | 0.0000 |
| Total TPS moves with Program failure rate | +0.181 | 1120 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 1098 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 1098 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 70.30 USD | Jupiter (on-chain DEX): 70.32 USD | -0.03% | agree |
| Circulating supply | getSupply (RPC): 592.18M SOL | CoinGecko: 592.18M SOL | -0.00% | agree |

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

**Latest Agave release:** [v4.5.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.5.0-rc.0) (2026-11-25)

**Latest Firedancer release:** [v26.11.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.1) (2026-11-25)

## Ecosystem news

- **[Japan’s SBI, SMFG launch Solana joint venture for stablecoin payments and tokenization](https://www.theblock.co/news/business/2026-11-25-japans-sbi-smfg-tap-solana-stablecoin-tokenization-joint-venture-446131)** - The Block, 2026-11-25
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
