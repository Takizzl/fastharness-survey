# ASPIRE: Agentic /Skills Discovery for Robotics

| 项目 | 内容 |
|---|---|
| 模块 | 4. 技能增长 |
| Year / Venue | 2026 / `arXiv` |
| Paper | https://arxiv.org/abs/2607.00272 |
| Code | https://github.com/NVlabs/ASPIRE |
| Website | https://research.nvidia.com/labs/gear/aspire/ |
| Team | NVIDIA GEAR（Jim Fan、朱玉可组）、UMich、UIUC、UC Berkeley、CMU |
| Review | ⏳ 待审核 |

## 一句话

按原语级 trace 定位并修补失败，验证有效的修复沉淀为技能库供后续任务复用。

## 问题

程序失败后难定位原因，修复经验无法跨任务积累。

## 方法

**执行引擎**记录每次原语调用的输入、输出、返回状态和前后关键帧，Coding Agent（Claude Code）据此**定位失败的原语并只修补该部分**；**进化搜索**每轮生成 K 个候选程序，以前 3 名和剩余失败为参考继续改，分数更高才替换；在验证种子上有效的修复由 Coordinator **审核后写入 Skill Library**，后续任务检索使用。

## 仿真结果

**LIBERO-Pro（30 个任务 × 50 次，对比 CaP-Agent0）**
- 18% → 72%

**Robosuite（7 个任务 × 100 次）**
- 平均：68% → 81%
- 双臂交接：20% → 92%

**BEHAVIOR-1K（2 个家务任务 × 25 次）**
- 拿收音机：56% → 88%
- 拿汽水罐：72% → 88%

**补充分析**
- 执行引擎 / 进化搜索消融：14% → 62% → 72%
- 进化轮数分析
- 技能库零样本迁移：LIBERO-Pro Long 23% / 38%，基线约 4%

## 真机结果

**双臂 YAM（3 个任务 × 20 次，技能从 Franka 仿真迁移）**
- 碗放盘子：20/20 → 20/20
- 拿汽水罐：13/20 → 19/20
- 开抽屉：0/20 → 11/20
- token 少 2~9 倍
