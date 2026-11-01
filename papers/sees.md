# SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation

| 项目 | 内容 |
|---|---|
| 模块 | 7. RSI Projects |
| Year / Venue | arXiv 2026.09 |
| Team | MBZUAI、University of Sydney、University of Oxford、AI2 Robotics、University of Waterloo、University of Melbourne |
| Paper | https://arxiv.org/abs/2609.32698v1 |

[返回分类](../README.md#rsi-projects)

## 一句话

识别长程任务中频繁失败的原子技能，在仿真中构造 RL 任务并更新对应技能类别的共享适配器。

## 问题

长程任务中的高频失败原子技能会阻塞整条任务，人工定位和补示范成本高。

## 方法

统计失败原子技能，恢复仿真状态并生成成功检测函数，用PPO训练技能类别共享LoRA。

11个预定义技能类别分别共享适配器。保存子任务起始状态，历史瓶颈与当前瓶颈一起重新采样训练；仅当验证瓶颈平均成功率提高才注册新checkpoint。不是每个任务单独一个LoRA，也不是直接重放旧成功轨迹。

## 实验结果

表1 GR00T三轮：原子任务47.2%→55.7%，已见组合任务10.2%→13.1%，未见组合任务3.5%→6.1%。表2 LIBERO四套任务均值53.10%→65.40%。

## 真机结果

未报告真机评测；主方法依赖可恢复的仿真状态及成功检测API。

来源：原论文v1 §3、表1/2、图3、附录A；本地精读笔记。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
