# Solana Ecosystem Report

*Generated 2026-08-22 11:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 7.1 robust standard deviations above its 7-day baseline: a 21.0% move to 92.97 USD from a typical 76.84.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 6.0 robust standard deviations above its 7-day baseline: a 13.7% move to 5,551,639,872.00 USD from a typical 4,883,930,394.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.4K |
| TPS (non-vote) | 1.5K |
| Slot time | 363.6 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1020 (62.34% complete, ~16.4h remaining) |
| Lifetime transactions | 540.7B |
| Circulating supply | 583.2M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,469 lamports (about $0.00051) |
| Transaction fee p90 / p99 | 29,000 / 505,000 lamports |
| Paying no priority fee | 19.20% of 7,116 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 9.30% of slots needed a priority fee (max 3.2M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 9 |
| Delinquent stake | 0.02% |
| Total active stake | 433.4M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.29% / 24.33% / 35.70% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.28% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.1M | 3.70% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.81% | 0% |
| 4 | `Catz…Diqb` | 11.8M | 2.72% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.4M | 1.94% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.51% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $92.97 (+1.50% 24h) |
| Market cap | $54.22B (rank #7) |
| 24h volume | $8.65B |
| ATH | $293.31 (-68.30% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.55B |
| Stablecoin supply | $15.85B |
| DEX volume (24h) | $3.60B (+30.15% 1d) |
| App fees (24h, all protocols) | $13.24M |
| Chain fees (24h) | $898.90K |
| Jito MEV tips (24h) | $196.33K |
| **REV - Real Economic Value (24h)** | **$1.10M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.27B | +8.16% |
| USDT | $2.74B | -5.52% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $677.12M | -0.25% |
| USDG | $610.25M | -3.15% |
| USDe | $536.93M | -0.29% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $672.20M |
| PumpSwap | $600.74M |
| BisonFi | $562.98M |
| Raydium AMM | $287.24M |
| Scorch | $242.28M |
| Meteora DLMM | $237.06M |
| Manifest Trade | $226.22M |
| HumidiFi | $213.79M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.22M |
| pump.fun | $1.78M |
| Axiom | $1.42M |
| Jupiter Perpetual Exchange | $619.81K |
| Meteora DLMM | $506.71K |
| fomo Wallet | $481.18K |
| Raydium AMM | $475.13K |
| Sanctum Validator LSTs | $455.86K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 315 |
| Persistently-active cohort (capture-recapture est.) | 3.0K |
| Unique payers across sampled blocks | 1.8K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $421.72M |
| xStocks 24h DEX volume | $33.82M |
| xStocks holder positions | 273.2K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($65.64M), CRCLX ($64.63M), MSTRX ($47.12M), SPYX ($47.01M), GOOGLX ($31.40M)

## Program activity and chain health

Chain tip lag: **+13.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 32,244 | 20.10% | 1.8 s |
| Pump.fun | 16,073 | 88.90% | 3.6 s |
| Jupiter v6 | 2,327 | 52.00% | 25.5 s |
| Orca Whirlpools | 1,650 | 56.20% | 36 s |
| Raydium AMM v4 | 947 | 42.90% | 63.3 s |

Median failure rate across the sampled programs: **52.00%** (range 20.10% to 88.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **46.42 SOL**.

## Exchange and large-holder balances

12.94M SOL ($1.20B) across 8 publicly-attributed accounts. Net **35K SOL (0.27%) moved off exchanges** over the last 23.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.01B | 0.9/h | 0 |
| Binance (2) | 1.12M | $103.82M | 1.8K/h | 0 |
| Gate.io | 383.05K | $35.61M | 256/h | 0 |
| Bybit | 373.02K | $34.68M | 58.7/h | 0 |
| Coinbase (2) | 73.10K | $6.80M | 201.1/h | 0 |
| Bitget | 40.01K | $3.72M | 337.7/h | 0 |
| Coinbase | 26.35K | $2.45M | 221.1/h | 0 |
| Kraken | 23.85K | $2.22M | 315.2/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 6 of 117 tested pairs survive, over 556 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.209 | 515 | 0.0000 |
| DEX volume moves with App fees | +0.200 | 515 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.197 | 522 | 0.0000 |
| Total TPS moves with Slot time | +0.158 | 522 | 0.0003 |
| Slot time moves with AMM write-lock congestion | +0.151 | 481 | 0.0009 |
| AMM write-lock congestion moves with Program failure rate | +0.144 | 481 | 0.0015 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 590.25K USD | DeFiLlama: 898.90K USD | -41.45% | *indicative*: 0.66x, within the order-of-magnitude band |
| SOL price | coingecko: 92.97 USD | Jupiter (on-chain DEX): 92.84 USD | +0.14% | agree |
| Circulating supply | getSupply (RPC): 583.18M SOL | CoinGecko: 583.18M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-21
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

## Ecosystem news

- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
- **[South Korea’s Shinhan partners with Solana Foundation, Etherfuse, Orca for tokenized fund issuance](https://www.theblock.co/news/regulation/2026-08-21-south-korea-shinhan-partners-solana-412420)** - The Block, 2026-08-21
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
