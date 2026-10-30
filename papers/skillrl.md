# SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

| 项目 | 内容 |
|---|---|
| 模块 | 9. RL 后训练优化 |
| Year / Venue | NeurIPS 2026 |
| Team | UNC-Chapel Hill、University of Chicago、UC San Diego、NEC Labs America、UC Berkeley、UC Santa Cruz |
| Paper | https://arxiv.org/abs/2602.08234v2 |
| Code | https://github.com/aiming-lab/SkillRL |

[完整阅读笔记](../ideas/skillrl-reading.md) · [HTML汇报](../reports/skillrl.html) · [返回分类](../README.md#rl-post-training)

## 问题

原始轨迹冗余、含失败噪声，难以提炼可复用策略并持续改进Agent。

## 一句话

从成功与失败经验提炼文字技能，通过SFT和GRPO训练Qwen使用技能；训练批次之间更新SkillBank，区分技能更新、策略更新与验证反馈。

## 方法

o3提炼文字技能，SFT与GRPO训练Qwen使用技能，训练失败推动技能库更新。

数据采集、参数更新节奏、用户关注问题及限制见完整阅读笔记。

## 实验结果

ALFWorld／WebShop：GRPO为77.6%／66.1%，固定技能库84.4%／70.3%，完整SkillRL89.9%／72.7%；去除SFT为65.2%／46.5%。动态更新发生在训练过程中，不能作为部署期单episode热更新的证据。

## 真机结果

未报告真实机器人或图像输入VLA实验。ALFWorld采用文本交互，另有WebShop与搜索问答。

来源：论文v2 §3、表1/3、附录B–E；官方README录用声明；本地官方代码4d984d4的ALFWorld脚本、ray_trainer、skill_updater和SFT生成实现。

整理与核对：Codex，2026-10-31；根据原论文与用户阅读讨论整理，未运行论文实验。
