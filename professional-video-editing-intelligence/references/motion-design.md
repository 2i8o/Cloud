# Motion Design Principles

Tags: **[BM-syl]** Ben Marriott *Master Motion Design* course page (syllabus text only; lessons are paywalled and were **not** accessed). **[BM-vid]** Ben Marriott free videos (transcripts read: 60-minute After Effects fundamentals; 10-minute fundamentals excerpt). **[Adobe]** Adobe Blog interview with Issara Willenskomer and Adobe's principles page. **[Tuts+]** Envato Tuts+ "Principles of Motion Design". **[Heur]** practitioner heuristic (a third-party motion-craft guide; its numbers are one project's taste, not standards). **[Synth]** this skill's reasoning.

## 1. The purpose test

Motion exists to do one of four jobs: **direct attention**, **show cause and effect / process**, **create continuity between states**, or **carry emotion/tone**. Anything else is decoration.

Gate for every animation: *Which job? What does the viewer understand or feel differently with it than without it?* Remove it once; if nothing is lost, it stays removed. [Synth]

## 2. Easing is the one universal principle

- "You want all motion to always ease. When you don't ease it, it looks artificial and doesn't feel natural, so that's one of the animation principles that carries over." (Willenskomer) [Adobe]
- Real objects accelerate and decelerate; easing (After Effects "Easy Ease", F9) is the first fix for stiff motion. Linear motion has narrow uses (opacity under ~150 ms, loops, rotation, tickers). [BM-vid, Heur]
- Choose easing by event: **entrances** ease out (fast start, long settle); **exits** ease in and are 20-30% shorter than the entrance; **moves between two rest positions** ease in-out. [Heur]
- Refine with the speed/value graph: steeper = faster. [Tuts+]

## 3. How much of the "12 principles" actually transfers

Willenskomer argues that most of the Disney principles were built for physical characters and do not all transfer to interface/graphic motion; he singles out easing as universal and notes "staging" in UX terms is just layout. [Adobe] A practitioner reference ranks screen-motion priorities as: slow-in/slow-out, timing, follow-through/overlap, anticipation, staging, arcs, with squash/stretch, exaggeration and secondary action as brand-dependent. [Heur] Ben Marriott's advanced course opens with the 12 principles, "focusing in detail on anticipation and overlapping action" (syllabus). [BM-syl]

**Use as a toolbox, ranked by payoff** [Synth from the above]:
1. Easing 2. Timing (weight/mood: fast = light/urgent, slow = heavy/calm) 3. Overlap / follow-through (parts don't stop at once) 4. Anticipation (a small counter-move telegraphs an action) 5. Staging (one thing leads; dim/de-emphasize the rest) 6. Arcs (natural paths curve)
Add squash/stretch, exaggeration, secondary action only when tone calls for it.

## 4. Timing and hierarchy

"Timing is essentially like hierarchy, but in the fourth dimension": time changes what the viewer reads first. Block key moments first (storyboard/blocking), then refine between them. [Tuts+] Marriott's syllabus likewise has a week on "professional process and workflow... blocking animation, animating with arcs." [BM-syl]

**Procedure**
1. Write the beats in order of importance.
2. Block: key poses/positions at correct times, no easing.
3. Add easing, then adjust timing by feel.
4. Offset related elements (delay layers a few frames) to create flow - Marriott's "offset" is delaying motion to create a rhythmic fill. [BM-vid]
5. Add overlap/follow-through only after the base motion reads.
6. Remove anything that competes with the lead element.

**Stagger/offset starting points** [Heur]: letters 15-25 ms, words 30-60 ms, list items 60-100 ms; keep a group's total under ~0.4-0.5 s; over ~9 items use one wipe instead of a staircase. Lead with the most important element.

## 5. Hold, then move

After an element lands, hold at least ~0.5 s (short-form) before the next change; hold 1.5-2.5 s for anything that must be read or understood. [Heur] A hold longer than ~2 s with no motion can read as frozen - add a very slow drift (a few % scale over the hold) or restructure. A text-only scene past ~2.5 s needs some motion. [Heur]

## 6. Typography and visual hierarchy

- One thing dominates the frame (an "eye-catcher"); group related items; repeat styles for recognition; asymmetry creates tension. [Fecher, Motion Graphics Design Academy ebook excerpt - secondary]
- Headline >= ~7% of frame height; body minimum ~36 px at 1080p landscape / ~48 px at 1080x1920. [Heur]
- Two families at most, with strong contrast in weight; tight display tracking. [Heur]
- One idea per card, ~1-6 words. [Heur]
- Emphasis by weight, color, or scale - one at a time. Avoid text shake, wiggle, rainbow. [Heur]
- Safe areas: platform UI covers parts of a vertical frame. **Use the project's template or current platform spec.** Conservative default for 1080x1920 when none is available [Guess, verify]: keep essential text and faces at least ~250 px from the top, ~420 px from the bottom, ~64 px from the sides.
- Arabic and other RTL scripts: set direction explicitly, check letter joining, numerals, punctuation placement, and diacritics in the actual render; do not apply Latin reading-time numbers unchanged.
- Always check contrast on the real background after grading.

## 7. Visual metaphors and scientific graphics

A metaphor is legitimate only if its **structure** matches the idea:
- Which properties of the metaphor map to the real system, and which do not? State the limit on screen or in narration if the mismatch could mislead.
- A metaphor is not evidence. Pair it with real footage, measurement, or a correct diagram.
- **Physical correctness beats beauty** for educational diagrams: ray paths obey the law they illustrate (e.g. refraction bends toward the normal entering a denser medium), anatomy proportions are accurate, motion directions are consistent. A wrong-but-pretty graphic fails the integrity gate.
- Reveal in **causal order**: cause object -> mechanism -> effect.
- **Physics QC procedure:** (1) list every physical relationship the graphic asserts (ray direction, bend direction, positions, proportions); (2) check each against the governing law or a numerical trace - `examples/lens_ray_check.py` shows a Snell's-law trace that reproduces the lens-focus behaviour; (3) decide explicitly whether a simplification is acceptable for the audience and say so on screen, in narration, or in the description; (4) re-check in the final render.
- One metaphor per beat; never layer two.
- Preserve the geometry and identity of depicted objects across shots (same lens, same frame, same scale).

## 8. 2D camera and scale

Scale change < ~5% reads as static, 10-15% comfortable, > ~30% dramatic. [Heur] Don't apply the same ambient zoom to every scene; stillness after motion is powerful.

## 9. Flashing and accessibility

Avoid more than three flashes per second and large high-contrast flashing areas (common photosensitivity guidance, also applied to signage and video). [Heur] If a strobe effect is required, keep area small and brief, and tell the user.

## 10. Cheap-looking tells -> fixes [Heur]

| Tell | Fix |
|---|---|
| Overshoot/bounce on everything | Ease-out; overshoot once on one hero element |
| Everything enters at t=0 | Lead with the hero, stagger the rest in importance order |
| Every item enters from y+30 with a fade | Vary technique by group; use masks/wipes where it clarifies |
| Endless "breathing" loops | One subtle ambient motion per scene, or none |
| A different transition every cut | One primary + 1-2 accents |
| Heavy full-screen gradients (banding) | Flat fills or subtle noise/grain; follow brand rules |
| Linear moves | Ease every spatial move |
| Strobing fast snap | Add motion blur only on the fast frames |

## 11. Motion-graphics sequence workflow

See `workflows/cinematic-motion-graphics.md`. Software details: `after-effects-and-blender.md`.
