# 离线阅读、编辑器定位与核验

**在线**打开 [数据切分](01-data-layout.md) 或 [Ring](02-ring.md)。图为仓库内的 SVG，静态页面即可显示。**离线**保存 [reader.html](reader.html)，用支持 DecompressionStream 的现代 Edge、Chrome 或 Firefox 打开。五章正文、图像、索引及收录的源码均已内嵌。点章节末的源码链接可以直接跳到行；在源码页搜索 runRing 或 ncclComputeCollChannelLayout 并按文件区分同名定义。点击函数步骤中的行号会高亮对应语句。图旁列出可追溯的源码位置。

## 从编辑器选中一行跳图

下载本分支完整源码，保留目录结构。源码注释与基线逐行对应。工具根据“文件路径＋行号”定位；若当前函数没有专门配图，仍显示源码及函数步骤。

|入口|操作|
|---|---|
|VS Code|打开仓库根目录，使用 **Tasks: Run Task**，选择 **NCCL：查看当前源码图解**。任务将当前文件和光标行交给 Python。|
|Source Insight 4|在 Options → Custom Commands 新增命令，将下面示例中的脚本绝对路径换为你的路径，在 Key Assignments 中自行绑定 Ctrl+Alt+G。|
|终端|执行下方命令定位四 rank 算例中“归约完成并转发”的原语。增加 --print-url 可检查定位且不启动浏览器。|

```text
python "D:\nccl\tools\zh_walkthrough\open_diagram.py" --file "%f" --line %l
```

```bash
python3 tools/zh_walkthrough/open_diagram.py --file src/device/all_reduce.h --line 64
```

## 如何复现检查

在保留基线提交 ad2d192 的源码分析分支克隆中，使用 Python 3.9+、Git 和支持 C++17 的主机编译器。Windows 可用 WSL 执行完整检查。独立阅读 HTML 无需 Python 或 CUDA。

```bash
python3 tools/zh_walkthrough/verify.py
```

|检查|验证的内容|
|---|---|
|源码完整性|对基线 src 中每个已跟踪文件，剥离本分支两种注释后重算 Git blob，与基线树逐一比较。新增注释保持源行号，便于版本间交叉定位。|
|源码与图解引用|遍历中文 Markdown 的本地链接，检查目标文件和 #L 行号范围，并解析全部 SVG。|
|离线内容|解压 HTML 内的源码并逐文件比对分支；检查内嵌 SVG 与原图字节一致、专题链接可导航到有效源码行、图示文字与源码注释一致。|
|调用原版函数|CPU 程序从本分支提取 ncclComputeCollChannelLayout、ncclCollCbdPart、ncclSimpleSliceSize、ncclP2pPartBounds、runRing 等真实函数体；host 桩记录 GPU 通信原语的 offset 和有效长度。用四 rank 双通道大例核对 C3 的首地址和两片长度。|
|轮次、尾块与空块|2–8 ranks、12 种长度共 84 组，包括零元素、部分尾圈和多圈。逐跳检查发送与接收地址吻合、每个 rank 对每块归约恰有一次贡献、每个输出元素恰好完成一次；另查 56 组 P2P 分区连续覆盖。|
|Tree 双树与尾块|调用 ncclGetDtree、connectTrees、runTreeSplit 与 runTreeUpDown 的源码函数体，核对四个 rank 的两套父子关系、上行与广播原语、每通道 16 个 chunk 的起点和长度。|
|物理执行边界|上述 CPU 桩刻意只记录路由和区间。GPU 内存序、DMA/RDMA 可见性、CUDA 模板构建、真实 P2P/IB 时延和吞吐量需相应工具链与硬件验证。|

只检查文档可运行 `python3 tools/zh_walkthrough/verify.py --docs-only`。索引覆盖 src 下 C/C++/CUDA 与 nccl.h.in，跳过第三方 nvtx3 头文件。语法索引保留未展开宏和编译条件，各平台特化的实际实例化集合取决于构建；步骤标签表示源文件中的语句位置，调用宏、条件分支和两个同名特化须结合上下文阅读。
