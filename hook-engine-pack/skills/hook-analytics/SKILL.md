---
name: hook-analytics
description: Measurement and learning loop for hooks - defines the current YouTube Shorts, Instagram Reels and TikTok metrics, logs experiments (hook mechanism, wording, first frame, duration, architecture, metrics, context, confounders), compares a video only with comparable videos from the creator's own history, and records observations without turning noise into rules. Use for stage 9, when the user shares analytics or asks "did this hook work?", "why did views drop?", or wants to plan an A/B test.
user-invocable: true
---

# Analytics and experimentation

**Never claim a hook caused a result from one video outperforming another.** Views are driven by distribution, topic, timing, audience state and luck. Prefer the creator's own baseline over universal benchmarks (none are published by the platforms).

## Procedure
1. **Identify available metrics** per platform (`references/protocol.md`); definitions change - check date. If none -> **hypothesis mode**: state the hypothesis, the metric that would test it, and a minimal experiment.
2. **Log the video** (template `templates/experiment_log.csv`): topic, audience, mechanism id, opening wording, first-frame concept, duration, architecture, publish date, observation window, sample (impressions/shown-in-feed), metrics, traffic context, confounders.
3. **Choose comparators**: same platform, similar duration (+-25% or +-8 s), similar topic/audience lane, similar distribution context, similar age of video. Need **>= 5** comparators for any statement of "typical"; fewer -> say "insufficient baseline".
3b. **Is the test worth running?** `python3 ${CLAUDE_SKILL_DIR}/scripts/sample_size.py BASELINE_RATE MIN_DIFFERENCE` gives impressions per arm for a two-proportion comparison (e.g. 0.60 vs 0.65 needs ~1,468 viewers per arm). If your videos do not reach that many impressions, the comparison is a hypothesis, not evidence.
4. **Compare** (script: `python3 ${CLAUDE_SKILL_DIR}/scripts/analytics_compare.py videos.csv VIDEO_ID` - reports median/IQR of the creator's comparable videos and where the new video falls; no causal output). Always report n, window, and uncertainty.
5. **Interpret with hedged language**: "is associated with", "consistent with", "one observation". Phrases like "proves", "caused", "the hook worked because" are banned.
6. **Update the learning log** with a status: *observation* (one video) -> *hypothesis* (stated, untested) -> *tentative pattern* (>= 3 comparable replications, directionally consistent, confounders noted) -> never *rule*. Conflicts are recorded, not hidden.
7. **Next experiment**: change one variable (hook mechanism OR first frame OR length), keep topic lane similar, pre-register the metric and the window.

## Metric awareness (verified 2026-10-20; re-check)
- YouTube: since 2025-03-31 Shorts **views** count starts/replays with no minimum watch time; the former view metric is **engaged views**; **Stayed to watch** (formerly "viewed vs swiped away") = % of times viewers stayed past "the initial seconds" (undisclosed length); average view duration and average % viewed are computed **among those who stayed**; **from 2026-08-24 views count from first frame across all formats**. -> Never compare views across 2025-03-31 or 2026-08-24; compare engaged views and stayed-to-watch (S01, S02, S04, S05).
- Retention graph is video-level (S03). Instagram: Retention chart and **skip rate** (% of views skipped in the first 3 s) announced Aug 2025 (S10, reported quotes of Instagram). TikTok: average watch time, watched-full-video, retention graph, traffic sources reported by secondary sources - official definitions **not verified** here (S61).
- Platform-specific numbers are not interchangeable (a view starts differently per platform).

## Guardrails
- Small samples: report counts, not just percentages.
- Early observation windows are unstable; state the window.
- Do not rank hooks by raw views. Do not average across platforms.
- Record confounders: topic seasonality, trending sound, collab, posting time, thumbnail/cover (YouTube), caption text, distribution surface.

## References
- `references/protocol.md` - metric dictionary, experiment design, record fields, interpretation templates, learning-log statuses.
