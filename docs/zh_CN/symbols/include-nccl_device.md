# include-nccl_device 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/include/nccl_device/barrier.h

[整个文件](../../../src/include/nccl_device/barrier.h)

- 结构体 [ncclBarrierSession · L19](../../../src/include/nccl_device/barrier.h#L19)

## src/include/nccl_device/cft.h

[整个文件](../../../src/include/nccl_device/cft.h)

- 枚举 [ncclMemProxyType · L15](../../../src/include/nccl_device/cft.h#L15)
- 枚举 [ncclMemFenceScope · L20](../../../src/include/nccl_device/cft.h#L20)
- 结构体 [ncclCft · L35](../../../src/include/nccl_device/cft.h#L35)

## src/include/nccl_device/cft_barrier.h

[整个文件](../../../src/include/nccl_device/cft_barrier.h)

- 结构体 [ncclCftBarrierSession · L17](../../../src/include/nccl_device/cft_barrier.h#L17)

## src/include/nccl_device/comm.h

[整个文件](../../../src/include/nccl_device/comm.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/coop.h

[整个文件](../../../src/include/nccl_device/coop.h)

- 结构体 [ncclCoopTile · L21](../../../src/include/nccl_device/coop.h#L21)
- 函数 [thread_rank · L24](../../../src/include/nccl_device/coop.h#L24)
- 函数 [size · L27](../../../src/include/nccl_device/coop.h#L27)
- 函数 [num_threads · L30](../../../src/include/nccl_device/coop.h#L30)
- 函数 [laneMask · L34](../../../src/include/nccl_device/coop.h#L34)
- 函数 [sync · L37](../../../src/include/nccl_device/coop.h#L37)
- 结构体 [ncclCoopLanes · L49](../../../src/include/nccl_device/coop.h#L49)
- 函数 [ncclCoopLanes · L52](../../../src/include/nccl_device/coop.h#L52)
- 函数 [thread_rank · L54](../../../src/include/nccl_device/coop.h#L54)
- 函数 [size · L57](../../../src/include/nccl_device/coop.h#L57)
- 函数 [num_threads · L60](../../../src/include/nccl_device/coop.h#L60)
- 函数 [sync · L63](../../../src/include/nccl_device/coop.h#L63)
- 结构体 [ncclCoopWarpSpan · L73](../../../src/include/nccl_device/coop.h#L73)
- 函数 [thread_rank · L78](../../../src/include/nccl_device/coop.h#L78)
- 函数 [size · L81](../../../src/include/nccl_device/coop.h#L81)
- 函数 [num_threads · L84](../../../src/include/nccl_device/coop.h#L84)
- 函数 [sync · L88](../../../src/include/nccl_device/coop.h#L88)
- 结构体 [ncclCoopCta · L96](../../../src/include/nccl_device/coop.h#L96)
- 函数 [thread_rank · L97](../../../src/include/nccl_device/coop.h#L97)
- 函数 [size · L100](../../../src/include/nccl_device/coop.h#L100)
- 函数 [num_threads · L103](../../../src/include/nccl_device/coop.h#L103)
- 函数 [sync · L106](../../../src/include/nccl_device/coop.h#L106)
- 函数 [ncclCoopGetLaneMask · L114](../../../src/include/nccl_device/coop.h#L114)
- 函数 [ncclCoopGetLaneMask · L117](../../../src/include/nccl_device/coop.h#L117)
- 函数 [ncclCoopGetLaneMask · L120](../../../src/include/nccl_device/coop.h#L120)
- 函数 [ncclCoopGetLaneMask · L123](../../../src/include/nccl_device/coop.h#L123)
- 函数 [ncclCoopIsThread · L132](../../../src/include/nccl_device/coop.h#L132)
- 函数 [ncclCoopIsThread · L135](../../../src/include/nccl_device/coop.h#L135)
- 函数 [ncclCoopIsThread · L138](../../../src/include/nccl_device/coop.h#L138)
- 函数 [ncclCoopIsThread · L141](../../../src/include/nccl_device/coop.h#L141)
- 函数 [ncclCoopWithinWarp · L148](../../../src/include/nccl_device/coop.h#L148)
- 函数 [ncclCoopWithinWarp · L151](../../../src/include/nccl_device/coop.h#L151)
- 函数 [ncclCoopWithinWarp · L154](../../../src/include/nccl_device/coop.h#L154)
- 函数 [ncclCoopWithinWarp · L157](../../../src/include/nccl_device/coop.h#L157)
- 函数 [ncclCoopBcast · L187](../../../src/include/nccl_device/coop.h#L187)
- 函数 [ncclCoopBcast · L199](../../../src/include/nccl_device/coop.h#L199)
- 函数 [ncclCoopBcast_WarpSpan_stash · L213](../../../src/include/nccl_device/coop.h#L213)
- 函数 [ncclCoopBcast · L219](../../../src/include/nccl_device/coop.h#L219)
- 函数 [ncclCoopBcast_Cta_stash · L227](../../../src/include/nccl_device/coop.h#L227)
- 函数 [ncclCoopBcast · L233](../../../src/include/nccl_device/coop.h#L233)

## src/include/nccl_device/core.h

[整个文件](../../../src/include/nccl_device/core.h)

- 结构体 [ncclTeam · L52](../../../src/include/nccl_device/core.h#L52)
- 结构体 [ncclTeamTagWorld · L62](../../../src/include/nccl_device/core.h#L62)
- 结构体 [ncclTeamTagLsa · L63](../../../src/include/nccl_device/core.h#L63)
- 结构体 [ncclTeamTagRail · L64](../../../src/include/nccl_device/core.h#L64)

## src/include/nccl_device/flow.h

[整个文件](../../../src/include/nccl_device/flow.h)

- 函数 [ncclFlowThreadPart · L26](../../../src/include/nccl_device/flow.h#L26)
- 结构体 [ncclFlowNullPtrFn · L39](../../../src/include/nccl_device/flow.h#L39)
- 函数 [operator() · L40](../../../src/include/nccl_device/flow.h#L40)
- 结构体 [ncclFlowSendTag · L46](../../../src/include/nccl_device/flow.h#L46)
- 函数 [ncclFlowSendTag · L50](../../../src/include/nccl_device/flow.h#L50)
- 结构体 [ncclFlowRecvTag · L57](../../../src/include/nccl_device/flow.h#L57)
- 函数 [ncclFlowRecvTag · L61](../../../src/include/nccl_device/flow.h#L61)
- 结构体 [ncclFlowConfig&lt;0&gt; · L109](../../../src/include/nccl_device/flow.h#L109)
- 结构体 [ncclFlowConfig · L119](../../../src/include/nccl_device/flow.h#L119)
- 结构体 [ncclFlowProcessor · L152](../../../src/include/nccl_device/flow.h#L152)
- 函数 [process · L187](../../../src/include/nccl_device/flow.h#L187)
- 函数 [close · L194](../../../src/include/nccl_device/flow.h#L194)
- 结构体 [ncclFlowProcessor · L219](../../../src/include/nccl_device/flow.h#L219)
- 函数 [ncclFlowProcessor · L225](../../../src/include/nccl_device/flow.h#L225)

## src/include/nccl_device/gin.h

[整个文件](../../../src/include/nccl_device/gin.h)

- 结构体 [ncclGin_None · L21](../../../src/include/nccl_device/gin.h#L21)
- 结构体 [ncclGin_StrongVASignalInc · L24](../../../src/include/nccl_device/gin.h#L24)
- 结构体 [ncclGin_WeakVASignalInc · L29](../../../src/include/nccl_device/gin.h#L29)
- 结构体 [ncclGin_VASignalInc · L34](../../../src/include/nccl_device/gin.h#L34)
- 结构体 [ncclGin_StrongVASignalAdd · L40](../../../src/include/nccl_device/gin.h#L40)
- 结构体 [ncclGin_WeakVASignalAdd · L46](../../../src/include/nccl_device/gin.h#L46)
- 结构体 [ncclGin_VASignalAdd · L52](../../../src/include/nccl_device/gin.h#L52)
- 结构体 [ncclGin_StrongSignalAdd · L59](../../../src/include/nccl_device/gin.h#L59)
- 结构体 [ncclGin_WeakSignalAdd · L64](../../../src/include/nccl_device/gin.h#L64)
- 结构体 [ncclGin_SignalAdd · L69](../../../src/include/nccl_device/gin.h#L69)
- 结构体 [ncclGin_StrongSignalInc · L76](../../../src/include/nccl_device/gin.h#L76)
- 结构体 [ncclGin_WeakSignalInc · L83](../../../src/include/nccl_device/gin.h#L83)
- 结构体 [ncclGin_SignalInc · L88](../../../src/include/nccl_device/gin.h#L88)
- 结构体 [ncclGin_CounterInc · L96](../../../src/include/nccl_device/gin.h#L96)
- 结构体 [ncclGin_WeakCounterInc · L101](../../../src/include/nccl_device/gin.h#L101)
- 结构体 [ncclGin_DescriptorSmem · L105](../../../src/include/nccl_device/gin.h#L105)
- 结构体 [ncclGin_SegmentDevice · L110](../../../src/include/nccl_device/gin.h#L110)
- 结构体 [ncclGin_SegmentMixed · L111](../../../src/include/nccl_device/gin.h#L111)
- 结构体 [ncclGin_SegmentHostNuma · L112](../../../src/include/nccl_device/gin.h#L112)
- 结构体 [ncclGin_BackendMask · L123](../../../src/include/nccl_device/gin.h#L123)

## src/include/nccl_device/gin/efa_gda/gin_efa_gda.h

[整个文件](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h)

- 枚举 [efaGdaRdmaOp · L68](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L68)
- 函数 [scopedAtomicLoad · L76](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L76)
- 函数 [scopedAtomicAdd · L82](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L82)
- 函数 [hwCounterLoad · L97](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L97)
- 函数 [ringDoorbell · L121](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L121)
- 结构体 [RdmaSgeEncoder · L136](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L136)
- 函数 [encode · L141](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L141)
- 结构体 [PutValuePayloadEncoder · L150](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L150)
- 函数 [PutValuePayloadEncoder · L153](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L153)
- 函数 [encode · L155](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L155)
- 函数 [postPutThread · L167](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L167)
- 结构体 [PostRdmaOpModeTag · L220](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L220)
- 函数 [postRdmaOpImpl · L226](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L226)
- 函数 [postRdmaOpImpl · L235](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L235)
- 函数 [postRdmaOp · L439](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L439)
- 函数 [putImplMode · L449](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L449)
- 函数 [putImpl · L686](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L686)
- 函数 [getImplMode · L722](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L722)
- 函数 [getImpl · L769](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L769)
- 函数 [putValueImplMode · L786](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L786)
- 函数 [putValueImpl · L855](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L855)
- 结构体 [ncclGinApi_Put&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L968](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L968)
- 函数 [call · L970](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L970)
- 结构体 [ncclGinApi_PutValue&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L985](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L985)
- 函数 [call · L987](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L987)
- 结构体 [ncclGinApi_Get&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1000](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1000)
- 函数 [call · L1002](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1002)
- 结构体 [ncclGinApi_FlushAsync&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1014](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1014)
- 函数 [call · L1015](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1015)
- 结构体 [ncclGinApi_Wait&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1029](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1029)
- 函数 [call · L1030](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1030)
- 函数 [call · L1040](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1040)
- 结构体 [ncclGinApi_Flush&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1057](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1057)
- 函数 [call · L1059](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1059)
- 结构体 [ncclGinApi_SupportsStrongSignal&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1078](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1078)
- 函数 [call · L1079](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1079)
- 结构体 [ncclGinApi_FlushesAllPutsOnAnySignal&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1086](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1086)
- 函数 [call · L1089](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1089)
- 结构体 [ncclGinApi_BarrierOptions&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1096](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1096)
- 函数 [call · L1098](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1098)
- 结构体 [ncclGinApi_GetSignalPtr&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1106](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1106)
- 函数 [call · L1107](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1107)
- 结构体 [ncclGinApi_GetCounterPtr&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1117](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1117)
- 函数 [call · L1118](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1118)
- 结构体 [ncclGinApi_ResetSignal&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1128](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1128)
- 函数 [call · L1129](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1129)
- 结构体 [ncclGinApi_ResetCounter&lt;NCCL_NET_DEVICE_GIN_EFA_GDA&gt; · L1144](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1144)
- 函数 [call · L1145](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda.h#L1145)

## src/include/nccl_device/gin/efa_gda/gin_efa_gda_dev.h

[整个文件](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_dev.h)

- 结构体 [nccl_ofi_gin_gdaki_dev_endpoint_handle · L23](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_dev.h#L23)
- 结构体 [nccl_ofi_gin_gdaki_dev_counter_handle · L99](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_dev.h#L99)
- 结构体 [nccl_ofi_gin_gdaki_dev_handle · L120](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_dev.h#L120)
- 结构体 [nccl_ofi_gin_gdaki_mr_peer · L187](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_dev.h#L187)
- 结构体 [nccl_ofi_gin_gdaki_mr_handle · L193](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_dev.h#L193)

## src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h

[整个文件](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h)

- 函数 [word · L29](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h#L29)
- 函数 [bit · L32](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h#L32)
- 函数 [inWord · L35](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h#L35)
- 结构体 [EfaGdaWriteWqeRegs · L88](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h#L88)
- 函数 [EfaGdaWriteWqeRegs · L91](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h#L91)
- 函数 [storeMmio · L107](../../../src/include/nccl_device/gin/efa_gda/gin_efa_gda_wqe.h#L107)

## src/include/nccl_device/gin/gdaki/gin_gdaki.h

[整个文件](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h)

- 结构体 [ncclGinGdakiRequest · L29](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L29)
- 函数 [docaOptFlagsFromGinOptFlags · L44](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L44)
- 函数 [putImplMode · L52](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L52)
- 函数 [putImpl · L131](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L131)
- 函数 [putValueImplMode · L158](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L158)
- 函数 [putValueImpl · L205](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L205)
- 函数 [atomicMaxAtIndex · L233](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L233)
- 函数 [loadAtIndex · L248](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L248)
- 函数 [getImplMode · L261](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L261)
- 函数 [getImpl · L287](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L287)
- 函数 [flushAsyncImpl · L308](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L308)
- 函数 [waitImpl · L381](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L381)
- 函数 [flushImplMode · L441](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L441)
- 函数 [flushImpl · L452](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L452)
- 结构体 [ncclGinApi_Get&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L484](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L484)
- 函数 [call · L486](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L486)
- 结构体 [ncclGinApi_FlushAsync&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L495](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L495)
- 函数 [call · L496](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L496)
- 结构体 [ncclGinApi_Wait&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L516](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L516)
- 函数 [call · L517](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L517)
- 函数 [call · L532](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L532)
- 结构体 [ncclGinApi_Put&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L550](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L550)
- 函数 [call · L552](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L552)
- 结构体 [ncclGinApi_PutValue&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L578](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L578)
- 函数 [call · L580](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L580)
- 结构体 [ncclGinApi_SupportsStrongSignal&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L604](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L604)
- 函数 [call · L605](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L605)
- 结构体 [ncclGinApi_ResetCounter&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L611](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L611)
- 函数 [call · L612](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L612)
- 结构体 [ncclGinApi_ResetSignal&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L620](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L620)
- 函数 [call · L621](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L621)
- 结构体 [ncclGinApi_GetCounterPtr&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L634](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L634)
- 函数 [call · L635](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L635)
- 结构体 [ncclGinApi_GetSignalPtr&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L643](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L643)
- 函数 [call · L644](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L644)
- 结构体 [ncclGinApi_FlushesAllPutsOnAnySignal&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L652](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L652)
- 函数 [call · L656](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L656)
- 结构体 [ncclGinApi_BarrierOptions&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L662](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L662)
- 函数 [call · L663](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L663)
- 结构体 [ncclGinApi_Flush&lt;NCCL_NET_DEVICE_GIN_GDAKI&gt; · L669](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L669)
- 函数 [call · L671](../../../src/include/nccl_device/gin/gdaki/gin_gdaki.h#L671)

## src/include/nccl_device/gin/gdaki/gin_gdaki_device_host_common.h

[整个文件](../../../src/include/nccl_device/gin/gdaki/gin_gdaki_device_host_common.h)

- 结构体 [ncclGinGdakiGlobalGPUBufferTable · L18](../../../src/include/nccl_device/gin/gdaki/gin_gdaki_device_host_common.h#L18)
- 结构体 [ncclGinGdakiGPUContext · L25](../../../src/include/nccl_device/gin/gdaki/gin_gdaki_device_host_common.h#L25)
- 结构体 [ncclGinGdakiMemHandle · L39](../../../src/include/nccl_device/gin/gdaki/gin_gdaki_device_host_common.h#L39)

## src/include/nccl_device/gin/gin_device_api.h

[整个文件](../../../src/include/nccl_device/gin/gin_device_api.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/gin/gin_device_common.h

[整个文件](../../../src/include/nccl_device/gin/gin_device_common.h)

- 枚举 [ncclGinOptFlags · L48](../../../src/include/nccl_device/gin/gin_device_common.h#L48)
- 枚举 [ncclGinResourceSharingMode · L66](../../../src/include/nccl_device/gin/gin_device_common.h#L66)
- 结构体 [ncclGinCtx · L72](../../../src/include/nccl_device/gin/gin_device_common.h#L72)
- 结构体 [ncclGinCtx_M · L83](../../../src/include/nccl_device/gin/gin_device_common.h#L83)
- 结构体 [ncclGinDescriptorSmem · L85](../../../src/include/nccl_device/gin/gin_device_common.h#L85)
- 枚举 [ncclGinSignalType · L89](../../../src/include/nccl_device/gin/gin_device_common.h#L89)
- 结构体 [ncclGinSignalDescriptor · L95](../../../src/include/nccl_device/gin/gin_device_common.h#L95)
- 结构体 [ncclGinApi_Wait · L114](../../../src/include/nccl_device/gin/gin_device_common.h#L114)
- 结构体 [ncclGinApi_FlushAsync · L123](../../../src/include/nccl_device/gin/gin_device_common.h#L123)
- 结构体 [ncclGinApi_Get · L129](../../../src/include/nccl_device/gin/gin_device_common.h#L129)
- 结构体 [ncclGinApi_Put · L137](../../../src/include/nccl_device/gin/gin_device_common.h#L137)
- 结构体 [ncclGinApi_PutValue · L148](../../../src/include/nccl_device/gin/gin_device_common.h#L148)
- 结构体 [ncclGinOffsetPtr · L157](../../../src/include/nccl_device/gin/gin_device_common.h#L157)
- 结构体 [ncclGinApi_GetSignalPtr · L163](../../../src/include/nccl_device/gin/gin_device_common.h#L163)
- 结构体 [ncclGinApi_GetCounterPtr · L168](../../../src/include/nccl_device/gin/gin_device_common.h#L168)
- 结构体 [ncclGinApi_ResetSignal · L173](../../../src/include/nccl_device/gin/gin_device_common.h#L173)
- 结构体 [ncclGinApi_ResetCounter · L178](../../../src/include/nccl_device/gin/gin_device_common.h#L178)
- 结构体 [ncclGinApi_Flush · L183](../../../src/include/nccl_device/gin/gin_device_common.h#L183)
- 结构体 [ncclGinApi_SupportsStrongSignal · L195](../../../src/include/nccl_device/gin/gin_device_common.h#L195)
- 结构体 [ncclGinApi_FlushesAllPutsOnAnySignal · L202](../../../src/include/nccl_device/gin/gin_device_common.h#L202)
- 结构体 [ncclGinApi_BarrierOptions · L207](../../../src/include/nccl_device/gin/gin_device_common.h#L207)

## src/include/nccl_device/gin/gin_device_host_common.h

[整个文件](../../../src/include/nccl_device/gin/gin_device_host_common.h)

- 枚举 [ncclGinSignalOp_t · L20](../../../src/include/nccl_device/gin/gin_device_host_common.h#L20)

## src/include/nccl_device/gin/gpi/gin_gpi.h

[整个文件](../../../src/include/nccl_device/gin/gpi/gin_gpi.h)

- 结构体 [ncclGinGpiRequest · L38](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L38)
- 函数 [gpi_gpu_channel_get_ptr · L48](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L48)
- 函数 [gpi_flush_tickets_get_ptr · L52](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L52)
- 函数 [gpi_atomic_add · L57](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L57)
- 函数 [gpi_gpu_channel_read_ci_shadow · L72](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L72)
- 函数 [gpi_gpu_channel_write_ci_shadow · L87](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L87)
- 函数 [gpi_gpu_channel_get_pi · L98](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L98)
- 函数 [gpi_gpu_channel_get_idx · L117](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L117)
- 函数 [gpi_gpu_channel_set_gfd_flag · L122](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L122)
- 函数 [gpi_gpu_channel_get_counter_value · L130](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L130)
- 函数 [gpi_gpu_channel_reset_signal · L134](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L134)
- 函数 [gpi_gpu_channel_reset_signal_flag · L139](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L139)
- 函数 [gpi_gpu_channel_reset_counter · L145](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L145)
- 函数 [gpi_gpu_channel_get_signal_value · L151](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L151)
- 函数 [gpi_gpu_channel_is_signal_flags · L156](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L156)
- 函数 [__as_ptr_smem · L163](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L163)
- 函数 [__as_ptr_gmem · L168](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L168)
- 函数 [TmaCopy · L173](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L173)
- 函数 [TmaCommit · L181](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L181)
- 函数 [TmaWait · L185](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L185)
- 函数 [gpi_gpu_channel_post_gfd_tma · L190](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L190)
- 函数 [gpi_gpu_channel_post_gfd_thread · L211](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L211)
- 函数 [gpi_gpu_build_data_transfer_gfd · L241](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L241)
- 函数 [gpi_gpu_build_inline_data_transfer_gfd · L260](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L260)
- 函数 [gpi_gpu_build_control_gfd · L279](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L279)
- 函数 [gpi_gpu_build_pe_flush_gfd · L287](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L287)
- 函数 [gpi_gpu_channel_post_gfd · L301](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L301)
- 函数 [GpiFenceAcquireSys · L309](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L309)
- 函数 [GpiFenceRelease · L314](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L314)
- 函数 [putImplMode · L326](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L326)
- 函数 [putValueImplMode · L407](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L407)
- 函数 [flushImplMode · L519](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L519)
- 结构体 [ncclGinApi_Put&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L568](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L568)
- 函数 [call · L570](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L570)
- 结构体 [ncclGinApi_PutValue&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L600](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L600)
- 函数 [call · L602](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L602)
- 结构体 [ncclGinApi_SupportsStrongSignal&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L629](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L629)
- 函数 [call · L630](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L630)
- 结构体 [ncclGinApi_ResetCounter&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L636](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L636)
- 函数 [call · L637](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L637)
- 结构体 [ncclGinApi_ResetSignal&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L658](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L658)
- 函数 [call · L659](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L659)
- 结构体 [ncclGinApi_GetCounterPtr&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L694](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L694)
- 函数 [call · L695](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L695)
- 结构体 [ncclGinApi_GetSignalPtr&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L703](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L703)
- 函数 [call · L704](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L704)
- 结构体 [ncclGinApi_FlushesAllPutsOnAnySignal&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L712](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L712)
- 函数 [call · L713](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L713)
- 结构体 [ncclGinApi_BarrierOptions&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L719](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L719)
- 函数 [call · L720](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L720)
- 结构体 [ncclGinApi_Flush&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L726](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L726)
- 函数 [call · L728](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L728)
- 结构体 [ncclGinApi_Get&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L765](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L765)
- 函数 [call · L767](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L767)
- 结构体 [ncclGinApi_FlushAsync&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L801](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L801)
- 函数 [call · L802](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L802)
- 结构体 [ncclGinApi_Wait&lt;NCCL_NET_DEVICE_GIN_GPI&gt; · L839](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L839)
- 函数 [call · L840](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L840)
- 函数 [call · L845](../../../src/include/nccl_device/gin/gpi/gin_gpi.h#L845)

## src/include/nccl_device/gin/gpi/gin_gpi_device_host_common.h

[整个文件](../../../src/include/nccl_device/gin/gpi/gin_gpi_device_host_common.h)

- 枚举 [gpi_gfd_ctrl_op · L53](../../../src/include/nccl_device/gin/gpi/gin_gpi_device_host_common.h#L53)
- 枚举 [gpi_gfd_data_op · L61](../../../src/include/nccl_device/gin/gpi/gin_gpi_device_host_common.h#L61)
- 枚举 [gpi_gfd_segment_id · L125](../../../src/include/nccl_device/gin/gpi/gin_gpi_device_host_common.h#L125)
- 枚举 [gpi_resource_sharing_mode · L173](../../../src/include/nccl_device/gin/gpi/gin_gpi_device_host_common.h#L173)
- 枚举 [gpi_post_mode · L178](../../../src/include/nccl_device/gin/gpi/gin_gpi_device_host_common.h#L178)

## src/include/nccl_device/gin/proxy/gin_proxy.h

[整个文件](../../../src/include/nccl_device/gin/proxy/gin_proxy.h)

- 结构体 [ncclGinCpuProxyRequest · L27](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L27)
- 函数 [waitForGfdComplete · L65](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L65)
- 函数 [flush · L88](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L88)
- 函数 [postGfd · L99](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L99)
- 函数 [buildGfd · L148](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L148)
- 函数 [constructProxyOp · L192](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L192)
- 函数 [get · L232](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L232)
- 函数 [put · L252](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L252)
- 结构体 [ncclGinApi_Get&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L362](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L362)
- 函数 [call · L364](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L364)
- 结构体 [ncclGinApi_FlushAsync&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L375](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L375)
- 函数 [call · L376](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L376)
- 结构体 [ncclGinApi_Wait&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L397](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L397)
- 函数 [call · L398](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L398)
- 函数 [call · L405](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L405)
- 结构体 [ncclGinApi_GetCounterPtr&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L415](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L415)
- 函数 [call · L416](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L416)
- 结构体 [ncclGinApi_SupportsStrongSignal&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L423](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L423)
- 函数 [call · L424](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L424)
- 结构体 [ncclGinApi_ResetCounter&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L430](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L430)
- 函数 [call · L431](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L431)
- 结构体 [ncclGinApi_GetSignalPtr&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L439](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L439)
- 函数 [call · L440](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L440)
- 结构体 [ncclGinApi_FlushesAllPutsOnAnySignal&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L448](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L448)
- 函数 [call · L449](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L449)
- 结构体 [ncclGinApi_BarrierOptions&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L456](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L456)
- 函数 [call · L457](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L457)
- 结构体 [ncclGinApi_ResetSignal&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L463](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L463)
- 函数 [call · L464](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L464)
- 结构体 [ncclGinApi_Flush&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L478](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L478)
- 函数 [call · L480](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L480)
- 结构体 [ncclGinApi_Put&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L511](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L511)
- 函数 [call · L513](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L513)
- 结构体 [ncclGinApi_PutValue&lt;NCCL_NET_DEVICE_GIN_PROXY&gt; · L528](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L528)
- 函数 [call · L530](../../../src/include/nccl_device/gin/proxy/gin_proxy.h#L530)

## src/include/nccl_device/gin/proxy/gin_proxy_device_host_common.h

[整个文件](../../../src/include/nccl_device/gin/proxy/gin_proxy_device_host_common.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/gin_barrier.h

[整个文件](../../../src/include/nccl_device/gin_barrier.h)

- 枚举 [ncclGinFenceLevel · L22](../../../src/include/nccl_device/gin_barrier.h#L22)
- 结构体 [ncclGinAllContexts · L42](../../../src/include/nccl_device/gin_barrier.h#L42)
- 函数 [ncclGinAllContexts · L44](../../../src/include/nccl_device/gin_barrier.h#L44)
- 结构体 [ncclGinBarrierSession · L51](../../../src/include/nccl_device/gin_barrier.h#L51)

## src/include/nccl_device/gin_flow.h

[整个文件](../../../src/include/nccl_device/gin_flow.h)

- 结构体 [ncclGinFlowConn · L17](../../../src/include/nccl_device/gin_flow.h#L17)

## src/include/nccl_device/gin_win_stub.h

[整个文件](../../../src/include/nccl_device/gin_win_stub.h)

- 结构体 [ncclGin_BackendMask · L25](../../../src/include/nccl_device/gin_win_stub.h#L25)
- 函数 [_barrierOptions · L31](../../../src/include/nccl_device/gin_win_stub.h#L31)
- 结构体 [ncclGinOutboxHandle · L43](../../../src/include/nccl_device/gin_win_stub.h#L43)
- 结构体 [ncclGinInboxA2AHandle · L47](../../../src/include/nccl_device/gin_win_stub.h#L47)
- 结构体 [ncclGinSyncHandle · L53](../../../src/include/nccl_device/gin_win_stub.h#L53)
- 结构体 [ncclGin_None · L57](../../../src/include/nccl_device/gin_win_stub.h#L57)

## src/include/nccl_device/host.h

[整个文件](../../../src/include/nccl_device/host.h)

- 结构体 [ncclDevResourceRequirements · L13](../../../src/include/nccl_device/host.h#L13)
- 结构体 [ncclTeamRequirements · L23](../../../src/include/nccl_device/host.h#L23)
- 结构体 [ncclDevCommRequirements · L30](../../../src/include/nccl_device/host.h#L30)
- 结构体 [ncclCommProperties · L121](../../../src/include/nccl_device/host.h#L121)

## src/include/nccl_device/impl/barrier__funcs.h

[整个文件](../../../src/include/nccl_device/impl/barrier__funcs.h)

- 函数 [ncclBarrierSession&lt;Coop&gt;::selectBarrierAlgo · L79](../../../src/include/nccl_device/impl/barrier__funcs.h#L79)
- 函数 [ncclBarrierSession&lt;Coop&gt;::sync · L142](../../../src/include/nccl_device/impl/barrier__funcs.h#L142)
- 函数 [ncclBarrier · L215](../../../src/include/nccl_device/impl/barrier__funcs.h#L215)
- 函数 [ncclBarrier · L222](../../../src/include/nccl_device/impl/barrier__funcs.h#L222)

## src/include/nccl_device/impl/barrier__types.h

[整个文件](../../../src/include/nccl_device/impl/barrier__types.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/impl/cft__funcs.h

[整个文件](../../../src/include/nccl_device/impl/cft__funcs.h)

- 函数 [elected · L30](../../../src/include/nccl_device/impl/cft__funcs.h#L30)
- 函数 [elected · L35](../../../src/include/nccl_device/impl/cft__funcs.h#L35)
- 函数 [elected · L40](../../../src/include/nccl_device/impl/cft__funcs.h#L40)
- 函数 [unsupported · L52](../../../src/include/nccl_device/impl/cft__funcs.h#L52)
- 函数 [smemAddr · L57](../../../src/include/nccl_device/impl/cft__funcs.h#L57)
- 函数 [smemAddr · L64](../../../src/include/nccl_device/impl/cft__funcs.h#L64)
- 函数 [waitMbarrier · L68](../../../src/include/nccl_device/impl/cft__funcs.h#L68)
- 函数 [redOpUnsupported · L126](../../../src/include/nccl_device/impl/cft__funcs.h#L126)
- 函数 [ncclMemFence · L299](../../../src/include/nccl_device/impl/cft__funcs.h#L299)
- 函数 [ncclCft&lt;Coop&gt;::~ncclCft · L386](../../../src/include/nccl_device/impl/cft__funcs.h#L386)
- 函数 [ncclCft&lt;Coop&gt;::submit · L403](../../../src/include/nccl_device/impl/cft__funcs.h#L403)
- 函数 [ncclCft&lt;Coop&gt;::flushSmem · L421](../../../src/include/nccl_device/impl/cft__funcs.h#L421)
- 函数 [ncclCft&lt;Coop&gt;::flush · L434](../../../src/include/nccl_device/impl/cft__funcs.h#L434)
- 函数 [ncclCft&lt;Coop&gt;::waitCounted · L460](../../../src/include/nccl_device/impl/cft__funcs.h#L460)
- 函数 [ncclCft&lt;Coop&gt;::put · L498](../../../src/include/nccl_device/impl/cft__funcs.h#L498)
- 函数 [ncclCft&lt;Coop&gt;::putCpMask · L530](../../../src/include/nccl_device/impl/cft__funcs.h#L530)
- 函数 [ncclCft&lt;Coop&gt;::putCounted · L562](../../../src/include/nccl_device/impl/cft__funcs.h#L562)
- 函数 [ncclCft&lt;Coop&gt;::putMultimem · L594](../../../src/include/nccl_device/impl/cft__funcs.h#L594)
- 函数 [ncclCft&lt;Coop&gt;::putMultimemCounted · L626](../../../src/include/nccl_device/impl/cft__funcs.h#L626)
- 函数 [ncclCft&lt;Coop&gt;::putMultimemCpMask · L658](../../../src/include/nccl_device/impl/cft__funcs.h#L658)
- 函数 [ncclCft&lt;Coop&gt;::get · L691](../../../src/include/nccl_device/impl/cft__funcs.h#L691)
- 函数 [ncclCft&lt;Coop&gt;::red · L723](../../../src/include/nccl_device/impl/cft__funcs.h#L723)
- 函数 [ncclCft&lt;Coop&gt;::redCounted · L750](../../../src/include/nccl_device/impl/cft__funcs.h#L750)
- 函数 [ncclCft&lt;Coop&gt;::redMultimem · L778](../../../src/include/nccl_device/impl/cft__funcs.h#L778)
- 函数 [ncclCft&lt;Coop&gt;::redMultimemCounted · L805](../../../src/include/nccl_device/impl/cft__funcs.h#L805)
- 函数 [ncclCft&lt;Coop&gt;::pullRed · L835](../../../src/include/nccl_device/impl/cft__funcs.h#L835)

## src/include/nccl_device/impl/cft__types.h

[整个文件](../../../src/include/nccl_device/impl/cft__types.h)

- 结构体 [ncclCftSmem · L15](../../../src/include/nccl_device/impl/cft__types.h#L15)
- 结构体 [ncclCft_internal · L20](../../../src/include/nccl_device/impl/cft__types.h#L20)
- 结构体 [ncclCftOpSum · L28](../../../src/include/nccl_device/impl/cft__types.h#L28)
- 结构体 [ncclCftOpAnd · L30](../../../src/include/nccl_device/impl/cft__types.h#L30)
- 结构体 [ncclCftOpXor · L32](../../../src/include/nccl_device/impl/cft__types.h#L32)
- 结构体 [ncclCftOpOr · L34](../../../src/include/nccl_device/impl/cft__types.h#L34)
- 结构体 [ncclCftOpMin · L36](../../../src/include/nccl_device/impl/cft__types.h#L36)
- 结构体 [ncclCftOpMax · L38](../../../src/include/nccl_device/impl/cft__types.h#L38)

## src/include/nccl_device/impl/cft_barrier__funcs.h

[整个文件](../../../src/include/nccl_device/impl/cft_barrier__funcs.h)

- 函数 [ncclCftBarrierSession&lt;Coop&gt;::~ncclCftBarrierSession · L35](../../../src/include/nccl_device/impl/cft_barrier__funcs.h#L35)
- 函数 [ncclCftBarrierSession&lt;Coop&gt;::arrive · L45](../../../src/include/nccl_device/impl/cft_barrier__funcs.h#L45)
- 函数 [ncclCftBarrierSession&lt;Coop&gt;::wait · L147](../../../src/include/nccl_device/impl/cft_barrier__funcs.h#L147)
- 函数 [ncclCftBarrierSession&lt;Coop&gt;::sync · L159](../../../src/include/nccl_device/impl/cft_barrier__funcs.h#L159)

## src/include/nccl_device/impl/cft_barrier__types.h

[整个文件](../../../src/include/nccl_device/impl/cft_barrier__types.h)

- 结构体 [ncclCftBarrierHandle · L18](../../../src/include/nccl_device/impl/cft_barrier__types.h#L18)
- 结构体 [ncclCftBarrierSession_internal · L25](../../../src/include/nccl_device/impl/cft_barrier__types.h#L25)
- 函数 [useMultimem · L34](../../../src/include/nccl_device/impl/cft_barrier__types.h#L34)
- 函数 [mcInbox · L38](../../../src/include/nccl_device/impl/cft_barrier__types.h#L38)
- 函数 [ucInbox · L43](../../../src/include/nccl_device/impl/cft_barrier__types.h#L43)
- 函数 [mcInbox · L48](../../../src/include/nccl_device/impl/cft_barrier__types.h#L48)
- 函数 [ucInbox · L57](../../../src/include/nccl_device/impl/cft_barrier__types.h#L57)

## src/include/nccl_device/impl/comm__funcs.h

[整个文件](../../../src/include/nccl_device/impl/comm__funcs.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/impl/comm__types.h

[整个文件](../../../src/include/nccl_device/impl/comm__types.h)

- 结构体 [ncclDevCommWindowTable · L18](../../../src/include/nccl_device/impl/comm__types.h#L18)
- 结构体 [Entry · L19](../../../src/include/nccl_device/impl/comm__types.h#L19)
- 结构体 [ncclDevComm · L28](../../../src/include/nccl_device/impl/comm__types.h#L28)

## src/include/nccl_device/impl/core__funcs.h

[整个文件](../../../src/include/nccl_device/impl/core__funcs.h)

- 函数 [ncclTeamWorld · L16](../../../src/include/nccl_device/impl/core__funcs.h#L16)
- 函数 [ncclTeamLsa · L26](../../../src/include/nccl_device/impl/core__funcs.h#L26)
- 函数 [ncclTeamCft · L36](../../../src/include/nccl_device/impl/core__funcs.h#L36)
- 函数 [ncclTeamCftMultimem · L57](../../../src/include/nccl_device/impl/core__funcs.h#L57)
- 函数 [ncclTeamRail · L67](../../../src/include/nccl_device/impl/core__funcs.h#L67)
- 函数 [ncclTeamRankIsMember · L76](../../../src/include/nccl_device/impl/core__funcs.h#L76)
- 函数 [ncclTeamRankToTeam · L84](../../../src/include/nccl_device/impl/core__funcs.h#L84)
- 函数 [ncclTeamRankToWorld · L93](../../../src/include/nccl_device/impl/core__funcs.h#L93)
- 函数 [ncclTeamRankToLsa · L99](../../../src/include/nccl_device/impl/core__funcs.h#L99)
- 函数 [ncclDevCommCanGetPeerPointer · L105](../../../src/include/nccl_device/impl/core__funcs.h#L105)
- 函数 [ncclTeamInnerFactor · L112](../../../src/include/nccl_device/impl/core__funcs.h#L112)
- 函数 [ncclTeamOuterFactor · L120](../../../src/include/nccl_device/impl/core__funcs.h#L120)
- 函数 [ncclTeamRankInDifference · L128](../../../src/include/nccl_device/impl/core__funcs.h#L128)
- 函数 [ncclGetLocalPointer · L145](../../../src/include/nccl_device/impl/core__funcs.h#L145)
- 函数 [ncclGetLsaPointer · L154](../../../src/include/nccl_device/impl/core__funcs.h#L154)
- 函数 [ncclGetPeerPointer · L163](../../../src/include/nccl_device/impl/core__funcs.h#L163)
- 函数 [ncclGetPeerPointer · L172](../../../src/include/nccl_device/impl/core__funcs.h#L172)
- 函数 [ncclGetMultimemPointer · L179](../../../src/include/nccl_device/impl/core__funcs.h#L179)
- 函数 [ncclGetLsaMultimemPointer · L187](../../../src/include/nccl_device/impl/core__funcs.h#L187)
- 函数 [ncclGetCftLeInfo · L193](../../../src/include/nccl_device/impl/core__funcs.h#L193)
- 函数 [ncclGetPeerLeInfo · L202](../../../src/include/nccl_device/impl/core__funcs.h#L202)
- 函数 [ncclGetMultimemLeInfo · L213](../../../src/include/nccl_device/impl/core__funcs.h#L213)
- 函数 [ncclGetResourceBufferOffset · L253](../../../src/include/nccl_device/impl/core__funcs.h#L253)
- 函数 [ncclGetResourceBufferLocalPointer · L258](../../../src/include/nccl_device/impl/core__funcs.h#L258)
- 函数 [ncclGetResourceBufferLsaPointer · L267](../../../src/include/nccl_device/impl/core__funcs.h#L267)
- 函数 [ncclGetResourceBufferPeerPointer · L277](../../../src/include/nccl_device/impl/core__funcs.h#L277)
- 函数 [ncclGetResourceBufferMultimemPointer · L288](../../../src/include/nccl_device/impl/core__funcs.h#L288)
- 函数 [ncclGetResourceBufferLsaMultimemPointer · L298](../../../src/include/nccl_device/impl/core__funcs.h#L298)
- 函数 [ncclGetResourceBufferCftLeInfo · L304](../../../src/include/nccl_device/impl/core__funcs.h#L304)
- 函数 [ncclGetResourceBufferPeerLeInfo · L313](../../../src/include/nccl_device/impl/core__funcs.h#L313)
- 函数 [ncclGetResourceBufferMultimemLeInfo · L323](../../../src/include/nccl_device/impl/core__funcs.h#L323)

## src/include/nccl_device/impl/core__types.h

[整个文件](../../../src/include/nccl_device/impl/core__types.h)

- 结构体 [ncclSegmentWindow · L24](../../../src/include/nccl_device/impl/core__types.h#L24)
- 结构体 [ncclWindow_vidmem · L31](../../../src/include/nccl_device/impl/core__types.h#L31)
- 结构体 [ncclResourceWindow_vidmem · L51](../../../src/include/nccl_device/impl/core__types.h#L51)
- 结构体 [ncclMultimemHandle · L57](../../../src/include/nccl_device/impl/core__types.h#L57)

## src/include/nccl_device/impl/flow__funcs.h

[整个文件](../../../src/include/nccl_device/impl/flow__funcs.h)

- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::threadRole · L22](../../../src/include/nccl_device/impl/flow__funcs.h#L22)
- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::roleType · L56](../../../src/include/nccl_device/impl/flow__funcs.h#L56)
- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::initShmem · L99](../../../src/include/nccl_device/impl/flow__funcs.h#L99)
- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::close · L114](../../../src/include/nccl_device/impl/flow__funcs.h#L114)
- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::process · L122](../../../src/include/nccl_device/impl/flow__funcs.h#L122)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::construct · L132](../../../src/include/nccl_device/impl/flow__funcs.h#L132)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::close · L149](../../../src/include/nccl_device/impl/flow__funcs.h#L149)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::waitSend · L154](../../../src/include/nccl_device/impl/flow__funcs.h#L154)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::postSend · L159](../../../src/include/nccl_device/impl/flow__funcs.h#L159)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::postSend · L164](../../../src/include/nccl_device/impl/flow__funcs.h#L164)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::waitRecv · L170](../../../src/include/nccl_device/impl/flow__funcs.h#L170)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::postRecv · L175](../../../src/include/nccl_device/impl/flow__funcs.h#L175)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::advanceStep · L180](../../../src/include/nccl_device/impl/flow__funcs.h#L180)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::advanceSlice · L185](../../../src/include/nccl_device/impl/flow__funcs.h#L185)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::stepFlag · L190](../../../src/include/nccl_device/impl/flow__funcs.h#L190)
- 函数 [ncclFlowConnection&lt;0, Protocol&gt;::usesGin · L195](../../../src/include/nccl_device/impl/flow__funcs.h#L195)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::construct · L201](../../../src/include/nccl_device/impl/flow__funcs.h#L201)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::close · L235](../../../src/include/nccl_device/impl/flow__funcs.h#L235)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::waitSend · L241](../../../src/include/nccl_device/impl/flow__funcs.h#L241)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::postSend · L246](../../../src/include/nccl_device/impl/flow__funcs.h#L246)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::postSend · L252](../../../src/include/nccl_device/impl/flow__funcs.h#L252)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::waitRecv · L264](../../../src/include/nccl_device/impl/flow__funcs.h#L264)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::postRecv · L269](../../../src/include/nccl_device/impl/flow__funcs.h#L269)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::advanceStep · L275](../../../src/include/nccl_device/impl/flow__funcs.h#L275)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::advanceSlice · L281](../../../src/include/nccl_device/impl/flow__funcs.h#L281)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::stepFlag · L286](../../../src/include/nccl_device/impl/flow__funcs.h#L286)
- 函数 [ncclFlowConnection&lt;GinBackendMask, Protocol&gt;::usesGin · L291](../../../src/include/nccl_device/impl/flow__funcs.h#L291)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::closeBackend · L327](../../../src/include/nccl_device/impl/flow__funcs.h#L327)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::waitSend · L332](../../../src/include/nccl_device/impl/flow__funcs.h#L332)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::postSend · L337](../../../src/include/nccl_device/impl/flow__funcs.h#L337)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::postSend · L343](../../../src/include/nccl_device/impl/flow__funcs.h#L343)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::waitRecv · L349](../../../src/include/nccl_device/impl/flow__funcs.h#L349)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::postRecv · L354](../../../src/include/nccl_device/impl/flow__funcs.h#L354)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::advanceStep · L359](../../../src/include/nccl_device/impl/flow__funcs.h#L359)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::advanceSlice · L364](../../../src/include/nccl_device/impl/flow__funcs.h#L364)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::stepFlag · L370](../../../src/include/nccl_device/impl/flow__funcs.h#L370)
- 函数 [ncclFlowProcessor&lt;GinBackendMask, SlicesPerChunk, MaxPeers, Protocol, FlowOps&gt;::usesGin · L376](../../../src/include/nccl_device/impl/flow__funcs.h#L376)

## src/include/nccl_device/impl/flow__internals.h

[整个文件](../../../src/include/nccl_device/impl/flow__internals.h)

- 结构体 [ncclFlowProtocolTag · L19](../../../src/include/nccl_device/impl/flow__internals.h#L19)
- 结构体 [ncclFlowBase · L37](../../../src/include/nccl_device/impl/flow__internals.h#L37)
- 结构体 [ncclFlowConnection&lt;0, Protocol&gt; · L105](../../../src/include/nccl_device/impl/flow__internals.h#L105)
- 联合体 [Storage · L106](../../../src/include/nccl_device/impl/flow__internals.h#L106)
- 函数 [Storage · L109](../../../src/include/nccl_device/impl/flow__internals.h#L109)
- 函数 [Storage · L110](../../../src/include/nccl_device/impl/flow__internals.h#L110)
- 函数 [ncclFlowConnection · L113](../../../src/include/nccl_device/impl/flow__internals.h#L113)
- 结构体 [ncclFlowConnection · L133](../../../src/include/nccl_device/impl/flow__internals.h#L133)
- 联合体 [Storage · L136](../../../src/include/nccl_device/impl/flow__internals.h#L136)
- 函数 [Storage · L140](../../../src/include/nccl_device/impl/flow__internals.h#L140)
- 函数 [Storage · L141](../../../src/include/nccl_device/impl/flow__internals.h#L141)
- 函数 [ncclFlowConnection · L145](../../../src/include/nccl_device/impl/flow__internals.h#L145)

## src/include/nccl_device/impl/flow__ll128_funcs.h

[整个文件](../../../src/include/nccl_device/impl/flow__ll128_funcs.h)

- 函数 [ncclFlowLL128Load128 · L16](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L16)
- 函数 [ncclFlowLL128Store128 · L20](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L20)
- 函数 [ncclFlowLL128LoadDataWord · L25](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L25)
- 函数 [ncclFlowLL128LoadDataBegin · L37](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L37)
- 函数 [ncclFlowLL128LoadDataFinish · L76](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L76)
- 函数 [ncclFlowLL128StoreData · L85](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L85)
- 函数 [ncclFlowLL128LoadWire · L126](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L126)
- 函数 [ncclFlowLL128StoreWire · L146](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L146)
- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::process · L157](../../../src/include/nccl_device/impl/flow__ll128_funcs.h#L157)

## src/include/nccl_device/impl/flow__ll_funcs.h

[整个文件](../../../src/include/nccl_device/impl/flow__ll_funcs.h)

- 函数 [ncclFlowLLLoad · L16](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L16)
- 函数 [ncclFlowLLStore · L29](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L29)
- 函数 [ncclFlowLLNeedsCleanup · L35](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L35)
- 函数 [ncclFlowLLLoadData · L47](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L47)
- 结构体 [ncclFlowLLDataLoader · L62](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L62)
- 函数 [begin · L70](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L70)
- 函数 [finish · L86](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L86)
- 函数 [ncclFlowLLStoreData · L92](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L92)
- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::process · L115](../../../src/include/nccl_device/impl/flow__ll_funcs.h#L115)

## src/include/nccl_device/impl/flow__simple_funcs.h

[整个文件](../../../src/include/nccl_device/impl/flow__simple_funcs.h)

- 函数 [ncclFlowBase&lt;Backend, SlicesPerChunk, MaxPeers&gt;::process · L19](../../../src/include/nccl_device/impl/flow__simple_funcs.h#L19)

## src/include/nccl_device/impl/flow__types.h

[整个文件](../../../src/include/nccl_device/impl/flow__types.h)

- 结构体 [ncclFlowConnState · L34](../../../src/include/nccl_device/impl/flow__types.h#L34)
- 枚举 [ncclFlowProtocol · L50](../../../src/include/nccl_device/impl/flow__types.h#L50)
- 函数 [ncclFlowGetSignalWarpsPerPart · L57](../../../src/include/nccl_device/impl/flow__types.h#L57)
- 函数 [ncclFlowPartWorkerWarps · L61](../../../src/include/nccl_device/impl/flow__types.h#L61)
- 函数 [ncclFlowPartWorkerWarp0 · L66](../../../src/include/nccl_device/impl/flow__types.h#L66)
- 结构体 [ncclFlowPartShmem · L74](../../../src/include/nccl_device/impl/flow__types.h#L74)
- 结构体 [ncclFlowShmem · L83](../../../src/include/nccl_device/impl/flow__types.h#L83)

## src/include/nccl_device/impl/gin__funcs.h

[整个文件](../../../src/include/nccl_device/impl/gin__funcs.h)

- 函数 [windowOffsetToGinOffset · L19](../../../src/include/nccl_device/impl/gin__funcs.h#L19)
- 函数 [teamRankToGinRank · L43](../../../src/include/nccl_device/impl/gin__funcs.h#L43)
- 函数 [findSegmentFromWindow · L52](../../../src/include/nccl_device/impl/gin__funcs.h#L52)
- 函数 [getSegmentChunkSize · L69](../../../src/include/nccl_device/impl/gin__funcs.h#L69)
- 函数 [advanceSegmentCursor · L76](../../../src/include/nccl_device/impl/gin__funcs.h#L76)
- 函数 [ncclGinInitCommon · L113](../../../src/include/nccl_device/impl/gin__funcs.h#L113)
- 函数 [ncclGin_isDescriptor · L167](../../../src/include/nccl_device/impl/gin__funcs.h#L167)
- 函数 [ncclGin_isDescriptor · L175](../../../src/include/nccl_device/impl/gin__funcs.h#L175)
- 函数 [ncclGin_getSignalOpArg · L192](../../../src/include/nccl_device/impl/gin__funcs.h#L192)
- 函数 [ncclGin_getSignalOpArg · L217](../../../src/include/nccl_device/impl/gin__funcs.h#L217)
- 函数 [ncclGin_getSignalOpArg · L235](../../../src/include/nccl_device/impl/gin__funcs.h#L235)
- 函数 [ncclGin_getSignalOpArg · L253](../../../src/include/nccl_device/impl/gin__funcs.h#L253)
- 函数 [ncclGin_getSignalOpArg · L271](../../../src/include/nccl_device/impl/gin__funcs.h#L271)
- 函数 [ncclGin_getSignalOpArg · L289](../../../src/include/nccl_device/impl/gin__funcs.h#L289)
- 函数 [ncclGin_getSignalOpArg · L307](../../../src/include/nccl_device/impl/gin__funcs.h#L307)
- 函数 [ncclGin_getSignalOpArg · L328](../../../src/include/nccl_device/impl/gin__funcs.h#L328)
- 函数 [ncclGin_getSignalOpArg · L349](../../../src/include/nccl_device/impl/gin__funcs.h#L349)
- 函数 [ncclGin_getSignalOpArg · L370](../../../src/include/nccl_device/impl/gin__funcs.h#L370)
- 函数 [ncclGin_getSignalOpArg · L391](../../../src/include/nccl_device/impl/gin__funcs.h#L391)
- 函数 [ncclGin_getSignalOpArg · L412](../../../src/include/nccl_device/impl/gin__funcs.h#L412)
- 函数 [ncclGin_getSignalOpArg · L433](../../../src/include/nccl_device/impl/gin__funcs.h#L433)
- 函数 [ncclGin_isCounter · L443](../../../src/include/nccl_device/impl/gin__funcs.h#L443)
- 函数 [ncclGin_isCounter · L453](../../../src/include/nccl_device/impl/gin__funcs.h#L453)
- 函数 [ncclGin_isCounter · L464](../../../src/include/nccl_device/impl/gin__funcs.h#L464)
- 函数 [ncclGin_isDeviceOnly · L480](../../../src/include/nccl_device/impl/gin__funcs.h#L480)
- 函数 [ncclGin_isDeviceOnly · L483](../../../src/include/nccl_device/impl/gin__funcs.h#L483)
- 函数 [ncclGin_isDeviceOnly · L486](../../../src/include/nccl_device/impl/gin__funcs.h#L486)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::put · L500](../../../src/include/nccl_device/impl/gin__funcs.h#L500)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::_supportsStrongSignal · L585](../../../src/include/nccl_device/impl/gin__funcs.h#L585)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::put · L596](../../../src/include/nccl_device/impl/gin__funcs.h#L596)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::putValue · L610](../../../src/include/nccl_device/impl/gin__funcs.h#L610)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::putValue · L637](../../../src/include/nccl_device/impl/gin__funcs.h#L637)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::signal · L649](../../../src/include/nccl_device/impl/gin__funcs.h#L649)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::flush · L671](../../../src/include/nccl_device/impl/gin__funcs.h#L671)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::_flushesAllPutsOnAnySignal · L695](../../../src/include/nccl_device/impl/gin__funcs.h#L695)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::waitCounter · L710](../../../src/include/nccl_device/impl/gin__funcs.h#L710)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::readCounter · L740](../../../src/include/nccl_device/impl/gin__funcs.h#L740)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::getSignalShadowPtr · L752](../../../src/include/nccl_device/impl/gin__funcs.h#L752)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::increaseSignalShadow · L760](../../../src/include/nccl_device/impl/gin__funcs.h#L760)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::readSignal · L769](../../../src/include/nccl_device/impl/gin__funcs.h#L769)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::readSignal · L778](../../../src/include/nccl_device/impl/gin__funcs.h#L778)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::wait · L791](../../../src/include/nccl_device/impl/gin__funcs.h#L791)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::flushAsync · L818](../../../src/include/nccl_device/impl/gin__funcs.h#L818)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::get · L832](../../../src/include/nccl_device/impl/gin__funcs.h#L832)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::waitSignal · L893](../../../src/include/nccl_device/impl/gin__funcs.h#L893)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::waitSignal · L921](../../../src/include/nccl_device/impl/gin__funcs.h#L921)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::waitSignalMeetShadow · L954](../../../src/include/nccl_device/impl/gin__funcs.h#L954)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::waitSignalFollowShadow · L970](../../../src/include/nccl_device/impl/gin__funcs.h#L970)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::resetCounter · L1007](../../../src/include/nccl_device/impl/gin__funcs.h#L1007)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::resetSignal · L1015](../../../src/include/nccl_device/impl/gin__funcs.h#L1015)
- 函数 [ncclGin_BackendMask&lt;beMask&gt;::resetSignal · L1024](../../../src/include/nccl_device/impl/gin__funcs.h#L1024)

## src/include/nccl_device/impl/gin__types.h

[整个文件](../../../src/include/nccl_device/impl/gin__types.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/impl/gin_barrier__funcs.h

[整个文件](../../../src/include/nccl_device/impl/gin_barrier__funcs.h)

- 函数 [ncclGinBarrierSession&lt;Coop&gt;::~ncclGinBarrierSession · L65](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L65)
- 函数 [ncclGinBarrierSession&lt;Coop&gt;::sync · L330](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L330)
- 函数 [ncclGinBarrier · L346](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L346)
- 函数 [ncclGinBarrier · L353](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L353)
- 函数 [ncclGinBarrier · L360](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L360)
- 函数 [ncclGinBarrier · L367](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L367)
- 函数 [ncclGinBarrier · L374](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L374)
- 函数 [ncclGinBarrier · L381](../../../src/include/nccl_device/impl/gin_barrier__funcs.h#L381)

## src/include/nccl_device/impl/gin_barrier__types.h

[整个文件](../../../src/include/nccl_device/impl/gin_barrier__types.h)

- 结构体 [ncclGinBarrierHandle · L14](../../../src/include/nccl_device/impl/gin_barrier__types.h#L14)
- 函数 [ncclGinBarrierSlots · L23](../../../src/include/nccl_device/impl/gin_barrier__types.h#L23)
- 结构体 [ncclGinBarrierState · L36](../../../src/include/nccl_device/impl/gin_barrier__types.h#L36)
- 结构体 [ncclGinBarrierSession_internal · L42](../../../src/include/nccl_device/impl/gin_barrier__types.h#L42)

## src/include/nccl_device/impl/gin_flow__funcs.h

[整个文件](../../../src/include/nccl_device/impl/gin_flow__funcs.h)

- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::close · L52](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L52)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::waitSend · L60](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L60)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::postSend · L67](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L67)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::postSendFrom · L79](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L79)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::postSendDirect · L86](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L86)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::postSendSimple · L98](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L98)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::advanceStep · L112](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L112)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::signal · L118](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L118)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::waitRecv · L126](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L126)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::advanceSlice · L133](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L133)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::stepFlag · L141](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L141)
- 函数 [ncclGinFlowConn&lt;GinBackendMask, Protocol&gt;::postRecv · L146](../../../src/include/nccl_device/impl/gin_flow__funcs.h#L146)

## src/include/nccl_device/impl/gin_flow__types.h

[整个文件](../../../src/include/nccl_device/impl/gin_flow__types.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/impl/ll128__types.h

[整个文件](../../../src/include/nccl_device/impl/ll128__types.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/impl/ll__types.h

[整个文件](../../../src/include/nccl_device/impl/ll__types.h)

- 联合体 [ncclLLFifoLine · L14](../../../src/include/nccl_device/impl/ll__types.h#L14)

## src/include/nccl_device/impl/ll_a2a__funcs.h

[整个文件](../../../src/include/nccl_device/impl/ll_a2a__funcs.h)

- 函数 [ncclLLA2ASession&lt;Coop&gt;::~ncclLLA2ASession · L30](../../../src/include/nccl_device/impl/ll_a2a__funcs.h#L30)
- 函数 [ncclLLA2ASession&lt;Coop&gt;::send · L41](../../../src/include/nccl_device/impl/ll_a2a__funcs.h#L41)
- 函数 [ncclLLA2ASession&lt;Coop&gt;::bcast · L68](../../../src/include/nccl_device/impl/ll_a2a__funcs.h#L68)
- 函数 [ncclLLA2ASession&lt;Coop&gt;::recv · L147](../../../src/include/nccl_device/impl/ll_a2a__funcs.h#L147)
- 函数 [ncclLLA2ASession&lt;Coop&gt;::recvUnrolled · L157](../../../src/include/nccl_device/impl/ll_a2a__funcs.h#L157)
- 函数 [ncclLLA2ASession&lt;Coop&gt;::recvReduce · L223](../../../src/include/nccl_device/impl/ll_a2a__funcs.h#L223)
- 函数 [ncclLLA2ASession&lt;Coop&gt;::endEpoch · L254](../../../src/include/nccl_device/impl/ll_a2a__funcs.h#L254)

## src/include/nccl_device/impl/ll_a2a__types.h

[整个文件](../../../src/include/nccl_device/impl/ll_a2a__types.h)

- 结构体 [ncclLLA2AHandle · L13](../../../src/include/nccl_device/impl/ll_a2a__types.h#L13)
- 结构体 [ncclLLA2ASession_internal · L20](../../../src/include/nccl_device/impl/ll_a2a__types.h#L20)
- 函数 [calcSlotOffset · L32](../../../src/include/nccl_device/impl/ll_a2a__types.h#L32)

## src/include/nccl_device/impl/lsa_barrier__funcs.h

[整个文件](../../../src/include/nccl_device/impl/lsa_barrier__funcs.h)

- 函数 [ncclLsaBarrierSession&lt;Coop&gt;::ncclLsaBarrierSession · L15](../../../src/include/nccl_device/impl/lsa_barrier__funcs.h#L15)
- 函数 [ncclLsaBarrierSession&lt;Coop&gt;::~ncclLsaBarrierSession · L39](../../../src/include/nccl_device/impl/lsa_barrier__funcs.h#L39)
- 函数 [ncclLsaBarrierSession&lt;Coop&gt;::arrive · L55](../../../src/include/nccl_device/impl/lsa_barrier__funcs.h#L55)
- 函数 [ncclLsaBarrierSession&lt;Coop&gt;::wait · L149](../../../src/include/nccl_device/impl/lsa_barrier__funcs.h#L149)
- 函数 [ncclLsaBarrierSession&lt;Coop&gt;::sync · L165](../../../src/include/nccl_device/impl/lsa_barrier__funcs.h#L165)

## src/include/nccl_device/impl/lsa_barrier__types.h

[整个文件](../../../src/include/nccl_device/impl/lsa_barrier__types.h)

- 结构体 [ncclLsaBarrierHandle · L13](../../../src/include/nccl_device/impl/lsa_barrier__types.h#L13)
- 结构体 [ncclLsaBarrierSession_internal · L20](../../../src/include/nccl_device/impl/lsa_barrier__types.h#L20)
- 函数 [mcInbox · L30](../../../src/include/nccl_device/impl/lsa_barrier__types.h#L30)
- 函数 [ucInbox · L42](../../../src/include/nccl_device/impl/lsa_barrier__types.h#L42)

## src/include/nccl_device/impl/lsa_flow__funcs.h

[整个文件](../../../src/include/nccl_device/impl/lsa_flow__funcs.h)

- 函数 [ncclLsaFlowLoadSignal · L18](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L18)
- 函数 [ncclLsaFlowStoreSignal · L24](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L24)
- 函数 [ncclLsaFlowFence · L32](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L32)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::close · L67](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L67)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::waitSend · L75](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L75)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::postSend · L90](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L90)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::advanceStep · L98](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L98)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::waitRecv · L105](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L105)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::advanceSlice · L118](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L118)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::stepFlag · L126](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L126)
- 函数 [ncclLsaFlowConn&lt;Protocol&gt;::postRecv · L132](../../../src/include/nccl_device/impl/lsa_flow__funcs.h#L132)

## src/include/nccl_device/impl/lsa_flow__types.h

[整个文件](../../../src/include/nccl_device/impl/lsa_flow__types.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/impl/multimem__funcs.h

[整个文件](../../../src/include/nccl_device/impl/multimem__funcs.h)

- 结构体 [LoadImpl · L24](../../../src/include/nccl_device/impl/multimem__funcs.h#L24)
- 函数 [run · L25](../../../src/include/nccl_device/impl/multimem__funcs.h#L25)
- 结构体 [LoadImpl&lt;Pack, UseMultimem, RedOp, 0&gt; · L47](../../../src/include/nccl_device/impl/multimem__funcs.h#L47)
- 函数 [run · L48](../../../src/include/nccl_device/impl/multimem__funcs.h#L48)
- 函数 [load · L54](../../../src/include/nccl_device/impl/multimem__funcs.h#L54)
- 联合体 [BytePack · L655](../../../src/include/nccl_device/impl/multimem__funcs.h#L655)
- 函数 [multimem_st_global&lt;0&gt; · L669](../../../src/include/nccl_device/impl/multimem__funcs.h#L669)
- 函数 [multimem_st_global&lt;1&gt; · L674](../../../src/include/nccl_device/impl/multimem__funcs.h#L674)
- 函数 [multimem_st_global&lt;2&gt; · L688](../../../src/include/nccl_device/impl/multimem__funcs.h#L688)
- 函数 [multimem_st_global&lt;4&gt; · L702](../../../src/include/nccl_device/impl/multimem__funcs.h#L702)
- 函数 [multimem_st_global&lt;8&gt; · L707](../../../src/include/nccl_device/impl/multimem__funcs.h#L707)
- 函数 [multimem_st_global&lt;16&gt; · L712](../../../src/include/nccl_device/impl/multimem__funcs.h#L712)
- 函数 [multimemStore · L723](../../../src/include/nccl_device/impl/multimem__funcs.h#L723)
- 函数 [store · L744](../../../src/include/nccl_device/impl/multimem__funcs.h#L744)

## src/include/nccl_device/impl/ptr__funcs.h

[整个文件](../../../src/include/nccl_device/impl/ptr__funcs.h)

- 函数 [ncclSymPtr&lt;T&gt;::localPtr · L94](../../../src/include/nccl_device/impl/ptr__funcs.h#L94)
- 函数 [ncclSymPtr&lt;T&gt;::lsaPtr · L105](../../../src/include/nccl_device/impl/ptr__funcs.h#L105)
- 函数 [ncclSymPtr&lt;T&gt;::peerPtr · L112](../../../src/include/nccl_device/impl/ptr__funcs.h#L112)
- 函数 [ncclSymPtr&lt;T&gt;::peerPtr · L119](../../../src/include/nccl_device/impl/ptr__funcs.h#L119)
- 函数 [ncclSymPtr&lt;T&gt;::multimemPtr · L126](../../../src/include/nccl_device/impl/ptr__funcs.h#L126)
- 函数 [ncclSymPtr&lt;T&gt;::lsaMultimemPtr · L133](../../../src/include/nccl_device/impl/ptr__funcs.h#L133)
- 函数 [operator- · L147](../../../src/include/nccl_device/impl/ptr__funcs.h#L147)
- 函数 [operator== · L152](../../../src/include/nccl_device/impl/ptr__funcs.h#L152)
- 函数 [operator!= · L156](../../../src/include/nccl_device/impl/ptr__funcs.h#L156)

## src/include/nccl_device/impl/ptr__types.h

[整个文件](../../../src/include/nccl_device/impl/ptr__types.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/impl/reduce_copy__funcs.h

[整个文件](../../../src/include/nccl_device/impl/reduce_copy__funcs.h)

- 函数 [ncclLsaReduceLsaCopy · L42](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L42)
- 函数 [ncclLsaReduceMultimemCopy · L54](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L54)
- 函数 [ncclLsaReduceSumLsaCopy · L67](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L67)
- 函数 [ncclLsaReduceSumMultimemCopy · L75](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L75)
- 函数 [ncclMultimemReduceSumLsaCopy · L83](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L83)
- 函数 [ncclMultimemReduceSumMultimemCopy · L97](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L97)
- 函数 [ncclLsaReduceSum · L115](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L115)
- 函数 [ncclLsaReduceSum · L124](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L124)
- 函数 [ncclLsaReduceSum · L146](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L146)
- 函数 [ncclLsaReduceSum · L156](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L156)
- 函数 [ncclLsaReduceSum · L166](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L166)
- 函数 [ncclMultimemReduceSum · L176](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L176)
- 函数 [ncclMultimemReduceSum · L191](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L191)
- 函数 [ncclMultimemReduceSum · L205](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L205)
- 函数 [ncclLocalReduceSum · L215](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L215)
- 函数 [ncclLocalReduceSum · L224](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L224)
- 函数 [ncclLsaCopy · L246](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L246)
- 函数 [ncclLsaCopy · L255](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L255)
- 函数 [ncclLsaCopy · L277](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L277)
- 函数 [ncclLsaCopy · L286](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L286)
- 函数 [ncclLsaCopy · L296](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L296)
- 函数 [ncclLsaCopyTma · L306](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L306)
- 函数 [ncclLsaCopyTma · L342](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L342)
- 函数 [ncclLsaCopyTma · L381](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L381)
- 函数 [ncclLsaCopyTma · L390](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L390)
- 函数 [ncclLsaCopyTma · L399](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L399)
- 函数 [ncclMultimemCopy · L408](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L408)
- 函数 [ncclMultimemCopy · L423](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L423)
- 函数 [ncclMultimemCopy · L437](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L437)
- 函数 [ncclLocalCopy · L447](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L447)
- 函数 [ncclLocalCopy · L456](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L456)
- 函数 [ncclLsaReduceSumCopy · L476](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L476)
- 函数 [ncclLsaReduceSumCopy · L497](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L497)
- 函数 [ncclLsaReduceSumCopy · L505](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L505)
- 函数 [ncclLsaReduceSumCopy · L515](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L515)
- 函数 [ncclLsaReduceSumCopy · L526](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L526)
- 函数 [ncclMultimemReduceSumCopy · L548](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L548)
- 函数 [ncclMultimemReduceSumCopy · L562](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L562)
- 函数 [ncclMultimemReduceSumCopy · L575](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L575)
- 函数 [ncclLsaReduceSumMultimemCopy · L587](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L587)
- 函数 [ncclLsaReduceSumMultimemCopy · L610](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L610)
- 函数 [ncclMultimemReduceSumLsaCopy · L633](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L633)
- 函数 [ncclMultimemReduceSumLsaCopy · L656](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L656)
- 函数 [ncclLocalReduceSumCopy · L679](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L679)
- 函数 [ncclLsaReduceLsaCopy · L706](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L706)
- 函数 [ncclLsaReduceMultimemCopy · L719](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L719)
- 函数 [ncclLsaReduceSumLsaCopy · L727](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L727)
- 函数 [ncclLsaReduceSumMultimemCopy · L734](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L734)
- 函数 [ncclMultimemReduceSumLsaCopy · L741](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L741)
- 函数 [ncclMultimemReduceSumMultimemCopy · L748](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L748)
- 函数 [ncclLsaReduceSum · L756](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L756)
- 函数 [ncclLsaReduceSum · L763](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L763)
- 函数 [ncclLsaReduceSum · L770](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L770)
- 函数 [ncclLsaReduceSum · L777](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L777)
- 函数 [ncclLsaReduceSum · L784](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L784)
- 函数 [ncclMultimemReduceSum · L791](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L791)
- 函数 [ncclMultimemReduceSum · L799](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L799)
- 函数 [ncclMultimemReduceSum · L806](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L806)
- 函数 [ncclLocalReduceSum · L814](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L814)
- 函数 [ncclLocalReduceSum · L822](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L822)
- 函数 [ncclLsaCopy · L832](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L832)
- 函数 [ncclLsaCopy · L840](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L840)
- 函数 [ncclLsaCopy · L848](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L848)
- 函数 [ncclLsaCopy · L856](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L856)
- 函数 [ncclLsaCopy · L864](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L864)
- 函数 [ncclLsaCopyTma · L872](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L872)
- 函数 [ncclLsaCopyTma · L880](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L880)
- 函数 [ncclLsaCopyTma · L888](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L888)
- 函数 [ncclLsaCopyTma · L896](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L896)
- 函数 [ncclLsaCopyTma · L904](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L904)
- 函数 [ncclMultimemCopy · L912](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L912)
- 函数 [ncclMultimemCopy · L920](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L920)
- 函数 [ncclMultimemCopy · L928](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L928)
- 函数 [ncclLocalCopy · L936](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L936)
- 函数 [ncclLocalCopy · L944](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L944)
- 函数 [ncclLsaReduceSumCopy · L954](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L954)
- 函数 [ncclLsaReduceSumCopy · L962](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L962)
- 函数 [ncclLsaReduceSumCopy · L970](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L970)
- 函数 [ncclLsaReduceSumCopy · L978](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L978)
- 函数 [ncclLsaReduceSumCopy · L987](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L987)
- 函数 [ncclMultimemReduceSumCopy · L995](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L995)
- 函数 [ncclMultimemReduceSumCopy · L1004](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L1004)
- 函数 [ncclMultimemReduceSumCopy · L1012](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L1012)
- 函数 [ncclLsaReduceSumMultimemCopy · L1021](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L1021)
- 函数 [ncclLsaReduceSumMultimemCopy · L1030](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L1030)
- 函数 [ncclMultimemReduceSumLsaCopy · L1038](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L1038)
- 函数 [ncclMultimemReduceSumLsaCopy · L1047](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L1047)
- 函数 [ncclLocalReduceSumCopy · L1055](../../../src/include/nccl_device/impl/reduce_copy__funcs.h#L1055)

## src/include/nccl_device/impl/reduce_copy__impl.h

[整个文件](../../../src/include/nccl_device/impl/reduce_copy__impl.h)

- 函数 [reduceCopyLoopCoreImpl · L47](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L47)
- 函数 [reduceCopyLoopCore · L186](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L186)
- 结构体 [ReduceCopyLoopParams · L208](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L208)
- 函数 [ReduceCopyLoopParams · L216](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L216)
- 函数 [reduceCopyLoop · L244](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L244)
- 函数 [reduceCopyScalarLoop · L290](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L290)
- 函数 [reduceCopy · L318](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L318)
- 函数 [lsaCopyTma · L429](../../../src/include/nccl_device/impl/reduce_copy__impl.h#L429)

## src/include/nccl_device/impl/reduce_copy__types.h

[整个文件](../../../src/include/nccl_device/impl/reduce_copy__types.h)

- 结构体 [OpSum · L25](../../../src/include/nccl_device/impl/reduce_copy__types.h#L25)
- 函数 [operator() · L27](../../../src/include/nccl_device/impl/reduce_copy__types.h#L27)
- 结构体 [AccRedOp · L35](../../../src/include/nccl_device/impl/reduce_copy__types.h#L35)
- 结构体 [AccRedOp&lt;Red&lt;T&gt;, AccEltType&gt; · L42](../../../src/include/nccl_device/impl/reduce_copy__types.h#L42)
- 结构体 [CoopStride · L48](../../../src/include/nccl_device/impl/reduce_copy__types.h#L48)
- 结构体 [CoopStride&lt;ncclCoopWarp&gt; · L56](../../../src/include/nccl_device/impl/reduce_copy__types.h#L56)
- 结构体 [CoopStride&lt;ncclCoopCta&gt; · L62](../../../src/include/nccl_device/impl/reduce_copy__types.h#L62)
- 结构体 [CoopStride&lt;ncclCoopThread&gt; · L68](../../../src/include/nccl_device/impl/reduce_copy__types.h#L68)
- 结构体 [OpSum&lt;__nv_fp8_e4m3&gt; · L76](../../../src/include/nccl_device/impl/reduce_copy__types.h#L76)
- 函数 [operator() · L78](../../../src/include/nccl_device/impl/reduce_copy__types.h#L78)
- 结构体 [OpSum&lt;__nv_fp8_e5m2&gt; · L90](../../../src/include/nccl_device/impl/reduce_copy__types.h#L90)
- 函数 [operator() · L92](../../../src/include/nccl_device/impl/reduce_copy__types.h#L92)

## src/include/nccl_device/impl/vector__funcs.h

[整个文件](../../../src/include/nccl_device/impl/vector__funcs.h)

- 函数 [getAlignment · L34](../../../src/include/nccl_device/impl/vector__funcs.h#L34)
- 函数 [safeDiv · L40](../../../src/include/nccl_device/impl/vector__funcs.h#L40)
- 函数 [computeCommonAlignment · L48](../../../src/include/nccl_device/impl/vector__funcs.h#L48)
- 函数 [computeAlignmentForPackSize · L74](../../../src/include/nccl_device/impl/vector__funcs.h#L74)
- 函数 [tryLambdaAlignmentForPackSize · L95](../../../src/include/nccl_device/impl/vector__funcs.h#L95)
- 结构体 [AlignmentResult · L156](../../../src/include/nccl_device/impl/vector__funcs.h#L156)
- 函数 [tryPointerPairAlignmentForPackSize · L189](../../../src/include/nccl_device/impl/vector__funcs.h#L189)
- 函数 [computePointerPairAlignmentWithFallback · L229](../../../src/include/nccl_device/impl/vector__funcs.h#L229)
- 函数 [tryStridedAlignmentForPackSize · L249](../../../src/include/nccl_device/impl/vector__funcs.h#L249)
- 函数 [tryComplexStridedAlignmentForPackSize · L271](../../../src/include/nccl_device/impl/vector__funcs.h#L271)
- 函数 [computeStridedAlignmentWithFallback · L323](../../../src/include/nccl_device/impl/vector__funcs.h#L323)
- 结构体 [PackAccess · L349](../../../src/include/nccl_device/impl/vector__funcs.h#L349)
- 结构体 [PackAccess&lt;T, 1&gt; · L360](../../../src/include/nccl_device/impl/vector__funcs.h#L360)
- 结构体 [PackAccess&lt;T, 0&gt; · L373](../../../src/include/nccl_device/impl/vector__funcs.h#L373)
- 结构体 [CastPackImpl · L391](../../../src/include/nccl_device/impl/vector__funcs.h#L391)
- 函数 [run · L392](../../../src/include/nccl_device/impl/vector__funcs.h#L392)
- 结构体 [CastPackImpl&lt;Y, X, n, true&gt; · L407](../../../src/include/nccl_device/impl/vector__funcs.h#L407)
- 函数 [run · L408](../../../src/include/nccl_device/impl/vector__funcs.h#L408)
- 联合体 [Half2PackAccess · L441](../../../src/include/nccl_device/impl/vector__funcs.h#L441)
- 联合体 [Float2PackAccess · L445](../../../src/include/nccl_device/impl/vector__funcs.h#L445)
- 联合体 [Half2PackAccess · L466](../../../src/include/nccl_device/impl/vector__funcs.h#L466)
- 联合体 [Bf162PackAccess · L487](../../../src/include/nccl_device/impl/vector__funcs.h#L487)
- 联合体 [Float2PackAccess · L491](../../../src/include/nccl_device/impl/vector__funcs.h#L491)
- 联合体 [Bf162PackAccess · L512](../../../src/include/nccl_device/impl/vector__funcs.h#L512)
- 联合体 [Float2PackAccess · L516](../../../src/include/nccl_device/impl/vector__funcs.h#L516)
- 联合体 [HalfRawAccess · L534](../../../src/include/nccl_device/impl/vector__funcs.h#L534)
- 联合体 [Fp8E4m3Access1 · L538](../../../src/include/nccl_device/impl/vector__funcs.h#L538)
- 联合体 [Half2RawAccess · L554](../../../src/include/nccl_device/impl/vector__funcs.h#L554)
- 联合体 [Half2PackAccess · L558](../../../src/include/nccl_device/impl/vector__funcs.h#L558)
- 联合体 [Fp8E4m3Access2 · L562](../../../src/include/nccl_device/impl/vector__funcs.h#L562)
- 联合体 [HalfRawAccess · L587](../../../src/include/nccl_device/impl/vector__funcs.h#L587)
- 联合体 [Fp8E5m2Access1 · L591](../../../src/include/nccl_device/impl/vector__funcs.h#L591)
- 联合体 [Half2RawAccess · L607](../../../src/include/nccl_device/impl/vector__funcs.h#L607)
- 联合体 [Half2PackAccess · L611](../../../src/include/nccl_device/impl/vector__funcs.h#L611)
- 联合体 [Fp8E5m2Access2 · L615](../../../src/include/nccl_device/impl/vector__funcs.h#L615)
- 联合体 [HalfRawAccess · L640](../../../src/include/nccl_device/impl/vector__funcs.h#L640)
- 联合体 [Fp8E4m3Access1 · L644](../../../src/include/nccl_device/impl/vector__funcs.h#L644)
- 联合体 [Half2RawAccess · L658](../../../src/include/nccl_device/impl/vector__funcs.h#L658)
- 联合体 [Half2PackAccess · L662](../../../src/include/nccl_device/impl/vector__funcs.h#L662)
- 联合体 [Fp8E4m3Access2 · L667](../../../src/include/nccl_device/impl/vector__funcs.h#L667)
- 联合体 [HalfRawAccess · L691](../../../src/include/nccl_device/impl/vector__funcs.h#L691)
- 联合体 [Fp8E5m2Access1 · L695](../../../src/include/nccl_device/impl/vector__funcs.h#L695)
- 联合体 [Half2RawAccess · L709](../../../src/include/nccl_device/impl/vector__funcs.h#L709)
- 联合体 [Half2PackAccess · L713](../../../src/include/nccl_device/impl/vector__funcs.h#L713)
- 联合体 [Fp8E5m2Access2 · L718](../../../src/include/nccl_device/impl/vector__funcs.h#L718)
- 联合体 [Int8PackAccess4 · L772](../../../src/include/nccl_device/impl/vector__funcs.h#L772)
- 联合体 [PackU8 · L790](../../../src/include/nccl_device/impl/vector__funcs.h#L790)
- 联合体 [Half2PackAccess · L809](../../../src/include/nccl_device/impl/vector__funcs.h#L809)
- 联合体 [Bf16PackAccess2 · L836](../../../src/include/nccl_device/impl/vector__funcs.h#L836)

## src/include/nccl_device/impl/vector__types.h

[整个文件](../../../src/include/nccl_device/impl/vector__types.h)

- 结构体 [EltPack · L36](../../../src/include/nccl_device/impl/vector__types.h#L36)
- 函数 [elts · L48](../../../src/include/nccl_device/impl/vector__types.h#L48)
- 函数 [elts · L51](../../../src/include/nccl_device/impl/vector__types.h#L51)
- 结构体 [EltPack&lt;T, 0&gt; · L58](../../../src/include/nccl_device/impl/vector__types.h#L58)
- 函数 [elts · L65](../../../src/include/nccl_device/impl/vector__types.h#L65)
- 函数 [elts · L68](../../../src/include/nccl_device/impl/vector__types.h#L68)
- 结构体 [AccumulateType · L88](../../../src/include/nccl_device/impl/vector__types.h#L88)
- 结构体 [AccumulateType&lt;Red&lt;T&gt;&gt; · L95](../../../src/include/nccl_device/impl/vector__types.h#L95)
- 结构体 [AccumulateType&lt;OpSum&lt;half&gt;&gt; · L101](../../../src/include/nccl_device/impl/vector__types.h#L101)
- 结构体 [AccumulateType&lt;OpSum&lt;__nv_bfloat16&gt;&gt; · L107](../../../src/include/nccl_device/impl/vector__types.h#L107)
- 结构体 [AccumulateType&lt;OpSum&lt;__nv_fp8_e4m3&gt;&gt; · L114](../../../src/include/nccl_device/impl/vector__types.h#L114)
- 结构体 [AccumulateType&lt;OpSum&lt;__nv_fp8_e5m2&gt;&gt; · L118](../../../src/include/nccl_device/impl/vector__types.h#L118)
- 结构体 [MinMultimemType · L129](../../../src/include/nccl_device/impl/vector__types.h#L129)
- 结构体 [MinMultimemType&lt;half&gt; · L134](../../../src/include/nccl_device/impl/vector__types.h#L134)
- 结构体 [MinMultimemType&lt;__nv_bfloat16&gt; · L140](../../../src/include/nccl_device/impl/vector__types.h#L140)
- 结构体 [MinMultimemType&lt;__nv_fp8_e4m3&gt; · L148](../../../src/include/nccl_device/impl/vector__types.h#L148)
- 结构体 [MinMultimemType&lt;__nv_fp8_e5m2&gt; · L153](../../../src/include/nccl_device/impl/vector__types.h#L153)

## src/include/nccl_device/ll_a2a.h

[整个文件](../../../src/include/nccl_device/ll_a2a.h)

- 结构体 [ncclLLA2ASession · L19](../../../src/include/nccl_device/ll_a2a.h#L19)

## src/include/nccl_device/lsa_barrier.h

[整个文件](../../../src/include/nccl_device/lsa_barrier.h)

- 结构体 [ncclLsaBarrierSession · L19](../../../src/include/nccl_device/lsa_barrier.h#L19)

## src/include/nccl_device/lsa_flow.h

[整个文件](../../../src/include/nccl_device/lsa_flow.h)

- 结构体 [ncclLsaFlowConn · L19](../../../src/include/nccl_device/lsa_flow.h#L19)

## src/include/nccl_device/net_device.h

[整个文件](../../../src/include/nccl_device/net_device.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/ptr.h

[整个文件](../../../src/include/nccl_device/ptr.h)

- 结构体 [ncclSymPtr · L15](../../../src/include/nccl_device/ptr.h#L15)

## src/include/nccl_device/reduce_copy.h

[整个文件](../../../src/include/nccl_device/reduce_copy.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device/utility.h

[整个文件](../../../src/include/nccl_device/utility.h)

- 函数 [testAbort · L73](../../../src/include/nccl_device/utility.h#L73)
- 函数 [testAbort · L83](../../../src/include/nccl_device/utility.h#L83)
- 结构体 [always_false · L101](../../../src/include/nccl_device/utility.h#L101)
- 结构体 [ValueAsType · L106](../../../src/include/nccl_device/utility.h#L106)
- 函数 [opaqueZero · L114](../../../src/include/nccl_device/utility.h#L114)
- 函数 [divUp · L121](../../../src/include/nccl_device/utility.h#L121)
- 函数 [roundUp · L126](../../../src/include/nccl_device/utility.h#L126)
- 函数 [roundDown · L130](../../../src/include/nccl_device/utility.h#L130)
- 函数 [alignUp · L136](../../../src/include/nccl_device/utility.h#L136)
- 函数 [alignUp · L140](../../../src/include/nccl_device/utility.h#L140)
- 函数 [alignUp · L145](../../../src/include/nccl_device/utility.h#L145)
- 函数 [alignDown · L151](../../../src/include/nccl_device/utility.h#L151)
- 函数 [alignDown · L155](../../../src/include/nccl_device/utility.h#L155)
- 函数 [alignDown · L160](../../../src/include/nccl_device/utility.h#L160)
- 函数 [add4G · L165](../../../src/include/nccl_device/utility.h#L165)
- 函数 [isPow2 · L176](../../../src/include/nccl_device/utility.h#L176)
- 函数 [rollingLessEq · L181](../../../src/include/nccl_device/utility.h#L181)
- 函数 [rollingLessThan · L187](../../../src/include/nccl_device/utility.h#L187)
- 函数 [idivRcp32 · L192](../../../src/include/nccl_device/utility.h#L192)
- 函数 [idivRcp64 · L195](../../../src/include/nccl_device/utility.h#L195)
- 函数 [mul32hi · L199](../../../src/include/nccl_device/utility.h#L199)
- 函数 [mul64hi · L206](../../../src/include/nccl_device/utility.h#L206)
- 函数 [imulRcp32 · L219](../../../src/include/nccl_device/utility.h#L219)
- 函数 [imulRcp64 · L227](../../../src/include/nccl_device/utility.h#L227)
- 函数 [idivmodFast32 · L238](../../../src/include/nccl_device/utility.h#L238)
- 函数 [idivmodFast64 · L248](../../../src/include/nccl_device/utility.h#L248)
- 函数 [idivFast32 · L259](../../../src/include/nccl_device/utility.h#L259)
- 函数 [idivFast64 · L264](../../../src/include/nccl_device/utility.h#L264)
- 函数 [imodFast32 · L270](../../../src/include/nccl_device/utility.h#L270)
- 函数 [imodFast64 · L275](../../../src/include/nccl_device/utility.h#L275)
- 函数 [idivRcp64_upto64 · L284](../../../src/include/nccl_device/utility.h#L284)
- 函数 [idivRcp32_upto64 · L311](../../../src/include/nccl_device/utility.h#L311)
- 函数 [atomicLoad · L331](../../../src/include/nccl_device/utility.h#L331)
- 函数 [atomicStore · L349](../../../src/include/nccl_device/utility.h#L349)
- 函数 [lane · L370](../../../src/include/nccl_device/utility.h#L370)
- 函数 [lanemask_lt · L375](../../../src/include/nccl_device/utility.h#L375)
- 函数 [loadConstLdg · L386](../../../src/include/nccl_device/utility.h#L386)
- 函数 [loadConst · L428](../../../src/include/nccl_device/utility.h#L428)
- 结构体 [IntSeq · L444](../../../src/include/nccl_device/utility.h#L444)
- 结构体 [IntSeqUpTo · L447](../../../src/include/nccl_device/utility.h#L447)
- 结构体 [IntSeqUpTo&lt;n, n, i...&gt; · L449](../../../src/include/nccl_device/utility.h#L449)
- 结构体 [Present&lt;&gt; · L457](../../../src/include/nccl_device/utility.h#L457)
- 结构体 [Present&lt;H, T...&gt; · L459](../../../src/include/nccl_device/utility.h#L459)
- 函数 [get · L466](../../../src/include/nccl_device/utility.h#L466)
- 函数 [get · L470](../../../src/include/nccl_device/utility.h#L470)
- 函数 [present · L475](../../../src/include/nccl_device/utility.h#L475)
- 结构体 [Absent · L483](../../../src/include/nccl_device/utility.h#L483)
- 结构体 [Optional · L486](../../../src/include/nccl_device/utility.h#L486)
- 函数 [Optional · L493](../../../src/include/nccl_device/utility.h#L493)
- 函数 [Optional · L494](../../../src/include/nccl_device/utility.h#L494)
- 函数 [Optional · L498](../../../src/include/nccl_device/utility.h#L498)
- 函数 [Optional · L505](../../../src/include/nccl_device/utility.h#L505)
