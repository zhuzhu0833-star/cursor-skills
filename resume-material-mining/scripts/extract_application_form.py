#!/usr/bin/env python3
"""Extract resume-relevant sections from Chinese 申研表 .docx intake forms."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("Error: python-docx required. Install: pip install python-docx", file=sys.stderr)
    sys.exit(1)

VAGUE_PATTERNS = re.compile(
    r"参与|了解|协助|学习|认识|熟悉|接触|负责|支持", re.IGNORECASE
)
CONTRIBUTION_LABELS = ("贡献", "成绩", "主要贡献")


def _cell_text(cell) -> str:
    return " ".join(cell.text.split())


def _row_map(row) -> dict[str, str]:
    """Map label -> value for 2-col or 4-col intake table rows."""
    texts = [_cell_text(c) for c in row.cells]
    # Deduplicate merged cells (common in Word tables)
    deduped: list[str] = []
    for t in texts:
        if not deduped or t != deduped[-1]:
            deduped.append(t)
    if len(deduped) >= 2 and deduped[0] != deduped[1]:
        return {deduped[0]: deduped[1]}
    # Multi-field rows: label, value, label, value, ...
    out: dict[str, str] = {}
    i = 0
    while i < len(deduped) - 1:
        label, value = deduped[i], deduped[i + 1]
        if label and value and label != value:
            out[label] = value
        i += 2
    return out


def _table_title(table) -> str:
    if not table.rows:
        return ""
    first = _cell_text(table.rows[0].cells[0])
    return first


def _is_internship_table(title: str) -> bool:
    return "工作" in title or "实习" in title


def _is_education_table(title: str) -> bool:
    return "教育经历" in title or "大学" in title and "研究生" in title


def _is_activity_table(title: str) -> bool:
    return "其他活动" in title or "活动经历" in title


def _is_academic_project_table(title: str) -> bool:
    return "学术项目" in title


def _is_award_table(title: str) -> bool:
    return "奖项" in title or "荣誉" in title


def _is_research_table(title: str) -> bool:
    return "研究经历" in title


def _parse_block(rows: list, start: int) -> tuple[dict, int]:
    """Parse one experience block starting at date row."""
    block: dict[str, str] = {}
    i = start
    while i < len(rows):
        row_map = _row_map(rows[i])
        if not row_map:
            i += 1
            continue
        label = next(iter(row_map))
        # Next block starts at new date range row after first field
        if i > start and "起止日期" in label:
            break
        block.update(row_map)
        i += 1
    return block, i


def _parse_repeating_blocks(table) -> list[dict]:
    rows = table.rows
    blocks: list[dict] = []
    i = 0
    while i < len(rows):
        row_map = _row_map(rows[i])
        if any("起止日期" in k for k in row_map):
            block, next_i = _parse_block(rows, i)
            if block.get("起止日期") or block.get("单位名称（中英文）") or block.get("活动名称"):
                blocks.append(block)
            i = next_i
        else:
            i += 1
    return blocks


def _parse_education(table) -> list[dict]:
    rows = table.rows
    entries: list[dict] = []
    current: dict[str, str] | None = None
    marker_re = re.compile(r"教育经历[一二三四五六七八九十\d]+")
    for row in rows:
        texts = [_cell_text(c) for c in row.cells]
        deduped: list[str] = []
        for t in texts:
            if not deduped or t != deduped[-1]:
                deduped.append(t)
        joined = " ".join(deduped)
        if marker_re.search(joined):
            if current:
                entries.append(current)
            current = {"marker": marker_re.search(joined).group()}
            continue
        row_map = _row_map(row)
        if row_map and current is not None:
            current.update(row_map)
    if current:
        entries.append(current)
    return [e for e in entries if e.get("学校名称（中英文）") or e.get("大学名称（中英文）")]


def _gap_flags(block: dict) -> list[str]:
    flags: list[str] = []
    for k, v in block.items():
        if any(x in k for x in CONTRIBUTION_LABELS) and not v.strip():
            flags.append("empty_contribution")
    duty_keys = [k for k in block if "工作内容" in k or "工作职责" in k or "主要负责" in k]
    for k in duty_keys:
        val = block.get(k, "")
        if val and len(val) < 30:
            flags.append("brief_duty")
        if val and VAGUE_PATTERNS.search(val) and not re.search(r"\d", val):
            flags.append("vague_no_numbers")
    return flags


def extract(doc_path: Path) -> dict:
    doc = Document(str(doc_path))
    result: dict = {
        "source": str(doc_path),
        "education": [],
        "internships": [],
        "activities": [],
        "academic_projects": [],
        "awards": [],
        "research_notes": [],
        "gaps_summary": [],
    }

    for table in doc.tables:
        title = _table_title(table)
        if _is_education_table(title):
            result["education"] = _parse_education(table)
        elif _is_internship_table(title):
            blocks = _parse_repeating_blocks(table)
            for b in blocks:
                b["_gaps"] = _gap_flags(b)
                result["internships"].append(b)
        elif _is_activity_table(title):
            result["activities"] = _parse_repeating_blocks(table)
        elif _is_academic_project_table(title):
            # Academic table uses course blocks, not date rows — flatten pairs
            proj: dict[str, str] = {}
            for row in table.rows:
                proj.update(_row_map(row))
            if any(v for k, v in proj.items() if "课程" in k or "项目" in k):
                result["academic_projects"].append(proj)
        elif _is_award_table(title):
            for row in table.rows[2:]:
                cells = [_cell_text(c) for c in row.cells]
                if len(cells) >= 3 and cells[1].strip():
                    result["awards"].append(
                        {"date": cells[1], "name": cells[2], "level": cells[3] if len(cells) > 3 else ""}
                    )
        elif _is_research_table(title):
            result["research_notes"].append(title)

    # Summarize gaps
    for idx, intern in enumerate(result["internships"], 1):
        org = intern.get("单位名称（中英文）", intern.get("起止日期", f"Internship {idx}"))
        gaps = intern.get("_gaps", [])
        if gaps:
            result["gaps_summary"].append({"experience": org[:80], "flags": gaps})

    empty_sections = []
    if not any(a.get("name") for a in result["awards"]):
        pass  # awards may still have entries
    if not result["activities"] or all(not b.get("活动名称") for b in result["activities"]):
        empty_sections.append("activities")
    if not result["academic_projects"] or all(
        not p.get("课程上完成的项目作业名") for p in result["academic_projects"]
    ):
        empty_sections.append("academic_projects")
    result["empty_sections"] = empty_sections

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract 申研表 experiences for resume mining")
    parser.add_argument("docx", type=Path, help="Path to 1-申研表.docx")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if not args.docx.exists():
        print(f"File not found: {args.docx}", file=sys.stderr)
        sys.exit(1)

    data = extract(args.docx)

    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    print(f"Source: {data['source']}\n")

    print("=== EDUCATION ===")
    for e in data["education"]:
        school = e.get("学校名称（中英文）", e.get("大学名称（中英文）", ""))
        dates = e.get("起止日期（年月日－年月日）", e.get("起止日期", ""))
        major = e.get("专业名称（中英文）", "")
        gpa = e.get("GPA", "")
        print(f"- {school} | {dates} | {major} | GPA: {gpa or '(empty)'}")

    print("\n=== INTERNSHIPS ===")
    for i, intern in enumerate(data["internships"], 1):
        org = intern.get("单位名称（中英文）", "")
        dates = intern.get("起止日期（年月日－年月日）", "")
        dept = intern.get("部门名称", "")
        role = intern.get("职位", "")
        duty = intern.get("工作内容/工作职责（请首先考虑与申请专业相关的方面）", "")
        contrib = intern.get("工作/实习期间做出的贡献/成绩", "")
        gaps = ", ".join(intern.get("_gaps", [])) or "ok"
        print(f"\n[{i}] {org}")
        print(f"    Dates: {dates} | Dept: {dept} | Role: {role}")
        print(f"    Duty: {duty[:120]}{'...' if len(duty) > 120 else ''}")
        print(f"    Contribution: {contrib or '(EMPTY)'}")
        print(f"    Flags: {gaps}")

    print("\n=== AWARDS ===")
    for a in data["awards"]:
        print(f"- {a.get('date')} | {a.get('name')} | {a.get('level')}")

    print("\n=== EMPTY SECTIONS TO PROBE ===")
    print(", ".join(data["empty_sections"]) or "none detected")

    print("\n=== GAP SUMMARY ===")
    for g in data["gaps_summary"]:
        print(f"- {g['experience']}: {', '.join(g['flags'])}")


if __name__ == "__main__":
    main()
