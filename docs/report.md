# Solana Ecosystem Report

*Generated 2026-11-19 09:39 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 10.0 robust standard deviations below its 7-day baseline: a 9.3% move to 12,637,731,048.00 USD from a typical 13,939,097,084.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.4K |
| TPS (non-vote) | 1.4K |
| Slot time | 214.7 ms |
| Slot | 471M |
| Block height | 449M |
| Epoch | 1090 (94.59% complete, ~1.4h remaining) |
| Lifetime transactions | 567.4B |
| Circulating supply | 591.8M SOL |
| Inflation (annual) | 3.55% |
| AMM write-lock congestion (150-slot window) | 12.70% of slots needed a priority fee (max 10.0M µlam/CU) |
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
| SOL price | $74.41 (-0.65% 24h) |
| Market cap | $44.04B (rank #7) |
| 24h volume | $2.13B |
| ATH | $293.31 (-74.63% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.79B |
| Stablecoin supply | $12.64B |
| DEX volume (24h) | $1.70B (+12.72% 1d) |
| App fees (24h, all protocols) | $9.97M |
| Chain fees (24h) | $560.49K |
| Jito MEV tips (24h) | $152.75K |
| **REV - Real Economic Value (24h)** | **$713.24K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $6.40B | -8.98% |
| USDT | $1.94B | -9.75% |
| USDGO | $1.00B | -7.21% |
| USD1 | $916.41M | -18.80% |
| PYUSD | $689.97M | -14.26% |
| USDG | $426.35M | -13.66% |
| SOFID | $276.12M | +2.74% |
| USDe | $267.13M | -4.92% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $330.65M |
| Orca DEX | $259.76M |
| Meteora DLMM | $172.72M |
| BisonFi | $149.60M |
| Raydium AMM | $131.29M |
| pump.fun | $114.24M |
| Manifest Trade | $94.87M |
| Scorch | $80.34M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.01M |
| pump.fun | $1.72M |
| Meteora DLMM | $451.91K |
| Axiom | $433.46K |
| Lunar Lander | $346.89K |
| Jupiter Perpetual Exchange | $302.08K |
| Raydium AMM | $265.28K |
| Sanctum Validator LSTs | $224.51K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $41.50M |
| xStocks holder positions | 936.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $560.49M |

## Program activity and chain health

Chain tip lag: **+1.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 42,431 | 21.60% | 1.3 s |
| Pump.fun | 7,158 | 77.10% | 8.4 s |
| Jupiter v6 | 4,137 | 74.30% | 14.2 s |
| Orca Whirlpools | 3,784 | 14.50% | 15.5 s |
| Raydium AMM v4 | 1,505 | 5.80% | 39.7 s |

Median failure rate across the sampled programs: **21.60%** (range 5.80% to 77.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **804.51 SOL**.

## Exchange and large-holder balances

9.71M SOL ($722.72M) across 7 publicly-attributed accounts. Net **211K SOL (2.22%) moved onto exchanges** over the last 21.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $692.01M | 0.3/h | 2 |
| Bybit | 133.49K | $9.93M | 49.2/h | 0 |
| Coinbase | 92.56K | $6.89M | 136/h | 0 |
| Gate.io | 71.18K | $5.30M | 198.7/h | 0 |
| Bitget | 53.23K | $3.96M | 4.5K/h | 0 |
| Kraken | 42.23K | $3.14M | 222.2/h | 0 |
| Coinbase (2) | 19.93K | $1.48M | 145.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1150 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| SOL price moves with DeFi TVL | +0.255 | 1150 | 0.0000 |
| DEX volume moves with App fees | +0.251 | 1109 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.248 | 1077 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.244 | 1077 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.221 | 1118 | 0.0000 |
| Total TPS moves with Slot time | +0.191 | 1118 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.177 | 1099 | 0.0000 |
| Total TPS moves with Program failure rate | +0.176 | 1099 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.146 | 1077 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.131 | 1077 | 0.0000 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 74.41 USD | Jupiter (on-chain DEX): 74.42 USD | -0.01% | agree |
| Circulating supply | getSupply (RPC): 591.80M SOL | CoinGecko: 591.80M SOL | -0.00% | agree |

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
