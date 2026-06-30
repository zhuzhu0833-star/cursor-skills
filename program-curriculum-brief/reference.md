# Program Curriculum Brief — Reference

## Official source hierarchy

| Priority | Source | Use for |
|----------|--------|---------|
| 1 | University admissions programme page | Meta info, admission reqs, programme description |
| 2 | Faculty / school programme site | Curriculum overview, concentrations, features |
| 3 | University Student Handbook (current AY) | Core course list with codes/units, concentration requirements |
| 4 | JUPAS / Non-JUPAS / Mainland JEE page | Intake, JUPAS code, HKDSE reqs (cross-check) |
| 5 | Common Data Set / third-party | **Avoid** unless official site lacks data; note uncertainty |

Handbook URL pattern (HKBU example):
`http://handbook.ar.hkbu.edu.hk/{AY}/academic-programmes/undergraduate-programmes/...`

Always note the **academic year** in footer (e.g. 2025/26 学年).

## Field checklist

### Programme meta

| Field | 中文 | Notes |
|-------|------|-------|
| Programme code | 专业编号 | JS2120, etc. |
| Duration | 修读年期 | 四年全日制 |
| Start date | 开学日期 | 2026年9月 |
| Medium | 授课语言 | English / 中英 / etc. |
| Funding | 资助类别 | 政府资助 / 自资 |
| Total credits | 毕业学分 | units / credits |
| Admission route | 招生通道 | Mainland JEE, JUPAS, International |

### Credit structure

| Common categories | Typical labels |
|-------------------|----------------|
| Major / core | 主修 / 商科核心 / 专业必修 |
| Concentration / stream | 专修 / 方向 / 主修细分 |
| University language | 大学语言 |
| General education | 通识教育 |
| Free electives | 自由选修 |

Verify totals sum to graduation requirement.

### Curriculum content

| Field | Extract |
|-------|---------|
| Core courses | Course name, units, course code if in handbook |
| Concentrations | Name (ZH + EN), required vs elective split, 1-line focus |
| Learning path | Year 1 common curriculum? When declare major? |
| Capstone | Honours project, thesis, final year project |
| Experiential | Internship hours, exchange, service learning |
| Online learning | LinkedIn Learning, MOOC requirements |
| Double degree | Partner school, 2+2 / 1+2+1 pattern |
| Minor / double major | Options outside primary major |
| Accreditation | AACSB, EQUIS, professional body — verify on official site |

### Admission (Mainland JEE focus)

| Field | 中文 |
|-------|------|
| Score threshold | 一本线 / 特控线 |
| English sub-score | 英语单科要求 |
| Subject requirement | 文理 / 选考科目 |
| Interview | 设 / 不设面试 |
| Admission basis | 高考成绩择优 / 面试综合 |
| Independent admission | 独立招生，不参与统招 |
| Competitive note | 实际录取线通常高于最低要求 |

## Terminology (EN → ZH)

| English | 中文（常用） |
|---------|-------------|
| Concentration | 专修 |
| Major | 主修 |
| Minor | 副修 |
| Double concentration | 双专修 |
| Second major | 第二主修 |
| Transdisciplinary second major | 跨学科第二主修 |
| General education | 通识教育 |
| Free electives | 自由选修 |
| Honours project / capstone | 毕业项目 |
| Experiential learning | 体验学习 |
| Broad-based admission | 大类招生 / 一年级探索 |
| Units / credits | 学分 (units) |
| Mainland JEE | 内地应届高考生 |
| Government funded | 政府资助 |

## HTML section → data mapping

| HTML section | Primary data source |
|--------------|---------------------|
| `.header h1` | University + programme title |
| `.header .sub` | Faculty + programme code |
| `.meta` spans | Duration, start, language, funding, credits, route |
| 专业定位 paragraph | Admissions「专业简介」+ faculty overview |
| `.credits-table` rows | Handbook curriculum structure table |
| 学习路径 `.box` | Year 1–4 progression from handbook or faculty site |
| `.core-courses` | Handbook required courses list |
| `.conc-grid` | Handbook concentration pages (summary only) |
| `.highlight` | Second concentration, minor, double major options |
| `.grid-3` col 1 | Graduation requirements (experiential, online) |
| `.grid-3` col 2 | Dual degree / exchange (optional column) |
| `.grid-3` col 3 | Mainland JEE or relevant admission block |
| `.footer` | Source URLs, email, phone, 整理 date |

## Section numbering (user edit requests)

When user says「第 N 块」:

| # | Block |
|---|-------|
| 1 | 页头 `.header` |
| 2 | 专业定位 |
| 3 | 学分结构 |
| 4 | 学习路径（左栏） |
| 5 | 核心课程（右栏） |
| 6 | 专修 / 主修方向 |
| 7 | 页脚 `.footer` |

Note: `.grid-3` bottom row is **not** numbered separately — treat as part of content blocks 4–6 area; if user means footer, they usually say「页脚」.

## WeChat copy guidelines

**Do:**

- Lead with programme fit («适合还没定方向的同学»)
- Use concrete facts (7 专修、128 学分、120 小时体验学习)
- Cite verifiable credentials (三冠认证 — only if official)
- End with soft CTA

**Avoid:**

- Guaranteed admission claims
- Ranking superlatives without source
- Fabricated employment rates
- Student names in public copy unless requested

## Output naming

| Artifact | Pattern | Example |
|----------|---------|---------|
| HTML | `{SchoolCode}_{Short}_{Code}_课程设置单页.html` | `HKBU_BBA_JS2120_课程设置单页.html` |
| SchoolCode | 3–6 letter abbreviation | HKBU, CityU, HKU |
| Short | Programme abbreviation | BBA, IRGA, CS |

## Research commands (agent)

Prefer `WebFetch` on official URLs. If handbook page times out, retry or search:
`site:{university.domain} {programme name} handbook curriculum`

For HK programmes, also check:
- `{uni}.edu.hk/admissions` programme page
- Faculty subdomain (e.g. `bba.hkbu.edu.hk`)
- `handbook.ar.{uni}.edu.hk` for course lists
