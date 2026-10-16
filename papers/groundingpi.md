# GroundingPI: GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives

| 项目 | 内容 |
|---|---|
| 模块 | 8. 感知基础模型 |
| Year / Venue | arXiv 2026.09 |
| Paper | https://arxiv.org/abs/2609.39601 |
| Code | https://github.com/groundingpi/GroundingPI |
| Website | -（权重页不代替独立项目主页） |
| Team | 小鹏汽车、北京大学、香港大学、UC Berkeley、Princeton、NUS、清华、HKUST (GZ) |
| Review | 依据已有资料整合；未核实字段保留待审核 |

## 一句话

用定位监督训练视觉语言底座，将中间特征接入动作模型，支持精确感知与控制。

## 问题

通用语义理解不能保证细粒度空间定位，动作示范同时承担视觉学习与控制学习的负担。

## 方法

4B 级视觉语言基础模型，以量化坐标词元统一标签、点和框输出。机器人分支将中间视觉语言特征注入 Action DiT；不是直接把框坐标换成机械臂动作。

## 实验结果

现有笔记未给出可直接入表的具体成绩。34 项感知基准平均分、nuScenes 开环轨迹误差和机器人成功率属于不同指标，不能混写。

## 真机结果

当前笔记未提供可确认的真机量化结果。

## 资料补充与边界

Paper：arXiv:2609.39601v1，2026-09-30。笔记记录团队：小鹏汽车、北京大学、香港大学、UC Berkeley、Princeton、NUS、清华、HKUST (GZ)。代码 [GroundingPI 官方仓库](https://github.com/groundingpi/GroundingPI)；权重 https://huggingface.co/GroundingPI/GroundingPI。

需要继续从现有原论文抽取各基准具体成绩及协议；完整训练数据公开状态、代码核对和模块归属尚缺。

## 来源

2026-10-17，Codex 按用户要求从已有资料整理，未重新联网确认发布状态。

- [已有笔记原文](../review/2026-10-17-资料补充/sources/groundingpi.txt)
- [本次缺项与补充记录](../review/2026-10-17-资料补充/index.html#groundingpi)
