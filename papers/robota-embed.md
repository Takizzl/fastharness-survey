# Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution

| 项目 | 内容 |
|---|---|
| 模块 | 3. Memory |
| Year / Venue | arXiv 2026.10；v1 2026-10-14，arXiv 预印本 |
| Paper | https://arxiv.org/abs/2610.19495v1 |
| Website | https://robota-ai.github.io/robota-embed/ |
| Team | NVIDIA、MIT、UC Berkeley、Oxford、CMU（论文首页） |

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

## 核对依据

[表 6](https://arxiv.org/html/2610.19495v1)
