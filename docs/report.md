# Solana Ecosystem Report

*Generated 2026-11-12 12:03 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Stablecoin supply** (critical): Stablecoin supply is 7.9 robust standard deviations below its 7-day baseline: a 5.0% move to 13,877,505,561.00 USD from a typical 14,601,406,023.00.
- 🟠 **SOL price** (warning): SOL price is 4.0 robust standard deviations below its 7-day baseline: a 7.7% move to 82.32 USD from a typical 89.22.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.5K |
| TPS (non-vote) | 1.5K |
| Slot time | 214.7 ms |
| Slot | 469M |
| Block height | 447M |
| Epoch | 1084 (53.33% complete, ~12.0h remaining) |
| Lifetime transactions | 566.3B |
| Circulating supply | 591.5M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 12.00% of slots needed a priority fee (max 483.8K µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 660 |
| Delinquent validators | 38 |
| Delinquent stake | 0.16% |
| Total active stake | 432.7M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.19% / 24.52% / 36.07% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 22.78% |

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
| SOL price | $82.32 (-1.83% 24h) |
| Market cap | $48.70B (rank #7) |
| 24h volume | $1.84B |
| ATH | $293.31 (-71.93% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.05B |
| Stablecoin supply | $13.88B |
| DEX volume (24h) | $1.62B (+20.81% 1d) |
| App fees (24h, all protocols) | $10.18M |
| Chain fees (24h) | $500.87K |
| Jito MEV tips (24h) | $137.89K |
| **REV - Real Economic Value (24h)** | **$638.76K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.01B | -1.34% |
| USDT | $2.15B | -15.99% |
| USD1 | $1.12B | -15.17% |
| USDGO | $1.08B | -8.00% |
| PYUSD | $752.71M | +10.34% |
| USDG | $493.13M | -1.40% |
| USDe | $280.93M | -5.24% |
| SOFID | $270.83M | +4.35% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $395.67M |
| Orca DEX | $201.52M |
| Meteora DLMM | $163.36M |
| BisonFi | $144.68M |
| Raydium AMM | $125.56M |
| Manifest Trade | $105.66M |
| pump.fun | $103.23M |
| Scorch | $62.59M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.25M |
| pump.fun | $1.29M |
| Meteora DLMM | $1.07M |
| Axiom | $658.96K |
| Collector Crypt | $369.50K |
| Lunar Lander | $297.77K |
| fomo Wallet | $262.84K |
| Raydium AMM | $262.46K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $97.06M |
| xStocks holder positions | 910.7K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $582.39M |

## Program activity and chain health

Chain tip lag: **+1.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 42,897 | 40.00% | 1.3 s |
| Pump.fun | 10,501 | 60.40% | 5.6 s |
| Jupiter v6 | 3,709 | 59.30% | 15.9 s |
| Orca Whirlpools | 3,316 | 69.20% | 17.8 s |
| Raydium AMM v4 | 1,075 | 41.70% | 55.2 s |

Median failure rate across the sampled programs: **59.30%** (range 40.00% to 69.20%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **849.74 SOL**.

## Exchange and large-holder balances

9.53M SOL ($784.51M) across 6 publicly-attributed accounts. Net **27K SOL (0.28%) moved off exchanges** over the last 19.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $765.58M | 0.3/h | 5 |
| Bybit | 97.55K | $8.03M | 29.6/h | 0 |
| Gate.io | 53.60K | $4.41M | 160.1/h | 0 |
| Coinbase | 30.02K | $2.47M | 160.9/h | 0 |
| Kraken | 28.89K | $2.38M | 203.4/h | 0 |
| Coinbase (2) | 19.98K | $1.64M | 180.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1126 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.259 | 1085 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.240 | 1053 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.235 | 1053 | 0.0000 |
| SOL price moves with DeFi TVL | +0.229 | 1126 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.226 | 1094 | 0.0000 |
| Total TPS moves with Slot time | +0.194 | 1094 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.173 | 1075 | 0.0000 |
| Total TPS moves with Program failure rate | +0.172 | 1075 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 1053 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.123 | 1053 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 82.32 USD | Jupiter (on-chain DEX): 82.24 USD | +0.10% | agree |
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

- **[‘Milestone quarter’: Solana Company reports Q3 revenue growth driven by staking rewards](https://www.theblock.co/news/business/2026-11-11-solana-company-reports-q3-revenue-growth-438448)** - The Block, 2026-11-12
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
