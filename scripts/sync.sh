#!/usr/bin/env bash
# Sync ~/.cursor/skills monorepo with GitHub.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Error: ~/.cursor/skills is not a git repository." >&2
  echo "Clone: git clone https://github.com/zhuzhu0833-star/cursor-skills.git ~/.cursor/skills" >&2
  exit 1
fi

cmd="${1:-status}"
default_msg="chore: update cursor skills"

case "$cmd" in
  pull)
    git pull --rebase origin main
    echo "Pulled latest from origin/main."
    ;;
  push)
    if [[ -n "$(git status --porcelain)" ]]; then
      git add -A
      git commit -m "${2:-$default_msg}"
    else
      echo "Nothing to commit."
    fi
    git push origin main
    echo "Pushed to origin/main."
    ;;
  sync)
    git pull --rebase origin main
    if [[ -n "$(git status --porcelain)" ]]; then
      git add -A
      git commit -m "${2:-$default_msg}"
      git push origin main
      echo "Synced: pulled, committed, pushed."
    else
      echo "Already up to date with origin/main."
    fi
    ;;
  status)
    git status -sb
    echo ""
    git remote -v 2>/dev/null || true
    echo ""
    echo "Skills:"
    find "$ROOT" -maxdepth 2 -name 'SKILL.md' -print | sed "s|$ROOT/||; s|/SKILL.md||" | sort
    ;;
  *)
    echo "Usage: $0 {pull|push|sync|status} [commit-message]" >&2
    exit 1
    ;;
esac
