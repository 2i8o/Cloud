# Analytics and experiment protocol

## 1. Metric dictionary (as of 2026-10-20)

| Platform | Metric | Definition (source) | Caveat |
|---|---|---|---|
| YouTube | Views (Shorts) | Times a Short starts or replays, no minimum watch time (from 2025-03-31, S02); from 2026-08-24 views count from the first frame across all formats (S04, S05) | not comparable with pre-change views |
| YouTube | Engaged views | "How many times viewers stayed to watch past the initial seconds, not including any loops" (S01) | seconds threshold unpublished and may vary by surface (S05) |
| YouTube | Stayed to watch | "The percentage of times viewers stayed to watch past the initial seconds of a Short" (S01); earlier labelled Viewed vs swiped away (S09) | %-of-times, not people; not CTR (S06); no official benchmark |
| YouTube | Shown in feed | Times the Short was shown in the Shorts feed (S09 intro; definition text reproduced by secondary sites) | denominator for the stay decision |
| YouTube | Average view duration / average % viewed | computed among viewers who stayed (S01) | swipers excluded -> can be high while most swiped |
| YouTube | Audience retention (graph) | video-level report; flat = watched through, dips = abandonment, spikes = rewatch/share (S03) | compare against your own typical retention for similar length (YouTube shows "typical" for 10 latest similar-length videos, S03) |
| Instagram | Retention chart; skip rate | Retention shows % of views still watching at each moment; skip rate = % of views skipped within the first 3 s, replacing view rate (Instagram quote in S10, Aug 2025) | verified through press quoting Instagram; Meta help page not opened |
| Instagram | Average watch time | total watch time / initial plays (secondary sources) | definition unverified from first-party page |
| TikTok | Average watch time; Watched full video; retention graph; traffic sources | reported by secondary sources (S61) | **official definitions not verified**; treat as provisional |

Looping: engaged views exclude loops; TikTok "Watched full video" is described by secondary sources as unique-viewer based (unverified).

## 2. Experiment record fields
`video_id, platform, publish_date, observation_days, topic, lane, audience, duration_s, hook_mechanism, insight_key, opening_wording, first_frame, architecture, thumbnail/cover (if any), views, engaged_views, stayed_to_watch_pct, avg_view_duration_s, avg_pct_viewed, skip_rate_pct (IG), retention_at_3s, retention_at_10s, completion_pct, rewatch_flag, shown_in_feed (or reach), traffic_sources, shares, saves, confounders, notes`. Missing metrics stay blank; never fill with estimates.

## 3. Comparability rules
Same platform - duration within +-25% (or +-8 s) - similar lane/audience - same metric definition epoch - observation window >= 72 h (hypothesis; use the same window for all) - similar distribution surface. If distribution differs by >2x in impressions, flag as non-comparable or compare stay-rates only.

## 4. Designing an A/B-style test (organic)
True randomisation is unavailable. Use **matched pairs in sequence** (same topic family, same length, same format, same posting slot), change one variable, pre-state the metric (e.g. stayed-to-watch), minimum 3 pairs before calling anything a tentative pattern. Where available, platform features that show variants to separate audiences (e.g. Instagram "Trial Reels", mentioned by a secondary source) are an option; this package did not verify their mechanics.

## 5. Interpretation templates
- Insufficient data: "Only n=3 comparable videos; baseline unreliable. Hypothesis: [..]. Test: [..]."
- Consistent: "Stayed-to-watch of 71% sits above the creator's median of 64% (IQR 60-67, n=8, same lane, 7-day window). This is one observation; confounders: [..]."
- Contradiction: "Mechanism M02 beat M08 in 3 pairs but lost in 2; no pattern yet."
- Banned: "proves", "caused", "the hook worked because", "this always works".

## 6. Learning-log statuses
`observation` (1) -> `hypothesis` -> `tentative pattern` (>= 3 comparable replications, same direction, confounders listed) -> `retired` (if later contradicted). There is no `rule`/`law` status. Each entry keeps date, n, window, confounders, and a link to the video ids.

## 7. Official-doc update triggers
Re-open YouTube Help "Understand your YouTube content performance" (S01) and Creator Insider announcements quarterly or whenever a metric name changes; log the date in the ledger.
