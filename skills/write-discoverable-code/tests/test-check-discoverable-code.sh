#!/usr/bin/env bash
# Regression tests for scripts/check-discoverable-code.sh.
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CHECKER="$SKILL_DIR/scripts/check-discoverable-code.sh"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

assert_contains() {
  local needle="$1"
  local file="$2"
  if ! rg -Fq "$needle" "$file"; then
    echo "expected '$needle' in $file" >&2
    cat "$file" >&2
    exit 1
  fi
}

assert_not_contains() {
  local needle="$1"
  local file="$2"
  if rg -Fq "$needle" "$file"; then
    echo "did not expect '$needle' in $file" >&2
    cat "$file" >&2
    exit 1
  fi
}

# Ordinary “folder” names and testless configuration files must not fail.
mkdir -p "$TMP/modern"
printf 'def locate_folder():\n    return "active"\n' > "$TMP/modern/folder_fallbacks.py"
printf 'export default {};\n' > "$TMP/modern/vite.config.ts"
"$CHECKER" "$TMP/modern" > "$TMP/modern.out"
assert_not_contains "UNMARKED LEGACY" "$TMP/modern.out"
assert_not_contains "MISSING TEST" "$TMP/modern.out"

# Whole legacy components remain enforced.
mkdir -p "$TMP/legacy"
printf 'def parse():\n    return None\n' > "$TMP/legacy/old_parser.py"
if "$CHECKER" "$TMP/legacy" > "$TMP/legacy.out"; then
  echo "expected an unmarked legacy path to fail" >&2
  exit 1
fi
assert_contains "UNMARKED LEGACY" "$TMP/legacy.out"

# Type signals are advisory, detect any variadic identifier, and ignore typed ones.
mkdir -p "$TMP/types"
cat > "$TMP/types/internal.ts" <<'EOF'
function parseInternal(value: unknown): string {
  const decoded: any = JSON.parse(String(value));
  return String(decoded.value);
}
EOF
cat > "$TMP/types/variadics.py" <<'EOF'
def collect(*values):
    return values

def configure(**options):
    return options

def typed(*values: str, **options: str):
    return values, options
EOF
"$CHECKER" "$TMP/types" > "$TMP/types.out"
assert_contains "REVIEW TS TYPES" "$TMP/types.out"
assert_contains "REVIEW PYTHON TYPES" "$TMP/types.out"
assert_contains "variadics.py:1" "$TMP/types.out"
assert_contains "variadics.py:4" "$TMP/types.out"
assert_not_contains "variadics.py:7" "$TMP/types.out"

echo "PASS: check-discoverable-code regression tests"
