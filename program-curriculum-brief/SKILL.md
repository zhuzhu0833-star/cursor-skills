---
name: program-curriculum-brief
description: >-
  Researches official university programme pages and handbooks, writes a Chinese
  curriculum summary, generates an A4 single-page HTML brief, and drafts WeChat
  moment promotional copy. Use when the user asks to 总结课程设置, 专业介绍单页,
  课程总结, 朋友圈宣传, curriculum brief, programme overview HTML, or send a
  programme summary to a student.
---

# Program Curriculum Brief（课程设置总结 → 单页 HTML → 朋友圈文案）

Research any university programme from official sources, deliver a Chinese curriculum summary, an A4 printable HTML one-pager, and WeChat moment copy.

## Quick start

1. **Confirm input**: university, programme name, programme code (if any), official URL(s), output folder, audience (student / parent / WeChat).
2. **Research** from official sources (see [reference.md](reference.md)); cross-check ≥2 sources when possible.
3. **Write Chinese summary** in chat (structured sections below).
4. **Generate HTML** from [html-template.html](html-template.html); save as `{SchoolCode}_{ProgramShort}_{ProgramCode}_课程设置单页.html`.
5. **Draft WeChat copy**: standard version (150–250 chars) + short version (≤100 chars).
6. **Deliver** file path + summary + both copy versions to user.

Default output folder: `申请/{SchoolCode}/` under the current student workspace. Create the folder if missing.

## Workflow checklist

```
- [ ] Input confirmed (school / programme / URL / output path / audience)
- [ ] Official sources fetched (≥2 sources cross-checked when available)
- [ ] Chinese summary delivered in chat
- [ ] A4 HTML one-pager written to target path
- [ ] WeChat copy: standard + short versions delivered
- [ ] Footer cites source URLs and academic year
```

## Step 1 — Confirm input

| Item | Required | Notes |
|------|----------|-------|
| University | Yes | Chinese + English name |
| Programme | Yes | Full degree title |
| Programme code | If exists | e.g. JS2120, JS1001 |
| Official URL(s) | Yes | Admissions + faculty/handbook |
| Output path | Default | `申请/{SchoolCode}/` |
| Audience | Optional | Affects WeChat tone |
| Highlights | Optional | e.g. emphasize one concentration |
| Omit sections | Optional | e.g. drop admission block for general brief |

Ask only when critical info is missing. If user provides a URL, proceed with research.

## Step 2 — Official research

**Source priority** (full rules in [reference.md](reference.md)):

1. University admissions programme page
2. Faculty / school programme site
3. University Student Handbook (current AY)
4. JUPAS / Non-JUPAS / Mainland JEE page

**Must extract when available:**

- Duration, mode, start date, medium of instruction, funding type
- Total credits/units and credit breakdown
- Core/required courses (names + units if listed)
- Majors, concentrations, streams, electives structure
- Year-by-year learning path
- Graduation requirements beyond credits (internship, exchange, capstone, etc.)
- International options (dual degree, exchange)
- Admission requirements (especially Mainland JEE: 一本线, English sub-score, interview, 文理)
- Contact email / phone
- Accreditation or distinctive features (fact-based only)

**Rules:**

- Do **not** invent course names, credit counts, or admission thresholds.
- If data is missing, write「官网未列明」— do not guess.
- Prefer the **current academic year** handbook over outdated pages.
- Record source URLs for the HTML footer.

## Step 3 — Chinese summary (chat output)

Use this structure:

```markdown
## [大学] · [专业名]（[编号]）课程设置总结

### 基本信息
（修读年期、授课语言、毕业学分、资助、招生通道）

### 专业定位
（1 段：课程设计理念、适合谁）

### 学分结构
（表格：类别 | 学分 | 说明）

### 学习路径
（按年级简述）

### 核心 / 必修课程
（列表；含 units 若官网有）

### 专修 / 主修 / 方向
（每项 1 行简介；不必列全部选修 unless user asks）

### 毕业要求
（体验学习、毕业项目、在线学习等）

### 特色选项
（双学位、副修、跨学科主修等）

### 入学要求
（内地高考生 / 国际生，按用户场景）

### 资料来源
（链接列表 + 学年）
```

