# application-case-closing

Cursor Agent Skill：为签约学生制作申请季结案交付物——祝福卡片 PNG、录取成果总结 PNG、微信群发送文案。

## 安装

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/zhuzhu0833-star/application-case-closing.git ~/.cursor/skills/application-case-closing
```

## 使用

在 Cursor 新对话中说，例如：

- 「用 application-case-closing 给 XX 做结案」
- 「做送别祝福卡片，学生明天出发」

Agent 会收集：顾问祝福语、录取结果、入读院校 URL 或 slogan，生成 HTML 并导出 PNG。

## 依赖

- macOS Google Chrome（headless 截图导出 PNG）

## 导出 PNG

```bash
bash ~/.cursor/skills/application-case-closing/scripts/export_png.sh \
  "/path/to/学生/结案"
```

## 文件结构

```
application-case-closing/
├── SKILL.md
├── reference.md
├── README.md
├── templates/
│   ├── blessing-card.html
│   └── admission-summary.html
└── scripts/
    └── export_png.sh
```

## 同步到其他电脑

```bash
cd ~/.cursor/skills/application-case-closing
git pull
```
