---
name: hook-scientific-validation
description: Scientific and medical-educational safety gate for optometry, optics and vision claims in hooks and scripts - verifies each claim against primary/official sources, caps the wording at the evidence strength, separates optometry from ophthalmology, blocks fear framing and diagnostic language, and flags claims needing professional review. Use before any definitive hook is written, whenever a number/health implication/standard is mentioned, and when the user asks "is this true?" or "can I say this?".
user-invocable: true
---

# Scientific validation gate

**Rule 0:** A hook with an unverified definitive claim is rejected - or rewritten as a question/hypothesis the video resolves with evidence. Never invent a source, quotation, DOI, number or study. If you cannot open a source, say so and keep the claim `unverified`.

## Procedure
1. **Extract every claim** - spoken hook, script, on-screen text, captions, thumbnail text, demo implications.
2. **Classify**: F fact - M mechanism - N number/statistic - H health implication - P professional scope - S standard/definition.
3. **Source it** (priority: systematic review/meta-analysis > RCT/cohort > official professional body (AAO/AOA/WHO) > standards bodies (ISO) > textbooks/StatPearls > reputable journalism; community = anecdotal). Open the source page; confirm the source supports the *exact* wording, population, date.
4. **Assign status**: `verified` (read source supports exact wording) - `plausible` (consistent with sources but not read/checked) - `unverified` - `contested` (credible bodies disagree) - `false`.
5. **Cap the verb** by evidence (table below).
6. **Run the safety rules** (below). Any failure = REWRITE or REJECT.
7. **Flag for professional review** when triggered (below). Say which claim and why.
8. Return a claim table: `claim | class | source id/URL | status | wording cap | review flag`.

## Wording ceilings
| Evidence | Allowed | Not allowed |
|---|---|---|
| Meta-analysis/RCTs | "on average reduces/slows ..." (state population, size) | "cures", "prevents" without outcome evidence; extrapolating to other ages |
| Observational/cross-sectional | "is associated with" | "causes" |
| Lab/cell/animal | "in cells/animals ..." | statements about people |
| Official body position | "according to AAO/AOA ..." (attribute) | stating it as universal law |
| Narrative review | "a 2023 review found no consistent evidence" | "proven useless" |
| Expert quote / single clinician | attribute and flag as quote | generalise to a population |
| Standard text | describe what the standard says and its stated scope | imply clinical/legal certification (e.g. ISO 8596 is neither a clinical measurement nor blindness-certification standard, S42) |

## Safety rules
1. No exaggerated health risk to create curiosity; no manufactured fear; no false urgency.
2. No implication that a behaviour causes a medical condition unless evidence supports causation. (AAO: screens do not damage eyes; discomfort relates to reduced blinking and how screens are used, S32, S33, S35.)
3. No diagnosis from a screening observation or a screen demo. Use "this is not a diagnosis; see an eye professional if ...".
4. No misleading before/after (see hook-visual-design).
5. **Optometry != Ophthalmology.** AAO: ophthalmologists are medical/osteopathic doctors who can perform eye surgery; optometrists hold an OD and provide primary vision care, exams, lens prescription and, in some places, medication for certain conditions (S36). AOA describes doctors of optometry as primary eye-health providers (S37). Scope of practice varies by jurisdiction and is **contested between the professional bodies** (S36 vs S37, S38) - never assert scope-of-practice facts for Iraq without local verification. Never call an optometrist a surgeon; never attribute surgery to optometry; do not use "طبيب عيون" for the creator unless that is his verified title.
6. Preserve standards' meaning (acuity notation, ISO scopes, legal vision thresholds vary by country; AAO's "20/40 for unrestricted licence in most states" is US-specific, S44).
7. Reject an attention-grabbing claim that cannot be substantiated; offer a truthful neighbouring hook.
8. Cite the evidence supporting every scientific statement in the creator-facing notes (short: id + year).
9. Separate evidence / interpretation / speculation in the claim table.

## Professional-review triggers
Paediatric vision or myopia treatment advice - any medication/atropine - contact-lens hygiene and infection - red-flag symptoms (sudden vision loss, flashes/floaters, pain) - driving or occupational vision thresholds - eye-health claims from photos - supplements - post-surgical issues - scope-of-practice or regulatory statements - anything that tells a viewer to stop or delay care. Output: "Needs review by [optometrist/ophthalmologist] before publishing". Educational content may state the standard guidance, but must not replace care.

## Claim registry (verified in this project; re-check dates before each use)
See `references/accuracy-rules.md` for the registry (AAO blue-light, digital eye strain, 20-20-20, glasses dependence, 20/20 meaning, pinhole, outdoor time, myopia-control lenses, colour blindness facts) with exact allowed wording and the myths that still need research.

## Disclosure lines (Iraqi draft)
`هذا مو تشخيص — إذا عندك أعراض مستمرة راجع مختص نظر.` / `الأرقام متوسط دراسات، مو نتيجتك الشخصية.`
