# Hooks, Curiosity, and Retention

Evidence here is weaker than for editing craft. Tags: **[Obs]** observational data (correlation only), **[Indirect]** adjacent research, **[Heur]** practitioner rule, **[Synth]** this skill's reasoning. No source in this file proves a causal rule; use them to choose *what to test*, and tell the user so. One paper found during research ("Hook Analytics: Optimizing the First 3 Seconds") analysed a *synthetic* 13-video dataset by its own description and is **not** used as evidence.

## 1. What a hook is

A hook = **a promise of a specific payoff + an open question the viewer wants closed**, delivered through whatever channel is fastest: an image, a line, on-screen text, or an action. It is not an attention grab; grabs without a promise produce a click and an exit.

Two tests, both must pass:
- **Curiosity test:** can the viewer state the question in one sentence after 3 seconds? ("Why does the straw look broken?")
- **Contract test:** does the video resolve *that* question, at the scope promised? (`storytelling-and-editing.md` section 3)

## 2. Hook channels (use at least one; combine deliberately)

| Channel | Strength | Risk |
|---|---|---|
| **Visual question** (an impossible-looking image, an unresolved action) | Works muted; universal | Image must be real/accurate, and must reappear in the payoff |
| **Spoken promise** (a plain question or surprising claim) | Specific, fast | Clickbait phrasing; over-claiming |
| **On-screen text** | Sound-off viewers; reinforces promise | Clutter; unreadable in safe-area; duplicating narration word for word |
| **Result-first** (show the outcome, then how) | Clear payoff promise | Gives away the answer if the outcome *is* the answer |

[Obs] In a 1,272-video sample of business/creator accounts, videos with on-screen hook text earned about 1.8x the account's typical views; spoken-only hooks about 0.6x; hook length (words) showed no clear effect. Treat as a reason to *test* text + visual together, not a rule. A first frame showing "a real place" did better than "a product close-up" in the same data - consistent with "show a situation, not an advert." [Obs]

## 3. Hook patterns (choose by content, not by fashion)

| Pattern | Use when | Failure mode |
|---|---|---|
| Paradox / illusion ("this looks impossible") | A real perceptual/physical surprise exists | Surprise is faked or not explained |
| Demonstration-first | The phenomenon is visual and quick | Demo is unclear without context |
| Direct question | Audience already has the question | Generic question with no stakes |
| Counter-intuitive claim | Claim is *true* and verifiable | Claim is exaggerated; payoff weaker than claim |
| Result-first / reverse | Process is the interesting part | Result is dull |
| Personal stake ("I tested...") | Creator really did the test | Staged "experiments" |
| Mystery object / partial reveal | One object can carry curiosity | Never revealed, or revealed in a way that disappoints |
| Misconception flip ("you've been told X - test it") | A common belief is demonstrably wrong or incomplete | Do not *state* the false premise as fact in the hook (show it as the viewer's impression); no strawman; needs evidence the viewer can see; label the premise as common belief |

## 4. Integrity gate (non-negotiable for factual / health-adjacent content)

1. The hook's strongest claim must be supported by a **named source** at the *same scope* (population, conditions, strength).
2. No fear-based framing ("this is destroying your eyes") unless the evidence supports the harm, the magnitude, and the audience's exposure.
3. If the honest answer is "unknown/debated," the promise is the *explanation of the debate or the illusion*, not a secret answer. Say so in the first beat if the video's honest result is "we don't fully know."
4. Hook visuals must not be physically impossible or misleading (e.g., a diagram that contradicts the physics, fake before/after). Cut the hook rather than ship it.
5. Medical content: educational, not diagnostic. Avoid individual diagnosis claims.
6. **Exclusions are claims.** "It's not dirt, it's not your breath" needs the same sourcing and scope as "it's condensation." Hooks love dismissing the obvious answer; verify each dismissed answer is actually wrong in the scenario shown (or soften to "not only").
7. Mark in the plan which lines are **verified**, which are **to verify**, and who verifies them; do not leave that implicit.

## 5. Structure that sustains curiosity

[Synth; each element testable with the platform's retention graph]

```
0-1.5 s   First frame + first line carry the question (no logo, no throat-clearing)
1.5-4 s   Stakes/context: why the obvious answer fails (open loop stays open)
4-?  s    Evidence beats: each one answers a sub-question and opens the next
peak      Turn / payoff: the answer, visually proven
+hold     Let it land (see storytelling section 4)
end       One-line takeaway or a callback to the first frame
```

- **Open-loop discipline:** every open loop is closed before the end, in the reverse or natural order. A loop left open is a broken promise.
- **Re-hook:** where retention normally dips (visible in analytics), insert a new question, number, or visual state. Not a new effect.
- **Callback ending:** end on the first frame's object in its new, understood meaning. Supports rewatch without trickery. [Heur]

[Indirect] Peak-end: people judge experiences largely by the most intense moment and the end; a short-video recommender paper (RecSys 2025) built a retention model on this. It supports designing a deliberate peak and a strong final beat; it does not prove how a specific video should be cut.

## 6. Endings

[Obs] In the same 1,272-video sample: recap/summary endings about 1.5x typical views; soft invitations like "let me know below" about 0.6x; captions ending in a question were low (small n). Use: end on the payoff or a one-line takeaway; skip generic prompts. Do not claim causation.

## 7. 10-second hook template (timing at 30 fps)

| Time | Visual | Sound | Text | Job |
|---|---|---|---|---|
| 0.0-0.5 s | The impossible/surprising image, already in motion (frame 0 = interesting) | Ambient or a single sync'd hit; no music swell | none yet or 2-4 words | Image -> question |
| 0.5-3.0 s | Hold or slow push; one clear subject | Voice states the question plainly | Question as text, 1 line, big | Question stated in two channels |
| 3.0-6.0 s | Cut to the first evidence or a "wait, look" frame | Silence/ambience dip, then voice | Optional label | Raise stakes: why the obvious answer fails |
| 6.0-8.5 s | The pivot: teaser of the answer's mechanism | Sound design begins (single rise) | Keyword | Promise of resolution |
| 8.5-10.0 s | Transition into main content, motivated by the same object | Hit on the cut or direct cut | - | Hand-off without a gimmick |

Check: mute -> still understandable? Audio only -> the question still audible? Remove the logo/intro card: nothing lost?

## 8. Metrics to look at (when platform analytics exist)

- Viewed-vs-swiped at ~3 s; average % viewed; the retention curve's cliffs (hook failures) and slopes (pacing failures).
- Interpret by position: early cliff -> promise unclear; mid-slope -> repetition/low density; end drop -> payoff delivered early or ending weak.
- Change one thing per version; otherwise nothing is learned.

## 9. Common mistakes -> corrections

| Mistake | Fix |
|---|---|
| Slow logo/intro before the question | Delete it; brand on the end frame or as a persistent small mark |
| Hook is a statement of the topic ("Today: refraction") | Turn into a question or a surprising image |
| Hook and payoff scope differ | Rewrite the hook to the actually-proven scope |
| Three hooks stacked | One question; make the others sub-questions later |
| Text duplicates narration exactly | Text = the question/keyword; narration = the detail |
