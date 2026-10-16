# CHANGELOG

最新的放最上面。每次合入都写清楚：新增了哪些论文、改了哪些字段、谁审核的。

## 2026-10-16 · Robota-Embed 汇报合并至 Memory

- 根据用户已有《Robota-Embed论文解读.html》与配套阅读记录，新增 [Robota-Embed](papers/robota-embed.md)，同步 Memory 五列表格和审阅表，标待人工审核。
- 方法突出视觉、语言和动作 embedding 检索记忆；区分检索准确率、机器人成功率、真机任务进度与 token 成本。
- 与论文 v1 表格核对：ManiSkill 五任务每条件每任务 20 次，Astra Direct 24%→Embed2Evolve 68%；开发积累长期记忆，正式测试固定记忆及配置。
- 保留团队的 RoboDojo + Astra 经验复用目标及待验证问题，不将 ManiSkill 成绩写成 RoboDojo 结果。官方代码、权重入口尚未核实。
- 来源核对与中文整理：Codex；原有条目未修改，未新增机器人实验。

## 2026-10-14 · RSI 项目与 Code + Policy 来源核查

- 新增 [LoopROS / LoopMaster](papers/loopros.md)、[PhysicalRSI](papers/physicalrsi.md) 到 RSI Projects，新增 [GPT-as-Policy](papers/gpt-as-policy.md) 到 Code + Policy；README 与审阅表使用现有表格样式，均标待审核。
- 核实官网与代码对应关系、公开范围和结果口径。LoopROS 只有客户端公开，论文 coming soon，10 任务 100 回合自报 82%；PhysicalRSI 仅 Preview，榜单 Score 36.27 / SR 31.38% 可交叉核对，旧 No.1 排名不沿用。
- GPT-as-Policy 公共逐样例表核算：混合 24/50、Direct 13/50；Direct Score 只用 48 个有效值。外部官方模型是重加权参考，并非同种子重跑。
- 保存核查链接、代码版本和证据摘要；原有已入库论文与 JitRL 内容不变。来源核查与中文整理：Codex；未运行付费模型或机器人实验。

## 2026-10-12 · 导入 FastHarness 文档与讨论

- 按用户要求，Memory 改为与其他类别相同的五列表格；方法提取自文档，缺失字段用 —，讨论原话保留在 Ideas。待审核行允许缺失元数据，已入库行仍执行原有完整性检查。

- 补充 README 的 Memory 栏：首页展示 JitRL 的待审核问题与方法，以及文档中的 Memory 和经验复用讨论；目录明确区分已入库与待审核数量。
- 保存用户提供的 [FastHarness 原始文档及配图](meetings/sources/2026-10-12-FastHarness/FastHarness.md)，补充第一次会议的文档入口；原文未注明会议日期。
- 导入 [团队思考与测评方向](ideas/2026-10-12-FastHarness讨论与测评.md)，保留原话，包含 RPG 阅读线索、Memory、VLA 能力学习与仿真 / 真机测评设想。
- 审阅表 Memory 类别新增 JitRL：问题与方法取自该文档，标为待审核，实验、团队信息尚未提供；未同步进 README 的论文列表。
- README 与 Ideas 增加讨论入口；已有 9 篇入库论文的内容和审核状态未修改。
- 来源为用户提供的文档；文件归档、分栏与导航由 Codex 整理，未新增论文结论。

## 2026-10-11 · 链接与发表信息核对

- [ENPIRE](papers/enpire.md)：Venue 由 arXiv 改为 **CoRL 2026**（arXiv v2 备注 + UT Austin RPL、CMU LeCAR 论文列表）
- [RoboHarness](papers/roboharness.md)：补上 Code 链接（官方仓库 markli1hoshipu/RoboHarness，目前只有项目说明）
- 9 篇论文的 Paper、Code、Website 共 27 个链接全部检查可访问

## 2026-10-10 · 仓库初始化

**新增论文（9 篇）**

| 模块 | 论文 |
|---|---|
| 1. VLM1 + VLM2 | [Spotter](papers/spotter.md) |
| 2. Code + Policy | [CaP-X](papers/cap-x.md)、[Harness VLA](papers/harness-vla.md)、[PyRUA-Lean](papers/pyrua-lean.md)、[Show-Harness](papers/show-harness.md)、[RoboHarness](papers/roboharness.md) |
| 4. 技能增长 | [ASPIRE](papers/aspire.md) |
| 5. 真机迭代恢复 | [ENPIRE](papers/enpire.md) |
| 6. Harness 迭代边界 | [RRSI](papers/rrsi.md) |

**新增会议**
- [第一次会议](meetings/01-第一次会议.md)
