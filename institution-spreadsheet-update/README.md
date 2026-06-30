# institution-spreadsheet-update

Cursor Agent Skill：更新 Excel/CSV 院校表格中每所院校各列信息，将变更单元格以红色字体标出，并生成 PDF 变更报告。

## 安装

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/zhuzhu0833-star/institution-spreadsheet-update.git ~/.cursor/skills/institution-spreadsheet-update
```

或手动将本仓库复制到 `~/.cursor/skills/institution-spreadsheet-update/`。

## 依赖

```bash
python3 -m pip install openpyxl fpdf2
```

## 使用

在 Cursor 新对话中说，例如：

- 「用 institution-spreadsheet-update 更新这份选校表 `/path/to/top30.csv`」
- 「更新院校表格，标红变更，输出 PDF 报告」

Agent 会读取 `SKILL.md`，逐校调研并生成 `changes.json`，然后运行：

```bash
python3 ~/.cursor/skills/institution-spreadsheet-update/scripts/apply_updates_and_report.py \
  --input "/path/to/table.csv" \
  --changes "/path/to/changes.json" \
  --output-dir "/same/folder/as/input"
```

## 输出文件

| 文件 | 说明 |
|------|------|
| `{stem}_updated_{date}.xlsx` | 完整表格，变更单元格红色字体 |
| `{stem}_updated_{date}.csv` | 同步更新的 CSV |
| `{stem}_update_report_{date}.pdf` | 中文变更报告 |
| `{stem}_changes_{date}.json` | 机器可读 diff 存档 |

## 文件结构

```
institution-spreadsheet-update/
├── SKILL.md              # 主流程
├── reference.md          # 列名映射与调研优先级
├── README.md
└── scripts/
    ├── apply_updates_and_report.py
    └── apply_merged_header_xlsx.py
```

## 同步到其他电脑

```bash
cd ~/.cursor/skills/institution-spreadsheet-update
git pull
```

## 更新后推送

```bash
git add .
git commit -m "描述你的修改"
git push
```
