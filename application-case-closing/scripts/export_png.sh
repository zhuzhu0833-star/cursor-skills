#!/usr/bin/env bash
# Export case-closing HTML files to PNG (1080×1920) via Chrome headless.
# Usage: export_png.sh "/path/to/学生/结案"
set -euo pipefail

DIR="${1:?Usage: export_png.sh /path/to/结案/folder}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [[ ! -d "$DIR" ]]; then
  echo "Error: directory not found: $DIR" >&2
  exit 1
fi

if [[ ! -x "$CHROME" ]]; then
  echo "Error: Google Chrome not found at $CHROME" >&2
  exit 1
fi

export_one() {
  local html="$1"
  local png="$2"
  if [[ ! -f "$html" ]]; then
    echo "Skip (not found): $html" >&2
    return 0
  fi
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --window-size=1080,1920 \
    --force-device-scale-factor=1 \
    --run-all-compositor-stages-before-draw \
    --virtual-time-budget=3000 \
    --screenshot="$png" \
    "file://$html" 2>&1 | tail -1
  echo "OK: $png"
}

shopt -s nullglob
for html in "$DIR"/*_祝福卡片.html; do
  base="${html%.html}"
  export_one "$html" "${base}.png"
done

for html in "$DIR"/*_录取成果总结.html; do
  base="${html%.html}"
  export_one "$html" "${base}.png"
done
