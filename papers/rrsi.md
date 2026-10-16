# RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

| 项目 | 内容 |
|---|---|
| 模块 | 6. Harness 迭代边界 |
| Year / Venue | 2026 / `arXiv` |
| Paper | https://arxiv.org/abs/2609.24972 |
| Code | https://github.com/google-research/rrsi |
| Website | https://regularized-rsi.com |
| Team | Google Cloud AI Research（Tomas Pfister 组）、UNC、Stanford |

## 一句话

在 harness 进化的「提改动」和「留改动」两端加约束，防止越改越贴合评测集。

## 问题

Harness 自进化用同一批题提改动、选改动，出现自适应过拟合。

## 方法

**提出端**：每轮可改动数量随轮次递减；记录全部历史，失败过的思路作为反面证据；停滞时转向没改过的组件。**选择端**：Critic 先**筛掉带评测题答案的改动**；提升必须超过重复评测的**噪声带**；多花的 token 要和提升成比例；长期没贡献的组件**剪掉**。

## 实验结果（非机器人基准）

**Agent 工作任务（在 Harvey LAB 上进化）**
- 未见任务 JobBench / GDPval / APEX-Agents 平均：39.7 → 43.6
- 不加选择端筛选：Harvey LAB 91.5，未见任务只有 41.0

**编程任务（在 Terminal-Bench 上进化）**
- Terminal-Bench：74.2 → 80.2
- 迁到 SWE-bench Verified：82.0 → 83.8

**补充分析**
- 正则项消融
- 换 Gemini 3.5 Flash
- 迁移到更弱的模型
- token 比无约束进化少约 30%

## 真机结果

不涉及（不是机器人工作）。

## 核对依据

[未见任务汇总](https://arxiv.org/abs/2609.24972)
