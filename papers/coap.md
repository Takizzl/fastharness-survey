# COAP: Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | arXiv 2026.10 |
| Paper | https://arxiv.org/abs/2610.12369 |
| Website | https://etmcode-bit.github.io/ |
| Team | NTU、Ropedia |

## 一句话

编码 Agent 根据执行反馈修改共享程序，最终冻结程序，用显式状态和重试完成任务。

## 问题

需要将机器人任务的执行反馈转化为可复用的程序，并区分开发探索与最终执行。

## 方法

开发阶段由编码 Agent 运行任务、分析失败、修改程序、验证并合并到共享代码库。执行阶段冻结程序，通过显式状态、程序决策、检查和重试控制机器人，不调用 VLM / VLA。

## 实验结果

论文报告 RoboDojo 42 项任务整体成功率 70.24%；40 项有程序，2 项无程序。每任务 3 个种子 × 50 个布局 = 150 条 episode 是最终评测规模，不是开发探索量。所有结果来自仿真；没有真机验证。

## 真机结果

尚未进行真机验证；已有笔记中的成绩均来自仿真。

## 来源

- [已有笔记原文](../review/2026-10-17-资料补充/sources/coap.txt)


## 核对依据

[摘要、实验与附录；作者项目主页](https://arxiv.org/html/2610.12369v1)
