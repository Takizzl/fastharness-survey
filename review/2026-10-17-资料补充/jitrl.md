# JitRL · 补充草稿

状态：待人工审核。由 Codex 根据已有本地材料整理，尚未替换已审核条目。

## 建议分类

Memory

## 原有缺口

首页 Venue / Result / Team 为空；缺独立论文卡。

## 问题与方法

问题：冻结模型容易重复错误，直接将经验放进提示词不能保证有效利用。方法：完成轨迹后，由 LLM 评价步骤奖励，累计回报并存储状态—动作—回报；遇到相似状态时检索经验、估计动作价值，修正候选动作概率，不更新模型参数。

## 实验与结论边界

论文附录 J.1 / Table 13：使用非 WebArena-Lite 任务积累经验，再固定记忆库测试 165 个留出任务；模型为 Llama-3.1-70B-Instruct。基础模型 12.70%，JitRL 40.88%，WebRL 46.06%。这组固定记忆实验中 JitRL 低于 WebRL，不应套用其他实验的领先结论。

## 基础信息与证据

团队：National University of Singapore。Paper：arXiv:2601.18510v4。已有 meta.json 记录代码为 https://github.com/liushiliushi/JitRL。日期可先写 arXiv 2026.01；本地报告写 ICML 2026，但论文采用 ICML 模板不等于已录用。

## 仍待确认

ICML 录用依据、独立项目主页和代码链接当前可访问性尚需确认。机器人例子是教学迁移示例，不是真机实验。

## 首页候选文案

- Method：检索状态、动作与回报，估计动作价值并修正候选动作概率，模型参数不变。
- Result：WebArena-Lite 留出165任务：12.70%→40.88%

## 本地材料

[导入时的笔记快照](sources/jitrl.txt)

原位置：`papers/jitrl/paper_report.zh.md`。快照保留笔记原文；其中相对图像路径不作为本审阅页的图片入口。
