# Example: HKBU BBA JS2120

Full worked example for the `program-curriculum-brief` skill.

## User input

| Field | Value |
|-------|-------|
| University | 香港浸会大学 Hong Kong Baptist University |
| Programme | 工商管理学士（荣誉）Bachelor of Business Administration (Honours) |
| Code | JS2120 |
| URL | https://admissions.hkbu.edu.hk/programmes/school-of-business/bachelor-of-business-administration-hons-year1-jee.html |
| Output | `申请/HKBU/HKBU_BBA_JS2120_课程设置单页.html` |
| Audience | 顾问 → 学生 + 朋友圈 |

## Sources used

1. Admissions: https://admissions.hkbu.edu.hk/programmes/school-of-business/bachelor-of-business-administration-hons-year1-jee.html
2. Curriculum overview: https://bba.hkbu.edu.hk/academics/curriculum-overview.html
3. Student handbook: http://handbook.ar.hkbu.edu.hk/2025-2026/academic-programmes/undergraduate-programmes/school-of-business-1/bachelor-of-business-administration-honours
4. Mainland JEE: https://admissions.hkbu.edu.hk/admissions/mainland-jee.html

## Key data extracted

| Field | Value |
|-------|-------|
| Duration | 四年全日制 |
| Credits | 128 units |
| Language | 英语 |
| Funding | 政府资助 |
| Business core | 46 units |
| Concentration | 21 units |
| University language | 9 units |
| General education | 22 units |
| Free electives | 30 units |
| Concentrations | 7 (declare end of Year 1, no quota) |
| Experiential learning | ≥120 hours |
| LinkedIn Learning | ≥40 hours |
| Mainland JEE | 一本线+, English 110+, 文理兼收, 无面试 |

## Chinese summary (excerpt)

### 学分结构

| 类别 | 学分 | 说明 |
|------|------|------|
| 商科核心 | 46 | 会计、经济、金融、营销、管理、法律、AI、毕业项目 |
| 专修 | 21 | 二年级起在所选方向修读 |
| 大学语言 | 9 | 英语及中文 |
| 通识教育 | 22 | 健康、文化、量化推理、价值与人生 |
| 自由选修 | 30 | 副修、双专修、跨学科第二主修 |

### 七大专修

经济学及数据分析 · 财务学 · 人力资源 · 资讯系统与商业智能 · 市场学 · 策略零售管理与创新 · 财富及资产管理

## Output file

```
申请/HKBU/HKBU_BBA_JS2120_课程设置单页.html
```

## WeChat copy — standard version

浸会大学工商管理学士 JS2120，是我今年很愿意推荐给「想读商科、但还没想好细分方向」同学的一条路。

几个亮点：
- **一年级通识探索，二年级再选专修** — 7 个方向（经济数据分析 / 财务 / 市场 / 人力资源 / 资讯系统 / 零售 / 财富管理），**按意愿分配，不设名额上限**
- **课程很新** — 核心课已纳入 AI 商业应用、商业数据分析、商业伦理与 CSR
- **商学院三冠认证**（AACSB / EQUIS / AMBA），认可度高
- **毕业不止上课** — 120 小时体验学习（实习/交换/服务学习）+ 40 小时 LinkedIn Learning
- 还可选 **瑞士 / 法国双学位** 路径

内地高考生：**文理兼收、不设面试**，英语 110+、达一本线即可申请。

如果你或身边有人正在考虑香港商科，这个专业值得放进清单里聊一聊。

## WeChat copy — short version

浸会 BBA｜JS2120  
「先探索，再专修」的弹性商科路径  
7 大专修不设限额 · AI+数据进核心课 · 三冠认证  
120h 实习/交换/服务学习 · 可选瑞士/法国双学位  
内地高考生：文理兼收，无面试，英语110+

## HTML section fill reference

| Placeholder | HKBU value |
|-------------|------------|
| PAGE_TITLE | 浸会大学 BBA（JS2120）课程设置 |
| UNIVERSITY_ZH | 香港浸会大学 |
| PROGRAMME_TITLE_ZH | 工商管理学士（荣誉）BBA |
| FACULTY_EN | School of Business |
| FACULTY_ZH | 工商管理学院 |
| PROGRAMME_CODE | JS2120 |
| TOTAL_CREDITS | 128 units |
| ADMISSION_ROUTE | 内地应届高考生（Mainland JEE） |
| ACADEMIC_YEAR | 2025/26 |
| CONTACT_EMAIL | bba@hkbu.edu.hk |
| CONTACT_PHONE | (852) 3411 5265 |

## Variations tried in conversation

- User asked to edit **section 7 (footer)**: remove student name, keep source links + compile date
- User asked for **WeChat promotional copy** only → deliver standard + short versions from summary
- User can request **highlight Marketing / Economics concentration** → bold matching `.conc-item` in HTML
