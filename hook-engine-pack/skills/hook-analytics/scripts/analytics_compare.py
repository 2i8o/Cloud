#!/usr/bin/env python3
"""analytics_compare.py - compare one video with the creator's OWN comparable videos.

Descriptive only: it reports where a video sits relative to a baseline built
from comparable videos (same platform, similar duration, same lane if given,
enough observation days). It never outputs a causal claim and refuses to
state a "typical" value when the baseline is too small.

Usage:
  python3 analytics_compare.py videos.csv VIDEO_ID [--min-n 5] [--min-days 3]
          [--metrics stayed_to_watch_pct,avg_pct_viewed] [--json]

CSV columns (see templates/experiment_log.csv): video_id, platform, publish_date,
observation_days, lane, duration_s, hook_mechanism, views, engaged_views,
stayed_to_watch_pct, avg_view_duration_s, avg_pct_viewed, skip_rate_pct,
retention_3s_pct, completion_pct, shown_in_feed, confounders ...
Stdlib only (Python >= 3.8).
"""
import csv
import json
import statistics
import sys
from datetime import date

DEFAULT_METRICS = ["stayed_to_watch_pct", "avg_pct_viewed", "skip_rate_pct",
                   "retention_3s_pct", "completion_pct", "avg_view_duration_s"]
# Definition-change dates that make raw YouTube view counts non-comparable.
YT_VIEW_EPOCHS = [date(2025, 3, 31), date(2026, 8, 24)]
DISCLAIMER = ("Descriptive comparison only. It does not establish causation for any "
              "hook, mechanism or edit; distribution, topic, timing and audience "
              "state are uncontrolled.")


def num(x):
    try:
        return float(str(x).strip())
    except (TypeError, ValueError):
        return None


def parse_date(s):
    try:
        return date.fromisoformat(str(s).strip()[:10])
    except ValueError:
        return None


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def comparable(target, other, min_days):
    if other["video_id"] == target["video_id"]:
        return False
    if other.get("platform") != target.get("platform"):
        return False
    td, od = num(target.get("duration_s")), num(other.get("duration_s"))
    if td is None or od is None:
        return False
    if abs(td - od) > max(8.0, 0.25 * td):
        return False
    if target.get("lane") and other.get("lane") and target["lane"] != other["lane"]:
        return False
    days = num(other.get("observation_days"))
    return days is not None and days >= min_days


def quartiles(vals):
    if len(vals) < 2:
        return (vals[0], vals[0], vals[0]) if vals else (None,) * 3
    q = statistics.quantiles(vals, n=4, method="inclusive")
    return q[0], q[1], q[2]


def compare(rows, vid, min_n=5, min_days=3, metrics=None):
    metrics = metrics or DEFAULT_METRICS
    target = next((r for r in rows if r["video_id"] == vid), None)
    if target is None:
        raise SystemExit(f"video_id {vid!r} not found")
    comps = [r for r in rows if comparable(target, r, min_days)]
    out = {"video_id": vid, "platform": target.get("platform"),
           "n_comparators": len(comps), "min_n": min_n, "metrics": {}, "warnings": []}
    t_days = num(target.get("observation_days"))
    if t_days is None:
        out["warnings"].append("target observation_days missing: window unknown")
    elif t_days < min_days:
        out["warnings"].append(f"target observed only {t_days:g} day(s) (< {min_days}): early numbers are unstable")
    if comps and t_days is not None:
        med_days = statistics.median(num(c["observation_days"]) for c in comps)
        if t_days < 0.5 * med_days or t_days > 2 * med_days:
            out["warnings"].append(f"observation window differs from comparators (target {t_days:g} d vs median {med_days:g} d)")
    if target.get("platform", "").lower().startswith("youtube"):
        dates = [parse_date(target.get("publish_date"))] + [parse_date(c.get("publish_date")) for c in comps]
        dates = [d for d in dates if d]
        if dates and any(min(dates) < e <= max(dates) for e in YT_VIEW_EPOCHS):
            out["warnings"].append("comparators span a YouTube view-definition change (2025-03-31 / 2026-08-24): do NOT compare raw views; use engaged views / stayed-to-watch")
    if target.get("confounders"):
        out["confounders_noted"] = target["confounders"]
    for m in metrics:
        tv = num(target.get(m))
        vals = [v for v in (num(c.get(m)) for c in comps) if v is not None]
        if tv is None:
            continue
        entry = {"target": tv, "n": len(vals)}
        if len(vals) < min_n:
            entry["status"] = f"INSUFFICIENT BASELINE (n={len(vals)} < {min_n}): hypothesis mode, no 'typical' value reported"
        else:
            q1, med, q3 = quartiles(vals)
            entry.update(median=round(med, 2), q1=round(q1, 2), q3=round(q3, 2),
                         rank=round(sum(1 for v in vals if v <= tv) / len(vals), 2))
            entry["position"] = ("above IQR" if tv > q3 else "below IQR" if tv < q1 else "within IQR")
            entry["status"] = "descriptive"
        out["metrics"][m] = entry
    out["disclaimer"] = DISCLAIMER
    return out


def render(res):
    lines = [f"Video {res['video_id']} ({res['platform']}) vs {res['n_comparators']} comparable video(s) "
             f"[same platform, similar duration, same lane if given, >= min observation days]"]
    for w in res["warnings"]:
        lines.append(f"WARNING: {w}")
    if not res["metrics"]:
        lines.append("No requested metric has a value for this video.")
    for m, e in res["metrics"].items():
        if e["status"].startswith("INSUFFICIENT"):
            lines.append(f"- {m}: value {e['target']:g} | {e['status']}")
        else:
            lines.append(f"- {m}: value {e['target']:g} | baseline median {e['median']:g} (IQR {e['q1']:g}-{e['q3']:g}, n={e['n']}) "
                         f"| {e['position']} | at/below this value: {int(e['rank']*100)}% of comparators")
    lines.append(res["disclaimer"])
    return "\n".join(lines)


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    path, vid = argv[1], argv[2]
    opts = {"--min-n": 5, "--min-days": 3, "--metrics": None}
    i = 3
    while i < len(argv):
        if argv[i] in opts and i + 1 < len(argv):
            opts[argv[i]] = argv[i + 1]
            i += 2
        else:
            i += 1
    metrics = opts["--metrics"].split(",") if opts["--metrics"] else None
    try:
        rows = load(path)
    except OSError as e:
        print(f"cannot read CSV: {e}", file=sys.stderr)
        return 2
    res = compare(rows, vid, int(opts["--min-n"]), int(opts["--min-days"]), metrics)
    print(json.dumps(res, ensure_ascii=False, indent=2) if "--json" in argv else render(res))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
