---
name: hook-idea-diagnosis
description: Decides whether a video IDEA is worth hooking before any hook is written - returns PROCEED, RE-ANGLE, RESEARCH or REJECT - then maps the viewer's curiosity (what they believe, what they misunderstand, what accurate surprise closes the gap). Use for stages 2-3 of the hook pipeline, or when the user asks "is this idea good?", "why is this topic weak?", "which angle?". Also holds the curiosity/attention psychology reference.
user-invocable: true
---

# Idea diagnosis and curiosity mapping

A weak idea cannot be rescued by dramatic wording. Diagnose the idea first.

## Step 1 - one-sentence insight test
Fill this exactly:
> Most [audience] think **X**. Actually **Y**, because **Z**. You can see it by **D** (demo/visual/evidence).

- Cannot fill X, Y, Z or D -> idea is under-developed -> RESEARCH or RE-ANGLE.
- Filled but unremarkable ("eyes are important", "20/20 is good vision") -> **idea is weak**, not the hook.
- Filled and remarkable but candidate hooks do not land -> **hook is weak** (go to hook-writing).
State which of the three you found in the first line of your answer.

## Step 2 - score the idea (0-2 each; see `references/idea-gate.md` for anchors)
Audience demand - relevance to the target viewer - novelty/distinctiveness - strength of insight - curiosity-gap potential - demonstrability - scientific credibility - practical usefulness - emotional/intellectual significance - payoff deliverable in the time - fits 20-45 s - similarity to saturated content (inverse) - recognisable opening image - evidence and production resources.
Scores are a reasoning aid, not a prediction of performance. Say so.

## Step 3 - decision gate
| Verdict | When | Output |
|---|---|---|
| **PROCEED** | specific question a target viewer holds or can be led to hold + accurate non-obvious answer + payoff <= duration + verifiable | go to curiosity map |
| **RE-ANGLE** | topic generic/saturated, too broad for the time, or no visible mechanism - but a sharper mechanism, demonstration or question exists | 2-3 concrete stronger angles (each with X/Y/Z/D) |
| **RESEARCH** | central claim plausible but unverified, or a number/threshold is needed | exact claims to verify + route to hook-scientific-validation |
| **REJECT** | central claim unsupported or false; payoff impossible without distortion; fear is the only engine | say why in one line; offer a truthful neighbouring idea |

If more than one verdict applies, report the most blocking one first in this order: REJECT > RESEARCH > RE-ANGLE > PROCEED, and list the others as follow-ups (e.g. "RE-ANGLE, then RESEARCH the chosen angle").

## Step 4 - curiosity map (only after PROCEED)
Write six lines: (1) what the audience believes/knows, (2) what they likely misunderstand, (3) what relevant information is missing, (4) the accurate, surprising insight that closes the gap, (5) what the viewer should expect to learn, (6) the evidence or demonstration that delivers it.
Check the **partial-knowledge rule**: the hook should touch something the viewer already half-knows (e.g. "20/20", glasses, screens). Curiosity in lab studies peaks at intermediate confidence and falls when people know nothing or know everything (Kang 2009; Kidd & Hayden 2015) - **Likely** for short video; transfer from lab trivia is untested.

## Guardrails
- Never invent audience demand. Mark signals `verified` or `inferred`.
- Popularity of a topic is not proof of a claim.
- Prefer ideas the image can carry, but do not reject a strong idea only for lacking a demo.
- Hand off claims to `hook-scientific-validation` before any definitive hook is written.

## References (read only when needed)
- `references/idea-gate.md` - scoring anchors, worked weak-vs-strong idea examples.
- `references/curiosity-psychology.md` - 17 concepts: what evidence supports, what is overstated, how to use, when it fails, good/bad Iraqi examples.
