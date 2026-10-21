# CHANGELOG

最新的放最上面。每次合入都写清楚：新增了哪些论文、改了哪些字段、谁审核的。

## 2026-10-21 · 清理详情入口

- 删除首页和论文汇总表的详情、资料整理与来源核对入口文字。

## 2026-10-21 · Memory 新增 MemEvolve

- 新增 MemEvolve 详情、Memory 首页索引和论文汇总表，Memory 共 4 项。
- 对照论文表 2–3、附录 B.1 与官方仓库整理方法、实验、主要单位及 ICML 2026 信息；区分跨任务评测、演化使用题目和 pass@1 / pass@3。
- Codex 核对来源并进行提交前审查。

## 2026-10-17 · 核实后发布与页面清理

- 全部 17 个条目按论文、官方项目及已有原文记录核对，新增逐项来源索引。
- 移除所有公开条目中的审核状态和流程说明，删除过期补充草稿；无依据的代码、单位及结果字段不展示。
- GPT-as-Policy 团队确认为 Galbot（银河通用）；GroundingPI 补入表 5 的每框 token 数，区分序列化成本与机器人成功率。
- 更新收录规范与检查器，缺少来源或含未完成发布字段时阻断提交；增加发布内容回归检查。

## 2026-10-17 · 简写与待审核项目链接核查

- 精简首页 COAP、GroundingPI 重复标题、方法和机构名。
- 逐项核查 8 个待审核项目：正常链接保留；补 PhysMem 官方代码、GroundingPI 与 COAP 主页、COAP 团队和 JitRL 官方仓库声明的 ICML Spotlight 信息。
- PhysMem 解读固定链接至 v1，避免旧标题及方法与新版页面混用。保留技术报告、Preview 和未确认字段的事实边界。

## 2026-10-17 · 按已有资料整合论文与机制补充

- 按用户要求整合 7 项补充：新增 JitRL、COAP、PhysMem、GroundingPI 详情卡，同步首页和审阅表；新增感知基础模型分类。
- 补充 ASPIRE 的修复/搜索协议、HarnessVLA 的建库与评测边界、PhysicalRSI 的开发/评测及三类记忆分工；保留原已审核结果。
- 导入 7 份本地笔记快照及 SHA-256 清单，保留 17 项缺项审查记录。
- JitRL 固定记忆结果注明 165 个留出任务与基线；PhysMem 定性图不改写为总体成功率；PhysicalRSI 仍标 Preview。
- 整合由用户授权；尚无依据的会议、代码公开状态与实验字段继续标待核实，不把整合授权作为这些事实已获确认。

## 2026-10-16 · 全仓库一致性与检查修复

- 修复审阅表 Code + Policy、Memory、RSI 的合并单元格行数，避免新增条目错列；论文内容与实验数字保持不变。
- 修复查询脚本遗漏无 arXiv 项目、错误匹配正文引用与错误宣称全部内容已人工审核的问题；按元数据定位来源，保留逐条审核状态。
- 9 篇已入库论文详情页的 Review 字段与审阅表同步；明确待审核报告、Preview 的首页展示规则。
- 格式检查新增条目对应关系、模块、审核状态、总数和站内目标检查；新增 8 项回归测试并纳入 CI，覆盖类别计数、检索、表格列数、网络诊断与失败退出逻辑。
- 外链覆盖扩展至维护文档和审阅表，正确解析 Markdown 转义和 HTML 实体。原始文档归档不改写。全量 47 条外链本机验证成功。
- 移除误跟踪的 Python 字节码，添加缓存忽略规则；实际渲染核对审阅表排版。

## 2026-10-16 · 区分格式与外链检查

- 工作流改名 repository-checks，格式与链接检查拆为独立任务。
- 明确 HTTP 错误继续阻断；网络连接异常、限流、服务端错误标为访问未核实警告，重试一次并打印具体原因，不计为链接验证通过。移除吞掉所有异常的处理。
- 验证分类、重试、退出状态；本机全量 45 条链接通过。GitHub 环境的站点访问情况以 CI 注释为准。

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
