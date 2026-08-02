"""Test suite for the collector. Standard library `unittest` only, matching
the no-dependency rule for the rest of the pipeline.

    python3 -m unittest discover -s tests -v

Nothing here touches the network: every test runs against fixtures or stubs,
so it is safe to run in CI and offline.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import time
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sentinel import (  # noqa: E402
    anomaly, collect_activity, collect_defi, collector, crosscheck, fmt,
    history, main,
)
from sentinel.collect_news import _items_from_feed, _parse_date  # noqa: E402


def flat_history(n: int = 200, **series) -> list[dict]:
    """n evenly spaced runs where each named metric holds a steady value."""
    now = int(time.time())
    return [
        {"ts": now - (n - i) * 1800,
         **{k: v + (i % 5) * (abs(v) * 0.001) for k, v in series.items()}}
        for i in range(n)
    ]


class TestRobustZ(unittest.TestCase):
    def test_returns_none_below_minimum_baseline(self):
        self.assertIsNone(anomaly.robust_z(100.0, [1.0, 2.0, 3.0]))

    def test_zero_for_a_value_at_the_median(self):
        # 49/50/51 repeating: median 50, MAD 1, so 50 scores exactly zero.
        window = [49.0 + (i % 3) for i in range(60)]
        self.assertEqual(anomaly.robust_z(50.0, window), 0.0)

    def test_scales_with_distance_from_the_median(self):
        window = [10.0 + (i % 4) for i in range(60)]
        near = anomaly.robust_z(14.0, window)
        far = anomaly.robust_z(40.0, window)
        self.assertIsNotNone(near)
        self.assertIsNotNone(far)
        self.assertGreater(abs(far), abs(near))

    def test_constant_window_reports_infinity_not_a_crash(self):
        # MAD and stdev are both zero; the estimator has no scale to divide by.
        self.assertEqual(anomaly.robust_z(5.0, [3.0] * 40), float("inf"))
        self.assertIsNone(anomaly.robust_z(3.0, [3.0] * 40))


class TestDetect(unittest.TestCase):
    def test_silent_on_a_normal_snapshot(self):
        rows = flat_history(tps=2800, slot_time_ms=420, sol_price=72.0)
        latest = dict(rows[-1], ts=int(time.time()))
        self.assertEqual(anomaly.detect(rows, latest), [])

    def test_flags_a_throughput_collapse(self):
        rows = flat_history(tps=2800)
        latest = {"ts": int(time.time()), "tps": 400}
        metrics = {f["metric"] for f in anomaly.detect(rows, latest)}
        self.assertIn("tps", metrics)

    def test_ignores_a_throughput_surge(self):
        # TPS is watched in the "drop" direction: more throughput is not an
        # incident, and alerting on it would cry wolf on every busy day.
        rows = flat_history(tps=2800)
        latest = {"ts": int(time.time()), "tps": 9000}
        self.assertEqual(anomaly.detect(rows, latest), [])

    def test_ignores_a_slot_time_improvement(self):
        rows = flat_history(slot_time_ms=450)
        latest = {"ts": int(time.time()), "slot_time_ms": 300}
        self.assertEqual(anomaly.detect(rows, latest), [])

    def test_price_is_watched_in_both_directions(self):
        rows = flat_history(sol_price=72.0)
        up = anomaly.detect(rows, {"ts": 1, "sol_price": 200.0})
        down = anomaly.detect(rows, {"ts": 1, "sol_price": 20.0})
        self.assertTrue(any(f["metric"] == "sol_price" for f in up))
        self.assertTrue(any(f["metric"] == "sol_price" for f in down))

    def test_one_finding_per_metric(self):
        # A collapse trips the statistical layer and the absolute rule at once.
        rows = flat_history(tps=2800, slot_time_ms=420, delinquent_stake_pct=0.07)
        latest = {"ts": int(time.time()), "tps": 200, "slot_time_ms": 900,
                  "delinquent_stake_pct": 15.0}
        found = anomaly.detect(rows, latest)
        metrics = [f["metric"] for f in found]
        self.assertEqual(len(metrics), len(set(metrics)), f"duplicates: {metrics}")

    def test_merged_finding_records_the_other_layer(self):
        rows = flat_history(tps=2800)
        latest = {"ts": int(time.time()), "tps": 200}
        tps = next(f for f in anomaly.detect(rows, latest) if f["metric"] == "tps")
        self.assertEqual(tps.get("also_flagged_by"), "drop")

    def test_infinite_z_score_is_not_rendered_as_inf(self):
        rows = [{"ts": int(time.time()) - i * 1800, "tvl": 4.7e9} for i in range(60)]
        found = anomaly.detect(rows, {"ts": int(time.time()), "tvl": 3.0e9})
        tvl = next(f for f in found if f["metric"] == "tvl")
        self.assertIsNone(tvl["z_score"])
        self.assertNotIn("inf", tvl["detail"])

    def test_every_finding_is_json_serializable(self):
        rows = flat_history(tps=2800, sol_price=72.0)
        found = anomaly.detect(rows, {"ts": 1, "tps": 100, "sol_price": 10.0,
                                      "sol_change_24h": -40.0})
        self.assertTrue(found)
        json.dumps(found)  # the report pipeline would fail on a NaN or inf

    def test_no_em_dashes_in_alert_text(self):
        rows = flat_history(tps=2800, slot_time_ms=420)
        found = anomaly.detect(rows, {"ts": 1, "tps": 100, "slot_time_ms": 900,
                                      "sol_change_24h": -30.0})
        self.assertTrue(found)
        for f in found:
            self.assertNotIn("—", f["detail"])


class TestHistoryContract(unittest.TestCase):
    """Guards the seam between modules: history writes the keys that the
    anomaly engine watches. A typo on either side would silently stop a metric
    from ever alerting, with no error anywhere."""

    SNAPSHOT = {
        "ts": 1,
        "network": {"slot": 1, "block_height": 2, "tps": 2800.0, "true_tps": 1200.0,
                    "slot_time_ms": 421.0, "median_prioritization_fee": 0,
                    "inflation_total_pct": 3.7,
                    "epoch": {"epoch": 1010, "pct": 80.0},
                    "supply": {"circulating_sol": 581_000_000}},
        "validators": {"active": 693, "delinquent": 11, "delinquent_stake_pct": 0.07,
                       "nakamoto_coefficient": 18, "avg_commission": 3.8,
                       "total_active_stake_sol": 432_000_000},
        "market": {"price_usd": 72.0, "change_24h_pct": -1.3, "market_cap_usd": 4.1e10},
        "defi": {"tvl_usd": 4.7e9, "stablecoins_usd": 1.5e10,
                 "dex_volume_24h_usd": 1.3e9, "fees_24h_usd": 5.7e6,
                 "rev_24h_usd": 5.2e5},
        "activity": {"activity_index": 240, "active_cohort_est": 2300},
    }

    def test_every_watched_metric_is_written_to_history(self):
        row = history.headline_row(self.SNAPSHOT)
        missing = [k for k in anomaly.WATCHED if k not in row]
        self.assertEqual(missing, [], f"watched but never recorded: {missing}")

    def test_watched_metrics_carry_real_values(self):
        row = history.headline_row(self.SNAPSHOT)
        empty = [k for k in anomaly.WATCHED
                 if k in row and row[k] is None and k in
                 ("tps", "sol_price", "tvl", "activity_idx")]
        self.assertEqual(empty, [], f"recorded as None: {empty}")

    def test_missing_sections_do_not_raise(self):
        self.assertIsNone(history.headline_row({"ts": 1})["tps"])

    def test_stale_sections_are_recorded_as_gaps_not_repeated_values(self):
        # Re-recording last run's price under this run's timestamp would
        # fabricate a data point and, over a multi-run outage, flatten the
        # anomaly baseline to zero variance.
        row = history.headline_row(self.SNAPSHOT, stale=["market"])
        self.assertIsNone(row["sol_price"])
        self.assertIsNone(row["market_cap"])
        self.assertEqual(row["tps"], 2800.0)  # unaffected sections stay live

    def test_a_gap_does_not_flatten_the_baseline(self):
        now = int(time.time())
        rows = [{"ts": now - (60 - i) * 1800,
                 "sol_price": None if i >= 30 else 72.0 + (i % 3)}
                for i in range(60)]
        # The outage half contributes nothing rather than 30 identical points.
        self.assertEqual(len(history.series(rows, "sol_price")), 30)

    def test_round_trip_through_the_jsonl_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "data", "history.jsonl")
            history.append({"ts": 1, "tps": 100}, path)
            history.append({"ts": 2, "tps": 200}, path)
            self.assertEqual([r["tps"] for r in history.load(path)], [100, 200])

    def test_a_corrupt_line_does_not_lose_the_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "history.jsonl")
            with open(path, "w", encoding="utf-8") as f:
                f.write('{"ts":1,"tps":100}\n{ broken\n{"ts":2,"tps":200}\n')
            self.assertEqual([r["tps"] for r in history.load(path)], [100, 200])


class TestErrorIsolation(unittest.TestCase):
    def test_a_dead_source_degrades_only_its_own_section(self):
        def boom():
            raise RuntimeError("endpoint down")

        with tempfile.TemporaryDirectory() as tmp:
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                with mock.patch.object(
                    collector, "SECTIONS",
                    [("network", lambda: {"tps": 2800, "supply": {}}),
                     ("market", boom)],
                ):
                    snap = collector.collect(verbose=False)
                    self.assertEqual(snap["network"]["tps"], 2800)
                    self.assertIn("market", snap["errors"])
                    # No previous snapshot exists, so the section is omitted
                    # rather than presented with stale numbers.
                    self.assertNotIn("market", snap)
                    self.assertEqual(snap["stale_sections"], [])
            finally:
                os.chdir(cwd)

    def test_a_failed_section_falls_back_to_the_last_good_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            cwd = os.getcwd()
            os.chdir(tmp)
            try:
                os.makedirs("data", exist_ok=True)
                with open(collector.LATEST_PATH, "w", encoding="utf-8") as f:
                    json.dump({"market": {"price_usd": 70.0}}, f)

                def boom():
                    raise RuntimeError("endpoint down")

                # crosscheck is stubbed because it would otherwise reach
                # Jupiter for a live price; it has its own offline tests below.
                with mock.patch.object(collector, "SECTIONS", [("market", boom)]), \
                        mock.patch.object(collector.crosscheck, "crosscheck",
                                          return_value={"checks": [], "agree": 0,
                                                        "total": 0,
                                                        "divergences": []}):
                    snap = collector.collect(verbose=False)
                    self.assertEqual(snap["market"]["price_usd"], 70.0)
                    # The report must say so rather than pass it off as fresh.
                    self.assertIn("market", snap["stale_sections"])
            finally:
                os.chdir(cwd)


class TestDefiPartialFailure(unittest.TestCase):
    """The DeFi section fans out to four independent DeFiLlama endpoints, so
    one bad endpoint must not blank the three that worked."""

    def test_a_failed_endpoint_keeps_the_others(self):
        def boom():
            raise RuntimeError("llama 500")

        with mock.patch.multiple(
            collect_defi,
            tvl=lambda: {"tvl_usd": 4.7e9, "stablecoins_usd": 1.5e10},
            dex=lambda: {"dex_volume_24h_usd": 1.3e9},
            fees_and_rev=boom,
            stablecoin_breakdown=lambda: [],
        ):
            out = collect_defi.defi()
        self.assertEqual(out["tvl_usd"], 4.7e9)
        self.assertEqual(out["dex_volume_24h_usd"], 1.3e9)
        self.assertIn("fees", out["partial_errors"])

    def test_total_failure_raises_so_the_section_goes_stale(self):
        def boom():
            raise RuntimeError("llama down")

        with mock.patch.multiple(collect_defi, tvl=boom, dex=boom,
                                 fees_and_rev=boom,
                                 stablecoin_breakdown=boom):
            with self.assertRaises(Exception):
                collect_defi.defi()

    def test_missing_solana_row_gives_a_readable_error(self):
        with self.assertRaises(Exception) as ctx:
            collect_defi._find_solana([{"name": "Ethereum"}], "llama /v2/chains")
        self.assertIn("Solana", str(ctx.exception))


class TestAtomicWrites(unittest.TestCase):
    def test_a_failed_render_cannot_truncate_the_previous_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "report.json")
            main._write(path, '{"good": true}')
            try:
                main._write(path, json.dumps({"x": float("nan")},
                                             allow_nan=False))
            except ValueError:
                pass
            with open(path, encoding="utf-8") as f:
                self.assertEqual(json.load(f), {"good": True})


class TestCrossCheck(unittest.TestCase):
    """Cross-source validation compares two independent readings of the same
    quantity. These run offline by supplying both readings directly."""

    def snapshot(self, **over):
        base = {
            "network": {"supply": {"circulating_sol": 581_000_000}},
            "market": {"price_usd": 70.0, "source": "jupiter",
                       "circulating_supply": 581_000_000},
            "defi": {"chain_fees_24h_usd": 400_000},
            "activity": {"measured_daily_fees_sol": 5_000,
                         "measured_daily_fees_sol_low": 3_000,
                         "measured_daily_fees_sol_high": 7_000},
        }
        for k, v in over.items():
            base.setdefault(k, {}).update(v)
        return base

    def test_agrees_when_the_other_source_falls_inside_the_interval(self):
        # Our interval is 3,000-7,000 SOL at $70 = $210k-$490k; llama says
        # $400k, which is inside.
        res = crosscheck.crosscheck(self.snapshot())
        fees = next(c for c in res["checks"] if c["check"] == "chain_fees")
        self.assertTrue(fees["agrees"])
        self.assertEqual(fees["a_interval_95"], [210_000, 490_000])
        self.assertEqual(res["divergences"], [])

    def test_diverges_when_the_other_source_falls_outside(self):
        res = crosscheck.crosscheck(
            self.snapshot(defi={"chain_fees_24h_usd": 2_000_000}))
        fees = next(c for c in res["checks"] if c["check"] == "chain_fees")
        self.assertFalse(fees["agrees"])
        self.assertEqual(len(res["divergences"]), 1)

    def test_a_divergence_becomes_a_finding(self):
        res = crosscheck.crosscheck(
            self.snapshot(defi={"chain_fees_24h_usd": 2_000_000}))
        findings = crosscheck.divergence_findings(res)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "warning")
        self.assertIn("95% interval", findings[0]["detail"])
        # Must match the anomaly finding shape so both render identically.
        for key in ("metric", "label", "severity", "kind", "detail"):
            self.assertIn(key, findings[0])

    def test_supply_mismatch_is_caught(self):
        res = crosscheck.crosscheck(
            self.snapshot(market={"circulating_supply": 700_000_000}))
        supply = next(c for c in res["checks"]
                      if c["check"] == "circulating_supply")
        self.assertFalse(supply["agrees"])

    def test_gap_is_symmetric_between_sources(self):
        # Measured against the mean, so neither source is treated as truth.
        self.assertEqual(crosscheck._gap_pct(100, 200),
                         -crosscheck._gap_pct(200, 100))

    def test_missing_inputs_are_skipped_not_guessed(self):
        res = crosscheck.crosscheck({"network": {}, "market": {}, "defi": {},
                                     "activity": {}})
        self.assertEqual(res["checks"], [])
        self.assertEqual(res["total"], 0)


class TestFeeStats(unittest.TestCase):
    def test_percentiles_and_base_fee_share(self):
        fees = [5000] * 50 + [50_000] * 40 + [5_000_000] * 10
        out = collect_activity._fee_stats(fees, [])
        self.assertEqual(out["median_tx_fee_lamports"], 50_000)
        self.assertEqual(out["base_fee_only_pct"], 50.0)
        self.assertEqual(out["fee_sampled_txs"], 100)
        # The mean is dragged far above the median by the heavy tail, which is
        # exactly why the report leads with the median.
        self.assertGreater(out["mean_tx_fee_lamports"],
                           out["median_tx_fee_lamports"])

    def test_confidence_interval_brackets_the_estimate(self):
        out = collect_activity._fee_stats([], [10**9, 12**8, 11**8, 9**8,
                                               10**8, 13**8, 8**8, 10**8])
        self.assertLessEqual(out["measured_daily_fees_sol_low"],
                             out["measured_daily_fees_sol"])
        self.assertGreaterEqual(out["measured_daily_fees_sol_high"],
                                out["measured_daily_fees_sol"])

    def test_interval_is_omitted_when_the_sample_is_too_small(self):
        out = collect_activity._fee_stats([], [10**9, 10**9])
        self.assertNotIn("measured_daily_fees_sol_low", out)

    def test_no_samples_yields_no_claims(self):
        self.assertEqual(collect_activity._fee_stats([], []), {})


class TestNewsParsing(unittest.TestCase):
    RSS = """<?xml version="1.0"?><rss version="2.0"><channel>
      <item><title>Alpenglow ships</title><link>https://example.com/a</link>
        <description>A summary.</description>
        <pubDate>Thu, 30 Jul 2026 15:25:00 GMT</pubDate></item>
    </channel></rss>"""

    ATOM = """<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">
      <entry><title>Preconfirmations</title>
        <link href="https://example.com/b"/>
        <summary>Another summary.</summary>
        <updated>2026-07-29T18:00:00.000Z</updated></entry>
    </feed>"""

    def test_parses_rss(self):
        items = _items_from_feed(self.RSS)
        self.assertEqual(items[0]["title"], "Alpenglow ships")
        self.assertEqual(items[0]["link"], "https://example.com/a")
        self.assertGreater(items[0]["ts"], 0)

    def test_parses_atom_including_the_link_attribute(self):
        items = _items_from_feed(self.ATOM)
        self.assertEqual(items[0]["title"], "Preconfirmations")
        self.assertEqual(items[0]["link"], "https://example.com/b")
        self.assertGreater(items[0]["ts"], 0)

    def test_unparseable_date_sorts_last_instead_of_raising(self):
        self.assertEqual(_parse_date("not a date"), 0.0)
        self.assertEqual(_parse_date(""), 0.0)


class TestFormatting(unittest.TestCase):
    def test_compact_units(self):
        self.assertEqual(fmt.usd(4_700_000_000), "$4.70B")
        self.assertEqual(fmt.usd(523_300), "$523.30K")
        self.assertEqual(fmt.num(2_842), "2.8K")

    def test_none_renders_as_a_placeholder_not_a_crash(self):
        for fn in (fmt.usd, fmt.num, fmt.pct, fmt.iso_day):
            self.assertEqual(fn(None), "-")
        self.assertEqual(fmt.short_pubkey(None), "-")

    def test_signed_percentages(self):
        self.assertEqual(fmt.pct(1.5, signed=True), "+1.50%")
        self.assertEqual(fmt.pct(-1.5, signed=True), "-1.50%")
        self.assertEqual(fmt.pct(1.5), "1.50%")

    def test_zero_is_not_treated_as_missing(self):
        self.assertEqual(fmt.pct(0.0), "0.00%")
        self.assertEqual(fmt.num(0), "0")

    def test_exact_never_abbreviates(self):
        # A 5,514-lamport fee compacted to "6K" would lose the whole point.
        self.assertEqual(fmt.exact(5514), "5,514")
        self.assertEqual(fmt.exact(6031), "6,031")
        self.assertEqual(fmt.exact(None), "-")


if __name__ == "__main__":
    unittest.main()
