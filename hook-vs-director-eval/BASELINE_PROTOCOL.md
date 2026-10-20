# Baseline protocol: Hook Engine vs Hook Director

Status: **BLOCKED - experiment not run.** Date: 2026-10-20.

## 1. Verified state of the two tools
| Tool | Verified location | Version | Instructions available | Status |
|---|---|---|---|---|
| Hook Engine | `hook-engine-pack/skills/` (9 skills), repo commit 20dd74c | 1.1.0 (CHANGELOG.md) | Yes, full text | Accessible. skills-tree hash (sha256 of sorted file hashes, first 16 hex): `9f2d8e17315c3a78`. Not installed in ~/.claude/skills, so it would be loaded by copying the tree into an isolated run. |
| Hook Director | **NOT FOUND** | unknown | **None** | **BLOCKER** |

## 2. Evidence for the Hook Director blocker
- `find / -iname '*hook-director*'` returns no directory or file.
- `~/.claude/skills/` and `~/.claude/plugins/` contain no such skill; the synced-skills manifest does not list it.
- claude.ai skill listing and search ("hook", "hook director", "opening seconds short video") returned nothing named Hook Director.
- The only trace is one line in `abbas-work-profile/references/skills-catalog.md`: "hook-director - Design or evaluate the opening seconds of a short video", inside a snapshot of the **Codex** environment dated 2026-10-13, which says it is an inventory and not a transfer of software.
- That line gives no version, instructions, inputs or outputs. Anything beyond it would be invented.

## 3. Consequence
The comparison needs both arms. Without Hook Director's actual instructions, any "Hook Director output" would be Hook Engine or me imitating a guess. I produced none. No winner can be named.

## 4. Design to run once Hook Director is supplied (frozen in advance)
1. Freeze 12 briefs (TEST_BRIEFS.md) with source packets and hash them before any generation.
2. Run each tool in a separate fresh context, one brief per context, same neutral prompt template, 3 genuinely different concepts per brief. Each concept: opening line, first-frame idea, curiosity gap, transition to next beat, retention sequence, final payoff.
3. Save raw output, exact prompt, tool version/hash and UTC timestamp to RAW_OUTPUTS/ before any anonymization.
4. Neither tool may read the other's outputs or this directory before both baseline runs are complete; Hook Engine agents are forbidden from hook-engine-pack/validation/ and tests/.
5. Neither skill is modified during the baseline. Fix the skill hashes before the run and re-check after.
6. Normalize format (strip tool-specific field names, evidence-record tags, scores), randomize candidate IDs with a seeded shuffle, store the key separately (sealed until ratings are filed).
7. Independent evaluators rate with EVALUATION_RUBRIC.md. Linting and self-scores are not evidence of creative effectiveness.
8. If fewer than 3 independent human evaluators rate, the whole review is labelled **preliminary**. Model reviewers, if used, are labelled non-human and do not count toward the 3.
9. Analyse per dimension, paired by brief, with evaluator agreement. No significance claims on 12 briefs unless a pre-stated test supports them. No claim about real retention.

## 5. What I can and cannot say now
Cannot: compare, rank, or recommend either tool on observed results. Can: state the blocker, supply the protocol, briefs list, rubric and recording sheet.
