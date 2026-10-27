# PyRUA-Lean Coder：直接用 GRPO 训练高层代码规划器

| 项目 | 内容 |
|---|---|
| 论文全名 | Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens |
| 模块 | 9. RL 后训练优化 |
| Year / Venue | arXiv 2026.10；本文依据 v2（2026-10-13） |
| Paper | https://arxiv.org/abs/2610.01939 |
| Code | https://github.com/DAGroup-PKU/PyRUA-Lean |
| Website | https://dagroup-pku.github.io/PyRUA-Lean/ |
| Team | 北京大学、NUS、NVIDIA、Impossible Research |

## 问题

逐步工具调用反复读取历史与图像，成本高；已有原语不变时，能否用代码组合减少调用，并通过环境交互训练小模型的规划与接口使用能力？

## 一句话：解决方案

在冻结的机器人原语与 VLA 上，让 Qwen3.5-4B 自行生成和执行 Python 代码，用完整任务的成败奖励做 GRPO，提升高层接口使用能力。

## 方法：系统框架

PyRUA-Lean 把原语和 VLA 封装为 Python 对象 `robo`。VLM 每次生成代码 cell，在 cell 内组合运动、感知、夹爪与 VLA，做条件判断和本地重试；变量与函数在同一 episode 中保留，只回传打印信息和主动请求的图像。**PyRUA-Lean Coder 是基于这套接口做 GRPO 后训练的 Qwen3.5-4B。**

| 环节 | 实际信息流 |
|---|---|
| 初始输入 | API 说明、操作指南、任务指令、初始机器人状态、第一组相机图像 |
| Planner 输出 | 推理与 `python(code)`；一个 cell 可以调用多个原语 |
| 环境执行 | Python 运行时调用冻结原语 / VLA，执行检查与重试 |
| 后续输入 | 工具文本结果，以及代码主动请求的图像；不自动逐原语回图 |
| 继续规划 | 读取反馈后再生成 cell，直到任务结束或达到预算 |
| 学习信号 | 完整 episode 最终成功 1、失败 0，之后批量更新 Planner |

“需要新图像才能判断下一步”仍需请求并读取新图像，程序不会替代视觉判断。主实验不使用跨 episode 自动积累的记忆；操作指南是预先提供的上下文知识。

