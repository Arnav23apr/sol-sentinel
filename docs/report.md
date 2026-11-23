# Solana Ecosystem Report

*Generated 2026-11-23 04:48 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.2K |
| TPS (non-vote) | 1.2K |
| Slot time | 213.2 ms |
| Slot | 473M |
| Block height | 451M |
| Epoch | 1094 (47.76% complete, ~13.4h remaining) |
| Lifetime transactions | 568.0B |
| Circulating supply | 592.0M SOL |
| Inflation (annual) | 3.54% |
| AMM write-lock congestion (150-slot window) | 3.30% of slots needed a priority fee (max 536.8K µlam/CU) |
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
| SOL price | $71.27 (+2.76% 24h) |
| Market cap | $42.21B (rank #7) |
| 24h volume | $1.91B |
| ATH | $293.31 (-75.70% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.63B |
| Stablecoin supply | $13.11B |
| DEX volume (24h) | $1.19B (-11.85% 1d) |
| App fees (24h, all protocols) | $6.01M |
| Chain fees (24h) | $287.12K |
| Jito MEV tips (24h) | $77.51K |
| **REV - Real Economic Value (24h)** | **$364.63K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.88B | -8.16% |
| USDT | $1.99B | -0.50% |
| USDGO | $984.72M | -7.52% |
| USD1 | $867.27M | -15.07% |
| PYUSD | $716.61M | -10.62% |
| USDG | $443.94M | +0.48% |
| SOFID | $282.31M | +3.11% |
| USDe | $252.81M | -8.75% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $153.40M |
| Orca DEX | $132.41M |
| Scorch | $127.86M |
| PumpSwap | $109.84M |
| Raydium AMM | $99.45M |
| Meteora DLMM | $96.82M |
| pump.fun | $83.40M |
| SolFi V2 | $67.43M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.10M |
| pump.fun | $955.78K |
| Jupiter Perpetual Exchange | $507.42K |
| Axiom | $326.90K |
| Meteora DLMM | $233.87K |
| Sanctum Validator LSTs | $207.21K |
| Raydium AMM | $191.40K |
| Lunar Lander | $136.16K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $41.32M |
| xStocks holder positions | 949.8K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $522.01M |

## Program activity and chain health

Chain tip lag: **+1.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 38,368 | 48.50% | 1.3 s |
| Pump.fun | 17,061 | 81.20% | 3.4 s |
| Orca Whirlpools | 1,872 | 50.90% | 31.8 s |
| Jupiter v6 | 1,635 | 52.90% | 36.7 s |
| Raydium AMM v4 | 940 | 27.00% | 63.1 s |

Median failure rate across the sampled programs: **50.90%** (range 27.00% to 81.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.85K SOL**.

## Exchange and large-holder balances

9.61M SOL ($684.70M) across 6 publicly-attributed accounts. Net **87K SOL (0.90%) moved off exchanges** over the last 17.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $662.81M | 0.3/h | 2 |
| Bybit | 120.74K | $8.61M | 19/h | 0 |
| Gate.io | 96.03K | $6.84M | 96/h | 0 |
| Kraken | 37.21K | $2.65M | 126.3/h | 0 |
| Coinbase | 34.14K | $2.43M | 198.3/h | 0 |
| Bitget | 19.00K | $1.35M | 78.9/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1164 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.256 | 1123 | 0.0000 |
| SOL price moves with DeFi TVL | +0.253 | 1164 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.245 | 1091 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.241 | 1091 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.219 | 1132 | 0.0000 |
| Total TPS moves with Slot time | +0.189 | 1132 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.176 | 1113 | 0.0000 |
| Total TPS moves with Program failure rate | +0.175 | 1113 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.149 | 1091 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.134 | 1091 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 71.27 USD | Jupiter (on-chain DEX): 71.16 USD | +0.15% | agree |
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
