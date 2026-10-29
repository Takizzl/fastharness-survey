<div align="center">

# FastHarness Survey


</div>

## Contents

| Category | Focus | Papers |
|:---:|:---:|:---:|
| [1. VLM1 + VLM2](#vlm) | Plugging in VLMs, failure reflection | 1 |
| [2. Code + Policy](#code-policy) | Code / orchestration driving policies | 7 |
| [3. Memory](#memory) | Memory mechanisms | 5 |
| [4. Skill Growth](#skill) | Accumulating a skill library | 1 |
| [5. Real-Robot Self-Improvement](#real-robot) | Iterating policies on real robots | 1 |
| [6. Harness Evolution](#harness-evolution) | Harness search, selection, diagnosis and constraints | 4 |
| [7. RSI Projects](#rsi-projects) | Integrated robot systems and self-improvement | 3 |
| [8. Perception Foundation Models](#perception) | Spatial grounding for action models | 1 |
| [9. RL 后训练优化](#rl-post-training) | Planner, tool use and code generation | 2 |
| [10. Sim2Real](#sim2real) | Simulation practice and physical deployment | 1 |

<br>

<a id="vlm"></a>

## 1. VLM1 + VLM2

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **Spotter**: Let the Embodied Model Lead, and the VLM Reflect for It<br>\[[Paper](https://arxiv.org/abs/2609.36808)\] \[[Code](https://github.com/zqc3117/Spotter)\] \[[Website](https://zqc3117.github.io/Spotter/)\] | arXiv 2026.09 | VLA 执行；VLM1（Qwen）给每段动作打出错风险分，出错时 VLM2（Astra）诊断、修复并验证后交还 | Franka 真机 3 个任务各 10 次：π0.5 单独 53%，加上后 83% | Griffith Univ.<br>Tsinghua |

<br>

<a id="code-policy"></a>

## 2. Code + Policy

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **CaP-X**: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation<br>\[[Paper](https://arxiv.org/abs/2603.22435)\] \[[Code](https://github.com/capgym/cap-x)\] \[[Website](https://capgym.github.io)\] | ICML 2026 | Coding Agent 只用 SAM3、IK、运动规划这些低级原语写代码，每轮读报错和画面变化描述再改 | CaP-Bench（Robosuite 7 个任务）：底层接口多轮 54%，高层接口单次 39% | NVIDIA<br>UC Berkeley |
| **Harness VLA**: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents<br>\[[Paper](https://arxiv.org/abs/2607.08448)\] \[[Code](https://github.com/RLinf/RPent)\] \[[Website](https://harnessvla.github.io/)\] | arXiv 2026.07 | 冻结的 VLA 只做抓取放置，Agent 用移动、旋转、夹爪原语摆位，没抓住就重摆再调 VLA | LIBERO-Pro 扰动测试：82.4%，单用 VLA 50.0% | Tsinghua |
| **Show-Harness**: Just a VLM Agent Can Play Robots<br>\[[Paper](https://arxiv.org/abs/2609.10522)\] \[[Code](https://github.com/showlab/Show-Harness)\] \[[Website](https://showlab.github.io/Show-Harness)\] | arXiv 2026.09 | VLM 每步输出一个语义动作（前、后、左、右、上、下、旋转、抓取、松开），换算成 2 或 4 cm 末端位移 | Franka 真机 10 个抓放任务：89%，π0.5 只有 39% | NUS |
| **RoboHarness**: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning<br>\[[Paper](https://arxiv.org/abs/2607.18060)\] \[[Code](https://github.com/markli1hoshipu/RoboHarness)\] \[[Website](https://robo-harness.com)\] | ECCV 2026 Workshop<br>**Best Paper** | Agent 按能力把子任务分给 VLA、RL、TAMP，换策略前先把机器人移到下一个策略熟悉的状态 | LIBERO-LoHo 长任务：95.2%，单用 π0.5 只有 6.4% | Huawei Noah's Ark |
| **GPT-as-Policy**: GPT 6 Astra as an Embodied Policy<br>\[[Report](https://anonymous-report-421.github.io/public-website/?view=1)\] \[[Code](https://github.com/anonymous-report-421/GPT-as-Policy)\] \[[Website](https://anonymous-report-421.github.io/public-website/?view=1)\] | 技术报告 2026 | GPT 检查 π0.5 动作与执行历史，确认失败或子目标错位后修正，恢复后交还控制。 | RoboDojo 50 例：混合 48%，Direct 26% | Galbot |
| **COAP**: Embodied Turing Machines<br>\[[Paper](https://arxiv.org/abs/2610.12369)\] \[[Website](https://etmcode-bit.github.io/)\] | arXiv 2026.10 | Agent 根据反馈改程序；测试冻结代码，用显式状态与重试执行。 | RoboDojo 42任务：成功率70.24%，均为仿真 | NTU<br>Ropedia |
| **RoboAuto**: Autonomous Robot Program Search through Multi-Level Physical Understanding<br>\[[Paper](https://arxiv.org/abs/2610.36533v1)\] \[[Website](https://roboauto-ai.github.io/)\] · [笔记](papers/roboauto.md) | arXiv 2026.10 | Agent检索物体知识、测量场景，分阶段写代码并验证，失败后修改或做诊断实验。 | RoboTwin 4任务各50次：24.5%→91.5% | Washington Univ. in St. Louis |

<br>

<a id="memory"></a>

## 3. Memory

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **JitRL**: Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates<br>\[[Paper](https://arxiv.org/abs/2601.18510)\] \[[Code](https://github.com/liushiliushi/JitRL)\] | ICML 2026 Spotlight | 检索历史回报，修正候选动作概率，不更新模型参数。 | WebArena-Lite 留出165任务：12.70%→40.88% | NUS |
| **Robota-Embed**: Unified VLA Embeddings for Robot In-Context Learning and Evolution<br>\[[Paper](https://arxiv.org/abs/2610.19495v1)\] \[[Website](https://robota-ai.github.io/robota-embed/)\] | arXiv 2026.10 | 将任务、画面和动作编码为向量，检索历史执行片段，把画面、命令和反馈交给策略复用。 | ManiSkill 5 任务×20 次：Astra 24%→68% | NVIDIA<br>MIT |
| **PhysMem**: Learning Physical Principles from Interaction: Self-Evolving Planning via Test-Time Memory<br>\[[Paper](https://arxiv.org/abs/2602.20323v1)\] \[[Code](https://github.com/haoyangli16/PhysMem)\] \[[Website](https://phys-mem.github.io/)\] | arXiv 2026.02 | 从交互中生成并验证物理假设，将可靠原则写入记忆，检索后辅助下一次规划。 | 真机推球：12 次连续交互定性展示 | UC San Diego<br>Stanford |
| **MemEvolve**: Meta-Evolution of Agent Memory Systems<br>\[[Paper](https://arxiv.org/abs/2512.18746v1)\] \[[Code](https://github.com/bingreeky/MemEvolve)\] | ICML 2026 | 内层积累执行记忆，外层根据反馈改写记忆编码、存储、检索与管理代码。 | xBench-DS 100题：Flash-Searcher 69%→74%（pass@1） | OPPO<br>NUS |
| **EmbodiedRSI**: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution<br>\[[Paper](https://arxiv.org/abs/2610.10498v1)\] \[[Website](https://geeksongs.github.io/agentic_robotics/)\] · [知识笔记](papers/embodiedrsi.md) | arXiv 2026.10 | 冻结VLA，试验演化代码与技能，用后续执行收益通过PPO训练记忆管理器。 | RoboCasa365总体：Harness VLA 63.6%→77.0% | Columbia<br>Princeton |


<br>

<a id="skill"></a>

## 4. Skill Growth

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ASPIRE**: Agentic /Skills Discovery for Robotics<br>\[[Paper](https://arxiv.org/abs/2607.00272)\] \[[Code](https://github.com/NVlabs/ASPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/aspire/)\] | arXiv 2026.06 | 记录每个原语调用的输入、输出和画面，Agent 只修出错的原语，验证有效的修复存入技能库 | LIBERO-Pro 扰动测试：72%，之前最好的 CaP-Agent0 18% | NVIDIA |

<br>

<a id="real-robot"></a>

## 5. Real-Robot Self-Improvement

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **ENPIRE**: Agentic Robot Policy Self-Improvement in the Real World<br>\[[Paper](https://arxiv.org/abs/2606.19980)\] \[[Code](https://github.com/NVlabs/ENPIRE)\] \[[Website](https://research.nvidia.com/labs/gear/enpire/)\] | CoRL 2026 | Agent 先写好自动复位和成功判定并固定，再在真机上改 BC / RL 训练代码，8 台机器经 Git 共享 | YAM 双臂真机插销、推 T、剪扎带：99%（允许重试 8 次） | NVIDIA<br>CMU |

<br>

<a id="harness-evolution"></a>

## 6. Harness Evolution

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **RRSI**: Regularized Recursive Self-Improvement of Agent Harnesses<br>\[[Paper](https://arxiv.org/abs/2609.24972)\] \[[Code](https://github.com/google-research/rrsi)\] \[[Website](https://regularized-rsi.com)\] | arXiv 2026.09 | 每轮能改的地方逐轮减少；只保留不含测试题答案、提升超过随机波动、多花的 token 有回报的改动 | JobBench、GDPval、APEX-Agents 平均：原始 harness 39.7 → 43.6 | Google |
| **GEAR**: An Open General Evolutionary Architecture for Recursive Self-Improvement of LLM Agent Harness<br>\[[Report](https://rsi-gear.github.io/)\] \[[Code](https://github.com/rsi-gear/gear)\] \[[Website](https://rsi-gear.github.io/)\] | 项目预印本 2026.10 | Meta-Agent 按模块化搜索策略生成、评测并迭代 Harness | Marketing 100共享任务：Luna 27%→40% | Imperial College London<br>Duke University |
| **RSIFlow**: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent<br>\[[Paper](https://arxiv.org/abs/2610.21791)\] \[[Code](https://github.com/1HUAN1/RSI-Flow)\] | arXiv 2026.10 | Task-Agent 执行任务，Meta-Agent 据反馈改进 Task 系统和自身 Harness，形成协同演化 | 六基准留出评测：4B平均SIA 45.15→51.21 | Beihang University<br>Tsinghua University |
| **BiPA**: Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution<br>\[[Paper](https://arxiv.org/abs/2610.37201)\] \[[Code](https://github.com/valleysprings/BiPA)\] | arXiv 2026.10 | 回放候选选择检验收益可信度，用轮次与上下文二部图分解 Skill 更新的执行成本 | 三基准16技能：成功率+0.1pp，输入token×1.16 | Shanghai AI Laboratory<br>Fudan University |

<br>

<a id="rsi-projects"></a>

## 7. RSI Projects

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **LoopROS / LoopMaster**: A Recursively Self-Evolving Robot Operating System for Agentic Manipulation<br>\[[Report](https://loopmaster.ai/loopros/)\] \[[Code](https://github.com/Boxjod/LoopROS_Client)\] \[[Website](https://loopmaster.ai/)\] | 技术报告 2026.10 | Agent 读示范与场景，在线规划并执行；把动作反馈组织为任务 Skills，供后续检索复用。 | 自报 RoboDojo 10 任务 100 例：SR 82%，Score 88.90 | LoopMaster |
| **PhysicalRSI**: Physical RSI 1.0: Recursive Self-Harness for Scaling Embodied Skills<br>\[[Code](https://github.com/PhysicalRSI/PhysicalRSI)\] \[[Website](https://mmlab.hk/research/PhysicalRSI)\] | Preview 2026 | Agent 根据执行反馈改写 harness，评测候选并保留更优版本，继承代码技能与任务记忆。 | RoboDojo 官网快照：Score 36.27，SR 31.38% | HKU MMLab<br>KAI |
| **RAX**: Scaling Online Exploration for Robot Agents<br>\[[Paper](https://arxiv.org/abs/2610.22496v1)\] \[[Code](https://github.com/robot-agent-exploration/rax)\] \[[Website](https://robot-agent-exploration.com/)\] | arXiv 2026.10 | Coding Agent 自主探索，合成感知、规划与控制程序，保存经验并复用已验证技能 | RoboDojo 7任务：Score 24.9%→78.3% | Harvard<br>NVIDIA |


<a id="perception"></a>

## 8. Perception Foundation Models

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **GroundingPI**: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives<br>\[[Paper](https://arxiv.org/abs/2609.39601)\] \[[Code](https://github.com/groundingpi/GroundingPI)\] \[[Website](https://groundingpi.github.io/)\] | arXiv 2026.09 | 用定位监督训练视觉语言底座，将中间特征接入动作模型，支持精确感知与控制。 | COCO：每框输出 7.6 tokens | XPeng、PKU、HKU |

<br>

<a id="rl-post-training"></a>

## 9. RL 后训练优化

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **PyRUA-Lean Coder**: Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens<br>\[[Paper](https://arxiv.org/abs/2610.01939)\] \[[Code](https://github.com/DAGroup-PKU/PyRUA-Lean)\] \[[Website](https://dagroup-pku.github.io/PyRUA-Lean/)\] | arXiv 2026.10 | 冻结原语与 VLA，用成败奖励做 GRPO，训练 4B Planner 组合代码、检查与重试 | LIBERO、RoboTwin、RC365 未见655例：18.8%→44.1% | PKU<br>NUS |
| **AgenticRoboRL**: Bringing Coding-Agent Post-Training to Agentic Robotics<br>\[[Paper](https://arxiv.org/abs/2610.28589)\] \[[Code](https://github.com/xinxinliu-ai/AgenticRoboRL)\] \[[Website](https://xinxinliu-ai.github.io/AgenticRoboRL/)\] | arXiv 2026.10 | 成功示范 SFT 后，用多轮 RL 训练 9B Planner 调用 VLA 或生成控制代码 | RPent / LIBERO-PRO：18.1%→65.1%→71.0% | UCF<br>USC |

<br>

<a id="sim2real"></a>

## 10. Sim2Real

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Venue&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Method&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;Team&nbsp;&nbsp;&nbsp; |
|:---:|:---:|:---:|:---:|:---:|
| **RPG**: Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents<br>\[[Paper](https://arxiv.org/abs/2610.02204v1)\] \[[Website](https://rpg-robot.github.io/)\] | arXiv 2026.10 | 从离线数据构造仿真练习，用执行与视频诊断迭代技能和提示词，验证后部署真机 | MuJoCo/YAM 22任务：28.6%→95.0% | UC Berkeley<br>Amazon FAR |
