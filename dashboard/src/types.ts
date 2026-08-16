/** Shape of docs/report.json, produced by the Python collector. */

export type Anomaly = {
  ts: number
  metric: string
  label: string
  severity: "critical" | "warning" | "info"
  kind: "spike" | "drop" | "threshold"
  value: number | null
  baseline_median?: number
  z_score?: number
  unit?: string
  detail: string
}

export type PerfSample = {
  slot: number
  tps: number
  true_tps: number | null
  slot_time_ms: number | null
}

export type Network = {
  health: string
  node_version: string | null
  slot: number
  block_height: number
  tx_count_total: number | null
  tps?: number
  true_tps?: number | null
  slot_time_ms?: number | null
  perf_samples: PerfSample[]
  epoch: {
    epoch: number
    slot_index: number
    slots_in_epoch: number
    pct: number
    eta_hours: number
  }
  supply: {
    total_sol: number
    circulating_sol: number
    non_circulating_sol: number
  }
  median_prioritization_fee?: number
  p90_prioritization_fee?: number
  max_prioritization_fee?: number
  prio_fee_nonzero_pct?: number
  blocks_per_day_measured?: number
  inflation_total_pct?: number
  inflation_validator_pct?: number
  inflation_terminal_pct?: number
}

export type Validators = {
  active: number
  delinquent: number
  total_active_stake_sol: number
  delinquent_stake_sol: number
  delinquent_stake_pct: number
  nakamoto_coefficient: number
  top5_stake_pct: number
  top10_stake_pct: number
  top20_stake_pct: number
  avg_commission: number | null
  avg_commission_unweighted: number | null
  private_stake_pct: number | null
  commission_buckets: Record<string, number>
  /** Cumulative stake share per validator, ordered by rank: index 0 is #1. */
  stake_curve: number[]
  top_validators: {
    vote: string
    node: string
    stake_sol: number
    share_pct: number
    commission: number | null
  }[]
}

export type Market = {
  source: string
  price_usd: number
  change_24h_pct: number | null
  market_cap_usd: number | null
  market_cap_rank?: number
  market_cap_estimated?: boolean
  volume_24h_usd?: number
  high_24h?: number
  low_24h?: number
  ath_usd?: number
  ath_change_pct?: number
  circulating_supply?: number
  price_history_7d?: [number, number][]
}

export type DeFi = {
  tvl_usd: number
  tvl_history: [number, number][]
  stablecoins_usd: number
  stablecoins_top?: {
    symbol: string
    name: string
    on_solana_usd: number
    change_7d_pct: number | null
  }[]
  dex_volume_24h_usd: number
  dex_volume_7d_usd: number
  dex_change_1d_pct: number | null
  dex_history: [number, number][]
  dex_top: { name: string; volume_24h_usd: number }[]
  app_fees_24h_usd: number
  chain_fees_24h_usd: number | null
  jito_tips_24h_usd: number | null
  rev_24h_usd?: number
  fees_24h_usd: number
  rev_history?: [number, number][]
  top_fee_apps: { name: string; fees_24h_usd: number }[]
}

export type Activity = {
  sampled_blocks: number
  unique_payers_per_block_avg?: number
  unique_payers_per_block?: number[]
  union_unique_payers?: number
  activity_index?: number
  active_cohort_est?: number | null
  cohort_lower_bound?: number
  estimator?: string
  median_tx_fee_lamports?: number
  p90_tx_fee_lamports?: number
  p99_tx_fee_lamports?: number
  mean_tx_fee_lamports?: number
  base_fee_only_pct?: number
  fee_sampled_txs?: number
  avg_fees_per_block_sol?: number
  fees_per_block_sol_low?: number
  fees_per_block_sol_high?: number
}

export type ProgramStat = {
  name: string
  address: string
  sampled: number
  failure_rate_pct: number
  tx_per_min?: number
  tx_per_min_lower_bound?: number
  window_secs?: number
  window_slots?: number
  counted?: number
  low_precision?: boolean
}

export type OnChain = {
  slot_secs_used?: number
  programs?: ProgramStat[]
  median_program_failure_rate_pct?: number
  failure_rate_span_pct?: [number, number]
  reference_slot?: number
  chain_time?: number
  drift_secs?: number
  vote_accounts?: { vote: string; stake_sol?: number; balance_sol: number }[]
  unwithdrawn_sol_top8?: number
  errors?: Record<string, string>
}

export type Correlation = {
  a: string
  b: string
  a_label: string
  b_label: string
  rho: number
  n: number
  p: number
  significant: boolean
}

export type Correlations = {
  method: string
  metrics_considered: number
  pairs_tested: number
  significant_count: number
  sample_size: number
  top: Correlation[]
}

export type CrossCheck = {
  check: string
  label: string
  a_source: string
  a_value: number
  b_source: string
  b_value: number
  unit: string
  gap_pct: number | null
  agrees: boolean
  tolerance_pct?: number
  a_interval_95?: [number, number]
  ratio?: number | null
  blocks_per_day?: number
  basis?: string
  /** False when the check is reported for corroboration but is too noisy to
   * raise an alert from. */
  alerting?: boolean
}

export type Tokenized = {
  xstocks_aum_usd?: number
  xstocks_top?: { ticker: string; usd: number }[]
  xstocks_history?: [number, number][]
  xstocks_volume_24h_usd?: number
  xstocks_holders?: number
  rwa_tvl_usd?: number
  rwa_top?: { name: string; usd: number }[]
}

export type PullRequest = {
  number: number
  simd: string | null
  title: string
  url: string
  author: string
  updated_at: string
  merged_at: string | null
  draft: boolean
}

export type Release = {
  tag: string
  name: string
  prerelease: boolean
  published_at: string
  url: string
}

export type Dev = {
  simd_open: PullRequest[]
  simd_recent_merged: PullRequest[]
  watchlist: PullRequest[]
  agave_releases?: Release[]
  firedancer_releases?: Release[]
}

export type NewsItem = {
  title: string
  link: string
  summary: string
  ts: number
  source: string
  date: string
}

export type Report = {
  ts: number
  generated_utc: string
  errors: Record<string, string>
  stale_sections: string[]
  anomalies: Anomaly[]
  network: Network
  validators: Validators
  market: Market
  defi: DeFi
  activity: Activity
  tokenized: Tokenized
  dev: Dev
  onchain?: OnChain
  correlations?: Correlations
  news: { items: NewsItem[]; feed_errors: Record<string, string> | null }
  crosscheck?: {
    checks: CrossCheck[]
    agree: number
    total: number
    divergences: CrossCheck[]
  }
}

/** One row of docs/history.json (the rolling metric history). */
export type HistoryRow = {
  ts: number
  tps?: number | null
  true_tps?: number | null
  slot_time_ms?: number | null
  validators_active?: number | null
  validators_delinquent?: number | null
  delinquent_stake_pct?: number | null
  nakamoto?: number | null
  sol_price?: number | null
  sol_change_24h?: number | null
  market_cap?: number | null
  tvl?: number | null
  stables?: number | null
  dex_vol_24h?: number | null
  fees_24h?: number | null
  rev_24h?: number | null
  activity_idx?: number | null
  active_cohort?: number | null
  [key: string]: number | null | undefined
}
