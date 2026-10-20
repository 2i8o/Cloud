#!/usr/bin/env python3
"""hook_lint.py - deterministic checks for hook-engine finalist sets.

It enforces the machine-checkable part of the hard gates and the diversity
constraint. It does NOT judge Iraqi-Arabic naturalness, truth, or likely
performance; those need a human or the model (see skills/hook-evaluation).

Usage:
  python3 hook_lint.py candidates.json            # human-readable report
  python3 hook_lint.py candidates.json --json     # machine-readable
  python3 hook_lint.py --causal-text report.md    # scan analytics prose

Exit codes: 0 = no errors, 1 = at least one error, 2 = usage / bad input.
Stdlib only (Python >= 3.8).
"""
import json
import re
import sys
import unicodedata
from itertools import combinations

REQUIRED = ["id", "hook_ar", "mechanism", "insight_key", "payoff_key", "first_frame",
            "continuation", "payoff", "gap_carrier"]
SCI_RANK = {"verified": 3, "plausible": 2, "unverified": 1,
            "contested": 1, "false": 0}

# Arabic-script patterns are matched on normalised text (see norm()).
BANNED_ANYWHERE = [
    "لن تصدق", "ما راح تصدق", "ما راح تصدگ", "لا تصدق", "you won't believe",
    "you wont believe", "doctors don't want", "doctors dont want",
    "الحقيقة التي لا يريدك", "الحقيقة الي ما يگولها", "الحقيقه الي ما يگولها",
    "صدمة", "صادم", "shocking truth",
]
BANNED_OPENER = [
    "هل تعلم", "هل تعرف", "شنو سر", "سر ", "اسرار", "اسرار ", "did you know",
    "the truth about", "the secret",
]
FEAR_STRONG = [
    "يعمي", "تعمي", "راح تعمي", "يدمر", "تدمر", "يخرب", "تخرب", "يتلف",
    "will blind", "destroy", "destroys", "ruin your eyes", "damage your eyes forever",
]
FEAR_MILD = ["خطر", "خطير", "تحذير", "احذر", "danger", "warning"]
DIAG = [
    r"عندك\s+(ساد|ماء ابيض|جلوكوما|ماء ازرق|التهاب|اعتلال)",
    r"you have (cataract|glaucoma|macular|keratoconus|retinopathy)",
    r"اكيد عندك", r"you definitely have",
]
OPTOM = ["optometrist", "optometry", "اخصائي بصريات", "اخصائي النظر", "فاحص نظر", "طبيب بصريات"]
SURGERY = ["surgery", "surgeon", "جراحة", "جراح", "عملية ليزك", "lasik", "عملية الماء", "عملية الساد"]
BRAND = ["optinest", "بيت البصر"]
PRODUCT = ["اشتر", "اشتري", "buy now", "discount", "خصم", "عرض خاص", "اطلب الان", "كود خصم"]
MSA_SOFT = ["اضعاف", "يعتبر", "اجهاد", "فجوات", "تتعطل", "نتعرف", "يتضح", "بالتالي", "حيث"]
DEMO_AS_TEST = [r"نص الفحص", r"هذا الفحص", r"اختبر نفسك", r"هذا هو الاختبار", r"this is the test", r"test yourself", r"نتيجتك تعني"]
MSA_MARKERS = ["سوف", "لقد", "حيث ان", "ماذا", "لماذا", "كيف", "اين", "الان",
               "جدا", "يوجد", "ليس", "هؤلاء", "في هذا الفيديو"]
COMPARATIVES = ["اكثر", "اقل", "اخطر", "اسوا", "اعلى", "اكبر", "افضل", "اقوى", "اضعف", "اسرع"]
EFFECT_WORDS = ["louder", "faster cuts", "more effects", "zoom", "flash", "riser",
                "bass", "اسرع", "مؤثرات اكثر", "موسيقى اعلى", "تقطيع اسرع"]
CAUSAL = [
    r"\bproves?\b", r"\bproved\b", r"\bcaused\b", r"because of the hook",
    r"the hook (worked|caused|made)", r"\balways works\b", r"\bguaranteed\b",
    r"definitely (caused|due to)", r"اثبت", r"بسبب الهوك", r"السبب هو الهوك",
    r"دائما ينجح", r"اكيد بسبب",
]
STOP = set("""و في من على الى عن مع ما مو لا هذا هاي هذه هذول ذلك الي اللي التي
the a an of to is are in on and or it this that for with at by""".split())


