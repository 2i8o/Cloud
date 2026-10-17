# professional-video-editing-intelligence

A self-contained Claude Code skill that gives Claude an **editing decision framework**: narrative structure, hooks and retention, cut timing and rhythm, continuity, B-roll, sound design, motion graphics, After Effects / Blender / Resolve pipelines, finishing, and quality control, plus a review procedure and two measurement scripts.

It does **not** retrain or modify the model. It is a set of instructions and reference files that Claude reads when the skill loads.

## Install (manual, Windows)

Your skills folder is `C:\Users\aaabb\.claude\skills` (the brief showed `C:\Users\aaabb.claude\skills`, which looks like a lost backslash; confirm that the folder `C:\Users\aaabb\.claude` exists). Personal skills live at `~/.claude/skills/<skill-name>/SKILL.md` per the Claude Code documentation.

1. Download `professional-video-editing-intelligence.zip`.
2. Make sure no folder named `professional-video-editing-intelligence` already exists in the skills directory (if one does, rename it as a backup).
3. In PowerShell:
   ```powershell
   Expand-Archive -Path "$HOME\Downloads\professional-video-editing-intelligence.zip" -DestinationPath "$HOME\.claude\skills"
   ```
   (Or right-click the zip -> Extract All, choosing `C:\Users\aaabb\.claude\skills`.)
4. Confirm the result is exactly:
   `C:\Users\aaabb\.claude\skills\professional-video-editing-intelligence\SKILL.md` (with `references\`, `workflows\`, `examples\`, `brand\`, `scripts\` beside it). The folder must not be nested twice.
5. Start (or restart) Claude Code. In a session, run `/skills` and look for `professional-video-editing-intelligence`. If the `skills` folder did not exist before this session started, run `/reload-skills`.

macOS/Linux: unzip into `~/.claude/skills/`.

## Using it

- **Direct:** type `/professional-video-editing-intelligence` then your request, e.g. `/professional-video-editing-intelligence review this Reel script and shot list`.
- **Automatic:** Claude Code puts the skill's `description` in context and may load the skill when your request matches it ("tighten this edit", "plan a 30-second Reel", "why does this animation feel cheap"). Per the documentation this is a matching decision by the model, **not a guarantee**. If it does not trigger, invoke it by name.
- The skill's main file is deliberately short. It routes Claude to `references/`, `workflows/`, and `examples/` as needed.

## What is verified and what is not

| Item | Status |
|---|---|
| Location, `SKILL.md` format, `name`/`description` frontmatter, live reload, `/skills`, `/reload-skills`, supporting files | Read from the official Claude Code skills documentation during the build (Claude Code docs, 2026-10-17) |
| The package structure and extracted-ZIP integrity | Tested in the build sandbox (see `BUILD-LOG.md`) |
| `scripts/video_qc.py` and `scripts/shot_rhythm.py` | Run on a synthetic clip with known cuts, a silence gap and a black segment (see `BUILD-LOG.md`) |
| Discovery/activation **on your machine** | **Not verified.** The sandbox is a cloud Linux session; personal skills in `~/.claude/skills` are not loaded in cloud sessions. After installing, `/skills` is the check |
| After Effects, Blender, Resolve commands | **Not tested** (not installed in the sandbox). Marked in the references as `[Known]`/`[Web]`; verify on your installed versions |
| Videos | No video or audio was watched or heard during research; transcripts and page text were read (see `references/learning-sources.md`) |

## Optional dependencies

- `ffmpeg` and `ffprobe` on PATH for `scripts/`. Python 3 (`py` or `python` on Windows) to run them:
  ```powershell
  py "$HOME\.claude\skills\professional-video-editing-intelligence\scripts\video_qc.py" final.mp4 --expect-width 1080 --expect-height 1920 --expect-fps 30
  py "$HOME\.claude\skills\professional-video-editing-intelligence\scripts\shot_rhythm.py" final.mp4
  ```
- Everything else is plain Markdown that works offline. External links appear only as provenance.

## Contents

```
professional-video-editing-intelligence/
|- SKILL.md                      entry point: ladder, nine questions, routing, ledger, hard rules
|- README.md                     this file
|- BUILD-LOG.md                  what was built, tested, found, and fixed; limits; resume notes
|- references/
|  |- storytelling-and-editing.md   cuts as punctuation, Rule of Six, narrative skeleton, emotion timing
|  |- pacing-and-continuity.md      rhythm, shot-length curve, transitions, continuity
|  |- hook-and-retention.md         hooks, integrity gate, structure, 10-second template
|  |- sound-design.md               layer budget, silence, sync, J/L cuts, mix, loudness
|  |- motion-design.md              purpose test, easing, timing, typography, metaphors, physics QC
|  |- after-effects-and-blender.md  capability probe, tool choice, AE practice, Blender->AE handoff
|  |- color-and-finishing.md        color order, grading controls, delivery, captions
|  |- quality-control.md            scored rubric, diagnosis tables, checklists
|  `- learning-sources.md           sources: what was actually accessed, tiers, limits
|- workflows/
|  |- creative-brief-to-edit.md     brief -> export with exit tests and branches
|  |- short-form-video.md           15-60 s vertical workflow and budgets
|  |- cinematic-motion-graphics.md  intent -> animatic -> build path -> QC
|  `- editing-review.md             evidence-first review procedure and output template
|- examples/
|  |- hook-analysis.md              Test A: 10-second hook, failed draft -> revised
|  |- educational-reel.md           Test B: 30-45 second educational Reel
|  |- motion-graphics-sequence.md   Test C: cinematic sequence with Blender + AE
|  `- lens_ray_check.py             Snell's-law check used in Test C
|- brand/
|  `- abbas-abdulmunem.md           opt-in brand/production overlay (not part of the universal logic)
`- scripts/
   |- video_qc.py                   specs, loudness, silence/black/freeze candidates
   |- shot_rhythm.py                shot lengths and rhythm curve
   `- validate_package.py           checks this package after you edit it
```

## Maintenance

- Edit the Markdown directly; Claude Code watches the skills directory and reloads changes in the running session (new top-level skills folder: `/reload-skills`).
- Keep `SKILL.md` short; put detail in `references/`.
- Keep brand rules only in `brand/`. Add a new file there for another brand rather than editing universal files.
- `description` plus `when_to_use` is truncated at 1,536 characters in the skill listing (documented), so keep trigger phrases early.
- To stop automatic loading but keep the manual command, add `disable-model-invocation: true` to the frontmatter.

## Provenance and honesty notes

- Core editing principles come from sources whose transcripts/pages were read (Every Frame a Painting; StudioBinder on Walter Murch; Murch's writings; Ben Marriott's free videos and course syllabus; Casey Faris's Resolve course; added motion/sound/pipeline sources). Each rule in the references is tagged by evidence tier; short-form retention data is correlational and is used only as "what to test."
- Ben Marriott's *Master Motion Design* lessons are paywalled and were not accessed. Only the public syllabus text and a one-minute promo were read.
