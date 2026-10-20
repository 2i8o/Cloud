---
name: hook-research
description: Source-evaluation and ledger-maintenance skill for the hook system - finds, opens and grades sources (primary research, official platform docs, original creator education, secondary analysis, community), extracts techniques with evidence level and limits, and appends verified entries to the research ledger without claiming access that did not happen. Use when the user asks to add/update research, verify a source or link, refresh platform definitions, or study a new creator/paper.
user-invocable: true
---

# Research and ledger maintenance

## Non-negotiables
- **Access honesty.** Record exactly what you opened: `full_text | abstract_only | transcript_text_third_party | description_only | search_snippet | not_accessed`. Never say you watched a video or read a book/course you only saw summarised. If a source is inaccessible, log the limitation and find an alternative.
- No invented quotes, timestamps, statistics, DOIs or URLs. Timestamps only when read in a transcript or on the video itself; otherwise leave blank.
- Quote sparingly (a few words), never reproduce course material or long transcripts. Summarise in your own words.
- Popularity is not causation: view counts and creator fame are not evidence a technique caused success.

## Source priority
1 primary/peer-reviewed - 2 official platform docs and first-party creator education - 3 original lectures/interviews/courses by practitioners - 4 credible secondary analysis - 5 community (label **anecdotal**). Break ties by recency for platform docs, by design quality for studies.

## Procedure
1. State the research question and the decision it serves.
2. Search with several focused queries (English + Arabic where useful).
3. **Open** the source (page/abstract/transcript). Note date, author, type.
4. Extract: concept/technique - supporting evidence - practical application to 20-45 s - limits/contradictions - confidence (مؤكد/مرجح/تخمين) - target skill module.
5. Compare with existing ledger rows; mark agreement/disagreement; do not average opinions.
6. Append a row to `RESEARCH_LEDGER.csv` (columns in `references/ledger-format.md`) and a line to `SOURCE_BIBLIOGRAPHY.md`.
7. Convert to a **decision rule** only if evidence level supports it; otherwise store as a hypothesis to test in hook-analytics.

## Evidence classes
Established (replicated/meta-analytic/official) - Practitioner heuristic - Personal opinion - Untested hypothesis. Never present a heuristic as established.

## Updating existing content
When a source changes a rule in another skill, write the change proposal (file, old text, new text, source id) and let the user approve before editing their installed skills.

## References
- `references/ledger-format.md` - column definitions, access-status values, grading rubric.
