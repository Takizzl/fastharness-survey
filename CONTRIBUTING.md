# 贡献规则

这个仓库只收录**经人工阅读原文、核对数据**的内容。可以用 AI 起草，但必须有人逐条核对后才能合入 `main`。

## 新增一篇论文

1. 从 `main` 新建分支，例如 `add/spotter`。
2. 复制 [`templates/paper.md`](templates/paper.md) 到 `papers/<简称>.md`，填写全部字段。
3. 在 [`README.md`](README.md) 对应模块的表格里加一行。
4. 在 [`CHANGELOG.md`](CHANGELOG.md) 最上面写明本次新增 / 修改了什么。
5. 提交 Pull Request，按模板勾选核对项，至少一位审核人批准后合入。

## 收录标准

- 团队：大厂实验室（NVIDIA、Google、华为诺亚等）或知名高校团队（清北、复交、港大、港科大、NUS、Stanford、Berkeley、CMU 等）
- 必须和某个模块直接相关；不相关的放进 PR 讨论，不直接收录

## 写法要求

- **Method**：一句话说清核心思想，30 字左右，不写实验细节
- **Key Result**：只写一个最有代表性的结果，注明仿真 / 真机和对比对象
- 数字必须能在论文正文或表格里找到；从图上读的数字标「约」并注明
- Venue 只写已确认的会议；只在 arXiv 备注里提到的写在 Note 里，标「待确认」
- Workshop 奖要写明是 Workshop，不能写成主会

## Review 状态

- ⏳ 待审核：初稿，数据未复核
- ✅ 已审核：审核人已对照原文核对，并在论文页底部签名和日期
