---
name: hook-evaluation
description: Critically evaluates hook candidates - applies hard rejection gates, scores with a weighted rubric, runs the first-3-seconds diagnostic for four viewer states, diagnoses why an opening fails (vague, slow, irrelevant, confusing, predictable, unsupported), enforces diversity, and selects three meaningfully different finalists with one recommendation. Use for stage 5 and 7 of the hook pipeline, or whenever the user asks to rank, critique or choose between hooks.
user-invocable: true
---

# Hook evaluation

Scores are a reasoning aid, **not a prediction of virality**. Gates come first; weights come second; diversity third.

## Step 1 - hard gates (any fail = reject or rewrite; never trade off against score)
| Gate | Fails when |
|---|---|
| G1 Factual | a definitive claim is unverified/false/contested without attribution (route: hook-scientific-validation) |
| G2 Medical | implies diagnosis, causation without evidence, or fear/false urgency |
| G3 Promise-payoff | the video cannot deliver what the hook implies; payoff missing/late/different |
| G4 Comprehension | a viewer cannot state the question in ~3 s (visual or verbal) |
| G5 Identity/scope | blurs optometry/ophthalmology, brands as OptiNest, or promotes a product/offer unasked |
| G6 Honesty of form | invented anecdote, misleading demo/before-after, camera-vs-eye misrepresentation |
| G7 Demo-as-test / symptom-to-cause | wording calls a screen or home demo "the test", tells the viewer what their own result means, or names a condition/cause for their symptoms |
| G8 Claim evidence | a hook assertion without `support_quote` + `scope`, resting on a claim that is not `verified`, or containing a number/size/comparator/absolute absent from the quote (see hook-scientific-validation) |
| G10 Payoff readiness | the payoff depends on evidence not yet retrieved (`payoff_ready: false`): may be shown only as conditional and never recommended |
| G9 Gap floor | no curiosity gap: the hook is a bare statement, instruction, or conclusion AND the first frame/on-screen text does not pose the question (`gap_carrier: none`). Statement hooks are allowed only if the frame or text carries an unanswered question |

## Step 2 - rubric (0-5 each; weights are **initial defaults, untested**, editable)
| Dimension | Weight |
|---|---|
| Immediate clarity | 15 |
| Promise-payoff alignment | 14 |
| Curiosity strength (specific, answerable gap) | 14 |
| Relevance to target audience | 12 |
| Specificity | 10 |
| Visual potential | 9 |
| Spoken naturalness (Iraqi) | 8 |
| Novelty | 8 |
| Retention potential (is there a real beat 2?) | 6 |
| Significance (intellectual/practical) | 4 |
Total 100. Weighted score = sum(weight x score/5). Reasoning for the weights: clarity and promise-payoff carry most weight because failures there cause both swipe-aways and disappointment; the order within the rest is a judgement. Ask the creator to re-weight after 10+ published tests. Scientific credibility is a gate, not a score; originality is the diversity rule.
See `references/rubric.md` for 1/3/5 anchors per dimension.

## Step 3 - first-3-seconds diagnostic (four viewers)
Evaluate separately; each answers "what does this viewer have after ~3 s?"
1. **Active scroller** (sound on, thumb moving): is there a readable object/event + a spoken keyword that matches it?
2. **Sound-off viewer:** frame + <= 5 words of text give the question?
3. **Heard-but-not-seen:** the first sentence alone (audio only) - does it still carry a specific question?
4. **Understood, needs a reason to continue:** is there an unresolved, specific question whose answer is promised and plausible?
Mark each Pass / Weak / Fail. Two Fails = rewrite the opening, not the editing.

## Step 4 - failure diagnosis (classify every weak opening)
| Class | Test | Typical fix |
|---|---|---|
| Vague | swap topic - sentence still works | name the object/phenomenon/number |
| Slow | first meaningful event after > ~2 s | cut preamble; start inside the demo |
| Irrelevant | target viewer cannot see themselves | find the recognisable situation |
| Confusing | two questions at once or unfamiliar term | one question; gloss the term |
| Predictable | viewer can state the answer from the hook | withhold the mechanism, not the point |
| Unsupported | claim lacks source | verify, scope, or reframe as a question |
Never "fix" a weak premise with louder sound, faster cuts or extra effects. If the diagnosis is Vague/Predictable at idea level, return to `hook-idea-diagnosis`.

## Step 5 - diversity and selection
- Group candidates by `insight_key`; keep the best per group.
- Finalists must differ in **mechanism**, **insight** AND **payoff** (`payoff_key`: what the viewer walks away with - three hooks that all end in "so blink more" are one video), have low textual overlap, and use at least two different hook shapes (question / statement / instruction / visual-led). Phase-2 testing: 16/30 baseline hooks were statements, 14/30 questions, but within briefs finalists often converged on one payoff.
- If the hook already states the answer (`answer_in_hook: true`), the plan must open a *different* question by beat 2 (`beat2_question`) - otherwise the viewer has no reason to stay. If fewer than three survive, say why and propose new angles.
- Pick three. Recommend one. State the deciding reason and what evidence would flip it. If the highest-scoring candidate has weaker scientific status than another, it cannot be the recommendation.
- Output the finalists as JSON per `templates/candidate_schema.json` and, if scripts are available, run `python3 ${CLAUDE_SKILL_DIR}/scripts/hook_lint.py <file>` (exit 1 = errors); paste only violations. If scripts are unavailable, do the same checks by hand.

## Step 6 - adversarial self-check (before showing anything)
Answer in one line each, per finalist; fix or drop on any "no": (1) Can a stranger state the question in 3 s, muted? (2) What exactly is unanswered after the hook - and does the hook already contain the conclusion (then set `answer_in_hook: true` and write `beat2_question`)? (3) What is the angle that no explainer already uses? (4) Would the Iraqi line be said by a person, or does it contain MSA/calques (flag, native review)? (5) Can the first frame be filmed legibly with the creator's means? (6) Does every beat add information and does the last beat contain the written closing line? (7) Is each claim backed by a quote from its own source with scope? (8) Is anything misleading, generic, confusing or overdramatic? This step is a process aid, not proof of quality: it was added after the baseline showed 21/30 candidates with a defect.

## References
- `references/rubric.md` - anchors, gate examples, selection template, 12 red-team failure modes and the expected behaviour.
