# gin 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/gin/gin_host.cc

[整个文件](../../../src/gin/gin_host.cc)

- 函数 [ncclGetGinType · L28](../../../src/gin/gin_host.cc#L28)
- 函数 [ncclGetRailedGinType · L36](../../../src/gin/gin_host.cc#L36)
- 函数 [ginProgressWriteLock · L44](../../../src/gin/gin_host.cc#L44)
- 函数 [ginProgressWriteUnlock · L50](../../../src/gin/gin_host.cc#L50)
- 函数 [ncclGinProgress · L57](../../../src/gin/gin_host.cc#L57)
- 函数 [ncclGinConnectOnce · L93](../../../src/gin/gin_host.cc#L93)
- 函数 [ncclGinValidateSignalRequest · L248](../../../src/gin/gin_host.cc#L248)
- 函数 [ginAssignSignals · L264](../../../src/gin/gin_host.cc#L264)
- 函数 [ginDevCommSetupWithBackend · L281](../../../src/gin/gin_host.cc#L281)
- 函数 [ncclGinDevCommSetup · L512](../../../src/gin/gin_host.cc#L512)
- 函数 [ncclGinDevCommFree · L553](../../../src/gin/gin_host.cc#L553)
- 函数 [ncclGinHostFinalize · L584](../../../src/gin/gin_host.cc#L584)
- 函数 [ncclGinRegister · L608](../../../src/gin/gin_host.cc#L608)
- 函数 [ncclGinDeregister · L639](../../../src/gin/gin_host.cc#L639)
- 函数 [ncclGinQueryLastError · L652](../../../src/gin/gin_host.cc#L652)

## src/gin/gin_host_proxy.cc

[整个文件](../../../src/gin/gin_host_proxy.cc)

- 结构体 [ginProxyOutstandingOp · L25](../../../src/gin/gin_host_proxy.cc#L25)
- 结构体 [ginProxyHostGpuCtx · L36](../../../src/gin/gin_host_proxy.cc#L36)
- 结构体 [ginProxyCtx · L67](../../../src/gin/gin_host_proxy.cc#L67)
- 函数 [proxyGinAllocOutstandingOp · L95](../../../src/gin/gin_host_proxy.cc#L95)
- 函数 [proxyGinAppendOutstandingOp · L102](../../../src/gin/gin_host_proxy.cc#L102)
- 函数 [proxyGinFreeOutstandingOp · L108](../../../src/gin/gin_host_proxy.cc#L108)
- 函数 [getDmaBufFd · L113](../../../src/gin/gin_host_proxy.cc#L113)
- 函数 [proxyGinPollCompletions · L137](../../../src/gin/gin_host_proxy.cc#L137)
- 函数 [extractSignalVal · L188](../../../src/gin/gin_host_proxy.cc#L188)
- 函数 [extractOp · L195](../../../src/gin/gin_host_proxy.cc#L195)
- 函数 [extractIsStrongSignal · L199](../../../src/gin/gin_host_proxy.cc#L199)
- 函数 [isGfdAvailable · L206](../../../src/gin/gin_host_proxy.cc#L206)
- 函数 [proxyGinPollGfd · L214](../../../src/gin/gin_host_proxy.cc#L214)
- 函数 [mapGfdOpToSignalOp · L267](../../../src/gin/gin_host_proxy.cc#L267)
- 函数 [proxyGinProcessGfd · L280](../../../src/gin/gin_host_proxy.cc#L280)
- 结构体 [ncclGinProxyListenComm · L376](../../../src/gin/gin_host_proxy.cc#L376)
- 函数 [ncclGinProxyGetProperties · L381](../../../src/gin/gin_host_proxy.cc#L381)
- 函数 [ncclGinProxyListen · L388](../../../src/gin/gin_host_proxy.cc#L388)
- 函数 [ncclGinProxyCloseListen · L401](../../../src/gin/gin_host_proxy.cc#L401)
- 结构体 [ncclGinProxyCollComm · L408](../../../src/gin/gin_host_proxy.cc#L408)
- 函数 [ncclGinProxyFlushesAllPutsOnAnySignal · L414](../../../src/gin/gin_host_proxy.cc#L414)
- 函数 [ncclGinProxyConnect · L422](../../../src/gin/gin_host_proxy.cc#L422)
- 函数 [ncclGinProxyCloseColl · L439](../../../src/gin/gin_host_proxy.cc#L439)
- 函数 [ncclGinProxyRegMrSym · L448](../../../src/gin/gin_host_proxy.cc#L448)
- 函数 [ncclGinProxyDeregMrSym · L486](../../../src/gin/gin_host_proxy.cc#L486)
- 函数 [isPowerOfTwo · L493](../../../src/gin/gin_host_proxy.cc#L493)
- 函数 [ncclGinProxyCreateContext · L499](../../../src/gin/gin_host_proxy.cc#L499)
- 函数 [ncclGinProxyDestroyContext · L663](../../../src/gin/gin_host_proxy.cc#L663)
- 函数 [ncclGinProxyProgress · L714](../../../src/gin/gin_host_proxy.cc#L714)
- 函数 [ncclGinProxyQueryLastError · L742](../../../src/gin/gin_host_proxy.cc#L742)
- 函数 [ncclGinProxyInit · L773](../../../src/gin/gin_host_proxy.cc#L773)

## src/gin/proxy_gpucontext/gpucontext.cc

[整个文件](../../../src/gin/proxy_gpucontext/gpucontext.cc)

- 函数 [ncclGinProxyGpuCtx_initCurrent · L11](../../../src/gin/proxy_gpucontext/gpucontext.cc#L11)
- 函数 [ncclGinProxyGpuCtx_init · L29](../../../src/gin/proxy_gpucontext/gpucontext.cc#L29)

## src/gin/proxy_gpucontext/gpucontext.h

[整个文件](../../../src/gin/proxy_gpucontext/gpucontext.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/gin/proxy_gpucontext/gpucontext_v1.cc

[整个文件](../../../src/gin/proxy_gpucontext/gpucontext_v1.cc)

- 函数 [ncclGinProxyGpuCtx_v1_init · L10](../../../src/gin/proxy_gpucontext/gpucontext_v1.cc#L10)

## src/gin/proxy_gpucontext/gpucontext_v1.h

[整个文件](../../../src/gin/proxy_gpucontext/gpucontext_v1.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/gin/proxy_gpucontext/gpucontext_v2.cc

[整个文件](../../../src/gin/proxy_gpucontext/gpucontext_v2.cc)

- 函数 [ncclGinProxyGpuCtx_v2_init · L10](../../../src/gin/proxy_gpucontext/gpucontext_v2.cc#L10)

## src/gin/proxy_gpucontext/gpucontext_v2.h

[整个文件](../../../src/gin/proxy_gpucontext/gpucontext_v2.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。
