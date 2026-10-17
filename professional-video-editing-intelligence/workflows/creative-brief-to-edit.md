# Workflow: Creative Brief -> Finished Edit

Pipeline: Brief -> Narrative structure -> Shot plan -> Rough cut -> Rhythm + continuity -> Sound -> Motion graphics -> Color + finishing -> QC -> Export. Each stage has an **exit test**; don't advance until it passes. Skip stages that don't apply, and say which and why.

## Stage 0 - Intake (ask only what is missing; otherwise state assumptions)

Fill this table from the user's message and project files. Ask the user only for items that change the creative direction and cannot be inferred; list defaults for the rest.

| Item | Default if unstated |
|---|---|
| Audience + one thing they should understand/feel | Infer from brief; state it |
| Platform + length | Vertical 9:16, 20-45 s for short-form; 16:9 for long-form |
| Spec (res/fps/safe areas/loudness) | Project files first; else 1080x1920, 30 fps, confirm |
| Materials available (footage, VO, graphics, 3D assets, music) | Inspect directory; list what exists |
| Claims needing sources | Mark every factual claim |
| Brand/project rules | Look for brand/spec files; apply `brand/` only for the matching owner |
| Tools available | Probe (`after-effects-and-blender.md` section 1) |
| Hard constraints (don't alter speech, face visible, etc.) | Preserve originals |

**Exit test:** one sentence "Viewer should (understand/feel) X by the end," plus one sentence "The video asks Y and answers Y."

## Stage 1 - Narrative structure

Write: promise, tension, evidence beats, turn, payoff, landing (`storytelling-and-editing.md` section 3). For each beat give: purpose, duration estimate, and the *evidence type* (footage / graphic / measurement / words).
**Exit test:** the contract test (promise scope = payoff scope); every claim has a source or is cut; total duration fits the platform.

## Stage 2 - Shot plan

For every beat list: shot (what is seen), source (existing footage / to shoot / to animate / to render), purpose (illustrate / evidence / metaphor), and fallback if the asset isn't available. Mark physics/anatomy-sensitive visuals for QC.
**Exit test:** mute test on the shot list read in order - can the story be followed from images alone? Every shot has a job.

## Stage 3 - Rough cut (structure only)

Assemble in order. Cut to thought boundaries. No effects, no music. Trim redundancy aggressively.
**Exit test:** read-through is comprehensible with ugly visuals; length within +/-10% of target before polishing.

## Stage 4 - Rhythm and continuity pass

Apply `pacing-and-continuity.md`: build/peak/release curve, holds after payoff, J/L cuts, direction and identity continuity, transition choices (direct cut by default). Run `scripts/shot_rhythm.py` when an export exists.
**Exit test:** the 5 cuts you like least are justified in the Decision Ledger or fixed.

## Stage 5 - Sound design

Apply `sound-design.md`: VO clean -> ambience bed -> hard-sync FX -> accents -> music last. Layer count per 5 s, silence placement, ducking.
**Exit test:** picture-off listen is followable; <= ~5 layers; no unmotivated hits.

## Stage 6 - Motion graphics

Apply `motion-design.md`: purpose test per element, hierarchy, easing, hold-then-move, safe areas. Block -> ease -> offset -> polish. For 3D, follow `after-effects-and-blender.md` section 4.
**Exit test:** remove each graphic once; those whose removal is unnoticed stay out. Sound-off comprehension still works.

## Stage 7 - Color and finishing

Apply `color-and-finishing.md`: color management -> balance -> look -> unify composited layers -> check graphic contrast after the grade.
**Exit test:** consistent across cuts; subject legible; graphics readable.

## Stage 8 - Quality control

Run the rubric in `quality-control.md` and `scripts/video_qc.py`. Fix blockers (any 0 in clarity, integrity, technical).
**Exit test:** no blocker; remaining weak scores (<=1) are either fixed or listed with a reason.

## Stage 9 - Export

Master -> delivery derivatives; versioned filenames; originals untouched; verify the final file by re-running QC on the *exported* file, not the project.
**Exit test:** exported file passes the spec checks; user receives a short change log.

## Branches

| Project type | What changes |
|---|---|
| Talking head | Stage 3-4 dominate: cut on thought; J/L cuts; motion graphics are annotations |
| B-roll explainer | Stage 2 dominates: shot meaning and evidence; metaphor accuracy |
| Pure motion graphics | Replace Stage 3 with an **animatic** (timed boards + temp sound); sound leads rhythm |
| 3D hero + graphics | Add style frames before Stage 6 and a Blender render + handoff checklist |
| AI-generated assets | Add object-identity and physics QC after Stage 2; reject assets that fail |
| Tight deadline | Keep Stages 1, 3, 4, 8; reduce 6/7 to the minimum that serves clarity; say what was dropped |

## Output of this workflow

A plan document containing: the intake table, narrative beat sheet, shot plan, the Decision Ledger (SKILL.md section 5), a risk list, and the QC plan. If the user asked for execution, then the artifacts that were actually produced (and where), clearly separated from the artifacts that are only proposed.
