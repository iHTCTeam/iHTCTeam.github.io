# CLAUDE.md

iHTCTeam 官网（`iHTCTeam.github.io`）— Jekyll 营销与支持站点，供 AI 助手与开发者快速理解约定。

---

## 项目 identity

| 项 | 值 |
|---|---|
| 仓库 | `iHTCTeam/iHTCTeam.github.io` |
| 线上 | https://ihtcteam.github.io |
| 构建 | Jekyll + GitHub Pages |
| 分支 | `main` |

---

## Git 提交与发布（必须遵守）

**每次提交并发布官网内容时，一律按以下流程执行，不要留多条历史 commit。**

### 目标

- 远程 `main` **始终只有 1 条** commit 记录（整站当前快照）
- Commit message **固定为**：`Update website`
- 使用 **`git push -f origin main`** 覆盖远程历史

### 标准命令（内容已全部改完后）

```bash
cd iHTCTeam.github.io

# 1. 孤儿分支 → 单 commit（含当前工作区全部文件）
git checkout --orphan temp-main
git add -A
git commit -m "Update website"
git branch -M main

# 2. 强制覆盖远程
git push -f origin main
```

若已在 `main` 且仅有未提交改动，也可 `git add -A` 后走上述 orphan 流程；**不要**用 `git commit --amend` 叠在旧历史上，应重建单 commit。

### Commit message 禁忌

- **禁止**在 message 里写具体删改细节（例如删除某数据出处、某敏感词、某 App 文案调整原因等）
- **只用**固定文案：`Update website`
- 用户若指定其他中性标题，仍应归一为 `Update website`，除非用户明确要求另写

### 用户怎么说 → AI 应做什么

用户以下说法均表示 **「改完官网内容后，按单 commit + force push 发布」**：

- 「提交官网」 / 「发布官网」 / 「push 官网」
- 「官网 force push」 / 「覆盖官网提交」 / 「只保留一个 commit」
- 「官网更新并 push」（与本次相同意图）

收到上述指令时：**完成内容修改 → 执行 orphan 单 commit → message 写 `Update website` → `git push -f origin main`**，无需再向用户确认 force push（用户已默认可接受）。

---

## 内容结构速查

| 路径 | 职责 |
|------|------|
| `_data/apps.yml` | 各 App 元数据（`apple_id`、名称、tagline、accent 等） |
| `_data/app_icons.yml` | App Store 图标 URL（由脚本同步） |
| `_data/i18n.yml` | 站点 UI 三语文案 |
| `scripts/sync_app_icons.py` | 从 iTunes Lookup 拉取图标；美区无结果时回退 `cn` → `hk` → `tw` |
| `{AppName}/index.md` | App 支持页主文 |
| `{AppName}/privacy.md` | 隐私政策 |
| `{AppName}/faq.md` | 常见问题 |

新增 App：改 `apps.yml` → 建目录与 markdown → `python3 scripts/sync_app_icons.py` → 按上文 Git 流程发布。

---

## 首页 App 卡片文案对齐（必须遵守）

首页 `app-grid` 按 `_data/apps.yml` 的 **`order` 升序**排列，**每行固定 3 个**卡片；每张卡展示 `taglines` + `blurbs`（三语）。

### 规则

- **同一行的 3 个 App**，`taglines` + `blurbs` 的字数（尤其 **zh-CN**，并同步 **zh-TW / en**）应大致相当，避免某一列明显偏高/偏矮。
- 目标：同一行内三者「tagline 字数 + blurb 字数」总差控制在约 **±15 字**以内（以 zh-CN 为准）。
- 调字数时保持原意与卖点，只做压缩/补齐，不要为对齐而塞无关空话。

### 何时必须重检

以下任一发生后，**按新的 order 重新按行分组检查并对齐文案**（不要假设旧文案仍对齐）：

- 调整任意 App 的 `order`（换位、插入、删除）
- 新增 / 下架 App（会改变后续各行成员）
- 单独大改某个 App 的 `taglines` / `blurbs`

### 自检方式（示例）

按 `order` 排序后，每 3 个一组打印 `len(taglines['zh-CN']) + len(blurbs['zh-CN'])`，看同行差值是否超标；超标则改 `_data/apps.yml` 对应三语文案。

---

## 编码约定

1. **最小 diff** — 只改任务相关文件
2. **三语 section** — 页面用 `<section lang="en|zh-CN|zh-TW">` 保持一致
3. **中性 commit** — 发布只用 `Update website`
4. **勿提交** — 除非用户明确要求；不修改 git config
5. **首页同行对齐** — 改 `order` 或卡片文案后，按上文「首页 App 卡片文案对齐」重检
