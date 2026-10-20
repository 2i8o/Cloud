# Adversarial review of HELD-OUT BASELINE v1.0.0 (B11-B13). Same rubric/reviewer as review_v1.py (same-model bias applies).
REVIEW = {
"B11-A": (4,3,3,3,5,4,4,["DIAG"],"Analogy invites self-diagnosis ('is your eye rugby-shaped?'); AAO says cornea/lens, not the whole eye.","hook-scientific-validation / hook-writing"),
"B11-B": (3,2,3,3,2,4,5,["NOGAP"],"Long statement hook.","hook-writing"),
"B11-C": (4,2,2,4,2,3,2,["CITATION","MISLEAD","NOGAP"],"'mostly inherited' and 'not from screens' are stronger than S84 (risk is inherited; reading light/close TV are myths). Claim marked plausible in the hook.","hook-scientific-validation (plausible loophole; span support)"),
"B12-A": (4,4,4,3,3,4,4,["CONFUSING"],"'More than what?' (wearing none? clear lenses?). Single Q&A source.","hook-writing (comparator must be explicit)"),
"B12-B": (3,2,2,3,4,4,4,["NOGAP","GENERIC"],"Instruction with 'ورقة' for label (odd).","hook-writing"),
"B12-C": (4,2,3,4,3,4,4,["NOGAP"],"Answer inside the hook.","hook-writing (answer-in-hook)"),
"B13-A": (4,3,4,4,4,4,3,["SCOPE"],"'Because they are dry' states a single cause; source lists dryness as one of the most common causes and outflow obstruction as another.","hook-scientific-validation (scope: 'one common cause')"),
"B13-B": (4,3,3,4,4,3,5,[],"Teaser list; fine.","-"),
"B13-C": (3,3,3,3,3,3,2,["DIAG","SCOPE"],"Names a cause for the viewer's symptoms ('maybe the problem is the oily layer').","hook-scientific-validation (symptom->cause guard)"),
}
