# 贡献规则

这个仓库只收录**经人工阅读原文、核对数据**的内容。

## 每次会议后

1. 在 `meetings/` 新建纪要（复制 [`templates/meeting.md`](templates/meeting.md)），文件名如 `02-第二次会议.md`。
2. 更新 `README.md` 顶部的 **当前主线**：换成本次会议定下的新主线，并把「更新于」链接指向本次纪要。旧主线不用保留在 README，会议纪要里有记录。
3. 在 `CHANGELOG.md` 最上面记一条。

## 新增论文

1. **先进 HTML 审阅表**：新论文先写进审阅表，包含问题、方法、仿真结果、真机结果、团队。
2. **人工审核**：对照原文逐条核对。
3. **再进仓库**：
   - `README.md` 论文表格对应模块下加一行
   - `papers/<简称>.md` 写详情（复制 [`templates/paper.md`](templates/paper.md)）
   - `CHANGELOG.md` 最上面写明本次新增 / 修改了什么
4. 提交 Pull Request，按模板勾选核对项。

## 收录标准

- 团队：大厂实验室（NVIDIA、Google、华为诺亚等）或知名高校团队（清北、复交、港大、港科大、NUS、Stanford、Berkeley、CMU 等）
- 必须和某个模块直接相关

## README 论文表格写法

- **只有一张表**，所有模块共用，保证列宽一致
- 列固定为：Module | Year | Venue | Paper Title | Repository | Method | Result | Team | Website，全部居中（`:---:`）
- Module 只写在该模块第一行，同模块其他行留空；新论文插在对应模块的最后一行之后
- Paper Title 写完整标题；超过 40 个字符的用 `<br>` 从中间断成两行，每行内的空格写成 `&nbsp;`
- Repository：GitHub 星数徽章 `[![GitHub stars](https://img.shields.io/github/stars/<owner>/<repo>.svg?style=social)](https://github.com/<owner>/<repo>)`，没有代码写 `---`
- Method：一句话核心思想
- Result：一个最有代表性的数字，注明真机或基准名
- Website：`[website](链接)`，没有写 `---`
- Venue 只写已确认的会议；Workshop 奖写成 `` `ECCV Workshop`<br>🏆 Best Paper ``
- 数字必须能在论文里找到；从图上读的标「约」
