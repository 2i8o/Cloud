# Hook Engine - Claude Code skill package (v1.1.0)

A modular set of nine Claude Code skills for designing **short-form educational video hooks and retention** for Abbas Abdulmunem's optometry / optics / vision-science channel (YouTube Shorts, Instagram Reels, TikTok; 20-45 s; scripts in natural Iraqi Arabic, documentation in English).

It optimises two separate things that are easy to confuse:
1. **Scroll-stopping** - the right viewer stops within the first 1-3 seconds.
2. **Sustained retention** - the curiosity is real, progresses, and ends in a payoff that matches the promise.

An opening that attracts and then disappoints is treated as a failure.

> **Read this first - what this package is and is not.** It is a disciplined *process* with hard gates (accuracy, honesty, diversity), built from 94 sources that were actually opened (see `validation/phase2/FINAL_REPORT.md` for what Phase-2 testing did and did not show). It is **not** a proven predictor of virality; no hook formula here was validated on 20-45 s feeds. Iraqi Arabic examples are drafts for the creator's review. See `SOURCE_BIBLIOGRAPHY.md` ("What was NOT accessed") and `tests/RESULTS.md` for limits.

## Contents

```
hook-engine-pack/
  skills/                      <- the installable part (9 skills)
    hook-engine/               entry point + router + pipeline + output format
    hook-idea-diagnosis/       idea gate (PROCEED/RE-ANGLE/RESEARCH/REJECT) + curiosity map + psychology reference
    hook-writing/              24-mechanism taxonomy, Iraqi Arabic guide, examples
    hook-retention/            narrative architectures, beat sheets, open-loop ledger
    hook-visual-design/        first frame, production brief, camera-vs-eye rules
    hook-scientific-validation/ claim gate, optometry vs ophthalmology, verified claim registry
    hook-evaluation/           hard gates, rubric, 3-second diagnostic, diversity; scripts/hook_lint.py
    hook-analytics/            metric dictionary, experiment protocol; scripts/analytics_compare.py
    hook-research/             source grading + ledger maintenance
  docs/                        long-form documents (generated from the skills' references)
  RESEARCH_LEDGER.csv          94 sources with access status, extraction, limits, confidence
  SOURCE_BIBLIOGRAPHY.md       readable bibliography + what was not accessed + recorded disagreements
  RESEARCH_METHODOLOGY.md      how research was done and graded
  TEST_CASES.md                49 behaviour specifications (10 held-out)
  validation/phase2/           audit, 13-brief before/after evaluation, failure patterns, improvement log, experiment plan
  tests/                       cases.json, fixtures, run_tests.py, RESULTS.md, DRY_RUNS.md
  scripts/                     install.sh, validate_package.py, build_docs.py
  QUICKSTART.md  CHANGELOG.md  VERSION
```

Only `skills/` is needed at runtime. Claude Code does **not** auto-load the other Markdown files; each skill reads its own `references/` on demand through the relative paths written in its `SKILL.md`.

## Requirements
- Claude Code (developed against 2.1.304). No API keys, subscriptions or external services.
- Optional: Python 3.8+ (stdlib only) for the two helper scripts; `bash` for `install.sh`.
- Web access is useful for claim verification; without it the skills keep claims `unverified`.

## Install (manual, non-destructive)

Option A - script (recommended). From the unzipped folder:

```bash
bash scripts/install.sh --dry-run          # shows what would be copied
bash scripts/install.sh                    # copies skills/* into ~/.claude/skills/
# project-only instead:  bash scripts/install.sh --dest /path/to/repo/.claude/skills
```

The script is all-or-nothing: if **any** target skill folder already exists it copies nothing, changes nothing, and exits with status 3. It never deletes, renames or edits existing skills.

Option B - by hand:

```bash
mkdir -p ~/.claude/skills
for d in skills/hook-*; do n=$(basename "$d")
  if [ -e ~/.claude/skills/"$n" ]; then echo "EXISTS, skipped: $n"; else cp -R "$d" ~/.claude/skills/; fi
done
```

Then: Claude Code picks up added/edited skills inside an existing `~/.claude/skills/` during the session. If `~/.claude/skills/` did not exist when the session started, run `/reload-skills` (or restart). Check with `/skills` or ask "What skills are available?". Invoke with `/hook-engine <topic>` or just describe the task.

Windows: use Option B with PowerShell `Copy-Item -Recurse skills\hook-* $env:USERPROFILE\.claude\skills\` (not tested here).

## Use
See `QUICKSTART.md`. In short: `/hook-engine` + topic -> idea verdict -> three different finalists (with first frame, continuation, payoff, risks, confidence) -> one recommendation -> you choose -> script.

## Verify the install
```bash
python3 scripts/validate_package.py .        # structure, frontmatter, paths, ledger, cases
python3 tests/run_tests.py                   # machine checks (see tests/RESULTS.md)
claude plugin validate ~/.claude/skills      # Claude Code's own validator (v2.1.233+)
```

## Troubleshooting
| Symptom | Fix |
|---|---|
| `/hook-engine` not recognised | run `/reload-skills`; confirm `~/.claude/skills/hook-engine/SKILL.md` exists; run `claude plugin validate ~/.claude/skills` (flags unparsable frontmatter) |
| Skill never triggers by itself | invoke directly with `/hook-engine`; descriptions are capped at 1,536 characters and trimmed if you have many skills (`/doctor`) |
| Installer exits 3 | a folder with that name exists. Rename/remove it yourself if you want to replace it; the installer will not |
| Claude stops following rules in a long session | invoke `/hook-engine` again; after compaction only the first ~5,000 tokens of an invoked skill are kept, so the important rules are at the top |
| Script not found | the scripts live inside the installed skills: `~/.claude/skills/hook-evaluation/scripts/hook_lint.py`, `~/.claude/skills/hook-analytics/scripts/analytics_compare.py` |
| Arabic looks odd | files are UTF-8; use an editor that renders RTL |

## Remove
```bash
rm -r ~/.claude/skills/hook-engine ~/.claude/skills/hook-idea-diagnosis ~/.claude/skills/hook-writing \
      ~/.claude/skills/hook-retention ~/.claude/skills/hook-visual-design ~/.claude/skills/hook-scientific-validation \
      ~/.claude/skills/hook-evaluation ~/.claude/skills/hook-analytics ~/.claude/skills/hook-research
```
(Only these nine names; the package touches nothing else.)

## Maintaining the package
Edit the sources (`skills/*/references/*.md`, `RESEARCH_LEDGER.csv`, `tests/cases.json`) then run `python3 scripts/build_docs.py` to regenerate `docs/`, `SOURCE_BIBLIOGRAPHY.md`, `TEST_CASES.md`; run `python3 tests/run_tests.py`.

## Permanent constraints built into every skill
Active identity = Abbas Abdulmunem (never OptiNest); optometry != ophthalmology; no misleading medical claims, manufactured fear, fabricated facts, false urgency or undeliverable clickbait; no product/service recommendations unless requested; improve the idea, curiosity, progression and payoff - not volume, cuts or effects; never overwrite existing skills.
