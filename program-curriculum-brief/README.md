# program-curriculum-brief

Cursor Agent Skill：从大学官网抓取课程设置，生成中文总结、A4 单页 HTML、朋友圈宣传文案。

## 文件结构

```
program-curriculum-brief/
├── SKILL.md              # 主流程
├── reference.md          # 数据源与字段清单
├── html-template.html    # A4 单页模板
├── examples.md           # HKBU BBA JS2120 示例
└── scripts/sync.sh       # 与 GitHub 同步
```

## 安装与更新

本 skill 已纳入统一仓库 [cursor-skills](https://github.com/zhuzhu0833-star/cursor-skills)。

```bash
git clone https://github.com/zhuzhu0833-star/cursor-skills.git ~/.cursor/skills
cd ~/.cursor/skills && ./scripts/sync.sh pull   # 日常更新
```

## 触发词

`总结课程设置` · `专业介绍单页` · `课程总结` · `朋友圈宣传` · `curriculum brief`

## 输出物

1. 中文课程设置总结（聊天）
2. `{SchoolCode}_{Program}_{Code}_课程设置单页.html`
3. 朋友圈文案（标准版 + 短版）
