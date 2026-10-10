# AGENTS.md — AI 助手在本仓库的工作规则

本仓库是 FastHarness 小组的会议记录与论文调研，**只收录经人工审核的内容**。任何 AI 助手（Claude Code、Codex 等）在这里新增或修改论文、会议时，必须遵守以下规则。完整格式见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 新增论文：两步走，不能跳过

### 第一步：写进审阅表，标「待审核」

用户给出一篇论文时（可能只给一个链接或标题），先补齐全部信息，再写进 [`review/论文审阅表.html`](review/论文审阅表.html)，状态标 `<span class="st wait">待审核</span>`。

**用户没给的信息，必须自己从原文补齐，不能留空，也不能编造：**

| 字段 | 从哪里找 |
|---|---|
| 模块 | 对照 README 的模块划分判断；判断不了就问用户 |
| 完整标题、Year | arXiv 页面 |
| Venue | arXiv 的 Comments / Journal-ref，会议官网录用名单；查不到就写 `arXiv`；Workshop 奖必须注明 Workshop |
| 团队 | PDF 首页的作者单位，标出通讯作者单位 |
| Code / Website | 论文摘要、项目主页里的链接；逐个打开确认存在；没有就省略 |
| 问题、方法 | 读正文。问题一句话；方法写机制流程，关键动作加粗，术语保留英文 |
| 仿真结果 | **读完实验部分的表格和图**，写基准名、规模（任务数 × 次数）、本方法与对比对象的数字 |
| 真机结果 | 同上，写机器人型号、任务数 × 次数、逐任务结果；只有演示视频就写「只有演示，没报成功率」；没做就写「没做」 |

读论文的要求：
- 必须读全文，包括实验表格、图和附录里的结果，不能只看摘要
- 每个数字都要能在论文里找到出处；从图上读出的数字标「约」
- 成功率的定义特殊时要注明（例如「允许重试 8 次」）
- 找不到的信息写「未找到」，并在回复里告诉用户

写完后告诉用户：已加入审阅表、待审核，请对照原文核对。

### 第二步：用户确认审核通过后，才同步到仓库

**没有得到用户明确的「审核通过」，不能改 README。** 通过后：

1. `README.md`：在对应类别的表格最后一行之后插入一行，格式严格按 CONTRIBUTING.md（每类一张表、表头照抄、7 列 Name | Paper | Venue | Method | Result | Team | Links 居中、Method 中文一句话、Result 中文两行「比什么<br>对比对象 → 本方法」、Team 用 <br> 分行）；新类别要新建 `## 类别名` 和整张表
2. `papers/<简称>.md`：按 [`templates/paper.md`](templates/paper.md) 写详情
3. `CHANGELOG.md`：最上面加一条，写明日期、新增 / 修改了什么
4. README 顶部徽章（Papers、Updated）和 Contents 一行里的论文数同步更新；README 里「当前主线」、Method、Result 用中文，其余用英文
5. 审阅表里该论文的状态改成 `<span class="st ok">已入库</span>`
6. 新建分支、提交、开 Pull Request，PR 描述按模板填写

## 会议更新

用户给出新的会议内容时：
1. 按 [`templates/meeting.md`](templates/meeting.md) 在 `meetings/` 新建纪要，编号顺延
2. 替换 README 的「当前主线」（中文，照会议原话精简）为本次会议的新主线，标题里的会议链接改成新纪要
3. README 的 Meetings、Updated 徽章同步更新
4. CHANGELOG 加一条

会议里没写的信息（日期、参会人、负责人）写「待填」，不要猜。

## 禁止

- 不要把未经用户审核的论文直接写进 README 或 `papers/`
- 不要编造数字、单位、会议或链接
- 不要直接推送到 `main`，一律走 Pull Request
- 不要删除或改写已入库论文的数据，除非用户要求并说明原因
