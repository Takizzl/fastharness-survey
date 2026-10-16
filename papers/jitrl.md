# JitRL: Just-In-Time Reinforcement Learning: Continual Learning in LLM Agents Without Gradient Updates

| 项目 | 内容 |
|---|---|
| 模块 | 3. Memory |
| Year / Venue | ICML 2026 Spotlight（官方仓库 README 声明） |
| Paper | https://arxiv.org/abs/2601.18510 |
| Code | https://github.com/liushiliushi/JitRL |
| Website | -（已有材料未确认独立项目主页） |
| Team | National University of Singapore |
| Review | 依据已有资料整合；未核实字段保留待审核 |

## 一句话

检索状态、动作与回报，估计动作价值并修正候选动作概率，模型参数不变。

## 问题

模型参数冻结后容易重复错误，直接提供历史经验不保证能正确利用。

## 方法

问题：冻结模型容易重复错误，直接将经验放进提示词不能保证有效利用。方法：完成轨迹后，由 LLM 评价步骤奖励，累计回报并存储状态—动作—回报；遇到相似状态时检索经验、估计动作价值，修正候选动作概率，不更新模型参数。

## 实验结果

论文附录 J.1 / Table 13：使用非 WebArena-Lite 任务积累经验，再固定记忆库测试 165 个留出任务；模型为 Llama-3.1-70B-Instruct。基础模型 12.70%，JitRL 40.88%，WebRL 46.06%。这组固定记忆实验中 JitRL 低于 WebRL，不应套用其他实验的领先结论。

## 真机结果

不涉及机器人真机实验；具身例子为教学迁移示例。

## 资料补充与边界

团队：National University of Singapore。Paper：arXiv:2601.18510v4。已有 meta.json 记录代码为 [JitRL 官方仓库](https://github.com/liushiliushi/JitRL)。录用信息见下方官网核查。

独立项目主页未确认。机器人例子是教学迁移示例，不是真机实验。

## 来源

初稿依据已有资料整理；本轮联网核查见下方记录。

- [已有笔记原文](../review/2026-10-17-资料补充/sources/jitrl.txt)
- [本次缺项与补充记录](../review/2026-10-17-资料补充/index.html#jitrl)

## 链接核查 · 2026-10-17

[官方仓库](https://github.com/liushiliushi/JitRL) 明确标注 ICML 2026 Spotlight；代码入口正常。独立项目主页未确认。
