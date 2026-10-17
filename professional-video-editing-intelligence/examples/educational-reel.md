# Worked Example B - A 30-45 Second Educational Reel

**Brief (hypothetical):** "A ~40 s vertical Reel for a general audience: why a straw in a glass of water looks broken. Optics-education channel, so the physics must be right. Real footage of a glass and straw is available; I can also animate a diagram."

Planning exercise only; nothing was rendered. Brand overlay for an optics-education channel is described in `brand/abbas-abdulmunem.md`; the plan below is brand-neutral except where marked **[brand]**.

## Step 1 - Contract

- **Question:** "Why does a straw look broken in water?"
- **Answer (scope):** Light bends (refracts) when it passes from water to air; your brain assumes light travels in straight lines, so the submerged part appears shifted. The straw is not bent.
- **Physics I rely on:** refraction at the water-air boundary (n water ~1.33, air ~1.00) - **Established**. Apparent-depth relation (near-normal viewing): apparent depth ~ real depth / 1.33 - **Established** (paraxial approximation; label as "approximately"). A round glass also acts as a lens and magnifies/distorts sideways - **Established**; mention only if it helps, because it adds a second effect.
- **Do not claim:** "the straw is bending", "your eyes are fooled" (the brain's inference is an interpretation - phrase as "the light bends, and the picture your brain builds assumes straight paths").
- **Takeaway:** "Next time, look from above and watch the break change."

## Step 2 - Draft v1 and its problems

v1 beats (40 s): (1) title card "Optical illusion!" 3 s -> (2) talking head defining refraction 8 s -> (3) animated rays diagram 10 s -> (4) real glass shot 6 s -> (5) formula n1 sin... 6 s -> (6) "follow for more" 4 s.

| Problem | Ladder level | Evidence from the framework |
|---|---|---|
| Hook is a label ("Optical illusion!") with no question | Clarity/hook | Curiosity test fails |
| Real demonstration comes **after** the explanation | Story | The evidence should precede or accompany the claim |
| Diagram shows rays but not what the *eye* infers | Clarity/accuracy | Without the straight-back-extended line, "why it looks broken" is unexplained |
| A formula appears without being needed | Restraint | Removal test: nothing lost for this audience |
| Generic outro | Landing | Weak ending |
| Duration use: payoff has no hold | Emotion | Next claim stacks on the aha |

## Step 3 - Draft v2: shot plan with timing (30 fps)

| Time | Visual (job) | Sound | On-screen text | Why now |
|---|---|---|---|---|
| 0.0-3.0 | Real shot: straw standing in a clear glass, **broken at the surface**, slow push-in. Pour water in so the break *appears* (evidence + visual question) | Room tone; the pour; no music | "Why does the straw look broken?" (2 lines max) | Question and the phenomenon in the first frames; the pour makes it live, not a still |
| 3.0-7.0 | Hand lifts the straw out: it is straight. Back in: broken again | VO: "It isn't bent. Look." Ambience, one light water sound | none | Direct disproof of the misconception; short, tactile |
| 7.0-10.0 | Cut to side view; camera moves to look through the glass from above; the break changes | VO continues; ambience | "Change the angle - the break changes." | Sets up that the effect depends on viewpoint (a prediction the diagram must explain) |
| 10.0-20.0 | Animated cross-section diagram (water, air, straw tip). Ray leaves the submerged point, **bends at the surface**, reaches the eye; a dotted straight line extends back from the eye and lands at a shallower point. The tip label moves from "real" to "seen" | VO explains; soft tick at each ray segment landing; no whooshes | Short labels: "water", "air", "real", "seen" | The causal chain in the order it happens: source -> bend -> eye -> brain's straight-line assumption |
| 20.0-26.0 | Hold on the finished diagram with a clean ray path; **VO silent for ~1 s** | Near-silence, ambience | Key phrase: "Light bends. Your brain assumes straight." | The payoff gets a hold |
| 26.0-34.0 | Real footage again with a **diagram overlay** locked to the glass edge: the overlay's "seen" point matches where the straw appears broken | One soft tick on lock | none | Evidence ties the model to the real thing |
| 34.0-40.0 | Callback: the broken straw; hand removes water or tilts; VO: "Try it from above. Watch the break move." Fade audio under the last line | Ambience | Takeaway line, large | Landing + action the viewer can repeat |

Layers per 5 s: voice, ambience, one accent = 3. Within the budget.

## Step 4 - Alternatives considered

| Decision | Option A (chosen) | Option B | Why A |
|---|---|---|---|
| Opening | Live pour reveals the break | Static broken-straw image | A makes the effect arrive visibly; the question forms during the pour |
| Explanation | One animated cross-section | Real-time ray-tracing 3D render | Simpler, readable at phone size, more accurate to control |
| Formula | Omit | Show Snell's law | Fails restraint test for the stated audience; offer as a follow-up |
| Camera | Static for the diagram | Slow push on diagram | Static keeps attention on the rays; the live shots carry the camera moves |

## Step 5 - Physics/geometry QC (must pass before animating)

- Ray bends **away from the normal** when it exits water into air (water is the denser medium) - the exiting ray in the diagram must show this.
- The "seen" point lies on the straight extension of the *exiting* ray, back from the eye, and is shallower than the real point.
- Water level line is horizontal and continuous across diagram and overlay.
- Straw geometry in the diagram is the same straw in the footage (diameter, angle).
- The direction of light flow is consistent (source -> eye) in every ray graphic.

## Step 6 - Review against the rubric (v2)

| Dim | Score | Evidence / notes |
|---|---|---|
| A Clarity | 3 | Question 0-3 s; disproof 3-7 s; mechanism 10-20 s |
| B Emotion | 2 | Curiosity -> surprise (straight when lifted) -> understanding; hold at 20-26 |
| C Rhythm | 2 | Beats 3.0/4.0/3.0/10.0/6.0/8.0/6.0 s: the 10-s diagram is the longest block - risk of a flat middle (see weaknesses) |
| D Continuity | 3 | Same straw/glass across footage and overlay; consistent light direction |
| E Sound | 3 | 3 layers; silence at the payoff; no whooshes |
| F Hierarchy | 2 | Verify text sizes and safe areas in the real template |
| G Technical | 2 | Overlay lock needs tracking; confirm alpha edges, fps, loudness |
| H Restraint | 3 | No formula, no decorative effects |
| I Integrity | 3 | Claims limited to refraction and apparent depth; "approximately" used |

## Weaknesses and revisions

1. **The 10-s diagram block is the longest and carries the most information.** Revision: break it into three sub-beats with the camera or highlight moving along the ray (source -> surface -> eye) at ~3 s each, so something new appears every ~3 s without adding decoration.
2. The overlay lock in 26-34 s is the riskiest production step (tracking drift). Fallback: use a **side-by-side** (real | diagram) instead of an overlay.
3. Round-glass distortion can contradict a flat-surface diagram. Mitigation: film in a flat-sided container or acknowledge the glass effect in one line.
4. Reading load: the labels are small words; keep them single-line and hold >= 1 s each.

## **[brand]** overlay (only if the content is for the optics-education channel)

Apply the palette/typography/safe-area rules from `brand/abbas-abdulmunem.md` and the project's own token files; keep gradients minimal; keep faces uncovered if a presenter is on screen; verify any Arabic text direction and joining in the render; do not change the presenter's spoken words.

## What this test taught the skill

- Plans that explain **after** showing the phenomenon are weaker: the skill now says in `short-form-video.md` step 3 that evidence should precede or accompany the claim (existing "Evidence" beat) and the review table flags "explanation before demonstration."
- The physics QC list is reusable for any optics diagram: see `motion-graphics-sequence.md` and `lens_ray_check.py` for a numerical check.
