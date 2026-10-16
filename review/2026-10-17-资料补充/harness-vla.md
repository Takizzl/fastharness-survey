# HarnessVLA · 补充草稿

状态：待人工审核。由 Codex 根据已有本地材料整理，尚未替换已审核条目。

## 建议分类

Code + Policy

## 原有缺口

已有结果和 task/global memory 描述，但缺建库、评测权限及论文和发布实现差异。

## 问题与方法

探索阶段为 inbox_write，评测阶段为 read_only。探索结束后合并记忆；根据环境 terminated 决定是否导出成功 recipe，使用最后 reset 之后的记录。当前实现还区分 task-family；不能把发布实现与论文 task/global 两层描述完全等同。

## 实验与结论边界

主要 few-shot 成绩使用每任务 seed 0 经验，不能解释为完全未见任务迁移；没有 JitRL 式每步累计回报与动作优势估计。现有汇报中的 Flash 选卡和时间口径需要单独说明，不据此宣称端到端加速倍数。

## 基础信息与证据

已有源码笔记定位：rpent/memory/manager.py、robots/libero/robot_spec.py、robots/libero/tools.py、rpent/cli/main.py。当前 merge_memory 不覆盖已有完整任务配对，与论文“可换为更短／可靠序列”描述存在边界。

## 仍待确认

源码来自本地保存的官方压缩包；不把后续发布实现差异当作论文结果的纠正。

## 本地材料

[导入时的笔记快照](sources/harness-vla.txt)

原位置：`papers/harnessvla/精读笔记.md`。快照保留笔记原文；其中相对图像路径不作为本审阅页的图片入口。
