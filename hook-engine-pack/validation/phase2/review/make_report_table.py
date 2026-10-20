import os, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
def L(p, n):
    s = importlib.util.spec_from_file_location(n, os.path.join(here, p)); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
b2 = L("../revised/revised_data.py", "c")
rows = ["| Brief | Recommended | Finalist hooks (v1.1.0) - mechanism - payoff |", "|---|---|---|"]
for b in b2.BRIEFS:
    if b["held_out"]: continue
    hooks = "<br>".join(f"**{f['id']}** {f['hook']} - {f['mech']} - {f['pkey']}" for f in b["fin"])
    rows.append(f"| {b['id']} {b['title']} ({b['platform']}, {b['dur']} s) | {b['rec']} | {hooks} |")
print("\n".join(rows))
