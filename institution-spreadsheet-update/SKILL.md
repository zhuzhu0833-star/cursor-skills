---
name: institution-spreadsheet-update
description: >-
  Updates each institution row and column in selected Excel/CSV spreadsheets from
  official sources, marks changed cells in red font in the output workbook, and
  generates a PDF change report. Use when the user asks to 更新院校表格, 更新选校表,
  标红更新, 红色字体, 表格信息更新, refresh college spreadsheet, update institution
  table columns, or export a PDF report of spreadsheet changes.
---

# Institution Spreadsheet Update

Update institution data in Excel/CSV files, highlight changes in **red font**, and deliver a PDF change report.

## Quick start

1. **Confirm input**: user-selected `.csv` / `.xlsx` path(s). If multiple files, process each independently.
2. **Read schema**: first row = headers. Identify key column (`school_id` preferred; else `school_name_en` / `school_name_zh`).
3. **Research & update**: for each institution row, verify **every non-metadata column** against official sources. See [reference.md](reference.md).
4. **Build changes JSON** (see format below). Only include cells whose normalized value actually changed.
5. **Apply & report**:
   ```bash
   python3 -m pip install openpyxl fpdf2
   python ~/.cursor/skills/institution-spreadsheet-update/scripts/apply_updates_and_report.py \
     --input "/path/to/table.csv" \
     --changes "/path/to/changes.json" \
     --output-dir "/same/folder/as/input"
   ```
6. **Deliver** to user:
   - `{stem}_updated_{YYYYMMDD}.xlsx` — full table, **changed cells in red**
   - `{stem}_updated_{YYYYMMDD}.csv` — plain CSV mirror (no color)
   - `{stem}_update_report_{YYYYMMDD}.pdf` — Chinese change summary
   - `{stem}_changes_{YYYYMMDD}.json` — machine-readable diff (saved alongside)

## Workflow checklist

```
- [ ] Input file(s) confirmed
- [ ] Baseline captured (current cell values)
- [ ] Each school researched from official / primary sources
- [ ] changes.json written
- [ ] apply_updates_and_report.py executed successfully
- [ ] PDF + highlighted XLSX paths reported to user
```

## Changes JSON format

Write an array of per-school objects:

```json
[
  {
    "school_id": "stanford",
    "school_name_en": "Stanford University",
    "school_name_zh": "斯坦福大学",
    "changes": [
      {
        "field": "test_policy",
        "label_zh": "标化政策",
        "old": "optional",
        "new": "required"
      }
    ]
  }
]
```

Rules:
- `field` must match the spreadsheet header exactly.
- `label_zh` = human-readable column name for the PDF (use [reference.md](reference.md) mapping when available).
- Treat empty, `—`, `N/A`, whitespace-only as equivalent when comparing.
- Always add/update `last_updated` → today's date (`YYYY-MM-DD`) when any field changes.
- Do **not** list unchanged fields.

## Research rules

- **Primary sources first**: official admissions / international-student pages.
- **One school at a time** — do not batch-guess across schools.
- Record evidence in `source_url` and `source_notes` when those columns exist.
- Put concise Chinese context in `notes_zh` when policy wording is nuanced.
- If a field cannot be verified, leave the old value and note it under `## 未能核实` in the PDF (via `unverified` array in JSON — see script `--changes` extended format).

Extended changes file (optional):

```json
{
  "checked_at": "2026-06-17",
  "schools": [ /* same as above */ ],
  "unverified": [
    {"school_id": "foo", "field": "toefl_min_ibt", "reason": "官网未标明最低分"}
  ]
}
```

## Output conventions

| Artifact | Naming | Notes |
|----------|--------|-------|
| Highlighted workbook | `{stem}_updated_{date}.xlsx` | **Red font** (`#FF0000`) on changed cells only |
| Updated CSV | `{stem}_updated_{date}.csv` | Same data, UTF-8 with BOM |
| PDF report | `{stem}_update_report_{date}.pdf` | Chinese summary; see template below |
| Changes JSON | `{stem}_changes_{date}.json` | Archive for next diff |

All outputs go in `--output-dir` (default: same folder as input).

## PDF report structure

The script renders:

1. **封面摘要** — 检查日期、文件路径、院校总数、变更院校数、变更字段总数
2. **变更详情** — per school: 中英校名 + table (`字段 | 旧值 | 新值`)
3. **变更解读** — agent-written `summary_zh` bullets (pass via `--summary-md` or embed in changes JSON as `"summary_zh": ["..."]`)
4. **未能核实** — optional unverified list

After the script runs, **always** add 2–5 bullets of plain-language `summary_zh` interpretation (policy trends, deadline shifts, testing changes) before handing off to the user.

## Multiple files

When the user selects several spreadsheets (e.g. `top30.csv`, `lac_top20.csv`):

1. Process each file separately (own changes JSON + outputs).
2. Optionally merge PDFs or provide one combined `--summary-md` covering cross-file trends.

## Metadata columns (auto-handling)

These columns are updated by the pipeline but **not** highlighted in red:

- `last_updated` — set to check date when any other field changes

## Dependencies

```bash
python3 -m pip install openpyxl fpdf2
```

PDF Chinese rendering uses macOS `PingFang.ttc` or `STHeiti Light.ttc` when available; falls back to bundled font path via `--font`.

## Additional resources

- Column labels & research priorities: [reference.md](reference.md)
