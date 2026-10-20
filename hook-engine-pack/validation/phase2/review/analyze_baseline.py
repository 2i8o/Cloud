"""Compute the numbers behind the failure-pattern claims. Reads baseline data (frozen) and review_v1.py. Usage: python3 analyze_baseline.py [--data PATH] [--review PATH]"""
import sys, os, re, collections, statistics, importlib.util, itertools
def load(path, name):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
here = os.path.dirname(os.path.abspath(__file__))
data = load(sys.argv[sys.argv.index("--data")+1] if "--data" in sys.argv else os.path.join(here, "../baseline/baseline_data.py"), "d")
rev = load(sys.argv[sys.argv.index("--review")+1] if "--review" in sys.argv else os.path.join(here, "review_v1.py"), "r")
F = [(b["id"], f, b) for b in data.BRIEFS for f in b["fin"]]
n = len(F); R = rev.REVIEW
dims = ["clarity","curiosity","originality","iraqi","visual","continuity","sci"]
print(f"candidates: {n}; reviewed: {len(R)}")
for i, d in enumerate(dims):
    v = [R[f"{b}-{f['id']}"][i] for b, f, _ in F]
    print(f"  {d:12} mean {statistics.mean(v):.2f}  min {min(v)}  share<=2: {sum(x<=2 for x in v)}/{n}")
tot = [sum(R[f"{b}-{f['id']}"][:7]) / 7 for b, f, _ in F]
print(f"  overall mean {statistics.mean(tot):.2f}")
fl = collections.Counter(x for k in R for x in R[k][7])
print("flags:", dict(fl.most_common()), "| candidates with >=1 flag:", sum(1 for k in R if R[k][7]), "/", n)
weak = [k for k in R if min(R[k][:7]) <= 2 or len(R[k][7]) >= 2]
print("weak (any dim<=2 or >=2 flags):", len(weak), "/", n)
print("sci<=3:", sum(R[k][6] <= 3 for k in R), "| sci<=2:", sum(R[k][6] <= 2 for k in R))
# surface patterns
q = sum("؟" in f["hook"] for _, f, _ in F); print(f"hooks containing a question mark: {q}/{n}")
shapes = collections.Counter()
for _, f, _ in F:
    h = f["hook"].strip()
    shapes["question" if "؟" in h else "statement/instruction"] += 1
print("shapes:", dict(shapes))
fw = collections.Counter(f["hook"].split()[0] for _, f, _ in F); print("most common first words:", fw.most_common(4))
print("mechanism histogram:", dict(collections.Counter(f["mech"] for _, f, _ in F).most_common()))
last = [f["beats"][-1][1] for _, f, _ in F]
def body(t): return re.sub(r"^(Close|See|Hook)\b[:\s-]*", "", t).strip()
empty = sum(len(body(t).split()) <= 3 for t in last)
print(f"final beats with <=3 words of content after 'Close' (empty ending): {empty}/{n}")
print("final beats that are 'Close' with no stated payoff/implication:", sum(t.startswith("Close") for t in last), "/", n)
print("beat counts:", dict(collections.Counter(len(f['beats']) for _, f, _ in F)))
starts = collections.Counter(f["beats"][0][0].split("-")[0] + "-" + f["beats"][1][0].split("-")[0] for _, f, _ in F); print("opening beat boundaries (t0-t1):", starts.most_common(3))
pl = collections.Counter(c[2] for _, f, _ in F for c in f["claims"]); print("claim statuses:", dict(pl))
pl_hook = [(b, f["id"]) for b, f, _ in F for c in f["claims"] if c[2] == "plausible" and c[3]]; print("hook assertions resting on 'plausible' claims:", len(pl_hook), pl_hook)
def toks(s): return set(re.findall(r"\w+", s))
dup = []
for b in data.BRIEFS:
    for x, y in itertools.combinations(b["fin"], 2):
        a, c = toks(x["payoff"] + " " + x["cont"]), toks(y["payoff"] + " " + y["cont"])
        j = len(a & c) / len(a | c) if a | c else 0
        if j >= 0.2: dup.append((b["id"], x["id"], y["id"], round(j, 2)))
print("sibling pairs with overlapping payoff/continuation (J>=0.2):", dup)
