# AgenticRoboRL：用 SFT 与多轮 RL 训练机器人 Planner

| 项目 | 内容 |
|---|---|
| 论文全名 | AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics |
| 模块 | 9. RL 后训练优化 |
| Year / Venue | arXiv 2026.10；本文依据 v2（2026-10-21） |
| Paper | https://arxiv.org/abs/2610.28589 |
| Code | https://github.com/xinxinliu-ai/AgenticRoboRL |
| Website | https://xinxinliu-ai.github.io/AgenticRoboRL/ |
| Team | University of Central Florida、University of Southern California、Michigan State University |

## 问题

已有机器人 Harness 主要改工具和外部记忆，依赖强大的现成 Planner；如何直接训练 Planner，并兼容调用 VLA 与生成控制代码这两种执行方式？

## 一句话：解决方案

固定 VLA、感知和控制器，用成功示范做 SFT，再用完整任务的成败奖励训练 Planner 的多轮工具调用与代码生成。

## 方法：系统框架

**先用强模型成功轨迹训练 Qwen3.5-9B，再让它在原 Harness 中执行任务，收集多轮交互并做 RL；只更新 Planner，执行组件保持冻结。**

| 环节 | 输入 | 操作与输出 |
|---|---|---|
| SFT | Qwen3.8-27B 教师的成功 episode | 按每次模型调用拆成“学生当时能看到的上下文 → 教师回答”，训练学生 |
| Planner 执行 | 当前任务及 Harness 实际组织的上下文、观察、工具结果 | RPent 输出工具调用；CaP-X 输出 Python 控制代码 |
| 调用记录 | 每次实际发给模型的请求与实际生成的回答 | 代理记录 prompt/output token IDs、rollout log-probabilities，保留训练所需输入 |
| 结果关联 | 完整 episode 的结果、任务和初始状态 | 适配器关联模型调用与最终奖励，同一任务和初始状态的尝试组成一组 |
| 参数更新 | 已完成的 episode 与逐轮调用记录 | 计算组内相对优势，优化所选回答；更新权重后开始下一轮采样 |

**执行期间不更新参数。** 一个 episode 中可以多次观察、调用、失败恢复；收集一轮完整尝试后才优化。训练接口设在模型调用处，不要求两个 Harness 具有相同的低层动作表示。

