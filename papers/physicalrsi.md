# PhysicalRSI: Physical RSI 1.0: Recursive Self-Harness for Scaling Embodied Skills

| 项目 | 内容 |
|---|---|
| 模块 | 7. RSI Projects |
| Year / Venue | Preview 2026 |
| Paper | - |
| Code | https://github.com/PhysicalRSI/PhysicalRSI |
| Website | https://mmlab.hk/research/PhysicalRSI |
| Team | HKU MMLab & KAI（RoboDojo 官方榜单署名）；代码引用为 MMLab & PhysicalRSI contributors |
| Review | 仅 Preview；公开架构与基线代码；无已核实独立论文；待人工审核 |

## 一句话

Agent 根据执行反馈改写 harness，评测候选并保留更优版本，继承代码技能与任务记忆。

## 问题

固定策略难应对开放任务，需要根据执行反馈改写、筛选并积累控制技能。

## 方法

Agent 根据执行反馈改写 harness，评测候选并保留更优版本，继承代码技能与任务记忆。

## 仿真结果

RoboDojo 官方榜单公开数据：Score 36.27、SR 31.38%，团队 HKU MMLab & KAI；网站提及 52 个 task×layout settings。项目网页使用 2026-10-03 结果快照、注明 10-08 核对。2026-10-14 读取的基准前端数据快照为 10-09，PhysicalRSI 仍是相同分数，但 VPP2 已为 Score 39.26、SR 32.26%，不沿用项目页旧的 No.1 文案。

## 真机结果

官网当前主要为仿真与技能演示；未找到可确认的真机量化成功率。代码中物理机器人 SDK 与部署为外部依赖，演示不能视为真机基准验证。

## 来源可靠性与公开范围

MMLab 项目页与 PhysicalRSI 代码仓库双向对应，仓库 README 和 CITATION 明确 Preview release；可见真实框架、实验运行时、Self-Harness、baseline 集成及示例源码，不能称为完整正式论文复现。Score 和 SR 已与基准官网发布的前端数据交叉对应。独立论文 PDF / arXiv 未找到。代码版本晚于项目页快照，不能直接假定最新 preview 就是历史榜单结果的完整可复现产物。

核查日期：2026-10-14。来源核验与中文整理：Codex；仍待人工审核。代码核查版本：`aa92a7dd009cb7cd9ef45af6d95809c5174be0ec`。

## 来源

- [项目页面](https://mmlab.hk/research/PhysicalRSI)
- [代码与发布说明](https://github.com/PhysicalRSI/PhysicalRSI)
- [RoboDojo 官方榜单](https://robodojo-benchmark.com/leaderboard)
- [基线集成](https://github.com/XPolicyLab/XPolicyLab/tree/main/policy/physicalRSI)
- [Preview 声明](https://github.com/PhysicalRSI/PhysicalRSI#physicalrsi)
