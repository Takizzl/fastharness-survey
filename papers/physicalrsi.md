# PhysicalRSI: Physical RSI 1.0: Recursive Self-Harness for Scaling Embodied Skills

| 项目 | 内容 |
|---|---|
| 模块 | 7. RSI Projects |
| Year / Venue | Preview 2026 |
| Code | https://github.com/PhysicalRSI/PhysicalRSI |
| Website | https://mmlab.hk/research/PhysicalRSI |
| Team | HKU MMLab & KAI（RoboDojo 官方榜单署名）；代码引用为 MMLab & PhysicalRSI contributors |

## 一句话

Agent 根据执行反馈改写 harness，评测候选并保留更优版本，继承代码技能与任务记忆。

## 问题

固定策略难应对开放任务，需要根据执行反馈改写、筛选并积累控制技能。

## 方法

Agent 根据执行反馈改写 harness，评测候选并保留更优版本，继承代码技能与任务记忆。

## 仿真结果

RoboDojo 官方榜单公开数据：Score 36.27、SR 31.38%，团队 HKU MMLab & KAI；网站提及 52 个 task×layout settings。项目网页使用 2026-10-03 结果快照、注明 10-08 核对。2026-10-14 读取的基准前端数据快照为 10-09，PhysicalRSI 仍是相同分数，但 VPP2 已为 Score 39.26、SR 32.26%，不沿用项目页旧的 No.1 文案。

## 来源可靠性与公开范围

MMLab 项目页与 PhysicalRSI 代码仓库双向对应，仓库 README 和 CITATION 明确 Preview release；可见真实框架、实验运行时、Self-Harness、baseline 集成及示例源码，不能称为完整正式论文复现。Score 和 SR 已与基准官网发布的前端数据交叉对应。独立论文 PDF / arXiv 未找到。代码版本晚于项目页快照，不能直接假定最新 preview 就是历史榜单结果的完整可复现产物。

## 来源

- [项目页面](https://mmlab.hk/research/PhysicalRSI)
- [代码与发布说明](https://github.com/PhysicalRSI/PhysicalRSI)
- [RoboDojo 官方榜单](https://robodojo-benchmark.com/leaderboard)
- [基线集成](https://github.com/XPolicyLab/XPolicyLab/tree/main/policy/physicalRSI)
- [Preview 声明](https://github.com/PhysicalRSI/PhysicalRSI#physicalrsi)

## 开发、评测与经验复用

开发模型返回新代码和经验；评测选择代理返回现成技能的选择。默认混合模式先比较已有 VLA 的开发分数，未达阈值才进入代码开发；learned_skill / code_policy 模式会改变分支。候选与父版本在同一批、排除开发布局的验证案例上比较，满足提升和不退步条件才接受。

memory_rules.json 提供开发修改参考及 policy(robot, memory) 参数；policy_memory.json / run_context 供评测选择代理使用；发布包 programs/steps 供技能执行器绑定并执行已注册方法。

依据本地开发代码 3c8cf7f12d4041babe30bab98854cc504a5afe88 与发布适配器 393f730788e7277c7d86829dd5806a924ac31e74；与仓库条目中的另一个核查版本分开记录。公开阶段仍是 Preview。

尚无开发 memory_rules 到发布操作记忆的完整转换历史，也没有 22 个发布技能由该流程生成的完整证据链；不能补成已确认事实。

[笔记原文](../review/2026-10-17-资料补充/sources/physicalrsi.txt)


## 核对依据

[官方榜单 2026-10-09 快照与 Preview 仓库](https://mmlab.hk/research/PhysicalRSI)
