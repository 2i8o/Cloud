#!/usr/bin/env python3
"""run_tests.py - executes every machine-checkable test in the package.

Scope (be honest about it): these tests prove the helper scripts, installer, validator
and package structure behave as specified, and that the linter rejects the red-team
fixtures and accepts the gold fixtures. They do NOT measure the quality of model-written
hooks or real-world performance; the model-driven behaviour specs live in tests/cases.json.

Usage: python3 tests/run_tests.py [--zip FILE] [--write-results]
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable
LINT = ROOT / "skills/hook-evaluation/scripts/hook_lint.py"
ANA = ROOT / "skills/hook-analytics/scripts/analytics_compare.py"
INSTALL = ROOT / "scripts/install.sh"
VALIDATE = ROOT / "scripts/validate_package.py"
FIX = ROOT / "tests/fixtures"

results = []  # (name, ok, detail)


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + name + (f"  -- {detail}" if detail and not ok else ""))


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def lint_codes(path):
    r = run([PY, "-I", str(LINT), str(path), "--json"])
    try:
        return {x["code"] for x in json.loads(r.stdout)}, r.returncode
    except ValueError:
        return set(), r.returncode


def tree_hash(p):
    h = hashlib.sha256()
    for f in sorted(Path(p).rglob("*")):
        if f.is_file():
            h.update(str(f.relative_to(p)).encode())
            h.update(f.read_bytes())
    return h.hexdigest()


def main(argv):
    # 1 package validator
    r = run([PY, "-I", str(VALIDATE), str(ROOT)])
    check("validate_package: package is structurally valid", r.returncode == 0, r.stdout[-400:])

    # 2 docs freshness
    r = run([PY, "-I", str(ROOT / "scripts/build_docs.py"), "--check"])
    check("build_docs --check: generated documents are current", r.returncode == 0, r.stdout)

    # 3 gold fixtures
    for g in sorted((FIX / "gold").glob("G0*.json")):
        codes, rc = lint_codes(g)
        errs = {c for c in codes if c.startswith("E_")}
        check(f"lint gold/{g.name}: 0 errors", rc == 0 and not errs, str(errs))

    # 4 red-team fixtures -> expected codes
    expected = {
        "R01_same_hook": {"E_INSIGHT_DUP", "E_MECH_DUP", "E_TEXT_OVERLAP"},
        "R02_sensational_recommended": {"E_UNVERIFIED_CLAIM", "E_RECOMMEND_SCI", "E_FEAR"},
        "R03_spoils_payoff": {"E_SPOILS_PAYOFF"},
        "R04_no_continuation": {"E_MISSING_FIELD"},
        "R05_generic_question": {"E_GENERIC_OPENER", "E_GENERIC"},
        "R06_effects_instead_of_premise": {"E_EFFECT_FIX"},
        "R07_invented_citation": {"E_UNKNOWN_SOURCE"},
        "R08_not_accessed_source": {"E_SOURCE_NOT_ACCESSED"},
        "R09_msa": {"E_MSA"},
        "R10_profession": {"E_PROFESSION"},
        "R11_cliffhanger": {"E_NO_PAYOFF_MATCH"},
        "R12_ambiguity_rewarded": {"E_RECOMMEND_CLARITY"},
        "R_fear": {"E_FEAR"}, "R_diagnostic": {"E_DIAGNOSTIC"}, "R_banned": {"E_BANNED_PHRASE"},
        "R_product": {"E_PRODUCT"}, "R_brand": {"E_BRAND"},
    }
    for name, want in expected.items():
        codes, rc = lint_codes(FIX / "redteam" / f"{name}.json")
        check(f"lint redteam/{name}: rejects with {sorted(want)}", rc == 1 and want <= codes, f"got {sorted(codes)}")

    # product language is allowed only when the brief explicitly requests it
    with tempfile.TemporaryDirectory() as td:
        d = json.loads((FIX / "redteam/R_product.json").read_text(encoding="utf-8"))
        d["brief"]["product_mention_requested"] = True
        q = Path(td) / "p.json"
        q.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        codes, _ = lint_codes(q)
        check("lint: product language allowed when explicitly requested by the creator", "E_PRODUCT" not in codes, str(codes))

    # 5 cases.json automated_check links must be consistent with the lint results
    cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))["cases"]
    for c in cases:
        a = c.get("automated_check")
        if isinstance(a, dict) and a.get("type") == "lint":
            codes, _ = lint_codes(FIX / a["fixture"])
            check(f"case {c['id']} automated lint", set(a["expect"]) <= codes, f"got {sorted(codes)}")
        elif isinstance(a, dict) and a.get("type") == "causal_text":
            r = run([PY, "-I", str(LINT), "--causal-text", str(FIX / a["fixture"])])
            check(f"case {c['id']} causal-language detector fires", r.returncode == 1)
    r = run([PY, "-I", str(LINT), "--causal-text", str(FIX / "gold/G_causal_ok.md")])
    check("causal-language detector accepts hedged analytics prose", r.returncode == 0, r.stdout)

    # 6 analytics script
    csvp = FIX / "analytics_sample.csv"
    r = run([PY, "-I", str(ANA), str(csvp), "NEW1"])
    check("analytics_compare: sufficient baseline reports position", r.returncode == 0 and "above IQR" in r.stdout and "n=10" in r.stdout, r.stdout[-300:])
    check("analytics_compare: warns about YouTube view-definition epochs", "view-definition change" in r.stdout)
    check("analytics_compare: output has no causal language", run([PY, "-I", str(LINT), "--causal-text", "/dev/stdin"], input=r.stdout).returncode == 0)
    r2 = run([PY, "-I", str(ANA), str(csvp), "SMALL1"])
    check("analytics_compare: small baseline -> hypothesis mode, no 'typical' value", "INSUFFICIENT BASELINE" in r2.stdout and "median" not in r2.stdout.split("Descriptive")[0], r2.stdout[-300:])

    # 7 installer (R14) in a throw-away HOME
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "skills"
        r = run(["bash", str(INSTALL), "--dest", str(dest)])
        n_src = len([d for d in (ROOT / "skills").iterdir() if d.is_dir()])
        installed = [d for d in dest.iterdir() if (d / "SKILL.md").is_file()] if dest.exists() else []
        check("install.sh: fresh install copies all skills", r.returncode == 0 and len(installed) == n_src, r.stderr[-200:])
        check("install.sh: installed skills have bundled scripts/templates", (dest / "hook-evaluation/scripts/hook_lint.py").is_file() and (dest / "hook-analytics/templates/experiment_log.csv").is_file())
        before = tree_hash(dest)
        r = run(["bash", str(INSTALL), "--dest", str(dest)])
        check("install.sh: second run refuses (exit 3) and changes nothing", r.returncode == 3 and tree_hash(dest) == before, r.stderr[-200:])
    with tempfile.TemporaryDirectory() as td:
        dest = Path(td) / "skills"
        (dest / "hook-engine").mkdir(parents=True)
        marker = dest / "hook-engine" / "MY_EDITS.md"
        marker.write_text("user's own edits")
        before = tree_hash(dest)
        r = run(["bash", str(INSTALL), "--dest", str(dest)])
        after_dirs = sorted(p.name for p in dest.iterdir())
        check("install.sh (R14): existing skill dir is never overwritten; nothing else copied", r.returncode == 3 and tree_hash(dest) == before and after_dirs == ["hook-engine"], f"{r.returncode} {after_dirs}")
    r = run(["bash", str(INSTALL), "--dest", "/nonexistent-dir-xyz/skills", "--dry-run"])
    check("install.sh: --dry-run writes nothing", r.returncode == 0 and not Path("/nonexistent-dir-xyz").exists())

    # 8 validator negative tests (R15)
    with tempfile.TemporaryDirectory() as td:
        cp = Path(td) / "pkg"
        shutil.copytree(ROOT, cp, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "dist"))
        (cp / "skills/hook-retention/references/retention-architecture.md").unlink()
        r = run([PY, "-I", str(cp / "scripts/validate_package.py"), str(cp)])
        check("validator (R15): detects a missing referenced file", r.returncode == 1 and "referenced path missing" in r.stdout, r.stdout[-200:])
    with tempfile.TemporaryDirectory() as td:
        cp = Path(td) / "pkg"
        shutil.copytree(ROOT, cp, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "dist"))
        f = cp / "skills/hook-writing/SKILL.md"
        f.write_text(f.read_text(encoding="utf-8").replace("name: hook-writing", "name: wrong-name", 1), encoding="utf-8")
        r = run([PY, "-I", str(cp / "scripts/validate_package.py"), str(cp)])
        check("validator: detects name/directory mismatch", r.returncode == 1 and "!= directory name" in r.stdout)
    with tempfile.TemporaryDirectory() as td:
        cp = Path(td) / "pkg"
        shutil.copytree(ROOT, cp, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "dist"))
        f = cp / "skills/hook-engine/SKILL.md"
        f.write_text(f.read_text(encoding="utf-8") + "\nCites S99 which does not exist.\n", encoding="utf-8")
        r = run([PY, "-I", str(cp / "scripts/validate_package.py"), str(cp)])
        check("validator: detects a citation missing from the ledger", r.returncode == 1 and "S99" in r.stdout)

    # 9 official validator, if the CLI exists
    if shutil.which("claude"):
        r = run(["claude", "plugin", "validate", str(ROOT / "skills")], timeout=180)
        check("claude plugin validate (official) passes on skills/", r.returncode == 0 and "passed" in r.stdout.lower(), r.stdout[-300:] + r.stderr[-300:])
    else:
        print("SKIP claude plugin validate (claude CLI not found)")

    # 10 zip
    if "--zip" in argv:
        z = argv[argv.index("--zip") + 1]
        r = run([PY, "-I", str(VALIDATE), str(ROOT), "--zip", z])
        check("validator: ZIP integrity, contents and secret scan", r.returncode == 0, r.stdout[-400:])

    ok = sum(1 for _, k, _ in results if k)
    print(f"\n{ok}/{len(results)} checks passed")
    if "--write-results" in argv:
        lines = ["# Test results (machine-checkable part)", "",
                 f"Executed with `python3 tests/run_tests.py`. {ok}/{len(results)} checks passed.", "",
                 "| Result | Check |", "|---|---|"]
        lines += [f"| {'PASS' if k else 'FAIL'} | {n} |" for n, k, _ in results]
        lines += ["", "## What these results do and do not show", "",
                  "- They show the helper scripts, installer, validator and fixtures behave as specified, and that the linter's gates fire on the 17 red-team fixtures while accepting the 2 gold fixtures.",
                  "- They do **not** show that model-written hooks are good, that Iraqi phrasing is natural, that claims are true, or that any hook performs better on a platform.",
                  "- The 38 behaviour specifications in `TEST_CASES.md` (12 held-out) are specifications. Eight were dry-run by the package author (`DRY_RUNS.md`, self-graded); no independent grader or live model-run harness was executed in this environment, so the model-driven workflow is NOT verified end to end."]
        (ROOT / "tests/RESULTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
