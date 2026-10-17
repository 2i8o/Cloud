# Workflow: Reviewing and Improving an Existing Edit

Purpose: diagnose why an edit is weak and deliver the smallest set of changes that fixes it. Always start from **what evidence you can actually access**.

## Step 1 - Inventory the evidence (be exact about it)

| You have | What you can legitimately conclude |
|---|---|
| Script / transcript / voice-over text | Narrative structure, hook-payoff contract, claim integrity, word-level pacing |
| Shot list / EDL / XML / timeline export | Shot lengths, transitions used, track/layer counts, structure |
| A video file | Technical specs, loudness, silence/black/freeze candidates (`scripts/video_qc.py`), cut times and shot-length curve (`scripts/shot_rhythm.py`), extracted frames (use ffmpeg to dump frames at the cut points and view them) |
| Extracted frames | Composition, hierarchy, text legibility, continuity of objects, graphic accuracy |
| Nothing but the user's description | Hypotheses only - ask for the script or an export |

**Never say "I watched the video" or "I heard the mix."** Say "from the extracted frames at cut points 1-12 and the loudness measurement ..." Name what each conclusion rests on.

Frame extraction example: `ffmpeg -i in.mp4 -vf "fps=2,scale=360:-1" frames/f_%03d.jpg` (then read selected frames).

## Step 2 - State intent

Ask or infer: audience, the intended single takeaway, platform, target emotion. Review against *their* intent, not generic taste.

## Step 3 - Run the passes in this order (high-level first; polishing never fixes structure)

1. **Contract pass:** hook question vs payoff scope. Are there open loops left open?
2. **Clarity pass:** can each beat be summarized in one line? Where is information missing or redundant?
3. **Emotion/rhythm pass:** shot-length curve, holds after payoff, cut placement (thought/action/beat).
4. **Continuity pass:** direction, object identity, eye-trace, ambience.
5. **Sound pass:** layers per 5 s, ducking, silence use, sync.
6. **Graphics pass:** purpose of each element, hierarchy, easing, safe areas, accuracy.
7. **Technical pass:** `video_qc.py` + checklist.
8. **Restraint pass:** what can be removed.

## Step 4 - Score and diagnose

Use the rubric in `quality-control.md` (A-I, 0-3). Cite evidence for every score <= 1. Apply the symptom -> fix table. Rank problems by **impact on the viewer**, using the priority ladder (emotion/meaning > clarity > rhythm > ...). Don't offer ten notes; offer the highest-impact three, then the rest briefly.

## Step 5 - Propose fixes as decisions

For each fix: **problem -> why it matters (which ladder level) -> exact change (timestamp, element) -> alternative if the creator disagrees -> risk**. Where the choice is subjective, give two defensible options and recommend one.

If the user asks for implementation: produce an explicit edit list (cut X, trim Y by N frames, move sound Z), never altering the spoken words or original media; export a new version.

## Step 6 - Verify the change

Re-run the same measurements on the new export. State which issues are resolved and which remain; do not claim improvement that was not measured or inspected.

## Output template

```
VERDICT: <one sentence>
EVIDENCE ACCESSED: <exact list>
LADDER LEVEL OF MAIN PROBLEM: <emotion / clarity / rhythm / ...>
SCORES: A..I  (evidence for <=1)
TOP 3 FIXES: ...
OTHER NOTES: ...
REMOVE: ...
CONFIDENCE: Established / Heuristic / Guess per claim
NEXT MEASUREMENT: <what to run after the fix>
```

## Anti-patterns for reviewers

- Praising before diagnosing; generic notes ("make it punchier"); recommending more effects as the fix; fixing the loudest symptom instead of the root cause; treating a platform heuristic as law; reviewing taste without the creator's intent.
