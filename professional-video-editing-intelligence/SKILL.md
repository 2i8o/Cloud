---
name: professional-video-editing-intelligence
description: Editing-decision framework for planning, building and critiquing video - narrative structure, hooks and retention, shot selection, cut timing and rhythm, continuity, B-roll, sound design, motion graphics and typography, After Effects / Blender / DaVinci Resolve pipelines, finishing and QC. Use when the user asks to plan, storyboard, edit, review, tighten or diagnose a video, Reel/Short, hook, title sequence or motion-graphics piece, or asks why an edit feels slow, flat, cluttered or confusing. Not for button-by-button software help.
---

# Professional Video Editing Intelligence

A decision framework, not a list of effects. Every shot, cut, sound, and animation must earn its place by changing what the viewer **understands, feels, or expects**. If it does none of these, cut it.

## 0. Honest capability check (do this first, once per task)

State which of these is true before promising anything:

| Claude can | Claude cannot |
|---|---|
| Read scripts, transcripts, EDLs/XML, shot lists, images, extracted frames | Watch or listen to a video file directly |
| Run `ffmpeg`/`ffprobe` and `scripts/*.py` to measure cuts, loudness, silence, freezes, specs | Judge taste from numbers alone - numbers flag, humans/frames confirm |
| Write plans, ExtendScript/`bpy` scripts, ffmpeg commands | Control After Effects / Blender / Resolve unless a verified integration is present |

Probe tools instead of assuming: `ffmpeg -version`, `blender --version`, `where aerender` (Windows) / `which aerender`. Never claim a render, export, or playback happened unless a file was produced and checked. See `references/after-effects-and-blender.md` section 1.

## 1. The priority ladder (what wins when goals conflict)

Adapted from Walter Murch's "Rule of Six" (his weights were "slightly tongue-in-cheek"; the *order* is the lesson). Sacrifice from the bottom up:

1. **Meaning / emotion** - what the viewer feels or concludes (for explainers: also *what they believe is true*)
2. **Story / clarity** - does this advance the idea; can a first-time viewer follow it
3. **Rhythm** - is the cut/beat at a "right" moment
4. **Eye-trace** - is attention where the next shot expects it
5. **Screen direction / planarity** - left-right and axis consistency
6. **Spatial continuity** - physical layout consistency
7. **Polish** - grade, grain, easing refinement (never above 1-3)

Explainer addendum (synthesis, not Murch): **Accuracy** sits at level 1. A beautiful cut that implies something false loses.

## 2. The nine questions (ask for every shot, cut, sound, and animation)

1. What does this serve - emotion, information, rhythm, or attention? (If "looks cool": remove.)
2. Why does the viewer need it *at this exact moment*?
3. Does this cut improve meaning, emotion, clarity, or rhythm? Which one?
4. Would a direct cut beat this transition? (Default: yes.)
5. Does this sound reinforce the action or compete with it?
6. Does this motion clarify the concept or decorate the frame?
7. Does the hook's promise match what the video delivers?
8. Does the sequence work with the sound off, and with the picture off?
9. What can be removed so the strongest element lands harder?

## 3. Route the task

| Task | Read first | Then |
|---|---|---|
| Turn an idea/brief into an edit plan | `workflows/creative-brief-to-edit.md` | `references/storytelling-and-editing.md` |
| Reel / Short / TikTok (15-60 s) | `workflows/short-form-video.md` | `references/hook-and-retention.md`, `references/pacing-and-continuity.md` |
| Hook only (first 3-10 s) | `references/hook-and-retention.md` | `examples/hook-analysis.md` |
| Cinematic / motion-graphics sequence | `workflows/cinematic-motion-graphics.md` | `references/motion-design.md`, `references/after-effects-and-blender.md` |
| Review / critique / "why is this weak" | `workflows/editing-review.md` | `references/quality-control.md` |
| Cut timing, rhythm, B-roll, continuity | `references/pacing-and-continuity.md` | `references/storytelling-and-editing.md` |
| Sound, music, SFX, mix | `references/sound-design.md` | `references/quality-control.md` |
| Color, grain, export, delivery | `references/color-and-finishing.md` | `references/quality-control.md` |
| Sources / "how do you know that" | `references/learning-sources.md` | - |
| Worked examples to imitate | `examples/` | - |

Load only what the task needs. Detailed rules live in the references; this file stays an entry point.

## 4. Pipeline (branch as the project demands)

Brief -> Narrative structure -> Shot plan -> Rough cut -> Rhythm + continuity pass -> Sound design -> Motion graphics -> Color + finishing -> QC -> Export.

Branches: talking-head (rhythm and cut-on-thought dominate; motion graphics support), B-roll explainer (shot-meaning relationships dominate), motion-graphics-only (timing/easing/hierarchy dominate; sound drives rhythm), 3D-assisted (add Blender render + composite stage), AI-generated imagery (add object-identity and physics QC). Each stage has an exit test in `workflows/creative-brief-to-edit.md`.

## 5. Required output: the Decision Ledger

When proposing or reviewing an edit, give decisions in this shape (short rows, not essays):

| Time | Element | Job (emotion / info / rhythm / attention) | Why now | Alternative considered | Risk |
|---|---|---|---|---|---|

Every row needs a job. Rows whose job is "style" are candidates for deletion. Label key claims **Established** (taught by multiple sources/read in a source), **Heuristic** (practitioner rule of thumb), or **Guess** (inference/untested). The reference files tag each rule with its source tier.

## 6. Hard rules

- **Do not alter the user's spoken words or meaning.** Propose an edit list; never overwrite originals or finals; write new versions.
- **Hook <-> payoff contract:** a curiosity gap must be resolved honestly. No bait-and-switch, no fabricated stakes, no fearmongering. Facts in graphics/captions are checked against a named source before they ship.
- **Restraint test:** remove each effect once. If nothing is lost, it stays removed.
- **No false certainty about taste.** Offer 2 defensible options when the choice is genuinely subjective; recommend one.
- **Respect the destination spec** (resolution, fps, safe areas, loudness) before polishing.

## 7. Brand and project gate

This skill is brand-neutral. If the content is for **Abbas Abdulmunem** (optics/vision education, Arabic, short vertical video), also read `brand/abbas-abdulmunem.md` and any project files it points to (e.g. `brand.ts`, `theme.ts`, `STANDARDS.md`); those override defaults here. For any other client or project, read that project's own brand/spec files instead and do not import Abbas's palette or identity.

## 8. Working with other skills

If present in the environment, defer to them for their specialty and use this skill for the *edit logic*: script/hook-writing skills (copy), platform-spec skills (exact dimensions, caption rules), research/fact-check skills (evidence for claims), personal-profile skills (brand facts). This skill decides *what the picture and sound should do*; those decide *what the words are and which spec applies*.

## 9. Respond in the user's language

Match the user's language. For Arabic text in graphics: verify shaping, direction (RTL), numerals, and punctuation in the actual render; never assume Latin-text timing rules (reading speed) apply unchanged.
