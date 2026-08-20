# Solana Ecosystem Report

*Generated 2026-08-20 02:10 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🔴 **SOL price** (critical): SOL price is 19.6 robust standard deviations above its 7-day baseline: a 12.9% move to 85.29 USD from a typical 75.56.
- 🔴 **DeFi TVL** (critical): DeFi TVL is 14.9 robust standard deviations above its 7-day baseline: a 8.5% move to 5,229,371,035.00 USD from a typical 4,821,544,292.00.
- 🟠 **SOL price move** (warning): SOL moved +10.9% in 24h.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.7K |
| TPS (non-vote) | 2.0K |
| Slot time | 413.8 ms |
| Slot | 440M |
| Block height | 418M |
| Epoch | 1019 (40.65% complete, ~29.5h remaining) |
| Lifetime transactions | 539.8B |
| Circulating supply | 583.0M SOL |
| Inflation (annual) | 3.69% |
| Median transaction fee | 5,612 lamports (about $0.00048) |
| Transaction fee p90 / p99 | 32,936 / 895,727 lamports |
| Paying no priority fee | 15.10% of 8,622 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 7.30% of slots needed a priority fee (max 762.8K µlam/CU) |
| Node version (RPC) | 4.2.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 688 |
| Delinquent validators | 8 |
| Delinquent stake | 0.02% |
| Total active stake | 435.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.38% / 24.38% / 35.72% |
| Commission (stake-weighted, delegatable validators) | 3.81% |
| Stake on private (100% commission) validators | 24.19% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.1M | 3.93% | 7% |
| 2 | `he1i…uBtk` | 16.0M | 3.68% | 0% |
| 3 | `Catz…Diqb` | 12.4M | 2.85% | 5% |
| 4 | `3N7s…iD5g` | 12.2M | 2.80% | 0% |
| 5 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 6 | `51JB…UNAm` | 9.0M | 2.07% | 10% |
| 7 | `8Gbw…F8iD` | 8.3M | 1.91% | 0% |
| 8 | `9QU2…29mF` | 8.0M | 1.84% | 7% |
| 9 | `CvSb…wycB` | 7.3M | 1.69% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.50% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $85.29 (+10.90% 24h) |
| Market cap | $49.73B (rank #7) |
| 24h volume | $4.62B |
| ATH | $293.31 (-70.92% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.23B |
| Stablecoin supply | $15.74B |
| DEX volume (24h) | $2.76B (+49.92% 1d) |
| App fees (24h, all protocols) | $10.60M |
| Chain fees (24h) | $649.17K |
| Jito MEV tips (24h) | $119.86K |
| **REV - Real Economic Value (24h)** | **$769.03K** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.09B | +1.88% |
| USDT | $2.86B | -3.38% |
| USDGO | $1.19B | +2.62% |
| USD1 | $1.06B | +0.86% |
| BUIDL | $740.49M | +1.69% |
| PYUSD | $668.87M | -1.79% |
| USDG | $629.98M | -3.31% |
| USDe | $537.57M | -0.03% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $753.62M |
| BisonFi | $440.28M |
| HumidiFi | $331.84M |
| Orca DEX | $278.60M |
| Meteora DLMM | $157.58M |
| Manifest Trade | $153.96M |
| Raydium AMM | $136.18M |
| pump.fun | $111.39M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $2.85M |
| pump.fun | $1.51M |
| Axiom | $1.31M |
| Phantom Wallet | $544.74K |
| fomo Wallet | $449.17K |
| Meteora DLMM | $442.63K |
| Collector Crypt | $362.58K |
| Jito Liquid Staking | $243.45K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 360 |
| Persistently-active cohort (capture-recapture est.) | 3.6K |
| Unique payers across sampled blocks | 2.1K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $406.25M |
| xStocks 24h DEX volume | $29.72M |
| xStocks holder positions | 272.1K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.90B |

Top tokenized equities: TSLAX ($63.79M), CRCLX ($59.51M), SPYX ($44.92M), MSTRX ($44.30M), GOOGLX ($31.01M)

## Program activity and chain health

Chain tip lag: **+15.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 68,366 (approx.) | 25.70% | 0.8 s |
| Pump.fun | 38,811 | 90.40% | 1.2 s |
| Jupiter v6 | 9,000 | 75.30% | 6.2 s |
| Orca Whirlpools | 4,819 | 66.30% | 12.4 s |
| Raydium AMM v4 | 1,414 | 36.00% | 41.8 s |

Median failure rate across the sampled programs: **66.30%** (range 25.70% to 90.40%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **311.44 SOL**.

## Exchange and large-holder balances

12.62M SOL ($1.08B) across 8 publicly-attributed accounts. Net **446K SOL (3.66%) moved onto exchanges** over the last 24.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 10.91M | $930.40M | 1.7/h | 0 |
| Binance (2) | 833.90K | $71.12M | 932.6/h | 0 |
| Gate.io | 362.30K | $30.90M | 149.8/h | 0 |
| Bybit | 325.52K | $27.76M | 65.7/h | 0 |
| Bitget | 61.05K | $5.21M | 142.4/h | 0 |
| Coinbase | 46.62K | $3.98M | 399.1/h | 0 |
| Coinbase (2) | 42.86K | $3.66M | 370.8/h | 0 |
| Kraken | 37.77K | $3.22M | 297/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 4 of 117 tested pairs survive, over 471 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.245 | 430 | 0.0000 |
| AMM write-lock congestion moves with Program failure rate | +0.190 | 396 | 0.0001 |
| DEX volume moves with App fees | +0.185 | 430 | 0.0001 |
| Non-vote TPS moves with Slot time | +0.173 | 437 | 0.0003 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 2.28M USD | DeFiLlama: 649.17K USD | +111.37% | *indicative*: 3.51x, within the order-of-magnitude band |
| SOL price | coingecko: 85.29 USD | Jupiter (on-chain DEX): 85.12 USD | +0.20% | agree |
| Circulating supply | getSupply (RPC): 583.01M SOL | CoinGecko: 583.01M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-14
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0602: Disallow Nonce Account as Program ID](https://github.com/solana-foundation/solana-improvement-documents/pull/602) - updated 2026-08-19
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - updated 2026-08-14
- [simd-0504: remove identical signature requirement](https://github.com/solana-foundation/solana-improvement-documents/pull/593) - updated 2026-08-07
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-08-14
- [SIMD-0579: Keccak-p1600 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/579) - updated 2026-07-27
- [SIMD-0571: Soft Deprecation of Durable Nonce Transactions](https://github.com/solana-foundation/solana-improvement-documents/pull/571) - updated 2026-08-19

**Recently merged SIMDs:**

- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12
- [re-amend SIMD-0340: additional inter- and intra- validation](https://github.com/solana-foundation/solana-improvement-documents/pull/551) - updated 2026-07-31
- [SIMD-0433: Loader V3: Set Program Data to ELF Length](https://github.com/solana-foundation/solana-improvement-documents/pull/433) - updated 2026-07-31
- [SIMD-0266: Efficient Token program](https://github.com/solana-foundation/solana-improvement-documents/pull/266) - updated 2026-07-29
- [SIMD-0392: Clarify included stake accounts and calculations](https://github.com/solana-foundation/solana-improvement-documents/pull/572) - updated 2026-07-16

**Latest Agave release:** [v4.2.1](https://github.com/anza-xyz/agave/releases/tag/v4.2.1) (2026-08-13)

**Latest Firedancer release:** [v0.1106.40201](https://github.com/firedancer-io/firedancer/releases/tag/v0.1106.40201) (2026-08-19)

## Ecosystem news

- **[Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic)** - Solana.com, 2026-08-19
- **[Solana Policy Institute CEO says Clarity Act in ‘August recess purgatory,’ gives it 10% odds before midterms](https://www.theblock.co/news/regulation/2026-08-18-solana-policy-institute-ceo-larity-act-august-recess-purgatory-gives-10-odds-midterms-412171)** - The Block, 2026-08-18
- **[Securitize brings Neuberger’s $230 billion fixed-income platform onchain with new tokenized fund](https://www.theblock.co/news/markets/2026-08-18-securitize-neubergers-230-billion-fixed-income-platform-onchain-new-tokenized-fund-412102)** - The Block, 2026-08-18
- **[Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off)** - Solana.com, 2026-08-17
- **[Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026)** - Solana.com, 2026-08-13
- **[How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi)** - Solana.com, 2026-08-13
- **[Why Asia Is Ahead on Stablecoins, According to Reap's Daren Guo](https://solana.com/news/bits-to-bricks-asia-ahead-stablecoins-daren-guo-reap)** - Solana.com, 2026-08-12
- **[Agave 4.2 Update:  All You Need to Know](https://www.helius.dev/blog/agave-v4-2)** - Helius, 2026-08-11
- **[MoneyGram Ramps launches on Solana](https://solana.com/news/moneygram-ramps)** - Solana.com, 2026-08-11
- **[Solana Changelog: August 6, 2026](https://solana.com/news/solana-changelog-august-6-2026)** - Solana.com, 2026-08-06

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
