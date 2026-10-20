#!/usr/bin/env python3
"""validate_package.py - structural QA for the hook-engine package.

Checks (each failure is an ERROR, exit status 1):
  * every skills/<name>/ has SKILL.md with parseable frontmatter, name == dir name,
    allowed keys only, combined description+when_to_use <= 1536 chars, <= 500 lines
  * every relative path mentioned in SKILL.md (references/, scripts/, templates/,
    ${CLAUDE_SKILL_DIR}/...) exists; every file under references/ is referenced
  * required top-level files exist; VERSION is semver
  * RESEARCH_LEDGER.csv: required columns, unique ids, enum values, every S## id cited in
    skills/docs/README exists in the ledger
  * tests/cases.json: schema, >= 30 cases, all 15 categories, held-out >= 8
  * all tests/fixtures/**/*.json parse
  * optional: --zip FILE verifies archive integrity, expected members, no unsafe paths,
    no secret-looking strings
Usage: python3 validate_package.py [PACKAGE_ROOT] [--zip FILE]
Stdlib only; uses PyYAML if installed for stricter frontmatter parsing.
"""
import csv
import json
import re
import sys
import zipfile
from pathlib import Path

ALLOWED_KEYS = {"name", "description", "when_to_use", "argument-hint", "arguments",
                "disable-model-invocation", "user-invocable", "allowed-tools",
                "disallowed-tools", "model", "effort", "context", "agent", "background",
                "hooks", "paths", "shell", "metadata", "license", "compatibility"}
REQUIRED_TOP = ["README.md", "QUICKSTART.md", "RESEARCH_METHODOLOGY.md", "SOURCE_BIBLIOGRAPHY.md",
                "RESEARCH_LEDGER.csv", "TEST_CASES.md", "CHANGELOG.md", "VERSION",
                "docs/HOOK_TAXONOMY.md", "docs/CURIOSITY_AND_RETENTION_FRAMEWORK.md",
                "docs/ARABIC_HOOK_WRITING_GUIDE.md", "docs/SCIENTIFIC_ACCURACY_RULES.md",
                "docs/ANALYTICS_EXPERIMENT_PROTOCOL.md", "docs/EVALUATION_RUBRIC.md",
                "docs/EXAMPLES.md", "scripts/install.sh", "scripts/validate_package.py",
                "scripts/build_docs.py", "tests/run_tests.py", "tests/cases.json"]
LEDGER_COLS = ("source_id title author url source_type publication_date date_accessed access_status "
               "timestamps_verified timestamps concept_extracted evidence_supporting application_20_45s "
               "limitations evidence_class confidence skill_module").split()
ACCESS = {"full_text", "partial_text", "abstract_only", "transcript_text_third_party",
          "description_only", "search_snippet", "not_accessed"}
CLASSES = {"established", "practitioner_heuristic", "opinion", "hypothesis", "contested", "anecdotal"}
CONF = {"certain", "likely", "guess"}
CATEGORIES = {
    "strong_idea_weak_wording", "weak_idea_dramatic_wording", "generic_curiosity_question",
    "counterintuitive_accurate", "visually_demonstrable", "needs_research", "interesting_unsupported",
    "misleading_medical_reject", "stylistically_different_same_idea", "opens_but_fails_retention",
    "excessive_ambiguity", "payoff_mismatch", "iraqi_arabic_naturalness", "visual_demo_over_spoken",
    "duration_audience_variation"}
CASE_FIELDS = ["id", "category", "held_out", "input_brief", "expected_behavior",
               "hard_failures", "quality_criteria", "expected_output_structure"]

errors, warns = [], []


def err(m): errors.append(m)
def warn(m): warns.append(m)


