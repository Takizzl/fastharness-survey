# PLD · Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

| 项目 | 内容 |
|---|---|
| 模块 | 5. Real-Robot Self-Improvement |
| Year / Venue | arXiv 2025.10 |
| Team | NVIDIA、UC Berkeley、CMU、UT Austin |
| Paper | https://arxiv.org/abs/2511.00091v1 |
| Website | https://wenlixiao.com/self-improve-VLA-PLD |

[返回分类](../README.md#real-robot)

## 一句话

训练任务残差专家，采集基础 VLA 与专家共同执行的恢复轨迹，再用 SFT 更新多任务 VLA。

## 问题

VLA依赖人工示范，单纯采集专家状态又可能偏离基础策略部署时会遇到的状态。

## 方法

训练残差专家，用基础VLA与残差混合采集恢复轨迹，再通过SFT更新通用VLA。

第一阶段冻结VLA训练轻量残差；第二阶段让残差干预覆盖基础策略常访问状态并收集恢复数据；第三阶段SFT蒸馏回VLA。训练残差可用失败交互，最终SFT示范选择成功轨迹，可含失败后恢复。

## 实验结果

原文报告LIBERO成功率99%，并在SimplerEnv评估。残差专家用于采集，整理后的轨迹通过标准SFT更新通用模型。

## 真机结果

Franka与YAM操作；YAM展示GPU插拔四阶段循环持续1小时无需人工复位。Franka特制桌面支持部分自动复位，论文未给总体人工恢复比例。

来源：原论文v1 §3、§4.4、Algorithm 1、附录D；首次提交2025-10-30，按日期而非arXiv编号定年月。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
