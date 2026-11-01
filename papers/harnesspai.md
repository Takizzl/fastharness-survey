# HarnessPAI: An Evolving Harness for Physical AI

| 项目 | 内容 |
|---|---|
| 模块 | 6. Harness Evolution |
| Year / Venue | arXiv 2026.09 |
| Team | Darwin Agent Team；小米、清华大学、南京大学 |
| Paper | https://arxiv.org/abs/2609.29166v2 |
| Code | https://github.com/Darwin-Agent/HarnessPAI |
| Website | https://darwin-agent.github.io/HarnessPAI/ |

[返回分类](../README.md#harness-evolution)

## 一句话

固定动作模型，跨 rollout 修改并验证任务程序，将失败修复按工作流节点存储；单次 rollout 执行固定程序及预设检查。

## 问题

动作模型遇到目标和布局变化易失败，同一任务反复在线规划也增加推理成本。

## 方法

Agent跨rollout改写验证程序，按工作流节点存储修复；执行时固定程序调用动作模型。

Task Memory关联任务与程序，Structured Skill Memory按工作流阶段存失败和修复，Executable Code Memory保存验证实现。开发中执行、诊断、修改并验证，单次rollout内程序固定但仍使用感知反馈和预设恢复。

## 实验结果

LIBERO-PRO 60扰动任务、每任务50 seeds：34.9%→96.5%，含15个开发seed和35个额外seed；RoboCasa Atomic-Seen 18任务×20次：65.0%→92.2%。不能按纯留出任务泛化解释。

## 真机结果

七类实验场景为仿真，未报告真机批量成功率。另用成功程序轨迹SFT π0.5，在LIBERO-PRO上34.9%→73.7%。

来源：原论文v2 §4–5、表4–7、图8–11及18–23；本地精读笔记与官方代码。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
