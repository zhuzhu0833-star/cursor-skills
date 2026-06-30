# Transcript JSON Schema & Reference

## `student_info` fields

| Field | Required | Notes |
|-------|----------|-------|
| `university` | yes | Official English name |
| `student_name` | yes | As printed |
| `student_id` | yes | |
| `date_printed` | yes | As printed |
| `document_type` | yes | e.g. Unofficial Transcript, Official Transcript |
| `current_program` | no | Latest program/school |
| `current_major` | no | Latest plan/major line |
| `concentrations` | no | Subplans, minors, tracks — semicolon-separated |
| `cumulative_gpa` | yes | Final cum GPA on transcript |
| `cumulative_credits` | yes | Final cum credits earned |

## `academic_history` row

| Field | Required | Example |
|-------|----------|---------|
| `period` | yes | `FALL 2023 - SPRING 2024` |
| `school_program` | yes | `Architecture, Art and Planning (AAP)` |
| `major_plan` | yes | `Urban & Regional Studies (URGN-BS)` |
| `action` | yes | `Undergraduate Year 1` / `Major transfer` / `Leave of Absence` |

## `courses` row

| Field | Required | Example |
|-------|----------|---------|
| `term` | yes | `FALL 2023` |
| `program` | yes | `Architecture, Art and Planning` |
| `plan` | yes | `Urban & Regional Studies Major (URGN-BS)` |
| `end_of_study` | no | `Leave of Absence: 2025-05-18` or `2022-08-21` |
| `course_code` | yes | `AEM 3991` |
| `course_description` | yes | `GLOBAL BUSINESS STRATEGY` |
| `credits` | yes | numeric, e.g. `3.00` |
| `grade` | yes | letter grade, `SX`, or `(In Progress)` |
| `course_topic` | no | Topic sub-line if present |

## `term_gpa` row

| Field | Required | Example |
|-------|----------|---------|
| `term` | yes | `SPRING 2024` |
| `program` | yes | |
| `plan` | yes | |
| `term_gpa` | yes | numeric |
| `term_credits` | yes | numeric |
| `cum_gpa` | yes | numeric |
| `cum_credits` | yes | numeric |
| `notes` | no | e.g. `No courses enrolled`, `Major change` |

## `milestones` row

| Field | Required | Example |
|-------|----------|---------|
| `program` | yes | |
| `milestone` | yes | `Swim Test` |
| `level` | no | `REQUIREMENT` |
| `status` | no | `Completed` |
| `date_completed` | no | `08/22/2023` |
| `attempt_status` | no | |
| `attempted_on` | no | |

## Grade codes (US transcripts)

### GPA-eligible (include in 成绩分布)
`A+`, `A`, `A-`, `B+`, `B`, `B-`, `C+`, `C`, `C-`, `D+`, `D`, `D-`, `F`

### Non-GPA (exclude from distribution, still list in 课程明细)
| Code | Typical meaning |
|------|-----------------|
| `SX` | Satisfactory/experience — no GPA impact |
| `P` / `S` | Pass / Satisfactory |
| `W` | Withdrawn |
| `AU` | Audit |
| `NG` | No grade |
| `(In Progress)` | Agent-assigned for 0-credit in-progress rows |

## Excel column mapping (Chinese headers)

### 学生信息
`Field` | `Value`

### 学业轨迹
`Period` | `School/Program` | `Major/Plan` | `Action`

### 课程明细
`Term` | `Program` | `Plan` | `End of Study` | `Course Code` | `Course Description` | `Credits` | `Grade` | `Course Topic`

### 学期GPA
`Term` | `Program` | `Plan` | `Term GPA` | `Term Credits` | `Cum GPA` | `Cum Credits` | `Notes`

### 成绩分布
`Grade` | `Count`

### 里程碑
`Program` | `Milestone` | `Level` | `Status` | `Date Completed` | `Attempt Status` | `Attempted On`

## Analysis signals to flag

- **GPA trend**: term GPA drop ≥ 0.5 vs prior term
- **Major change**: program or plan string changes between terms
- **Leave / gap**: `Leave of Absence`, or term with 0 credits
- **Recovery**: cum GPA rebound after a low term
- **Concentration alignment**: finance/quant courses vs stated subplans
- **Graduation gap**: in-progress credits vs typical degree total (institution-specific; note only if obvious)

## Script CLI

```bash
python3 scripts/build_transcript_excel.py \
  --input transcript.json \
  --output-dir /path/to/folder \
  [--output-name Custom_Name.xlsx]
```

Exit code 0 prints the saved `.xlsx` path to stdout.
