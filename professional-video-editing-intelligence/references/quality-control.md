# Quality Control and Review Framework

Use for self-review before delivering a plan, and for critiquing an existing edit. Procedure: `workflows/editing-review.md`.

## 1. Scored rubric (0-3 per dimension)

0 = broken / absent, 1 = weak, 2 = solid, 3 = exemplary. Cite *evidence* (timestamp, frame, measurement) for any score <= 1.

| Dimension | Passes when | Typical failures |
|---|---|---|
| **A. Narrative clarity** | A first-time viewer can say what the video asks and what it answers; hook promise = payoff scope | Hook/payoff mismatch; unclear subject; missing setup; open loops left open |
| **B. Emotional progression** | Intended emotion builds, peaks, and releases; payoff gets time | Flat; payoff buried; emotions stacked without holds |
| **C. Rhythm** | Shot/beat lengths vary purposefully with a build/peak/release; cuts at thought/action/beat | Uniform lengths; cuts mid-thought; rushing the key beat |
| **D. Continuity** | Eye-trace, direction, object identity, ambience consistent | Direction flips; changing object geometry; ambience jumps |
| **E. Sound** | Every sound has a job; <= ~5 layers; VO intelligible; silence used on purpose | Whoosh spam; music over VO; clipping; dead air |
| **F. Visual hierarchy** | One lead element at a time; text readable within safe areas; motion directs attention | Competing animations; tiny text; clutter |
| **G. Technical execution** | Spec-correct (res/fps/loudness), no artifacts, alpha/edges clean, color consistent | Banding; aliasing; wrong fps; low-bitrate smearing |
| **H. Restraint / complexity** | Nothing can be removed without loss | Effects stacked "to look pro"; redundant overlays |
| **I. Integrity** (factual content) | Claims sourced at correct scope; graphics physically/anatomically correct; no bait-and-switch | Over-claiming; misleading graphic; fear framing |

**Gate rules (override the total):** any 0 in A, I, or G fails the edit. Any claim without a source in factual content blocks release until sourced or removed.

## 2. Diagnosis: symptom -> check -> fix

| Symptom | First check | Fix |
|---|---|---|
| "Boring" | Where does retention/attention drop? Is there information per beat? | Increase information per beat or cut redundancy; add a new question at the dip |
| "Confusing" | Missing orientation? Pronoun-like visuals (what is "this")? | Add establishing frame; label; re-order causal steps |
| "Too busy" | Count simultaneous moving elements; layers of sound | Lead + support only; remove an element each pass |
| "Cheap" | Linear motion, stock overshoot, gradient banding, sync misses | Ease, align to sound beat, flatten gradients, simplify |
| "Slow" | Beat longer than the idea needs | Trim to thought boundary; overlap audio |
| "Rushed" | Payoff followed immediately by next point | Hold; separate beats |
| "Hook doesn't land" | Can the question be stated after 3 s? | Make the visual question explicit; restate in text |
| "Explanation doesn't stick" | Does the explanation come before the viewer has seen the thing explained? | Show the phenomenon first (or alongside); lock the graphic to the real object |
| "Long middle sags" | Is one block >~8 s carrying most of the information? | Split into 3 sub-beats; move a highlight/camera along the causal chain |
| "Inconsistent" | Palette/fonts/easing differ between sections | Consolidate to one style sheet |
| "Fake-looking 3D/AI object" | Geometry, scale, shadow, reflection continuity | Reference sheet; regenerate/rebuild; add contact shadow |

## 3. Technical QC checklist

- [ ] Resolution, frame rate, aspect ratio, duration match the spec (`scripts/video_qc.py`)
- [ ] Loudness measured (integrated + true peak); dialogue intelligible on phone speaker
- [ ] No unintended black frames, freezes, silence gaps (script flags candidates; human confirms)
- [ ] No clipping / distortion; no abrupt ambience changes
- [ ] Text and faces inside safe areas of every platform UI overlay
- [ ] Text contrast and size verified on a phone-sized preview
- [ ] Captions synced and correct (spelling, direction, punctuation)
- [ ] Color consistent across cuts; skin/neutrals plausible; grade applied once
- [ ] Alpha edges clean over light and dark backgrounds (for overlays)
- [ ] Compression artifacts acceptable (gradients, fine text) at final bitrate
- [ ] Flash/strobe safety (<= 3 flashes per second) checked
- [ ] File naming/versioning; originals untouched; project archived

## 4. Content integrity checklist (educational / health-adjacent)

- [ ] Each factual claim has a named source with matching scope (population, condition, strength)
- [ ] Statements that dismiss an alternative ("it's not X") are sourced like positive claims
- [ ] Evidence vs. speculation is distinguished on screen or in narration
- [ ] No fear-based framing beyond the evidence; no diagnosis implied
- [ ] Graphics follow the relevant physics/anatomy (ray paths, proportions, directions)
- [ ] Hook promise equals delivered payoff
- [ ] Numbers, units, and labels re-checked in the final render, not just the script

## 5. Review output format

```
VERDICT: <ship / revise / rebuild> - one sentence
EVIDENCE ACCESSED: <what Claude actually inspected: script/transcript/frames/metrics - never "watched">
SCORES: A..I table with evidence for <=1
TOP 3 FIXES (highest impact first), each with: problem -> why it matters -> exact change -> alternative
WHAT TO REMOVE: list
CONFIDENCE: Established / Heuristic / Guess per major claim
```

## 6. Restraint pass (always last)

Remove each non-essential element once: overlay, transition, sound layer, camera move, text line. Re-watch. Anything whose removal is not noticed stays out.
