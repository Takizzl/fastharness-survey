# RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | 2026 / `ECCV Workshop` Best Paper（Agent in the World Workshop，非主会） |
| Paper | https://arxiv.org/abs/2607.18060 |
| Code | https://github.com/markli1hoshipu/RoboHarness（官方仓库，2026-10 时只有项目说明，尚无源码） |
| Website | https://robo-harness.com |
| Team | 华为诺亚方舟实验室 |
| Review | 已入库（与审阅表一致） |

## 一句话

按能力给子任务分配 VLA / RL / TAMP，交接前用 Memory Bridge 把机器人挪到下一个策略熟悉的状态。

## 问题

长任务单一策略做不完，多策略接力时交接容易断。

## 方法

Coding Agent（Codex）作为**调度器**，把 VLA、RL、TAMP 封装成带 **Policy Card**（能力、接口、历史成功率）的技能；**Understanding Skills** 评估当前场景与各策略训练分布的相似度，**按能力分配子任务**；交接时 **Memory Bridge** 检索下一个策略的成功轨迹、估计其熟悉的状态区域，用运动规划把机器人**先挪过去再交接**；持续失败时 **Evolution Skills** 调整路由规则和参数。

> 论文称框架兼容 WAM（world-action model），但实验中实际只用了 VLA、RL、TAMP。

## 仿真结果

**LIBERO-Plus（7 类扰动）**
- RoboHarness：93.2%
- π0.5：85.7%

**LIBERO-LoHo（5 个长任务）**
- RoboHarness：95.2%
- 最强基线 H-WM：64.8%
- π0.5 单独：6.4%

**自建 500 个长任务**
- RoboHarness：86.0%

**补充分析**
- 不同扰动下 VLA / TAMP 调用比例
- 组件消融（Memory Bridge、Evolution、Understanding）

## 真机结果

**UR5e（TAMP + π0.5，135 次）**
- 5 种搭积木结构：67%~93%
- 4 种干扰：67%~87%
- 没和基线比
