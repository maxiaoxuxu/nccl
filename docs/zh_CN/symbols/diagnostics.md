# diagnostics 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/diagnostics/device/p2p.cu

[整个文件](../../../src/diagnostics/device/p2p.cu)

- 函数 [diagP2pInitSlotsKernel · L13](../../../src/diagnostics/device/p2p.cu#L13)
- 函数 [diagP2pRemoteWriteKernel · L22](../../../src/diagnostics/device/p2p.cu#L22)
- 函数 [diagP2pVerifyWritesKernel · L29](../../../src/diagnostics/device/p2p.cu#L29)
- 函数 [diagP2pRemoteReadKernel · L35](../../../src/diagnostics/device/p2p.cu#L35)
- 函数 [diagP2pBlocks · L42](../../../src/diagnostics/device/p2p.cu#L42)
- 函数 [ncclDiagP2pInitSlots · L46](../../../src/diagnostics/device/p2p.cu#L46)
- 函数 [ncclDiagP2pRemoteWrite · L55](../../../src/diagnostics/device/p2p.cu#L55)
- 函数 [ncclDiagP2pVerifyWrites · L62](../../../src/diagnostics/device/p2p.cu#L62)
- 函数 [ncclDiagP2pRemoteRead · L69](../../../src/diagnostics/device/p2p.cu#L69)

## src/diagnostics/ib_write_bw.cc

[整个文件](../../../src/diagnostics/ib_write_bw.cc)

- 结构体 [LocalInfo · L56](../../../src/diagnostics/ib_write_bw.cc#L56)
- 函数 [isSafeShellArgument · L67](../../../src/diagnostics/ib_write_bw.cc#L67)
- 结构体 [RankBandwidth · L73](../../../src/diagnostics/ib_write_bw.cc#L73)
- 结构体 [DeviceGroup · L79](../../../src/diagnostics/ib_write_bw.cc#L79)
- 函数 [nodeInventory · L85](../../../src/diagnostics/ib_write_bw.cc#L85)
- 函数 [findGroup · L98](../../../src/diagnostics/ib_write_bw.cc#L98)
- 函数 [rankPosition · L106](../../../src/diagnostics/ib_write_bw.cc#L106)
- 函数 [findPair · L116](../../../src/diagnostics/ib_write_bw.cc#L116)
- 函数 [benchmarkPort · L158](../../../src/diagnostics/ib_write_bw.cc#L158)
- 函数 [toolFailure · L163](../../../src/diagnostics/ib_write_bw.cc#L163)
- 函数 [pluginSupportsIb · L171](../../../src/diagnostics/ib_write_bw.cc#L171)
- 函数 [ibDeviceExists · L181](../../../src/diagnostics/ib_write_bw.cc#L181)
- 函数 [resolveDeviceName · L189](../../../src/diagnostics/ib_write_bw.cc#L189)
- 函数 [segmentCount · L201](../../../src/diagnostics/ib_write_bw.cc#L201)
- 函数 [probeCapabilities · L208](../../../src/diagnostics/ib_write_bw.cc#L208)
- 函数 [discoverLocal · L216](../../../src/diagnostics/ib_write_bw.cc#L216)
- 函数 [buildCommand · L302](../../../src/diagnostics/ib_write_bw.cc#L302)
- 函数 [parseBandwidth · L320](../../../src/diagnostics/ib_write_bw.cc#L320)
- 函数 [computeBandwidthStats · L330](../../../src/diagnostics/ib_write_bw.cc#L330)
- 函数 [allRanksOk · L349](../../../src/diagnostics/ib_write_bw.cc#L349)
- 函数 [syncPair · L359](../../../src/diagnostics/ib_write_bw.cc#L359)
- 函数 [bandwidthOutlier · L372](../../../src/diagnostics/ib_write_bw.cc#L372)
- 函数 [reportBandwidthStats · L376](../../../src/diagnostics/ib_write_bw.cc#L376)
- 结构体 [ServerReadyCtx · L404](../../../src/diagnostics/ib_write_bw.cc#L404)
- 函数 [serverListenLine · L410](../../../src/diagnostics/ib_write_bw.cc#L410)
- 函数 [runPair · L420](../../../src/diagnostics/ib_write_bw.cc#L420)
- 函数 [runSchedule · L498](../../../src/diagnostics/ib_write_bw.cc#L498)
- 函数 [commUsesCrossNic · L539](../../../src/diagnostics/ib_write_bw.cc#L539)
- 函数 [ncclDiagRunIbWriteBw · L548](../../../src/diagnostics/ib_write_bw.cc#L548)

## src/diagnostics/ib_write_bw.h

[整个文件](../../../src/diagnostics/ib_write_bw.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/diagnostics/p2p.cc

[整个文件](../../../src/diagnostics/p2p.cc)

- 枚举 [ncclDiagP2pHandlePath · L28](../../../src/diagnostics/p2p.cc#L28)
- 枚举 [ncclDiagP2pReason · L36](../../../src/diagnostics/p2p.cc#L36)
- 结构体 [ncclDiagP2pEdgeInfo · L53](../../../src/diagnostics/p2p.cc#L53)
- 结构体 [ncclDiagP2pMemDesc · L61](../../../src/diagnostics/p2p.cc#L61)
- 结构体 [ncclDiagP2pEdgeResult · L68](../../../src/diagnostics/p2p.cc#L68)
- 结构体 [ncclDiagP2pWriteObs · L76](../../../src/diagnostics/p2p.cc#L76)
- 结构体 [ncclDiagP2pSummary · L81](../../../src/diagnostics/p2p.cc#L81)
- 结构体 [ncclDiagP2pMapping · L86](../../../src/diagnostics/p2p.cc#L86)
- 函数 [ncclDiagP2pBuildRankSet · L97](../../../src/diagnostics/p2p.cc#L97)
- 函数 [ncclDiagP2pRankToSlot · L106](../../../src/diagnostics/p2p.cc#L106)
- 函数 [ncclDiagP2pSameProcess · L113](../../../src/diagnostics/p2p.cc#L113)
- 函数 [ncclDiagP2pHandleType · L119](../../../src/diagnostics/p2p.cc#L119)
- 函数 [ncclDiagP2pHandleName · L129](../../../src/diagnostics/p2p.cc#L129)
- 函数 [ncclDiagP2pReasonName · L146](../../../src/diagnostics/p2p.cc#L146)
- 函数 [ncclDiagP2pPathName · L171](../../../src/diagnostics/p2p.cc#L171)
- 函数 [ncclDiagP2pIsFabricEdge · L175](../../../src/diagnostics/p2p.cc#L175)
- 函数 [ncclDiagP2pEdgeAdvice · L180](../../../src/diagnostics/p2p.cc#L180)
- 函数 [ncclDiagP2pImportAdvice · L202](../../../src/diagnostics/p2p.cc#L202)
- 函数 [ncclDiagP2pPathType · L217](../../../src/diagnostics/p2p.cc#L217)
- 函数 [ncclDiagP2pSetReason · L229](../../../src/diagnostics/p2p.cc#L229)
- 函数 [ncclDiagP2pSetLocalReason · L233](../../../src/diagnostics/p2p.cc#L233)
- 函数 [ncclDiagP2pCudaSuccess · L241](../../../src/diagnostics/p2p.cc#L241)
- 函数 [ncclDiagP2pNcclSuccess · L248](../../../src/diagnostics/p2p.cc#L248)
- 函数 [ncclDiagP2pLogEdge · L254](../../../src/diagnostics/p2p.cc#L254)
- 函数 [ncclDiagP2pFormatPeerFields · L266](../../../src/diagnostics/p2p.cc#L266)
- 函数 [ncclDiagP2pReport · L275](../../../src/diagnostics/p2p.cc#L275)
- 函数 [ncclDiagP2pBuildGroupSummary · L332](../../../src/diagnostics/p2p.cc#L332)
- 函数 [ncclDiagP2pReportSummary · L345](../../../src/diagnostics/p2p.cc#L345)
- 函数 [ncclDiagP2pReportGroupFailures · L373](../../../src/diagnostics/p2p.cc#L373)
- 函数 [ncclDiagP2pDiscoverLocalEdges · L386](../../../src/diagnostics/p2p.cc#L386)
- 函数 [ncclDiagP2pBuildInboundPeers · L425](../../../src/diagnostics/p2p.cc#L425)
- 函数 [ncclDiagP2pReleaseLocalHandle · L442](../../../src/diagnostics/p2p.cc#L442)
- 函数 [ncclDiagP2pMapSameProcess · L451](../../../src/diagnostics/p2p.cc#L451)
- 函数 [ncclDiagP2pFreeMapping · L493](../../../src/diagnostics/p2p.cc#L493)
- 函数 [ncclDiagP2pImportMappings · L527](../../../src/diagnostics/p2p.cc#L527)
- 函数 [ncclDiagP2pPrepareRemoteOps · L574](../../../src/diagnostics/p2p.cc#L574)
- 函数 [ncclDiagP2pRun · L613](../../../src/diagnostics/p2p.cc#L613)

## src/diagnostics/p2p.h

[整个文件](../../../src/diagnostics/p2p.h)

- 结构体 [ncclDiagP2pSlot · L18](../../../src/diagnostics/p2p.h#L18)
- 结构体 [ncclDiagP2pRemoteOp · L24](../../../src/diagnostics/p2p.h#L24)
- 函数 [ncclDiagP2pWritePattern · L43](../../../src/diagnostics/p2p.h#L43)
- 函数 [ncclDiagP2pReadPattern · L48](../../../src/diagnostics/p2p.h#L48)
