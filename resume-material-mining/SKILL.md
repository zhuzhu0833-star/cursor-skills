---
name: resume-material-mining
description: >-
  Mines resume material from Chinese graduate application intake forms (申研表)
  for any major or program by analyzing experiences, generating targeted student
  questionnaires, and drafting English resume bullet points. Use when the user asks
  to 挖掘简历素材, 简历素材, 申研表, 实习问卷, 经历提问, resume mining, intake form
  analysis, STAR questions, or完善实习/教育/项目经历填写.
---

# Resume Material Mining（申研表 → 简历素材）

Turn sparse 申研表 entries into quantified, resume-ready material for **any graduate program or major** via structured questioning and optional Word questionnaire output.

## Quick start

1. **Locate inputs**: `1-申研表.docx` (or user-provided intake form); optional school list / planning doc.
2. **Extract experiences**:
   ```bash
   python3 ~/.cursor/skills/resume-material-mining/scripts/extract_application_form.py \
     "/path/to/1-申研表.docx"
   ```
3. **Gap analysis**: flag empty「贡献/成绩」fields, vague verbs (参与/了解/协助), missing numbers/tools/deliverables.
4. **Identify target context** (from user materials — do not assume a field):
   - Target degree, country, program names
   - Program type: research / professional / analytical / creative / policy / clinical / etc.
   - Competencies the field values (see [reference.md](reference.md) → Program-type lens)
5. **Produce outputs** (per user request):
   - Questionnaire Word doc (`.docx`) with per-experience sections
   - Reference answer examples (1–2 sentences each, marked as 示范)
   - English resume bullet drafts after student replies
6. **Never fabricate** student facts in final resume bullets; reference examples are format-only.

## Workflow checklist

```
- [ ] Intake form parsed (education, awards, internships, activities, projects, research)
- [ ] Target major / programs / narrative direction confirmed from user files (not assumed)
- [ ] Gap analysis table produced (priority: 贡献/成绩 blank > vague duties > missing education)
- [ ] Universal questions (tools, numbers, supervisors, deliverables) drafted
- [ ] Per-experience questions tailored to role + target field relevance
- [ ] Empty sections probed (activities, academic projects, certificates)
- [ ] Questionnaire .docx saved (if requested)
- [ ] Student follow-up plan noted (supervisor call, documents to collect)
```

## Core framework: STAR + 量化 + 工具/方法

Every experience question should eventually yield:

| Layer | Ask for |
|-------|---------|
| **S** | Context — where, when, what problem or goal |
| **T** | Your specific role — independent vs assisted |
| **A** | Actions — methods, tools, collaborators, workflow steps |
| **R** | Result — numbers, impact, feedback, before/after |
| **Tools/Methods** | Software, lab techniques, frameworks, languages, platforms used |

Adapt metrics to the field: headcount, budget, sample size, accuracy %, time saved, audience reach, revenue, citations, error rate, etc.

### Interview tactics (顾问 → 学生)

- Replace「你做了什么？」→「**某一周/某个具体任务或项目**里，你亲手完成了哪一步？」
- When answer is「参与/了解/协助」→「**有没有独立完成的 deliverable？** 是什么？」
- When「没有数字」→「大概多少（人/次/页/小时/金额/样本/事件）？估算也行。」
- End each experience:「**supervisor/导师会如何评价你？** 愿意写推荐信吗？」

## Experience-type routing

| Section | Typical resume weight | Action |
|---------|----------------------|--------|
| Work/internship (工作/实习) | Usually highest | Deep-dive by role; see [reference.md](reference.md) |
| Research (研究经历) | High for research programs | Methods, contribution, output |
| Education (教育经历) | Always include; higher if pivoting | GPA, relevant coursework, thesis |
| Academic projects (学术项目) | High when research is thin | Course projects, methods, outcomes |
| Awards (奖项) | Medium | Tie to skills valued by target field |
| Activities (其他活动) | Medium | Leadership, initiative, measurable impact |
| Off-target experiences | Context-dependent | Include if space allows or extract transferable skills for essays |

**Relevance is relative to the student's target program** — determine from school list / planning doc, not from a built-in default major.

### Internship / work sub-routing

| Pattern | Strategy |
|---------|----------|
| ≥ 4 weeks | Full STAR + role-specific questions |
| 1–3 weeks | 1–2 concrete deliverables + intensity |
| Rotation (轮岗) | Split by department/function; ask where most time was spent |
| Same org, multiple stints | Consider merged entry if narrative is stronger |

## Questionnaire document structure

When user asks for a Word questionnaire, use this outline:

```markdown
# [Student Name] — 简历素材完善问题清单
适用申请方向：[student's target major/programs — from user materials]
文档用途：请逐条以「答：」填写；无法回答标注「待确认 + 需问谁」

## 一、整体策略说明
## 二、通用问题（所有与申请相关的经历）
## 三、{Experience 1}（日期 · 单位/项目 · 角色 · 时长）
### 现状诊断 + Q1…Qn
## …
## N、简历呈现策略问题
## N+1、针对目标项目/专业的补充问题
## 填写指引
```

Formatting: 宋体 11pt for body; section headings; optional callout for「现状」diagnosis per experience.

## Tailoring questions to any major

Before writing specialized questions:

1. Read target program materials (选校表, planning doc, user message).
2. Infer 3–5 **valued competencies** for that field (e.g., data analysis, writing, lab skills, client service, design, policy analysis, teaching, coding).
3. For each experience, ask:
   - What from this experience maps to those competencies?
   - What jargon or field-specific terms need clarification? (Explain to student if needed.)
4. Use role-based question banks in [reference.md](reference.md) — pick sections that match the **role**, not a hardcoded major.

## Reference answer examples

When user asks for 参考回答, provide **1–2 sentences per key question**, labeled **示范**. See [examples.md](examples.md) for cross-field templates (corporate, research, nonprofit, teaching, student org).

Rules:
- Use placeholders student must verify (names, numbers, tools)
- Show **action + tool/method + quantified result** pattern
- Match tone to student's actual industry/context

## Resume bullet conversion

After student answers, convert each experience to 2–4 bullets:

```
[Strong verb] + [what] + [how/tool/method] + [quantified result or scope]
```

Verb tiers: Led / Managed / Coordinated / Designed / Analyzed / Developed / Implemented / Authored / Assisted (Assist only when truly supportive).

Generic pattern:
> Researched [topic] using [method/tool], analyzing [N] samples/sources and presenting findings that [outcome/informed decision].

Field-specific verbs and metrics come from the student's target program — do not default to one industry.

## Priority matrix (default)

| Priority | Signal |
|----------|--------|
| 🔴 Critical | 「贡献/成绩」blank; experiences most relevant to stated target program |
| 🟡 Medium | Education GPA/courses blank; academic projects empty; awards undetailed |
| 🟢 Low | Experiences with weak stated relevance — confirm with user before deep-dive or omit from 1-page resume |

Re-rank after user confirms target major and which experiences to emphasize.

## Communication plan (suggest to user)

1. **Meeting 1 (60–90 min)**: universal questions + highest-priority experiences chronologically
2. **Send questionnaire**: student fills offline
3. **Meeting 2**: follow up vague/blank answers; confirm numbers with supervisor/mentor
4. **Collect artifacts**: reports, slides, code, designs, emails, datasets
5. **Deliver**: English bullets + update 申研表

## Additional resources

- Universal & role-based question banks: [reference.md](reference.md)
- Cross-field sample answers: [examples.md](examples.md)