def parse_frontmatter(text, where):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{where}: missing frontmatter")
        return {}
    block = m.group(1)
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(block)
        if not isinstance(data, dict):
            err(f"{where}: frontmatter is not a mapping")
            return {}
        return data
    except ImportError:
        data = {}
        for line in block.splitlines():
            if re.match(r"^[A-Za-z_-]+:", line):
                k, v = line.split(":", 1)
                v = v.strip()
                if v[:1] in "'\"" and v[-1:] == v[:1]:
                    v = v[1:-1]
                data[k] = v
        return data
    except Exception as e:  # yaml error
        err(f"{where}: YAML error: {e}")
        return {}


def check_skills(root):
    skills = root / "skills"
    dirs = sorted(p for p in skills.iterdir() if p.is_dir()) if skills.is_dir() else []
    if not dirs:
        err("skills/ is empty or missing")
    for d in dirs:
        f = d / "SKILL.md"
        w = f"skills/{d.name}"
        if not f.is_file():
            err(f"{w}: SKILL.md missing")
            continue
        text = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(text, w)
        if fm.get("name") != d.name:
            err(f"{w}: frontmatter name {fm.get('name')!r} != directory name")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", d.name):
            err(f"{w}: invalid directory/skill name")
        if d.name == "synced" or d.name.startswith("anthropic-skills"):
            err(f"{w}: reserved name")
        for k in fm:
            if k not in ALLOWED_KEYS:
                err(f"{w}: unknown frontmatter key {k!r}")
        desc = str(fm.get("description", ""))
        if not desc.strip():
            err(f"{w}: description missing")
        if len(desc) + len(str(fm.get("when_to_use", ""))) > 1536:
            err(f"{w}: description+when_to_use exceeds 1536 chars")
        if len(text.splitlines()) > 500:
            err(f"{w}: SKILL.md exceeds 500 lines")
        # referenced paths
        paths = set(re.findall(r"`((?:references|scripts|templates)/[^`\s]+)`", text))
        paths |= {p.split("}/", 1)[1].split()[0] for p in re.findall(r"\$\{CLAUDE_SKILL_DIR\}/[^\s`)]+", text)}
        for p in paths:
            p = p.rstrip(".,;:)")
            if "<" in p or "*" in p:
                continue
            if not (d / p).exists():
                err(f"{w}: referenced path missing: {p}")
        refs = d / "references"
        if refs.is_dir():
            for rf in refs.iterdir():
                if rf.is_file() and f"references/{rf.name}" not in text:
                    warn(f"{w}: references/{rf.name} is not mentioned in SKILL.md")
        # cross-skill mentions like hook-evaluation/scripts/hook_lint.py
        for other, rel in re.findall(r"`(hook-[a-z-]+)/((?:scripts|templates|references)/[^`\s]+)`", text):
            if "<" in rel:
                continue
            if not (skills / other / rel).exists():
                err(f"{w}: cross-skill path missing: {other}/{rel}")
    return {d.name for d in dirs}


def check_files(root):
    for f in REQUIRED_TOP:
        if not (root / f).is_file():
            err(f"required file missing: {f}")
    v = root / "VERSION"
    if v.is_file() and not re.fullmatch(r"\d+\.\d+\.\d+", v.read_text().strip()):
        err("VERSION is not semver")


def check_ledger(root):
    p = root / "RESEARCH_LEDGER.csv"
    if not p.is_file():
        return set()
    rows = list(csv.DictReader(p.open(encoding="utf-8", newline="")))
    if rows and list(rows[0].keys()) != LEDGER_COLS:
        err("ledger columns differ from the specification")
    ids = [r["source_id"] for r in rows]
    if len(ids) != len(set(ids)):
        err("ledger has duplicate source_id")
    for r in rows:
        i = r["source_id"]
        if r["access_status"] not in ACCESS: err(f"ledger {i}: bad access_status {r['access_status']!r}")
        if r["evidence_class"] not in CLASSES: err(f"ledger {i}: bad evidence_class")
        if r["confidence"] not in CONF: err(f"ledger {i}: bad confidence")
        if not r["url"].startswith("http"): err(f"ledger {i}: url not http(s)")
        if r["access_status"] == "not_accessed": err(f"ledger {i}: not_accessed rows must not feed claims")
        if r["timestamps_verified"] == "yes" and not r["timestamps"]: err(f"ledger {i}: verified timestamps empty")
        if r["timestamps_verified"] != "yes" and r["timestamps"]: err(f"ledger {i}: timestamps present but not verified")
        if not r["date_accessed"]: err(f"ledger {i}: date_accessed empty")
    return set(ids)


