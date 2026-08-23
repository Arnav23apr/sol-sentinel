# Solana Ecosystem Report

*Generated 2026-08-23 21:11 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.2K |
| TPS (non-vote) | 2.3K |
| Slot time | 365.9 ms |
| Slot | 441M |
| Block height | 419M |
| Epoch | 1021 (39.69% complete, ~26.5h remaining) |
| Lifetime transactions | 541.1B |
| Circulating supply | 583.3M SOL |
| Inflation (annual) | 3.68% |
| Median transaction fee | 5,400 lamports (about $0.00052) |
| Transaction fee p90 / p99 | 20,000 / 410,000 lamports |
| Paying no priority fee | 23.00% of 5,496 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 17.30% of slots needed a priority fee (max 454.7K µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 685 |
| Delinquent validators | 10 |
| Delinquent stake | 0.04% |
| Total active stake | 433.3M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.26% / 24.31% / 35.70% |
| Commission (stake-weighted, delegatable validators) | 3.79% |
| Stake on private (100% commission) validators | 24.24% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.0M | 3.92% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.70% | 0% |
| 3 | `3N7s…iD5g` | 12.2M | 2.82% | 0% |
| 4 | `Catz…Diqb` | 11.7M | 2.71% | 5% |
| 5 | `26pV…3dJx` | 9.2M | 2.12% | 7% |
| 6 | `51JB…UNAm` | 8.9M | 2.05% | 10% |
| 7 | `8Gbw…F8iD` | 8.5M | 1.96% | 0% |
| 8 | `9QU2…29mF` | 7.9M | 1.83% | 7% |
| 9 | `CvSb…wycB` | 7.4M | 1.70% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.52% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $95.54 (+0.70% 24h) |
| Market cap | $55.73B (rank #7) |
| 24h volume | $4.40B |
| ATH | $293.31 (-67.43% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.58B |
| Stablecoin supply | $15.92B |
| DEX volume (24h) | $3.73B (+3.65% 1d) |
| App fees (24h, all protocols) | $12.02M |
| Chain fees (24h) | $785.84K |
| Jito MEV tips (24h) | $159.24K |
| **REV - Real Economic Value (24h)** | **$945.08K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.23B | +7.82% |
| USDT | $2.83B | -2.24% |
| USDGO | $1.19B | +0.55% |
| USD1 | $1.07B | +1.52% |
| BUIDL | $777.14M | +4.88% |
| PYUSD | $688.04M | +1.39% |
| USDG | $608.49M | -4.26% |
| USDe | $536.77M | -0.21% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $584.36M |
| PumpSwap | $570.01M |
| Orca DEX | $403.84M |
| Meteora DLMM | $377.27M |
| Scorch | $363.43M |
| Raydium AMM | $219.06M |
| Tessera V | $175.26M |
| Manifest Trade | $140.96M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.01M |
| pump.fun | $1.50M |
| Axiom | $1.16M |
| Jupiter Perpetual Exchange | $1.04M |
| Meteora DLMM | $985.54K |
| fomo Wallet | $476.51K |
| Raydium AMM | $399.99K |
| Collector Crypt | $290.50K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 275 |
| Persistently-active cohort (capture-recapture est.) | 2.6K |
| Unique payers across sampled blocks | 1.6K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $420.55M |
| xStocks 24h DEX volume | $8.45M |
| xStocks holder positions | 273.6K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.95B |

Top tokenized equities: TSLAX ($66.04M), CRCLX ($63.91M), SPYX ($47.13M), MSTRX ($45.06M), GOOGLX ($31.34M)

## Program activity and chain health

Chain tip lag: **+13.4 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 49,631 | 31.30% | 1.1 s |
| Pump.fun | 30,697 | 78.50% | 1.8 s |
| Jupiter v6 | 5,012 | 48.60% | 11.7 s |
| Orca Whirlpools | 3,506 | 62.10% | 16.5 s |
| Raydium AMM v4 | 2,590 | 19.10% | 23.1 s |

Median failure rate across the sampled programs: **48.60%** (range 19.10% to 78.50%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **35.30 SOL**.

## Exchange and large-holder balances

13.03M SOL ($1.24B) across 7 publicly-attributed accounts. Net **104K SOL (0.81%) moved onto exchanges** over the last 23.5 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $1.04B | 1.2/h | 0 |
| Binance (2) | 1.23M | $117.71M | 930.2/h | 0 |
| Gate.io | 392.27K | $37.48M | 142.9/h | 0 |
| Bybit | 373.03K | $35.64M | 22/h | 0 |
| Bitget | 67.28K | $6.43M | 184.1/h | 0 |
| Kraken | 34.91K | $3.34M | 324.3/h | 0 |
| Coinbase | 18.18K | $1.74M | 451.1/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 8 of 117 tested pairs survive, over 616 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.214 | 575 | 0.0000 |
| DEX volume moves with App fees | +0.209 | 575 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.181 | 582 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.144 | 541 | 0.0008 |
| Total TPS moves with Slot time | +0.143 | 582 | 0.0006 |
| Non-vote TPS moves with AMM write-lock congestion | +0.138 | 541 | 0.0013 |
| Total TPS moves with AMM write-lock congestion | +0.136 | 541 | 0.0016 |
| Non-vote TPS moves with Activity index | +0.122 | 581 | 0.0033 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 411.13K USD | DeFiLlama: 785.84K USD | -62.61% | *indicative*: 0.52x, within the order-of-magnitude band |
| SOL price | coingecko: 95.54 USD | Jupiter (on-chain DEX): 95.59 USD | -0.05% | agree |
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

- **[Solana cuts mainnet slot time to 350 milliseconds in first step toward 200ms goal](https://www.theblock.co/news/ecosystems/2026-08-22-solana-cuts-mainnet-slot-time-to-350-milliseconds-in-first-step-toward-200ms-goal-412521)** - The Block, 2026-08-22
- **[Solana Just Got Faster—Is It Bullish for SOL?](https://decrypt.co/376245/solana-faster-bullish-sol-price)** - Decrypt, 2026-08-21
- **[South Korea’s Shinhan partners with Solana Foundation, Etherfuse, Orca for tokenized fund issuance](https://www.theblock.co/news/regulation/2026-08-21-south-korea-shinhan-partners-solana-412420)** - The Block, 2026-08-21
- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
