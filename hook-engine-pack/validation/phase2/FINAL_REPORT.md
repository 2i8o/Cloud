# Phase 2 final report - practical validation of Hook Engine (v1.0.0 -> v1.1.0)

## 0. Bottom line (uncomfortable part first)
- **v1.1.0 is more disciplined; it is not shown to be more effective.** Everything below is the model grading itself. No real audience, no independent grader and no creator analytics were involved (none exist in the repository). Claims about "stronger hooks" are therefore **hypotheses** until the experiment in `EXPERIMENT_PLAN.md` is run.
- **v1.0.0 was weaker than its test results suggested.** Its 47 passing machine checks said almost nothing about hook quality: against 39 frozen baseline finalists, its own linter flagged 8 of the 26 that the review judged weak (31%). The recommended pinhole hook contained an unsupported physical parameter ("pin-sized hole": clinical holes are ~1.2 mm; below ~0.75 mm vision gets *worse*) and a lay-viewer inference ("sharper means refractive error, not disease") that the sources do not license. The error sat in 21 files because examples were reused as fixtures.
- **My own first v1.1 draft failed the new linter on 31 of 39 finalists**, and my review of it then found 8 more substantive defects the linter cannot see. The process catches errors; it does not make the author correct on the first try.

## 1. Original vs revised evaluation results
Method: 10 realistic optics briefs (B01-B10) + 3 held-out briefs (B11-B13, baseline frozen before any change). Three finalists each, with retention plan, curiosity gap, payoff and source records. Reviewed on clarity, curiosity, originality, Iraqi naturalness, visual demonstrability, continuity (hook -> payoff), scientific accuracy and misleading/generic/confusing/overdramatic flags. Scores 1-5, assigned by the generating model (`review/*.py`). **Iraqi naturalness cannot be scored by it and is excluded from the headline.**

| | v1.0.0 (B01-B10, n=30) | v1.1.0 (B01-B10) | v1.0.0 held-out (B11-B13, n=9) | v1.1.0 held-out |
|---|---|---|---|---|
| clarity | 3.83 | 4.00 | 3.67 | 4.00 |
| curiosity | 2.87 | 3.37 | 2.67 | 3.22 |
| originality | 2.80 | 3.43 | 3.00 | 3.56 |
| visual demonstrability | 3.23 | 3.47 | 3.33 | 3.67 |
| continuity | 3.50 | 3.80 | 3.67 | 4.00 |
| scientific accuracy | 3.37 | 3.70 | 3.67 | 4.22 |
| mean of those six | 3.27 | 3.63 | 3.33 | 3.78 |
| finalists with >= 1 flag | 26/30 | 13/30 | 8/9 | 3/9 |
| weak finalists (any score <= 2 or >= 2 flags) | 21/30 | 6/30 | 5/9 | 0/9 |
| **Objective counts (not self-scored)** | | | | |
| hook assertions resting on non-verified claims | 4 | 0 | 1 | 0 |
| plans ending in an empty "Close" | 27/30 | 0/30 short closings | 9/9 | 0/9 |
| hook claims carrying quote + scope | not recorded | 33/33 | not recorded | 9/9 |

(`review/compare_versions.py`, `review/lint_vs_review.py`.) Interpretation, with the limits that matter:
- The **objective** rows improved because the rules now demand them - that is compliance, not proof of quality.
- The **scored** rows improved, but the reviewer wrote the new rules, knew the rubric and generated the outputs. My first scoring of v1.1 assigned far fewer flags than the same standard produced for v1.0; I redid it with the v1.0 standard (`review_v11.py`, "consistency pass"). Expect an independent expert to find more defects than I did (known soft spots: B06-C moon size not in the source, B07-A dated source, B10 trade-journal evidence, B08 US data).
- **Held-out is weak:** the baselines were frozen first, and registry entries for those topics were withheld until after the test, **but I had read their baseline defects before writing v1.1.** Treat B11-B13 as a sanity check, not a blind test.
- Absolute level: v1.1 curiosity averages ~3.3/5 and originality ~3.5/5; 5/39 finalists still score originality <= 2 and 7 carry SCOPE flags (single-source, US-only, dated or practitioner evidence).

## 2. The 10 test briefs and their three finalists (v1.1.0)
Full before/after tables with scores and flags: `BRIEFS_AND_FINALISTS.md`. Full retention plans: `revised/Bxx.md` (v1.1) and `baseline/Bxx.md` (v1.0, unchanged). Every finalist has a gap, first frame, payoff, beat table with a written closing line, and an evidence record (claim, source id, quote, scope).

