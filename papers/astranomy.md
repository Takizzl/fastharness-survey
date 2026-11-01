# Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy

| 项目 | 内容 |
|---|---|
| 模块 | 12. Perception and Execution |
| Year / Venue | 技术报告 2026.10 |
| Team | NVIDIA Seattle Robotics Lab |
| Paper | https://research.nvidia.com/labs/srl/projects/astranomy/ |
| Website | https://research.nvidia.com/labs/srl/projects/astranomy/ |

[返回分类](../README.md#perception-execution)

## 一句话

比较 Astra 直接控制、Agent 执行和监督下游策略，分析几何、历史与动作接口的影响及运行成本。

## 问题

Astra的执行效果同时受到输入信息、动作接口、上下文与执行循环影响。

## 方法

固定Astra，对比直接控制、Agent执行和监督下游策略，消融几何、历史与动作接口。

相机与夹爪几何、当前episode的模型文字与决策图像均影响执行。当前状态与运动反馈是共同输入。历史消融没有分别量化计划、动作记录、推理文字各自贡献，也未直接度量位置判断与任务进度判断的变化。

## 实验结果

RoboLab-120共120任务、每任务5次：Direct 66.3%，Agentic 74.8%，Orchestrated 66.5%。历史小样本：文本历史加当前图20/23，仅视觉历史13/23，两者完整23/23；不是轨迹理解准确率，也不是跨任务经验。

## 真机结果

本文是RoboLab仿真研究，不将这些成功率标为真机结果。Direct单次推理18.56秒；Agentic成本按成功episode计为30.9M tokens、36.40美元。

来源：官方在线技术报告§2、§3.1.2–3.1.3、图2、§4；本地阅读收获。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
