# How Far Does a Frontier Agent Get as an Embodied Policy?

| 字段 | 内容 |
|---|---|
| 模块 | 12. Perception and Execution |
| Year / Venue | Technical Report 2026 |
| Team | Shanghai AI Lab、SJTU |
| Paper | https://internrobotics.github.io/EBench-Astra-Tech-Report/ |
| Website | https://internrobotics.github.io/EBench-Astra-Tech-Report/ |

[返回分类](../README.md#perception-execution) · [完整阅读HTML](../reports/ebench-astra.html)

## 一句话

Astra读取单条加工示范，根据图像和状态直接输出动作块，与VLA和WAM独立对比。

## 问题

检验前沿Agent在任务变化、长流程和精细接触下的直接控制能力。

## 方法

Astra读取单条加工示范，根据图像和状态直接输出动作块，与VLA和WAM独立对比。下面按输入、路由、执行与评测展开。

更新日期：2026-11-03。依据官方技术报告与本轮问答整理。

## 报告与关注问题

How Far Does a Frontier Agent Get as an Embodied Policy? 团队为上海人工智能实验室，与上海交大、复旦、浙江大学作者。官方页面仍标 arXiv Coming soon，当前以在线报告为原文。

[Report／Website](https://internrobotics.github.io/EBench-Astra-Tech-Report/) · [REA 笔记](rea.md)

**主评测由 Astra 直接控制机器人，与后训练 VLA／WAM 独立比较，没有下游 VLA 接管或修正 Astra 动作。**

## 输入、示范与执行过程

| 阶段 | 输入与处理 | 后续动作 |
|---|---|---|
| 示范加工 | 另一个 high-effort Astra 读取每任务一条训练视频，选择 10–18 关键帧并注释，配状态和动作 | 得到该任务的 ICL 包，同任务跨 seed 复用，不更新参数 |
| 开局 | 任务、接口、总览／左腕／右腕 RGB，EEF、夹爪、底座与当前仿真步数 | high-effort Astra 生成动作调用 |
| 执行 | EEF 路点、夹爪／底座目标、执行时长 | 固定接口插值执行，动作块内开环，无新观测 |
| 下一决策 | 返回请求的相机画面和状态 | Astra 调整动作或重规划，直至结束或预算耗尽 |

不提供深度、物体真值、标定、分割、中间评分或子目标完成信号。没有统一固定的 25 步 Judge 间隔，也没有独立 Router；最大物理步数预算不向模型显示。

物理步数上限与各任务基线一致；没有额外累计 token、工具调用或推理时间上限，因此不是等推理成本对照。来源：报告 §02。

## 仿真结果：VLA／WAM 对照

26 任务、510 个 episode。SR 与部分完成 Score 先在任务内平均，再对任务等权平均，不等于合并所有 episode 算成功比例。

| 模型 | 任务等权 SR | Score |
|---|---:|---:|
| OpenWAM-α | 55.3% | 0.701 |
| AMapbot | 48.9% | 0.639 |
| GPT-6-Astra | 46.7% | 0.654 |
| Qwen-RobotManip | 45.6% | 0.608 |
| π0.5 | 41.4% | 0.544 |
| InternVLA-A1.5 | 34.2% | 0.468 |
| π0 | 33.7% | 0.475 |
| GigaBrain-0.7 | 33.3% | 0.460 |
| Fast-WAM | 25.6% | 0.371 |

AMapbot 纳入总榜，但因缺少公开报告和代码，不在后续详细分析内。Astra 总榜第 3，排除 AMapbot 的八模型分析第 2；低于 OpenWAM-α 8.6 个百分点，高于 π0.5 5.3 个百分点。

| 任务组 | Astra SR | 参考 |
|---|---:|---|
| 11 个短任务 | 73.2% | OpenWAM-α 65.9%；其中 8 个任务为低精度要求 |
| 15 个长任务 | 27.3% | OpenWAM-α 47.6% |
| 7 个桌面灵巧精细任务 | 20.0% | Qwen-RobotManip 50.0% |

七个后训练 VLA／WAM 使用其 EBench 榜单报告值，训练数据为 26 任务、6,600 条 episode；Astra 每任务读一条加工示范，无参数更新，适配方式不同。来源：§01–§04。

## 恢复与上下游协作

苹果运输案例中，Astra 根据图像与夹爪间隙推断滑落，重新观察和抓取，改用固定底座、机械臂运输。这是同会话重规划，没有 VLA 接管或外部记忆参数更新。

“Agent 做探索和目标修订、局部控制器做高频精细接触”属于未来方向；报告讨论滑落／阻力中断和交接协议，但主评测没有验证这套混合 Router。

没有独立 Router 的调用次数，也未给出统一逐模块 token 消耗表，不能从案例补造总量。来源：§04–§05、§07。

## 与 REA 的区别及相关问题

| 问题 | EBench-Astra | REA |
|---|---|---|
| 大模型参与方式 | 每次决策直接产生动作目标 | 依实验生成程序、选择候选、视觉检查或后台建议 |
| 下游执行器 | 固定 EEF／夹爪／底座接口 | 固定程序、VLA、原生技能或在线 Code |
| VLA 中途接管 | 主评测没有 | Aloha 异步有；RoboTwin 86% 只在开局选择 |
| 示范与记忆 | 单条加工示范同任务复用，无参数更新 | 路由记忆为开发统计；学习式选择器另有训练 |

- 已确认：灵活恢复不等于精细接触控制；报告分别呈现短流程优势和长任务、精细对齐不足。
- 尚未由主评测回答：如何触发交接和中断，以及混合系统在等端到端预算下能否同时提高成功率与效率。


## 真机结果

本报告主评测为EBench仿真，没有单列真机机器人成功率实验。

## 来源

[在线报告§01–04、§07；任务等权指标与物理步数／模型预算条件](https://internrobotics.github.io/EBench-Astra-Tech-Report/)。Codex依据原文、官方实现与用户阅读问答整理；阅读判断单列。
