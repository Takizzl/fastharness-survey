# GPT-as-Policy: GPT 6 Astra as an Embodied Policy

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | 技术报告 2026 |
| Paper | https://anonymous-report-421.github.io/public-website/?view=1 |
| Code | https://github.com/anonymous-report-421/GPT-as-Policy |
| Website | https://anonymous-report-421.github.io/public-website/?view=1 |
| Team | Galbot（银河通用） |

## 一句话

GPT 检查 π0.5 动作与执行历史，确认失败或子目标错位后修正，恢复后交还控制。

## 问题

GPT 直接控制机器人的表现有限，需要判断何时修正 VLA 动作。

## 方法

GPT 检查 π0.5 动作与执行历史，确认失败或子目标错位后修正，恢复后交还控制。

## 仿真结果

10 个 RoboDojo 任务，各 5 个对齐样例。混合策略 24/50 成功（48%），Score 62.60（50 个有效分数）；Direct 13/50 成功（26%），Score 37.81（48 个有效分数）。混合策略修正了 14.4% 的已执行控制步。成功率分母均为 50，不能把 Direct 的分数分母 48 用作成功率分母。

## 来源可靠性与公开范围

作者发布的技术报告、实际评测代码、逐样例 JSON 与 CSV 可以互相核对。用 evaluation_cases.json 重算得到 24/50、13/50、0.626、0.378125，修正步比例 14.4421%。外部官方模型结果为重加权公开参考，并非同种子重跑；原始模型会话、操作日志、仿真资产和权重不在公开快照中。

## 来源

- [项目页面](https://anonymous-report-421.github.io/public-website/?view=1)
- [代码与发布说明](https://github.com/anonymous-report-421/GPT-as-Policy)
- [技术报告（非已确认同行评审论文）](https://anonymous-report-421.github.io/public-website/?view=1)
- [逐样例元数据](https://github.com/anonymous-report-421/GPT-as-Policy/blob/main/public_results/evaluation_cases.json)
- [分数表](https://github.com/anonymous-report-421/GPT-as-Policy/blob/main/public_results/scores.csv)
- [控制判断提示](https://github.com/anonymous-report-421/GPT-as-Policy/blob/main/hybrid_rollout/robodojo/skill/gate_prompt.md)

## 团队来源

[Galbot 官方报告](https://galaxygeneralrobotics.github.io/astra-policy/index.html) · [Galbot Team 论文](https://arxiv.org/abs/2609.38537)

## 核对依据

[项目公开逐例数据；Galbot 官方报告与 arXiv:2609.38537](https://anonymous-report-421.github.io/public-website/?view=1)
