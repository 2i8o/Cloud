# Research methodology

Date of research: 2026-10-20 (Claude Code 2.1.304 environment; web access through search/fetch tools, no direct browser).

## 1. Principles
- Open before citing. Each source in `RESEARCH_LEDGER.csv` carries an `access_status` stating what was actually opened (`full_text`, `partial_text`, `abstract_only`, `transcript_text_third_party`, `description_only`, `search_snippet`). Nothing was upgraded after the fact.
- Evidence class is separate from fame: `established` (replicated / meta-analytic / official), `practitioner_heuristic`, `opinion`, `hypothesis`, `contested`, `anecdotal`. View counts and creator popularity were never treated as proof of causation.
- Priority order used: (1) peer-reviewed / meta-analyses, (2) official platform documentation and first-party creator education, (3) original lectures, interviews and courses by practitioners, (4) credible secondary analysis, (5) community (labelled anecdotal).
- Confidence labels: certain / likely / guess (mapped to مؤكد / مرجح / تخمين in outputs).

## 2. Tools and procedure
1. Environment audit: inspected `~/.claude/skills` (existing: session-start-hook; synced claude.ai skills incl. the creator's profile skills, read only), Claude Code 2.1.304, Python 3.13.
2. Claude Code skill format taken from the official Skills documentation (frontmatter fields, 1,536-char description cap, 500-line guidance, `${CLAUDE_SKILL_DIR}`, live change detection, post-compaction retention of the first 5,000 tokens).
3. Search by track (A-J) with several focused queries; fetch of pages/transcripts through a web-search/fetch connector (Exa) and WebSearch/WebFetch; peer-reviewed metadata via a scholarly search connector (Consensus) and publisher/PubMed/PMC pages.
4. Direct HTTP clients (curl) were blocked by the sandbox proxy for most hosts; `support.google.com` could not be reached by the WebFetch tool (DNS failure) but YouTube Help pages were retrieved as excerpts through the Exa fetch/search tool.
5. Extraction into the ledger: concept, supporting evidence, application to 20-45 s, limitations, class, confidence, target skill.
6. Synthesis into decision rules only where evidence class allows; otherwise stored as hypotheses with an experiment (hook-analytics).

## 3. Per-track coverage
| Track | Covered by | Strength |
|---|---|---|
| A Creator education (Hormozi, Film Booth, MrBeast/Team Beast, Galloway, Colin & Samir, YouTube/Creator Insider) | S05-S07, S48-S58 | transcripts/snippets, **no video watched**; Hormozi limited to a book chapter; MrBeast via third-party interview transcripts; Team Beast internal documents deliberately excluded |
| B Psychology of curiosity | S11-S31 | abstracts/partial text; transfer to feeds untested |
| C Taxonomy | synthesised (hook-writing) | design judgement + sources above |
| D First 3 seconds | S03, S06, S10, S25-S26, S52 | mostly heuristics; four-viewer diagnostic is a design of this package |
| E Retention architecture | S27, S48-S56 | practitioner heuristics; lab support only for story engagement |
| F Idea selection | S52 (idea funnel) + package gate | heuristic; weights untested |
| G Language | S59-S60 + model knowledge | **no script corpus**; naturalness unverified |
| H Visual/audio | S23-S25, S42-S43 | multimedia-learning lab results; camera-vs-eye rule from optics reasoning |
| I Scientific accuracy | S32-S47 | AAO/AOA/ISO/PMC excerpts; professional review still required |
| J Platform analytics | S01-S10, S61 | YouTube first-party; Instagram via quotes; TikTok secondary only |

## 4. Verified platform facts that change how results must be read
- YouTube Shorts: since 2025-03-31 views = starts or replays with no minimum watch time; the old metric is engaged views; from 2026-08-24 views count from the first frame across all formats (S02, S04, S05). Stayed to watch, engaged views and average view duration/percentage are defined in S01.
- YouTube does not publish the number of seconds behind "initial seconds" or any benchmark (S01, S05, S06).
- Instagram replaced view rate with skip rate (first 3 s) and added a Retention chart in Aug 2025 (S10).

## 5. Contradictions and how they were handled
See "Disagreements and tensions recorded" in `SOURCE_BIBLIOGRAPHY.md`. Policy: record both sides, label the working rule as a hypothesis, and make the creator's analytics the arbiter.

## 6. Known gaps (research not completed)
- No TikTok first-party documentation; Meta help pages not opened.
- No full-text reading of core psychology papers; no replication check beyond the Zeigarnik meta-analysis.
- No Arabic/Iraqi short-video corpus; no measurement of dialect naturalness.
- No evidence about Iraq-specific optometry regulation or prevalence figures.
- Creator videos were not watched; ranking of creators is by usefulness of extracted, process-like material (see below), not by fame.

## 7. Ranked learning path (usefulness x credibility x accessibility x relevance to 20-45 s educational optics)
1. YouTube first-party definitions and Creator Insider (S01-S07) - authoritative on what is measured.
2. Ed Lawrence (S49-S51, S58) - repeatable script-level retention diagnostics (re-hook after payoff, three drop types); long-form origin.
3. Paddy Galloway (S52) - idea filters (core/casual/new, feasibility, packaging test); thumbnails/long-form origin.
4. Colin & Samir (S53, S55-S57) - causal beats ("but/therefore"), three acts, caution about transfer.
5. MrBeast interviews (S53, S54) - first-seconds clarity and side stories; metrics targets not transferable.
6. Alex Hormozi (S48) - hook/retain/reward as a promise-reward contract; least procedural for optics.
