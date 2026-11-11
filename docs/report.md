# Solana Ecosystem Report

*Generated 2026-11-11 01:34 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **SOL price** (warning): SOL price is 5.4 robust standard deviations below its 7-day baseline: a 7.1% move to 83.36 USD from a typical 89.76.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 1.8K |
| TPS (non-vote) | 1.8K |
| Slot time | 215.4 ms |
| Slot | 468M |
| Block height | 446M |
| Epoch | 1083 (19.55% complete, ~20.8h remaining) |
| Lifetime transactions | 566.1B |
| Circulating supply | 591.4M SOL |
| Inflation (annual) | 3.56% |
| AMM write-lock congestion (150-slot window) | 7.30% of slots needed a priority fee (max 5.4M µlam/CU) |
| Node version (RPC) | 4.4.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 658 |
| Delinquent validators | 41 |
| Delinquent stake | 0.23% |
| Total active stake | 432.4M SOL |
| Nakamoto coefficient | 17 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.62% / 36.15% |
| Commission (stake-weighted, delegatable validators) | 3.83% |
| Stake on private (100% commission) validators | 22.88% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1i…uBtk` | 16.8M | 3.88% | 0% |
| 2 | `CcaH…oTN1` | 16.6M | 3.83% | 7% |
| 3 | `3N7s…iD5g` | 13.0M | 3.01% | 0% |
| 4 | `8Gbw…F8iD` | 10.1M | 2.34% | 0% |
| 5 | `51JB…UNAm` | 9.6M | 2.23% | 10% |
| 6 | `Catz…Diqb` | 9.6M | 2.21% | 5% |
| 7 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 8 | `9QU2…29mF` | 7.8M | 1.81% | 7% |
| 9 | `Dumi…Zk4a` | 7.0M | 1.62% | 0% |
| 10 | `CvSb…wycB` | 6.7M | 1.56% | 5% |

## Market

| Metric | Value |
|---|---|
| SOL price | $83.36 (-3.44% 24h) |
| Market cap | $49.30B (rank #7) |
| 24h volume | $2.90B |
| ATH | $293.31 (-71.58% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.06B |
| Stablecoin supply | $14.52B |
| DEX volume (24h) | $1.34B (-10.21% 1d) |
| App fees (24h, all protocols) | $8.73M |
| Chain fees (24h) | $444.51K |
| Jito MEV tips (24h) | $122.68K |
| **REV - Real Economic Value (24h)** | **$567.20K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.12B | +2.09% |
| USDT | $2.15B | -5.28% |
| USD1 | $1.13B | -17.37% |
| USDGO | $1.08B | -9.75% |
| PYUSD | $795.82M | +14.53% |
| BUIDL | $483.83M | -28.09% |
| USDG | $475.13M | +1.00% |
| USDe | $285.48M | -4.10% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $220.26M |
| BisonFi | $157.07M |
| Raydium AMM | $142.13M |
| Meteora DLMM | $122.68M |
| PumpSwap | $94.39M |
| pump.fun | $91.08M |
| Scorch | $88.81M |
| PancakeSwap AMM V3 | $52.78M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.27M |
| pump.fun | $1.21M |
| Axiom | $505.79K |
| Meteora DLMM | $411.07K |
| Raydium AMM | $329.70K |
| LaunchLab | $316.55K |
| Jupiter Perpetual Exchange | $304.48K |
| Sanctum Validator LSTs | $233.82K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $64.54M |
| xStocks holder positions | 904.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $582.30M |

## Program activity and chain health

Chain tip lag: **+1.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 80,501 | 40.10% | 0.6 s |
| Pump.fun | 13,579 | 80.70% | 4.3 s |
| Orca Whirlpools | 3,473 | 31.60% | 17 s |
| Jupiter v6 | 2,957 | 45.80% | 20.2 s |
| Raydium AMM v4 | 1,426 | 10.40% | 42 s |

Median failure rate across the sampled programs: **40.10%** (range 10.40% to 80.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **707.09 SOL**.

## Exchange and large-holder balances

9.60M SOL ($800.37M) across 7 publicly-attributed accounts. Net **40K SOL (0.42%) moved off exchanges** over the last 17.7 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.30M | $775.25M | 0.4/h | 5 |
| Bybit | 97.64K | $8.14M | 88.1/h | 0 |
| Gate.io | 88.39K | $7.37M | 144/h | 0 |
| Kraken | 42.85K | $3.57M | 257/h | 0 |
| Coinbase | 39.54K | $3.30M | 324.9/h | 0 |
| Coinbase (2) | 21.16K | $1.76M | 319.4/h | 0 |
| Bitget | 11.82K | $985.14K | 112/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 14 of 117 tested pairs survive, over 1121 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.261 | 1080 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.238 | 1048 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.233 | 1048 | 0.0000 |
| SOL price moves with DeFi TVL | +0.229 | 1121 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.227 | 1089 | 0.0000 |
| Total TPS moves with Slot time | +0.196 | 1089 | 0.0000 |
| Total TPS moves with Program failure rate | +0.171 | 1070 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.171 | 1070 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.154 | 1048 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.125 | 1048 | 0.0001 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 83.36 USD | Jupiter (on-chain DEX): 83.42 USD | -0.07% | agree |
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

**Latest Firedancer release:** [v26.10.6](https://github.com/firedancer-io/firedancer/releases/tag/v26.10.6) (2026-11-05)

## Ecosystem news

- **[Solana's Jupiter Expands Beyond Trading With Token Baskets, Yield Vaults and New Portfolio](https://decrypt.co/382836/solanas-jupiter-expands-beyond-trading-with-token-baskets-yield-vaults-and-new-portfolio)** - Decrypt, 2026-11-10
- **[Decrypt Money Account Gets Confidential Transfers With Solana Privacy Firm Helius](https://decrypt.co/382806/decrypt-money-account-gets-confidential-transfers-with-solana-privacy-firm-helius)** - Decrypt, 2026-11-10
- **[Introducing Solana Privacy Rings](https://www.helius.dev/blog/solana-privacy-rings)** - Helius, 2026-11-10
- **[Solana Set for Another Tokenized Stock Venue as Formation Notifies the SEC](https://decrypt.co/382859/solana-tokenized-stock-venue-formation-sec)** - Decrypt, 2026-11-09
- **[Introducing the Parsed Events Scan API](https://www.helius.dev/blog/parsed-events-scan)** - Helius, 2026-11-03
- **[Agave 4.4 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-4)** - Helius, 2026-10-28
- **[The Price of Cheap Writes: How does RocksDB read?](https://www.helius.dev/blog/rocksdb-read-path)** - Helius, 2026-10-19

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
