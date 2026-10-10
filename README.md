# FastHarness Survey

FastHarness 小组的会议记录与论文调研。**所有内容经人工阅读原文、核对数据后才合入 `main`**，不收录自动生成、未经审核的内容。

- 每次会议讨论了什么 → [`meetings/`](meetings/)
- 最近新增 / 修改了哪些论文 → [`CHANGELOG.md`](CHANGELOG.md)
- 单篇论文的完整问题、方法、实验结果 → 点下表 **Method** 列的「详情」
- 如何新增论文、提交审核 → [`CONTRIBUTING.md`](CONTRIBUTING.md)

## 当前主线（阶段 1）

> 来自 [第一次会议](meetings/01-第一次会议.md)

1. **LLM + VLM**：GPT 怎么外挂 VLM；Qwen 等 VLM 尽量只做选择题
2. **Code + Policy**：代码怎么调用 VLA、策略怎么组织（读到源码）；有没有 WAM
3. **Memory**（阶段 2）：从 LLM 的 memory 做法迁移

**要求**：兼容多个 LLM 和下游 policy

## 字段说明

| 字段 | 含义 |
|---|---|
| Venue | 发表会议 / 期刊；🏆 表示获奖；`arXiv` 表示尚未查到录用信息 |
| Method | **一句话核心思想**，点「详情」看完整内容 |
| Key Result | 最能说明问题的一个结果，注明仿真 / 真机 |
| Real Robot | ✅ 有真机实验并报了成功率；🎬 只有演示视频；❌ 没做 |
| Team | 第一单位 / 通讯单位及知名组 |
| Review | ✅ 已人工审核；⏳ 待审核（初稿，数据未复核） |

## 目录

- [1. LLM + VLM](#1-llm--vlm)
- [2. Code + Policy](#2-code--policy)
- [3. Memory](#3-memory)
- [4. 技能增长](#4-技能增长)
- [5. 真机迭代恢复](#5-真机迭代恢复)
- [6. Harness 迭代边界](#6-harness-迭代边界)

---

## 1. LLM + VLM

| Year | Venue | Paper Title | Repository | Method | Key Result | Real Robot | Team | Note | Review |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [Spotter: Let the Embodied Model Lead, and the VLM Reflect for It](https://arxiv.org/pdf/2609.36808) | [![GitHub stars](https://img.shields.io/github/stars/zqc3117/Spotter.svg?style=social)](https://github.com/zqc3117/Spotter) | VLA 主导执行，VLM 并行监控，确认出错才接管修复，修完交还。[详情](papers/spotter.md) | 真机 π0.5：53% → 83% | ✅ Franka | Griffith Univ.、清华交叉信息院 | 本地 Qwen 初筛 + GPT-6 Astra 复核 | ⏳ |

## 2. Code + Policy

| Year | Venue | Paper Title | Repository | Method | Key Result | Real Robot | Team | Note | Review |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | `ICML` | [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/pdf/2603.22435) | [![GitHub stars](https://img.shields.io/github/stars/capgym/cap-x.svg?style=social)](https://github.com/capgym/cap-x) | 只给低级原语 + 多轮执行反馈，Coding Agent 就能超过高层 API 单轮写代码。[详情](papers/cap-x.md) | 仿真：低级多轮 54% vs 高级单轮 39%；真机 RL：24% → 84% | ✅ Franka | NVIDIA、UC Berkeley | [website](https://capgym.github.io) | ⏳ |
| 2026 | `arXiv` | [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/pdf/2607.08448) | [![GitHub stars](https://img.shields.io/github/stars/RLinf/RPent.svg?style=social)](https://github.com/RLinf/RPent) | 冻结 VLA 只做接触动作，Agent 用固定原语 + 记忆负责定位、移动和重试。[详情](papers/harness-vla.md) | 仿真 LIBERO-Pro：82.4% vs 最强基线 43.8% | 🎬 双 Franka | 清华 | [website](https://harnessvla.github.io/) | ⏳ |
| 2026 | `arXiv` | [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/pdf/2610.01939) | [![GitHub stars](https://img.shields.io/github/stars/DAGroup-PKU/PyRUA-Lean.svg?style=social)](https://github.com/DAGroup-PKU/PyRUA-Lean) | 用 Python 代码块代替逐步工具调用，一次做完多步，只回传需要的信息。[详情](papers/pyrua-lean.md) | 仿真 700 个实例：63.1% → 71.7%，token −65% | ❌ | 北大 | PyRUA-Lean · [website](https://dagroup-pku.github.io/PyRUA-Lean/) | ⏳ |
| 2026 | `arXiv` | [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/pdf/2609.10522) | [![GitHub stars](https://img.shields.io/github/stars/showlab/Show-Harness.svg?style=social)](https://github.com/showlab/Show-Harness) | VLM 每步输出「前移 / 下降 / 抓取」等语义小动作，由解释器转成机器人运动。[详情](papers/show-harness.md) | 真机 10 个任务：89% vs π0.5 39% | ✅ Franka、AgileX | NUS Show Lab | [website](https://showlab.github.io/Show-Harness) | ⏳ |
| 2026 | `ECCV Workshop` 🏆 Best Paper | [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/pdf/2607.18060) | --- | 按能力给子任务分配 VLA / RL / TAMP，交接前用 Memory Bridge 把机器人挪到下一个策略熟悉的状态。[详情](papers/roboharness.md) | 仿真 LIBERO-LoHo：95.2% vs 64.8% | ✅ UR5e | 华为诺亚方舟 | Agent in the World Workshop | ⏳ |

## 3. Memory

待补。

## 4. 技能增长

| Year | Venue | Paper Title | Repository | Method | Key Result | Real Robot | Team | Note | Review |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/pdf/2607.00272) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ASPIRE.svg?style=social)](https://github.com/NVlabs/ASPIRE) | 按原语级 trace 定位并修补失败，验证有效的修复沉淀为技能库供后续任务复用。[详情](papers/aspire.md) | 仿真 LIBERO-Pro：18% → 72%；真机开抽屉：0 → 11/20 | ✅ YAM | NVIDIA GEAR | [website](https://research.nvidia.com/labs/gear/aspire/) | ⏳ |

## 5. 真机迭代恢复

| Year | Venue | Paper Title | Repository | Method | Key Result | Real Robot | Team | Note | Review |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/pdf/2606.19980) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ENPIRE.svg?style=social)](https://github.com/NVlabs/ENPIRE) | 先让 Agent 搭好自动复位和成功判定，再让它在真机上自己改训练代码迭代策略。[详情](papers/enpire.md) | 真机插销等任务达 99%（8 次重试内） | ✅ 8 台 YAM | NVIDIA GEAR、CMU | arXiv 备注 CoRL 2026，录用待确认 · [website](https://research.nvidia.com/labs/gear/enpire/) | ⏳ |

## 6. Harness 迭代边界

| Year | Venue | Paper Title | Repository | Method | Key Result | Real Robot | Team | Note | Review |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/pdf/2609.24972) | [![GitHub stars](https://img.shields.io/github/stars/google-research/rrsi.svg?style=social)](https://github.com/google-research/rrsi) | 在 harness 进化的「提改动」和「留改动」两端加约束，防止越改越贴合评测集。[详情](papers/rrsi.md) | 未见任务：39.7 → 43.6（非机器人基准） | ❌ 非机器人 | Google Cloud AI Research | [website](https://regularized-rsi.com) | ⏳ |
