# OmniBrain-0: A Unified Agentic Model for Embodied Intelligence

| 项目 | 内容 |
|---|---|
| 模块 | 7. RSI Projects |
| Year / Venue | arXiv 2026.10 |
| Team | 小米具身智能团队、澳门大学、清华大学 |
| Paper | https://arxiv.org/abs/2610.36013v1 |
| Code | https://github.com/luo-yc17/OmniBrain-0 |
| Website | https://public-bots.github.io/OmniBrain-0/ |

[完整阅读笔记](../ideas/omnibrain0-reading.md) · [HTML汇报](../reports/omnibrain0.html) · [返回分类](../README.md#rsi-projects)

## 问题

小模型难以复现强模型的规划、进度判断与恢复能力，操作和导航决策仍需统一。

## 一句话

先采集教师交互，预训练Base并训练操作／导航专家，经MOPD得到统一Planner；RSI先验证执行提醒，再回收成功轨迹训练专家和统一模型。

## 方法

训练操作与导航专家，再蒸馏统一Planner；迭代提醒、回收成功轨迹并重新训练。

数据采集、参数更新节奏、用户关注问题及限制见完整阅读笔记。

## 实验结果

9B→RSI：LIBERO-Pro65.5%→69.3%，Plus83.8%→84.5%，RoboCasa36539.6%→43.2%，RoboTwin2.0 88.2%→89.4%，R2R-CE65%→66%。初始3,846条示范、RSI新增1,142条。主表评测不使用外部Experience Library；总RSI轮数与每轮采集量未说明。

## 真机结果

堆积木、苹果入碗、开抽屉各20次：OmniBrain-0为75%／60%／85%，平均73.3%；π0.5平均58.3%，GPT-5.6-Sol平均86.7%。Planner无真机评测任务额外微调，底层硬件对齐细节未完整报告。

来源：原论文v1 §3–5、表1–5、图7/8、§6.4.1与附录A–C；作者项目仓库目前标记训练代码release soon。

整理与核对：Codex，2026-10-31；根据原论文与用户阅读讨论整理，未运行论文实验。
