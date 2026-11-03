# REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control

| 字段 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | arXiv 2026.10 |
| Team | NUS、InfRec |
| Paper | https://arxiv.org/abs/2610.42053v1 |
| Code | https://github.com/InfRec-Cardinal/REA |
| Website | https://mikeeeeeeeeeeeeee.github.io/REA/ |

[返回分类](../README.md#code-policy) · [完整阅读HTML](../reports/rea.html)

## 一句话

统一策略接口，按统计或Agent选程序，按异常或视觉判断触发恢复。

## 问题

大模型延迟会阻塞快策略；只凭异常不能发现任务未完成的静默失败。

## 方法

统一策略接口，按统计或Agent选程序，按异常或视觉判断触发恢复。下面按输入、路由、执行与评测展开。

更新日期：2026-11-03。依据原论文、官方代码与本轮阅读问答整理。重点是大模型与下游策略的分工、Route Memory、Judge 和评测条件。

## 论文与主要贡献

REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control，arXiv:2610.42053v1，2026-10-30。

团队：NUS HPC-AI Lab、InfRec Cardinal AI Lab、UC Berkeley、东京大学、中科院深圳先进院、HKUST。

[Paper](https://arxiv.org/html/2610.42053v1) · [Code](https://github.com/InfRec-Cardinal/REA) · [Website](https://mikeeeeeeeeeeeeee.github.io/REA/) · [EBench-Astra 笔记](ebench-astra.md)

**主要贡献是统一执行接口，并利用路由记忆、边界检查与共享预算恢复，组织已有程序、VLA 和机器人技能。**

| 层次 | 负责什么 |
|---|---|
| System 0 | 执行 Python 程序、VLA 或原生机器人技能，产生实际动作 |
| System 1 | 选择策略、决定切换和恢复，不直接产生机器人动作 |
| System 2 | 离线或在线生成代码、建议策略或判断；不固定为 Astra |

来源：正文 §1、§3。不同实验实例化了不同 Router，不能把各实验功能拼成一条统一验证过的流程。

[原论文图与完整阅读页](../reports/rea.html)

## 程序来源与 Route Memory

LIBERO-Pro 候选由 Codex、Agents SDK、ASPIRE 或 Harness 生成，在评测前固定。REA 利用这些程序并选择执行，主要研究已有能力的组织。

**Route Memory 是开发集评测统计，不是梯度训练的记忆模型。**

1. 在开发种子上测试每个任务的各候选程序。
2. 保存成功次数、测试次数与执行步数，按成功率排序。
3. 成功率相同时，优先选择每次成功消耗步数较少者；代码以全部已评分运行步数除以成功次数计算成本。
4. 固定路由表，测试阶段查表选择；开发与测试种子分离。

完整库有 179 个程序，每程序 10 个开发种子，共 1,790 次评测。完整实验开发种子为 61–70，测试种子为 1–50。此过程更新统计和排序，没有 PPO 或基础模型参数更新。

两个候选的典型恢复顺序为 `A → B → A`；三个候选时按排名依次尝试。换程序从当前物理状态继续，不 reset；所有运行与 Judge 共用步数、时间预算。

来源：§3.2、§4.1–4.2、附录 A.2、B.4；官方 `docs/routed-systems.md`。以上运行顺序对应论文实验，当前代码另有可配置的运行次数。

## Router 方法与模型分工

正式命名的变体有 REA-M、REA-A、REA-V；另有学习式选择器、真机异步调度。

| 方法 | 选择依据 | 何时选择或恢复 | 模型与更新 |
|---|---|---|---|
| REA-M | 开发成功率与成本 | 开局查表；异常或截断后，有预算才尝试后续候选；正常返回不检查完成 | 无在线 System 2，无 Router 梯度训练 |
| REA-A | Route Memory、候选源码、本体状态、异常历史 | Agent 选择初始策略；异常门触发后再选恢复策略 | 文本 Agent，论文使用 jev-1.13.0，无额外训练 |
| REA-V | Route Memory 排序，视觉 Judge 控制停止或继续 | 每次策略返回后检查；done 停止，not_done 有预算则升级候选 | DeepSeek 视觉 Judge，开发阶段校准提示词和阈值 |
| RoboTwin 学习式 Router | 初始指令、三路图像、机器人状态 | 预测候选成功概率、取最大；开局选择一次，整局保持 | Qwen3.5-4B＋LoRA＋候选成功预测头 |
| Aloha 异步选择 | 任务、图像、关节状态、候选说明、执行反馈 | 大模型后台给建议，当前策略继续执行，在动作块边界应用建议 | 已有大模型推理＋固定调度，无专用选择器训练 |

**学习式 Router 选择一个策略，不生成整局策略顺序。REA-V 的 Judge 决定是否继续，下一候选仍主要来自预先排序。**

学习式选择器有七个 VLA 预测头。新增 Code 线性头用成败标签和 BCE 训练，这一步冻结编码器、LoRA 与七个 VLA 头；247 个训练场景、40 个开发场景，选 epoch 4。该实验不进行中途切换，不启用视觉 Judge。

选中 Code 后，GPT-6 Astra 根据图像、状态、标定与反馈生成 Python，每次计算一个 Cartesian `move_gripper` 目标，最多 40 次决策。由 Astra 提前写固定程序，与执行时继续调用 Astra，是不同参与方式。

另有盲目重试、去掉 Route Memory、阻塞式 Advisor 等消融。RoboTwin 200 场景和 BEHAVIOR 的旧版 reflex／deliberate 路由，不等同于学习式选择器。

来源：§3、§4.1、附录 B.1–B.2、C.1–C.2。

## DeepSeek Judge 的效果与指标

Judge 接收任务、初始画面与当前画面，输出 done／not_done；不读取在线环境成功信号。最终实验结果由环境独立评分。

| 开发校准输入 | 准确率 | 判完成的精确率 | 成功召回率 |
|---|---:|---:|---:|
| 仅当前画面 | 67.1% | 10.5% | 3.6% |
| 初始＋当前画面 | 79.2% | 58.7% | 66.1% |

216 条开发样本含 160 条失败、56 条成功，始终猜失败也有 `160 / 216 = 74.1%` 准确率。79.2% 是开发校准结果，不是独立测试准确率。单次判断约 1.6 秒；后继模型在同一开发标签上为 78.2%。

| 系统对照 | 异常门 REA-M | 视觉门 REA-V | 条件与代价 |
|---|---:|---:|---|
| LIBERO-Pro，590 次 | 424/590，71.9% | 442/590，74.9% | 净增 18 次，精确计数为 3.05 个百分点，论文写 +3.1；p=0.022；每成功一次平均耗时 57.9→120.7 秒 |
| 困难子集，72 次 | 37/72，51.4% | 48/72，66.7% | +15.3 个百分点；选择了 Fix 失败较多的样本，不能代表一般任务 |

590 次测试的最终判断中，说 done 共 305 次，其中 276 次真的完成、29 次未完成，所以判完成精确率为 `276 / 305 = 90.5%`。只统计每局最后一次判断，不覆盖所有中途升级判断。

**准确率是所有样本猜对的比例；判完成精确率是“它说完成”时有多少真的完成。** 74.1% 与 90.5% 来自不同数据集、不同指标，不能比较高低。

恢复能救回失败，也可能把已成功任务重新执行坏。论文对救回、破坏、重放波动的归因，使用 REA-M 独立运行作首次结果的代理，属于近似分解。

来源：§4.4–4.5、附录 B.5–B.6、表 13–14。困难集使用 deepseek-v4-flash-vision-exp，较大实验使用后继 deepseek-flash。

## 仿真结果与对照条件

| 实验 | 结果 | 条件 |
|---|---|---|
| LIBERO-Pro，60 配置×50 种子 | REA-M／A 95.9%，SDK 94.7% | 3,000 次，不含 Long；4,000 控制步、900 秒，共享恢复预算 |
| 程序对齐的 37 个任务 | REA-M 95.3%，最强单方法 93.7% | REA 候选与基线测试程序逐份一致，较直接支持选择收益 |
| RoboTwin，50 clean＋50 randomized | MEDex 80%，七 VLA 路由 84%，混合 86% | 开局固定选择；Code 选 9 场、成功 8 场，净增 2 场 |
| BEHAVIOR，5 个拾取任务×10 实例 | REA 27/50，54%；SDK 25/50，50% | 同模型工具及时间预算、交错运行；p=0.77，不显著 |
| RoboTwin，另一个 200 场景迁移实验 | 同期 REA 97/200，Codex 75/200 | 后来同配置 REA 133/200，有运行窗口波动，不能跨窗口混比 |

“37 个任务程序对齐”指：Codex 单独执行 A、SDK 执行 B、ASPIRE 执行 C，REA 从相同的 A／B／C 选择。不是所有方法运行同一段程序。

剩余 23 个任务中，14 个任务的 REA Codex 槽位用 Harness 程序，10 个任务用 ASPIRE Evo 而非基线 Fix，其中 1 个任务重叠。这部分收益无法全部归因于 Router。

RoboTwin 100 场景曾用于早期开发，仅明确从新增 Code head 的训练和选模中排除；部分基线是历史运行、MEDex 用另一主机，Show-Harness 历史版本有姿态更新错误，不能视为完全统一条件下的排名。

来源：表 1–2、§4.7、附录 A.2、C.1–C.2。

## 真机结果与路由

| 实验 | 方法 | 结果与限制 |
|---|---|---|
| G1 走近并推椅子 | DeepSeek 读头部、腕部图像，在技能边界选走路、推、收臂、停止，共 4 次决策 | REA 8/10，SDK 5/10；对 SDK 差异不显著，p=0.35 |
| Aloha 四 Agent 对比 | 只标 REA，未明确 M／A／V；最多 3 次抓取、无总时间上限 | REA 10/10，ASPIRE 8/10，Codex 5/10，SDK 4/10；REA 平均模型调用 41.1 次，耗时 1,618 秒 |
| Aloha π0.5＋Code | 10 次 REA 全部异步，Code 实际执行于 5 次；每块 15 目标／30 Hz | REA 8/10，π0.5 3/10；不同日期与配置，REA 更慢，不是严格配对大样本 |
| G1 低延迟服务 | 提前计算视觉决策＋传感器安全门，明确不使用 Router | 只测延迟；1–3.6 ms 是请求响应，不是模型推理时间 |

公开 Aloha 代码由后台大模型选 `candidateId`，固定程序负责边界切换、建议时效、最少连续执行块数；模型尚未返回时不阻塞当前控制器。当前配置默认每 4 块思考／切换，可修改，不等于全部论文实验设置。

异步是调度方式，不是另一种参数学习。未报告各 Router 的真机完整横向消融。RoboTwin 86% 不能归因于中途 VLA→Code 接管或 Judge，因为未启用。REA 未报告 RoboDojo 实验。

来源：附录 D.1–D.4；[Aloha Router](https://github.com/InfRec-Cardinal/REA/blob/main/src/policies/aloha-router.mjs)、[配置](https://github.com/InfRec-Cardinal/REA/blob/main/examples/aloha-real.config.mjs)、[异步运行文档](https://github.com/InfRec-Cardinal/REA/blob/main/docs/async-systems.md)。

## 与公开领先结果的比较

以下为 2026-11-02 核对快照，不是统一协议重测。

| 基准 | REA | 公开参考 | 比较边界 |
|---|---:|---|---|
| LIBERO-Pro | 95.9% | Encore 96.3%，60 配置、3,000 次 | 范围较接近，但模型、示范与开发不同；数值低 0.4 个百分点 |
| LIBERO-Pro 扩展参考 | 95.9% | Astra＋ICL 98.25%；扩大执行预算后 99.25% | 包含 Long、800 次，范围及预算不同 |
| RoboTwin | 混合 86% | GO-3 Nano Preview 官方均值 85.01% | REA 100 场景，榜单 10,000 次，不能据此认定超过 SOTA |
| BEHAVIOR | 5 个拾取任务 54% | 官方已验证 North Star 成功率 48.2% | 完整 100 任务与拾取子集不可排名 |

来源：[Encore](https://arxiv.org/html/2609.37359v1)、[Astra＋ICL](https://arxiv.org/html/2610.22471v2)、[RoboTwin 榜单](https://robotwin-platform.github.io/leaderboard)、[BEHAVIOR 已验证数据](https://huggingface.co/spaces/behavior-1k/2026-challenge-leaderboard/resolve/main/data/results.jsonl)。

## 阅读收获与相关问题

- 已确认：统计路由、Agent 选择、视觉完成判断、学习式开局选择、异步中途切换是不同机制；不都需要在线调用 Astra。
- 已确认：37 个程序对齐任务更适合判断路由收益；候选程序变化时，不能把全部收益归因于 Router。
- 未明确：Aloha 四 Agent 实验对应的命名 Router 与各次完整配置。
- 阅读判断：现有证据支持组织已有能力与恢复，尚不足以认定通用 VLA／大模型协同达到统一评测 SOTA。


## 来源

[§3–4；表1–2；附录A.2、B.5–B.6、C.1、D.1–D.4；官方Aloha Router与异步运行代码](https://arxiv.org/abs/2610.42053v1)。Codex依据原文、官方实现与用户阅读问答整理；阅读判断单列。
