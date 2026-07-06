# Application Case Closing — Reference

## 录取清单格式

顾问可按自然语言提供；agent 整理为结构化列表：

```yaml
admission_offers:
  - school_cn: 杜克大学
    school_en: Duke University
    program_en: Master of Quantitative Management: Business Analytics
    program_cn: 量化管理硕士 · 商业分析
    result: 无条件录取
    scholarship: null          # 如 "$30,000" 或 null
    is_final: true             # 仅一所 true
  - school_cn: 约翰霍普金斯大学
    school_en: Johns Hopkins University
    program_en: MS in Business Analytics and Artificial Intelligence
    program_cn: 商业分析与人工智能硕士
    result: 无条件录取
    scholarship: "$30,000"
    is_final: false
```

**总结图规则**
- 只展示 `result` 含「录取」的院校
- 不展示：已拒绝、WL、待结果、已过期（除非顾问明确要求）
- `is_final: true` 的院校放入「最终入读」高亮块
- 统计条：`N` 所录取 · `M` 所含奖学金 · 最终定校 `{SchoolShort}`

## 院校品牌色

优先从官网提取；无法提取时使用下表：

| 院校 | 主色 hex | 备注 |
|------|----------|------|
| Duke | `#003087` | Duke Blue |
| JHU | `#002D72` | Heritage Blue |
| WashU | `#A51417` | Red + `#003DA5` blue |
| UCSD | `#182B49` | Navy |
| Columbia | `#B9D9EB` / `#002B7F` | Light blue / navy |
| Cornell | `#B31B1B` | Carnelian |
| 默认 | `#1a365d` | 通用深蓝 |

点缀色默认 `#C2A569`（浅金），与 TC 品牌黄协调。

## 祝福语润色示例

**顾问原文（粗糙）**
> 不知不觉和小硕同行了一年半载，见证疑惑、焦灼、坚定。我们始终坚信他今天的成就。明天奔赴美国，服务结束但陪伴不结束。

**润色后（卡片用）**
> 不知不觉，我们已同行一年半。
> 从疑惑与焦灼，到坚定与欣喜——小硕的超强执行力和清晰目标感，让我们对他走到今天从未有过一丝怀疑。
> 明天，你将奔赴 **杜克大学**，开启新篇章。

## 微信群发送模板

```
【发送顺序与配文】

Step 1 — 发送：{姓名}_祝福卡片.png
配文：{昵称}，出发前送你一张卡片。

Step 2 — 发送：{姓名}_录取成果总结.png
配文：这是你这一申请季的录取成果，值得纪念。

Step 3 — 主顾问发送文字：
@{姓名} 和{昵称}同行{时长摘要}，从{N}所录取到最终选定 {SchoolShort}，再到{departure_note}——每一步都看在眼里。{项目简称}，很好的选择。申请告一段落，陪伴不会，到了报个平安。有幸同行，一路平安。

Step 4 — 其他顾问各一句接力（每人 1 句，含 1 处具体记忆）
```

## AskQuestion 首轮模板

当用户只说「做结案」而未给材料时，合并为 1–2 个问题：

**Q1 — 基础信息**
- 学生姓名 + 群内昵称
- 同行时间（如 2025.1 — 2026.7）
- 出发时间/语境

**Q2 — 内容（可让用户粘贴）**
- 顾问祝福语原文
- 录取院校列表（含最终入读、奖学金）
- 入读项目官网 URL 或院校 slogan

## 文件命名

| 文件 | 模式 |
|------|------|
| HTML/PNG | `{姓名}_祝福卡片.*` / `{姓名}_录取成果总结.*` |
| Logo | `横版logo png格式.png`（或顾问指定文件名） |
| 文案 | `微信群发送文案.txt` |

## HTML 模板占位符

从 `templates/` 复制到学生 `结案/` 目录后，替换以下字段：

**blessing-card.html**

| 占位 | 来源 |
|------|------|
| `<title>`、致 `{姓名}` | `student_name` |
| `.duke-en` / `.duke-cn` | 入读院校英/中文名 |
| `.content p` 段落 | 润色后的 `blessing_draft` |
| `.program-box` | `enrollment_term` + 项目英文名 |
| `.brand-bar img src` | `logo_path`（相对路径） |
| `.brand-name` | `company_name` |
| `.term` | 当前年月 |
| `.bg` 渐变 / 背景图 | `primary_color` 或 `background_image` |

**admission-summary.html**

| 占位 | 来源 |
|------|------|
| `.header h1` | `{姓名} {年份} 申请季录取成果` |
| `.header .sub` | 与 TC 同行时间 |
| `.stats` 三卡片 | 录取数 / 奖学金数 / 最终定校简称 |
| `.duke-block`（改名为 `.final-block` 亦可） | `is_final: true` 的院校 |
| `.offers-list` | 其余录取（不含 final） |
| `.footer` | 总结一句 |
| CSS 中 `#003087` | `primary_color`（全文替换） |

