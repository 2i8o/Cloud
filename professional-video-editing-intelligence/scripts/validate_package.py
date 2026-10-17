#!/usr/bin/env python3
"""Validate this skill package (run after editing it).

Checks: SKILL.md frontmatter (first line '---', name matches folder and is lowercase-hyphen <=64,
description present and <=1024 chars), file references resolve, no empty files, no placeholder
words, no obvious secrets, and that brand-specific names appear only in allowed files.

  python validate_package.py [package_dir]      # defaults to this script's parent folder
Exit 0 = all checks passed, 1 = failures.
"""
import os
import re
import sys

PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum|XXX)\b", re.I)
SECRETS = re.compile(r"(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}", re.I)
BRAND = re.compile(r"Abbas|OptiNest|عباس")
BRAND_ALLOWED = {"SKILL.md", "README.md", "BUILD-LOG.md", os.path.join("brand", "abbas-abdulmunem.md"),
                 os.path.join("examples", "educational-reel.md"), os.path.join("references", "learning-sources.md"),
                 os.path.join("scripts", "validate_package.py")}
EXTERNAL_OK = {"brand.ts", "theme.ts", "STANDARDS.md"}


def main():
    root = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    fails, notes = [], []

    def fail(msg):
        fails.append(msg)

    skill = os.path.join(root, "SKILL.md")
    if not os.path.isfile(skill):
        print("FAIL: SKILL.md missing at", root)
        return 1
    text = open(skill, encoding="utf-8").read()
    lines = text.split("\n")
    if lines[0].strip() != "---":
        fail("SKILL.md must start with '---' on line 1")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        end = None
        fail("SKILL.md frontmatter has no closing '---'")
    fm = {}
    if end:
        cur = None
        for ln in lines[1:end]:
            m = re.match(r"^([A-Za-z_\-]+):\s*(.*)$", ln)
            if m:
                cur = m.group(1)
                fm[cur] = m.group(2).strip()
            elif cur and ln.startswith((" ", "\t")):
                fm[cur] += " " + ln.strip()
    name = fm.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        fail(f"name '{name}' must be lowercase letters/digits/hyphens, <=64 chars")
    if name != os.path.basename(root):
        notes.append(f"folder '{os.path.basename(root)}' differs from name '{name}' (command name comes from the folder)")
    desc = fm.get("description", "")
    if not desc:
        fail("description missing")
    elif len(desc) > 1024:
        fail(f"description is {len(desc)} chars (>1024 limit for claude.ai upload)")
    notes.append(f"description length {len(desc)} chars; SKILL.md {len(lines)} lines")
    if len(lines) > 500:
        fail("SKILL.md exceeds 500 lines")

    all_files = []
    for d, _, fs in os.walk(root):
        for f in fs:
            all_files.append(os.path.join(d, f))
    basenames = {os.path.basename(p) for p in all_files}

    for p in all_files:
        rel = os.path.relpath(p, root)
        if os.path.getsize(p) == 0:
            fail(f"empty file: {rel}")
        if rel.endswith((".md", ".py")):
            t = open(p, encoding="utf-8").read()
            if PLACEHOLDERS.search(t) and rel != os.path.join("scripts", "validate_package.py"):
                fail(f"placeholder word in {rel}: {PLACEHOLDERS.search(t).group(0)}")
            if SECRETS.search(t) and rel != os.path.join("scripts", "validate_package.py"):
                fail(f"possible secret in {rel}")
            if BRAND.search(t) and rel not in BRAND_ALLOWED:
                fail(f"brand-specific name outside allowed files: {rel}")
            if rel.endswith(".md"):
                for m in re.finditer(r"`([A-Za-z0-9_\-./]+\.(?:md|py))`", t):
                    ref = m.group(1)
                    if "*" in ref or ref in EXTERNAL_OK:
                        continue
                    cands = [os.path.join(root, ref), os.path.join(os.path.dirname(p), ref)]
                    if not any(os.path.exists(c) for c in cands) and not ("/" not in ref and ref in basenames):
                        fail(f"unresolved reference in {rel}: {ref}")
                for m in re.finditer(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", t):
                    ref = m.group(1)
                    if ref.startswith(("http://", "https://", "mailto:")):
                        continue
                    if not os.path.exists(os.path.join(os.path.dirname(p), ref)):
                        fail(f"broken link in {rel}: {ref}")

    for n in notes:
        print("NOTE:", n)
    if fails:
        for f in fails:
            print("FAIL:", f)
        return 1
    print(f"OK: {len(all_files)} files checked, no failures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
