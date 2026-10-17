# Worked Example C - A Cinematic Motion-Graphics Sequence

**Brief (hypothetical):** "A 12-second cinematic opener for an optics explainer: light enters a lens and converges to a point; title appears. 16:9 master (3840x2160 target is optional; 1920x1080 fine), also needs a 9:16 recut. Tools: After Effects and Blender are installed on the editor's machine (not verified by Claude)."

Planning exercise only. The numerical lens check in this folder (`lens_ray_check.py`) was actually run; nothing else here was rendered.

## Step 1 - Translate "cinematic" into decisions

| Quality | Decision for this piece |
|---|---|
| Scale/depth | Slow dolly toward a glass lens with shallow depth of field; rays are the only bright elements |
| Light | One direction (left -> right), high contrast, dark background, rays as the hero light |
| Restraint | 3 elements: lens, rays, title. No particles, no lens flares unless justified |
| Sound | Designed bed + three accents + a long tail; silence before the convergence |
| Continuity | Rays always travel left -> right; lens geometry identical in every frame; same palette |

## Step 2 - Meaning and beats (animatic first)

Meaning: "Light bends and converges - order from a bundle of rays."

| Beat | Time | Lead element | Job | Camera |
|---|---|---|---|---|
| 1 Dark, then a single beam appears | 0.0-2.0 | One thin ray travelling right | Attention + curiosity | Static |
| 2 Beam widens into parallel rays | 2.0-4.5 | Ray bundle | Set up "many rays" | Slow push begins |
| 3 Rays meet the lens and bend | 4.5-7.5 | Lens + bending rays | Mechanism (information) | Push continues, focus on lens |
| 4 Rays converge to a point; silence | 7.5-9.0 | Focal point glow | **Peak** | Camera settles |
| 5 Title resolves over the converged point; hold | 9.0-12.0 | Title text | Landing | Static hold with imperceptible drift |

Shot-length curve: beats shorten into beat 3, peak at 4, release at 5. Animatic with scratch sound first; verify the curve before building.

## Step 3 - Build path decision

| Candidate | Verdict |
|---|---|
| Full Blender path-traced scene with a real light through a glass lens | **Rejected for the rays.** Light focused through glass forms caustics, which path tracers resolve slowly and noisily; physically correct yet unreliable to render. |
| **Computed ray geometry** in Blender (or AE) with a glass-looking lens | **Chosen.** Generate the ray paths numerically with Snell's law (see `lens_ray_check.py`), draw them as emissive curves; render the lens with glass look for depth/reflection only. Physical correctness comes from calculation. |
| Pure After Effects 2D | Viable fallback if 3D time is unavailable; loses depth and real perspective on the lens |

**Physics check actually run** (n=1.5, R=50 mm plano-convex, curved side toward light, t=6 mm): paraxial back focus ~96 mm behind the flat face; traced rays at heights 4/8/12/16/20 mm cross the axis at 95.8/95.3/94.3/93.0/91.2 mm. Conclusion for the graphic: a diagram where all rays meet exactly at one point is a **simplification**. Options: (a) show all rays meeting at the paraxial focus and call it an idealized "thin lens" model in narration, (b) show the small real spread (honest, subtle, makes the "peak" slightly softer) - **Decision: (a) with a one-line caveat in the video description**, because the audience is general; switch to (b) for an advanced audience.

## Step 4 - Production plan

**Blender (hero lens + rays):**
- Model the lens with real proportions; Glass BSDF with IOR ~1.5 (verify the chosen material); thin-surface artifacts checked.
- Generate ray curves from a script (`bpy`) using the traced coordinates; emission shader; animate a "growth" of each ray along its length (so light seems to travel).
- Camera: fixed lens (e.g., 50 mm equivalent), slow dolly; depth of field subtle.
- Render: **EXR multilayer** (beauty, emission/glare pass, depth) as an **image sequence**; film transparent for the beauty; a test of 2 s at final settings before the full render. Rays glow: render the glow additively (see PNG-alpha caution in `after-effects-and-blender.md`).

**After Effects (composite + title):**
- Import EXR sequence with correct color interpretation; add glow in AE if not baked.
- Title: type animates in with an ease-out reveal (mask), ~12-18 frames, placed where the focal point was; no letter-by-letter spray; hold >= 2 s.
- Grain + very subtle vignette to unify; no heavy gradients; palette per project/brand rules.
- Camera moves in 3D only if used; keep everything on one master camera.

**Sound (see `sound-design.md`):**
- Layers: room tone / low drone (bed), a soft rising tone as rays widen, a restrained "glass" tick on each ray's contact with the lens (one sound per rhythmic unit, staggered), a cut to near-silence before beat 4, a single clean tone on convergence, long tail through the title.
- Count: bed + tone + ticks = 3 layers; peak beat has 1-2.
- Not used: whooshes, impacts, music. (Music could be added as a final layer if the overall piece needs it.)

## Step 5 - Handoff and QC checklists

Blender -> AE handoff: fps/res/aspect match comp; alpha confirmed on bright and dark backgrounds; color space consistent; frames complete; one place decides motion blur.
Rubric table (target scores): Clarity 3, Rhythm 2-3, Continuity 3 (lens identical, light direction constant), Sound 3, Hierarchy 3 (only one lead at a time), Technical 2 (verify banding in dark gradients), Restraint 3, Integrity 3 (caveat about idealization).

## Step 6 - Weaknesses and decisions

| Weakness | Evidence | Decision |
|---|---|---|
| Dark scenes band after compression | Dark smooth gradients are prone to banding in H.264 | Add fine grain before encode; avoid soft dark gradient backdrops |
| 9:16 recut crops the wide composition | Aspect change | Compose with a center-weighted safe area; re-layout the lens vertically instead of cropping |
| 3D adds render time without adding understanding | The rays could be 2D | Keep 3D only for perspective/depth; fall back to 2D if time-boxed |
| Title competing with the glow | Hierarchy | Reduce the glow by ~30% at title time and ensure contrast on the real frame |
| Idealized convergence | Numerical check | Caveat in description; option (b) for advanced audience |

## Alternatives considered (explicit)

| Choice | Chosen | Alternative | Why |
|---|---|---|---|
| Rays | Computed geometry | Rendered light + caustics | Reliability + physical control |
| Transition into title | Convergence point becomes title location | Cut to black then title | Same object carries both scenes (motivated) |
| Camera | Slow dolly | Orbit around lens | Dolly keeps left-right light direction constant |
| Sound | Designed sound, no music | Music-driven | Sound carries the physical event; music can be added if the whole video needs it |

## What this test taught the skill

- A physics-sensitive animation needs a **numerical check** step, not just a visual check: the skill gained the "physics QC" lists in `motion-design.md` (section 7) and this worked check.
- "Cinematic" must be translated into explicit decisions (scale, light, restraint, sound, continuity): the workflow file now begins with that table.
