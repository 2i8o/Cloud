# Improvement log (v1.0.0 -> v1.1.0)

Status vocabulary: **VERIFIED-SOURCE** (the correction was checked against retrieved source text) - **VERIFIED-TEST** (a machine test exercises the new rule) - **OBSERVED** (seen in the self-graded re-review of outputs; same-model bias) - **HYPOTHESIS** (instruction change; effect on real performance unknown).

| ID | Trigger (evidence) | Change (files) | Status |
|---|---|---|---|
| I-01 | A1/A2: unsupported hole size; viewer-result inference | `skills/hook-scientific-validation/references/accuracy-rules.md` (C13 rewritten with 1.2 mm, <0.75 mm diffraction, +-5 D, disease caveat, "do not tell viewers what their result means"); `skills/hook-writing/references/examples.md` (pinhole ladder, worked example, correction note); `iraqi-arabic.md`, `curiosity-psychology.md`, `candidate_schema.json`, fixtures, `cases.json`, `DRY_RUNS.md` (phrase removed from all 21 files) | VERIFIED-SOURCE (S64-S68, S65); phrase absent from all non-baseline files |
| I-02 | A3: AAO pages disagree on colour-blindness prevalence | accuracy-rules C16 (use 5-8% range, attribute, flag the disagreement) | VERIFIED-SOURCE (S72 vs S35) |
| I-03 | Pattern 2: `verified` = "has an id"; `plausible` in hooks (5/39) | `hook-scientific-validation/SKILL.md` (evidence record: `support_quote` <= 15 words + `scope`; assertions need `verified`; parameter/number/comparator rule); `hook_lint.py` (E_UNVERIFIED_CLAIM now covers plausible, E_NO_EVIDENCE_RECORD, E_PARAM_NOT_SUPPORTED); G8 in `hook-evaluation/SKILL.md` | VERIFIED-TEST (fixtures R16, R17, R23). Quotes are self-reported; the linter cannot confirm they exist in the source - a human must |
| I-04 | Pattern 1: 13/39 no-gap hooks | `hook-writing/SKILL.md` (gap & shape rules, rewrite M07/M18 as questions, answer-in-hook rule), `hook-evaluation/SKILL.md` (G9, shape variety), linter (E_NO_GAP, E_ANSWER_IN_HOOK_NO_BEAT2, W_SHAPE) | VERIFIED-TEST (R19, R22); OBSERVED NOGAP 13/39 -> 4/39 on the re-review (self-graded) |
| I-05 | Pattern 3: 39/39 five-beat plans; 36/39 empty endings | `hook-retention/SKILL.md` (beat table with new information, written closing line, no default split), linter (E_NO_PLAN, E_EMPTY_BEAT, E_NO_CLOSING_LINE) | VERIFIED-TEST (R21); 0/39 short closings in v1.1 outputs. Beat counts are still all five (HYPOTHESIS that the rule alone will vary structure) |
| I-06 | Pattern 8: finalists converge on one takeaway | `hook-evaluation/SKILL.md` Step 5, `payoff_key` + E_PAYOFF_DUP | VERIFIED-TEST (R20) |
| I-07 | Pattern 5: abstract first frames | `hook-visual-design/SKILL.md` item 0 (concrete or it doesn't count; parameters from sources; mark UNFILMABLE) | HYPOTHESIS; OBSERVED visual <= 2: 11/39 -> 2/39 (self-graded) |
| I-08 | Pattern 7: demo presented as the test | `hook-visual-design/SKILL.md` rule 0 (+ participatory-measurement validity 0a), `hook-scientific-validation/SKILL.md` rule 3, G7, linter E_DEMO_AS_TEST | VERIFIED-TEST (R18); 0a is HYPOTHESIS (found in B02-B on the first v1.1 draft) |
| I-09 | v1.0 linter caught 8/26 weak finalists; `E_GENERIC` precision 3/7 | `hook_lint.py`: `E_GENERIC` -> warning `W_GENERIC`; report in `review/lint_vs_review_output.txt` | VERIFIED (numbers from the frozen baseline) |
| I-10 | Iteration-1 review: wrong location, category shift, symptom-to-cause by hedging, payoff not ready, comparator absent | `hook-scientific-validation/SKILL.md` (location/direction in the parameter rule; category shift; hedging does not exempt cause-naming), `hook-evaluation/SKILL.md` (G10, self-check item 2), linter (`payoff_ready`, W_COMPARATIVE, W_PAYOFF_PENDING, E_RECOMMEND_PENDING) | Payoff/comparator rules VERIFIED-TEST; the rest HYPOTHESIS |
| I-11 | Pattern 4: low originality | `hook-idea-diagnosis/SKILL.md` ("angle a standard explainer lacks" + topic fidelity) | HYPOTHESIS; OBSERVED originality <= 2: 12/39 -> 5/39 (self-graded) |
| I-12 | Pattern 10: Iraqi register | `hook-writing/references/iraqi-arabic.md` section 8b (candidate vocabulary swaps, marked Guess) | HYPOTHESIS - needs the creator's confirmation; `W_MSA_SOFT` only detects a few words |
| I-13 | New topics needed facts | `RESEARCH_LEDGER.csv` +31 rows (S64-S94); registry C21-C28 (C26-C28 added only after the held-out evaluation) | VERIFIED-SOURCE (excerpts) |
| I-14 | Experiment planning needs a size check | `hook-analytics/scripts/sample_size.py` + SKILL step 3b | VERIFIED-TEST (hand-computed 1,468 / 473) |

## Not changed (considered and rejected)
- No new skills; no change to the pipeline's order.
- No attempt to make the linter judge truth, originality or Iraqi naturalness - it cannot, and Phase 2 showed it should not be presented as if it did.
- Weights in the rubric: unchanged (no evidence either way).

## Re-tests after each revision
Iteration 1 (rules + first outputs) -> linter on all 39 finalists: 31 failed (48 errors). Iteration 2 (corrections) -> 0 errors, 9 warnings. Full `tests/run_tests.py` re-run after each code change; results in `tests/RESULTS.md`.
