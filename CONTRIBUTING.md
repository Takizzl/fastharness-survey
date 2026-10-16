# 贡献规则

收录前核实论文、作者项目页或官方代码。缺乏依据的字段不展示，证据不足的项目暂不收录。

## 每次会议后

1. 在 `meetings/` 新建纪要（复制 [`templates/meeting.md`](templates/meeting.md)），文件名如 `02-第二次会议.md`。
2. 更新 `README.md` 的 **当前主线**（中文，照会议原话精简）：换成本次会议定下的新主线，标题里的会议链接改成本次纪要（`## 当前主线 · [第 N 次会议](...)`）。旧主线不用保留在 README，会议纪要里有记录。
3. 在 `CHANGELOG.md` 最上面记一条。

## 记录想法

想法、思路、讨论直接记到 [`ideas/`](ideas/)，格式随意，不需要审核。

## 新增论文

1. 对照论文、项目页、代码核实方法、指标与团队。
2. 同步更新 `papers/`、README、论文汇总表与 `review/verified-sources.json`。
3. 未证实字段省略，不将 HTTP 200 当作内容核实。
4. 提交前运行格式、测试与外链检查。

## 收录标准

- 团队：大厂实验室（NVIDIA、Google、华为诺亚等）或知名高校团队（清北、复交、港大、港科大、NUS、Stanford、Berkeley、CMU 等）
- 必须和某个模块直接相关

## README 结构

从上到下固定为：居中标题 → 当前主线（中文） → Contents（目录表：Category | Focus | Papers） → 各类别表格。「当前主线」和表格里的 Method、Result 用中文，其余用英文。每次新增论文或会议，同时更新：
- Contents 目录表里对应类别的论文数（新类别要加一行）

## README 论文表格写法

参考 [Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) 的高信息密度写法，改成表格：

- **每个类别单独一张表**，表格上方依次是 `<br>`、空行、`<a id="英文锚点"></a>`、空行、`## 类别名`（`<br>` 让类别之间空一行）（不加图标）；还没有论文的类别写 `TBD.`
- 每张表的表头完全相同（复制已有的表头，表头里的 `&nbsp;` 用来固定列宽，不要增删）
- 列固定为：Paper | Venue | Method | Result | Team，全部居中（`:---:`）
- **所有字段都要填**；确实没有的写 `-`，不要留空
- 新论文插在对应类别表格的最后一行之后
- **Paper**：`**简称**: 标题<br>\[[Paper](arXiv 链接)\] \[[Code](GitHub 链接)\] \[[Website](项目主页)\]`；标题是去掉简称前缀后的部分（没有简称前缀就写完整标题）；只展示已确认的链接，至少包含 Paper 或 Report；各链接都要打开确认过（`python scripts/check_links.py`）
- **Venue**：会议 + 年份，如 `ICML 2026`；只在 arXiv 就写 `arXiv 2026.09`（年月取 arXiv 第一版的提交日期，不是编号）；获奖写 `ECCV 2026 Workshop<br>**Best Paper**`，Workshop 必须注明
- **Method**：中文，从审阅表里人工写好的「方法」浓缩成一句话，写清谁做什么；要让不了解这篇论文的人一眼看懂，领域常识词（VLA、SAM、IK、原语、RL、TAMP 等）直接用，只有论文自创的专有名词换成它实际做的事（如 Failure Risk Score →「给每段动作打出错风险分」），不超过 55 字，不换行
- **Result**：中文，从审阅表的仿真 / 真机结果里挑最能说明效果的一项，写清基准或机器人、规模、对比对象，如「Franka 真机 3 个任务各 10 次：成功率从 53% 提到 83%」；不超过 35 字，不换行
- Method、Result 不用「约、等、多个、一些、若干、大幅、显著、更好」这类模糊说法
- **Team**：主要单位，最多两个，每个单位一行，用 `<br>` 分行，不要用 `/`
- 数字必须能在论文里找到；从图上读的标「约」

## 发布检查

- 首页只保留核实后的条目、简短方法、结果与主要单位。
- 每项必须有可追溯的原始来源，数字保留基准、版本及试验口径。
- 运行 `python scripts/check_format.py`、`python -m unittest discover -s tests` 和 `python scripts/check_links.py`。
