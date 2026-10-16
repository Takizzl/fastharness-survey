# PhysMem: Learning Physical Principles from Interaction: Self-Evolving Planning via Test-Time Memory

| 项目 | 内容 |
|---|---|
| 模块 | 3. Memory |
| Year / Venue | arXiv 2026.02 |
| Paper | https://arxiv.org/abs/2602.20323v1 |
| Code | https://github.com/haoyangli16/PhysMem |
| Website | https://phys-mem.github.io/ |
| Team | UC San Diego、Stanford |
| Review | 依据已有资料整合；未核实字段保留待审核 |

## 一句话

从交互中生成并验证物理假设，将可靠原则写入记忆，检索后辅助下一次规划。

## 问题

通用物理知识不足以预测具体场景中的接触动力学，直接检索旧经验在物理条件变化后可能失效。

## 方法

记录观察、动作、结果、上下文和符号状态；由反思模型生成 Avoid / Prefer / Sequence 假设，通过交互结果更新置信度，满足条件后晋升为原则并压缩支持经验。检索已验证原则和活跃假设，以文本提供给 Planner。真机配置：Gemini-3.0-Flash 规划，Qwen3-VL 异步生成假设。

## 实验结果

现有解读未提供可直接入表的仿真量化对照。

## 真机结果

已有报告保留 Figure 6 的连续 12 次真机推球终态：第 8–12 次到达目标区域。这是定性过程展示，不能改写为总体成功率，也不能用最后五次替代完整试验统计。

## 资料补充与边界

Paper：arXiv:2602.20323v1；团队：UC San Diego、Stanford；作者 Haoyang Li、Yang You、Hao Su、Leonidas Guibas。已有报告链接项目页 https://phys-mem.github.io/。

缺可直接入表的量化对照、基线、重复次数和统计范围；会议录用未确认。

## 来源

初稿依据已有资料整理；本轮联网核查见下方记录。

- [已有笔记原文](../review/2026-10-17-资料补充/sources/physmem.txt)
- [本次缺项与补充记录](../review/2026-10-17-资料补充/index.html#physmem)

## 链接核查 · 2026-10-17

[官网](https://phys-mem.github.io/) 的 Code 链接指向 [PhysMem](https://github.com/haoyangli16/PhysMem)。当前官网标题已更新；本卡解读仍依据 [v1](https://arxiv.org/abs/2602.20323v1)，不混入新版实验。
