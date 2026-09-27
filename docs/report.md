# Solana Ecosystem Report

*Generated 2026-09-27 13:09 UTC by [sol-sentinel](https://github.com/Arnav23apr/sol-sentinel) - auto-updating, keyless, Python-stdlib-only.*

## Alerts

- 🟢 No anomalies detected. All watched metrics are within their 7-day baselines and absolute health thresholds.

## Network performance

| Metric | Value |
|---|---|
| RPC health | ok |
| TPS (total, 10-min median) | 4.6K |
| TPS (non-vote) | 2.1K |
| Slot time | 268.5 ms |
| Slot | 451M |
| Block height | 429M |
| Epoch | 1043 (99.58% complete, ~0.1h remaining) |
| Lifetime transactions | 553.3B |
| Circulating supply | 587.7M SOL |
| Inflation (annual) | 3.63% |
| AMM write-lock congestion (150-slot window) | 22.70% of slots needed a priority fee (max 10.0M µlam/CU) |
| Node version (RPC) | 4.3.0 |

## Validators & decentralization

| Metric | Value |
|---|---|
| Active validators | 676 |
| Delinquent validators | 11 |
| Delinquent stake | 0.01% |
| Total active stake | 437.5M SOL |
| Nakamoto coefficient | 18 |
| Top-5 / Top-10 / Top-20 stake share | 15.56% / 24.61% / 35.43% |
| Commission (stake-weighted, delegatable validators) | 3.82% |
| Stake on private (100% commission) validators | 23.17% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaH…oTN1` | 17.9M | 4.08% | 7% |
| 2 | `he1i…uBtk` | 15.8M | 3.61% | 0% |
| 3 | `3N7s…iD5g` | 12.3M | 2.82% | 0% |
| 4 | `Catz…Diqb` | 11.2M | 2.57% | 5% |
| 5 | `8Gbw…F8iD` | 10.8M | 2.48% | 0% |
| 6 | `26pV…3dJx` | 9.2M | 2.11% | 7% |
| 7 | `51JB…UNAm` | 9.2M | 2.10% | 10% |
| 8 | `9QU2…29mF` | 7.6M | 1.74% | 7% |
| 9 | `CvSb…wycB` | 7.1M | 1.62% | 5% |
| 10 | `Dumi…Zk4a` | 6.5M | 1.49% | 0% |

## Market

| Metric | Value |
|---|---|
| SOL price | $123.12 (+1.64% 24h) |
| Market cap | $72.33B (rank #7) |
| 24h volume | $3.51B |
| ATH | $293.31 (-58.02% from ATH) |
| Price source | coingecko |

## DeFi & economic indicators

| Metric | Value |
|---|---|
| TVL | $6.73B |
| Stablecoin supply | $16.49B |
| DEX volume (24h) | $2.16B (-17.52% 1d) |
| App fees (24h, all protocols) | $17.82M |
| Chain fees (24h) | $1.21M |
| Jito MEV tips (24h) | $268.11K |
| **REV - Real Economic Value (24h)** | **$1.48M** (chain fees + MEV tips) |

### Top stablecoins on Solana

| Symbol | $ on Solana | 7d Δ |
|---|---|---|
| USDC | $7.27B | +4.59% |
| USDT | $2.66B | +25.99% |
| USDGO | $1.41B | +1.73% |
| USD1 | $1.39B | +4.45% |
| BUIDL | $987.88M | -0.53% |
| PYUSD | $760.45M | +3.71% |
| USDG | $674.25M | +7.27% |
| USDe | $466.48M | -8.85% |

### Top DEXs by 24h volume

| DEX | 24h volume |
|---|---|
| PumpSwap | $513.61M |
| BisonFi | $251.33M |
| pump.fun | $210.79M |
| Orca DEX | $203.45M |
| Raydium AMM | $176.72M |
| fomo Wallet | $171.04M |
| Meteora DLMM | $162.30M |
| Axiom | $150.83M |

### Top apps by 24h fees

| App | 24h fees |
|---|---|
| PumpSwap | $5.59M |
| pump.fun | $2.70M |
| Axiom | $1.54M |
| Meteora DLMM | $1.09M |
| fomo Wallet | $680.49K |
| StonkFun | $582.58K |
| Raydium AMM | $499.17K |
| pump.fun Mobile App | $493.86K |

## Activity & tokenized assets

| Metric | Value |
|---|---|
| Activity index: unique fee payers per block (24h sampled avg) | - |
| Unique payers across sampled blocks | - (0 blocks over 24h) |
| xStocks tokenized-equity AUM | - |
| xStocks 24h DEX volume | $48.17M |
| xStocks holder positions | 645.3K (summed per ticker, so one wallet holding several is counted more than once) |
| Total RWA TVL on Solana | $546.81M |

## Program activity and chain health

Chain tip lag: **+10.3 s**, the age of the newest confirmed block's own timestamp against wall clock. It sits at a steady offset rather than accumulating; a rise means confirmations are falling behind.

Throughput and failure rate for major programs, from the last 1,000 signatures on each, timed by slot span. The failure rate is a direct read on user experience and is not published by volume-only dashboards.

| Program | Transactions/min | Failed | Sample window |
|---|---|---|---|
| SPL Token | 69,423 | 24.40% | 0.8 s |
| Pump.fun | 30,327 | 72.90% | 1.9 s |
| Orca Whirlpools | 5,186 | 18.10% | 11.5 s |
| Jupiter v6 | 2,861 | 54.50% | 20.7 s |
| Raydium AMM v4 | 2,419 | 23.80% | 24.7 s |

Median failure rate across the sampled programs: **24.40%** (range 18.10% to 72.90%). A median over five programs, not a chain-wide rate, and it varies widely between them.

Unwithdrawn inflation rewards sitting in the top 8 vote accounts: **83.45 SOL**.

## Exchange and large-holder balances

12.70M SOL ($1.56B) across 7 publicly-attributed accounts. Net **53K SOL (0.42%) moved onto exchanges** over the last 23.0 h.

| Account | Balance (SOL) | Value | Activity | Failed |
|---|---|---|---|---|
| Binance | 9.94M | $1.22B | 0.2/h | 0 |
| Binance (2) | 2.04M | $251.39M | 1.2K/h | 0 |
| Bybit | 387.38K | $47.69M | 37/h | 0 |
| Gate.io | 261.74K | $32.23M | 288.9/h | 3 |
| Kraken | 36.82K | $4.53M | 262/h | 0 |
| Coinbase | 15.89K | $1.96M | 213.3/h | 0 |
| Coinbase (2) | 11.29K | $1.39M | 297.3/h | 0 |

*Balances are re-verified on the chain every run and an account is dropped if it no longer holds a meaningful amount, so a stale label cannot become a false claim. Attribution is best-effort from public sources: Sentinel verifies what an account holds, never who controls it.*

## What moves together

Relationships between metrics, rather than each metric on its own. 12 of 117 tested pairs survive, over 904 observations.

*Method: Spearman rank correlation of period-over-period changes, with Benjamini-Hochberg false-discovery control at q=0.05 across all pairs tested. Changes are correlated rather than levels, because two series that both drift upward correlate near +1 whatever the real relationship. Rank correlation is used so a single outlier cannot manufacture a result.*

| Relationship | rho | n | p |
|---|---|---|---|
| DeFi TVL moves with xStocks AUM | +0.311 | 753 | 0.0000 |
| DEX volume moves with App fees | +0.223 | 863 | 0.0000 |
| Non-vote TPS moves with Slot time | +0.210 | 870 | 0.0000 |
| Non-vote TPS moves with AMM write-lock congestion | +0.191 | 829 | 0.0000 |
| Total TPS moves with AMM write-lock congestion | +0.186 | 829 | 0.0000 |
| Total TPS moves with Slot time | +0.170 | 870 | 0.0000 |
| Total TPS moves with Program failure rate | +0.155 | 851 | 0.0000 |
| Non-vote TPS moves with Program failure rate | +0.154 | 851 | 0.0000 |
| SOL price moves with DeFi TVL | +0.139 | 904 | 0.0000 |
| Slot time moves with AMM write-lock congestion | +0.129 | 829 | 0.0002 |
| Share paying base fee only moves with Activity index | +0.118 | 818 | 0.0007 |
| SOL price moves with xStocks AUM | +0.102 | 753 | 0.0049 |

## Cross-source validation

Quantities that two independent sources can both see, compared against each other. 2 of 2 precise checks agree this run.

| Quantity | Source A | Source B | Gap | Verdict |
|---|---|---|---|---|
| SOL price | coingecko: 123.12 USD | Jupiter (on-chain DEX): 123.06 USD | +0.05% | agree |
| Circulating supply | getSupply (RPC): 587.71M SOL | CoinGecko: 587.71M SOL | -0.00% | agree |

## Protocol development

**Upgrade watchlist** (consensus/fees/Alpenglow-related SIMDs):

- [SIMD-0643: Move fee burn rounding from per slot to per transaction](https://github.com/solana-foundation/solana-improvement-documents/pull/643) - *open*, updated 2026-09-17
- [SIMD-0123: Refine calculation and inclusion based on Alpenglow](https://github.com/solana-foundation/solana-improvement-documents/pull/641) - *open*, updated 2026-09-16
- [SIMD-0630: Slot Time Compensation for Alpenglow Fast Leader Handover](https://github.com/solana-foundation/solana-improvement-documents/pull/630) - *open*, updated 2026-09-25
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - *merged*, updated 2026-09-15

**Open SIMD proposals:**

- [SIMD: Typed Settlement Wire Linkage via SPL Memo v2 and Token-2022 Introspection](https://github.com/solana-foundation/solana-improvement-documents/pull/671) - updated 2026-09-27
- [SIMD-0670: ABIv1 invoke signed v2 syscall](https://github.com/solana-foundation/solana-improvement-documents/pull/670) - updated 2026-09-27
- [SIMD-0650: bn254 pairing output](https://github.com/solana-foundation/solana-improvement-documents/pull/650) - updated 2026-09-25
- [SIMD-0648: Unbound LoaderV3 Instruction Data](https://github.com/solana-foundation/solana-improvement-documents/pull/648) - updated 2026-09-23
- [SIMD-0646: Disable legacy and v0 transaction formats](https://github.com/solana-foundation/solana-improvement-documents/pull/646) - updated 2026-09-25
- [SIMD-0645: SVM JIT intrinsics sol_multi3](https://github.com/solana-foundation/solana-improvement-documents/pull/645) - updated 2026-09-23

**Recently merged SIMDs:**

- [Amend simd 0376 ed25519-zebra verification](https://github.com/solana-foundation/solana-improvement-documents/pull/616) - updated 2026-09-25
- [SIMD-0215: clarify LtHash security considerations](https://github.com/solana-foundation/solana-improvement-documents/pull/669) - updated 2026-09-25
- [SIMD-0558: Describe pointer validation & update CU cost](https://github.com/solana-foundation/solana-improvement-documents/pull/651) - updated 2026-09-23
- [SIMD-0582: Early detection of instruction trace overflow](https://github.com/solana-foundation/solana-improvement-documents/pull/582) - updated 2026-09-16
- [SIMD-0377: fix JMP32 register opcodes, JSGE32 condition and callx opcode](https://github.com/solana-foundation/solana-improvement-documents/pull/639) - updated 2026-09-15
- [SIMD-0609: Prohibit Vote Account Self-Withdrawals](https://github.com/solana-foundation/solana-improvement-documents/pull/609) - updated 2026-09-15

**Latest Agave release:** [v4.4.0-alpha.5](https://github.com/anza-xyz/agave/releases/tag/v4.4.0-alpha.5) (2026-09-18)

**Latest Firedancer release:** [v26.09.4](https://github.com/firedancer-io/firedancer/releases/tag/v26.09.4) (2026-09-22)

## Ecosystem news

- **[Bitcoin Rally Slows as $15.6 Billion Options Expiry Hits—XRP and Solana Keep Climbing](https://decrypt.co/379319/bitcoin-slows-billion-options-expiry-xrp-solana)** - Decrypt, 2026-09-25
- **[Solana treasury firm SkyAI keeps board after shareholder protest, loses equity plan vote](https://www.theblock.co/news/business/2026-09-24-solana-treasury-skyai-keeps-board-shareholder-protest-loses-equity-plan-vote-416298)** - The Block, 2026-09-24
- **[Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026)** - Solana.com, 2026-09-24
- **[Solana Foundation Hires Binance's Former Global CMO for Institutional Push](https://decrypt.co/379179/solana-foundation-hires-binances-former-global-cmo-for-institutional-push)** - Decrypt, 2026-09-24
- **[Solana Foundation taps Binance, Polygon vets to drive institutional adoption and payments](https://www.theblock.co/news/ecosystems/2026-09-24-solana-foundation-taps-binance-polygon-vets-to-drive-institutional-adoption-and-payments-416254)** - The Block, 2026-09-24
- **[Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption)** - Solana.com, 2026-09-23
- **[Agave 4.3 Update: All You Need to Know](https://www.helius.dev/blog/agave-v4-3)** - Helius, 2026-09-21
- **[Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026)** - Solana.com, 2026-09-19
- **[How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates)** - Solana.com, 2026-09-19
- **[Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana)** - Solana.com, 2026-09-16

---

**Data sources (all keyless):** Solana JSON-RPC (mainnet-beta + publicnode fallback), DeFiLlama, CoinGecko (Jupiter/Binance/Coinbase fallbacks), GitHub REST, solana.com & Helius RSS.
