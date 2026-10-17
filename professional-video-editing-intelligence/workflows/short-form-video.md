# Workflow: Short-Form Vertical Video (Reel / Short / TikTok, ~15-60 s)

Defaults to verify per project: 9:16, 1080x1920, 30 fps (or the project's fps), burned-in captions inside safe areas, mobile viewing in noisy places (sound often off or low).

## Step 1 - Contract (30 seconds of thinking)

- **Question** (hook) in one sentence.
- **Answer** (payoff) in one sentence at the same scope.
- **Evidence** the viewer can *see*.
- **Takeaway** in one line.
If the honest answer is nuanced, make the question about the nuance.

## Step 2 - Duration budget (starting allocations [Synth]; adapt)

| Total | Hook | Context/stakes | Evidence (2-4 beats) | Payoff + hold | Landing |
|---|---|---|---|---|---|
| 15 s | 0-2 s | 2-4 s | 4-11 s | 11-14 s | 14-15 s |
| 30 s | 0-3 s | 3-8 s | 8-24 s | 24-28 s | 28-30 s |
| 45 s | 0-3 s | 3-10 s | 10-36 s | 36-42 s | 42-45 s |

Rules of thumb: one new idea per 4-8 s; at most 3 evidence beats in 30 s; payoff gets a hold (>= 1 s of no new idea).

## Step 3 - Visual plan

For every beat, choose exactly one: **real footage**, **graphic explanation**, **text-forward card**, **3D hero**. Mix them only for contrast. Every visual has a job: illustrate / evidence / metaphor. If a beat has no visual of its own, it probably belongs inside the previous or next beat.

**Evidence order:** show the phenomenon (or the proof) *before or while* explaining it. An explanation that arrives before the viewer has seen the thing it explains has no anchor. Where a graphic explains a real object, show the real object first and lock the graphic to it.

## Step 4 - Cut plan

- Cut at thought boundaries; J/L cut on speech; no pause longer than needed.
- Build -> peak -> release across shot lengths; let the payoff shot be longer than the shots before it.
- Direct cuts by default; at most one signature transition.
- Text: 1-6 words per card, large; headline hold >= 1.0 s (`pacing` section 3); keep inside safe areas.
- Mute test and audio-only test on the plan.

## Step 5 - Sound plan

Voice first. Ambience bed under everything. One sync'd accent per key visual event. Music only if it adds energy without competing with voice; it ducks under voice. Place one beat of near-silence immediately before the payoff.

## Step 6 - QC and delivery

Run `scripts/video_qc.py final.mp4 --expect-width 1080 --expect-height 1920 --expect-fps 30` (change if the project differs). Check captions on a phone-sized preview. Verify every on-screen fact against its source.

## Failure modes -> fixes

| Failure | Fix |
|---|---|
| Hook is a topic label | Turn into an image + question |
| Evidence beats are all talking head | Replace one with a graphic or demonstration |
| Payoff arrives, then immediately another claim | Insert a hold; move the extra claim out |
| Over-captioned (every word animates) | Highlight key words only |
| Ending: "follow for more" | End on the takeaway or callback to the first frame |
| Too many ideas for the duration | Split into a series; keep one question per video |

## Template: Decision Ledger (short-form)

| Time | Element | Job | Why now | Alternative | Risk |
|---|---|---|---|---|---|
| 0.0-2.5 | ... | ... | ... | ... | ... |

Worked example: `examples/educational-reel.md`. Hook example: `examples/hook-analysis.md`.
