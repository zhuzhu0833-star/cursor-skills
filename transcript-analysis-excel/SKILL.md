---
name: transcript-analysis-excel
description: >-
  Analyzes academic transcript PDFs (成绩单), extracts courses/GPA/milestones,
  produces a structured multi-sheet Excel workbook, and delivers a Chinese
  analysis summary. Use when the user asks to 分析成绩单, 成绩单转Excel, 成绩单分析,
  transcript analysis, parse transcript PDF, SSR_TSRPT, unofficial transcript,
  or save transcript data as .xlsx.
---

# Transcript Analysis → Excel

Parse an academic transcript PDF, structure the data, export a styled `.xlsx`, and summarize findings for the student/advisor.

## Quick start

1. **Locate input**: user-provided PDF path (e.g. `成绩单/SSR_TSRPT(1).pdf`).
2. **Read source**: open the PDF and extract **all** visible text — student info, every term block, every course row, GPA lines, milestones, footers.
3. **Build JSON** matching [reference.md](reference.md) schema. Do not invent grades or credits.
4. **Export Excel**:
   ```bash
   python3 -m pip install openpyxl pandas
   python3 ~/.cursor/skills/transcript-analysis-excel/scripts/build_transcript_excel.py \
     --input "/path/to/transcript.json" \
     --output-dir "/same/folder/as/pdf"
   ```
5. **Deliver to user**:
   - `{FamilyName}_{GivenName}_{Institution}_Transcript.xlsx` path
   - Chinese analysis summary (see template below)
6. **Ask if missing**: output folder, preferred filename, whether to include in-progress courses.

## Workflow checklist

```
- [ ] PDF read page-by-page; no courses or GPA lines skipped
- [ ] Student info captured (name, ID, institution, print date, document type)
- [ ] Each term: program, plan/subplan, special notes (leave, end of study)
- [ ] Every course: code, description, credits, grade, optional topic line
- [ ] Term GPA + cumulative GPA rows captured per term
- [ ] Milestones / non-course requirements captured
- [ ] transcript.json written
- [ ] build_transcript_excel.py succeeded
- [ ] Analysis summary delivered in chat
```

## Extraction rules

### Course rows
- Preserve course code and description exactly as printed.
- If a `COURSE TOPIC(S):` line follows a course, store it in `course_topic`.
- Credits `0.00` with no grade → mark `(In Progress)` unless source shows another status.
- Non-GPA grades (e.g. `SX`, `P`, `W`, `AU`) → keep verbatim; exclude from grade-distribution sheet.

### Term blocks
- New term starts at headers like `FALL 2023`, `SPRING 2024`, `SUMMER 2022`.
- Capture `Program:`, `Plan:`, `Subplan:`, `Leave of Absence:`, `End of Study:` when present.
- Terms with GPA lines but **no courses** still go in `term_gpa` (e.g. gap semester).

### Academic trajectory
- Infer `academic_history` from program/plan changes across terms.
- Note major transfers, leave of absence, gap terms, current in-progress enrollment.

### Numbers
- Do **not** recalculate GPA unless the user asks.
- Use values exactly as printed on the transcript.

## JSON file shape

Minimal structure (full schema in [reference.md](reference.md)):

```json
{
  "student_info": {
    "university": "Cornell University",
    "student_name": "Matthew Ma",
    "student_id": "5460928",
    "date_printed": "6/2/2026",
    "document_type": "Unofficial Transcript",
    "current_program": "Business",
    "current_major": "Applied Economics & Management Major (AECN-BS)",
    "concentrations": "Entrepreneurship Concentration; Finance Concentration",
    "cumulative_gpa": "3.011",
    "cumulative_credits": "89.00"
  },
  "academic_history": [],
  "courses": [],
  "term_gpa": [],
  "milestones": []
}
```

Save as `{stem}_transcript.json` next to the PDF before running the build script.

## Excel output (6 sheets)

| Sheet | Content |
|-------|---------|
| 学生信息 | Key-value student summary |
| 学业轨迹 | Program/major timeline with notes |
| 课程明细 | All courses by term |
| 学期GPA | Term + cumulative GPA per term |
| 成绩分布 | Count of letter grades (GPA-eligible only) |
| 里程碑 | Non-course milestones (swim test, etc.) |

Default output name: `{FamilyName}_{GivenName}_{InstitutionShort}_Transcript.xlsx`

## Analysis summary template

After exporting, reply with a concise Chinese summary:

```markdown
## 成绩单分析摘要

### 基本信息
| 项目 | 内容 |
|------|------|
| 学校 | … |
| 学生 | … |
| 累计 GPA | … |
| 累计学分 | … |

### 学业轨迹
[Bullet timeline: programs, major changes, leave/gap terms]

### 学期 GPA 走势
[Table: Term | Term GPA | Cum GPA | 备注]

### 课程统计
[Total courses; SX/non-GPA count; in-progress count; grade distribution highlights]

### Excel 文件
[Full path to .xlsx and sheet list]
```

Highlight advisor-relevant signals: major transfer, GPA dips/recovery, leave of absence, weak subject clusters, in-progress credits needed to graduate.

## Edge cases

| Situation | Action |
|-----------|--------|
| Scanned/image-only PDF | Tell user OCR is needed; do not guess text |
| Chinese university transcript | Same workflow; column headers may differ — map to `courses` schema |
| Multiple degrees on one PDF | Separate `academic_history` segments; one combined Excel is OK unless user wants split files |
| Official vs unofficial | Record `document_type` exactly; do not upgrade wording |
| User also wants English translation | Hand off to `translate-academic-credentials` skill separately |

## Additional resources

- JSON schema & grade-code rules: [reference.md](reference.md)
- Worked example (Cornell): [examples.md](examples.md)
- Sample JSON fixture: [examples/matthew_ma_cornell.json](examples/matthew_ma_cornell.json)
