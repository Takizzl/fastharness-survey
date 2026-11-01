# SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation

| 项目 | 内容 |
|---|---|
| 模块 | 12. Perception and Execution |
| Year / Venue | arXiv 2026.10 |
| Team | 复旦大学、新加坡管理大学 |
| Paper | https://arxiv.org/abs/2610.12457v1 |
| Website | https://emilia113.github.io/SpatialHarness/ |

[返回分类](../README.md#perception-execution)

## 一句话

维护与执行同步的模拟场景，为冻结策略渲染补充视角，改善精细操作中的空间可见性。

## 问题

固定物理相机可能遮挡精细操作所需的空间关系，限制冻结策略的动作判断。

## 方法

维护与真实执行同步的仿真场景，渲染互补视角并提供物体位姿，辅助冻结Astra控制。

使用CAD、深度和相机标定初始化场景；区分静止、持物及抓放转换同步模式。执行前选择两个虚拟视角，执行中更新场景。整套系统同时增加虚拟图、物体位姿和同步计算，论文未分离各输入的独立贡献。代码主页标注Coming soon，不按已发布实现填写Code。

## 实验结果

仿真场景用于在线同步与渲染，主评测是真机操作，不能将渲染场景视为独立仿真benchmark。

## 真机结果

Franka Research 3，4任务×每方法15次，共120次。基线11/60、SpatialHarness50/60；插头26.67%→66.67%，孔套柱0%→100%。

来源：原论文v1 §3–5、图2/4–6；官方项目页；本地实验与涨点笔记。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
