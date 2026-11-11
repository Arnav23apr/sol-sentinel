# Solana Ecosystem Report

*Generated 2026-11-11 23:12 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 4.6 robust standard deviations below its 7-day baseline: a 7.3% move to 82.92 USD from a typical 89.41.
- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 5.4 robust standard deviations below its 7-day baseline: a 4.9% move to 13,907,653,493.00 USD from a typical 14,631,506,909.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.4K |
| TPS (non-vote) | 2.4K |
| Slot time | 214.3 ms |
| Slot | 468M |
| Block height | 446M |
| Epoch | 1084 (3.49% complete, ~24.8h remaining) |
| Lifetime transactions | 566.3B |
| Circulating supply | 591.5M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 1.2M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 661 |
| Delinquent validators | 37 |
| Delinquent stake | 0.16% |
| Total active stake | 432.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.19% / 24.52% / 36.07% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 22.77% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.88% | 0% |
| 2 | `CcaH…oTN1` | 16.1M | 3.72% | 7% |
| 3 | `3N7s…iD5g` | 13.0M | 3.01% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.34% | 0% |
| 5 | `51JB…UNAm` | 9.7M | 2.24% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.21% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.61% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $82.92 (+0.40% 24h) |
| Market cap | $49.04B (rank #7) |
| 24h volume | $2.01B |
| ATH | $293.31 (-71.73% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.12B |
| Stablecoin supply | $13.91B |
| DEX volume (24h) | $1.34B (-9.79% 1d) |
| App fees (24h, all protocols) | $8.41M |
| Chain fees (24h) | $444.51K |
| Jito MEV tips (24h) | $118.55K |
| **REV - Real Economic Value (24h)** | **$563.07K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.02B | +0.65% |
| USDT | $2.15B | -5.28% |
| USD1 | $1.13B | -17.40% |
| USDGO | $1.08B | -9.75% |
| PYUSD | $771.76M | +11.12% |
| USDG | $481.92M | +2.46% |
| USDe | $281.20M | -5.46% |
| SOFID | $269.07M | +2.31% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $184.36M |
| BisonFi | $152.62M |
| Raydium AMM | $130.02M |
| Meteora DLMM | $129.37M |
| Manifest Trade | $95.87M |
| PumpSwap | $94.39M |
| pump.fun | $92.13M |
| Scorch | $84.04M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.70M |
| pump.fun | $1.21M |
| Jupiter Perpetual Exchange | $513.04K |
| Meteora DLMM | $494.00K |
| Axiom | $487.11K |
| Collector Crypt | $349.75K |
| Raydium AMM | $313.57K |
| Sanctum Validator LSTs | $228.29K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $64.54M |
| xStocks holder positions | 908.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $582.34M |

## Program activity and chain health

Chain tip lag: **+1.2 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 134,671 (approx.) | 45.80% | 0.2 s |
| Pump.fun | 93,140 | 28.00% | 0.6 s |
| Jupiter v6 | 40,457 | 70.30% | 1.3 s |
| Orca Whirlpools | 27,550 | 56.40% | 2.1 s |
| Raydium AMM v4 | 7,815 | 23.80% | 7.5 s |

Median failure rate across the sampled programs: **45.80%** (range 23.80% to 70.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **1.01K SOL**.

## Exchange and large-holder balances

9.54M SOL ($791.13M) across 7 publicly-attributed accounts. Net **60K SOL (0.63%) moved off exchanges** over the last 21.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $771.16M | 0.3/h | 5 |
| Bybit | 97.55K | $8.09M | 22.9/h | 0 |
| Gate.io | 55.38K | $4.59M | 136.2/h | 0 |
| Kraken | 31.14K | $2.58M | 244.9/h | 0 |
| Coinbase (2) | 21.76K | $1.80M | 356.1/h | 0 |
| Coinbase | 19.65K | $1.63M | 351.6/h | 0 |
| Bitget | 15.42K | $1.28M | 129.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1124 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.260 | 1083 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.239 | 1051 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.234 | 1051 | 0.0000 |
| SOL price moves with DeFi TVL | +0.229 | 1124 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.226 | 1092 | 0.0000 |
| Total TPS moves with Slot time | +0.195 | 1092 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.172 | 1073 | 0.0000 |
| Total TPS moves with Program failure rate | +0.171 | 1073 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.154 | 1051 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.123 | 1051 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 82.92 USD | Jupiter (on-chain DEX): 82.20 USD | +0.87% | agree |
| Circulating supply | getSupply (RPC): 591.46M SOL | CoinGecko: 591.46M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-06
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

- **[What Are Solana Privacy Rings? Inside Helius’ Privacy Protocol for Solana](https://decrypt.co/resources/what-are-solana-privacy-rings-inside-helius-privacy-protocol-for-solana)** - Decrypt, 2026-11-11
- **[Decrypt Becomes First News Publisher to Offer Perps Trading, Powered by Solana's Phoenix](https://decrypt.co/382992/decrypt-becomes-first-news-publisher-to-offer-perps-trading-powered-by-solanas-phoenix)** - Decrypt, 2026-11-11
- **[Solana's Jupiter Expands Beyond Trading With Token Baskets, Yield Vaults and New Portfolio](https://decrypt.co/382836/solanas-jupiter-expands-beyond-trading-with-token-baskets-yield-vaults-and-new-portfolio)** - Decrypt, 2026-11-10
- **[Decrypt Money Account Gets Confidential Transfers With Solana Privacy Firm Helius](https://decrypt.co/382806/decrypt-money-account-gets-confidential-transfers-with-solana-privacy-firm-helius)** - Decrypt, 2026-11-10
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
