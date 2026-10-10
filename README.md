<div align="center">

# FastHarness Survey

<sub>9 Papers · 1 Meeting · Updated 2026.10.10</sub>

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

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **Spotter**: Let the Embodied Model Lead, and the VLM Reflect for It<br>\[[Paper](https://arxiv.org/abs/2609.36808)\] \[[Code](https://github.com/zqc3117/Spotter)\] \[[Website](https://zqc3117.github.io/Spotter/)\] | arXiv 2026.09 | VLA 执行，VLM1 监督，出错后由 VLM2 修复并验证 | 真机：π0.5 成功率 53% → 83% | Griffith Univ.<br>Tsinghua |

<br>

<a id="code-policy"></a>

## 2. Code + Policy

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **CaP-X**: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation<br>\[[Paper](https://arxiv.org/abs/2603.22435)\] \[[Code](https://github.com/capgym/cap-x)\] \[[Website](https://capgym.github.io)\] | ICML 2026 | Coding Agent 用低级原语写代码，按执行反馈多轮修改 | 低级原语多轮 54%，好过高级 API 单轮 39% | NVIDIA<br>UC Berkeley |
| **Harness VLA**: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents<br>\[[Paper](https://arxiv.org/abs/2607.08448)\] \[[Code](https://github.com/RLinf/RPent)\] \[[Website](https://harnessvla.github.io/)\] | arXiv 2026.07 | VLA 只做接触动作，Agent 用原语负责定位、移动和重试 | LIBERO-Pro 82.4%，原 VLA 只有 50% | Tsinghua |
| **PyRUA-Lean**: Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens<br>\[[Paper](https://arxiv.org/abs/2610.01939)\] \[[Code](https://github.com/DAGroup-PKU/PyRUA-Lean)\] \[[Website](https://dagroup-pku.github.io/PyRUA-Lean/)\] | arXiv 2026.10 | VLM 用一段 Python 代码组合多个原语，减少调用次数 | 成功率 63.1% → 71.7%，token 少 65% | PKU |
| **Show-Harness**: Just a VLM Agent Can Play Robots<br>\[[Paper](https://arxiv.org/abs/2609.10522)\] \[[Code](https://github.com/showlab/Show-Harness)\] \[[Website](https://showlab.github.io/Show-Harness)\] | arXiv 2026.09 | VLM 每步输出一个语义动作，由解释器转成机器人运动 | 真机 89%，π0.5 只有 39% | NUS |
| **RoboHarness**: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning<br>\[[Paper](https://arxiv.org/abs/2607.18060)\] \[[Website](https://robo-harness.com)\] | ECCV 2026 Workshop<br>**Best Paper** | Agent 按能力调度 VLA、RL、TAMP，交接前对齐状态 | 长任务 95.2%，π0.5 单独只有 6.4% | Huawei Noah's Ark |

<br>

<a id="memory"></a>

## 3. Memory

TBD.

<br>

<a id="skill"></a>

## 4. Skill Growth

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ASPIRE**: Agentic /Skills Discovery for Robotics<br>\[[Paper](https://arxiv.org/abs/2607.00272)\] \[[Code](https://github.com/NVlabs/ASPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/aspire/)\] | arXiv 2026.07 | Agent 根据调用记录定位并修复失败，经验存入技能库 | LIBERO-Pro：CaP-Agent0 18% → 72% | NVIDIA |

<br>

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ENPIRE**: Agentic Robot Policy Self-Improvement in the Real World<br>\[[Paper](https://arxiv.org/abs/2606.19980)\] \[[Code](https://github.com/NVlabs/ENPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/enpire/)\] | arXiv 2026.06 | Agent 先建好自动复位和成功判定，再在真机上迭代训练 | 真机插销等任务练到 99% | NVIDIA<br>CMU |

<br>

<a id="boundary"></a>

## 6. Harness Evolution Boundary

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **RRSI**: Regularized Recursive Self-Improvement of Agent Harnesses<br>\[[Paper](https://arxiv.org/abs/2609.24972)\] \[[Code](https://github.com/google-research/rrsi)\] \[[Website](https://regularized-rsi.com)\] | arXiv 2026.09 | 限制每轮改动并过滤无效改动，防止过拟合评测集 | 未见任务得分 39.7 → 43.6 | Google |
