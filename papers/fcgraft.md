# FCGraft · Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | ICML 2026 |
| Team | Sungkyunkwan University |
| Paper | https://arxiv.org/abs/2606.13097v2 |

[返回分类](../README.md#code-policy)

## 一句话

检索已验证的函数骨架及其 KV 缓存，通过拼接和局部修改生成新任务的控制代码。

## 问题

代码策略反复prefill带来生成延迟，全量重生成容易破坏有效控制结构。

## 方法

检索已验证函数及KV缓存，拼接代码并局部修补，成功后更新函数缓存库。

接口层保存函数ID、签名与KV，实现层保存代码和KV。任务生成时检索接口，执行前链接实现；失败时仅生成待修复代码区间。不更新代码模型参数，初始库含oracle基本函数。

## 实验结果

论文另评估仿真代码策略生成；本次索引保留已有笔记中的真机表2结果，不将策略合成时间当作整次任务耗时。

## 真机结果

办公桌整理、厨房准备各9种条件×3次，共54次；成功率77.78%／81.48%，策略合成时间3.80／2.85秒。办公桌RAGCache成功率44.44%。

来源：原论文v2首页、§4、表2、附录C.2表16；arXiv Comments标注ICML 2026。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
