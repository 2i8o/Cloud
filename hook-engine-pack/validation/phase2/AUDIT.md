# Phase 2 - Step 1: audit of the v1.0.0 package

Date: 2026-10-20. Every statement below was checked by running a command or reading the file named; items I could not check are listed as such at the end.

## A. Discrepancies in reported numbers - resolved

| Reported earlier | What is true (checked) |
|---|---|
| "46/46", "47/47", "48/48" checks | Three different runs: 46 before a product-flag test was added; **47** = `run_tests.py` without `--zip`; **48** = with `--zip` (adds the archive check). The final v1.0.0 numbers were 47 (48 with the ZIP). Not a contradiction, but I reported all three without explaining. |
| "12 held-out cases" | Only **7** were clean. A keyword search of the skill files (`grep` over `skills/`) found the "held-out" topics already present for T11 (`screen time` x2), T31 (`colour blind` x3 in the claim registry), T32 (`contact-lens`/`hygiene`), T37 (installer wording in README), T38 (`OptiNest` x4 in constraints). Reclassified to not held-out. Clean: T10, T12, T14, T23, T33, T34, T35. |
| "38 test cases ... executed" | They were **specifications**. Wired to an automated check: 11 (T05, T15, T16, T17, T18, T24, T26, T27, T35, T36, T38). T37 carried an `automated_check` string that no test loop executed (covered separately by installer tests). Dry-run by me and self-graded: 8 (T03, T05, T13, T15, T18, T23, T26, T35). The rest (about 20) were never run. The 47 machine checks were mostly linter/installer/validator checks, not model-behaviour tests. |
| ZIP = tree? | `diff -r` of the unzipped archive against `hook-engine-pack/` was clean; 67 files in both (v1.0.0). |
| Sources read | 63 rows; I did not re-open all of them in Phase 2 - only the pinhole, colour-blindness-prevalence and new-topic sources. Others stay as logged in `access_status`. |

## B. Scientific re-check of existing examples

| # | Finding | Evidence | Severity |
|---|---|---|---|
| A1 | **"ثقب بحجم دبوس" (pin-sized hole) is not supported and is probably wrong.** Clinical pinholes are ~1.2 mm (usable 0.94-1.75 mm); below ~0.75 mm diffraction makes vision worse; a pin tip is smaller than that. | S65 (Univ. Iowa teaching handout), S64 (IOVS 2009: 0.5 and 0.75 mm discs reduced corrected vision), S66 (IOVS 2014), S67 (Review of Optometry) | **High** - the hook of the recommended finalist, the registry-adjacent examples, 21 files |
| A2 | The pinhole closing beat told viewers that a sharpened result "means the blur is refractive rather than a disease". Clinically it is a clue under controlled conditions (adults, no ocular disease, errors up to ~+-5 D); macular disease or lens opacities can give no gain or a loss; "individuals with ocular disease should not be told ..." based on a pinhole alone. For a lay viewer this is a self-diagnosis step. | S65, S68, S64 | **High** (medical-interpretation wording) |
| A3 | C16 quoted "~1 in 10 males" from AAO's myths page, while AAO's 2017 explainer says 5-8% of males and 0.5% of females. The two AAO pages disagree. | S35 vs S72 | Medium |
| A4 | The v1.0 gate (`hook-scientific-validation`) accepted these because it only required "a source id" and allowed `plausible` claims in hooks; it never asked for the size or limits. The linter had no field that could catch them. | `hook_lint.py` v1.0, `accuracy-rules.md` C13 | Design flaw |
| A5 | Example anchoring: the flawed phrase appeared in **21 files** of the v1.0 tree (examples, taxonomy, curiosity doc, dry-runs, 17 fixtures, cases). A model copying "good examples" propagates the error. | `git grep -l "بحجم دبوس" da93c76` | Process risk |
| A6 | Other examples re-read against the AAO pages already in the ledger (glasses myth, blink, blue light, outdoor time, spectacle lenses, 20/20): consistent with their sources. Not re-verified: Iraqi phrasing, any figure marked "verify". | S32, S33, S35, S39, S40, S44 | OK / unverified Iraqi |
| A7 | "Diagnosis" language scan of the skill text and fixtures: no "you have X" statements in finished examples; but the v1.0 rules did not forbid hedged cause-naming for the viewer's symptom or calling a screen demo "the test" (both appeared in the Phase-2 baseline). | grep + baseline review | Medium |

## C. Existing workflow / published material
- No creator scripts, published-video analytics or exports exist in the repository, in `~/.claude`, or elsewhere on the machine searched (`find` for srt/csv). The only analytics file in the tree (`tests/fixtures/analytics_sample.csv`) is **synthetic** test data written by me and must never be read as the creator's results.
- The creator's own skill catalog (read-only, `abbas-work-profile/references/skills-catalog.md`) lists a `hook-director` skill ("design or evaluate the opening seconds of a short video"). It is **not installed in this environment**, so I could not compare outputs. Overlap with `hook-engine` is likely; the creator should say which one should own hook evaluation.
- **Requested from the creator** (see `EXPERIMENT_PLAN.md`): 10-20 published scripts with their hooks, platform exports (YouTube Stayed-to-watch/average % viewed, Instagram skip rate/retention, TikTok watch time), publication dates and any outputs from `hook-director`.

## D. What this audit could not verify
Iraqi naturalness of any line; the truth of claims in v1.0 sources that I did not re-open; the effect of any hook on real audiences; independent reproduction (every artefact in Phase 2 was produced and scored by the same model).
