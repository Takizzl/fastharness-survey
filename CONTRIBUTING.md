# 贡献规则

这个仓库只收录**经人工阅读原文、核对数据**的内容。

## 每次会议后

1. 在 `meetings/` 新建纪要（复制 [`templates/meeting.md`](templates/meeting.md)），文件名如 `02-第二次会议.md`。
2. 更新 `README.md` 顶部的 **当前主线**：换成本次会议定下的新主线，并把「更新于」链接指向本次纪要。旧主线不用保留在 README，会议纪要里有记录。
3. 在 `CHANGELOG.md` 最上面记一条。

## 新增论文

1. **先进 HTML 审阅表**：新论文先写进 [`review/论文审阅表.html`](review/论文审阅表.html)，状态标「待审核」，包含问题、方法、仿真结果、真机结果、团队。提交者没给的信息要从原文补齐（规则见 [`AGENTS.md`](AGENTS.md)）。
2. **人工审核**：审核人下载审阅表用浏览器打开，对照原文逐条核对。
3. **再进仓库**：
   - `README.md` 论文表格对应模块下加一行
   - `papers/<简称>.md` 写详情（复制 [`templates/paper.md`](templates/paper.md)）
   - `CHANGELOG.md` 最上面写明本次新增 / 修改了什么
   - 审阅表里该论文状态改成「已入库」
4. 提交 Pull Request，按模板勾选核对项。PR 会自动运行格式检查（`scripts/check_format.py`），不通过不能合并；本地可先运行 `python scripts/check_format.py`。

## 收录标准

- 团队：大厂实验室（NVIDIA、Google、华为诺亚等）或知名高校团队（清北、复交、港大、港科大、NUS、Stanford、Berkeley、CMU 等）
- 必须和某个模块直接相关

## README 结构

从上到下固定为：居中标题和徽章 → 当前主线 → 最近更新 → 目录 → 各类别表格。每次新增论文或会议，同时更新：
- 顶部徽章：`Papers-<论文总数>`、`Meetings-<纪要数>`、`Updated-<日期>`（格式检查会核对前两个）
- 最近更新：最上面加一条 `- **[YYYY.MM.DD]** 做了什么 → [CHANGELOG](CHANGELOG.md)`，只保留最近 5 条
- 目录：对应类别的论文数

## README 论文表格写法

- **每个类别单独一张表**，表格上方依次是 `<a id="英文锚点"></a>`、空行、`## 类别名`；表格下方是 `<div align="right"><a href="#top">回到顶部</a></div>`；还没有论文的类别写「待补。」
- 每张表的表头完全相同（复制已有的表头，里面的 `assets/spacer.png` 占位图用来固定列宽，不要改宽度）
- 列固定为：Year | Venue | Paper Title | Repository | Method | Result | Team | Website，全部居中（`:---:`）
- 新论文插在对应类别表格的最后一行之后
- Paper Title 写完整标题；超过 40 个字符的用 `<br>` 从中间断成两行，每行内的空格写成 `&nbsp;`
- Repository：GitHub 星数徽章 `[![GitHub stars](https://img.shields.io/github/stars/<owner>/<repo>.svg?style=social)](https://github.com/<owner>/<repo>)`，没有代码写 `---`
- Method：一句话核心思想
- Result：一个最有代表性的数字，注明真机或基准名
- Website：`[website](链接)`，没有写 `---`
- Venue 只写已确认的会议；Workshop 奖写成 `` `ECCV Workshop`<br>Best Paper ``
- 数字必须能在论文里找到；从图上读的标「约」
