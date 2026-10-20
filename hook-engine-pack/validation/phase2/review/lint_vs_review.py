"""How much of what the human-style review found did the v1.0.0 linter catch on the frozen baseline?
Needs the v1.0.0 linter source (git show da93c76:hook-engine-pack/skills/hook-evaluation/scripts/hook_lint.py > /tmp/v10/hook_lint_v10.py)."""
import json, os, sys, glob, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
def L(p, n):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
lint = L("/tmp/v10/hook_lint_v10.py", "lint10")
R = dict(L(os.path.join(here, "review_v1.py"), "r").REVIEW); R.update(L(os.path.join(here, "review_v1_heldout.py"), "rh").REVIEW)
flagged, per = {}, {}
for f in sorted(glob.glob(os.path.join(here, "../baseline/lint/B*.json"))):
    bid = os.path.basename(f)[:3]; data = json.load(open(f, encoding="utf-8"))
    for sev, code, cid, msg in lint.lint(data):
        if "+" in cid or cid in ("-", "?"): continue
        flagged.setdefault(f"{bid}-{cid}", set()).add(code)
weak = {k for k, v in R.items() if min(v[:7]) <= 2 or len(v[7]) >= 2}
withflag = {k for k, v in R.items() if v[7]}
print(f"v1.0.0 linter flagged {len(flagged)}/{len(R)} baseline finalists (any code)")
print(f"human-style review: {len(weak)} weak finalists, {len(withflag)} with >=1 flag")
print(f"weak finalists the linter flagged: {len(weak & set(flagged))}/{len(weak)}  -> missed {len(weak - set(flagged))}")
print(f"linter-flagged finalists that review did not consider weak: {sorted(set(flagged) - weak)}")
gen_h = {k for k, v in R.items() if "GENERIC" in v[7]}; gen_l = {k for k, c in flagged.items() if "E_GENERIC" in c}
print(f"E_GENERIC agreement with review GENERIC flag: both {len(gen_h & gen_l)}, linter-only (false alarm) {len(gen_l - gen_h)}, review-only (miss) {len(gen_h - gen_l)}")
for flag in ("CITATION", "MISLEAD", "SCOPE", "DIAG", "NOGAP"):
    h = {k for k, v in R.items() if flag in v[7]}
    print(f"review flag {flag}: {len(h)} finalists; linter flagged {len(h & set(flagged))} of them")
