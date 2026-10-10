<div align="center">

# FastHarness Survey

![Papers](https://img.shields.io/badge/Papers-9-blue?style=flat-square)
![Meetings](https://img.shields.io/badge/Meetings-1-orange?style=flat-square)
![Updated](https://img.shields.io/badge/Updated-2026.10.10-green?style=flat-square)

</div>

## Current Focus · [Meeting 01](meetings/01-第一次会议.md)

1. How GPT is combined with VLMs: how to plug in a VLM; Qwen-style VLMs should mainly answer multiple-choice questions
2. How code is combined with VLAs: how policies are organized (down to the source code); whether WAMs are used
3. Stage 2 (Haoran): how to build memory, transferring ideas from LLM agents

**Requirement:** compatible with multiple LLMs and downstream policies

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

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [Spotter:&nbsp;Let&nbsp;the&nbsp;Embodied&nbsp;Model<br>Lead,&nbsp;and&nbsp;the&nbsp;VLM&nbsp;Reflect&nbsp;for&nbsp;It](https://arxiv.org/pdf/2609.36808) | [![GitHub stars](https://img.shields.io/github/stars/zqc3117/Spotter.svg?style=social)](https://github.com/zqc3117/Spotter) | VLA leads execution; a VLM monitors in parallel and takes over only to repair errors | Real robot 53% → 83% | Griffith / Tsinghua | --- |

<a id="code-policy"></a>

## 2. Code + Policy

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `ICML` | [CaP-X:&nbsp;A&nbsp;Framework&nbsp;for&nbsp;Benchmarking&nbsp;and<br>Improving&nbsp;Coding&nbsp;Agents&nbsp;for&nbsp;Robot&nbsp;Manipulation](https://arxiv.org/pdf/2603.22435) | [![GitHub stars](https://img.shields.io/github/stars/capgym/cap-x.svg?style=social)](https://github.com/capgym/cap-x) | Coding agents write code over low-level primitives with multi-turn execution feedback | Real robot 24% → 84% | NVIDIA / Berkeley | [website](https://capgym.github.io) |
| 2026 | `arXiv` | [Harness&nbsp;VLA:&nbsp;Steering&nbsp;Frozen&nbsp;VLAs&nbsp;into&nbsp;Reliable<br>Manipulation&nbsp;Primitives&nbsp;via&nbsp;Memory-Guided&nbsp;Agents](https://arxiv.org/pdf/2607.08448) | [![GitHub stars](https://img.shields.io/github/stars/RLinf/RPent.svg?style=social)](https://github.com/RLinf/RPent) | A frozen VLA handles only contact-rich steps; the agent handles the rest | LIBERO-Pro 82.4% | Tsinghua | [website](https://harnessvla.github.io/) |
| 2026 | `arXiv` | [Fewer&nbsp;Tokens,&nbsp;Better&nbsp;Action:&nbsp;GPT-6&nbsp;Astra&nbsp;Robot&nbsp;Agents<br>with&nbsp;14%&nbsp;Higher&nbsp;Success&nbsp;Rate&nbsp;but&nbsp;65%&nbsp;Fewer&nbsp;Tokens](https://arxiv.org/pdf/2610.01939) | [![GitHub stars](https://img.shields.io/github/stars/DAGroup-PKU/PyRUA-Lean.svg?style=social)](https://github.com/DAGroup-PKU/PyRUA-Lean) | Python code cells replace step-by-step tool calls | Success +8.6 pts, tokens −65% | PKU | [website](https://dagroup-pku.github.io/PyRUA-Lean/) |
| 2026 | `arXiv` | [Show-Harness:&nbsp;Just&nbsp;a&nbsp;VLM<br>Agent&nbsp;Can&nbsp;Play&nbsp;Robots](https://arxiv.org/pdf/2609.10522) | [![GitHub stars](https://img.shields.io/github/stars/showlab/Show-Harness.svg?style=social)](https://github.com/showlab/Show-Harness) | The VLM outputs one small semantic action per step to drive the robot | Real robot 89% vs π0.5 39% | NUS | [website](https://showlab.github.io/Show-Harness) |
| 2026 | `ECCV Workshop`<br>Best Paper | [RoboHarness:&nbsp;Memory-Driven&nbsp;Orchestration&nbsp;of<br>Heterogeneous&nbsp;Robot&nbsp;Policies&nbsp;for&nbsp;Long-Horizon&nbsp;Planning](https://arxiv.org/pdf/2607.18060) | --- | Routes subtasks to heterogeneous policies by capability and aligns states before handoff | LIBERO-LoHo 95.2% | Huawei Noah's Ark | --- |

<a id="memory"></a>

## 3. Memory

TBD.

<a id="skill"></a>

## 4. Skill Growth

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [ASPIRE:&nbsp;Agentic&nbsp;/Skills<br>Discovery&nbsp;for&nbsp;Robotics](https://arxiv.org/pdf/2607.00272) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ASPIRE.svg?style=social)](https://github.com/NVlabs/ASPIRE) | Repairs failures from per-call traces and distills fixes into a skill library | LIBERO-Pro 18% → 72% | NVIDIA | [website](https://research.nvidia.com/labs/gear/aspire/) |

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [ENPIRE:&nbsp;Agentic&nbsp;Robot&nbsp;Policy<br>Self-Improvement&nbsp;in&nbsp;the&nbsp;Real&nbsp;World](https://arxiv.org/pdf/2606.19980) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ENPIRE.svg?style=social)](https://github.com/NVlabs/ENPIRE) | The agent builds auto-reset and success checks, then edits training code on real robots | Real robot 99% | NVIDIA / CMU | [website](https://research.nvidia.com/labs/gear/enpire/) |

<a id="boundary"></a>

## 6. Harness Evolution Boundary

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [RRSI:&nbsp;Regularized&nbsp;Recursive<br>Self-Improvement&nbsp;of&nbsp;Agent&nbsp;Harnesses](https://arxiv.org/pdf/2609.24972) | [![GitHub stars](https://img.shields.io/github/stars/google-research/rrsi.svg?style=social)](https://github.com/google-research/rrsi) | Regularizes how harness edits are proposed and kept, to avoid overfitting the eval set | Unseen tasks 39.7 → 43.6 | Google | [website](https://regularized-rsi.com) |
