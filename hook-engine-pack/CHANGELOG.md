# Changelog

## 1.1.0 - 2026-10-20 (Phase 2: practical validation)
Evidence: `validation/phase2/` (audit, 13 briefs x 3 finalists before/after, failure patterns, improvement log, experiment plan).
- **Scientific fixes:** removed the unsupported "pin-sized hole" (sources: ~1.2 mm; diffraction below ~0.75 mm) and the viewer-result inference from the pinhole example, fixtures and registry (C13 rewritten); corrected C16 (AAO pages disagree: 5-8% vs "1 in 10"); added registry entries C21-C28.
- **Evidence record (G8):** every claim in a hook needs `support_quote` + `scope`; only `verified` claims may be asserted (`plausible` is no longer allowed in an assertion hook); numbers/sizes/locations/comparators/category shifts must be in the quote.
- **Gap floor (G9), demo-as-test/symptom-to-cause (G7), payoff readiness (G10)**; finalists must differ in mechanism, insight and payoff; hook-shape variety; `answer_in_hook` requires a different beat-2 question.
- **Retention plans:** beat table with real new information and a written closing line; no default five-beat template.
- **Visual brief:** concrete first frame, parameters from sources, participatory-measurement validity check.
- **hook_lint.py:** new checks (E_NO_EVIDENCE_RECORD, E_PARAM_NOT_SUPPORTED, E_NO_GAP, E_DEMO_AS_TEST, E_PAYOFF_DUP, E_NO_PLAN, E_EMPTY_BEAT, E_NO_CLOSING_LINE, E_ANSWER_IN_HOOK_NO_BEAT2, E_RECOMMEND_PENDING, W_COMPARATIVE, W_PAYOFF_PENDING, W_MSA_SOFT, W_SHAPE); the topic-term check E_GENERIC demoted to a warning (precision 3/7 against human review).
- **New helper:** `sample_size.py` (impressions per arm for a two-proportion comparison).
- **Ledger:** +31 sources (S64-S94). **Tests:** 49 case specifications (10 held-out after reclassifying 5 contaminated ones), 25 red-team fixtures, Phase-2 checks (frozen-baseline hash, revised outputs lint clean).
- **Not shown to improve real-world performance** - see `validation/phase2/FINAL_REPORT.md`.

## 1.0.0 - 2026-10-20
- First release: nine skills (hook-engine, hook-idea-diagnosis, hook-writing, hook-retention, hook-visual-design, hook-scientific-validation, hook-evaluation, hook-analytics, hook-research).
- Research ledger of 63 sources (access status recorded per row), generated bibliography, methodology.
- 24-mechanism taxonomy, Iraqi Arabic writing guide, curiosity/attention reference (17 concepts), six retention architectures, claim registry (C01-C20), platform metric dictionary as of 2026-10-20.
- Helper scripts: hook_lint.py (hard gates + diversity), analytics_compare.py (own-baseline comparison, no causal output), install.sh (non-destructive), validate_package.py, build_docs.py.
- 38 test-case specifications (12 held-out), 2 gold and 17 red-team fixtures, runner and results.
- Passed `claude plugin validate` on skills/ (Claude Code 2.1.304).

### Merges from the provisional architecture
- `hook-psychology` merged into `hook-idea-diagnosis` (psychology is only used to diagnose ideas and map curiosity).
- Added `hook-idea-diagnosis` as an explicit stage (idea selection before hook writing).
