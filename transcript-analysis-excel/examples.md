# Example: Cornell Unofficial Transcript

Source: `SSR_TSRPT(1).pdf` — Matthew Ma, Student ID 5460928.

## Extracted student_info

```json
{
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
}
```

## Academic trajectory (inferred)

| Period | Program | Action |
|--------|---------|--------|
| SUMMER 2022 | Continuing Education | Summer College, 1 course |
| FALL 2023 – SPRING 2024 | AAP / URGN-BS | Urban & Regional Studies year 1 |
| FALL 2024 – present | Business / AEM-BS | Major transfer to Dyson |
| SPRING 2025 | Business | Leave of Absence 2025-05-18 |
| FALL 2025 | Business | No enrollment |
| FALL 2026 | Business | 5 courses in progress |

## Sample course rows

```json
[
  {
    "term": "FALL 2023",
    "program": "Architecture, Art and Planning",
    "plan": "Urban & Regional Studies Major (URGN-BS)",
    "end_of_study": "",
    "course_code": "ENGL 1158",
    "course_description": "FWS: AMERICAN VOICES",
    "credits": 3.0,
    "grade": "A-",
    "course_topic": "FWS: HAUNTINGS IN NARRATIVE"
  },
  {
    "term": "FALL 2024",
    "program": "Business",
    "plan": "Applied Economics & Management Major (AECN-BS)",
    "end_of_study": "",
    "course_code": "AEM 2225",
    "course_description": "FINANCIAL ACCOUNTING FOR DYSON",
    "credits": 4.0,
    "grade": "C-",
    "course_topic": ""
  },
  {
    "term": "FALL 2026",
    "program": "Business",
    "plan": "Applied Economics & Management Major (AECN-BS)",
    "end_of_study": "",
    "course_code": "AEM 3200",
    "course_description": "BUSINESS LAW",
    "credits": 0.0,
    "grade": "(In Progress)",
    "course_topic": ""
  }
]
```

## Term GPA highlights

| Term | Term GPA | Cum GPA | Note |
|------|----------|---------|------|
| SUMMER 2022 | 4.000 | 4.000 | |
| SPRING 2024 | 3.780 | 3.607 | Best URGN term |
| FALL 2024 | 2.279 | 3.164 | Post-transfer dip |
| SPRING 2025 | 2.617 | 3.000 | Before LOA |
| SPRING 2026 | 3.043 | 3.011 | Recovery after return |

## Grade distribution (29 GPA-eligible courses)

A-series: 9 | B-series: 9 | C-series: 11

SX (non-GPA): 4 courses — AAP 1100, CRP 1106, PE 1440, AEM 1101

## Output

```
成绩单/Matthew_Ma_Cornell_Transcript.xlsx
```

Sheets: 学生信息, 学业轨迹, 课程明细, 学期GPA, 成绩分布, 里程碑

## Advisor talking points (from this example)

- URGN → AEM transfer correlates with GPA drop; Spring 2026 shows partial recovery.
- Finance concentration courses (AEM 4570/4590/4670) cluster around B/C+ — worth probing in essays/interviews.
- LOA + Fall 2025 gap needs narrative context for applications.
- 5 in-progress Fall 2026 courses will affect final cum GPA at graduation.
