#!/usr/bin/env bash
#
# Apply the bundle Claude left in Dropbox, then push.
#
#     cd ~/Projects/highexplosive && ./push.sh
#
# That is the whole workflow. The script refuses rather than guesses: it will
# not run on a dirty tree, will not create a merge commit, and will not push
# anything it has not just fast-forwarded.

set -euo pipefail

# One exact file, not the newest match in a directory. The old version took
# whatever *.bundle was newest in Projects/, which meant any second bundle left
# nearby — the full-history backup, say — could quietly become the thing that
# got pushed.
DEFAULT_BUNDLE="$HOME/Library/CloudStorage/Dropbox/Games/BattleTech/Projects/HighExplosive.net/_Claude/hx-racing.bundle"

cd "$(dirname "$0")"

# --- find the bundle -------------------------------------------------------
bundle="${1:-$DEFAULT_BUNDLE}"
if [ ! -f "$bundle" ]; then
  echo "No bundle at $bundle" >&2
  echo "Pass one explicitly:  ./push.sh /path/to/file.bundle" >&2
  exit 1
fi
echo "Bundle:  $(basename "$bundle")  ($(date -r "$bundle" '+%d %b %H:%M'))"

# --- refuse to run over uncommitted work -----------------------------------
if [ -n "$(git status --porcelain)" ]; then
  echo >&2
  echo "You have uncommitted changes. Commit or stash them first:" >&2
  git status --short >&2
  exit 1
fi

# --- apply -----------------------------------------------------------------
before=$(git rev-parse --short HEAD)
git fetch "$bundle" HEAD

if git merge-base --is-ancestor FETCH_HEAD HEAD 2>/dev/null; then
  echo "Already applied — nothing to do."
  exit 0
fi

# --ff-only, so a bundle built on a stale base stops here rather than
# inventing a merge commit.
if ! git merge --ff-only FETCH_HEAD; then
  echo >&2
  echo "Not a fast-forward. The bundle was built on a different base than" >&2
  echo "your current HEAD ($before). Tell Claude, and don't force anything." >&2
  exit 1
fi

echo
git --no-pager log --oneline "$before"..HEAD
echo

# --- publish ---------------------------------------------------------------
git push
echo
echo "Pushed. The build takes about 40 seconds:"
echo "  https://github.com/comstar3025/highexplosive/actions"
