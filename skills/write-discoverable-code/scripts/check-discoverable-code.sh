#!/usr/bin/env bash
# check-discoverable-code.sh — checks the machine-checkable subset of
# write-discoverable-code against a target directory.
#
# Usage: check-discoverable-code.sh <target-dir>
# Exit: 0 = no enforced violations, 1 = enforced violations, 2 = misuse.
#
# Checks:
#   1. Advisory TypeScript/Python type signals for manual public-API review:
#        TS: : any, as any, : Object, : Function
#        Python: : Any (from typing.Any), untyped *name or **name
#   2. Legacy paths with a whole legacy-name component that lack @deprecated
#
# Requires: rg (ripgrep).

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $(basename "$0") <target-dir>" >&2
  exit 2
fi

TARGET="$1"
if [[ ! -d "$TARGET" ]]; then
  echo "error: '$TARGET' is not a directory" >&2
  exit 2
fi

if ! command -v rg >/dev/null 2>&1; then
  echo "error: required tool 'rg' not on PATH" >&2
  exit 2
fi

violations=0

# --- Check 1a: advisory TypeScript type signals ---
echo "== Check 1a: TypeScript type signals (advisory) =="
ts_hits=$(rg -n --type ts '(: any\b|as any\b|: Object\b|: Function\b)' "$TARGET" 2>/dev/null || true)
if [[ -n "$ts_hits" ]]; then
  echo "  REVIEW TS TYPES (confirm whether each occurrence is on a public API):"
  echo "$ts_hits" | sed 's/^/    /'
fi

# --- Check 1b: advisory Python type signals ---
echo "== Check 1b: Python type signals (advisory) =="
# : Any at parameter or return position.
py_any=$(rg -n --type py ': Any\b|-> Any\b' "$TARGET" 2>/dev/null || true)
# Untyped named variadics in single-line def signatures: no colon follows the name.
py_variadics=$(rg -n --type py 'def[[:space:]]+[a-zA-Z_][a-zA-Z0-9_]*[[:space:]]*\([^)]*\*\*?[a-zA-Z_][a-zA-Z0-9_]*[[:space:]]*[,)]' "$TARGET" 2>/dev/null || true)
py_hits="${py_any}${py_any:+$'\n'}${py_variadics}"
if [[ -n "${py_hits//[$'\n ']/}" ]]; then
  echo "  REVIEW PYTHON TYPES (confirm whether each occurrence is on a public API):"
  echo "$py_hits" | grep -v '^$' | sed 's/^/    /'
fi

# --- Check 2: legacy paths without @deprecated marker ---
echo "== Check 2: legacy paths without @deprecated marker =="
mapfile -t legacy < <(rg --files "$TARGET" 2>/dev/null | rg -i '(^|/|[_-])(legacy|deprecated|old)([_./-]|$)' || true)
for f in "${legacy[@]}"; do
  if ! rg -q '@deprecated' "$f" 2>/dev/null; then
    echo "    UNMARKED LEGACY: $f"
    violations=$((violations + 1))
  fi
done

echo
if [[ $violations -eq 0 ]]; then
  echo "OK — no enforced discoverability violations found in $TARGET"
  exit 0
else
  echo "FAIL — $violations discoverability violation(s) in $TARGET"
  exit 1
fi
