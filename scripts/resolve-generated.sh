#!/usr/bin/env bash
# Resolve merge conflicts in generated output.
#
# The scheduled job commits a refreshed snapshot every 30 minutes, so editing
# locally and pushing will sometimes collide with it. Only one file in that
# collision holds anything irreplaceable:
#
#   data/history.jsonl  the append-only metric database every anomaly
#                       baseline is computed from. .gitattributes merges it
#                       with merge=union, and history.load() deduplicates by
#                       timestamp, so it resolves itself.
#
#   everything else     docs/report.{md,json}, docs/history.json,
#                       data/latest.json are derived in full from the line
#                       above plus a fresh collection. A conflict in them
#                       carries no information; regenerating is the fix.
#
# Usage, mid-rebase or mid-merge:
#   ./scripts/resolve-generated.sh && git rebase --continue
set -euo pipefail
cd "$(dirname "$0")/.."

DERIVED=(data/latest.json docs/history.json docs/report.json docs/report.md)

for f in "${DERIVED[@]}"; do
  # --theirs during a rebase is the commit being replayed, i.e. the local work.
  git checkout --theirs -- "$f" 2>/dev/null || true
  git add "$f" 2>/dev/null || true
done

if git diff --name-only --diff-filter=U | grep -q .; then
  echo "Conflicts remain in files this script does not own:"
  git diff --name-only --diff-filter=U
  exit 1
fi

echo "Generated files resolved. Regenerating from the merged history..."
python3 -m sentinel.main --once
git add data docs
echo "Done. Continue the rebase, then push."
