# Solana Ecosystem Report

*Generated 2026-11-11 16:44 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 4.1 robust standard deviations below its 7-day baseline: a 5.5% move to 84.62 USD from a typical 89.55.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.9K |
| TPS (non-vote) | 1.9K |
| Slot time | 213.9 ms |
| Slot | 468M |
| Block height | 446M |
| Epoch | 1083 (78.43% complete, ~5.5h remaining) |
| Lifetime transactions | 566.2B |
| Circulating supply | 591.4M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 7.30% of slots needed a priority fee (max 2.0M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 658 |
| Delinquent validators | 41 |
| Delinquent stake | 0.31% |
| Total active stake | 432.1M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.30% / 24.64% / 36.18% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 22.90% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.88% | 0% |
| 2 | `CcaH…oTN1` | 16.6M | 3.83% | 7% |
| 3 | `3N7s…iD5g` | 13.0M | 3.02% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.34% | 0% |
| 5 | `51JB…UNAm` | 9.6M | 2.23% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.22% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.14% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $84.62 (+3.08% 24h) |
| Market cap | $50.05B (rank #7) |
| 24h volume | $2.21B |
| ATH | $293.31 (-71.15% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.08B |
| Stablecoin supply | $14.47B |
| DEX volume (24h) | $1.34B (-9.79% 1d) |
| App fees (24h, all protocols) | $8.41M |
| Chain fees (24h) | $444.51K |
| Jito MEV tips (24h) | $126.41K |
| **REV - Real Economic Value (24h)** | **$570.92K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.11B | +1.87% |
| USDT | $2.15B | -5.28% |
| USD1 | $1.13B | -17.37% |
| USDGO | $1.08B | -9.75% |
| PYUSD | $770.62M | +10.92% |
| BUIDL | $483.83M | -28.09% |
| USDG | $474.77M | +0.95% |
| USDe | $282.74M | -4.99% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $230.41M |
| BisonFi | $152.62M |
| Meteora DLMM | $129.37M |
| Raydium AMM | $123.96M |
| PumpSwap | $94.39M |
| pump.fun | $92.13M |
| Scorch | $84.04M |
| Manifest Trade | $74.16M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $1.70M |
| pump.fun | $1.21M |
| Jupiter Perpetual Exchange | $513.04K |
| Meteora DLMM | $494.00K |
| Axiom | $487.11K |
| Raydium AMM | $253.02K |
| Sanctum Validator LSTs | $228.29K |
| Orca DEX | $204.17K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $48.11M |
| xStocks holder positions | 904.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $582.32M |

## Program activity and chain health

Chain tip lag: **+1.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 57,433 | 45.20% | 0.9 s |
| Pump.fun | 18,513 | 81.20% | 3.2 s |
| Jupiter v6 | 5,909 | 66.10% | 10.1 s |
| Orca Whirlpools | 4,008 | 69.10% | 14.8 s |
| Raydium AMM v4 | 1,119 | 25.20% | 53.5 s |

Median failure rate across the sampled programs: **66.10%** (range 25.20% to 81.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **393.93 SOL**.

## Exchange and large-holder balances

9.56M SOL ($808.73M) across 7 publicly-attributed accounts. Net **70K SOL (0.73%) moved off exchanges** over the last 19.2 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $786.97M | 0.3/h | 5 |
| Bybit | 97.64K | $8.26M | 26.7/h | 0 |
| Gate.io | 59.30K | $5.02M | 164.1/h | 0 |
| Kraken | 34.71K | $2.94M | 302.8/h | 0 |
| Coinbase (2) | 25.95K | $2.20M | 297.5/h | 0 |
| Coinbase | 19.99K | $1.69M | 335.8/h | 0 |
| Bitget | 19.61K | $1.66M | 545.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1123 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.260 | 1082 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.238 | 1050 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.233 | 1050 | 0.0000 |
| SOL price moves with DeFi TVL | +0.232 | 1123 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.226 | 1091 | 0.0000 |
| Total TPS moves with Slot time | +0.195 | 1091 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.174 | 1072 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1072 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 1050 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.125 | 1050 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 84.62 USD | Jupiter (on-chain DEX): 84.52 USD | +0.12% | agree |
| Circulating supply | getSupply (RPC): 591.41M SOL | CoinGecko: 591.41M SOL | -0.00% | agree |

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

- **[Decrypt Becomes First News Publisher to Offer Perps Trading, Powered by Solana's Phoenix](https://decrypt.co/382992/decrypt-becomes-first-news-publisher-to-offer-perps-trading-powered-by-solanas-phoenix)** - Decrypt, 2026-11-11
- **[Solana's Jupiter Expands Beyond Trading With Token Baskets, Yield Vaults and New Portfolio](https://decrypt.co/382836/solanas-jupiter-expands-beyond-trading-with-token-baskets-yield-vaults-and-new-portfolio)** - Decrypt, 2026-11-10
- **[Decrypt Money Account Gets Confidential Transfers With Solana Privacy Firm Helius](https://decrypt.co/382806/decrypt-money-account-gets-confidential-transfers-with-solana-privacy-firm-helius)** - Decrypt, 2026-11-10
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Solana Set for Another Tokenized Stock Venue as Formation Notifies the SEC](https://decrypt.co/382859/solana-tokenized-stock-venue-formation-sec)** - Decrypt, 2026-11-09
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
