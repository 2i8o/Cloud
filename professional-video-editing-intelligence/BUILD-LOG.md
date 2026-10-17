# Build Log

Build date: 2026-10-17. Environment: cloud Linux sandbox (Claude Code 2.1.302), ffmpeg 6.1.1, Python 3.13. After Effects, Blender, DaVinci Resolve: **not installed, not tested**. The user's Windows skills folder was **not accessible and was not modified**; this package is for manual installation.

## 1. Research status

| Source | Status |
|---|---|
| Every Frame a Painting - "How Does an Editor Think and Feel?" | Done: full transcript read. Other episodes: pending |
| StudioBinder - Murch / *In the Blink of an Eye* | Done: full transcript read; Murch's text via excerpts |
| Walter Murch - Dense Clarity / Womb Tone | Done: text excerpts read |
| Ben Marriott - Master Motion Design | Promo transcript + public syllabus read; paid lessons NOT accessed |
| Ben Marriott - After Effects in 60 Minutes (+10-minute excerpt) | Done: transcript read |
| Casey Faris - Introduction to DaVinci Resolve | Full transcript retrieved; selected sections read; remainder unread |
| Motion principles, Blender/AE pipeline, short-form data | Done: excerpts read; tiers recorded |
| Claude Code skills documentation | Read (first part: locations, frontmatter, listing limits, live reload) |

Details, URLs, and verdicts per source: `references/learning-sources.md`. A paper on first-3-seconds hooks was rejected because it describes its own dataset as synthetic.

## 2. Files created

See the tree in `README.md`. 24 files including this log: 1 `SKILL.md`, 9 reference files, 4 workflows, 3 worked examples + 1 example script, 1 brand overlay, 3 scripts.

## 3. Tests of the knowledge (scenario tests)

| Test | File | Outcome | What it changed in the skill |
|---|---|---|---|
| A: 10-s curiosity hook (Moon illusion) | `examples/hook-analysis.md` | Draft v1 failed the integrity gate (false premise), logo-first, flash cuts. v2 passed rubric with noted weak spots (even beat lengths) | Added the "misconception flip" hook pattern and its conditions |
| B: 30-45 s educational Reel (straw looks broken) | `examples/educational-reel.md` | v1 explained before demonstrating, had a needless formula and generic outro; v2 plan scored 2-3 everywhere; weakness: long 10-s diagram block, overlay-tracking risk | Added "evidence order" rule and two diagnosis rows |
| C: Cinematic sequence (light converging in a lens) | `examples/motion-graphics-sequence.md` | Rejected path-traced caustics for computed ray geometry; ran a real Snell's-law trace (`examples/lens_ray_check.py`): paraxial back focus ~96 mm; rays at 4/8/12/16/20 mm crossed at 95.8/95.3/94.3/93.0/91.2 mm (spherical aberration) -> graphic must state its simplification | Added the physics-QC procedure to `motion-design.md` |

These are planning exercises. **No video was rendered; no application was operated.**

## 4. Tests with the installed Claude Code (sandbox, project-scope copy)

The package was copied to a temporary project's `.claude/skills/` and Claude Code 2.1.302 was run non-interactively (`claude -p`).

| Run | Prompt type | Result |
|---|---|---|
| 1 | "Do you have a skill named ...? Quote its description." | Yes - description quoted verbatim (discovery works) |
| 2 | Matching request (35 s Reel feels slow, weak hook) | The `Skill` tool was invoked automatically; answer opened with "I can't watch the video" (capability honesty) |
| 3 | Unrelated request (reverse a string) | No skill invoked |
| 4 | Hook for Moon topic | Skill invoked, then it read the worked example for the same topic - proves routing, but is **contaminated** (the topic matched the example) |
| 5 | Hook for a *different* topic (fogging glasses), before an edit | Skill invoked; `hook-and-retention.md` read; capability check + contract stated. Output contained an unsupported exclusion ("it's not your breath") |
| 6 | Same prompt after adding the "exclusions are claims" rule and asking for a claim list | Skill invoked; returned a claims table with verified/not-verified status and **left the unsupported exclusions out** |

Caveats: one trial per prompt, model outputs vary, project scope rather than personal scope, and in a cloud container. This shows the mechanism works on this version; it does **not** prove it will fire on every matching request on your machine. Direct invocation (`/professional-video-editing-intelligence`) is the reliable fallback.

## 5. Script tests

Synthetic clip: six color segments (1.0, 1.0, 0.5, 0.5, 0.8, 3.0 s), tone-silence-tone audio, final segment black.

- `shot_rhythm.py`: at threshold 0.3 it found 4 of 5 cuts (missed the low-contrast green->yellow cut); at 0.1 it found all 5 and the correct durations. The script's output now warns about this. `--cuts` mode works without a video.
- `video_qc.py`: correctly reported 360x640, 30 fps, h264/aac; silence 2.5-4.5 s; black from 3.8 s; freeze from 3.8 s (to end of file); spec mismatch gave exit code 1; missing audio flagged; missing file gave exit code 2. A bug was found and fixed in the freeze/silence duration for events that run to end of file.
- `lens_ray_check.py`: ran for two parameter sets; paraxial result agrees with the thin-lens estimate within the stated approximation.
- `validate_package.py`: see section 6.

## 6. Package validation

Run: `python scripts/validate_package.py` (checks frontmatter, name rules, description length, local references, empty files, placeholders, secrets patterns, brand-name containment). Results for the final package are reported in the delivery message (they were run on the extracted ZIP, not only on the source folder).

## 7. Known limitations

- No video/audio was watched or heard; transcripts only.
- Paid Ben Marriott lessons not accessed; Faris transcript read selectively; EFAP only one episode.
- Numeric thresholds (reading budget, stagger times, safe-area margins, loudness target, 2-4 s change interval) are heuristics from secondary sources; they are labeled and must be verified.
- Short-form data are correlational.
- Behavior of After Effects/Blender/Resolve not tested here.
- Personal-scope discovery on the user's Windows machine not tested; the documentation says personal skills do not load in Cowork or cloud sessions.
- Brand overlay is assembled from the user's brief and synced profile skills in that session; project token files override it. A discrepancy about palette roles (navy first vs blue-grey primary) is flagged inside it and unresolved.
- The user's stated path `C:\Users\aaabb.claude\skills` appears to have lost a backslash; the README uses `C:\Users\aaabb\.claude\skills`.

## 8. Resume / next improvements

1. Read more Every Frame a Painting episodes and Murch's full book; add what they contradict or refine.
2. On the user's machine: install, run `/skills`, try three real briefs, note where Claude over-reads files or misses a rule, then tighten descriptions.
3. Test the AE/Blender commands against the installed versions; record results in `references/after-effects-and-blender.md`.
4. Add a short, verified table of current platform safe zones and loudness targets (with links and dates).
5. Build a small regression set: five briefs with expected decisions (e.g., "must refuse a false-premise hook") to rerun after edits.
6. Add a second brand overlay only when the user provides one.
