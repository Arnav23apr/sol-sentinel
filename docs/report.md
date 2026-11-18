# Solana Ecosystem Report

*Generated 2026-11-18 20:01 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 8.1 robust standard deviations below its 7-day baseline: a 5.2% move to 13,222,159,554.00 USD from a typical 13,940,714,297.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.4K |
| TPS (non-vote) | 2.4K |
| Slot time | 213.9 ms |
| Slot | 471M |
| Block height | 449M |
| Epoch | 1090 (41.84% complete, ~14.9h remaining) |
| Lifetime transactions | 567.3B |
| Circulating supply | 591.8M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 28.00% of slots needed a priority fee (max 4.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 660 |
| Delinquent validators | 25 |
| Delinquent stake | 0.01% |
| Total active stake | 426.7M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.48% / 24.98% / 36.21% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 23.11% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 17.0M | 3.99% | 0% |
| 2 | `CcaH…oTN1` | 16.5M | 3.86% | 7% |
| 3 | `3N7s…iD5g` | 12.4M | 2.91% | 0% |
| 4 | `8Gbw…F8iD` | 10.3M | 2.41% | 0% |
| 5 | `51JB…UNAm` | 9.8M | 2.30% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.24% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.16% | 7% |
| 8 | `9QU2…29mF` | 8.0M | 1.87% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.64% | 0% |
| 10 | `CvSb…wycB` | 6.8M | 1.59% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $73.16 (+0.49% 24h) |
| Market cap | $43.29B (rank #7) |
| 24h volume | $2.41B |
| ATH | $293.31 (-75.06% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.74B |
| Stablecoin supply | $13.22B |
| DEX volume (24h) | $1.51B (+2.01% 1d) |
| App fees (24h, all protocols) | $8.20M |
| Chain fees (24h) | $445.21K |
| Jito MEV tips (24h) | $150.41K |
| **REV - Real Economic Value (24h)** | **$595.63K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.92B | -2.90% |
| USDT | $2.00B | -6.96% |
| USDGO | $1.02B | -5.36% |
| USD1 | $921.24M | -18.42% |
| PYUSD | $678.01M | -14.78% |
| USDG | $423.17M | -10.94% |
| SOFID | $273.84M | +2.15% |
| USDe | $267.32M | -6.29% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $229.48M |
| Meteora DLMM | $172.72M |
| Raydium AMM | $163.32M |
| PumpSwap | $155.29M |
| BisonFi | $149.60M |
| pump.fun | $114.24M |
| Manifest Trade | $87.22M |
| Scorch | $80.34M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.87M |
| pump.fun | $1.40M |
| Meteora DLMM | $451.91K |
| Axiom | $433.46K |
| Jupiter Perpetual Exchange | $349.64K |
| Raydium AMM | $328.73K |
| Lunar Lander | $309.69K |
| Collector Crypt | $278.61K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $73.10M |
| xStocks holder positions | 936.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $560.50M |

## Program activity and chain health

Chain tip lag: **+0.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 44,741 | 25.70% | 1.3 s |
| Pump.fun | 22,674 | 64.70% | 2.6 s |
| Jupiter v6 | 8,859 | 71.10% | 6.6 s |
| Orca Whirlpools | 8,850 | 49.60% | 6.2 s |
| Raydium AMM v4 | 1,882 | 8.50% | 31.7 s |

Median failure rate across the sampled programs: **49.60%** (range 8.50% to 71.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **707.46 SOL**.

## Exchange and large-holder balances

9.77M SOL ($714.69M) across 7 publicly-attributed accounts. Net **186K SOL (1.94%) moved onto exchanges** over the last 22.1 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $680.39M | 0.3/h | 2 |
| Coinbase | 150.49K | $11.01M | 385.4/h | 0 |
| Bybit | 133.80K | $9.79M | 33.4/h | 0 |
| Gate.io | 67.69K | $4.95M | 131.8/h | 0 |
| Bitget | 57.17K | $4.18M | 91.3/h | 0 |
| Kraken | 39.13K | $2.86M | 292.7/h | 0 |
| Coinbase (2) | 20.65K | $1.51M | 354/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1148 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.254 | 1148 | 0.0000 |
| DEX volume moves with App fees | +0.249 | 1107 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.246 | 1075 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.242 | 1075 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.222 | 1116 | 0.0000 |
| Total TPS moves with Slot time | +0.191 | 1116 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.175 | 1097 | 0.0000 |
| Total TPS moves with Program failure rate | +0.174 | 1097 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.147 | 1075 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.130 | 1075 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 73.16 USD | Jupiter (on-chain DEX): 72.95 USD | +0.29% | agree |
| Circulating supply | getSupply (RPC): 591.79M SOL | CoinGecko: 591.79M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-16
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

- **[Why CoinShares Just Sold All Its Ethereum and Half Its Solana](https://decrypt.co/383570/why-coinshares-just-sold-all-ethereum-half-solana)** - Decrypt, 2026-11-18
- **[AI Will Make the Next 12 Months 'a Slaughterhouse' for Crypto Security: Anchorage Exec](https://decrypt.co/383526/ai-will-make-the-next-12-months-a-slaughterhouse-for-crypto-security-anchorage-exec)** - Decrypt, 2026-11-18
- **[Standard Life Chair Wants Tokenized Gilts to Open UK Government Bonds to Retail Savers](https://decrypt.co/383434/standard-life-chair-wants-tokenized-gilts-to-open-uk-government-bonds-to-retail-savers)** - Decrypt, 2026-11-17
- **['The Biggest Opportunity in Crypto Is Already Underway': Solana Bets Big on AI Agents](https://decrypt.co/383417/the-biggest-opportunity-in-crypto-is-already-underway-solana-bets-big-on-ai-agents)** - Decrypt, 2026-11-17
- **[Solana Foundation Backs CoinGecko as Crypto Data Giant Eyes Trading](https://decrypt.co/383401/solana-foundation-backs-coingecko-eyes-trading)** - Decrypt, 2026-11-17
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
