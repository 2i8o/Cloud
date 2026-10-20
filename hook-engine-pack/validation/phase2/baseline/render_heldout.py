"""Render baseline_data.py into Markdown + linter JSON. Part of the immutable baseline."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from baseline_data_heldout import BRIEFS
REC = {"B11":"A","B12":"A","B13":"A"}
REASON = {"B11":"strong visual analogy","B12":"counterintuitive and sourced","B13":"paradox with a source"}
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
led = {r["source_id"]: r["access_status"] for r in csv.DictReader(open(os.path.join(ROOT, "RESEARCH_LEDGER.csv"), encoding="utf-8"))}
out = os.path.dirname(__file__)
os.makedirs(os.path.join(out, "lint"), exist_ok=True)
for b in BRIEFS:
    L = [f"# {b['id']} - {b['title']}  (HELD-OUT BASELINE v1.0.0 - do not edit)\n",
         f"**Brief:** {b['brief']}  \n**Audience:** {b['audience']} | **Platform:** {b['platform']} | **Duration:** {b['dur']} s\n",
         f"**Idea verdict:** {b['verdict']}\n", f"**Recommendation:** {REC[b['id']]} - {REASON[b['id']]}\n"]
    cands = []
    for f in b["fin"]:
        L.append(f"## Finalist {f['id']} - {f['mech']} / `{f['key']}`\n")
        L.append(f"- **Hook:** {f['hook']}\n- **Gloss:** {f['gloss']}\n- **Curiosity gap:** {f['gap']}\n- **First frame:** {f['frame']}\n- **Continuation:** {f['cont']}\n- **Payoff:** {f['payoff']}")
        L.append("- **Retention plan:**")
        for t, x in f["beats"]:
            L.append(f"  - {t} s: {x}")
        L.append("- **Claims:** " + "; ".join(f"{c[0]} [{c[1]}, {c[2]}{'' if c[3] else ', script-only'}]" for c in f["claims"]))
        L.append(f"- **Sources needed:** {f['sources_needed']}\n- **Strength:** {f['strength']}\n- **Risk:** {f['risk']}\n- **Confidence:** {f['conf']}\n")
        cands.append(dict(id=f["id"], hook_ar=f["hook"], gloss_en=f["gloss"], mechanism=f["mech"], insight_key=f["key"], tension=f["gap"], audience=b["audience"],
                          first_frame=f["frame"], continuation=f["cont"], payoff=f["payoff"], payoff_answers_gap=True, sound_off_ok=True,
                          claims=[dict(text=c[0], source=c[1], status=c[2], in_hook=c[3], needs_professional_review=False) for c in f["claims"]],
                          risk=f["risk"], confidence="likely"))
    open(os.path.join(out, f"{b['id']}.md"), "w", encoding="utf-8").write("\n".join(L))
    src = {s: {"access": led.get(s, "")} for s in {c["source"] for f in cands for c in f["claims"]}}
    json.dump(dict(brief=dict(subject_terms=b["terms"], duration_s=b["dur"], platform=b["platform"]), sources=src, diversity_exception="", recommended=REC[b["id"]], candidates=cands),
              open(os.path.join(out, "lint", f"{b['id']}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("rendered")
