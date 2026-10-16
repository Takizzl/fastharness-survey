# ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

| 项目 | 内容 |
|---|---|
| 模块 | 5. 真机迭代恢复 |
| Year / Venue | 2026 / `CoRL`（依据：arXiv v2 备注「2026 Conference on Robot Learning」；UT Austin RPL、CMU LeCAR 论文列表均列为 CoRL 2026） |
| Paper | https://arxiv.org/abs/2606.19980 |
| Code | https://github.com/NVlabs/ENPIRE |
| Website | https://research.nvidia.com/labs/gear/enpire/ |
| Team | NVIDIA GEAR、CMU（Guanya Shi 组）、UC Berkeley |
| Review | 已入库（与审阅表一致） |

## 一句话

先让 Agent 搭好自动复位和成功判定，再让它在真机上自己改训练代码迭代策略。

## 问题

真机策略训练依赖人做复位、判成败和调参。

## 方法

**阶段一**：Agent 在人反馈下写好**安全边界、自动复位和二值成功判定**（用成功 / 失败示教测准确率），之后固定为**不可修改的 Gym 接口**。**阶段二**：Agent **自己查文献、提假设、改训练代码**（BC、RL、启发式、Code-as-Policy），上真机 rollout，按成功率决定留不留；多台机器各配一个 Agent，**通过 Git 共享和合并**有效改动。

## 仿真结果

**Gym-PushT**
- 约 2 小时到 95%

**RoboCasa365（8 个任务 × 40 次）**
- ENPIRE：约 76%
- GR00T：约 53%
- CaP-X：约 27%（从图上读取）

**补充分析**
- 1 / 4 / 8 台机器扩展
- 机器与 token 利用率
- 有无原生视觉对比
- Codex / Claude Code / Kimi 对比

## 真机结果

**8 台双臂 YAM**
- 插销、Push-T、剪扎带：最终 99%（成功率定义：允许失败后重试 8 次）

**任务结果**
- 插销：约 55% → 95%（4 小时，从曲线读取）
- 插销 8 台并行：约 40 分钟接近 100%（单台 1.5 小时以上）
- Push-T：8 台并行约 2 小时达标（单台约 5 小时）
