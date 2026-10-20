"""Compare frozen baseline v1.0.0 with v1.1.0 on the same 13 briefs (B11-B13 held out). Prints objective counts and reviewer-score means.
Usage: python3 compare_versions.py"""
import os, sys, re, statistics, collections, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
def L(p, n):
    s = importlib.util.spec_from_file_location(n, os.path.join(here, p)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
b1 = L("../baseline/baseline_data.py", "b1"); b1h = L("../baseline/baseline_data_heldout.py", "b1h"); r1 = L("review_v1.py", "r1"); r1h = L("review_v1_heldout.py", "r1h")
b2 = L("../revised/revised_data.py", "b2"); r2 = L("review_v11.py", "r2")
dims = ["clarity","curiosity","originality","iraqi","visual","continuity","sci"]
def norm_v1(brief):  # normalise v1 finalists to a common view
    return [dict(brief=brief["id"], id=f["id"], hook=f["hook"], mech=f["mech"], beats=[(t, "", x, x) for t, x in f["beats"]], claims=[dict(status=c[2], in_hook=c[3]) for c in f["claims"]], v=1) for f in brief["fin"]]
def norm_v2(brief):
    return [dict(brief=brief["id"], id=f["id"], hook=f["hook"], mech=f["mech"], beats=f["beats"], claims=[dict(status=c[2], in_hook=c[4], form=c[3], quote=c[5], scope=c[6]) for c in f["claims"]], v=2, carrier=f["carrier"]) for f in brief["fin"]]
def stats(F, R, ids, label):
    sc = [R[f"{f['brief']}-{f['id']}"] for f in F]
    print(f"\n=== {label}: {len(F)} finalists")
    for i, d in enumerate(dims): print(f"  {d:11} mean {statistics.mean(s[i] for s in sc):.2f}  share<=2: {sum(s[i] <= 2 for s in sc)}/{len(sc)}")
    print(f"  overall mean (7 dims) {statistics.mean(sum(s[:7]) / 7 for s in sc):.2f}; excluding Iraqi naturalness (not scoreable by the generating model) {statistics.mean((sum(s[:7]) - s[3]) / 6 for s in sc):.2f}; with >=1 flag: {sum(1 for s in sc if s[7])}/{len(sc)}; any dim<=2 or >=2 flags: {sum(1 for s in sc if min(s[:7]) <= 2 or len(s[7]) >= 2)}/{len(sc)}")
    print(f"  question-mark hooks: {sum('؟' in f['hook'] for f in F)}/{len(F)}; hooks starting 'ليش': {sum(f['hook'].startswith('ليش') for f in F)}")
    print(f"  mechanism histogram: {dict(collections.Counter(f['mech'] for f in F).most_common(6))}")
    print(f"  beat counts: {dict(collections.Counter(len(f['beats']) for f in F))}")
    def body(s): return re.sub(r'^(Close|See|Hook)\b[:\s-]*', '', s).strip()
    if F[0]['v'] == 1: print(f"  empty endings (<=3 words after 'Close'): {sum(len(body(f['beats'][-1][3]).split()) <= 3 for f in F)}/{len(F)}")
    else: print(f"  closing lines < 4 words: {sum(len(f['beats'][-1][3].split()) < 4 for f in F)}/{len(F)}")
    print(f"  hook assertions on non-verified claims: {sum(1 for f in F for c in f['claims'] if c['in_hook'] and c['status'] != 'verified' and c.get('form') != 'question')}")
    if F[0]['v'] == 2: print(f"  hook claims with quote+scope: {sum(1 for f in F for c in f['claims'] if c['in_hook'] and c['quote'] and c['scope'])}/{sum(1 for f in F for c in f['claims'] if c['in_hook'])}")
F1 = [f for b in b1.BRIEFS for f in norm_v1(b)]; F1h = [f for b in b1h.BRIEFS for f in norm_v1(b)]
F2 = [f for b in b2.BRIEFS for f in norm_v2(b)]
R1 = dict(r1.REVIEW); R1.update(r1h.REVIEW); R2 = r2.REVIEW
stats(F1, R1, None, "v1.0.0 baseline B01-B10 (tuned-on)"); stats([f for f in F2 if not f['brief'] in ('B11','B12','B13')], R2, None, "v1.1.0 B01-B10 (tuned-on)")
stats(F1h, R1, None, "v1.0.0 baseline B11-B13 (HELD-OUT)"); stats([f for f in F2 if f['brief'] in ('B11','B12','B13')], R2, None, "v1.1.0 B11-B13 (HELD-OUT)")