| Brief | Recommended | Finalist hooks (v1.1.0) - mechanism - payoff |
|---|---|---|
| B01 Pinhole demo (YouTube Short, 30 s) | A | **A** نفس السطر. نفس الكاميرا. شنو تغيّر؟ - M11 - aperture-shrinks-blur<br>**B** تصغّر ثقب الورقة تشوف أحدّ… وتصغّره أكثر يصير أسوأ. ليش؟ - M05 - why-not-smaller<br>**C** نفس الثقب يحسّن النظر عند ناس، ويخليه أسوأ عند ناس آخرين. - M16 - clinical-clue-and-its-limits |
| B02 Why eyes burn after reels (Instagram Reel, 25 s) | B | **A** ليش عيونك تحرگ بعد ريلز… ومو بسبب الضوء الأزرق؟ - M02 - cause-is-use-not-light<br>**B** طالع بوجه واحد يتفرج ريلز دقيقة… وعدّ كم مرة يرمش. - M10 - your-own-count-vs-normal<br>**C** قاعدة ٢٠-٢٠-٢٠: تنفع لو بس نصيحة؟ - M08 - what-is-recommended-vs-proven |
| B03 Blue-light glasses (TikTok, 30 s) | A | **A** شلون تسوي تجربة على نظارة الضوء الأزرق… واللابس يعرف إنها الحقيقية؟ - M20 - why-trials-are-weak<br>**B** قبل النوم، المشكلة مو نظارتك. هي ساعات الشاشة. - M16 - screen-timing-for-sleep<br>**C** الضوء الأزرق من شاشتك يضر شبكيتك؟ الدليل لحد هسه ما يقول هيچ. - M08 - no-meaningful-link-to-retina |
| B04 Myopia-control lenses for parents (YouTube Short, 40 s) | B | **A** ٢٣ دراسة على ١٣ ألف طفل… شنو يعني "تبطّئ" قصر النظر؟ - M18 - what-slowing-means<br>**B** تقليل قوة نظارة الطفل ما يبطّئ قصر النظر… وممكن يسرّعه. - M02 - use-the-full-prescription<br>**C** وقت العطلة برا البيت… هل يغيّر قصر النظر عند الطفل؟ - M08 - outdoor-time-evidence |
| B05 Eye chart letters (Instagram Reel, 25 s) | C | **A** ليش سماكة خط الحرف بلوحة الفحص بالضبط خُمس ارتفاعه؟ - M05 - detail-equals-one-arcminute<br>**B** السطر يُحسب مقروء إذا قريت أكثر من نصف حروفه — حسب معيار ١٩٨٤. - M01 - how-scoring-works<br>**C** ليش فحص النظر يصير على ٦ أمتار؟ - M08 - relaxed-focus-at-distance |
| B06 Blind spot (TikTok, 30 s) | A | **A** غمّض عينك اليسار، مدّ إيدك اليمين، وطالع بظفر إبهامك… خنصرك راح يختفي. - M10 - where-the-blind-spot-is<br>**B** بكل عين اكو بقعة بدون خلايا مستقبلة… ليش ما تشوفها؟ - M04 - brain-fills-in-the-gap<br>**C** البقعة العمياء بعرض ٦ درجات… تخبّي ١٢ قمر! - M01 - size-comparison |
| B07 Colour-vision plate tests (YouTube Short, 35 s) | A | **A** لوحات الألوان تكشف ٩٦٪ بس من الحالات… والباقي؟ - M18 - why-screening-is-not-diagnosis<br>**B** أغلب عمى الألوان يشوف ألوان — بس بشكل مختلف. - M02 - most-see-colour<br>**C** اختبار ألوان على موبايلك… شنو ما يگدر يگوله لك؟ - M08 - online-tests-cannot-diagnose |
| B08 Sleeping in contact lenses (Instagram Reel, 35 s) | A | **A** حتى العدسة المخصصة للنوم… خطرها أعلى؟ CDC تگول نعم. - M20 - overnight-approved-lenses-still-riskier<br>**B** حتى النوم النادر بالعدسة — مو بس العادة — يرفع الخطر. - M03 - even-naps-count<br>**C** نص لابسي العدسات بأمريكا نام بيها مرة. وانت؟ - M09 - you-are-not-alone-but-it-matters |
| B09 Presbyopia (TikTok, 30 s) | A | **A** إذا تبعّد الموبايل حتى تقرأ، غالباً هذا عمر… والحل بسيط. - M09 - normal-and-fixable-with-caveat<br>**B** بعد الأربعين عدسة عيونك تصير أقسى… شلون يأثر هذا على القراءة؟ - M05 - how-focusing-works<br>**C** القراية القريبة تصعب وتصعب… ومتى تتوقف؟ - M08 - progression-stops-around-65 |
| B10 Phoropter: one or two? (YouTube Short, 30 s) | A | **A** "واحد لو اثنين؟" وانت مو متأكد؟ هذا متوقع. - M13 - neither-is-crystal-clear<br>**B** بفحص الاستجماتزم، الفرق بين "واحد" و"اثنين" أكبر مما تحس. - M05 - why-the-choices-are-exaggerated<br>**C** شوف الصورتين… أي أوضح؟ (مو فحص — بس تحس الإحساس). - M23 - just-noticeable-difference |

