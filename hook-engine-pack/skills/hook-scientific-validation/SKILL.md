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
   **Evidence record per claim (mandatory for any claim in a hook):** `support_quote` (<= 15 words copied from THAT source) and `scope` (population, setting/country, study design, and every parameter the claim states - size, distance, dose, time, age). A source ID alone is not evidence: Phase-2 testing found a claim citing the wrong source (a colour-vision page for a lens analogy) and a hook whose key parameter ("pin-sized hole") was in no source (the sourced clinical pinhole is ~1.2 mm; below ~0.75 mm diffraction makes vision worse).
4. **Assign status**: `verified` (the quote above supports the exact wording AND scope) - `plausible` (consistent with sources but not checked) - `unverified` - `contested` (credible bodies disagree) - `false`.
   **A hook may state an assertion only if every claim in it is `verified`.** `plausible`/`unverified` claims may appear only in a hook phrased as a question or test the video resolves (set `claim_form: question`), never as an assertion. Every number, size, location/direction ("in the middle of your vision"), comparator ("more than...") and absolute ("never/only/all") in the hook must appear in the quote or scope; otherwise remove it. A **category shift** is a scope violation too (source says "occasional overnight use" -> hook may not say "naps"; source says "may put eyes at greater risk" with no stated comparator -> hook may not say "more than clear lenses").
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
3. No diagnosis from a screening observation or a screen demo. Use "this is not a diagnosis; see an eye professional if ...". Do not name a condition or cause for the viewer's own symptoms or demo result ("your result means ..."); hedging ("your eyes may water because...") does not exempt it - state it as general knowledge in the third person ("excess tearing sometimes comes from dryness"), and never call a screen demo "the test" ("هذا نص الفحص"). Reassurance ("it's normal, not a disease") needs its caveat in the same beat (when to be examined; earlier/atypical onset).
   Disease-related findings (e.g. scotomas, infection risk multipliers) may be reported only with their population/design in the beat and an action; keep disease words out of the hook unless the evidence is attributed there.
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
