# Adversarial review of v1.1.0 outputs (after iteration 2). Same rubric, same reviewer (the generating model): bias risk is stated in the report.
# Scores 1-5: clarity, curiosity, originality, iraqi, visual, continuity, sci. flags as in review_v1.py plus PENDING (payoff needs research not yet done).
REVIEW = {
"B01-A": (4,4,3,4,5,4,4,[],"Defocused-camera demo is an analogy; labelled."),
"B01-B": (4,4,5,3,3,4,4,["UNFILMABLE"],"Smallest hole may not film legibly; 'ثقب الورقة' wording to confirm."),
"B01-C": (4,3,4,4,3,4,4,[],"Statement; gap carried by on-screen 'ليش؟'. Could be misread as a self-test; closing beat holds."),
"B02-A": (4,4,2,4,3,4,4,[],"Blue-light myth is mainstream: low originality."),
"B02-B": (4,3,4,4,4,4,3,[],"Counting someone else's blinks is informal; benchmark comparison still rough."),
"B02-C": (4,3,2,4,2,2,3,["PENDING"],"Promises evidence it cannot yet give; conditional only."),
"B03-A": (3,4,5,3,4,4,3,[],"Long hook; masking claim leans on one review citing another paper."),
"B03-B": (4,3,2,4,2,3,3,[],"Absolute 'المشكلة هي ساعات الشاشة'; low originality; sleep tangent."),
"B03-C": (5,3,3,4,3,4,4,[],"Answer in hook, beat-2 question declared."),
"B04-A": (3,4,3,3,3,4,4,[],"Number-first hook still heavy for parents."),
"B04-B": (4,4,4,3,3,4,4,[],"Strong; review is a secondary source for the RCT statement."),
"B04-C": (4,3,2,4,3,4,4,[],"Common advice; Iraq heat context absent."),
"B05-A": (3,3,4,3,5,4,4,[],"'خُمس' phrasing to test aloud."),
"B05-B": (4,3,4,3,4,4,4,[],"Source copy hosted on an unusual domain."),
"B05-C": (5,4,4,5,4,4,4,[],"Best of the set; mirror line unsourced (script-only, marked)."),
"B06-A": (5,4,3,4,5,4,4,[],"Geometry stated; reverse for the other eye."),
"B06-B": (4,4,4,4,3,4,4,[],"Fixed: no longer claims the spot is in the middle."),
"B06-C": (4,3,4,3,4,3,4,[],"Moon size (~0.5 degree) is not in the source."),
"B07-A": (4,3,5,3,3,4,3,[],"Dated source (NAS/NRC report); confirm with a recent source."),
"B07-B": (4,3,2,4,3,4,4,[],"Low originality; simulation caveat in plan."),
"B07-C": (4,3,3,4,3,4,4,[],"Health-system page, not a guideline."),
"B08-A": (4,4,4,4,3,4,3,[],"Comparator (risk vs not sleeping in them) implicit; US data."),
"B08-B": (4,3,3,4,3,4,4,[],"Fixed: no napping claim."),
"B08-C": (4,3,3,4,3,4,4,[],"US 2014 survey stated in the hook."),
"B09-A": (5,3,3,5,4,4,4,[],"Reassurance has its caveat beat."),
"B09-B": (4,3,3,3,4,4,4,[],"'عدسة عيونك' awkward."),
"B09-C": (4,4,4,4,3,4,4,[],"NEI vs AAO onset differ; stated."),
"B10-A": (4,3,3,4,4,4,3,[],"Practitioner (trade) evidence only."),
"B10-B": (3,3,5,3,3,3,3,[],"Jargon for laypeople; 2008 trade article; 'bigger than you feel' is a gloss."),
"B10-C": (4,3,3,4,5,3,3,[],"Simulation; disclaimer in hook."),
"B11-A": (4,3,3,4,5,4,4,[],"Analogy; closing beat guards against self-diagnosis."),
"B11-B": (4,3,3,4,3,4,5,[],"Statement; gap carried by on-screen question."),
"B11-C": (4,4,5,4,3,4,4,[],"New insight vs baseline; paediatric review needed."),
"B12-A": (4,4,4,4,3,4,4,[],"Fixed: comparator removed; single-source Q&A."),
"B12-B": (4,3,3,4,4,4,4,[],"Straightforward."),
"B12-C": (4,3,3,4,4,4,4,[],"Straightforward."),
"B13-A": (4,3,4,4,4,4,4,[],"Fixed: third-person general statement."),
"B13-B": (4,3,3,4,4,4,5,[],"Teaser; low stakes."),
"B13-C": (4,3,4,4,3,4,4,[],"Source ranks obstruction first for overflow; not a ranking for the viewer."),
}
# Substantive defects the review found in the ITERATION-1 draft that the linter did NOT catch (all fixed in iteration 2):
ITER1_DEFECTS = [
 ("B01-B","hook assumed the viewer already knew the clinical pinhole (not standalone)"),
 ("B02-B","self-counting blinks changes blinking (observer effect): invalid comparison with a norm"),
 ("B02-C","payoff (efficacy evidence) not yet retrieved: promise not deliverable"),
 ("B03-C","hook already states the answer but answer_in_hook was left false; last beat compared sun vs screen risk without a source"),
 ("B06-B","'a hole in the middle of your vision' - the blind spot is off-centre: wrong location"),
 ("B08-B","'nap' is a category shift from 'occasional overnight use'"),
 ("B12-A","'more rays' with no stated comparator (source gives none)"),
 ("B13-A","hedged cause-naming for the viewer's own symptom"),
]

# --- Consistency pass (added after noticing that the first scoring of v1.1 assigned far fewer flags than the v1.0 review for the same kinds of issue).
# Same standard as review_v1.py: originality <= 2 => GENERIC; statement/conclusion hooks whose gap is only a caption => NOGAP;
# practitioner/single-source/US-only/dated evidence => SCOPE; risk-multiplier or consequence hooks => DIAG (fear-adjacent).
_EXTRA = {"B03-B":["NOGAP"],"B07-B":["NOGAP"],"B11-B":["NOGAP"],"B12-C":["NOGAP"],
          "B08-A":["DIAG","SCOPE"],"B08-B":["DIAG"],"B10-A":["SCOPE"],"B10-B":["SCOPE"],"B07-A":["SCOPE"],"B03-A":["SCOPE"],"B12-A":["SCOPE"],"B02-B":["SCOPE"]}
for _k, _v in list(REVIEW.items()):
    fl = list(_v[7])
    for x in _EXTRA.get(_k, []):
        if x not in fl: fl.append(x)
    if _v[2] <= 2 and "GENERIC" not in fl: fl.append("GENERIC")
    REVIEW[_k] = _v[:7] + (fl,) + _v[8:]
