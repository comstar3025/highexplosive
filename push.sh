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

# One exact file, not the newest match in a directory. An older version took
# whatever *.bundle was newest in Projects/, which meant any second bundle left
# nearby — the full-history backup, say — could quietly become the thing that
# got pushed.
#
# The name is site-update.bundle because it carries whatever changed: the
# simulator, the comparator, the racing page, the splash. It was called
# hx-racing.bundle until the v1.3 release, from the first thing it ever
# carried, which made every later push look like it was touching the racing
# page. It was not.
BUNDLE_DIR="$HOME/Library/CloudStorage/Dropbox/Games/BattleTech/Projects/HighExplosive.net/_Claude"
DEFAULT_BUNDLE="$BUNDLE_DIR/site-update.bundle"
LEGACY_BUNDLE="$BUNDLE_DIR/hx-racing.bundle"

cd "$(dirname "$0")"

# --- find the bundle -------------------------------------------------------
bundle="${1:-$DEFAULT_BUNDLE}"
if [ ! -f "$bundle" ]; then
  echo "No bundle at $bundle" >&2
  # Transitional: say so plainly rather than leaving a stale bundle under the
  # old name looking like the answer. Never apply it silently — it predates
  # the rename and is therefore already pushed.
  if [ "$bundle" = "$DEFAULT_BUNDLE" ] && [ -f "$LEGACY_BUNDLE" ]; then
    echo >&2
    echo "There is still a bundle under the old name:" >&2
    echo "  $LEGACY_BUNDLE" >&2
    echo "That one predates the rename and has already been pushed. It is not" >&2
    echo "the release you are looking for — tell Claude the new bundle is" >&2
    echo "missing rather than reaching for it." >&2
  fi
  echo >&2
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

# --- catch up with the remote first ----------------------------------------
# A release uploaded through GitHub's web UI lands on origin/main and never
# reaches this clone, so the next bundle is built on a base this repo does not
# have and `git fetch <bundle>` fails with "Repository lacks these prerequisite
# commits". That happened twice before this guard existed. Fast-forwarding to
# origin/main first heals it; --ff-only so real divergence stops here instead
# of being papered over with a merge.
echo "Fetching origin…"
git fetch --quiet origin
if [ -n "$(git rev-list --count HEAD..origin/main 2>/dev/null)" ] &&
   [ "$(git rev-list --count HEAD..origin/main)" -gt 0 ]; then
  behind=$(git rev-list --count HEAD..origin/main)
  echo "Behind origin/main by $behind commit(s) — fast-forwarding first."
  if ! git merge --ff-only origin/main; then
    echo >&2
    echo "Cannot fast-forward to origin/main: this clone has commits the" >&2
    echo "remote does not. Tell Claude what \`git log --oneline" >&2
    echo "origin/main..HEAD\` says, and don't force anything." >&2
    exit 1
  fi
  echo
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
