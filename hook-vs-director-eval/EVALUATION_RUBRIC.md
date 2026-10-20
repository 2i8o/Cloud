# Evaluation rubric (fixed before any rating)

Each candidate = one concept (opening line, first frame, curiosity gap, transition, retention sequence, payoff). Rate 1-5 per dimension; rate from the anonymized text only.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| D1 Opening strength | Generic or confusing in the first line | Clear, ordinary | Stops the scroll and is instantly understood |
| D2 Clarity | Viewer cannot tell what the video is about | Mostly clear | Immediate, single idea |
| D3 Curiosity | No open question | Question exists but weak or generic | Specific gap the viewer wants closed |
| D4 Originality | Standard explainer opener | Familiar angle, fresh wording | Angle a typical explainer lacks |
| D5 Retention progression | Beats repeat or are empty | Some new info per beat | Each beat adds information and re-opens or narrows the gap |
| D6 Payoff | Not delivered or weak | Delivered, generic | Delivered, matches the promise, satisfying |
| D7 Scientific accuracy | Wrong | Defensible but loosely supported | Fully supported by the brief's source packet |
| D8 Natural Iraqi Arabic | MSA or unnatural | Mixed | Reads as natural spoken Iraqi, English terms only where appropriate |

## Hard rejection gates (any = REJECT, regardless of scores)
- G-A Unsupported scientific claim (not in the brief's source packet or wrong).
- G-B Misleading promise (hook promises what the video cannot deliver; fear, false urgency, undeliverable clickbait; medical diagnosis or implied self-diagnosis).
- G-C Unresolved central question (the gap opened in the hook is not closed by the payoff).

## Procedure
- Evaluators work independently and do not see the tool name, key, or other ratings.
- Record scores, gate result (PASS/REJECT with gate id), and one-line reasoning in EVALUATOR_RESULTS.csv.
- Disagreement of >=2 points on any dimension, or gate disagreement, is logged with each evaluator's reasoning, not averaged away.
- Separate two flags: concept quality (idea, gap, progression, payoff) vs wording quality (phrasing, dialect). Also flag "attention hook, weak continuation" (D1/D3 >= 4 with D5/D6 <= 2) and "strong plan, weak opening" (reverse).
- Report ties, and briefs where neither tool's candidates pass the gates.
- Linter output and the generating model's own scores are not ratings.
- Minimum for a non-preliminary review: 3 independent human evaluators. Fewer = preliminary.
