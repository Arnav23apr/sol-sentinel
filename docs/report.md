# Solana Ecosystem Report

*Generated 2026-08-24 13:28 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **Delinquent stake** (critical): Delinquent stake is 16.2 robust standard deviations above its 7-day baseline: a 1731.6% move to 0.52 % from a typical 0.03.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.9K |
| TPS (non-vote) | 2.1K |
| Slot time | 365.9 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1021 (76.87% complete, ~10.2h remaining) |
| Lifetime transactions | 541.4B |
| Circulating supply | 583.3M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,548 lamports (about $0.00053) |
| Transaction fee p90 / p99 | 26,863 / 417,170 lamports |
| Paying no priority fee | 19.40% of 5,863 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 8.70% of slots needed a priority fee (max 19.2M µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 684 |
| Delinquent validators | 11 |
| Delinquent stake | 0.52% |
| Total active stake | 431.2M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.34% / 24.43% / 35.87% |
| Commission (stake-weighted, delegatable validators) | 3.78% |
| Stake on private (100% commission) validators | 24.36% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.94% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.83% | 0% |
| 4 | `Catz…Diqb` | 11.7M | 2.72% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.13% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.06% | 10% |
| 7 | `8Gbw…F8iD` | 8.5M | 1.97% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.71% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $96.13 (+0.99% 24h) |
| Market cap | $56.06B (rank #7) |
| 24h volume | $4.24B |
| ATH | $293.31 (-67.22% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.57B |
| Stablecoin supply | $15.83B |
| DEX volume (24h) | $2.94B (-21.27% 1d) |
| App fees (24h, all protocols) | $12.56M |
| Chain fees (24h) | $696.89K |
| Jito MEV tips (24h) | $129.28K |
| **REV - Real Economic Value (24h)** | **$826.18K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.15B | +6.52% |
| USDT | $2.83B | -2.24% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.81% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $673.40M | -0.68% |
| USDG | $624.37M | -1.67% |
| USDe | $536.48M | -0.18% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $712.73M |
| BisonFi | $438.48M |
| Orca DEX | $323.38M |
| Scorch | $270.62M |
| Meteora DLMM | $269.04M |
| Raydium AMM | $172.68M |
| Manifest Trade | $136.97M |
| Tessera V | $87.16M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.25M |
| pump.fun | $1.42M |
| Axiom | $1.13M |
| Jupiter Perpetual Exchange | $651.76K |
| Meteora DLMM | $631.90K |
| fomo Wallet | $605.37K |
| Sanctum Validator LSTs | $403.69K |
| Phantom Wallet | $299.34K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 254 |
| Persistently-active cohort (capture-recapture est.) | 2.2K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $420.09M |
| xStocks 24h DEX volume | $13.18M |
| xStocks holder positions | 274.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($65.55M), CRCLX ($63.88M), SPYX ($47.04M), MSTRX ($45.43M), GOOGLX ($31.21M)

## Program activity and chain health

Chain tip lag: **+12.5 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 74,693 (approx.) | 38.70% | 0.7 s |
| Pump.fun | 24,980 | 88.70% | 2.2 s |
| Jupiter v6 | 4,549 | 53.10% | 12.8 s |
| Orca Whirlpools | 2,266 | 69.70% | 26 s |
| Raydium AMM v4 | 933 | 21.70% | 64 s |

Median failure rate across the sampled programs: **53.10%** (range 21.70% to 88.70%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.30 SOL**.

## Exchange and large-holder balances

13.16M SOL ($1.27B) across 8 publicly-attributed accounts. Net **67K SOL (0.52%) moved onto exchanges** over the last 23.6 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.05B | 1.3/h | 8 |
| Binance (2) | 1.24M | $118.89M | 1.1K/h | 0 |
| Gate.io | 427.13K | $41.06M | 250.3/h | 0 |
| Bybit | 373.02K | $35.86M | 41.6/h | 0 |
| Coinbase (2) | 95.42K | $9.17M | 308.7/h | 0 |
| Bitget | 66.64K | $6.41M | 300.3/h | 0 |
| Kraken | 41.23K | $3.96M | 199.3/h | 0 |
| Coinbase | 12.23K | $1.18M | 339.6/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 5 of 117 tested pairs survive, over 635 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.211 | 594 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.185 | 601 | 0.0000 |
| DEX volume moves with App fees | +0.183 | 594 | 0.0000 |
| Total TPS moves with Slot time | +0.147 | 601 | 0.0003 |
| Slot time moves with AMM write-lock congestion | +0.144 | 560 | 0.0007 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 761.18K USD | DeFiLlama: 696.89K USD | +8.82% | *indicative*: 1.09x, within the order-of-magnitude band |
| SOL price | coingecko: 96.13 USD | Jupiter (on-chain DEX): 96.02 USD | +0.11% | agree |
| Circulating supply | getSupply (RPC): 583.28M SOL | CoinGecko: 583.28M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [Correct bank hash components in SIMD-0298](https://github.com/solana-foundation/solana-improvement-documents/pull/604) - updated 2026-08-20
- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-22
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-20
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-24
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

- **[Solana cuts mainnet slot time to 350 milliseconds in first step toward 200ms goal](https://www.theblock.co/news/ecosystems/2026-08-22-solana-cuts-mainnet-slot-time-to-350-milliseconds-in-first-step-toward-200ms-goal-412521)** - The Block, 2026-08-22
- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
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
