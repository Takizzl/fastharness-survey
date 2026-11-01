# GO-3 Preview: Genie Master and WRAM

| 项目 | 内容 |
|---|---|
| 模块 | 7. RSI Projects |
| Year / Venue | Preview 2026.10 |
| Team | 智元 AGIBOT |
| Paper | https://www.agibot.com/article/231/detail/133.html |
| Website | https://www.agibot.com/article/231/detail/133.html |

[HTML汇报](../reports/go-3-preview.html) · [返回分类](../README.md#rsi-projects)

## 一句话

智元 GO-3 Preview：Genie Master 通过 EEP 组织任务执行与反馈，积累 Harness 与策略改进经验；WRAM 连接任务理解、未来状态预测与动作生成。

## 问题

部署后遇到新情况时，需要协调任务执行、故障恢复、经验积累与动作策略改进。

## 方法

Genie Master组织任务与反馈，经验写入记忆或用于策略训练；WRAM预测未来并生成动作。

Genie Master通过EEP连接观察、引导、执行反馈与任务进度。Harness RSI在执行中记录案例、任务结束后总结；Policy RSI将执行、接管与恢复数据后处理再训练策略。WRAM包含控制导向视觉表示、未来状态预测与动作生成；KASO选择与训练动作一致的候选未来。以上为Preview发布体系，不能直接视为GO-3 Nano Preview的完整评测配置。

## 实验结果

本条目收录Preview公开技术体系。发布稿提及RoboDojo、RoboTwin、RoboColiseum榜单，但所提供笔记未列完整评测协议与成功率，不补写数值。

## 真机结果

公开展示便利店挂货恢复与乐高装配；乐高示例含额外示范和微调。未提供可用于统一比较的任务次数与成功率。

来源：AGIBOT官方2026-10-29发布介绍；用户提供GO-3_Preview_Genie_Master_WRAM.html及其中5项来源。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
