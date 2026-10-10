# 贡献规则

这个仓库只收录**经人工阅读原文、核对数据**的内容。

## 新增论文的流程

1. **先进 HTML 审阅表**：新论文先写进本地的审阅表（`FastHarness相关工作表格.html`，不在仓库里），包含问题、方法、仿真结果、真机结果、团队。
2. **人工审核**：在浏览器里打开审阅表，对照原文逐条核对。
3. **再进仓库**：审核通过后，再同步到仓库：
   - `README.md` 对应模块的表格加一行
   - `papers/<简称>.md` 写详情
   - `CHANGELOG.md` 最上面写明本次新增 / 修改了什么
4. 提交 Pull Request，按模板勾选核对项。

## 收录标准

- 团队：大厂实验室（NVIDIA、Google、华为诺亚等）或知名高校团队（清北、复交、港大、港科大、NUS、Stanford、Berkeley、CMU 等）
- 必须和某个模块直接相关

## README 表格写法

- 列固定为：Year | Venue | Paper Title | Repository | Method | Result | Team | Website，全部居中
- Paper Title 写完整标题，不换行
- Method：一句话核心思想
- Result：一个最有代表性的数字，注明真机或基准名
- Venue 只写已确认的会议；Workshop 奖要写明 Workshop
- 数字必须能在论文里找到；从图上读的标「约」