Held-out briefs B11 (astigmatism), B12 (sunglasses/UV), B13 (watery eyes and dryness): see `BRIEFS_AND_FINALISTS.md`.

## 3. Most frequent failure patterns (baseline, 39 finalists)
1. No curiosity gap (statements/instructions): 13/39. 2. Evidence/scope overreach: SCOPE 11, MISLEAD 6, CITATION 3. 3. Formulaic retention plans: 39/39 five beats; 36/39 empty ending. 4. Low originality: 12/39. 5. Weak first frames: 11/39. 6. Fear-/diagnosis-adjacent wording: 6/39. 7. Demo presented as the test. 8. Finalists with the same takeaway. Details and sources of each: `FAILURE_PATTERNS.md`.

## 4. Files changed and why
Skills: `hook-scientific-validation/SKILL.md` + `references/accuracy-rules.md` (evidence record, assertion rule, parameter/category-shift rule, symptom-to-cause guard, C13 pinhole rewrite, C16 fix, C21-C28) - `hook-evaluation/SKILL.md`, `references/rubric.md`, `scripts/hook_lint.py`, `templates/candidate_schema.json` (G7-G10, payoff diversity, adversarial self-check, new checks) - `hook-writing/SKILL.md`, `references/examples.md`, `iraqi-arabic.md` (gap/shape rules, anti-patterns, pinhole example corrected, vocabulary flags) - `hook-retention/SKILL.md` (beat table, written closing line) - `hook-visual-design/SKILL.md` (concrete first frame, demo != test, participatory-measurement validity) - `hook-idea-diagnosis/SKILL.md` (angle + topic fidelity), `references/curiosity-psychology.md` (phrase fix) - `hook-engine/SKILL.md` (stage 5/7 fields) - `hook-analytics/SKILL.md` + `scripts/sample_size.py`. Package: `RESEARCH_LEDGER.csv` (+31), `tests/cases.json` (49 cases, held-out reclassified), `tests/run_tests.py`, fixtures (25 red-team), `scripts/validate_package.py`, README, CHANGELOG, VERSION. Each change is mapped to its evidence and status in `IMPROVEMENT_LOG.md`.

## 5. Remaining limitations
- **Scientific:** quotes in the evidence records were copied from retrieved excerpts and are self-reported - nothing automated checks that they exist in the source; many sources were read as excerpts (see `access_status`). Evidence for some topics is thin (trade-journal sources for phoropter questions; one ophthalmologist Q&A for the dark-lens/UV point; a 1984 standard hosted on an unusual domain; US-only CDC data; a review that is not systematic for blue-light glasses). Professional review is still required for paediatric, infection-risk and symptom-related topics. No Iraq-specific regulation or prevalence data.
- **Language:** all Iraqi lines are model drafts. Phase 2 added vocabulary flags (section 8b of the Iraqi guide) that are guesses until the creator confirms them. `W_MSA`/`W_MSA_SOFT` detect only a handful of words.
- **Measurement:** no real analytics. The synthetic sample CSV is not data. The experiment is underpowered unless videos reach thousands of impressions (e.g. ~1,468 per arm to detect 60% -> 65% stay-rate).
- **Method:** same-model generation and scoring; held-out leakage; the rubric weights are untested; the linter checks form only.
- **Overlap:** the creator's own `hook-director` skill could not be inspected.

## 6. Practical experiment plan
`EXPERIMENT_PLAN.md`: collect the creator's real scripts and platform exports -> own-baseline per platform -> 3-second comprehension pre-test with target viewers -> >= 5 matched pairs changing one variable (suggested first contrast: question vs statement hook on myth topics), pre-registered primary metric (Stayed to watch / skip rate / watch-time ratio), sample-size check with `sample_size.py`, sign-test and CI reporting, explicit invalidation list.

## 7. What was actually run in Phase 2
`git`/`diff`/`grep` audit of the ZIP and tree; web searches and page fetches for 31 new sources; frozen-baseline hashing (`BASELINE_MANIFEST.sha256`, re-verified by `tests/run_tests.py`); the v1.0 linter run on the baseline (from git history); the v1.1 linter on all 39 revised finalists (0 errors, 9 warnings); `tests/run_tests.py` (see `tests/RESULTS.md`); `claude plugin validate`. **Not run:** any independent grading, audience test, or analytics comparison.
