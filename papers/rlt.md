# RLT · RL Token: Bootstrapping Online RL with Vision-Language-Action Models

| 项目 | 内容 |
|---|---|
| 模块 | 5. Real-Robot Self-Improvement |
| Year / Venue | arXiv 2026.04 |
| Team | Physical Intelligence |
| Paper | https://arxiv.org/abs/2604.23073v2 |
| Website | https://www.pi.website/research/rlt |

[返回分类](../README.md#real-robot)

## 一句话

从冻结 VLA 提取 RL token 表征，训练轻量 Actor-Critic 输出动作，降低在线 RL 训练开销。

## 问题

精细动作需要快速在线改进，而完整VLA参数更新的计算与采样开销较高。

## 方法

VLA输出紧凑RL token，在线训练轻量Actor-Critic，改进精细操作阶段的动作。

先训练VLA提供RL token表征，在线阶段轻量Actor-Critic使用该表征学习动作。Evo-RLT是SJTU-MINT的复现实现，其manual、人为介入和控制路由设置与原论文须分开记录。复现代码：https://github.com/MINT-SJTU/Evo-RLT 。

## 实验结果

本条目以作者的真机实验为主，不将复现项目的模式开关视为原论文实验。

## 真机结果

螺丝安装、扎带紧固、充电器插入、网线插入四项任务；在线练习数分钟至数小时，精细阶段最高提速3倍。该数值不代表完整episode均提速3倍。

来源：原论文v2摘要与Physical Intelligence官方RLT介绍；Evo-RLT来源身份见本地entry记录。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
