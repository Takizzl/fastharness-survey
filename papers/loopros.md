# LoopROS / LoopMaster: A Recursively Self-Evolving Robot Operating System for Agentic Manipulation

| 项目 | 内容 |
|---|---|
| 模块 | 7. RSI Projects |
| Year / Venue | 技术报告 2026.10 |
| Paper | https://loopmaster.ai/loopros/ |
| Code | https://github.com/Boxjod/LoopROS_Client |
| Website | https://loopmaster.ai/ |
| Team | LoopMaster（官网页脚：天津市陆浦智能科技有限公司） |

## 一句话

Agent 读示范与场景，在线规划并执行；把动作反馈组织为任务 Skills，供后续检索复用。

## 问题

机器人执行经验难以转化为后续任务可检索、复用的操作能力。

## 方法

Agent 读示范与场景，在线规划并执行；把动作反馈组织为任务 Skills，供后续检索复用。

## 仿真结果

项目报告的 10 个选定任务，共 100 回合（每任务 10 回合），82 次成功，平均 Score 88.90，失败回合也计入。任务等权；含泛化测试的场景按标准:泛化=2:3 加权。非完整官方 RoboDojo 评测；外部方法可能采用不同设置，不当作同种子或同协议对比。

## 来源可靠性与公开范围

官网直接链接 LoopROS_Client，仓库明确 Paper coming soon。公开的是客户端；规划运行在私有云端 Brain，当前云端 preview 支持 store_laptop_and_headphones，insert_key 为实验性本地适配。官网公开 data.js 的 100 个 episode 可核算统计，但不能据此确认完整系统可独立复现。论文 PDF / arXiv 与云端 Brain 源码未找到。

## 来源

- [项目页面](https://loopmaster.ai/)
- [代码与发布说明](https://github.com/Boxjod/LoopROS_Client)
- [技术报告（非已确认同行评审论文）](https://loopmaster.ai/loopros/)
- [报告原始统计](https://loopmaster.ai/loopros/assets/data.js)
- [客户端公开范围](https://github.com/Boxjod/LoopROS_Client#loopros_client)


## 核对依据

[官网 data.js 100 回合统计；客户端 README](https://loopmaster.ai/loopros/)
