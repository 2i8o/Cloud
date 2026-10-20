# Changelog

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
