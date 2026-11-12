# Solana Ecosystem Report

*Generated 2026-11-12 20:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 3.9 robust standard deviations below its 7-day baseline: a 8.6% move to 81.43 USD from a typical 89.05.
- 🟠 **Stablecoin supply** (warning): Stablecoin supply is 5.8 robust standard deviations below its 7-day baseline: a 4.6% move to 13,908,199,922.00 USD from a typical 14,578,591,445.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 2.1K |
| TPS (non-vote) | 2.1K |
| Slot time | 213.5 ms |
| Slot | 469M |
| Block height | 447M |
| Epoch | 1084 (84.81% complete, ~3.9h remaining) |
| Lifetime transactions | 566.4B |
| Circulating supply | 591.5M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 14.00% of slots needed a priority fee (max 775.8K µlam/CU) |
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
| SOL price | $81.43 (-4.03% 24h) |
| Market cap | $48.16B (rank #7) |
| 24h volume | $2.23B |
| ATH | $293.31 (-72.24% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $4.98B |
| Stablecoin supply | $13.91B |
| DEX volume (24h) | $1.62B (+20.81% 1d) |
| App fees (24h, all protocols) | $10.19M |
| Chain fees (24h) | $500.87K |
| Jito MEV tips (24h) | $140.44K |
| **REV - Real Economic Value (24h)** | **$641.31K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.10B | -0.11% |
| USDT | $2.15B | -15.99% |
| USD1 | $1.09B | -17.51% |
| USDGO | $1.08B | -8.00% |
| PYUSD | $741.67M | +8.73% |
| USDG | $476.44M | -4.75% |
| USDe | $281.19M | -5.15% |
| SOFID | $270.69M | +4.35% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $395.67M |
| Orca DEX | $204.49M |
| Meteora DLMM | $163.36M |
| Raydium AMM | $149.02M |
| BisonFi | $144.68M |
| pump.fun | $103.23M |
| Manifest Trade | $97.95M |
| Scorch | $62.59M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.25M |
| pump.fun | $1.29M |
| Meteora DLMM | $1.07M |
| Axiom | $658.96K |
| Collector Crypt | $466.76K |
| Lunar Lander | $307.58K |
| Raydium AMM | $293.80K |
| fomo Wallet | $262.85K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $153.25M |
| xStocks holder positions | 918.5K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $582.11M |

## Program activity and chain health

Chain tip lag: **+0.6 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 46,417 | 43.90% | 1.3 s |
| Pump.fun | 31,686 | 78.80% | 1.7 s |
| Orca Whirlpools | 9,029 | 79.50% | 6.6 s |
| Jupiter v6 | 7,489 | 67.20% | 7.9 s |
| Raydium AMM v4 | 953 | 11.80% | 62.8 s |

Median failure rate across the sampled programs: **67.20%** (range 11.80% to 79.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **660.77 SOL**.

## Exchange and large-holder balances

9.56M SOL ($778.26M) across 7 publicly-attributed accounts. Net **17K SOL (0.17%) moved onto exchanges** over the last 21.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $757.30M | 0.3/h | 5 |
| Bybit | 97.55K | $7.94M | 27.2/h | 0 |
| Gate.io | 54.62K | $4.45M | 115.2/h | 0 |
| Kraken | 37.20K | $3.03M | 230.8/h | 0 |
| Coinbase | 29.26K | $2.38M | 277.6/h | 0 |
| Coinbase (2) | 25.06K | $2.04M | 297/h | 0 |
| Bitget | 13.73K | $1.12M | 134.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1127 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.258 | 1086 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.240 | 1054 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.236 | 1054 | 0.0000 |
| SOL price moves with DeFi TVL | +0.231 | 1127 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.225 | 1095 | 0.0000 |
| Total TPS moves with Slot time | +0.193 | 1095 | 0.0000 |
| Total TPS moves with Program failure rate | +0.173 | 1076 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.173 | 1076 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.153 | 1054 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.124 | 1054 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 81.43 USD | Jupiter (on-chain DEX): 81.35 USD | +0.10% | agree |
| Circulating supply | getSupply (RPC): 591.46M SOL | CoinGecko: 591.46M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0701: Vote Account v5](https://github.com/solana-foundation/solana-improvement-documents/pull/701) - *merged*, updated 2026-11-09

**Open SIMD proposals:**

- [Amend SIMD-0326: define BLS signer indices](https://github.com/solana-foundation/solana-improvement-documents/pull/727) - updated 2026-11-10
- [SIMD-0723: Remove Durable Nonces](https://github.com/solana-foundation/solana-improvement-documents/pull/723) - updated 2026-11-12
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

- **[DTCC plans to bring tokenized securities to Solana in second half of 2027](https://www.theblock.co/news/business/2026-11-12-dtcc-plans-bring-tokenized-securities-solana-second-half-of-2027-438559)** - The Block, 2026-11-12
- **[SoFi Brings Its Bank-Issued Stablecoin to Polygon’s Payments Stack](https://decrypt.co/383096/sofi-brings-bank-issued-stablecoin-polygon-payments-stack)** - Decrypt, 2026-11-12
- **[SoFiUSD goes live on Polygon as bank-issued stablecoin expands reach](https://www.theblock.co/news/ecosystems/2026-11-12-sofiusd-goes-live-on-polygon-as-bank-issued-stablecoin-expands-reach-438542)** - The Block, 2026-11-12
- **[DTCC to Bring Tokenized Stocks and Treasuries to Solana in 2027](https://decrypt.co/383132/dtcc-to-bring-tokenized-stocks-and-treasuries-to-solana-in-2027)** - Decrypt, 2026-11-12
- **[‘Milestone quarter’: Solana Company reports Q3 revenue growth driven by staking rewards](https://www.theblock.co/news/business/2026-11-11-solana-company-reports-q3-revenue-growth-438448)** - The Block, 2026-11-12
- **[What Are Solana Privacy Rings? Inside Helius’ Privacy Protocol for Solana](https://decrypt.co/resources/what-are-solana-privacy-rings-inside-helius-privacy-protocol-for-solana)** - Decrypt, 2026-11-11
- **[Decrypt Becomes First News Publisher to Offer Perps Trading, Powered by Solana's Phoenix](https://decrypt.co/382992/decrypt-becomes-first-news-publisher-to-offer-perps-trading-powered-by-solanas-phoenix)** - Decrypt, 2026-11-11
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
