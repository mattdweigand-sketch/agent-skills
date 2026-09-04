# Reference integrity and migration checks

Read before proposing a move. A navigable result does not prove that the move preserved its consumers.

## Before proposing

1. Identify the durable workspace root and a usable backup or recovery path. A local persistent folder is valid; publishing is not a prerequisite.
2. Enumerate references within the scoped workspace, including relative paths inside files being moved and symlinks pointing into or out of the moved tree. Ask the owner about external consumers such as other repositories, configurations, agents, and scheduled jobs. Record unknown coverage rather than claiming an exhaustive search.
3. Record each old path, destination, role, known referrers, and planned reference updates in the migration map. A file with a live referrer is held unless the reference will remain valid or its update is authorized in the same migration. Absence of obvious use does not establish that a file is dead.
4. Run the read-only preflight for every source/destination pair. Also compare planned destinations with each other for duplicate, overlapping, and case-folded names. Surface conflicts before approval; do not overwrite a destination.

## Read-only helper

From this skill directory, with Python 3:

```sh
python3 scripts/migration_preflight.py /absolute/source /absolute/destination
python3 scripts/migration_preflight.py /absolute/source /absolute/destination --verify
```

The first command requires an absent destination and checks existing ancestor names, overlapping source/destination trees, and case-folded name collisions at the destination and within the source tree. The second requires a completed copy and compares the relative directory/file inventory and whole-file SHA-256 hashes, including binary and Office files. Exit 0 means the requested checks passed; exit 1 means a conflict, mismatch, or filesystem error. Reports are JSON on stdout. Invalid command syntax exits 2.

Both commands only read. They reject symlinks and special files within the selected trees or their path components rather than following them. Such inputs need a separately reviewed migration that preserves link semantics. The helper does not find references, compare multiple proposed moves, check permissions or extended attributes for parity, or prove that an active writer has stopped. Run on quiescent inputs and recheck if they change. A successful report is evidence for review, not authorization to delete.

## Copy, verify, then remove

1. After the migration scope is authorized, copy to the exact destination checked by preflight, using a copy operation that refuses existing destinations. Keep the original and copied bytes unchanged during verification.
2. Run `--verify`. File counts alone are insufficient: every relative path, file type, and whole-file hash must match. Apply the same byte check to ZIP-based Office files; do not substitute unpacked-content comparisons for a plain copy.
3. Only after parity passes, perform the authorized removal and reference updates. Apply content edits after the unchanged copy has been verified. If a consumer needs a pointer at the old path, include that pointer in the approved map.
4. Recheck all previously resolving references from their new locations, then run the affected walk-test checks. A path that still resolves to the wrong file is also a failure.

If copying or verification fails, retain the source and report the partial destination. Do not continue to source removal. Resume only after resolving the failure and repeating the affected checks within the authorized scope.
