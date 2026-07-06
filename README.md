# Cursor Skills

个人 Cursor Agent Skills 统一仓库。每个子目录为一个独立 skill，供 Cursor 在对应任务中自动或手动调用。

## Skills 列表

| 目录 | 用途 |
|------|------|
| [application-case-closing](application-case-closing/) | 申请季结案：祝福卡片 + 录取成果总结 PNG、微信群文案 |
| [blader-humanizer](blader-humanizer/) | 文本去 AI 化 / humanizer |
| [frontend-slides](frontend-slides/) | 前端幻灯片生成（upstream: zarazhangrui/frontend-slides） |
| [institution-spreadsheet-update](institution-spreadsheet-update/) | 院校表格更新、标红变更、PDF 报告 |
| [program-curriculum-brief](program-curriculum-brief/) | 课程设置总结、A4 HTML 单页、朋友圈文案 |
| [resume-material-mining](resume-material-mining/) | 申研表 → 简历素材挖掘 |
| [transcript-analysis-excel](transcript-analysis-excel/) | 成绩单 PDF → Excel 分析 |
| [translate-academic-credentials](translate-academic-credentials/) | 学术凭证翻译 |
| [us-undergrad-colleges](us-undergrad-colleges/) | 美本院校（脚手架） |
| [us-undergrad-policy-monitor](us-undergrad-policy-monitor/) | 美本招生政策监控 |

## 安装

**新机器首次安装**（克隆整个 skills 目录）：

```bash
# 若已有旧版单 skill 仓库，先备份再替换
mv ~/.cursor/skills ~/.cursor/skills.bak 2>/dev/null || true
git clone https://github.com/zhuzhu0833-star/cursor-skills.git ~/.cursor/skills
```

**本机已是工作副本**：在仓库根目录同步即可（见下）。

## 日常更新

在 `~/.cursor/skills` 根目录执行：

```bash
# 查看状态
./scripts/sync.sh status

# 从 GitHub 拉取最新
./scripts/sync.sh pull

# 推送本地改动
./scripts/sync.sh push

# 先拉再推（推荐）
./scripts/sync.sh sync

# 只提交某个 skill 的改动
./scripts/sync.sh push "feat(program-curriculum-brief): update HTML template"
```

## 添加新 Skill

```bash
cd ~/.cursor/skills
mkdir -p my-new-skill
# 编写 my-new-skill/SKILL.md（含 YAML frontmatter）
./scripts/sync.sh push "feat: add my-new-skill"
```

## 目录约定

```
cursor-skills/
├── README.md           # 本文件
├── scripts/sync.sh     # 与 GitHub 同步
├── skill-name/
│   ├── SKILL.md        # 必需：skill 主文件
│   ├── reference.md    # 可选：详细参考
│   ├── examples.md     # 可选：示例
│   └── scripts/        # 可选：工具脚本
```

## 说明

- 本仓库为 **唯一 canonical 源**；此前分散的单 skill 仓库（如 `program-curriculum-brief`、`resume-material-mining` 等）已合并至此。
- Cursor 读取路径：`~/.cursor/skills/{skill-name}/SKILL.md`
- 修改 skill 后执行 `./scripts/sync.sh sync` 即可备份到 GitHub。
