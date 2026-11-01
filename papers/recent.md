# RECENT · Efficient Skill Grounding via Code Refactoring with Small Language Models

| 项目 | 内容 |
|---|---|
| 模块 | 4. Skill Growth |
| Year / Venue | ICML 2026 |
| Team | Sungkyunkwan University |
| Paper | https://arxiv.org/abs/2606.07999v1 |

[返回分类](../README.md#skill)

## 一句话

保留技能代码的控制结构，用小语言模型局部修改执行绑定，适配机器人本体与环境变化。

## 问题

本体和环境变化会使已有技能失效，全量重写增加执行中断与适配成本。

## 方法

保留技能代码控制结构，小语言模型修改本体和环境相关绑定，执行检查触发局部修复。

技能保存代码、能力需求、前置条件、预期效果与API信息。先诊断本体兼容性，执行期间由unit test触发局部FIM修补；目标是技能适配。Genesis是仿真器依赖，未作为RECENT官方代码收录。

## 实验结果

表1：换机械臂成功率73%，换夹爪82.5%。离线验证技能，部署时Qwen2.5-Coder-7B局部重构，不进行在线参数训练。

## 真机结果

表24扫码装袋共10次：RECENT 8/10，CaP 4/10；每次平均中断0.40对3.00次，中断耗时2.34对23.51秒。

来源：原论文v1 §4、表1、附录表24；arXiv Comments标注ICML 2026。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
