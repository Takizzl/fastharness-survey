# MemEvolve: Meta-Evolution of Agent Memory Systems

| 项目 | 内容 |
|---|---|
| 模块 | 3. Memory |
| Year / Venue | ICML 2026（官方仓库 README 声明） |
| Paper | https://arxiv.org/abs/2512.18746v1 |
| Code | https://github.com/bingreeky/MemEvolve |
| Team | OPPO AI Agent Team、LV-NUS lab |

## 一句话

内层从执行轨迹积累记忆，外层根据反馈改写记忆的编码、存储、检索和管理代码。

## 问题

固定记忆架构只能更新内容，无法针对任务改变经验的组织和使用方式；同一套人工设计的记忆机制迁移到其他任务时可能降低表现。

## 方法

EvolveLab 将记忆系统统一为 encode、store、retrieve、manage 四个模块。内层执行任务并写入经验；外层读取轨迹、成功率、成本和延迟，诊断现有机制，生成候选实现并评测筛选。论文配置为三轮演化，每轮保留一个父代、生成三个后代。架构选择采用成功率、成本和延迟的 Pareto 排序，同级优先成功率。

演化结果包括按任务阶段检索的 Lightweight，以及能提炼文本经验和可复用工具、维护记忆库的 Cerebra。改变的是记忆系统代码与内容，不依赖更新底层 LLM 权重。官方代码包含评测入口、记忆 provider 和自动多轮演化 CLI。

## 实验结果

表 2，同一 Flash-Searcher + GPT-5-mini，均为 pass@1：

| 基准 | 规模 | 原始框架 | 加 MemEvolve | 提升（百分点） |
|---|---|---|---|---|
| WebWalkerQA | 170 题子集 | 71.18% | 74.71% | 3.53 |
| xBench-DS | 100 题 | 69.00% | 74.00% | 5.00 |
| TaskCraft | 300 题工作子集 | 69.67% | 72.00% | 2.33 |
| GAIA | 165 题 | 69.09% | 73.33% | 4.24 |

附录 B.1：WebWalkerQA 和 xBench-DS 的记忆架构在 TaskCraft 上演化。TaskCraft 工作子集中的 120 题用于三轮演化，因此其整体结果不作为严格留出测试。GAIA 架构演化使用 GAIA Level-1 和 67 道 TaskCraft 题，GAIA 总体结果也不能称为完全未见任务测试。

表 2 还报告跨模型迁移：Flash-Searcher + Kimi K2 在 WebWalkerQA 上从 52.35% 到 69.41%，提升 17.06 个百分点；这不是 GPT-5-mini 的提升，也不是跨基准平均值。Smolagents + GPT-5-mini 在 GAIA 上的 pass@1 从 55.75% 到 64.24%。论文还评估 CK-Pro、OWL 框架迁移，以及记忆架构逐轮演化的效果。

表 3，Flash-Searcher 在 GAIA 上单题 API 费用从 $0.086 到 $0.085，平均延迟从 505.46 秒到 693.33 秒；xBench 从 $0.141 到 $0.136，延迟从 523.05 秒到 773.06 秒。费用略降不代表执行更快，这些单题指标也不等同于架构搜索总成本。

## 适用范围

实验为通用工具使用、信息检索和网页任务，不包含机器人仿真或真机成功率。对具身任务可借鉴的是：除了存储历史经验，还可将记忆筛选、检索和维护逻辑作为可演化对象。

## 来源

- [论文 v1：§3–5、表 2–3、附录 B.1](https://arxiv.org/pdf/2512.18746v1)
- [官方代码与 ICML 2026 录用声明](https://github.com/bingreeky/MemEvolve)
