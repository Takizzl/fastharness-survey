# CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

| 项目 | 内容 |
|---|---|
| 模块 | 9. RL 后训练优化 |
| Year / Venue | 技术论文 2026 |
| Team | 香港中文大学MMLab、NovaXBot |
| Paper | https://waltstephen.github.io/captain/assets/paper/CaPtain.pdf |
| Code | https://github.com/waltstephen/CaPtain |
| Website | https://waltstephen.github.io/captain/ |

[完整阅读笔记](../ideas/captain-reading.md) · [HTML汇报](../reports/captain.html) · [返回分类](../README.md#rl-post-training)

## 问题

小模型视觉代码控制不足，终局奖励难以区分长轨迹中各次模型调用的贡献。

## 一句话

先SFT再用仿真状态Critic辅助异步RL，训练Qwen3.5-4B编写低层机器人代码；按request分配信用，并明确区分episode、训练行和参数更新批次。

## 方法

Qwen先SFT再RL，物理状态Critic估计调用前后进展，为代码调用分配信用。

数据采集、参数更新节奏、用户关注问题及限制见完整阅读笔记。

## 实验结果

留出LIBERO40任务×6初始状态共240局：基础0%、SFT55.4%、RL73.8%；LIBERO-PRO0.3%／59.5%／78.5%。RoboTwin2.0为22.6%，RoboDojo0.8%。300轮×256=76,800 episodes，Qwen75次更新。论文25,961行／861M与公开数据24,440行／797.1M、2,036 episodes分开记录。

## 真机结果

Astrabot XR1：先在粗略XR1孪生仿真中适配，无真机训练数据；图5展示两条新物体／布局任务，不作为总体成功率。部署不使用Critic。

来源：作者33页PDF §3–4、图2/5/6、表1/5、附录A/C/H；官方CaPtain代码与数据卡。

整理与核对：Codex，2026-10-31；根据原论文与用户阅读讨论整理，未运行论文实验。
