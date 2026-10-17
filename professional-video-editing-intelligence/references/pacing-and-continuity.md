# Pacing, Rhythm, and Continuity

Tags as in `storytelling-and-editing.md`. New: **[Study-weak]** peer-unreviewed or small-sample evidence; **[Obs]** observational/correlational data.

## 1. Rhythm is the story's tempo, not the cut count

"There's an in-built relationship between the story itself, how to tell a story, and the rhythm with which you tell it, and editing is... 70% about rhythm." (Murch, quoted in [EFAP]). Every shot has "a natural rhythm"; timing "is not a conscious process, you're just responding" to it. [EFAP] Rhythm can be obvious (physical action) or subtle (people walking, a restaurant's bustle), and the subtle kind is harder to edit. [EFAP]

**Consequence:** "fast = engaging" is not a law. Evidence on pace:
- A small controlled experiment (N=242, a single 20-second talking-head clip) found higher pacing *reduced* sustained engagement overall, and seamless cuts raised liking while overlapping cuts raised completion at low pace. [Study-weak: conference paper, one clip, not generalizable]
- An observational sample of 1,272 TikToks/Reels found 10-25 cuts/min at 1.53x typical views versus single-take at 0.69x. [Obs: business/creator accounts; correlation; sample over-represents best/worst videos per the authors]
- Reading together: avoid both extremes; vary cadence, and match it to the goal (watch-through vs. likes). Do not cite either as proof.

## 2. The shot-length curve

From [EFAP]'s analysis of *Empire Strikes Back*: shots get shorter into the peak, then longer after it; the release outlasts the build.

```
shot length
 ^ long            ____                         ________
 |      \         /                            /
 |       \_ _ _  /     <- build: shorter       /  <- release: longer, held
 |              \/   peak                    /
 +------------------------------------------------> time
```

**Procedure** [Synth]
1. List shot durations in order (use `scripts/shot_rhythm.py` on an existing cut).
2. Mark the intended peak (reveal / payoff). Durations should trend down toward it and up after it.
3. Flat, uniform durations = monotone rhythm. Break with one deliberate long hold and one deliberate quick run.
4. Equal-length beats of equal weight read as mechanical; vary by at least ~25% unless the form is intentionally metronomic (music-synced montage).

## 3. Information-density budget

[Synth] Rhythm for explainers is driven by comprehension, not mood.
- One new idea per beat. A beat ends when that idea is understood.
- New on-screen element -> give it a hold equal to its reading/recognition time before the next change.
- Text reading budget heuristic: about 3 words/second, hold >= max(1.0 s, 0.5 s + characters/13). [Heur: third-party motion-craft guide]. **Calibrate with a read-aloud test** - script and typeface change this, and Arabic (with diacritics/connected script) is not covered by the heuristic.
- "Something changes every 2-4 s in short-form" is a practitioner heuristic. [Heur] Interpret "change" as a new *information state* (new visual, new question, new number, new camera framing), not necessarily a cut. A designed hold on the key message is not dead air.

## 4. Cut-point selection

| Situation | Cut at | Why |
|---|---|---|
| Speech | end of a complete thought, or just before the next thought's first word | Blink = thought completion [SB] |
| Action | mid-action (cutting on action) | The movement hides the join |
| Reaction | when the eyes change / decision is visible | [EFAP] |
| Reveal | after the setup is understood, before attention drifts | Anticipation |
| Silence/hold | after the feeling has been felt, not before | Emotions take time [EFAP] |
| Graphic explanation | when the next object is needed | Information-driven |

**Overlap (J/L) cuts:** audio arrives before (J) or lingers after (L) the picture change; softens the join and carries story across the cut. Default tool for talking-head and dialogue-driven edits. See `sound-design.md` section 5.

## 5. Choosing a transition (decision tree)

1. Is there a time/space jump the viewer must register? **No** -> direct cut. (Stop here for most cuts.)
2. Is there a *visual relationship* between outgoing and incoming frames (shape, motion direction, color, subject position)? **Yes** -> match cut / graphic match / whip with matched motion.
3. Is the jump a deliberate break (chapter, topic change, time skip)? **Yes** -> one consistent, short device (dip, wipe, title card). Reuse the same one so it reads as grammar.
4. Is motion graphics *content* itself the transition (an object becomes the next scene)? Only if the object means something in both scenes.
5. Else -> direct cut. Dissolves/glitches/swooshes used because "a cut feels bare" are decoration.

Rule: pick one primary transition for the piece plus at most 1-2 accents. [Heur: "a different transition every cut" is a recognized cheap tell]

## 6. Continuity checklist (apply per cut)

- **Eye-trace:** where is the viewer looking at the end of shot A? Put the key subject of shot B near that region, or use motion to lead. [SB, Murch]
- **Screen direction (axis/180°):** keep direction of travel consistent across the cut. For optics diagrams: **light travels in one fixed direction (usually left->right) across every cut and graphic**; reversing it without reason reads as a physics change.
- **30° rule:** when cutting between two shots of the same subject, change angle by about 30° or more (or change shot size markedly), else it feels like a jump cut. [SB]
- **Match cuts:** on action, on shape, on color, on concept. Murch's fan-to-helicopter is the standard example. [Video&Filmmaker summary of Murch]
- **Object identity:** the same object keeps the same geometry, scale, material, and position unless the story changes it. Critical for 3D and AI-generated imagery (see `quality-control.md`).
- **Jump cuts:** acceptable when the jump is the style (talking-head tightening) or serves urgency; avoid within a single continuous visual demonstration unless the jump is hidden by an insert.
- **Sound continuity:** room tone and ambience continue across a cut unless the scene changes; abrupt ambience change is a continuity break.

## 7. Tension and release

- Anticipation: a beat of stillness, silence, or a small counter-move before a payoff makes the payoff feel larger. [Synth + Adobe animation-principle for motion]
- Repetition sets an expectation; a variation pays it off. Establish a pattern (3 similar beats), then break it on the beat that matters.
- Parallel action (cross-cutting) raises stakes by contrast; keep point-of-view clear. (*Dunkirk* analysis cited in secondary sources.)
- Peak-end: viewers weigh the most intense moment and the ending when evaluating experiences. The 2025 RecSys paper applies this to retention modelling on a short-video platform; evidence for viewers' memory comes from the peak-end literature, not the paper's A/B test. [Indirect] -> make one clear peak and end on it, not on a weak outro.

## 8. Common mistakes -> corrections

| Symptom | Likely cause | Fix |
|---|---|---|
| "Feels rushed" | Beats shorter than comprehension time | Lengthen the hold after the key beat; cut a redundant beat instead of compressing all |
| "Feels slow" | Beats longer than information density | Trim heads/tails to the thought boundary; overlap audio; remove restatement |
| "Feels random" | Cuts not tied to thought/action/beat | Re-place cuts on thought completion; add a connective visual relationship |
| "Feels monotone" | Uniform shot lengths | Introduce build/peak/release; one deliberate long hold |
| "Confusing" | Missing orientation shot / axis flip / identity change | Add establishing frame; fix direction; stabilise object geometry |
| "Glitchy but not exciting" | Effect transitions on every cut | Return to direct cuts; keep one signature transition |
