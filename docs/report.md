# Solana Ecosystem Report

*Generated 2026-11-22 18:47 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.8K |
| TPS (non-vote) | 1.8K |
| Slot time | 213.2 ms |
| Slot | 473M |
| Block height | 451M |
| Epoch | 1094 (8.97% complete, ~23.3h remaining) |
| Lifetime transactions | 567.9B |
| Circulating supply | 592.0M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 14.70% of slots needed a priority fee (max 7.3M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 662 |
| Delinquent validators | 23 |
| Delinquent stake | 0.01% |
| Total active stake | 425.6M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.45% / 25.00% / 36.03% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 23.15% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.9M | 3.97% | 0% |
| 2 | `CcaH…oTN1` | 16.3M | 3.84% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.91% | 0% |
| 4 | `8Gbw…F8iD` | 10.2M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.31% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.26% | 5% |
| 7 | `26pV…3dJx` | 9.3M | 2.18% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.88% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.59% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $70.25 (-0.56% 24h) |
| Market cap | $41.59B (rank #7) |
| 24h volume | $1.84B |
| ATH | $293.31 (-76.05% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.64B |
| Stablecoin supply | $13.08B |
| DEX volume (24h) | $1.35B (-28.59% 1d) |
| App fees (24h, all protocols) | $7.59M |
| Chain fees (24h) | $317.05K |
| Jito MEV tips (24h) | $76.46K |
| **REV - Real Economic Value (24h)** | **$393.51K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.79B | -7.63% |
| USDT | $2.04B | +2.00% |
| USDGO | $984.24M | -7.52% |
| USD1 | $867.05M | -15.92% |
| PYUSD | $719.71M | -10.36% |
| USDG | $444.13M | -0.20% |
| SOFID | $282.39M | +3.11% |
| USDe | $252.94M | -8.63% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $153.40M |
| Scorch | $127.86M |
| Orca DEX | $124.75M |
| PumpSwap | $124.04M |
| Meteora DLMM | $96.82M |
| Raydium AMM | $93.70M |
| pump.fun | $83.40M |
| SolFi V2 | $67.43M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| Jupiter Perpetual Exchange | $1.51M |
| PumpSwap | $1.30M |
| pump.fun | $1.03M |
| Axiom | $326.90K |
| Meteora DLMM | $233.87K |
| Sanctum Validator LSTs | $203.39K |
| Collector Crypt | $164.31K |
| Raydium AMM | $147.32K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $26.48M |
| xStocks holder positions | 947.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $521.32M |

## Program activity and chain health

Chain tip lag: **+0.9 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 63,813 | 33.50% | 0.9 s |
| Pump.fun | 20,111 | 82.40% | 2.8 s |
| Orca Whirlpools | 4,009 | 23.80% | 14.7 s |
| Jupiter v6 | 2,373 | 53.50% | 25.2 s |
| Raydium AMM v4 | 1,011 | 24.10% | 59.3 s |

Median failure rate across the sampled programs: **33.50%** (range 23.80% to 82.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.94K SOL**.

## Exchange and large-holder balances

9.63M SOL ($676.67M) across 6 publicly-attributed accounts. Net **58K SOL (0.61%) moved onto exchanges** over the last 19.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $653.33M | 0.3/h | 2 |
| Bybit | 120.74K | $8.48M | 16.7/h | 0 |
| Gate.io | 94.88K | $6.67M | 153.3/h | 0 |
| Kraken | 42.77K | $3.00M | 280.2/h | 0 |
| Coinbase | 37.43K | $2.63M | 202.4/h | 0 |
| Bitget | 36.49K | $2.56M | 245.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1162 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.254 | 1162 | 0.0000 |
| DEX volume moves with App fees | +0.254 | 1121 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.245 | 1089 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.240 | 1089 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.218 | 1130 | 0.0000 |
| Total TPS moves with Slot time | +0.189 | 1130 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.176 | 1111 | 0.0000 |
| Total TPS moves with Program failure rate | +0.175 | 1111 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 1089 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.131 | 1089 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 70.25 USD | Jupiter (on-chain DEX): 70.26 USD | -0.01% | agree |
| Circulating supply | getSupply (RPC): 592.02M SOL | CoinGecko: 592.02M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-20
- [SIMD-0714: SIMD](https://github.com/solana-foundation/solana-improvement-documents/pull/714) - updated 2026-11-04
- [Add missing feature gate keys to SIMD front matter](https://github.com/solana-foundation/solana-improvement-documents/pull/713) - updated 2026-11-20
- [SIMD-0709: Process for SIMDs that add cryptographic syscalls](https://github.com/solana-foundation/solana-improvement-documents/pull/709) - updated 2026-11-19
- [SIMD-0706: Reject unknown syscalls and `sol_alloc_free_`](https://github.com/solana-foundation/solana-improvement-documents/pull/706) - updated 2026-11-19

**Recently merged SIMDs:**

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - updated 2026-11-09
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-11-06
- [SIMD-0685: Loader V3: Remove ExtendProgram](https://github.com/solana-foundation/solana-improvement-documents/pull/685) - updated 2026-11-02
- [rekey simd-0529 big int mod exp](https://github.com/solana-foundation/solana-improvement-documents/pull/715) - updated 2026-11-01
- [SIMD-0567: CU-optimized ATA Program (`p-ATA`)](https://github.com/solana-foundation/solana-improvement-documents/pull/567) - updated 2026-11-01
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-10-31

**Latest Agave release:** [v5.0.0-alpha.1](https://github.com/anza-xyz/agave/releases/tag/v5.0.0-alpha.1) (2026-11-19)

**Latest Firedancer release:** [v26.11.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.11.0) (2026-11-11)

## Ecosystem news

- **[Cathie Wood Bets $91M on Anthropic IPO While Paring Crypto Exposure](https://decrypt.co/383737/cathie-wood-bets-91m-anthropic-ipo-paring-crypto-exposure)** - Decrypt, 2026-11-20
- **[Ark buys $90 million worth of Anthropic shares on debut, trims Ethereum and Solana staking ETF holdings](https://www.theblock.co/news/markets/2026-11-20-ark-buys-90-million-worth-of-anthropic-shares-on-debut-trims-ethereum-and-solana-staking-etf-holdings-444226)** - The Block, 2026-11-20
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
