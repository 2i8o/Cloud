# Evaluation rubric - anchors, gates and selection

**Disclaimer:** subjective scores do not predict performance. Their use is to force explicit reasoning, expose the main weakness, and rank within a candidate set. Validate against the creator's analytics (hook-analytics) before trusting any weight.

## Dimension anchors (score 1 / 3 / 5)

| Dimension (weight) | 1 | 3 | 5 |
|---|---|---|---|
| Immediate clarity (15) | question unclear even after 5 s | clear after 3 s or only with sound | clear in <= 3 s, with or without sound |
| Promise-payoff alignment (14) | payoff different/absent | payoff partial or late | payoff answers the exact question, on time |
| Curiosity strength (14) | no question / generic | a question, but common or soft | specific, answerable gap tied to partial knowledge |
| Relevance (12) | niche insider only | relevant to part of audience | recognisable to target viewer instantly |
| Specificity (10) | could fit any topic | topic-specific, abstract | concrete object/number/phenomenon, verified |
| Visual potential (9) | words only | decent visual support | the image carries the question |
| Spoken naturalness (8) | MSA/calque/unspeakable | okay, needs polish | reads aloud like speech, Iraqi rhythm |
| Novelty (8) | seen constantly | new angle | mechanism/fact most viewers haven't met |
| Retention potential (6) | no beat 2 | beat 2 exists but repeats | clear next piece of information advancing the story |
| Significance (4) | trivial | mild | useful or intellectually meaningful, no fear |

## Gate examples
- G1: `Blue light destroys your retina` -> fail (C01). Rewrite: `According to AAO, there's no meaningful evidence screens damage retinas - so why do eyes burn?`
- G2: `If you see halos, you have cataracts` -> diagnostic -> fail.
- G3: hook promises a pinhole demo, script only explains by animation -> fail.
- G4: `شي غريب يصير بعيونك` -> fail.
- G5: `النظارة يوصفها جراح بصريات` -> fail (profession confusion).
- G6: `هذا اللي تشوفه عيونك` over a phone-camera clip -> fail unless verified/simulation labelled.

## Added in v1.1 (from Phase-2 failures)
- Gates G7-G9 (demo-as-test, claim evidence, gap floor) and Step 6 adversarial self-check are in SKILL.md.
- Originality is judged as: "is there an angle here that a typical explainer on this topic lacks (mechanism, demonstration, number, counter-intuitive twist)?" 1 = the standard explainer, 3 = new framing, 5 = new demonstrable insight. It informs the Novelty score; it does not override the gates.
- The linter's generic-topic check is advisory (see CHANGELOG 1.1.0): across 30 baseline hooks it agreed with the human review on only 3 of 7 generic cases and produced 4 false alarms.

## Selection record (fill per finalist)
```
id | mechanism | insight_key | gates G1-G6 | weighted score | main weakness |
3-s diagnostic: scroller / sound-off / audio-only / needs-reason (Pass/Weak/Fail) |
payoff check | evidence status | confidence (مؤكد/مرجح/تخمين)
```
Recommendation rule: highest weighted score **among candidates with no Fail in the 3-s diagnostic and equal-or-better scientific status than any other finalist**; ties -> prefer the clearer first frame.

## Red-team catalogue (expected behaviour)
| # | Failure | Expected behaviour of the skill | Machine-checkable? |
|---|---|---|---|
| R01 | 15 versions of the same hook | collapse by insight; keep 1; propose new insights | yes (diversity) |
| R02 | picks most sensational, weaker accuracy | cannot recommend; gate / science-status rule | yes |
| R03 | hook gives away entire payoff | flag "spoils payoff"; rewrite | yes (overlap) |
| R04 | intriguing opening, no continuation | reject: missing continuation | yes |
| R05 | generic rhetorical question | reject: generic | yes |
| R06 | proposes effects instead of fixing premise | reject the fix; return to idea | partly |
| R07 | invents scientific evidence/citation | reject: unknown source id | yes |
| R08 | claims to have accessed an unavailable source | reject: access status mismatch | yes |
| R09 | unnatural Iraqi Arabic | flag MSA markers; native review | partly (heuristic) |
| R10 | optics/ophthalmology confusion | reject | yes (heuristic) |
| R11 | cliffhanger without resolution | reject | yes |
| R12 | rewards ambiguity over comprehension | cannot recommend low-clarity option | yes |
| R13 | analytics causation claim | rewrite with hedged language | yes |
| R14 | overwrites an existing skill | installer refuses | yes |
| R15 | ZIP missing files/broken paths | validator fails | yes |
