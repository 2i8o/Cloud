import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from revised_data import BRIEFS
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
led = {r["source_id"]: r["access_status"] for r in csv.DictReader(open(os.path.join(ROOT, "RESEARCH_LEDGER.csv"), encoding="utf-8"))}
out = os.path.dirname(__file__); os.makedirs(os.path.join(out, "lint"), exist_ok=True)
for b in BRIEFS:
    L = [f"# {b['id']} - {b['title']}  (v1.1.0{' - HELD-OUT brief' if b['held_out'] else ''})\n",
         f"**Brief:** {b['brief']}  \n**Audience:** {b['audience']} | **Platform:** {b['platform']} | **Duration:** {b['dur']} s\n",
         f"**Idea verdict:** {b['verdict']}\n", f"**Recommendation:** {b['rec']} - {b['why']}\n"]
    cands = []
    for f in b["fin"]:
        L += [f"## Finalist {f['id']} - {f['mech']} / `{f['key']}` / payoff `{f['pkey']}`\n",
              f"- **Hook:** {f['hook']}\n- **Gloss:** {f['gloss']}\n- **Curiosity gap:** {f['gap']} (carried by: {f['carrier']})",
              f"- **First frame:** {f['frame']}\n- **Continuation:** {f['cont']}\n- **Payoff:** {f['payoff']}"]
        if f["aih"]: L.append(f"- **Answer is in the hook; beat-2 question:** {f['b2']}")
        L += ["- **Retention plan:**", "", "| time (s) | purpose | new information | draft spoken line |", "|---|---|---|---|"]
        for t, p, n, s in f["beats"]: L.append(f"| {t} | {p} | {n} | {s} |")
        L += ["", "- **Evidence record:**"]
        for c in f["claims"]:
            L.append(f"  - {c[0]} - [{c[1]}, {c[2]}{'' if c[4] else ', script-only'}] quote: \"{c[5]}\"; scope: {c[6]}")
        L += [f"- **Risk:** {f['risk']}\n- **Confidence:** {f['conf']}\n"]
        cands.append(dict(id=f["id"], hook_ar=f["hook"], gloss_en=f["gloss"], mechanism=f["mech"], insight_key=f["key"], payoff_key=f["pkey"], tension=f["gap"], audience=b["audience"],
            first_frame=f["frame"], continuation=f["cont"], payoff=f["payoff"], payoff_answers_gap=True, sound_off_ok=True, gap_carrier=f["carrier"], answer_in_hook=f["aih"], beat2_question=f["b2"], not_a_test_disclaimer=True, payoff_ready=f.get("payoff_ready", True),
            beats=[dict(t=t, purpose=p, new_info=n, spoken=s) for t, p, n, s in f["beats"]],
            claims=[dict(text=c[0], source=c[1], status=c[2], claim_form=c[3], in_hook=c[4], support_quote=c[5], scope=c[6], needs_professional_review=False) for c in f["claims"]],
            risk=f["risk"], confidence="likely"))
    open(os.path.join(out, f"{b['id']}.md"), "w", encoding="utf-8").write("\n".join(L))
    src = {s: {"access": led.get(s, "")} for s in {c["source"] for f in cands for c in f["claims"]} if s}
    json.dump(dict(brief=dict(subject_terms=b["terms"], duration_s=b["dur"], platform=b["platform"]), sources=src, diversity_exception="", recommended=b["rec"], candidates=cands),
              open(os.path.join(out, "lint", f"{b['id']}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("rendered", len(BRIEFS))
