#!/usr/bin/env bash
# install.sh - copy the hook-engine skills into a Claude Code skills directory.
#
# Safety: all-or-nothing and NON-DESTRUCTIVE. If any target skill directory
# already exists, nothing is copied and the script exits with status 3.
# It never deletes, renames or modifies anything that already exists.
#
# Usage: scripts/install.sh [--dest DIR] [--dry-run]
#   default DEST: $HOME/.claude/skills   (personal skills, all projects)
#   project-only: scripts/install.sh --dest /path/to/repo/.claude/skills
set -euo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$SELF_DIR/../skills"
DEST="${HOME}/.claude/skills"
DRY=0

while [ $# -gt 0 ]; do
  case "$1" in
    --dest) DEST="${2:?--dest needs a directory}"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) sed -n '2,12p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

[ -d "$SRC" ] || { echo "skills source not found: $SRC" >&2; exit 2; }

names=()
for d in "$SRC"/*/; do
  n="$(basename "$d")"
  [ -f "$d/SKILL.md" ] || { echo "skip (no SKILL.md): $n"; continue; }
  case "$n" in synced|anthropic-skills*) echo "refusing reserved name: $n" >&2; exit 2 ;; esac
  names+=("$n")
done
[ "${#names[@]}" -gt 0 ] || { echo "no skills found in $SRC" >&2; exit 2; }

conflicts=0
for n in "${names[@]}"; do
  if [ -e "$DEST/$n" ]; then
    echo "EXISTS: $DEST/$n  (will not overwrite)" >&2
    conflicts=$((conflicts + 1))
  fi
done
if [ "$conflicts" -gt 0 ]; then
  echo "Aborted: $conflicts existing skill(s) would be overwritten. Nothing was changed." >&2
  echo "Remove or rename them yourself if you really want to replace them." >&2
  exit 3
fi

if [ "$DRY" -eq 1 ]; then
  printf 'dry run - would install into %s:\n' "$DEST"; printf '  %s\n' "${names[@]}"; exit 0
fi

mkdir -p "$DEST"
for n in "${names[@]}"; do
  cp -R "$SRC/$n" "$DEST/$n"
  [ -f "$DEST/$n/SKILL.md" ] || { echo "copy failed for $n" >&2; exit 1; }
  echo "installed: $DEST/$n"
done
echo "Done. Start a new Claude Code session (or run /skills) and invoke /hook-engine."
