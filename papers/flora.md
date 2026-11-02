# Flora: An Open Model Suite for Scaling Robotics Data Engines

| 项目 | 内容 |
|---|---|
| 模块 | 13. Data Annotation |
| Year / Venue | 技术报告 2026.10（2026-10-20） |
| Team | NVIDIA GEAR |
| Paper | https://research.nvidia.com/labs/gear/flora/assets/paper/flora.pdf |
| Code | https://github.com/NVIDIA/Flora |
| Website | https://research.nvidia.com/labs/gear/flora/ |

[返回分类](../README.md#data-annotation)

## 一句话

将人类与机器人操作视频分段、生成带时间戳的动作描述，并标注任务完成度、过程质量及自定义评分项。

## 问题

机器人数据需要动作边界、语言描述和奖励标签；通用模型批量标注成本高，单一标注工具难以覆盖这些需求。

## 方法

三个模型分别定位动作时段、描述动作、评价执行结果与过程，输出时间戳、语言标签及奖励。

| 模块 | 输入 | 输出 |
|---|---|---|
| Flora-TempSeg | 操作视频的重叠窗口 | 动作起止时间与跨窗口延续标记，随后拼接为完整区间 |
| Flora-Captioner | 固定动作区间及前后视觉上下文 | 一条动作指令，包含物体、左右手分工与空间关系 |
| Flora-Rewarder | 任务指令、视频；按需增加评分规则 | 终局1–5分；每0.5秒的正常／次优／失败标签；自定义步骤分数 |

动作描述记录意图，不以描述中出现“抓取”作为抓取成功的证据。过程评分会查看后续画面，因此用于离线轨迹标注，不能直接充当实时反馈。

## 训练与开源

TempSeg基于Qwen3.5-9B，Captioner与Rewarder基于Qwen3.5-27B。三个模型先做SFT；前两者继续GRPO，公开Rewarder采用SFT。官方已公开模型权重和推理代码，仓库未包含训练代码。

## 实验结果

| 基准与指标 | Flora | GPT-6 Astra | 含义 |
|---|---:|---:|---|
| WGO-Bench：分段F1@0.75 ↑ | 50.3 | 46.0 | 100条视频中的动作时间定位 |
| WGO-Bench：联合语义F1@0.75 ↑ | 34.5 | 39.0 | 同时要求时间与描述匹配 |
| RoboRewardBench：MAE×100 ↓ | 40.0 | 55.4 | 2,831条episode的终局评分误差 |
| DenseRewardBench：失败召回率 ↑ | 53.3% | 0.0% | 40条episode、4,861个时间步的失败检测 |

表中数值沿用论文表1、2、4、5的尺度。分段优势不能扩展成所有描述指标都更优；Flora另将约11%的正常步骤误判为失败。

## 真机结果

上述结果评价已有操作视频的标注质量，不是机器人闭环执行成功率。本文未据此证明用Flora奖励训练后能获得多少任务成功率收益。

## 在知识库中的用途

归入“数据标注”，关联“轨迹评价与奖励建模”。可用于给已记录的episode补充动作片段、语言标签与质量评分；它与负责决定下一步动作的Planner分工不同。

## 来源

- [原论文](https://research.nvidia.com/labs/gear/flora/assets/paper/flora.pdf)：§2、§4.1–4.3，表1、2、4、5。
- [官方代码说明](https://github.com/NVIDIA/Flora)：输入输出、开放范围与离线过程评分限制。

整理与核对：Codex，2026-11-02；分类按用户要求，未运行作者实验。