def check_citations(root, ids):
    cited = set()
    for p in list(root.glob("skills/**/*.md")) + list(root.glob("docs/*.md")) + [root / "README.md"]:
        if p.is_file():
            cited |= set(re.findall(r"\bS(\d{2})\b", p.read_text(encoding="utf-8")))
    for n in sorted(cited):
        if f"S{n}" not in ids:
            err(f"cited source S{n} not in ledger")


def check_cases(root):
    p = root / "tests" / "cases.json"
    if not p.is_file():
        return
    try:
        cases = json.loads(p.read_text(encoding="utf-8"))["cases"]
    except Exception as e:
        err(f"tests/cases.json: {e}")
        return
    if len(cases) < 30:
        err(f"only {len(cases)} test cases (< 30)")
    seen = set()
    for c in cases:
        for f in CASE_FIELDS:
            if f not in c or c[f] in ("", None, []):
                err(f"case {c.get('id')}: missing/empty {f}")
        if c.get("id") in seen: err(f"duplicate case id {c.get('id')}")
        seen.add(c.get("id"))
        if c.get("category") not in CATEGORIES: err(f"case {c.get('id')}: unknown category {c.get('category')!r}")
    missing = CATEGORIES - {c.get("category") for c in cases}
    if missing:
        err(f"categories without a case: {sorted(missing)}")
    if sum(1 for c in cases if c.get("held_out")) < 8:
        err("fewer than 8 held-out cases")


def check_fixtures(root):
    for p in (root / "tests" / "fixtures").rglob("*.json"):
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            err(f"{p.relative_to(root)}: invalid JSON ({e})")


def check_zip(zpath, root):
    try:
        z = zipfile.ZipFile(zpath)
    except Exception as e:
        err(f"zip cannot be opened: {e}")
        return
    bad = z.testzip()
    if bad:
        err(f"zip CRC failure at {bad}")
    names = z.namelist()
    for n in names:
        if n.startswith("/") or ".." in Path(n).parts:
            err(f"unsafe path in zip: {n}")
    tops = {n.split("/", 1)[0] for n in names}
    if len(tops) != 1:
        err(f"zip should have exactly one top-level folder, found {sorted(tops)}")
    top = next(iter(tops)) if tops else ""
    for f in REQUIRED_TOP:
        if f"{top}/{f}" not in names:
            err(f"zip missing {f}")
    for d in (root / "skills").iterdir():
        if d.is_dir() and f"{top}/skills/{d.name}/SKILL.md" not in names:
            err(f"zip missing skills/{d.name}/SKILL.md")
    secret = re.compile(r"(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|ghp_[A-Za-z0-9]{30,})")
    for n in names:
        if n.endswith("/"):
            continue
        try:
            if secret.search(z.read(n).decode("utf-8", "ignore")):
                err(f"secret-looking string in {n}")
        except Exception:
            pass
    if any(n.endswith(".DS_Store") or "__pycache__" in n or n.endswith(".pyc") for n in names):
        err("zip contains junk files (.DS_Store / __pycache__ / .pyc)")


def main(argv):
    root = Path(argv[1]).resolve() if len(argv) > 1 and not argv[1].startswith("--") else Path(__file__).resolve().parent.parent
    check_files(root)
    check_skills(root)
    ids = check_ledger(root)
    check_citations(root, ids)
    check_cases(root)
    check_fixtures(root)
    if "--zip" in argv:
        check_zip(argv[argv.index("--zip") + 1], root)
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
