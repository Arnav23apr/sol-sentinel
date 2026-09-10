# Solana Ecosystem Report

*Generated 2026-09-10 15:24 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **App fees (24h, all protocols)** (warning): App fees (24h, all protocols) is 3.7 robust standard deviations above its 7-day baseline: a 41.1% move to 15,435,517.00 USD from a typical 10,935,785.00.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.0K |
| TPS (non-vote) | 2.0K |
| Slot time | 320 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1032 (21.63% complete, ~30.1h remaining) |
| Lifetime transactions | 547.1B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,502 lamports (about $0.00055) |
| Transaction fee p90 / p99 | 50,584 / 1,005,000 lamports |
| Paying no priority fee | 25.80% of 4,748 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 30.70% of slots needed a priority fee (max 13.7M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 675 |
| Delinquent validators | 14 |
| Delinquent stake | 0.05% |
| Total active stake | 439.0M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.32% / 24.22% / 35.50% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.97% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.4M | 3.97% | 7% |
| 2 | `he1i…uBtk` | 16.3M | 3.72% | 0% |
| 3 | `3N7s…iD5g` | 12.5M | 2.85% | 0% |
| 4 | `Catz…Diqb` | 11.4M | 2.59% | 5% |
| 5 | `8Gbw…F8iD` | 9.6M | 2.18% | 0% |
| 6 | `26pV…3dJx` | 9.3M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.0M | 2.06% | 10% |
| 8 | `9QU2…29mF` | 7.3M | 1.67% | 7% |
| 9 | `CvSb…wycB` | 6.9M | 1.57% | 5% |
| 10 | `Dumi…Zk4a` | 6.6M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $99.75 (-2.33% 24h) |
| Market cap | $58.46B (rank #7) |
| 24h volume | $3.48B |
| ATH | $293.31 (-65.99% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.77B |
| Stablecoin supply | $16.18B |
| DEX volume (24h) | $3.00B (+10.69% 1d) |
| App fees (24h, all protocols) | $15.44M |
| Chain fees (24h) | $978.48K |
| Jito MEV tips (24h) | $177.73K |
| **REV - Real Economic Value (24h)** | **$1.16M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.13B | +5.83% |
| USDT | $2.68B | -7.57% |
| USDGO | $1.38B | +10.24% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $992.17M | +11.39% |
| PYUSD | $735.84M | -7.95% |
| USDG | $599.13M | -1.38% |
| USDe | $536.25M | +0.09% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $402.77M |
| Raydium AMM | $348.41M |
| PumpSwap | $340.96M |
| Meteora DLMM | $322.25M |
| HumidiFi | $285.64M |
| Tessera V | $248.02M |
| Orca DEX | $198.14M |
| Manifest Trade | $142.91M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.36M |
| Axiom | $1.88M |
| fomo Wallet | $1.52M |
| pump.fun | $1.41M |
| Meteora DLMM | $1.19M |
| Raydium AMM | $1.18M |
| StonkFun | $968.30K |
| Orca DEX | $493.70K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 309 |
| Persistently-active cohort (capture-recapture est.) | 3.8K |
| Unique payers across sampled blocks | 1.9K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $188.17M |
| xStocks holder positions | 450.9K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $1.91B |

## Program activity and chain health

Chain tip lag: **+12.0 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 72,281 (approx.) | 24.80% | 0.6 s |
| Jupiter v6 | 8,934 | 79.00% | 6.4 s |
| Raydium AMM v4 | 5,352 | 35.50% | 11.2 s |
| Pump.fun | 4,793 | 61.20% | 12.5 s |
| Orca Whirlpools | 4,247 | 68.50% | 13.8 s |

Median failure rate across the sampled programs: **61.20%** (range 24.80% to 79.00%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **235.20 SOL**.

## Exchange and large-holder balances

11.68M SOL ($1.16B) across 8 publicly-attributed accounts. Net **20K SOL (0.17%) moved onto exchanges** over the last 21.3 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $916.55M | 0.3/h | 1 |
| Binance (2) | 1.84M | $183.53M | 1.7K/h | 0 |
| Gate.io | 293.86K | $29.31M | 184.5/h | 0 |
| Bybit | 211.98K | $21.15M | 45.8/h | 0 |
| Bitget | 57.42K | $5.73M | 275.7/h | 0 |
| Kraken | 36.15K | $3.61M | 216.3/h | 0 |
| Coinbase (2) | 26.43K | $2.64M | 461.5/h | 0 |
| Coinbase | 24.99K | $2.49M | 486.5/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 795 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.223 | 754 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.196 | 761 | 0.0000 |
| Total TPS moves with Slot time | +0.157 | 761 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.143 | 720 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.142 | 720 | 0.0001 |
| Total TPS moves with Program failure rate | +0.124 | 742 | 0.0007 |
| Non-vote TPS moves with Program failure rate | +0.124 | 742 | 0.0007 |
| Slot time moves with AMM write-lock congestion | +0.115 | 720 | 0.0021 |
| Share paying base fee only moves with Activity index | +0.111 | 784 | 0.0019 |
| Non-vote TPS moves with Activity index | +0.110 | 760 | 0.0024 |
| Total TPS moves with Activity index | +0.103 | 760 | 0.0046 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 824.98K USD | DeFiLlama: 978.48K USD | -17.02% | *indicative*: 0.84x, within the order-of-magnitude band |
| SOL price | coingecko: 99.75 USD | Jupiter (on-chain DEX): 99.74 USD | +0.01% | agree |
| Circulating supply | getSupply (RPC): 586.34M SOL | CoinGecko: 586.34M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-08
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *open*, updated 2026-09-02
- [simd-0553 amendment: adjust inclusion fee](https://github.com/solana-foundation/solana-improvement-documents/pull/600) - *open*, updated 2026-08-24
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - *merged*, updated 2026-09-08
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - *merged*, updated 2026-08-12

**Open SIMD proposals:**

- [SIMD-0558 Amendment: Specify use of sol_get_sysvar](https://github.com/solana-foundation/solana-improvement-documents/pull/634) - updated 2026-09-10
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - updated 2026-09-08
- [amend SIMD-0464: clarify aliasing rules](https://github.com/solana-foundation/solana-improvement-documents/pull/618) - updated 2026-09-03
- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-09
- [SIMD-0612: Two-Phase Leader Schedule](https://github.com/solana-foundation/solana-improvement-documents/pull/612) - updated 2026-08-26
- [SIMD-0610: Prohibit Nonce Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/610) - updated 2026-09-02

**Recently merged SIMDs:**

- [SIMD-0387: update feature ID](https://github.com/solana-foundation/solana-improvement-documents/pull/518) - updated 2026-09-10
- [SIMD-0558 - Leader Info Syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/621) - updated 2026-09-10
- [SIMD-0608: `DeactivateDelinquent` for Closed Vote Accounts](https://github.com/solana-foundation/solana-improvement-documents/pull/608) - updated 2026-09-08
- [SIMD-0599: Remove inactive stakes from partitioned epoch rewards](https://github.com/solana-foundation/solana-improvement-documents/pull/599) - updated 2026-08-27
- [SIMD-0553: Resource and Inclusion Fee](https://github.com/solana-foundation/solana-improvement-documents/pull/553) - updated 2026-08-12
- [SIMD-0550: Double disinflation](https://github.com/solana-foundation/solana-improvement-documents/pull/550) - updated 2026-08-12

**Latest Agave release:** [v4.3.0-rc.0](https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.0) (2026-09-04)

**Latest Firedancer release:** [v26.08.3](https://github.com/firedancer-io/firedancer/releases/tag/v26.08.3) (2026-09-10)

## Ecosystem news

- **[Solana treasury firm SkyAI faces board challenge from would-be acquirer Forward Industries, shareholder group](https://www.theblock.co/news/business/2026-09-09-solana-treasury-firm-skyai-board-challenge-would-be-acquirer-forward-industries-shareholder-group-414061)** - The Block, 2026-09-09
- **[Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances)** - Solana.com, 2026-09-08
- **[How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor)** - Solana.com, 2026-09-07
- **[Solana Transaction Versioning: Legacy, v0 and v1](https://www.helius.dev/blog/solana-transaction-versions)** - Helius, 2026-09-05
- **[Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026)** - Solana.com, 2026-09-04
- **[Introducing the Parsed Events API and Parsed Streams](https://www.helius.dev/blog/parsed-events-and-streams)** - Helius, 2026-09-03
- **[Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second)** - Solana.com, 2026-09-03
- **[How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction)** - Solana.com, 2026-09-03
- **[The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped)** - Solana.com, 2026-09-02
- **[Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america)** - Solana.com, 2026-09-01

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
