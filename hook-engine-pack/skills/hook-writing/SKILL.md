---
name: hook-writing
description: Generates and writes short-form hook candidates in natural Iraqi Arabic (with English scientific terms) from a diagnosed idea, using a 24-mechanism taxonomy; produces 10-15 genuinely different candidates internally and returns specs (hook, mechanism, tension, audience, visual, continuation, payoff, risk). Use for stage 4 and stage 8 of the hook pipeline, or when the user asks to write, rewrite, localise or de-genericise a hook or opening line.
user-invocable: true
---

# Hook writing (Iraqi Arabic)

Preconditions: the idea passed `hook-idea-diagnosis` (PROCEED) and every factual claim has a status from `hook-scientific-validation`. If not, stop and route there first.

## Procedure
1. **Pick mechanisms, not wordings.** From `references/taxonomy.md` choose >= 6 mechanisms from >= 4 families (Claim, Question, Visual/Device, Narrative, Evidence, Sensory). Two candidates may share a mechanism only if their underlying *insight* differs.
2. **One insight per candidate.** Each candidate carries an `insight_key` (e.g. `glasses-dont-weaken`, `pinhole-sharpens`). Ten rewordings of one insight = one candidate.
3. **Write 10-15 candidates internally.** For each: the actual hook (<= ~12 spoken words as a *test*, not a law), mechanism id, the question/tension, target audience, visual idea, continuation, payoff promised, principal risk.
4. **Speakability pass** (`references/iraqi-arabic.md`): read aloud; strip MSA calques and English-shaped syntax; prefer verbs and concrete nouns; keep scientific terms in English only where the audience would say them in English (e.g. "20/20", "Snellen", "OCT" is optional).
5. **Prune** duplicates by insight and by sentence pattern; send survivors to `hook-evaluation`. Do not show all 10-15 unless asked.
6. **After the creator picks (stage 8):** write the script beat by beat with `hook-retention`; the final payoff must answer the hook's question in the same terms. Re-verify any number that appears.

## Rules
- Never use: "هل تعلم" as an opener, "اسرار/سر ... " , "لن تصدق", "الحقيقة التي لا يريدك أن تعرفها", "صدمة", fake urgency, invented personal stories. (Linter: `hook-evaluation/scripts/hook_lint.py`.)
- A rhetorical question must be answerable by this video only. Test: swap the topic - if the sentence still works, it is generic.
- Specific question, withheld answer; specific facts only if verified.
- Keep the creator's voice: credible, curious, occasionally humorous - humour never undercuts a safety-relevant fact.
- Do not recommend editing effects to fix a weak premise; fix the premise (see hook-evaluation failure diagnosis).
- Mark all Arabic as **draft for creator review** (Guess-level naturalness; the creator is the native-dialect authority).

## Output spec per surviving candidate
```
id | hook_ar | gloss_en | mechanism | insight_key | tension/question | audience |
first_frame | continuation | payoff | risk | claims[{text, source, status}]
```
(Matches `hook-evaluation/templates/candidate_schema.json`.)

## References
- `references/taxonomy.md` - 24 mechanisms: why they work, when to use, failure modes, ethics, weak/improved/strong examples, optics suitability, combinations.
- `references/iraqi-arabic.md` - dialect markers, MSA-vs-Iraqi table, scientific term handling, anti-patterns, rewrite drills.
- `references/examples.md` - weak -> improved -> strong ladders and a full worked example.
