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

<a id="vlm"></a>

## 1. VLM1 + VLM2

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="245" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="240" height="1"> | Result<br><img src="assets/spacer.png" width="135" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Code<br><img src="assets/spacer.png" width="55" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Spotter** | [Let the Embodied Model Lead, and the VLM Reflect for It](https://arxiv.org/abs/2609.36808) | arXiv 2026.09 | VLA 主导执行，VLM 在旁监控，确认出错才接管修复 | 真机成功率从 π0.5 的 53% 提到 83% | Griffith Univ.<br>Tsinghua | [Code](https://github.com/zqc3117/Spotter) | [Website](https://zqc3117.github.io/Spotter/) |

<a id="code-policy"></a>

## 2. Code + Policy

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="245" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="240" height="1"> | Result<br><img src="assets/spacer.png" width="135" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Code<br><img src="assets/spacer.png" width="55" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CaP-X** | [A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) | ICML 2026 | 只给低级原语，让 Coding Agent 多轮写代码、看反馈再改 | RL 训练后真机成功率从 24% 提到 84% | NVIDIA<br>UC Berkeley | [Code](https://github.com/capgym/cap-x) | [Website](https://capgym.github.io) |
| **Harness VLA** | [Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448) | arXiv 2026.07 | 冻结的 VLA 只做接触动作，其余交给 Agent 用原语完成 | LIBERO-Pro 成功率 82.4%，最强基线 43.8% | Tsinghua | [Code](https://github.com/RLinf/RPent) | [Website](https://harnessvla.github.io/) |
| **PyRUA-Lean** | [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939) | arXiv 2026.10 | 用 Python 代码块代替逐步工具调用，一次做完多步 | 仿真成功率从 63.1% 提到 71.7%，token 少 65% | PKU | [Code](https://github.com/DAGroup-PKU/PyRUA-Lean) | [Website](https://dagroup-pku.github.io/PyRUA-Lean/) |
| **Show-Harness** | [Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) | arXiv 2026.09 | VLM 每步输出一个「前移 / 抓取」式小动作来控制机器人 | 真机成功率 89%，π0.5 只有 39% | NUS | [Code](https://github.com/showlab/Show-Harness) | [Website](https://showlab.github.io/Show-Harness) |
| **RoboHarness** | [Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060) | ECCV 2026 Workshop<br>**Best Paper** | 按能力把子任务分给不同策略，交接前先对齐状态 | LIBERO-LoHo 成功率 95.2%，最强基线 64.8% | Huawei Noah's Ark | - | [Website](https://robo-harness.com) |

<a id="memory"></a>

## 3. Memory

TBD.

<a id="skill"></a>

## 4. Skill Growth

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="245" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="240" height="1"> | Result<br><img src="assets/spacer.png" width="135" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Code<br><img src="assets/spacer.png" width="55" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **ASPIRE** | [Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272) | arXiv 2026.07 | 按调用记录定位并修补失败，修好的经验存进技能库 | LIBERO-Pro 成功率从 CaP-Agent0 的 18% 提到 72% | NVIDIA | [Code](https://github.com/NVlabs/ASPIRE) | [Website](https://research.nvidia.com/labs/gear/aspire/) |

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="245" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="240" height="1"> | Result<br><img src="assets/spacer.png" width="135" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Code<br><img src="assets/spacer.png" width="55" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **ENPIRE** | [Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980) | arXiv 2026.06 | Agent 先搭好自动复位和判成败，再在真机上自己改训练代码 | 真机插销成功率从约 55% 练到 99% | NVIDIA<br>CMU | [Code](https://github.com/NVlabs/ENPIRE) | [Website](https://research.nvidia.com/labs/gear/enpire/) |

<a id="boundary"></a>

## 6. Harness Evolution Boundary

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="245" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="240" height="1"> | Result<br><img src="assets/spacer.png" width="135" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Code<br><img src="assets/spacer.png" width="55" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **RRSI** | [Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) | arXiv 2026.09 | 限制改动的提出和保留，防止 harness 过拟合评测集 | 未见任务得分从 39.7 提到 43.6 | Google | [Code](https://github.com/google-research/rrsi) | [Website](https://regularized-rsi.com) |
