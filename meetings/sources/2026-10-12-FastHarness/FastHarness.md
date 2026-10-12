# FastHarness

## FastHarness第一次会议纪要

**当前主线\-阶段1：**

1. 调研gpt \+ vlm的结合方式相关方法，怎么外挂VLM的，Qwen等VLM尽量做选择题

2. 调研code \+ vla怎么结合起来的，策略如何组织（定位到源码分析）（有没有WAM）

**要求：需要兼容多个llm和下游policy**

3. **浩然**可能考虑阶段2的事，专注memory怎么去做，从LLM的角度迁移

![image\.png](图片和附件/image.png)

**当前比较值得看的工作：**

|模块|论文|问题|方法|可提炼|仿真结果|真机结果|团队|
|---|---|---|---|---|---|---|---|
|1\. VLM1\+ VLM2<br>|[Spotter](https://arxiv.org/abs/2609.36808)<br>|VLA策略执行，恢复能力较差<br>|VLA Policy正常执行；本地VLM（Qwen3\.8\-27B）**监控**，根据执行历史（视觉观测、Action Chunk、Robot State）输出异常风险评分（Failure Risk Score，0–10分），连续检测到异常后**触发恢复**；高级VLM（Astra）接收失败状态与历史信息，进行失败诊断与修复规划，通过固定**Primitive Skill与VLA Policy完成恢复**，并验证恢复结果后交还控制权。|用VLM来进行筛选的思想可以借鉴，但是怎么度量他VLM的判断很重要|**RoboCasa（24 个任务 × 50 次）**<br>• π₀\.₅：64\.3% → 71\.8%<br>• Cosmos Policy：67\.9% → 73\.5%<br>**RoboTwin 2\.0 Hard（50 个任务 × 10 次）**<br>• π₀\.₅：47\.2% → 57\.0%<br>**补充分析：**<br>• 失败恢复分析<br>• 动作评分评估<br>• 效率评估<br>• 消融实验|**Franka（3 个任务 × 10 次）**<br>• π₀\.₅：53% → 83%<br>**任务结果：**<br>• 叠杯：6/10 → 8/10<br>• 方块放置：7/10 → 10/10<br>• 两段任务：3/10 → 7/10<br>|Griffith University（通讯作者）、清华交叉信息院（共同一作）、复旦、腾讯、同济|
|2\. Code \+ Policy<br>|[CaP\-X](https://arxiv.org/abs/2603.22435)（ICML 2026）<br>|现有的CAP方法在机器人控制中的能力没有得到充分验证，依赖高级的API接口，当人工先验被移除、仅使用底层控制原语时，任务性能显著下降<br>|由于高级API完成任务的成功率很好，所以我们只提供低级的原语，让Agent在自迭代的过程中进行由低级原语组合高级原语进行代码合成，提高成功率。其中VDM处理图像来给到结构化的输出，给coding agent来进行代码生成<br>||CaP\-Bench（Robosuite 7 个任务，Gemini\-3\-Pro）：低级原语多轮 54%，高级 API 单轮 39%；CaP\-Agent0 平均 68%，4 个任务追平人类专家；CaP\-RL：Cube Lift 25% → 80%|Franka，CaP\-RL 从仿真迁过来：Cube Lift 24% → 84%，Cube Stack 12% → 76%（各 25 次）；零样本只有演示|NVIDIA、UC Berkeley、Stanford、CMU（Ken Goldberg、Jim Fan 组）|
||[Harness VLA / RPent](https://arxiv.org/abs/2607.08448)|VLA能力有上限，换位置会出错<br>|底层移动这些会由一些固定的原语来控制。把VLA作为一个tools，然后来进行调度，在相应的阶段调度vla\_act\(\)；也会维护一个局部的记忆和一个全局的记忆。<br>||LIBERO\-Pro（800 次）：82\.4%，最强基线 RATS 43\.8%，原 VLA 50\.0%；RoboCasa365（50 个任务）：57\.2%，RLDX\-1 30\.0%；RoboTwin C2R：58\.4%，原 VLA 50\.4%|双 Franka 只有演示视频，没报成功率|清华（于超、丁文伯组）、港科大、中科院自动化所等|
||[PyRUA\-Lean](https://arxiv.org/abs/2610.01939)|Agent 每步都调模型，token 太多|很大程度上把VLA tools和原语移动这些方法放在了代码里面来进行执行。减少Astra调用，主要以代码来执行策略||LIBERO\-PRO \+ RoboTwin 2\.0 \+ RoboCasa365（共 700 个实例）：63\.1% → 71\.7%，其中 LIBERO\-PRO 83% → 94%；两边都做成的任务里，token 少 65%|没做|北大（周大权组）、NUS、NVIDIA|
||[Show\-Harness](https://arxiv.org/abs/2609.10522)|VLM 的知识很难直接变成动作|VLM 每步只选"前移、下降、抓"这类小动作<br>||没做仿真基准|Franka 10 个抓放任务：零样本 89%，π0\.5 39%，最好的基线 57%；换背景、光照、视角：100%，π0\.5 40%；Franka \+ AgileX：93%，π0\.5 41%|NUS Show Lab（Mike Shou 组）|
||[RoboHarness](https://arxiv.org/abs/2607.18060)（ECCV 2026 Workshop 最佳论文）|长任务要多个策略接力，交接容易断|按能力给子任务分配策略，交接前先把机器人挪到下一个策略熟悉的位置||LIBERO\-Plus（7 类扰动）：93\.2%，π0\.5 85\.7%；LIBERO\-LoHo（长任务）：95\.2%，最强基线 64\.8%，π0\.5 单独 6\.4%；自建 500 个长任务：86\.0%|UR5e（TAMP \+ π0\.5），135 次：5 种搭积木结构 67%\~93%，4 种干扰 67%\~87%，没和基线比|华为诺亚方舟实验室|
|3\. Memory|[JitRL](https://arxiv.org/abs/2601.18510)|模型参数冻结后，容易重复之前的错误；把经验放进提示词，也不保证模型有效利用|从相似经验中估计动作价值，修正当前候选动作的选择概率|||||
|4\. 技能增长<br>|[ASPIRE](https://arxiv.org/abs/2607.00272)<br>|修好的经验不会攒下来|看调用记录找到失败处修好，验证有效就存进技能库<br>||对比 CaP\-Agent0：LIBERO\-Pro（30 个任务）18% → 72%；Robosuite（7 个任务）68% → 81%，双臂交接 20% → 92%；BEHAVIOR\-1K（2 个家务任务）拿收音机 56% → 88%；没见过的 LIBERO\-Pro Long 零样本 23% / 38%，基线约 4%|双臂 YAM，3 个任务各 20 次，技能从仿真迁过来：拿汽水罐 13 → 19/20，开抽屉 0 → 11/20，碗放盘 20/20 不变；token 少 2\~9 倍|NVIDIA GEAR（Jim Fan、朱玉可组）、UMich、UIUC、UC Berkeley、CMU|
|5\. 真机迭代恢复|[ENPIRE](https://arxiv.org/abs/2606.19980)（CoRL 2026，待确认）|真机上练策略离不开人|先让 Agent 写好自动复位和判成败，再让它自己改训练代码<br>||Gym\-PushT：约 2 小时到 95%；RoboCasa365（8 个任务 × 40 次）：约 76%，GR00T 约 53%，CaP\-X 约 27%（从图上读的）|8 台双臂 YAM：插销、Push\-T、剪扎带等最终到 99%（允许失败后重试 8 次）；插销约 55% → 95% 用了 4 小时，8 台并行约 40 分钟接近 100%|NVIDIA GEAR、CMU（Guanya Shi 组）、UC Berkeley|
|6\. Harness 迭代边界|[RRSI](https://arxiv.org/abs/2609.24972)|Harness 越改越贴合评测，换任务就不灵|限制每次改多少，留下的改动要过泄漏、噪声、成本三道筛<br>||非机器人基准：进化用 Harvey LAB（法律任务），没见过的 JobBench、GDPval、APEX\-Agents 平均 39\.7 → 43\.6；不加保留端筛选时 Harvey LAB 91\.5，未见任务只有 41\.0；Terminal\-Bench 74\.2 → 80\.2，迁到 SWE\-bench 82\.0 → 83\.8|不涉及|Google Cloud AI Research（Tomas Pfister 组）、UNC、Stanford|



RPG：https://arxiv\.org/pdf/2610\.02204

1. coap的方式无法叠衣服

2. 参考agentic的方式给模型提供memory

3. 当前我们把vla放在下游作为了tools、有没有考虑过其实有时候要增加利用这种pretrain的时候，把coding agent的一些使用tools的能力给vla，让vla能够学习到更好的recovery和推理的能力

4. 系统搭建过程中，希望底层提升动作能力、上层组合复杂的任务

同时上层需要去发现能力的缺失接口，提出学习的新技能、模型训练、能力评测和任务规划

5. 划分成多个部分了

vla是不是更需要多任务指令进行跟随了？任务的指令问题

6. Harness测评关注的问题

**仿真：**

1. 在Benchmark有限的尝试机会里，来进行经验积累然后复用

2. 在其他任务上进行经验积累，然后测试其他Benchmark

**真机：**

1. 先考虑一定的尝试次数（是否需要加示例）看看任务完成情况，同时在真机任务中可以考虑进行多次迭代，保证99%的成功率



