# Solana Ecosystem Report

*Generated 2026-08-22 15:42 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 6.7 robust standard deviations above its 7-day baseline: a 21.2% move to 93.23 USD from a typical 76.93.
- 🟠 **DeFi TVL** (warning): DeFi TVL is 4.8 robust standard deviations above its 7-day baseline: a 13.0% move to 5,529,324,703.00 USD from a typical 4,894,444,747.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.1K |
| TPS (non-vote) | 2.3K |
| Slot time | 369.2 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1020 (72.60% complete, ~12.1h remaining) |
| Lifetime transactions | 540.7B |
| Circulating supply | 583.2M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,896 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 29,194 / 410,000 lamports |
| Paying no priority fee | 18.90% of 5,867 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 12.70% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 686 |
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
| SOL price | $93.23 (+2.60% 24h) |
| Market cap | $54.37B (rank #7) |
| 24h volume | $8.25B |
| ATH | $293.31 (-68.21% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.53B |
| Stablecoin supply | $15.86B |
| DEX volume (24h) | $3.60B (+30.15% 1d) |
| App fees (24h, all protocols) | $13.33M |
| Chain fees (24h) | $898.90K |
| Jito MEV tips (24h) | $189.65K |
| **REV - Real Economic Value (24h)** | **$1.09M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.23B | +7.59% |
| USDT | $2.79B | -3.79% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $676.74M | -0.29% |
| USDG | $609.06M | -3.31% |
| USDe | $536.86M | -0.29% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| Orca DEX | $661.30M |
| PumpSwap | $600.74M |
| BisonFi | $562.98M |
| Raydium AMM | $281.50M |
| Scorch | $242.28M |
| Meteora DLMM | $237.06M |
| HumidiFi | $213.79M |
| Manifest Trade | $209.93M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.22M |
| pump.fun | $1.78M |
| Axiom | $1.42M |
| Jupiter Perpetual Exchange | $619.81K |
| Meteora DLMM | $506.71K |
| fomo Wallet | $481.19K |
| Raydium AMM | $457.46K |
| Sanctum Validator LSTs | $455.86K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 269 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $419.81M |
| xStocks 24h DEX volume | $21.21M |
| xStocks holder positions | 273.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($65.63M), CRCLX ($63.63M), SPYX ($47.10M), MSTRX ($46.27M), GOOGLX ($31.36M)

## Program activity and chain health

Chain tip lag: **+13.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| Pump.fun | 58,099 (approx.) | 92.10% | 0.7 s |
| SPL Token | 52,654 (approx.) | 21.50% | 0.7 s |
| Jupiter v6 | 2,230 | 25.60% | 25.5 s |
| Orca Whirlpools | 1,268 | 24.50% | 47.3 s |
| Raydium AMM v4 | 868 | 9.90% | 68.7 s |

Median failure rate across the sampled programs: **24.50%** (range 9.90% to 92.10%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **37.86 SOL**.

## Exchange and large-holder balances

12.99M SOL ($1.21B) across 8 publicly-attributed accounts. Net **19K SOL (0.15%) moved onto exchanges** over the last 23.4 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.02B | 0.9/h | 0 |
| Binance (2) | 1.13M | $105.02M | 1.7K/h | 0 |
| Bybit | 373.02K | $34.78M | 58.4/h | 0 |
| Gate.io | 370.00K | $34.50M | 187.4/h | 0 |
| Kraken | 86.72K | $8.08M | 250.3/h | 0 |
| Coinbase (2) | 59.46K | $5.54M | 390/h | 0 |
| Bitget | 38.69K | $3.61M | 265.1/h | 0 |
| Coinbase | 24.83K | $2.32M | 401.8/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 8 of 117 tested pairs survive, over 564 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.218 | 523 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.202 | 530 | 0.0000 |
| DEX volume moves with App fees | +0.199 | 523 | 0.0000 |
| Total TPS moves with Slot time | +0.163 | 530 | 0.0002 |
| Slot time moves with AMM write-lock congestion | +0.158 | 489 | 0.0004 |
| AMM write-lock congestion moves with Program failure rate | +0.136 | 489 | 0.0025 |
| Total TPS moves with AMM write-lock congestion | +0.135 | 489 | 0.0027 |
| Non-vote TPS moves with AMM write-lock congestion | +0.135 | 489 | 0.0028 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 518.37K USD | DeFiLlama: 898.90K USD | -53.70% | *indicative*: 0.58x, within the order-of-magnitude band |
| SOL price | coingecko: 93.23 USD | Jupiter (on-chain DEX): 93.21 USD | +0.02% | agree |
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

**Latest Agave release:** [v4.3.0-beta.2](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-beta.2) (2026-08-21)

**Latest Firedancer release:** [v26.08.1](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.1) (2026-08-21)

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
