# Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens（PyRUA-Lean）

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | 2026 / `arXiv` |
| Paper | https://arxiv.org/abs/2610.01939 |
| Code | https://github.com/DAGroup-PKU/PyRUA-Lean |
| Website | https://dagroup-pku.github.io/PyRUA-Lean/ |
| Team | 北大（周大权组）、NUS、NVIDIA |
| Review | 已入库（与审阅表一致） |

## 一句话

用 Python 代码块代替逐步工具调用，一次做完多步，只回传需要的信息。

## 问题

Tool Calling 每步调一次 VLM，token 开销大。

## 方法

把原语和 VLA Policy 封装成 Python 对象 robo，VLM **一次写一个代码块**，在块内**串联多个原语、做条件判断和本地重试**，变量跨代码块保留；只有代码中**主动请求**的图像和打印信息才回传给 VLM。

## 仿真结果

**LIBERO-PRO + RoboTwin 2.0 + RoboCasa365（共 700 个实例，同用 GPT-6 Astra）**
- 总体：63.1% → 71.7%（标题里的「14%」是相对提升）
- LIBERO-PRO：83.0% → 94.0%
- RoboTwin 2.0：60.0% → 69.2%
- RoboCasa365 原子任务：78.9% → 86.7%
- RoboCasa365 组合任务：34.4% → 39.4%

**效率（两边都做成的任务）**
- LLM 调用次数少 49%，输入 token 少 65%

**补充分析**
- token 节省来源分解
- 只按需回图的消融
- 去掉 VLA / 操作指南的消融
- RoboDojo 3 个任务小试：3.4% → 26.7%

## 真机结果

没做（论文写明）。
