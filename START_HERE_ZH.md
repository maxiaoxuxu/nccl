# NCCL 2.32.6 中文源码分析

第一次阅读，先看[数据到底切几层](docs/zh_CN/01-data-layout.md)，再看[四个 rank 怎样把同一块归约并传回所有 GPU](docs/zh_CN/02-ring.md)。两章都能从图直接回到本分支源码。

[四节点双树与尾块](docs/zh_CN/07-tree-allreduce.md) · [全仓目录与按问题导航](docs/zh_CN/README.md) · [初始化到 kernel](docs/zh_CN/03-execution.md) · [跨机与 QP/MR](docs/zh_CN/04-transport.md) · [文件与符号索引](docs/zh_CN/05-index.md) · [单文件离线阅读器](docs/zh_CN/reader.html) · [Source Insight、VS Code 和核验方法](docs/zh_CN/06-verification.md)

GitHub 在线看 Markdown 和 SVG。离线搜索请下载 reader.html，用现代浏览器打开；也可在源码中搜索“中文图解”找到逐项说明。
