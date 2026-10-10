<div align="center">

# FastHarness Survey

![Papers](https://img.shields.io/badge/Papers-9-blue?style=flat-square)
![Meetings](https://img.shields.io/badge/Meetings-1-orange?style=flat-square)
![Updated](https://img.shields.io/badge/Updated-2026.10.10-green?style=flat-square)

</div>

## 当前主线 · [第一次会议](meetings/01-第一次会议.md)

1. 调研 GPT + VLM 的结合方式相关方法，怎么外挂 VLM，Qwen 等 VLM 尽量做选择题
2. 调研 Code + VLA 怎么结合起来的，策略如何组织（定位到源码分析）（有没有 WAM）
3. 浩然可能考虑阶段 2 的事，专注 Memory 怎么去做，从 LLM 的角度迁移

**要求：** 需要兼容多个 LLM 和下游 policy

## Contents

[1. VLM1 + VLM2](#vlm) (1) · [2. Code + Policy](#code-policy) (5) · [3. Memory](#memory) (0) · [4. Skill Growth](#skill) (1) · [5. Real-Robot Self-Improvement](#real-robot) (1) · [6. Harness Evolution Boundary](#boundary) (1)

<a id="vlm"></a>

## 1. VLM1 + VLM2

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="250" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="250" height="1"> | Result<br><img src="assets/spacer.png" width="130" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Links<br><img src="assets/spacer.png" width="115" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Spotter** | Let the Embodied Model Lead, and the VLM Reflect for It | arXiv 2026.09 | VLA leads execution; a VLM monitors in parallel and takes over only to repair errors | Real robot 53% → 83% | Griffith / Tsinghua | [Paper](https://arxiv.org/abs/2609.36808) · [Code](https://github.com/zqc3117/Spotter) |

<a id="code-policy"></a>

## 2. Code + Policy

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="250" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="250" height="1"> | Result<br><img src="assets/spacer.png" width="130" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Links<br><img src="assets/spacer.png" width="115" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CaP-X** | A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation | ICML 2026 | Coding agents write code over low-level primitives with multi-turn execution feedback | Real robot 24% → 84% | NVIDIA / Berkeley | [Paper](https://arxiv.org/abs/2603.22435) · [Code](https://github.com/capgym/cap-x) · [Website](https://capgym.github.io) |
| **Harness VLA** | Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents | arXiv 2026.07 | A frozen VLA handles only contact-rich steps; the agent handles the rest | LIBERO-Pro 82.4% vs 43.8% | Tsinghua | [Paper](https://arxiv.org/abs/2607.08448) · [Code](https://github.com/RLinf/RPent) · [Website](https://harnessvla.github.io/) |
| **PyRUA-Lean** | Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens | arXiv 2026.10 | Python code cells replace step-by-step tool calls | Success +8.6 pts, tokens −65% | PKU | [Paper](https://arxiv.org/abs/2610.01939) · [Code](https://github.com/DAGroup-PKU/PyRUA-Lean) · [Website](https://dagroup-pku.github.io/PyRUA-Lean/) |
| **Show-Harness** | Just a VLM Agent Can Play Robots | arXiv 2026.09 | The VLM outputs one small semantic action per step to drive the robot | Real robot 89% vs π0.5 39% | NUS | [Paper](https://arxiv.org/abs/2609.10522) · [Code](https://github.com/showlab/Show-Harness) · [Website](https://showlab.github.io/Show-Harness) |
| **RoboHarness** | Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning | ECCV 2026 Workshop<br>**Best Paper** | Routes subtasks to heterogeneous policies by capability and aligns states before handoff | LIBERO-LoHo 95.2% vs 64.8% | Huawei Noah's Ark | [Paper](https://arxiv.org/abs/2607.18060) |

<a id="memory"></a>

## 3. Memory

TBD.

<a id="skill"></a>

## 4. Skill Growth

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="250" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="250" height="1"> | Result<br><img src="assets/spacer.png" width="130" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Links<br><img src="assets/spacer.png" width="115" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **ASPIRE** | Agentic /Skills Discovery for Robotics | arXiv 2026.07 | Repairs failures from per-call traces and distills fixes into a skill library | LIBERO-Pro 18% → 72% | NVIDIA | [Paper](https://arxiv.org/abs/2607.00272) · [Code](https://github.com/NVlabs/ASPIRE) · [Website](https://research.nvidia.com/labs/gear/aspire/) |

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="250" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="250" height="1"> | Result<br><img src="assets/spacer.png" width="130" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Links<br><img src="assets/spacer.png" width="115" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **ENPIRE** | Agentic Robot Policy Self-Improvement in the Real World | arXiv 2026.06 | The agent builds auto-reset and success checks, then edits training code on real robots | Real robot 99% | NVIDIA / CMU | [Paper](https://arxiv.org/abs/2606.19980) · [Code](https://github.com/NVlabs/ENPIRE) · [Website](https://research.nvidia.com/labs/gear/enpire/) |

<a id="boundary"></a>

## 6. Harness Evolution Boundary

| Name<br><img src="assets/spacer.png" width="90" height="1"> | Paper<br><img src="assets/spacer.png" width="250" height="1"> | Venue<br><img src="assets/spacer.png" width="95" height="1"> | Method<br><img src="assets/spacer.png" width="250" height="1"> | Result<br><img src="assets/spacer.png" width="130" height="1"> | Team<br><img src="assets/spacer.png" width="100" height="1"> | Links<br><img src="assets/spacer.png" width="115" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **RRSI** | Regularized Recursive Self-Improvement of Agent Harnesses | arXiv 2026.09 | Regularizes how harness edits are proposed and kept, to avoid overfitting the eval set | Unseen tasks 39.7 → 43.6 | Google | [Paper](https://arxiv.org/abs/2609.24972) · [Code](https://github.com/google-research/rrsi) · [Website](https://regularized-rsi.com) |
