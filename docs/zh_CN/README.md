# NCCL 2.32.6 中文源码阅读地图

|从哪个问题开始|跟随哪份讲解|
|---|---|
|一份输入被切几层？怎么计算 offset？|[通道、圈、chunk、slice，含完整 FP32 算例与变量表](01-data-layout.md)|
|同一块如何在四张卡上归约，最后落到哪个地址？|[五种 Ring 的逐步原语、缓冲布局与其他算法](02-ring.md)|
|相同输入改走 Tree，每棵树的根是谁、每个 rank 处理哪段？|[四节点双树、线程分组与尾块算例](07-tree-allreduce.md)|
|同一个 Ring 末块换 LL 或 LL128，FIFO 上发多长？|[三个协议的容量、尾圈地址、flag 和发送粒度](08-ring-protocols.md)|
|谁创建通道、选算法、打包计划并启动 kernel？|[communicator、Host 调度与 GPU 执行](03-execution.md)|
|AlltoAll、P2P、跨机 IB 怎样继续切分？|[peer 段、4 KiB 对齐、FIFO、QP 和 MR](04-transport.md)|
|要按函数名、类型或路径查定义和分支？|[文件与符号索引](05-index.md) · [离线源码图解](reader.html)|
|如何核验算例、从 Source Insight 或 VS Code 跳图？|[使用与核验](06-verification.md)|

## 按源码目录阅读

|源码位置|负责的问题|可沿着哪个对象继续追踪|
|---|---|---|
|[src/collectives.cc](../../src/collectives.cc)、[src/enqueue](../../src/enqueue)|API 组装、任务分类、调优、排队、计划|ncclInfo → ncclTaskColl / P2P → ncclDevWorkColl 或 ncclDevWorkP2p|
|[src/init.cc](../../src/init.cc)、[src/bootstrap.cc](../../src/bootstrap.cc)、[src/graph](../../src/graph)|rank 建组、交换信息、发现设备路径、为各算法构图|comm->topo → ncclTopoGraph → channel 的 ring/tree|
|[src/tuning](../../src/tuning)、[src/plugin](../../src/plugin)|协议与算法候选、性能模型和插件接口|tuning input → bestTuning → task.algorithm/protocol/nWarps|
|[src/channel.cc](../../src/channel.cc)、[src/include/device.h](../../src/include/device.h)|通道资源、布局计算与设备 work 描述|cells → countLo/Mid/Hi → partOffset/partCount|
|[src/group.cc](../../src/group.cc)、[src/device](../../src/device)|按计划 launch，CUDA 设备侧解析 batch 并执行原语|channelMask → block → channelId → RunWorkColl → Primitives|
|[src/transport](../../src/transport)、[src/proxy.cc](../../src/proxy.cc)、[src/register](../../src/register)|传输选择、异步推进、网络插件、注册|connector / proxyOp → NET request → QP/WR；注册句柄按内存范围关联|
|[src/devcomm](../../src/devcomm)、[src/nccl_device](../../src/nccl_device)、[src/gin](../../src/gin)、[src/rma](../../src/rma)|设备 communicator、设备通信接口、GPU 发起网络与远端内存操作|从对应 API 或 backend 入手，和普通 Ring CPU Proxy 路径分别查阅|
|[src/ras](../../src/ras)、[src/diagnostics](../../src/diagnostics)、[src/misc](../../src/misc)|运行状态、诊断、通用设施|适用于故障分析与资源回收跟踪|
|[plugins](../../plugins)、[bindings](../../bindings)、[contrib](../../contrib)、[docs/examples](../examples)|外部插件示例、语言绑定、扩展与用法|从示例调用公共 API，再接入上面的核心库路径|

基线为 [ad2d192](https://github.com/maxiaoxuxu/nccl/commit/ad2d192c1f279aefcaf340f67e07880b65a1116b)。沿用 [2.12.12 参考分支](https://github.com/maxiaoxuxu/nccl2.12.12.1/tree/codex/nccl-2.12.12-full-source-walkthrough) 的源码内注释、图解、函数步骤索引、编辑器定位和离线阅读方式。本分支的文件、字段、公式和跳转行号对应 2.32.6。
