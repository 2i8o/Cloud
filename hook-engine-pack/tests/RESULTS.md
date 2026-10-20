# Test results (machine-checkable part)

Executed with `python3 tests/run_tests.py`. 66/66 checks passed.

| Result | Check |
|---|---|
| PASS | validate_package: package is structurally valid |
| PASS | build_docs --check: generated documents are current |
| PASS | lint gold/G01_acuity_pinhole.json: 0 errors |
| PASS | lint gold/G02_myth_blink_lenses.json: 0 errors |
| PASS | lint redteam/R01_same_hook: rejects with ['E_INSIGHT_DUP', 'E_MECH_DUP', 'E_TEXT_OVERLAP'] |
| PASS | lint redteam/R02_sensational_recommended: rejects with ['E_FEAR', 'E_RECOMMEND_SCI', 'E_UNVERIFIED_CLAIM'] |
| PASS | lint redteam/R03_spoils_payoff: rejects with ['E_SPOILS_PAYOFF'] |
| PASS | lint redteam/R04_no_continuation: rejects with ['E_MISSING_FIELD'] |
| PASS | lint redteam/R05_generic_question: rejects with ['E_GENERIC_OPENER', 'W_GENERIC'] |
| PASS | lint redteam/R06_effects_instead_of_premise: rejects with ['E_EFFECT_FIX'] |
| PASS | lint redteam/R07_invented_citation: rejects with ['E_UNKNOWN_SOURCE'] |
| PASS | lint redteam/R08_not_accessed_source: rejects with ['E_SOURCE_NOT_ACCESSED'] |
| PASS | lint redteam/R09_msa: rejects with ['E_MSA'] |
| PASS | lint redteam/R10_profession: rejects with ['E_PROFESSION'] |
| PASS | lint redteam/R11_cliffhanger: rejects with ['E_NO_PAYOFF_MATCH'] |
| PASS | lint redteam/R12_ambiguity_rewarded: rejects with ['E_RECOMMEND_CLARITY'] |
| PASS | lint redteam/R_fear: rejects with ['E_FEAR'] |
| PASS | lint redteam/R_diagnostic: rejects with ['E_DIAGNOSTIC'] |
| PASS | lint redteam/R_banned: rejects with ['E_BANNED_PHRASE'] |
| PASS | lint redteam/R_product: rejects with ['E_PRODUCT'] |
| PASS | lint redteam/R_brand: rejects with ['E_BRAND'] |
| PASS | lint redteam/R16_plausible_assertion: rejects with ['E_UNVERIFIED_CLAIM'] |
| PASS | lint redteam/R17_number_not_in_quote: rejects with ['E_PARAM_NOT_SUPPORTED'] |
| PASS | lint redteam/R18_demo_as_test: rejects with ['E_DEMO_AS_TEST'] |
| PASS | lint redteam/R19_no_gap: rejects with ['E_NO_GAP'] |
| PASS | lint redteam/R20_payoff_dup: rejects with ['E_PAYOFF_DUP'] |
| PASS | lint redteam/R21_empty_beats: rejects with ['E_EMPTY_BEAT', 'E_NO_CLOSING_LINE'] |
| PASS | lint redteam/R22_answer_in_hook_no_beat2: rejects with ['E_ANSWER_IN_HOOK_NO_BEAT2'] |
| PASS | lint redteam/R23_no_evidence_record: rejects with ['E_NO_EVIDENCE_RECORD'] |
| PASS | lint: product language allowed when explicitly requested by the creator |
| PASS | case T05 automated lint |
| PASS | case T15 automated lint |
| PASS | case T16 automated lint |
| PASS | case T17 automated lint |
| PASS | case T18 automated lint |
| PASS | case T24 automated lint |
| PASS | case T26 automated lint |
| PASS | case T27 automated lint |
| PASS | case T35 causal-language detector fires |
| PASS | case T36 automated lint |
| PASS | case T38 automated lint |
| PASS | case T39 automated lint |
| PASS | case T41 automated lint |
| PASS | case T42 automated lint |
| PASS | case T43 automated lint |
| PASS | case T44 automated lint |
| PASS | case T45 automated lint |
| PASS | case T46 automated lint |
| PASS | causal-language detector accepts hedged analytics prose |
| PASS | phase2: all 13 v1.1 brief outputs pass the v1.1 linter (0 errors) |
| PASS | phase2: frozen v1.0.0 baseline files unchanged (sha256 manifest) |
| PASS | phase2: comparison script runs |
| PASS | analytics_compare: sufficient baseline reports position |
| PASS | analytics_compare: warns about YouTube view-definition epochs |
| PASS | analytics_compare: output has no causal language |
| PASS | analytics_compare: small baseline -> hypothesis mode, no 'typical' value |
| PASS | sample_size: 60% vs 65% needs 1468 per arm (hand-computed value) |
| PASS | install.sh: fresh install copies all skills |
| PASS | install.sh: installed skills have bundled scripts/templates |
| PASS | install.sh: second run refuses (exit 3) and changes nothing |
| PASS | install.sh (R14): existing skill dir is never overwritten; nothing else copied |
| PASS | install.sh: --dry-run writes nothing |
| PASS | validator (R15): detects a missing referenced file |
| PASS | validator: detects name/directory mismatch |
| PASS | validator: detects a citation missing from the ledger |
| PASS | claude plugin validate (official) passes on skills/ |

## What these results do and do not show

- They show the helper scripts, installer, validator and fixtures behave as specified, and that the linter's gates fire on the 25 red-team fixtures while accepting the 2 gold fixtures.
- They do **not** show that model-written hooks are good, that Iraqi phrasing is natural, that claims are true, or that any hook performs better on a platform.
- The 49 behaviour specifications in `TEST_CASES.md` (10 held-out) are specifications. Eight were dry-run by the package author in Phase 1 (`DRY_RUNS.md`); in Phase 2 thirteen briefs were run through the workflow and reviewed by the same model (`validation/phase2/`). No independent grader, audience test or live harness was run, so the model-driven workflow is NOT verified end to end.