Adjust sections when programme type differs (e.g. single-major STEM with no concentrations → merge into「主修课程」).

## Step 4 — A4 HTML one-pager

1. Read [html-template.html](html-template.html) for CSS and section layout.
2. Fill all sections; keep **one A4 page** — shorten prose if overflow (smaller lists, merge bullets).
3. **Filename**: `{SchoolCode}_{ProgramShort}_{ProgramCode}_课程设置单页.html`
   - Example: `HKBU_BBA_JS2120_课程设置单页.html`
4. **Title tag**: `{大学简称} {专业简称}（{编号}）课程设置` — no student name unless requested.
5. **Footer**: source links + contact + `整理：{YYYY年M月}` — no student name unless requested.

### HTML section map (for user edits like「改第 7 块」)

| # | Section | Template class |
|---|---------|----------------|
| 1 | 页头（标题 + meta） | `.header` |
| 2 | 专业定位 | `.section` → 专业定位 |
| 3 | 学分结构表 | `.credits-table` |
| 4 | 学习路径 | `.grid-2` left column |
| 5 | 核心必修课程 | `.grid-2` right column |
| 6 | 专修 / 主修方向 | `.conc-grid` + `.highlight` |
| 7 | 页脚 | `.footer` |
| — | 底部三栏（毕业要求 / 国际选项 / 入学要求） | `.grid-3` |

Bottom `.grid-3` columns are optional — omit a column or merge into `.grid-2` if programme has no equivalent (e.g. no dual degree).

### Layout adjustments

- **Concentrations ≠ 7**: add/remove `.conc-item` blocks; use 1-column if ≤3 items.
- **No concentrations**: replace section 6 with「主修课程」single-column list.
- **Long core course list**: keep top 12–15; add「等」if truncated.
- **User highlights one concentration**: bold that `.conc-item` or add `.highlight` note.

## Step 5 — WeChat moment copy

Deliver **two versions** in chat after HTML is saved.

### Standard version (150–250 字)

Structure:

1. Opening hook — who this programme suits
2. 3–5 bullet highlights (flexible major, accreditation, AI/data, experiential learning, etc.)
3. One line on admission threshold (审慎表述)
4. Soft CTA —「值得放进选校清单」

Tone: advisor recommendation, factual, not hype. Use「通常高于一本线」not「轻松录取」.

### Short version (≤100 字)

Format:

```
[大学] [专业]｜[编号]
[Tagline 1] · [Tagline 2] · [Tagline 3]
[Admission one-liner]
```

Suitable for image + caption posts.

### Optional variants (only if user asks)

- **家长版**: emphasize accreditation, career paths, safety of 政府资助
- **学生版**: emphasize flexibility, exchange, course names they'd enjoy
- **顾问口吻 / 学生视角**: adjust pronouns and CTA

## Conditional workflows

**User provides URL only** → research → full pipeline (summary + HTML + WeChat).

**User asks「总结课程设置」only** → Step 3 summary; offer HTML + WeChat.

**User asks「做单页发给学生」** → full pipeline; default save to `申请/{SchoolCode}/`.

**User asks「朋友圈宣传」only** → Step 5 from existing summary/HTML in context; if none, run research first.

**User asks to edit HTML section N** → use section map above; edit file in place; do not regenerate entire page unless asked.

**User asks to highlight a concentration** → bold in HTML `.conc-item` + mention in WeChat opening.

## Quality checks

Before delivering:

- [ ] Every credit number matches official source
- [ ] Course names are verbatim from handbook/admissions page
- [ ] HTML opens as valid document; fits ~1 A4 page
- [ ] Footer links work and include academic year
- [ ] WeChat copy has no unsupported superlatives
- [ ] No student PII in filename/title/footer unless explicitly requested

## Additional resources

- Field checklist and terminology: [reference.md](reference.md)
- Full worked example (HKBU BBA JS2120): [examples.md](examples.md)
- HTML skeleton: [html-template.html](html-template.html)
