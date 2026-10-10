# FastHarness Survey

## 1. LLM + VLM

| Year | Venue | Paper Title | Repository | Method | Result | Team | Website |
|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [Spotter:&nbsp;Let&nbsp;the&nbsp;Embodied&nbsp;Model&nbsp;Lead,&nbsp;and&nbsp;the&nbsp;VLM&nbsp;Reflect&nbsp;for&nbsp;It](https://arxiv.org/pdf/2609.36808) | [![GitHub stars](https://img.shields.io/github/stars/zqc3117/Spotter.svg?style=social)](https://github.com/zqc3117/Spotter) | VLA 主导执行，VLM 监控出错后接管修复 | 真机&nbsp;53%&nbsp;→&nbsp;83% | Griffith&nbsp;/&nbsp;清华 | --- |

## 2. Code + Policy

| Year | Venue | Paper Title | Repository | Method | Result | Team | Website |
|---|---|---|---|---|---|---|---|
| 2026 | `ICML` | [CaP-X:&nbsp;A&nbsp;Framework&nbsp;for&nbsp;Benchmarking&nbsp;and&nbsp;Improving&nbsp;Coding&nbsp;Agents&nbsp;for&nbsp;Robot&nbsp;Manipulation](https://arxiv.org/pdf/2603.22435) | [![GitHub stars](https://img.shields.io/github/stars/capgym/cap-x.svg?style=social)](https://github.com/capgym/cap-x) | 低级原语 + 多轮反馈写代码控制机器人 | 真机&nbsp;24%&nbsp;→&nbsp;84% | NVIDIA&nbsp;/&nbsp;Berkeley | [website](https://capgym.github.io) |
| 2026 | `arXiv` | [Harness&nbsp;VLA:&nbsp;Steering&nbsp;Frozen&nbsp;VLAs&nbsp;into&nbsp;Reliable&nbsp;Manipulation&nbsp;Primitives&nbsp;via&nbsp;Memory-Guided&nbsp;Agents](https://arxiv.org/pdf/2607.08448) | [![GitHub stars](https://img.shields.io/github/stars/RLinf/RPent.svg?style=social)](https://github.com/RLinf/RPent) | 冻结 VLA 只做接触动作，其余交给 Agent | LIBERO-Pro&nbsp;82.4% | 清华 | [website](https://harnessvla.github.io/) |
| 2026 | `arXiv` | [Fewer&nbsp;Tokens,&nbsp;Better&nbsp;Action:&nbsp;GPT-6&nbsp;Astra&nbsp;Robot&nbsp;Agents&nbsp;with&nbsp;14%&nbsp;Higher&nbsp;Success&nbsp;Rate&nbsp;but&nbsp;65%&nbsp;Fewer&nbsp;Tokens](https://arxiv.org/pdf/2610.01939) | [![GitHub stars](https://img.shields.io/github/stars/DAGroup-PKU/PyRUA-Lean.svg?style=social)](https://github.com/DAGroup-PKU/PyRUA-Lean) | 用 Python 代码块代替逐步工具调用 | 成功率&nbsp;+8.6，token&nbsp;−65% | 北大 | [website](https://dagroup-pku.github.io/PyRUA-Lean/) |
| 2026 | `arXiv` | [Show-Harness:&nbsp;Just&nbsp;a&nbsp;VLM&nbsp;Agent&nbsp;Can&nbsp;Play&nbsp;Robots](https://arxiv.org/pdf/2609.10522) | [![GitHub stars](https://img.shields.io/github/stars/showlab/Show-Harness.svg?style=social)](https://github.com/showlab/Show-Harness) | VLM 每步输出语义小动作控制机器人 | 真机&nbsp;89%&nbsp;vs&nbsp;π0.5&nbsp;39% | NUS | [website](https://showlab.github.io/Show-Harness) |
| 2026 | `ECCV&nbsp;Workshop`&nbsp;🏆&nbsp;Best&nbsp;Paper | [RoboHarness:&nbsp;Memory-Driven&nbsp;Orchestration&nbsp;of&nbsp;Heterogeneous&nbsp;Robot&nbsp;Policies&nbsp;for&nbsp;Long-Horizon&nbsp;Planning](https://arxiv.org/pdf/2607.18060) | --- | 按能力调度多种策略，交接前对齐状态 | LIBERO-LoHo&nbsp;95.2% | 华为诺亚 | --- |

## 3. Memory

待补。

## 4. 技能增长

| Year | Venue | Paper Title | Repository | Method | Result | Team | Website |
|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [ASPIRE:&nbsp;Agentic&nbsp;/Skills&nbsp;Discovery&nbsp;for&nbsp;Robotics](https://arxiv.org/pdf/2607.00272) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ASPIRE.svg?style=social)](https://github.com/NVlabs/ASPIRE) | 按调用记录修补失败，沉淀为技能库 | LIBERO-Pro&nbsp;18%&nbsp;→&nbsp;72% | NVIDIA | [website](https://research.nvidia.com/labs/gear/aspire/) |

## 5. 真机迭代恢复

| Year | Venue | Paper Title | Repository | Method | Result | Team | Website |
|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [ENPIRE:&nbsp;Agentic&nbsp;Robot&nbsp;Policy&nbsp;Self-Improvement&nbsp;in&nbsp;the&nbsp;Real&nbsp;World](https://arxiv.org/pdf/2606.19980) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ENPIRE.svg?style=social)](https://github.com/NVlabs/ENPIRE) | 自动复位与判成败，Agent 在真机上自己改训练代码 | 真机&nbsp;99% | NVIDIA&nbsp;/&nbsp;CMU | [website](https://research.nvidia.com/labs/gear/enpire/) |

## 6. Harness 迭代边界

| Year | Venue | Paper Title | Repository | Method | Result | Team | Website |
|---|---|---|---|---|---|---|---|
| 2026 | `arXiv` | [RRSI:&nbsp;Regularized&nbsp;Recursive&nbsp;Self-Improvement&nbsp;of&nbsp;Agent&nbsp;Harnesses](https://arxiv.org/pdf/2609.24972) | [![GitHub stars](https://img.shields.io/github/stars/google-research/rrsi.svg?style=social)](https://github.com/google-research/rrsi) | 约束改动的提出与保留，防止过拟合评测集 | 未见任务&nbsp;39.7&nbsp;→&nbsp;43.6 | Google | [website](https://regularized-rsi.com) |
