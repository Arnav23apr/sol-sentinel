# Solana Ecosystem Report

*Generated 2026-09-10 11:33 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟠 **App fees (24h, all protocols)** (warning): App fees (24h, all protocols) is 4.6 robust standard deviations above its 7-day baseline: a 43.0% move to 15,440,897.00 USD from a typical 10,796,465.50.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 3.8K |
| TPS (non-vote) | 1.6K |
| Slot time | 315.8 ms |
| Slot | 446M |
| Block height | 424M |
| Epoch | 1032 (11.51% complete, ~33.5h remaining) |
| Lifetime transactions | 547.0B |
| Circulating supply | 586.3M SOL |
| Inflation (annual) | 3.65% |
| Median transaction fee | 5,700 lamports (about $0.00058) |
| Transaction fee p90 / p99 | 52,002 / 587,540 lamports |
| Paying no priority fee | 21.30% of 4,886 sampled transactions (compared against the 5,000-lamport single-signature base fee, so multi-signature transactions are not counted here) |
| AMM write-lock congestion (150-slot window) | 34.00% of slots needed a priority fee (max 2.7M µlam/CU) |
| Node version (RPC) | 4.2.2 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 677 |
| Delinquent validators | 11 |
| Delinquent stake | 0.01% |
| Total active stake | 439.1M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.31% / 24.21% / 35.48% |
| Commission (stake-weighted, delegatable validators) | 3.77% |
| Stake on private (100% commission) validators | 23.96% |

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
| SOL price | $101.38 (-2.35% 24h) |
| Market cap | $59.44B (rank #7) |
| 24h volume | $3.15B |
| ATH | $293.31 (-65.44% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $5.83B |
| Stablecoin supply | $16.22B |
| DEX volume (24h) | $3.00B (+10.69% 1d) |
| App fees (24h, all protocols) | $15.44M |
| Chain fees (24h) | $978.48K |
| Jito MEV tips (24h) | $177.56K |
| **REV - Real Economic Value (24h)** | **$1.16M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.07B | +4.99% |
| USDT | $2.76B | -4.82% |
| USDGO | $1.38B | +10.24% |
| USD1 | $1.28B | +6.48% |
| BUIDL | $992.17M | +11.39% |
| PYUSD | $747.84M | -6.44% |
| USDG | $598.60M | -1.44% |
| USDe | $535.35M | -0.07% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| BisonFi | $402.77M |
| Raydium AMM | $364.79M |
| PumpSwap | $340.96M |
| Meteora DLMM | $322.25M |
| HumidiFi | $285.64M |
| Tessera V | $248.02M |
| Orca DEX | $198.14M |
| Manifest Trade | $131.21M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $3.36M |
| Axiom | $1.88M |
| fomo Wallet | $1.52M |
| pump.fun | $1.41M |
| Raydium AMM | $1.30M |
| Meteora DLMM | $1.19M |
| StonkFun | $968.30K |
| Orca DEX | $493.70K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | 253 |
| Persistently-active cohort (capture-recapture est.) | 2.3K |
| Unique payers across sampled blocks | 1.4K (8 blocks over 24h) |
| xStocks tokenized-equity AUM | $435.62M |
| xStocks 24h DEX volume | $189.83M |
| xStocks holder positions | 447.0K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $2.35B |

Top tokenized equities: TSLAX ($67.59M), CRCLX ($66.76M), MSTRX ($58.13M), SPYX ($46.24M), GOOGLX ($29.66M)

## Program activity and chain health

Chain tip lag: **+12.7 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 52,755 | 24.00% | 0.9 s |
| Pump.fun | 12,160 | 83.30% | 4.7 s |
| Jupiter v6 | 3,376 | 53.10% | 17.7 s |
| Orca Whirlpools | 1,835 | 41.60% | 32.5 s |
| Raydium AMM v4 | 1,295 | 27.60% | 46.1 s |

Median failure rate across the sampled programs: **41.60%** (range 24.00% to 83.30%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **648.93 SOL**.

## Exchange and large-holder balances

11.72M SOL ($1.19B) across 8 publicly-attributed accounts. Net **95K SOL (0.82%) moved onto exchanges** over the last 20.9 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.19M | $931.52M | 0.3/h | 1 |
| Binance (2) | 1.89M | $191.34M | 1.9K/h | 0 |
| Gate.io | 301.92K | $30.61M | 164.9/h | 0 |
| Bybit | 211.98K | $21.49M | 39.4/h | 0 |
| Bitget | 48.11K | $4.88M | 282.1/h | 0 |
| Kraken | 31.96K | $3.24M | 242.9/h | 0 |
| Coinbase | 27.69K | $2.81M | 263.4/h | 0 |
| Coinbase (2) | 26.94K | $2.73M | 238.4/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 13 of 117 tested pairs survive, over 794 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.223 | 753 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.194 | 760 | 0.0000 |
| Total TPS moves with Slot time | +0.155 | 760 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.144 | 719 | 0.0001 |
| Total TPS moves with AMM write-lock congestion | +0.143 | 719 | 0.0001 |
| Total TPS moves with Program failure rate | +0.122 | 741 | 0.0008 |
| Non-vote TPS moves with Program failure rate | +0.121 | 741 | 0.0009 |
| Slot time moves with AMM write-lock congestion | +0.116 | 719 | 0.0018 |
| Non-vote TPS moves with Activity index | +0.108 | 759 | 0.0029 |
| Share paying base fee only moves with Activity index | +0.108 | 783 | 0.0024 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run. A further 1 indicative check is reported for corroboration only (1 within band): their own measurement noise is wider than any threshold worth alerting on, so they never raise a finding and are not counted as agreement.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| Chain fees (24h) | sampled blocks (RPC): 786.57K USD | DeFiLlama: 978.48K USD | -21.74% | *indicative*: 0.80x, within the order-of-magnitude band |
| SOL price | coingecko: 101.38 USD | Jupiter (on-chain DEX): 101.44 USD | -0.06% | agree |
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

**Latest Firedancer release:** [v26.09.0](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.0) (2026-09-08)

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
