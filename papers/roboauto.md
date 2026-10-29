# RoboAuto：经验初始化、程序开发与 Sim2Real

| 项目 | 内容 |
|---|---|
| 论文全名 | RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding |
| 模块 | 2. Code + Policy |
| Year / Venue | arXiv 2026.10；依据v1，2026-10-27 |
| Paper | https://arxiv.org/abs/2610.36533v1 |
| Code | -；官方项目页未提供代码链接（2026-10-29） |
| Website | https://roboauto-ai.github.io/ |
| Team | Washington University in St. Louis |

[完整阅读笔记](../ideas/roboauto-initialization-sim2real.md) · [HTML汇报](../reports/roboauto.html) · [返回Code + Policy](../README.md#code-policy)

## 问题

仅凭执行反馈改代码，可能持续优化错误的物理假设；缺少当前场景的几何测量，以及阶段效果的验证。

## 一句话

检索物体知识、测量当前场景，分阶段搜索可执行程序，将有效证据与代码保存为知识和技能。

## 方法

Agent检索物体知识、测量场景，分阶段写代码并验证，失败后修改或做诊断实验。

初始物体知识来自LIBERO-90的90段成功示范。仿真Coder为Opus 4.6、1M上下文；阶段共享Python变量和连续场景，失败执行由独立Auditor审核。知识构建VLM与Auditor的具体型号未明确。

原文字段、测量程序、经验与技能更新、各benchmark预算及测试seed见完整笔记。开发可修改程序；留出测试固定最后一版程序，不将测试结果写回知识库。初始技能规模及库维护算法未完整披露。

## 仿真结果

| 基准 | RoboAuto成功率 | 开发预算／设置 | 留出测试／设置 |
|---|---:|---:|---:|
| LIBERO-PRO Object／Spatial／Goal | 98.7%／94.8%／73.7% | 45次 | 50次 |
| LIBERO-PRO Long | 73.4% | 55次 | 50次 |
| LIBERO-Plus | 90.3% | 短任务45次，长任务55次 | 50次 |
| Robosuite | 90.6% | 45次 | 100次 |
| RoboTwin 2.0 | 91.5% | 11次 | 50次 |

RoboTwin 4任务各50次：无保留知识24.5%，使用LIBERO分层知识库91.5%；两组均允许搜索与实验，预算相同。一次rollout是一份程序在一个开发场景执行一次，包含主动换视角与诊断实验的程序执行，不等于修改代码次数。

来源：原论文§4.2–4.3、附录A.1–A.3、B.2、B.4。

## 真机结果

WidowX AI机械臂，D405 RGB-D与C920相机。每任务最多10次搜索rollout，使用Opus 5、1M上下文，人工提供成败反馈与场景重置；固定程序后每任务20次新位置测试。

| 平均阶段完成评分 | RoboAuto | ASPIRE | π0.5 |
|---|---:|---:|---:|
| Sort Balls | 100.00% | 30.00% | 0.00% |
| Stack Dishes | 100.00% | 3.75% | 0.00% |
| Erase Board | 95.83% | 0.00% | 0.00% |

这是阶段完成评分，不是整任务二元成功率。Sim2Real迁移知识与技能后仍有目标任务的真机程序开发；接口与技能逐项适配细节未完整报告。

来源：原论文表1、§4.4及附录F。

整理与核对：Codex，2026-10-29；根据用户提问、原论文全文及附录整理，未运行机器人实验。
