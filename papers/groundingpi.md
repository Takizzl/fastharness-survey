# GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives

| 项目 | 内容 |
|---|---|
| 模块 | 8. 感知基础模型 |
| Year / Venue | arXiv 2026.09 |
| Paper | https://arxiv.org/abs/2609.39601 |
| Code | https://github.com/groundingpi/GroundingPI |
| Website | https://groundingpi.github.io/ |
| Team | 小鹏汽车、北京大学、香港大学、UC Berkeley、Princeton、NUS、清华、HKUST (GZ) |

## 一句话

用定位监督训练视觉语言底座，将中间特征接入动作模型，支持精确感知与控制。

## 问题

通用语义理解不能保证细粒度空间定位，动作示范同时承担视觉学习与控制学习的负担。

## 方法

4B 级视觉语言基础模型，以量化坐标词元统一标签、点和框输出。机器人分支将中间视觉语言特征注入 Action DiT；不是直接把框坐标换成机械臂动作。

## 实验结果

论文表 5：COCO 每框输出 7.6 tokens，Dense200 每框 5.1 tokens。这是输出序列化成本，不是推理速度或机器人成功率。

## 来源

- [已有笔记原文](../review/2026-10-17-资料补充/sources/groundingpi.txt)


## 核对依据

[表 5](https://arxiv.org/html/2609.39601v1)
