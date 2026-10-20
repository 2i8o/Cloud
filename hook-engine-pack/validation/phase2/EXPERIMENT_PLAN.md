# Practical experiment plan: do the new hooks beat the creator's own?

Purpose: replace the same-model scoring in this validation with evidence from real audiences. Nothing below has been run. Nothing here assumes the platform benchmarks that do not exist; the comparison is always against the creator's **own** comparable videos.

## 0. What the creator needs to supply (blocking)
1. 10-20 published Shorts/Reels/TikToks (last 6 months): script, spoken hook, first-frame description, duration, publication date, platform.
2. Platform exports/screenshots per video: YouTube **Stayed to watch**, **engaged views**, **average view duration / average % viewed**, retention graph; Instagram **skip rate**, **retention chart**, average watch time; TikTok **average watch time**, **watched full video**, retention graph, traffic sources. Date of export.
3. Any hook written with the existing `hook-director` skill (it exists in the creator's catalogue but was not installed here).
4. Confirmation of Iraqi terms flagged in `skills/hook-writing/references/iraqi-arabic.md` section 8b.
Put them in `skills/hook-analytics/templates/experiment_log.csv` format (one row per video).

## 1. Step 1 - baseline (no new videos needed)
`python3 skills/hook-analytics/scripts/analytics_compare.py videos.csv VIDEO_ID` for each old video: median/IQR of stay-rate (or skip rate) among comparable videos (same platform, duration within +-25%/8 s, same lane, >= 3 observation days). Need >= 5 comparators per platform or the baseline is "insufficient". This also tells you the spread you must beat.

## 2. Step 2 - cheap pre-test (before publishing): the 3-second comprehension check
For each candidate hook, show **only the first 3 seconds, muted and then with sound**, to 8-12 people from the target audience (not friends who know the topic). Ask three questions in writing, immediately: (a) "What is this video asking or promising?" (b) "Would you keep watching? why?" (c) "What do you expect the video to show next?". Score (a) as correct/incorrect against the intended gap; track (c) vs the real payoff (promise-payoff match). Compare old hook vs new hook on the same topic. Decision rule (pre-registered): a hook with < 70% correct on (a) is rewritten; the threshold is a **starting guess**, not a literature value. This measures clarity and expectation, **not** retention.

## 3. Step 3 - matched-pair field test
- **Unit of analysis:** a pair = two videos with the same lane and platform, duration within +-25%, topics of similar familiarity, published in comparable slots (alternate days; counterbalance which version goes first).
- **One variable per pair:** hook mechanism OR hook shape OR first frame OR length. Everything else (cover/caption/hashtags, sound policy, posting hour) held constant and logged.
- **Primary metric** (pre-registered): YouTube *Stayed to watch*; Instagram *skip rate* (lower is better); TikTok *average watch time / duration* (secondary: watched-full-video). **Secondary:** average % viewed (YouTube; computed among those who stayed), retention-graph shape, shares/saves per 1,000 views.
- **Observation window:** fixed in advance (suggest 7 days) and identical for both videos; stop earlier only if both reach the target impressions.
- **Sample size per arm (impressions/viewers who saw it, not views):**

| baseline stay-rate -> hoped-for | per arm (alpha .05, power .8) |
|---|---|
| 60% -> 65% | ~1,468 |
| 60% -> 70% | ~354 |
| 50% -> 60% | ~385 |

(`python3 skills/hook-analytics/scripts/sample_size.py BASE DIFF`; normal approximation, independent viewers. Organic posting is not randomised and viewers are not independent, so treat these as a lower bound.) If your videos reach far fewer impressions than this, say the test is underpowered and use only the pre-test and the retention-graph shape descriptively.
- **How many pairs:** the unit that matters is the pair. A sign test over pairs cannot reach p < .05 with fewer than 5 pairs (5 of 5 in the same direction: one-sided p = 0.031; 3 of 3: 0.125). Plan **>= 5 pairs per hypothesis** before calling anything a tentative pattern; fewer = observations only (hook-analytics learning-log rules).
- **Per pair report:** n impressions, the two stay-rates, difference, 95% CI of the difference (two-proportion), confounders (trending sound, collab, topic seasonality, distribution surface), and which numbers are missing.
- **Decision rules (pre-registered):** the new-engine hook is *tentatively* better only if (i) it wins >= 4 of 5 pairs on the primary metric, (ii) the pooled difference exceeds the creator's historical week-to-week noise (the IQR from Step 1), and (iii) it does not lose on promise-payoff signals (comment complaints, average % viewed). Otherwise: "no evidence of difference".

## 4. What would invalidate the test
Posting different topics under the label "same topic"; changing covers/captions between arms; stopping when the numbers look good; comparing views across the YouTube definition changes (2025-03-31, 2026-08-24); reading average view duration as if swipers were included (they are not); a viral outlier driven by an external share.

## 5. Cost and order
1. Week 0: collect data (Step 0) and compute baselines (Step 1).
2. Week 1: pre-test 6-9 candidate openings (Step 2) - no publishing risk.
3. Weeks 2-6: 5 matched pairs for the single most informative contrast (suggested: *question vs statement hook* on myth-correction topics, because that is where Phase 2 found most no-gap hooks).
4. Review: update the learning log with status *observation*/*hypothesis*/*tentative pattern* only as the rules above allow.

## 6. What is not testable this way
Iraqi naturalness (needs native readers), long-run brand effect, and any claim about "the algorithm".