def norm(s):
    """Normalise Arabic text for matching: strip diacritics/tatweel, unify alef/yaa/gaf."""
    s = unicodedata.normalize("NFKC", s or "").lower()
    s = re.sub(r"[ً-ٰٟـ]", "", s)
    s = re.sub("[أإآ]", "ا", s).replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي")
    return s.translate(str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789"))


def tokens(s):
    return [t for t in re.findall(r"[\w؀-ۿ]+", norm(s))
            if t not in STOP and len(t) > 1]


def jaccard(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0.0


def has_any(text, needles):
    t = norm(text)
    return [n for n in needles if norm(n) in t]


def lint(data):
    out = []  # (severity, code, candidate_id, message)

    def err(code, cid, msg):
        out.append(("ERROR", code, cid, msg))

    def warn(code, cid, msg):
        out.append(("WARN", code, cid, msg))

    cands = data.get("candidates") or []
    brief = data.get("brief") or {}
    sources = data.get("sources") or {}
    if not cands:
        err("E_NO_CANDIDATES", "-", "no candidates supplied")
        return out

    if len(cands) != 3 and not (data.get("diversity_exception") or "").strip():
        err("E_COUNT", "-", f"{len(cands)} finalists; need exactly 3 or a diversity_exception explaining why")

    for c in cands:
        cid = str(c.get("id", "?"))
        for f in REQUIRED:
            if not str(c.get(f, "")).strip():
                err("E_MISSING_FIELD", cid, f"missing or empty field: {f}")
        hook = c.get("hook_ar", "")
        visible = " ".join([hook, c.get("first_frame", ""), c.get("on_screen_text", "")])

        if c.get("payoff_answers_gap") is not True:
            err("E_NO_PAYOFF_MATCH", cid, "payoff_answers_gap is not true: cliffhanger / promise-payoff mismatch")
        if (c.get("scores") or {}).get("clarity") is not None and c["scores"]["clarity"] < 2:
            err("E_CLARITY", cid, "clarity score < 2: premise not understandable in ~3 s")

        for b in has_any(hook, BANNED_ANYWHERE):
            err("E_BANNED_PHRASE", cid, f"banned clickbait phrase: {b!r}")
        nh = norm(hook).strip()
        for b in BANNED_OPENER:
            if nh.startswith(norm(b)):
                err("E_GENERIC_OPENER", cid, f"generic opener: {b!r}")
        terms = brief.get("subject_terms") or []
        if terms and not any(norm(t) in norm(hook) for t in terms):
            warn("W_GENERIC", cid, "hook contains none of the brief's subject terms - apply the swap-the-topic test by hand (advisory: low precision in Phase-2 testing)")
        if len(tokens(hook)) > 14:
            warn("W_LONG", cid, f"hook has {len(tokens(hook))} content tokens; read aloud and test speakability")

        for b in has_any(visible, FEAR_STRONG):
            err("E_FEAR", cid, f"fear framing: {b!r}")
        for b in has_any(visible, FEAR_MILD):
            warn("W_FEAR_MILD", cid, f"possible fear framing: {b!r} - ensure evidence and an efficacy action")
        for pat in DIAG:
            if re.search(norm(pat), norm(visible)):
                err("E_DIAGNOSTIC", cid, "diagnostic language directed at the viewer")
        low = norm(" ".join(str(v) for v in c.values() if isinstance(v, str)))
        if any(norm(o) in low for o in OPTOM) and any(norm(s) in low for s in SURGERY):
            err("E_PROFESSION", cid, "optometry mentioned together with surgery: check optometry/ophthalmology scope")
        for b in has_any(low, BRAND):
            err("E_BRAND", cid, f"forbidden brand reference: {b!r} (active identity is Abbas Abdulmunem)")
        if not brief.get("product_mention_requested"):
            for b in has_any(visible + " " + c.get("payoff", ""), PRODUCT):
                err("E_PRODUCT", cid, f"product/offer language not requested: {b!r}")

        msa = [m for m in MSA_MARKERS if re.search(r"(^|\s)" + re.escape(norm(m)) + r"(\s|$|[،.؟!?…])", norm(hook))]
        if len(msa) >= 3:
            err("E_MSA", cid, f"hook reads as MSA ({', '.join(msa)}); rewrite in Iraqi")
        elif msa:
            warn("W_MSA", cid, f"MSA marker(s): {', '.join(msa)} - native review")

        if c.get("sound_off_ok") is False:
            warn("W_SOUND_OFF", cid, "question not readable without sound: add key-phrase text or change the frame")
        fix = " ".join([str(c.get("risk_fix", "")), str(c.get("improvement_notes", ""))])
        if fix.strip() and has_any(fix, EFFECT_WORDS) and c.get("idea_verdict") in ("RE-ANGLE", "REJECT"):
            err("E_EFFECT_FIX", cid, "proposes editing effects to rescue a weak premise")

        # spoil check
        j = jaccard(tokens(hook), tokens(c.get("payoff", "")))
        if j >= 0.7:
            err("E_SPOILS_PAYOFF", cid, f"hook and payoff overlap {j:.2f}: hook gives the payoff away")
        elif j >= 0.5:
            warn("W_SPOIL_RISK", cid, f"hook and payoff overlap {j:.2f}")

        # gap, answer-in-hook, demo-as-test, soft MSA, parameters, absolutes
        if str(c.get("gap_carrier", "")).strip().lower() in ("none", ""):
            err("E_NO_GAP", cid, "gap_carrier is none: neither voice, frame nor on-screen text poses an unanswered question")
        if c.get("answer_in_hook") is True and not str(c.get("beat2_question", "")).strip():
            err("E_ANSWER_IN_HOOK_NO_BEAT2", cid, "the hook states the answer but no different beat-2 question is given")
        for pat in DEMO_AS_TEST:
            if re.search(norm(pat), norm(visible + " " + c.get("payoff", "")), re.I) and not c.get("not_a_test_disclaimer"):
                err("E_DEMO_AS_TEST", cid, f"demo/screen presented as the test or as the viewer's result ({pat!r}); add not_a_test_disclaimer or reword")
        nh_tokens = norm(hook).split()
        comp = [w for w in COMPARATIVES if w in nh_tokens]
        if comp and not any(k in nh_tokens for k in ("من", "مما", "مقابل", "بدل", "عن")):
            warn("W_COMPARATIVE", cid, f"comparative {comp} without an explicit comparator ('more than what?')")
        if c.get("payoff_ready") is False:
            warn("W_PAYOFF_PENDING", cid, "payoff depends on research not yet done: show only as conditional, never recommend")
        soft = [m for m in MSA_SOFT if norm(m) in norm(hook)]
        if soft:
            warn("W_MSA_SOFT", cid, f"formal-register word(s): {', '.join(soft)} - native review")
        quotes = " ".join(str(cl.get("support_quote", "")) + " " + str(cl.get("scope", "")) for cl in c.get("claims") or [] if cl.get("in_hook", True))
        qnums = set(re.findall(r"\d+(?:[.,]\d+)?", norm(quotes).replace(",", "")))
        for n in re.findall(r"\d+(?:\.\d+)?", norm(hook).replace(",", "")):
            if n in ("20",) and "20/20" in norm(hook):
                continue
            if not any(q == n or (len(n) >= 2 and q.startswith(n)) for q in qnums):
                err("E_PARAM_NOT_SUPPORTED", cid, f"number {n!r} in the hook does not appear in any claim's support_quote/scope")
        for ab in ("دايما", "دائما", "ابدا", "كل الناس", "always", "never"):
            if norm(ab) in norm(hook) and norm(ab) not in norm(quotes):
                warn("W_ABSOLUTE", cid, f"absolute {ab!r} in hook is not in the supporting quote")
        # retention plan
        beats = c.get("beats")
        if not beats:
            err("E_NO_PLAN", cid, "no retention plan (beats) supplied")
        else:
            for i, b in enumerate(beats):
                ni = str(b.get("new_info", "")).strip() if isinstance(b, dict) else ""
                if len(ni.split()) < 3:
                    err("E_EMPTY_BEAT", cid, f"beat {i + 1} has no real new information")
            last = beats[-1] if isinstance(beats[-1], dict) else {}
            if len(str(last.get("spoken", "")).split()) < 4 or str(last.get("spoken", "")).strip().lower().startswith("close"):
                err("E_NO_CLOSING_LINE", cid, "final beat lacks a written closing line (>= 4 words)")

        # claims
        for cl in c.get("claims") or []:
            st = cl.get("status", "unverified")
            src = str(cl.get("source", "")).strip()
            in_hook = cl.get("in_hook", True)
            is_q = cl.get("claim_form") == "question"
            if in_hook and not is_q and st != "verified":
                err("E_UNVERIFIED_CLAIM", cid, f"hook asserts a {st} claim (only verified claims may be asserted; use claim_form=question): {cl.get('text','')[:70]!r}")
            elif in_hook and not is_q and not (str(cl.get("support_quote", "")).strip() and str(cl.get("scope", "")).strip()):
                err("E_NO_EVIDENCE_RECORD", cid, f"verified hook claim lacks support_quote and/or scope: {cl.get('text','')[:60]!r}")
            elif st in ("unverified", "false", "contested", "plausible") and not in_hook:
                warn("W_UNVERIFIED_SCRIPT_CLAIM", cid, f"script claim {st}: {cl.get('text','')[:70]!r}")
            if st in ("verified", "plausible"):
                if not src:
                    err("E_VERIFIED_NO_SOURCE", cid, f"claim marked {st} without source: {cl.get('text','')[:60]!r}")
                elif src not in sources and not re.match(r"https?://", src):
                    err("E_UNKNOWN_SOURCE", cid, f"source {src!r} is not in the supplied source table or a URL (invented citation?)")
                elif src in sources and sources[src].get("access") in ("not_accessed", None, ""):
                    err("E_SOURCE_NOT_ACCESSED", cid, f"claim rests on source {src} that was not accessed")
            if cl.get("needs_professional_review") is None and cl.get("class") in ("H", "P"):
                warn("W_REVIEW_FLAG", cid, "health/professional-scope claim has no needs_professional_review decision")

    # diversity
    for a, b in combinations(cands, 2):
        if a.get("mechanism") and a.get("mechanism") == b.get("mechanism"):
            err("E_MECH_DUP", f"{a.get('id')}+{b.get('id')}", f"same mechanism {a['mechanism']}")
        if a.get("insight_key") and a.get("insight_key") == b.get("insight_key"):
            err("E_INSIGHT_DUP", f"{a.get('id')}+{b.get('id')}", f"same insight_key {a['insight_key']}")
        ov = jaccard(tokens(a.get("hook_ar", "")), tokens(b.get("hook_ar", "")))
        if ov >= 0.5:
            err("E_TEXT_OVERLAP", f"{a.get('id')}+{b.get('id')}", f"hook wording overlap {ov:.2f}")

    keys = [c.get("payoff_key") for c in cands]
    for a, b in combinations(cands, 2):
        if a.get("payoff_key") and a.get("payoff_key") == b.get("payoff_key"):
            err("E_PAYOFF_DUP", f"{a.get('id')}+{b.get('id')}", f"same payoff_key {a['payoff_key']}: finalists end in the same takeaway")
    shapes = {("q" if "؟" in c.get("hook_ar", "") or "?" in c.get("hook_ar", "") else "s") for c in cands}
    if len(cands) >= 3 and len(shapes) == 1:
        warn("W_SHAPE", "-", "all finalists share one hook shape (all questions or all statements)")

    # recommendation
    rid = data.get("recommended")
    if rid is not None:
        rec = next((c for c in cands if str(c.get("id")) == str(rid)), None)
        if rec is None:
            err("E_RECOMMEND_MISSING", str(rid), "recommended id is not among the finalists")
        else:
            if rec.get("payoff_ready") is False:
                err("E_RECOMMEND_PENDING", str(rid), "recommended option's payoff still needs research")
            if (rec.get("scores") or {}).get("clarity", 5) < 3:
                err("E_RECOMMEND_CLARITY", str(rid), "recommended option has clarity < 3 (ambiguity rewarded over comprehension)")

            def sci(c):
                vals = [SCI_RANK.get(x.get("status", "unverified"), 1)
                        for x in c.get("claims") or [] if x.get("in_hook", True)]
                return min(vals) if vals else 3
            best = max(sci(c) for c in cands)
            if sci(rec) < best:
                err("E_RECOMMEND_SCI", str(rid), "recommended option has weaker scientific status than another finalist")
    return out


def causal_scan(text):
    findings = []
    for i, line in enumerate(text.splitlines(), 1):
        n = norm(line)
        for pat in CAUSAL:
            if re.search(norm(pat) if not pat.startswith("\\") else pat, n):
                findings.append((i, pat, line.strip()[:100]))
    return findings


def main(argv):
    if len(argv) >= 3 and argv[1] == "--causal-text":
        try:
            text = open(argv[2], encoding="utf-8").read()
        except OSError as e:
            print(f"cannot read: {e}", file=sys.stderr)
            return 2
        f = causal_scan(text)
        for i, pat, line in f:
            print(f"ERROR E_CAUSAL line {i}: causal/certainty language ({pat}): {line}")
        print("OK: no causal language found" if not f else f"{len(f)} causal-language problem(s)")
        return 1 if f else 0
    if len(argv) < 2 or argv[1].startswith("-"):
        print(__doc__)
        return 2
    try:
        data = json.load(open(argv[1], encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"cannot load JSON: {e}", file=sys.stderr)
        return 2
    res = lint(data)
    errors = [r for r in res if r[0] == "ERROR"]
    if "--json" in argv:
        print(json.dumps([dict(severity=s, code=c, candidate=i, message=m) for s, c, i, m in res],
                         ensure_ascii=False, indent=2))
    else:
        for s, c, i, m in res:
            print(f"{s:5} {c:24} [{i}] {m}")
        print(f"\n{len(errors)} error(s), {len(res) - len(errors)} warning(s)."
              " Linter checks form only; truth, naturalness and performance need review.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