来源：[§2–3、§5.1](https://arxiv.org/html/2610.01939v2#S5)。本页为 Codex 根据论文整理。

## GRPO：9 个任务、45 个实例、30 轮

| 项目 | 论文设置 |
|---|---|
| 更新模型 | Qwen3.5-4B 全参数微调；无 adapter / LoRA |
| 冻结部分 | VLA、SAM 3、运动与其他原语 |
| SFT / 示范 | 无 SFT 阶段，无专家示范数据；基础模型已有预训练能力 |
| 训练池 | LIBERO-PRO 的 goal、spatial、object 各 3 个任务，每任务 5 个 seed，共 9 任务 × 5 = 45 实例 |
| 每轮采样 | 从池中选 16 个实例，每实例尝试 8 次，共 128 episodes |
| 奖励 | 最终成败 1 / 0，无 shaping，无模型调用或仿真步数惩罚 |
| 优势 | 同一实例的 8 次奖励组内归一化；同一 episode 的生成推理与代码 token 使用同一优势 |
| 每轮优化 | 2 次 optimizer step，每次使用 64 episodes；Adam，学习率 1e−6，无 KL 项与熵项 |
| 总训练 | 30 轮 × 128 = 3,840 episodes；30 × 2 = 60 个 optimizer steps |
| 训练预算 | 每 episode 最多 24 cells、25 分钟；每次模型生成最多 4,096 tokens |

**9 个指任务，不是 9 条专家示例。** 45 个是任务与初始场景实例，之后的完整交互轨迹由当前模型自己采样。同一实例重复 8 次，用来比较随机采样得到的不同尝试。

**先收集、后更新：** 一轮内用固定权重完成 128 个 episode，随后分两个 64-episode 批次做梯度更新，再用新权重开始下一轮。不是每执行一个原语、每次看图或每次失败都更新参数；优化步也不是又执行一次任务。

来源：[§5.1、附录J表16](https://arxiv.org/html/2610.01939v2#S5.SS1)。

## 仿真结果

### Coder：后训练前后

| 评测范围 | 实例数 | 原始 Qwen3.5-4B | GRPO 后 4B |
|---|---:|---:|---:|
| LIBERO-PRO 训练实例 | 45 | 37.8% | 71.1% |
| LIBERO-PRO 未见任务 | 155 | 13.5% | 37.4% |
| RoboTwin 2.0 | 250 | 14.0% | 52.4% |
| RoboCasa365 atomic | 90 | 52.2% | 76.7% |
| RoboCasa365 composite | 160 | 12.5% | 19.4% |
| 全部未见实例 | 655 | 18.8% | 44.1% |
| 全部实例（含训练） | 700 | 20.0% | 45.9% |

训练只使用 LIBERO 的单臂机器人和 π0.5；迁移评测还涉及 RoboTwin 的双臂机器人 / LingBot-VLA 与 RoboCasa365 的移动操作 / RLDX-1。结果支持跨环境与原语库迁移，**没有独立证明代码能力、视觉理解、规划和调用能力各自贡献了多少**。该实验也不是通用 coding benchmark。

来源：[§5.2–5.3、表8–9](https://arxiv.org/html/2610.01939v2#S5.SS3)。

### 框架实验：不能混作 GRPO 收益

| 比较 | 结果 | 范围 |
|---|---|---|
| 同一 Astra：Tool → Code | 63.1% → 71.7% | 700 个仿真实例，改变交互接口 |
| 模型调用 / episode | 17.0 → 8.7 | 只统计两种方法都成功的实例 |
| 累计输入 token / episode | 788k → 276k | 同上，含缓存输入 |
| 估算费用 / episode | $1.63 → $0.74 | 同上，论文当时标价 |
| 无 VLA 的 RoboDojo RGB 测试 | SR 51.62%，Score 58.20 | Astra，42 任务、2,100 episodes，五维等权平均 |

这几项属于 Astra 使用 PyRUA-Lean 接口的实验，不是训练后 4B Coder 的表现。本文按 v2 更新 RoboDojo 完整评测，替换此前三任务试验的旧口径。

## 真机结果

论文 v2 未报告 Coder 真机成功率。官网后来展示 AF8 双臂的两个完整 episode，分别 41 / 42 cells、21:34 / 22:39；属于框架演示，不能当作 4B Coder 的真机泛化实验证据。

## 资源与部署

| 项目 | 已公开的信息 |
|---|---|
| 训练硬件与时间 | 单节点 8 GPUs，约 12 小时 |
| 框架 | miles 训练，SGLang 提供 rollout 服务；仿真与冻结 VLA / SAM 3 服务在旁运行 |
| 未披露 | GPU 型号、单卡显存峰值、服务设备分配，以及是否在训练阶段卸载 VLA / SAM |
| 推理 | 使用更新后的 Planner 权重，通过同一代码接口调用固定原语；不需部署优化器 |

因此，“完整 episode 采完再训练”有原文依据；“先卸载 VLA / SAM 再训练”只是可考虑的工程安排，不能写成作者已经这样实现。论文的 8 卡配置也不能证明单卡 32GB 的最低可行显存。

## 阅读收获与相关问题

**结合我们的系统（Codex 整理，待实验）：** 若 Planner 一次生成整条原语链，训练单位首先是这次模型输出；链内移动、抓取、VLA 的执行结果可回传，失败后的重规划构成下一轮输出。可参考 Coder 的完整 episode 采样和组内成败比较，同时参考 AgenticRoboRL 对真实上下文、图像与模型调用的记录方式。

- **信用分配仍粗：** 成败奖励作用于整条 episode 的生成内容，没有单独给每个重复原语评分；链变长后不一定能定位错误。
- **全失败组无相对信号：** 没有历史示范可以尝试直接 RL，但前提是当前模型偶尔能完成任务；不能从“无 SFT”推出完全不会执行也能稳定学起来。
- **参数学习与经验检索不同：** Coder 的改善写进模型参数，主实验未验证不断扩充历史 Memory 的独立效果。

## 核对依据

- [论文 v2](https://arxiv.org/html/2610.01939v2)：§3 框架，§4 RoboDojo，§5 Coder，附录J训练配置。
- [作者项目页](https://dagroup-pku.github.io/PyRUA-Lean/)：Coder 模型、评测表与后续真机演示。
- [官方仓库](https://github.com/DAGroup-PKU/PyRUA-Lean)：框架与模型入口。
