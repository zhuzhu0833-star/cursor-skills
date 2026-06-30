# resume-material-mining

Cursor Agent Skill：从中文研究生申研表（`.docx`）挖掘简历素材，生成针对性学生问卷，并将回答转化为英文 resume bullet points。**适用于任意专业/项目。**

## 安装

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/zhuzhu0833-star/resume-material-mining.git ~/.cursor/skills/resume-material-mining
```

或手动将本仓库复制到 `~/.cursor/skills/resume-material-mining/`。

## 依赖

```bash
python3 -m pip install python-docx
```

## 使用

在 Cursor 新对话中说，例如：

- 「根据申研表挖掘简历素材，生成问卷」
- 「读取 `/path/to/1-申研表.docx`，针对每段实习列出提问清单」
- 「帮学生把实习回答转成英文 resume bullets」

Agent 会读取 `SKILL.md`，按 STAR + 量化 + 工具/方法 框架生成问题；可选运行：

```bash
python3 ~/.cursor/skills/resume-material-mining/scripts/extract_application_form.py \
  "/path/to/1-申研表.docx"
```

## 输出

| 产出 | 说明 |
|------|------|
| 缺口分析 | 贡献/成绩空白、描述过短、仅有「参与/了解」等 |
| 问卷 `.docx` | 按经历分段的问题清单（按需生成） |
| 参考回答 | 1–2 句示范格式（需学生核实） |
| 英文 bullets | 学生回复后的简历要点 |

## 文件结构

```
resume-material-mining/
├── SKILL.md              # 主流程
├── reference.md          # 通用 & 分角色问题库
├── examples.md           # 跨领域示范回答
├── README.md
└── scripts/
    └── extract_application_form.py
```

## 同步到其他电脑

```bash
cd ~/.cursor/skills/resume-material-mining
git pull
```

## 更新后推送

```bash
git add .
git commit -m "描述你的修改"
git push
```