来源：[§3.1–3.3、图2](https://arxiv.org/html/2610.28589v2#S3)。本页内容为 Codex 根据原论文整理，研究建议单独列出。

## 奖励与 RL：并非标准 GRPO

| 项目 | 论文设置 |
|---|---|
| 奖励 | 环境判定任务成功为 1，正常执行但未成功为 0；基础设施故障排除 |
| 比较组 | 相同任务、相同初始状态的 6 次尝试 |
| 优势 | 本次奖励减去其余有效尝试的平均奖励，即 leave-one-out；不除以奖励标准差 |
| 优化目标 | dual-clipped PPO token loss，附加 rollout 与训练后端的概率不匹配修正 |
| 训练位置 | 每个 episode 至多选择 16 个有效回答；同一 episode 使用相同优势，每个回答权重为所选回答数的倒数 |
| Critic | 不训练独立价值模型 |
| 无效梯度组 | 六次奖励完全相同，优势为零，不提供训练样本 |

例如一组奖励为 **1、0、0、1、0、0**：成功尝试的优势为 **0.8**，失败尝试为 **−0.4**。这是按论文公式构造的计算例子，不是论文发布的真实轨迹。每个被选中的回答都继承所在 episode 的优势，并没有独立评价每个原语的贡献。

来源：[§3.3.2、附录A](https://arxiv.org/html/2610.28589v2#S3.SS3)。

## SFT 与采样规模

| 项目 | RPent / VLA 调用 | CaP-X / 控制代码 |
|---|---|---|
| 学生 / 教师 | Qwen3.5-9B / Qwen3.8-27B | 同左，使用 CaP-X 内重新采集的教师轨迹 |
| SFT 数据 | 40,047 个 target turns | 979 个成功 episode，2,370 个 target turns |
| SFT 更新 | 1 epoch 共 626 步；主结果选验证集最优的第 563 步 | 1 epoch，37 步 |
| RL 每轮 | 64 组 × 6 次 = 384 episodes | 同左 |
| RL 总量 | 运行 9 轮，报告验证选出的第 6 轮；前 6 轮共 2,304 episodes、26,052 个回答、206 个优化步 | 训练 15 轮；RL 任务池为 35 个任务 |
| RL 优化批量 | 每步 128 个所选回答，学习率 1e−6 | 同左 |
| 数据划分 | 初始状态 11–44 收集示范和 RL，45–49 验证，1–10 评测 | 同样划分；剩余 25 个评测任务未用于训练 |

RPent 的 SFT 更新语言模型与 visual merger，冻结 vision encoder。不能把“626 个 SFT 优化步”与“206 个 RL 优化步”合并为同一种数据批次。

RPent 教师使用外部记忆，学生在 RL 与评测时不访问外部记忆。SFT 前删除记忆调用与结果，改写依赖记忆的教师文字并用 judge 检查，**工具参数保持不变**。因此不能据此认定教师经验从未参与训练，也不能认定外部记忆没有价值。

来源：[§3.3.1、§4.1、附录C](https://arxiv.org/html/2610.28589v2#A3)。

## 仿真结果

| Harness / 评测 | 原始 9B | SFT 后 | SFT + RL 后 | 口径 |
|---|---:|---:|---:|---|
| RPent / LIBERO-PRO | 18.1% | 65.1% | 71.0% | 8 suites × 10 tasks × 10 初始状态，共 800 episodes；学生无外部记忆 |
| RPent / LIBERO-Plus | 19.2% | 66.7% | 72.2% | 10,030 个配置；使用前一行训练得到的 checkpoint，不再训练 |
| CaP-X / LIBERO-PRO | 2.7% | 18.7% | 28.5% | 60 任务 × 10 初始状态，共 600 episodes；另行训练的 checkpoint，使用 privileged state |

**RL 的独立增量要从 SFT 后比较：** RPent 为 **+5.9 个百分点**，CaP-X 为 **+9.8 个百分点**。18.1%→71.0% 是 SFT 与 RL 的合计收益。

LIBERO-Plus 支持未见扰动下的鲁棒性；它沿用底层 LIBERO 任务，不能写成完全未见任务的迁移。CaP-X 的几何真值输入与 RPent 的输入条件不同，不能直接横比两行高低。两种 Harness 分别训练，没有证明同一权重直接跨 Harness 使用。

来源：[表1–3、§4.1–4.4](https://arxiv.org/html/2610.28589v2#S4)。

## 真机结果

论文实验为仿真，未报告真机训练或真机成功率。公开论文未给出 GPU 型号、GPU 数量、训练墙钟时间和峰值显存，不能据此承诺单卡 32GB 复现原配置。

## 阅读收获：与 PyRUA-Lean Coder 怎样对应

| 关注点 | PyRUA-Lean Coder | AgenticRoboRL |
|---|---|---|
| 训练路线 | 直接全参数 GRPO，无 SFT | 成功示范 SFT → 多轮 RL |
| 学生 | Qwen3.5-4B | Qwen3.5-9B |
| Planner 输出 | Python cell，组合原语、条件检查与重试 | RPent 工具调用，或 CaP-X 控制代码 |
| 相对奖励 | 8 次尝试内归一化 | 6 次尝试内 leave-one-out，不做标准差归一化 |
| 更新时机 | 收集完整 episode 后批量更新 | 同左 |
| 值得参考的部分 | 无示范时，直接验证现有模型能否通过成功/失败自采样提高接口使用能力 | 保留实际多模态请求，把模型调用与 episode 结果关联，兼容不同执行接口 |

**结合我们 Harness 的判断（Codex 整理，待实验）：** 当前 Planner 一次生成一条粗粒度原语调用链，失败后重规划，可将“一次生成链 / 一次重规划”作为模型决策轮；链内原语执行仍留在运行时。奖励先用任务最终成败，不需要先做逐原语人工标注。若同一组尝试全部失败，组内相对奖励没有学习信号，需先改善成功率或收集成功示范，不能只增加训练轮数。

需要画面才能决定时，应在下一次 Planner 调用前返回当前图像。训练保存**当时实际可见**的图像、文本、生成内容和旧策略概率；不能把执行结束后的完整历史补到早期决策输入中。终局奖励可以用于训练多轮 Planner，但不能定位到底哪个原语导致失败。

关于 32GB 显卡：4B + LoRA、小组采样与分时运行训练/执行服务属于我们的工程候选方案，**不等于两篇论文的原配置**；VLA、SAM 即使冻结也占显存。应分别实测采样与训练峰值，再决定是否需要分机运行。

## 来源索引

- [论文 v2](https://arxiv.org/html/2610.28589v2)：§3 信息记录与训练，§4 评测与划分，附录A–C 优化与规模。
- [官方仓库](https://github.com/xinxinliu-ai/AgenticRoboRL)：框架说明、RPent / CaP-X 接口与训练入口；论文配置以带版本原文为准。
- [PyRUA-Lean v2](https://arxiv.org/html/2610.01939v2)：§5、表8–9、附录J，用于以上对照。
