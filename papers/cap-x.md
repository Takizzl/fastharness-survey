# CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy |
| Year / Venue | 2026 / `ICML` |
| Paper | https://arxiv.org/abs/2603.22435 |
| Code | https://github.com/capgym/cap-x |
| Website | https://capgym.github.io |
| Team | NVIDIA、UC Berkeley、Stanford、CMU（Ken Goldberg、Jim Fan 组） |
| Review | 已入库（与审阅表一致） |

## 一句话

只给低级原语 + 多轮执行反馈，Coding Agent 就能超过高层 API 单轮写代码。

## 问题

Code-as-Policy 依赖人写的高层 API，看不出模型本身的能力。

## 方法

Coding Agent 只拿 **Low-level Primitive**（SAM3 分割、IK 求解、Motion Planning），**多轮写代码**：每轮执行后读取 stdout / 报错，以及 VDM（把前后图像变化转成文字），据此改代码。CaP-Agent0 再加入从成功代码中**自动提炼的 Skill Library**，并让**多个模型并行生成、合成一份代码**执行。CaP-RL 用 **GRPO**、以仿真成功为奖励训练 Qwen2.5-Coder-7B。

## 仿真结果

**CaP-Bench（Robosuite 7 个任务 × 100 次，Gemini-3-Pro）**
- 高级 API 单轮：39%
- 低级原语单轮：24%
- 低级原语多轮：54%

**CaP-Agent0**
- 平均 68%，4/7 个任务追平人类专家代码

**CaP-RL（Qwen2.5-Coder-7B）**
- Cube Lift：25% → 80%
- Cube Stack：4% → 44%
- Spill Wipe：30% → 93%

**补充分析**
- 12 个模型的接口层级对比
- 直接回传图像反而降低成功率
- CaP-Agent0 消融（VDM、技能库、多模型并行）
- LIBERO-PRO、BEHAVIOR 扩展评测

## 真机结果

**Franka（2 个任务 × 25 次，CaP-RL 从仿真迁移）**
- Cube Lift：24% → 84%
- Cube Stack：12% → 76%

**零样本演示**
- Franka、AgiBot G1 上找杯下物体、解算式、按电梯等，没报成功率
