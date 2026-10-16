# Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution

| 项目 | 内容 |
|---|---|
| 模块 | 3. Memory |
| Year / Venue | arXiv 2026.10；v1 2026-10-14，未核实会议录用 |
| Paper | https://arxiv.org/abs/2610.19495v1 |
| Code | -（2026-10-16 未核实到官方代码、权重发布入口） |
| Website | https://robota-ai.github.io/robota-embed/ |
| Team | NVIDIA、MIT、UC Berkeley、Oxford、CMU（论文首页） |
| Review | 来源核对完成，待人工审核 |

## 一句话

用视觉、语言和动作 embedding 找到当前执行阶段可参考的历史经验，再交给机器人策略生成动作。

## 问题

只有任务文字或相似画面，容易找对任务却找错执行阶段，无法挑出适合当前动作的历史经验。

## 方法

将任务、画面和动作编码为向量，检索历史执行片段，把画面、命令和反馈交给策略复用。

- **怎么编码：** 当前任务指令、交互区域图像、同步 native action → 1024 维归一化向量；候选端编码历史指令、已记录的后续四秒视频及动作。使用余弦相似度匹配，不是在预测当前机器人的真实未来。
- **怎么读记忆：** 向量用于选片段；历史 RGB、命令、自身状态、反馈和时间戳提供给 Astra。向量本身不直接作为 Astra 输入，也不直接产生执行动作。
- **怎么累积：** Embed2Evolve 在开发阶段将已完成的成功和普通失败回合写入任务内记忆，调整检索数、刷新间隔、历史长度及成功/效率加分。正式测试固定记忆和配置，Astra 与 embedding 权重保持冻结。
- **两条应用：** Embed2ICL 为 DreamZero 提供参考视频，或训练 Fast-WAM 使用 Context Tokens；Embed2Evolve 围绕冻结 Astra 复用执行经验。不能把三条配置的收益混成一个实验。

## 仿真结果

Robota-Embed-Bench：4,000 个查询、8,000 条共享候选，片段级 R@1 47.33%、回合级 R@1 81.77%（摘要精确值；表格显示 47.3 / 81.8）。ManiSkill 五任务、每条件每任务 20 次：Astra Direct 24%、随机历史 20%、Evolve + Omni 33%、Embed2Evolve 68%；平均每测试回合策略 tokens 为 0.921M / 未报 / 约 2.531M / 0.518M，含失败、不含开发成本。DROID-Sim：无参考 47.0%、随机 36.0%、原始 top-1 50.3%、重排序后 56.3%；LIBERO 五个筛选难任务：86.4%→92.8%，该路线训练策略使用上下文。

ManiSkill 主表（论文表 6）：

| 任务 | Astra Direct | 随机历史 | Evolve + Omni | Embed2Evolve |
|---|---:|---:|---:|---:|
| Poke Cube | 45% | 15% | 45% | 80% |
| Stack Cube | 10% | 20% | 20% | 60% |
| Lift Peg Upright | 30% | 40% | 55% | 65% |
| Pull Cube with Tool | 10% | 10% | 20% | 50% |
| Two-Robot Stack Cube | 25% | 15% | 25% | 85% |
| 平均 | 24% | 20% | 33% | 68% |

相对 Evolve + Omni 的策略 tokens 少约 79.5%，属于独立开发记忆与配置后的完整系统对比，不是固定同一系统仅替换编码器的消融。DROID-Sim 的 56.3% 包含重排序收益；检索 R@1 不等于机器人成功率。

## 真机结果

三项真机任务报告的是任务进度分数，每条件每任务 12 次：DreamZero Banana→Bowl 21.67→40.00；Fast-WAM Pick Fruit 75.00→79.17、Split Cup 66.67→87.50。不是二元成功率；Fast-WAM 路线包含策略训练。

## 汇报中的研究重点：RoboDojo + Astra

用户已有汇报：`Robota-Embed论文解读.html`；配套可编辑源：`papers/robota-embed/paper_report.zh.md`（原工作区）。以下由 Codex 据该汇报整理，研究设想尚未实施。

- 用户目标原话：“我们现在考虑的都是在robodojo里面直接使用astra来进行推理”；“因为我要用他来复用经验，在robodojo中”。
- 我们优先参考 Embed2Evolve：当前观测检索历史执行材料，让 Astra 直接推理与行动，不优先走训练 Fast-WAM 的路线。
- 先固定策略、开发/测试划分与预算，对比无参考、随机参考、VL 检索、VLA 检索，分别评估阶段匹配、控制成功率和 token 成本。该建议来自汇报，尚无 RoboDojo 实验结果。
- 失败经历可被检索，回合成功标签不表示每个局部动作正确；历史材料保留反馈，不能自动改写为正确操作建议。
- ManiSkill 使用 endpoint-error action proxy 适配，是分布外适配；RoboDojo 的动作语义、codec、投影器与历史封装仍需核实，不能假定补零就能迁移。

## 来源与核对

- [arXiv v1](https://arxiv.org/abs/2610.19495v1)：标题、日期、摘要精确检索指标；34 页、14 图。
- 本地论文 LaTeX：第 3 节、5.2 节、附录 A / D；表 2、6 及真机进度分数表，与已有汇报交叉核对。
- [作者项目页](https://robota-ai.github.io/robota-embed/)：链接来自 arXiv；本次网络访问失败，未据此声称代码或权重已发布。未核实到代码不等于断言没有代码。
- 核对日期：2026-10-16。论文结果与团队讨论分别记录；未运行机器人实验。

## 链接核查 · 2026-10-17

论文标题与项目页对应，链接可访问；项目页未发现明确的 GitHub 发布入口，保留原有代码/权重公开范围说明。
