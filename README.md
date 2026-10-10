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

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **Spotter**: Let the Embodied Model Lead, and the VLM Reflect for It<br>\[[Paper](https://arxiv.org/abs/2609.36808)\] \[[Code](https://github.com/zqc3117/Spotter)\] \[[Website](https://zqc3117.github.io/Spotter/)\] | arXiv 2026.09 | VLA 执行；VLM1（Qwen3.8-27B）输出 Failure Risk Score 监督，VLM2（Astra）诊断修复并验证后交还 | Franka 真机 3 任务 × 10 次：π0.5 53% → 83% | Griffith Univ.<br>Tsinghua |

<br>

<a id="code-policy"></a>

## 2. Code + Policy

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **CaP-X**: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation<br>\[[Paper](https://arxiv.org/abs/2603.22435)\] \[[Code](https://github.com/capgym/cap-x)\] \[[Website](https://capgym.github.io)\] | ICML 2026 | Coding Agent 只用 Low-level Primitive（SAM3、IK、Motion Planning）写代码，读 stdout、报错和 VDM 后改代码 | CaP-Bench（Gemini-3-Pro）：低级原语多轮 54%，高级 API 单轮 39% | NVIDIA<br>UC Berkeley |
| **Harness VLA**: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents<br>\[[Paper](https://arxiv.org/abs/2607.08448)\] \[[Code](https://github.com/RLinf/RPent)\] \[[Website](https://harnessvla.github.io/)\] | arXiv 2026.07 | 冻结 VLA 封装成 vla_act 只做抓取放置，Agent 用 move_to、rotate、set_gripper、release、navigate 定位移动 | LIBERO-Pro：82.4%，原 VLA 50.0%，RATS 43.8% | Tsinghua |
| **PyRUA-Lean**: Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens<br>\[[Paper](https://arxiv.org/abs/2610.01939)\] \[[Code](https://github.com/DAGroup-PKU/PyRUA-Lean)\] \[[Website](https://dagroup-pku.github.io/PyRUA-Lean/)\] | arXiv 2026.10 | VLM 写 Python 代码块调用 robo 原语，块内做判断和重试，只回传代码主动请求的图像 | 700 个仿真实例：63.1% → 71.7%，输入 token 减少 65% | PKU |
| **Show-Harness**: Just a VLM Agent Can Play Robots<br>\[[Paper](https://arxiv.org/abs/2609.10522)\] \[[Code](https://github.com/showlab/Show-Harness)\] \[[Website](https://showlab.github.io/Show-Harness)\] | arXiv 2026.09 | VLM 每步选一个 Semantic Action Unit（MV_*、ROTATE、GRASP、RELEASE），Interpreter 转成 2 / 4 cm 末端位移 | Franka 10 个任务：Gemini 零样本 89%，π0.5 39% | NUS |
| **RoboHarness**: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning<br>\[[Paper](https://arxiv.org/abs/2607.18060)\] \[[Website](https://robo-harness.com)\] | ECCV 2026 Workshop<br>**Best Paper** | Codex 按 Policy Card 把子任务分给 VLA、RL、TAMP，Memory Bridge 交接前把机器人移到下一策略的熟悉状态 | LIBERO-LoHo：95.2%，H-WM 64.8%，π0.5 6.4% | Huawei Noah's Ark |

<br>

<a id="memory"></a>

## 3. Memory

TBD.

<br>

<a id="skill"></a>

## 4. Skill Growth

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ASPIRE**: Agentic /Skills Discovery for Robotics<br>\[[Paper](https://arxiv.org/abs/2607.00272)\] \[[Code](https://github.com/NVlabs/ASPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/aspire/)\] | arXiv 2026.07 | 执行引擎记录每次原语调用，Claude Code 只修失败的原语，验证通过的修复写入 Skill Library | LIBERO-Pro：72%，CaP-Agent0 18% | NVIDIA |

<br>

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ENPIRE**: Agentic Robot Policy Self-Improvement in the Real World<br>\[[Paper](https://arxiv.org/abs/2606.19980)\] \[[Code](https://github.com/NVlabs/ENPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/enpire/)\] | arXiv 2026.06 | Agent 先写好安全边界、自动复位和二值成功判定并固定，再在真机上改 BC / RL 训练代码，8 台机器经 Git 共享 | Push-T、插销、剪扎带真机成功率 99%（8 次重试内） | NVIDIA<br>CMU |

<br>

<a id="boundary"></a>

## 6. Harness Evolution Boundary

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **RRSI**: Regularized Recursive Self-Improvement of Agent Harnesses<br>\[[Paper](https://arxiv.org/abs/2609.24972)\] \[[Code](https://github.com/google-research/rrsi)\] \[[Website](https://regularized-rsi.com)\] | arXiv 2026.09 | 每轮可改数量递减、记录失败思路；Critic 剔除泄题改动，提升须超过噪声带，多花的 token 须有收益 | JobBench、GDPval、APEX-Agents 平均：39.7 → 43.6 | Google |
