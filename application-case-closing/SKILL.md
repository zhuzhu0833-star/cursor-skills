---
name: application-case-closing
description: >-
  Generates study-abroad case-closing deliverables for TC Edu: blessing card PNG,
  admission summary PNG, and WeChat group send copy. Collects consultant blessing
  text, student admission results, and final enrollment program URL or slogan.
  Use when user asks for 结案, 送别, 祝福卡片, 录取成果总结, case closing,
  farewell card, departure blessing, or 申请季结案仪式.
---

# Application Case Closing（申请季结案 · 祝福卡片 + 录取总结）

为签约学生制作结案仪式感交付物，默认输出至学生工作区 `{学生文件夹}/结案/`。

## 如何调用

1. **显式**：`用 application-case-closing 给小硕做结案`
2. **自然触发**：`做送别祝福卡片`、`申请季结案`、`录取成果总结图发微信群`

## Quick start

```
1. 收集输入（见下方清单；缺项用 AskQuestion）
2. 若有入读项目 URL → 抓取 slogan / 校名 / 品牌色
3. 润色祝福语 → 写入祝福卡片 HTML
4. 整理录取列表 → 写入录取成果总结 HTML（默认仅录取，不含拒绝/WL）
5. 运行 scripts/export_png.sh 导出两张 PNG
6. 生成 微信群发送文案.txt
7. 交付文件路径 + 发送顺序说明
```

## Step 1 — 向顾问收集信息

**必填**

| 字段 | 说明 | 示例 |
|------|------|------|
| `student_name` | 学生姓名（全名 + 群内昵称） | 张硕 / 小硕 |
| `companion_period` | 与 TC 同行时间 | 2025.1 — 2026.7 |
| `blessing_draft` | 顾问原始祝福语（可多条、可粗糙） | 「同行一年半，见证你从焦灼到坚定…」 |
| `admission_offers` | 已获得录取清单 | 见 [reference.md](reference.md#录取清单格式) |
| `final_enrollment` | 最终入读院校 + 项目（中英） | Duke · MQM: Business Analytics |
| `program_url_or_slogan` | **二选一或都提供**：项目/院校官网 URL；或校方 slogan / 宣传语 | `https://…` 或 `"Eruditio et Religio"` |
| `departure_note` | 出发语境 | 明天奔赴美国 |
| `enrollment_term` | 入学季 | 2026 Fall |

**品牌（默认 TC Edu，可覆盖）**

| 字段 | 默认 |
|------|------|
| `company_name` | 成都传胜留学 TC Edu |
| `logo_path` | 同目录 `横版logo png格式.png`（顾问可另传） |

**发送（默认微信群）**

| 字段 | 默认 |
|------|------|
| `send_channel` | 微信群：祝福卡片 → 录取总结图 → 主顾问文字 → 顾问接力 |
| `summary_scope` | 仅录取成果（不含拒绝/WL/待结果） |
| `include_scholarship` | 是（在总结图中展示金额） |

**可选**

- `primary_color` — 覆盖自动提取的院校主色（hex）
- `accent_color` — 点缀色，默认 `#C2A569`
- `wechat_main_text` — 主顾问群消息；未提供则按模板生成
- `background_image` — 校园图 URL 或本地路径（祝福卡片）

### 收集方式

信息不全时，**分批 AskQuestion**（每轮 1–2 题），不要一次问超过 5 项。

首轮必问（若用户未提供）：
1. 学生姓名 + 昵称
2. 顾问祝福语（请直接粘贴原文）
3. 录取院校列表 + 最终入读
4. 入读项目官网链接 **或** 院校 slogan

## Step 2 — 处理入读院校信息

**若提供 URL**（项目页或院校页）：
- 抓取：院校英文名、中文名、项目全称、slogan/tagline（如有）
- 提取或推断品牌主色（优先官网 CSS / 已知色表，见 [reference.md](reference.md#院校品牌色)）
- 可选：Campus 图片用于卡片背景（Wikimedia 或官网公开图；下载失败则用渐变纯色底）

**若仅提供 slogan**：
- 卡片顶部展示 slogan（英文）+ 院校中英文名
- 主色用手动指定或 reference 色表

**不要编造** slogan 或奖学金金额；缺失则省略该元素。

## Step 3 — 润色祝福语

将 `blessing_draft` 整理为祝福卡片正文（约 120–160 字）：

- 保留顾问原意与关键词（情绪词、具体评价）
- 删重复句（如「坚信不疑」+「一定成功」）
- 避免「服务结束」→ 改用「申请这段路告一段落，陪伴不会」
- 点名最终入读院校与项目
- 结尾钩子：「到了美国，记得报个平安」

卡片结构见 [templates/blessing-card.html](templates/blessing-card.html) 占位符。

## Step 4 — 生成 HTML

输出目录：`{学生工作区}/结案/`

| 文件 | 模板 |
|------|------|
| `{姓名}_祝福卡片.html` | [templates/blessing-card.html](templates/blessing-card.html) |
| `{姓名}_录取成果总结.html` | [templates/admission-summary.html](templates/admission-summary.html) |
| `微信群发送文案.txt` | 见 [reference.md](reference.md#微信群发送模板) |

**祝福卡片**：1080×1920 竖版；底部白底条 + Logo + 公司名。

**录取总结图**：1080×1920 竖版；顶部数据条（N 所录取 / 含奖学金数 / 最终定校）；入读院校高亮块；其余录取简要列表；**不含** Offer 过期、拒绝、WL。

若顾问提供 Logo，复制或链接到 `结案/` 目录，HTML 用相对路径引用。

## Step 5 — 导出 PNG

```bash
bash ~/.cursor/skills/application-case-closing/scripts/export_png.sh \
  "/path/to/学生/结案"
```

依赖：macOS Google Chrome（headless）。脚本导出：
- `{姓名}_祝福卡片.png`
- `{姓名}_录取成果总结.png`

HTML 修改后重新运行脚本即可更新 PNG。

## Step 6 — 交付

在 chat 中提供：

1. 两张 PNG 路径
2. `微信群发送文案.txt` 全文
3. 若顾问需接力：提示每人 1 句、含 1 处具体记忆
4. 发送时机建议：出发前夜

## Workflow checklist

```
- [ ] 必填输入已收集（姓名 / 祝福语 / 录取 / 入读 / URL或slogan）
- [ ] 院校信息已处理（校名 / 色 / 可选背景图）
- [ ] 祝福语已润色并写入卡片 HTML
- [ ] 录取总结 HTML 仅含录取成果
- [ ] Logo 已放入结案目录
- [ ] PNG 已导出
- [ ] 微信群发送文案已生成
```

## 设计规范

- 尺寸：1080×1920（9:16，微信友好）
- 字体：PingFang SC / 微软雅黑
- 入读院校区块：主色背景高亮 + `FINAL CHOICE · 最终定校` 徽章
- Logo 必须用半透明白底条（深色 Logo 不可直接叠加深色背景）

## 附加资源

- 输入格式与院校色表：[reference.md](reference.md)
- HTML 模板：[templates/](templates/)
