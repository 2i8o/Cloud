# Workflow: Cinematic Motion-Graphics Sequence

"Cinematic" is not an instruction. Translate it into decisions: **scale and depth** (camera, parallax, focus), **light** (one motivated direction, contrast), **restraint** (few elements, slow confident motion, holds), **sound** (designed layers, silence), and **continuity** (one visual language). Define which of these the brief means before starting.

## Phase 1 - Intent (before any software)

1. One-sentence meaning: what should the viewer understand or feel at the end?
2. Role of the sequence: opener, explainer segment, transition, title, climax?
3. Constraints: duration, fps, resolution, safe areas, palette/typography rules, loudness.
4. Reference language: 2-3 references (not to copy; to name qualities: pacing, contrast, camera behavior).

## Phase 2 - Beat sheet and animatic

- Beat sheet: 3-6 beats; each with job, duration, and the single lead element.
- **Animatic**: static boards timed to a temp sound track (VO scratch, rhythm track). Check shot-length curve (build/peak/release) here, where changes are cheap.
**Exit test:** the animatic communicates the idea with ugly graphics; the peak beat is identified; total time fits.

## Phase 3 - Style frames

Create 2-4 key frames at final resolution: composition, hierarchy, color, type, lighting. Validate readability on a phone-sized preview and within safe areas.
**Exit test:** a viewer can identify the lead element in each frame within a second.

## Phase 4 - Choose the build path (decision)

| If the sequence needs... | Then |
|---|---|
| Type, shapes, UI/infographic motion, masks | After Effects only |
| Parallax and depth without true 3D | After Effects 2.5D with camera |
| Physically correct glass/lens/refraction, true object rotation, accurate reflections | Blender hero render -> AE composite |
| Both | Blender for the hero element only; AE for everything else |

Probe tools first (`after-effects-and-blender.md` section 1). If a tool is not available to Claude, produce a precise build spec and scripts for the user to run, and say so.

## Phase 5 - Build

**2D (AE):** organize -> block key positions on the animatic timing -> ease -> offset -> overlap -> polish (`motion-design.md` section 4).
**3D (Blender):** model with real-world proportions; set materials physically (e.g. glass IOR); fix camera and lens before animating; render RGBA/EXR image sequence; test-render a short range; hand off with the checklist (`after-effects-and-blender.md` section 4).
**Composite:** match black levels, shadow direction, grain, blur; unify with one grade.

## Phase 6 - Typography

One lead per beat; hierarchy by scale/weight; reveal text with the narration or sound hit; hold long enough to read; never animate long text letter-by-letter; verify RTL and glyph joining for Arabic.

## Phase 7 - Sound

Layers designed to the picture's beats (`sound-design.md`): bed, accents on landings, a riser only if a payoff follows, silence before the peak, a long tail after. Decision on music last. Audit layer count per 5 s.

## Phase 8 - Finish and QC

Grade for readability + mood; add shared grain if CG is present; check banding; run `scripts/video_qc.py`; run the rubric (`quality-control.md`). Restraint pass last.

## Branch decisions

| Question | If yes | If no |
|---|---|---|
| Does the sequence explain a physical process? | Verify physics of every moving element before animating; show causal order | Free abstract language is fine |
| Is there narration? | Time graphics to phrases; J/L overlap | Sound design carries rhythm |
| Is it a loop? | Match first and last frames; no baked-in dead frames | Plan the entry and the end hold |
| Is it a transition between segments? | One motivated object carries both scenes | Standalone: ensure a strong end state |
| Is the budget/time tight? | Cut 3D; use 2.5D and strong type | Consider Blender hero |

## Mistakes -> fixes

| Mistake | Fix |
|---|---|
| Everything animates at once | One lead; others static or secondary |
| "Cinematic" = letterbox + teal-orange grade | Re-read the intent; decide camera, light, restraint explicitly |
| 3D for its own sake | Replace with a 2D diagram if it explains equally well |
| No holds | Add 0.5-1.5 s stillness after each landing |
| Text hard to read after grade | Raise contrast; add subtle shadow; verify on phone |
| Sound hits drift from landings | Re-sync to the landing frame; cut hit length |
| Heavy gradient backdrop bands | Flatten, add fine grain, respect brand rules |

Worked example: `examples/motion-graphics-sequence.md`.
