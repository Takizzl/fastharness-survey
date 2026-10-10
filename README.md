<div align="center">

# FastHarness Survey


</div>

## 当前主线 · [第一次会议](meetings/01-第一次会议.md)

1. 调研 GPT + VLM 的结合方式相关方法，怎么外挂 VLM，Qwen 等 VLM 尽量做选择题
2. 调研 Code + VLA 怎么结合起来的，策略如何组织（定位到源码分析）（有没有 WAM）
3. 考虑阶段 2 的事，专注 Memory 怎么去做，从 LLM 的角度迁移

**要求：** 需要兼容多个 LLM 和下游 policy

## Contents

| Category | Focus | Papers |
|:---:|:---:|:---:|
| [1. VLM1 + VLM2](#vlm) | Plugging in VLMs, failure reflection | 1 |
| [2. Code + Policy](#code-policy) | Code / orchestration driving policies | 5 |
| [3. Memory](#memory) | Memory mechanisms | 0 |
| [4. Skill Growth](#skill) | Accumulating a skill library | 1 |
| [5. Real-Robot Self-Improvement](#real-robot) | Iterating policies on real robots | 1 |
| [6. Harness Evolution Boundary](#boundary) | Guarding against overfitting | 1 |

<br>

<a id="vlm"></a>

## 1. VLM1 + VLM2

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **Spotter**: Let the Embodied Model Lead, and the VLM Reflect for It<br>\[[Paper](https://arxiv.org/abs/2609.36808)\] \[[Code](https://github.com/zqc3117/Spotter)\] \[[Website](https://zqc3117.github.io/Spotter/)\] | arXiv 2026.09 | VLA 执行任务；VLM1（Qwen）给每段动作打出错风险分，出错时 VLM2（Astra）找原因、修复并确认修好 | Franka 真机 3 个任务各 10 次：成功率从 53% 提到 83% | Griffith Univ.<br>Tsinghua |

<br>

<a id="code-policy"></a>

## 2. Code + Policy

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **CaP-X**: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation<br>\[[Paper](https://arxiv.org/abs/2603.22435)\] \[[Code](https://github.com/capgym/cap-x)\] \[[Website](https://capgym.github.io)\] | ICML 2026 | Coding Agent 只用分割、逆运动学、运动规划这类底层接口写代码，每轮看报错和画面变化再改 | CaP-Bench（Robosuite 7 个任务）：底层接口多轮 54%，高层接口单次 39% | NVIDIA<br>UC Berkeley |
| **Harness VLA**: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents<br>\[[Paper](https://arxiv.org/abs/2607.08448)\] \[[Code](https://github.com/RLinf/RPent)\] \[[Website](https://harnessvla.github.io/)\] | arXiv 2026.07 | VLA 只负责抓取和放置；Agent 用固定的移动、旋转、夹爪动作摆好位置，没抓住就重摆再抓 | LIBERO-Pro 扰动测试：82.4%，单用 VLA 50.0% | Tsinghua |
| **PyRUA-Lean**: Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens<br>\[[Paper](https://arxiv.org/abs/2610.01939)\] \[[Code](https://github.com/DAGroup-PKU/PyRUA-Lean)\] \[[Website](https://dagroup-pku.github.io/PyRUA-Lean/)\] | arXiv 2026.10 | VLM 写一段 Python 一次完成整段动作并自带重试，只把需要看的图片发回 VLM | LIBERO-Pro、RoboTwin 2.0、RoboCasa365：63.1% → 71.7%，token 减少 65% | PKU |
| **Show-Harness**: Just a VLM Agent Can Play Robots<br>\[[Paper](https://arxiv.org/abs/2609.10522)\] \[[Code](https://github.com/showlab/Show-Harness)\] \[[Website](https://showlab.github.io/Show-Harness)\] | arXiv 2026.09 | VLM 每一步只输出一个动作（前移、上升、旋转、抓取、松开），再换算成 2 或 4 厘米的移动 | Franka 真机 10 个抓放任务：89%，π0.5 只有 39% | NUS |
| **RoboHarness**: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning<br>\[[Paper](https://arxiv.org/abs/2607.18060)\] \[[Code](https://github.com/markli1hoshipu/RoboHarness)\] \[[Website](https://robo-harness.com)\] | ECCV 2026 Workshop<br>**Best Paper** | Agent 判断 VLA、强化学习、运动规划器各擅长什么来分配子任务，换策略前先把机器人移到对方熟悉的位置 | LIBERO-LoHo 长任务：95.2%，单用 π0.5 只有 6.4% | Huawei Noah's Ark |

<br>

<a id="memory"></a>

## 3. Memory

TBD.

<br>

<a id="skill"></a>

## 4. Skill Growth

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ASPIRE**: Agentic /Skills Discovery for Robotics<br>\[[Paper](https://arxiv.org/abs/2607.00272)\] \[[Code](https://github.com/NVlabs/ASPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/aspire/)\] | arXiv 2026.07 | 记录每一步调用的输入、输出和画面，Agent 只改出错的那一步，验证有效的修复存进技能库 | LIBERO-Pro 扰动测试：72%，之前最好的 CaP-Agent0 18% | NVIDIA |

<br>

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ENPIRE**: Agentic Robot Policy Self-Improvement in the Real World<br>\[[Paper](https://arxiv.org/abs/2606.19980)\] \[[Code](https://github.com/NVlabs/ENPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/enpire/)\] | CoRL 2026 | Agent 先写好自动复位、自动判成败的程序并固定，再在真机上反复改训练代码，8 台机器用 Git 共享 | YAM 双臂真机插销、推 T、剪扎带：99%（允许重试 8 次） | NVIDIA<br>CMU |

<br>

<a id="boundary"></a>

## 6. Harness Evolution Boundary

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **RRSI**: Regularized Recursive Self-Improvement of Agent Harnesses<br>\[[Paper](https://arxiv.org/abs/2609.24972)\] \[[Code](https://github.com/google-research/rrsi)\] \[[Website](https://regularized-rsi.com)\] | arXiv 2026.09 | 每轮能改的地方逐轮减少；只保留不含测试题答案、提升超过随机波动、多花的算力有回报的改动 | JobBench、GDPval、APEX-Agents 平均：39.7 → 43.6 | Google |
