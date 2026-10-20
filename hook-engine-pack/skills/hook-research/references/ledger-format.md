# Research ledger format

File: `RESEARCH_LEDGER.csv` (UTF-8, comma-separated, quoted where needed).

| Column | Meaning |
|---|---|
| source_id | `S##` unique id used across the package |
| title, author | as published |
| url | direct URL that was opened (or the best resolver) |
| source_type | peer_reviewed / meta_analysis / official_platform_doc / official_blog / first_party_creator_video / creator_interview_transcript / creator_social_post / book_transcript / standards_body / professional_body / secondary_analysis / community |
| publication_date | as shown; blank if unknown |
| date_accessed | ISO date |
| access_status | full_text / partial_text / abstract_only / transcript_text_third_party / description_only / search_snippet / not_accessed |
| timestamps_verified | `yes` only if timestamps were read in the transcript; else `no` |
| timestamps | e.g. `00:20:09 re-hook after payoff` |
| concept_extracted | the technique/finding |
| evidence_supporting | what supports it (study design, n, official statement) |
| application_20_45s | how to use in a short |
| limitations | contradictions, domain transfer, uncertainty |
| evidence_class | established / practitioner_heuristic / opinion / hypothesis / contested / anecdotal |
| confidence | certain / likely / guess |
| skill_module | which skill uses it |

Grading rubric for a new source: Does it teach a repeatable process? Is access verified? Is the claim testable? Does it conflict with a higher-priority source? Is it transferable to short vertical video, or only long-form?
