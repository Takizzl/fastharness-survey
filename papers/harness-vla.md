# Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | 2026 / `arXiv` |
| Paper | https://arxiv.org/abs/2607.08448 |
| Code | https://github.com/RLinf/RPent |
| Website | https://harnessvla.github.io/ |
| Team | 清华（于超、丁文伯组）、港科大、中科院自动化所等 |
| Review | 已入库（与审阅表一致） |

## 一句话

冻结 VLA 只做接触动作，Agent 用固定原语 + 记忆负责定位、移动和重试。

## 问题

VLA 泛化差，换目标、换位置就失败。

## 方法

VLA Policy **冻结**，封装成 **vla_act 原语**，只负责抓取、放置等接触动作。Agent（Codex / Claude Code）读取 RGB-D 与 Robot State，用固定的 **Analytic Primitive**（move_to、rotate、set_gripper、release、navigate）完成定位、移动与释放，接触失败时**重新摆位后再调 VLA**。参考种子上的成功调用序列存为 **Task Memory**，通用规则和失败模式存为 **Global Memory**，新场景中**按当前观测重新定位后复用**。

## 仿真结果

**LIBERO-Pro（8 种扰动 × 100 次）**
- Harness VLA：82.4%
- 原 VLA（π0.5）：50.0%
- 最强基线 RATS：43.8%

**RoboCasa365（50 个任务 × 5 次）**
- Harness VLA：57.2%
- RLDX-1：30.0%

**RoboTwin C2R（50 个任务 × 5 次）**
- Harness VLA：58.4%
- 原 VLA（LingBot-VLA）：50.4%

**补充分析**
- 不用记忆的零样本对比
- VLA 调用次数上限分析
- Flash Mode（不在线规划）：72.6%
- 换 GPT-6 Astra 规划：LIBERO-Pro 92.6%

## 真机结果

**双 Franka**
- 只有演示：换目标、按标记分拣、抓空后重试、倒珠子、擦盘子
- 没报成功率

## 已有资料补充：开发、评测与经验复用

2026-10-17，Codex 根据本地阅读与源码笔记整理，经用户要求整合；以下为补充证据，不替换前述论文实验。

探索阶段为 inbox_write，评测阶段为 read_only。探索结束后合并记忆；根据环境 terminated 决定是否导出成功 recipe，使用最后 reset 之后的记录。当前实现还区分 task-family；不能把发布实现与论文 task/global 两层描述完全等同。

主要 few-shot 成绩使用每任务 seed 0 经验，不能解释为完全未见任务迁移；没有 JitRL 式每步累计回报与动作优势估计。现有汇报中的 Flash 选卡和时间口径需要单独说明，不据此宣称端到端加速倍数。

已有源码笔记定位：rpent/memory/manager.py、robots/libero/robot_spec.py、robots/libero/tools.py、rpent/cli/main.py。当前 merge_memory 不覆盖已有完整任务配对，与论文“可换为更短／可靠序列”描述存在边界。

源码来自本地保存的官方压缩包；不把后续发布实现差异当作论文结果的纠正。

[笔记原文](../review/2026-10-17-资料补充/sources/harness-vla.txt)
