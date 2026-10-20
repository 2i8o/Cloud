# Quickstart - first use in 5 minutes

1. **Install** (see README): `bash scripts/install.sh`. Open Claude Code in any folder.
2. **Give it a topic, not a hook.**
   ```
   /hook-engine  موضوع: شنو يعني 20/20؟   مدة 30 ثانية، ريلز، جمهور: عراقيين 18-40
   ```
   Add what you already have: evidence, props, a draft hook, the platform.
3. **First reply = a verdict on the idea.** One of: PROCEED / RE-ANGLE / RESEARCH / REJECT. If it says the idea is weak, take that seriously: no wording fixes it. Pick one of the offered angles or give a new one.
4. **Then you get exactly three finalists** that differ in mechanism *and* insight, each with: hook text, mechanism, the viewer's question, first frame, continuation, payoff, strength/risk, confidence (مؤكد / مرجح / تخمين), and claim status (verified / plausible / unverified).
5. **Choose.** Reply with the letter (or ask for changes). Only then does it write the full script and the beat-by-beat retention plan.
6. **Before publishing:** check every claim marked *unverified* or *needs professional review*; read the Iraqi lines aloud and fix anything unnatural (the model's dialect is a draft).
7. **After publishing:** log the video (`hook-analytics/templates/experiment_log.csv`), compare only with your own comparable videos:
   ```bash
   python3 ~/.claude/skills/hook-analytics/scripts/analytics_compare.py my_videos.csv VIDEO_ID
   ```

## Other entry points
- Audit a hook: `/hook-engine audit: <your hook>`
- Why do viewers swipe away?: paste your first-3-seconds description and the stayed-to-watch / skip-rate numbers.
- Check a claim: `/hook-scientific-validation` + the sentence.
- Update research: `/hook-research` + a link.

## Rules of thumb it enforces
- Idea first, wording second. - One insight per hook; three finalists must be genuinely different.
- A hook is a promise; the payoff is written first. - Show the question in frame 1; sound only reinforces.
- No fear, no diagnosis, no invented stories, no product pushes. - Your own baseline beats any "benchmark".
