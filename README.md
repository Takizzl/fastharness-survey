# FastHarness Survey

## 当前主线

> 更新于 [第一次会议](meetings/01-第一次会议.md)

1. 调研 GPT + VLM 的结合方式：怎么外挂 VLM，Qwen 等 VLM 尽量做选择题
2. 调研 Code + VLA 的结合方式：策略如何组织（读到源码），有没有 WAM
3. 浩然考虑阶段 2：Memory 怎么做，从 LLM 的角度迁移

要求：兼容多个 LLM 和下游 policy

## 1. VLM1 + VLM2

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [Spotter:&nbsp;Let&nbsp;the&nbsp;Embodied&nbsp;Model<br>Lead,&nbsp;and&nbsp;the&nbsp;VLM&nbsp;Reflect&nbsp;for&nbsp;It](https://arxiv.org/pdf/2609.36808) | [![GitHub stars](https://img.shields.io/github/stars/zqc3117/Spotter.svg?style=social)](https://github.com/zqc3117/Spotter) | VLA 主导执行，VLM 监控出错后接管修复 | 真机 53% → 83% | Griffith / 清华 | --- |

## 2. Code + Policy

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `ICML` | [CaP-X:&nbsp;A&nbsp;Framework&nbsp;for&nbsp;Benchmarking&nbsp;and<br>Improving&nbsp;Coding&nbsp;Agents&nbsp;for&nbsp;Robot&nbsp;Manipulation](https://arxiv.org/pdf/2603.22435) | [![GitHub stars](https://img.shields.io/github/stars/capgym/cap-x.svg?style=social)](https://github.com/capgym/cap-x) | 低级原语 + 多轮反馈写代码控制机器人 | 真机 24% → 84% | NVIDIA / Berkeley | [website](https://capgym.github.io) |
| 2026 | `arXiv` | [Harness&nbsp;VLA:&nbsp;Steering&nbsp;Frozen&nbsp;VLAs&nbsp;into&nbsp;Reliable<br>Manipulation&nbsp;Primitives&nbsp;via&nbsp;Memory-Guided&nbsp;Agents](https://arxiv.org/pdf/2607.08448) | [![GitHub stars](https://img.shields.io/github/stars/RLinf/RPent.svg?style=social)](https://github.com/RLinf/RPent) | 冻结 VLA 只做接触动作，其余交给 Agent | LIBERO-Pro 82.4% | 清华 | [website](https://harnessvla.github.io/) |
| 2026 | `arXiv` | [Fewer&nbsp;Tokens,&nbsp;Better&nbsp;Action:&nbsp;GPT-6&nbsp;Astra&nbsp;Robot&nbsp;Agents<br>with&nbsp;14%&nbsp;Higher&nbsp;Success&nbsp;Rate&nbsp;but&nbsp;65%&nbsp;Fewer&nbsp;Tokens](https://arxiv.org/pdf/2610.01939) | [![GitHub stars](https://img.shields.io/github/stars/DAGroup-PKU/PyRUA-Lean.svg?style=social)](https://github.com/DAGroup-PKU/PyRUA-Lean) | 用 Python 代码块代替逐步工具调用 | 成功率 +8.6，token −65% | 北大 | [website](https://dagroup-pku.github.io/PyRUA-Lean/) |
| 2026 | `arXiv` | [Show-Harness:&nbsp;Just&nbsp;a&nbsp;VLM<br>Agent&nbsp;Can&nbsp;Play&nbsp;Robots](https://arxiv.org/pdf/2609.10522) | [![GitHub stars](https://img.shields.io/github/stars/showlab/Show-Harness.svg?style=social)](https://github.com/showlab/Show-Harness) | VLM 每步输出语义小动作控制机器人 | 真机 89% vs π0.5 39% | NUS | [website](https://showlab.github.io/Show-Harness) |
| 2026 | `ECCV Workshop`<br>🏆 Best Paper | [RoboHarness:&nbsp;Memory-Driven&nbsp;Orchestration&nbsp;of<br>Heterogeneous&nbsp;Robot&nbsp;Policies&nbsp;for&nbsp;Long-Horizon&nbsp;Planning](https://arxiv.org/pdf/2607.18060) | --- | 按能力调度多种策略，交接前对齐状态 | LIBERO-LoHo 95.2% | 华为诺亚 | --- |

## 3. Memory

待补。

## 4. 技能增长

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [ASPIRE:&nbsp;Agentic&nbsp;/Skills<br>Discovery&nbsp;for&nbsp;Robotics](https://arxiv.org/pdf/2607.00272) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ASPIRE.svg?style=social)](https://github.com/NVlabs/ASPIRE) | 按调用记录修补失败，沉淀为技能库 | LIBERO-Pro 18% → 72% | NVIDIA | [website](https://research.nvidia.com/labs/gear/aspire/) |

## 5. 真机迭代恢复

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [ENPIRE:&nbsp;Agentic&nbsp;Robot&nbsp;Policy<br>Self-Improvement&nbsp;in&nbsp;the&nbsp;Real&nbsp;World](https://arxiv.org/pdf/2606.19980) | [![GitHub stars](https://img.shields.io/github/stars/NVlabs/ENPIRE.svg?style=social)](https://github.com/NVlabs/ENPIRE) | 自动复位与判成败，Agent 在真机上自己改训练代码 | 真机 99% | NVIDIA / CMU | [website](https://research.nvidia.com/labs/gear/enpire/) |

## 6. Harness 迭代边界

| Year<br><img src="assets/spacer.png" width="50" height="1"> | Venue<br><img src="assets/spacer.png" width="130" height="1"> | Paper Title<br><img src="assets/spacer.png" width="440" height="1"> | Repository<br><img src="assets/spacer.png" width="110" height="1"> | Method<br><img src="assets/spacer.png" width="230" height="1"> | Result<br><img src="assets/spacer.png" width="160" height="1"> | Team<br><img src="assets/spacer.png" width="120" height="1"> | Website<br><img src="assets/spacer.png" width="70" height="1"> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2026 | `arXiv` | [RRSI:&nbsp;Regularized&nbsp;Recursive<br>Self-Improvement&nbsp;of&nbsp;Agent&nbsp;Harnesses](https://arxiv.org/pdf/2609.24972) | [![GitHub stars](https://img.shields.io/github/stars/google-research/rrsi.svg?style=social)](https://github.com/google-research/rrsi) | 约束改动的提出与保留，防止过拟合评测集 | 未见任务 39.7 → 43.6 | Google | [website](https://regularized-rsi.com) |
