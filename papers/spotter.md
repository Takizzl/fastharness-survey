# Spotter: Let the Embodied Model Lead, and the VLM Reflect for It

| 项目 | 内容 |
|---|---|
| 模块 | 1. VLM1 + VLM2 |
| Year / Venue | 2026 / `arXiv` |
| Paper | https://arxiv.org/abs/2609.36808 |
| Code | https://github.com/zqc3117/Spotter |
| Website | https://zqc3117.github.io/Spotter/ |
| Team | Griffith University（通讯作者）、清华交叉信息院（共同一作）、复旦、腾讯、同济 |
| Review | ⏳ 待审核 |

## 一句话

VLA 主导执行，VLM 并行监控，确认出错才接管修复，修完交还。

## 问题

VLA 策略执行，恢复能力较差。

## 方法

VLA Policy 正常执行；本地 VLM（Qwen3.8-27B）**监控**，根据执行历史（视觉观测、Action Chunk、Robot State）输出异常风险评分（Failure Risk Score，0–10 分），连续检测到异常后**触发恢复**；高级 VLM（GPT-6 Astra）接收失败状态与历史信息，进行失败诊断与修复规划，通过固定 **Primitive Skill 与 VLA Policy 完成恢复**，并验证恢复结果后交还控制权。

## 仿真结果

**RoboCasa（24 个任务 × 50 次）**
- π0.5：64.3% → 71.8%
- Cosmos Policy：67.9% → 73.5%

**RoboTwin 2.0 Hard（50 个任务 × 10 次）**
- π0.5：47.2% → 57.0%

**补充分析**
- 失败恢复分析：VLA 自身重采样 / 语言反馈 / 恢复数据微调，修复率都不到 10%
- 动作评分评估、效率评估、消融实验

## 真机结果

**Franka Research 3（3 个任务 × 10 次）**
- π0.5：53% → 83%

**任务结果**
- 叠杯：6/10 → 8/10
- 方块放置：7/10 → 10/10
- 两段任务：3/10 → 7/10
