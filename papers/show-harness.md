# Show-Harness: Just a VLM Agent Can Play Robots

| 项目 | 内容 |
|---|---|
| 模块 | 2. Code + Policy（严格说是 VLM 直接控制，不写代码） |
| Year / Venue | 2026 / `arXiv` |
| Paper | https://arxiv.org/abs/2609.10522 |
| Code | https://github.com/showlab/Show-Harness |
| Website | https://showlab.github.io/Show-Harness |
| Team | NUS Show Lab（Mike Shou 组） |
| Review | 已入库（与审阅表一致） |

## 一句话

VLM 每步输出「前移 / 下降 / 抓取」等语义小动作，由解释器转成机器人运动。

## 问题

VLM 难以直接控制细粒度动作。

## 方法

定义一组 **Semantic Action Unit**（MV_FWD / BACK / LEFT / RIGHT / UP / DOWN、ROTATE、GRASP、RELEASE、DONE），VLM 每步根据多视角图像、Proprioception 和动作历史**选一个动作单元**；**Interpreter** 按机器人本体转成固定步长的末端位移（远处 4 cm、近处 2 cm）；配合 Subtask Planning、Failure Recovery 等插件。支持 **Gemini 零样本**与 **Qwen3.5-2B LoRA 微调**两种模式。

## 仿真结果

没做仿真基准，仿真数据只用于训练后迁移到真机。

## 真机结果

**Franka（10 个抓放任务 × 10 次）**
- 零样本：89%
- 微调 2B：86%
- π0.5：39%
- 最好的基线 RATS：57%

**换环境（背景、光照、视角、干扰物）**
- 零样本：100%
- π0.5：40%

**跨本体（Franka + AgileX）**
- 零样本：93%
- π0.5：41%

**补充分析**
- 精细控制、旋转外推、双臂协同
- 推理任务、视频示范学习
- 不同 VLM 与思考强度对比
- 插件消融
