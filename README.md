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

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **Spotter** (arXiv 2026.09): Let the Embodied Model Lead, and the VLM Reflect for It<br>\[[Paper](https://arxiv.org/abs/2609.36808)\] \[[Code](https://github.com/zqc3117/Spotter)\] \[[Website](https://zqc3117.github.io/Spotter/)\] | VLA 策略执行，恢复能力较差 | VLA 执行；VLM1（Qwen）给每段动作打出错风险分，出错时 VLM2（Astra）诊断、修复并验证后交还 | Franka 真机 3 个任务各 10 次：π0.5 单独 53%，加上后 83% | Griffith Univ.<br>Tsinghua |

<br>

<a id="code-policy"></a>

## 2. Code + Policy

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **CaP-X** (ICML 2026): A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation<br>\[[Paper](https://arxiv.org/abs/2603.22435)\] \[[Code](https://github.com/capgym/cap-x)\] \[[Website](https://capgym.github.io)\] | Code-as-Policy 依赖人写的高层 API，看不出模型本身能力 | Coding Agent 只用 SAM3、IK、运动规划这些低级原语写代码，每轮读报错和画面变化描述再改 | CaP-Bench（Robosuite 7 个任务）：底层接口多轮 54%，高层接口单次 39% | NVIDIA<br>UC Berkeley |
| **Harness VLA** (arXiv 2026.07): Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents<br>\[[Paper](https://arxiv.org/abs/2607.08448)\] \[[Code](https://github.com/RLinf/RPent)\] \[[Website](https://harnessvla.github.io/)\] | VLA 泛化差，换目标、换位置就失败 | 冻结的 VLA 只做抓取放置，Agent 用移动、旋转、夹爪原语摆位，没抓住就重摆再调 VLA | LIBERO-Pro 扰动测试：82.4%，单用 VLA 50.0% | Tsinghua |
| **PyRUA-Lean** (arXiv 2026.10): Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens<br>\[[Paper](https://arxiv.org/abs/2610.01939)\] \[[Code](https://github.com/DAGroup-PKU/PyRUA-Lean)\] \[[Website](https://dagroup-pku.github.io/PyRUA-Lean/)\] | Tool Calling 每步调一次 VLM，token 开销大 | VLM 写一段 Python 串起原语和 VLA，在代码里判断、重试，只回传请求的图像 | LIBERO-Pro、RoboTwin 2.0、RoboCasa365：工具调用版 63.1% → 71.7% | PKU |
| **Show-Harness** (arXiv 2026.09): Just a VLM Agent Can Play Robots<br>\[[Paper](https://arxiv.org/abs/2609.10522)\] \[[Code](https://github.com/showlab/Show-Harness)\] \[[Website](https://showlab.github.io/Show-Harness)\] | VLM 难以直接控制细粒度动作 | VLM 每步输出一个语义动作（前、后、左、右、上、下、旋转、抓取、松开），换算成 2 或 4 cm 末端位移 | Franka 真机 10 个抓放任务：89%，π0.5 只有 39% | NUS |
| **RoboHarness** (ECCV 2026 Workshop, Best Paper): Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning<br>\[[Paper](https://arxiv.org/abs/2607.18060)\] \[[Code](https://github.com/markli1hoshipu/RoboHarness)\] \[[Website](https://robo-harness.com)\] | 长任务单一策略做不完，多策略接力时交接容易断 | Agent 按能力把子任务分给 VLA、RL、TAMP，换策略前先把机器人移到下一个策略熟悉的状态 | LIBERO-LoHo 长任务：95.2%，单用 π0.5 只有 6.4% | Huawei Noah's Ark |

<br>

<a id="memory"></a>

## 3. Memory

TBD.

<br>

<a id="skill"></a>

## 4. Skill Growth

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ASPIRE** (arXiv 2026.06): Agentic /Skills Discovery for Robotics<br>\[[Paper](https://arxiv.org/abs/2607.00272)\] \[[Code](https://github.com/NVlabs/ASPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/aspire/)\] | 程序失败后难定位原因，修复经验无法跨任务积累 | 记录每个原语调用的输入、输出和画面，Agent 只修出错的原语，验证有效的修复存入技能库 | LIBERO-Pro 扰动测试：72%，之前最好的 CaP-Agent0 18% | NVIDIA |

<br>

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ENPIRE** (CoRL 2026): Agentic Robot Policy Self-Improvement in the Real World<br>\[[Paper](https://arxiv.org/abs/2606.19980)\] \[[Code](https://github.com/NVlabs/ENPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/enpire/)\] | 真机策略训练依赖人做复位、判成败和调参 | Agent 先写好自动复位和成功判定并固定，再在真机上改 BC / RL 训练代码，8 台机器经 Git 共享 | YAM 双臂真机插销、推 T、剪扎带：99%（允许重试 8 次） | NVIDIA<br>CMU |

<br>

<a id="boundary"></a>

## 6. Harness Evolution Boundary

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Problem&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **RRSI** (arXiv 2026.09): Regularized Recursive Self-Improvement of Agent Harnesses<br>\[[Paper](https://arxiv.org/abs/2609.24972)\] \[[Code](https://github.com/google-research/rrsi)\] \[[Website](https://regularized-rsi.com)\] | Harness 自进化用同一批题提改动、选改动，出现自适应过拟合 | 每轮能改的地方逐轮减少；只保留不含测试题答案、提升超过随机波动、多花的 token 有回报的改动 | JobBench、GDPval、APEX-Agents 平均：原始 harness 39.7 → 43.6 | Google |
