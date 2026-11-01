# CausGround: Causal Interaction Grounding for Adaptive Embodied Planning

| 项目 | 内容 |
|---|---|
| 模块 | 11. Planner External Augmentation |
| Year / Venue | arXiv 2026.10 |
| Team | 华东师范大学、北京智源人工智能研究院、西北工业大学、中国科学院大学、中国科学院自动化研究所 |
| Paper | https://arxiv.org/abs/2610.29702v1 |
| Code | https://github.com/Intelligent-Interaction/CausGround |
| Website | https://causground.github.io/ |

[HTML汇报](../reports/causground.html) · [返回分类](../README.md#planner-augmentation)

## 一句话

将交互经验组织为动作前置条件、效果及依赖，检索后结合当前视觉状态辅助冻结Planner选择动作；不更新模型参数。

## 问题

Planner不了解环境中动作的前置条件与效果，原始交互轨迹也难以复用。

## 方法

从交互提取动作前置条件与效果，检索因果依赖并结合视觉状态，辅助冻结Planner选动作。

经验按before、action、after、outcome组织，提炼对象属性、关系、动作前置条件与效果。episode开始时检索任务因果子图并固定，当前视觉状态每步更新；主评测不更新Planner参数，也未验证每步向全局知识库写回经验的循环。

## 实验结果

改编VirtualHome平均成功率24.9%→53.3%；RoboCasa闭环规划43.0%→57.0%；SWITCH交互推理准确率25.8%→31.9%。RoboCasa按离线轨迹边界解析高层动作，在各方法均未遇到UNKNOWN的共同子集比较，非完整在线物理控制。

## 真机结果

展示顺序操作案例；未报告重复次数、成功率或真机对照。MLLM解析目标后，从前置条件和效果反推高层动作，已有控制器执行。

来源：原论文v1 §3、§4、表1–4、附录B/C/E；官方知识构建与检索代码；本地已整理阅读报告。

整理与核对：Codex，2026-11-01；索引根据原文和已有笔记整理，未运行作者实验。
