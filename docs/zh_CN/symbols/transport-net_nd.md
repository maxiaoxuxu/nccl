# transport-net_nd 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/transport/net_nd/common.cc

[整个文件](../../../src/transport/net_nd/common.cc)

- 函数 [ncclNdStatsRequireReport · L30](../../../src/transport/net_nd/common.cc#L30)
- 函数 [ncclNdStatsAddResource · L51](../../../src/transport/net_nd/common.cc#L51)
- 函数 [ncclNdStatsRemoveResource · L59](../../../src/transport/net_nd/common.cc#L59)
- 函数 [ncclNdPrimaryDevice · L68](../../../src/transport/net_nd/common.cc#L68)
- 函数 [ncclNdStatsConnectionStart · L79](../../../src/transport/net_nd/common.cc#L79)
- 函数 [ncclNdStatsConnectionComplete · L91](../../../src/transport/net_nd/common.cc#L91)
- 函数 [ncclNdStatsConnectionFailed · L100](../../../src/transport/net_nd/common.cc#L100)
- 函数 [ncclNdLogStats · L111](../../../src/transport/net_nd/common.cc#L111)
- 函数 [ncclNdTryAcquireDeviceComm · L159](../../../src/transport/net_nd/common.cc#L159)
- 函数 [ncclNdTryAcquireComm · L175](../../../src/transport/net_nd/common.cc#L175)
- 函数 [ncclNdReleaseComm · L203](../../../src/transport/net_nd/common.cc#L203)
- 函数 [ncclNdGetRequest · L215](../../../src/transport/net_nd/common.cc#L215)
- 函数 [ncclNdFreeRequest · L245](../../../src/transport/net_nd/common.cc#L245)

## src/transport/net_nd/common.h

[整个文件](../../../src/transport/net_nd/common.h)

- 枚举 [ncclNdMemType · L38](../../../src/transport/net_nd/common.h#L38)
- 结构体 [ncclNdMr · L86](../../../src/transport/net_nd/common.h#L86)
- 结构体 [ncclNdMrCache · L101](../../../src/transport/net_nd/common.h#L101)
- 结构体 [ncclNdStats · L107](../../../src/transport/net_nd/common.h#L107)
- 结构体 [ncclNdGpuCaps · L142](../../../src/transport/net_nd/common.h#L142)
- 结构体 [ncclNdDev · L150](../../../src/transport/net_nd/common.h#L150)
- 函数 [ncclNdConfiguredInlineBytes · L173](../../../src/transport/net_nd/common.h#L173)
- 结构体 [ncclNdMergedDev · L179](../../../src/transport/net_nd/common.h#L179)
- 结构体 [ncclNdDevInfo · L193](../../../src/transport/net_nd/common.h#L193)
- 结构体 [ncclNdProtocolHeader · L217](../../../src/transport/net_nd/common.h#L217)
- 结构体 [ncclNdConnectionMetadata · L229](../../../src/transport/net_nd/common.h#L229)
- 函数 [ncclNdConnectionOptions · L236](../../../src/transport/net_nd/common.h#L236)
- 结构体 [ncclNdConnectionSetup · L242](../../../src/transport/net_nd/common.h#L242)
- 结构体 [ncclNdQp · L252](../../../src/transport/net_nd/common.h#L252)
- 结构体 [ncclNdSendFifo · L266](../../../src/transport/net_nd/common.h#L266)
- 结构体 [ncclNdRemCompletionRecords · L276](../../../src/transport/net_nd/common.h#L276)
- 结构体 [ncclNdNetCommDevBase · L284](../../../src/transport/net_nd/common.h#L284)
- 结构体 [ncclNdSendCommDev · L293](../../../src/transport/net_nd/common.h#L293)
- 结构体 [ncclNdMrHandle · L302](../../../src/transport/net_nd/common.h#L302)
- 结构体 [ncclNdScopedSrwLock · L313](../../../src/transport/net_nd/common.h#L313)
- 函数 [ncclNdScopedSrwLock · L314](../../../src/transport/net_nd/common.h#L314)
- 函数 [~ncclNdScopedSrwLock · L317](../../../src/transport/net_nd/common.h#L317)
- 结构体 [ncclNdRequest · L326](../../../src/transport/net_nd/common.h#L326)
- 结构体 [ncclNdNetCommBase · L358](../../../src/transport/net_nd/common.h#L358)
- 结构体 [ncclNdSendComm · L395](../../../src/transport/net_nd/common.h#L395)
- 结构体 [ncclNdRecvCommDev · L417](../../../src/transport/net_nd/common.h#L417)
- 结构体 [ncclNdRecvComm · L426](../../../src/transport/net_nd/common.h#L426)
- 结构体 [ncclNdHandle · L445](../../../src/transport/net_nd/common.h#L445)
- 结构体 [ncclNdListenComm · L453](../../../src/transport/net_nd/common.h#L453)
- 枚举 [ncclNdConnectState · L465](../../../src/transport/net_nd/common.h#L465)
- 枚举 [ncclNdAcceptState · L479](../../../src/transport/net_nd/common.h#L479)
- 函数 [ncclNdGetNetCommDevBase · L495](../../../src/transport/net_nd/common.h#L495)
- 函数 [ncclNdGetFatalError · L508](../../../src/transport/net_nd/common.h#L508)
- 函数 [ncclNdSetFatalError · L512](../../../src/transport/net_nd/common.h#L512)
- 函数 [ncclNdStatsInit · L524](../../../src/transport/net_nd/common.h#L524)
- 函数 [ncclNdAddEvent · L570](../../../src/transport/net_nd/common.h#L570)

## src/transport/net_nd/connect.cc

[整个文件](../../../src/transport/net_nd/connect.cc)

- 函数 [ncclNdConnectionDeadline · L15](../../../src/transport/net_nd/connect.cc#L15)
- 函数 [ncclNdConnectionExpired · L23](../../../src/transport/net_nd/connect.cc#L23)
- 函数 [ncclNdInitProtocolHeader · L28](../../../src/transport/net_nd/connect.cc#L28)
- 函数 [ncclNdValidateProtocolHeader · L38](../../../src/transport/net_nd/connect.cc#L38)
- 函数 [ncclNdValidateConnectionMetadata · L53](../../../src/transport/net_nd/connect.cc#L53)
- 函数 [ncclNdValidateConnectionSetup · L73](../../../src/transport/net_nd/connect.cc#L73)
- 函数 [ncclNdSetVProps · L95](../../../src/transport/net_nd/connect.cc#L95)
- 函数 [ncclNdAbortConnect · L108](../../../src/transport/net_nd/connect.cc#L108)
- 函数 [ncclNdAbortAccept · L122](../../../src/transport/net_nd/connect.cc#L122)
- 函数 [ncclNdStartConnectQp · L136](../../../src/transport/net_nd/connect.cc#L136)
- 函数 [ncclNdArmCqErrorNotification · L157](../../../src/transport/net_nd/connect.cc#L157)
- 函数 [ncclNdReleaseCq · L165](../../../src/transport/net_nd/connect.cc#L165)
- 函数 [ncclNdListen · L180](../../../src/transport/net_nd/connect.cc#L180)
- 函数 [ncclNdConnect · L247](../../../src/transport/net_nd/connect.cc#L247)
- 函数 [ncclNdAccept · L585](../../../src/transport/net_nd/connect.cc#L585)
- 函数 [ncclNdDiscardRequests · L930](../../../src/transport/net_nd/connect.cc#L930)
- 函数 [ncclNdCloseSend · L946](../../../src/transport/net_nd/connect.cc#L946)
- 函数 [ncclNdCloseRecv · L1022](../../../src/transport/net_nd/connect.cc#L1022)
- 函数 [ncclNdCloseListen · L1098](../../../src/transport/net_nd/connect.cc#L1098)

## src/transport/net_nd/init.cc

[整个文件](../../../src/transport/net_nd/init.cc)

- 结构体 [ncclNdAdapterEntry · L26](../../../src/transport/net_nd/init.cc#L26)
- 函数 [ncclNdAddressRank · L33](../../../src/transport/net_nd/init.cc#L33)
- 函数 [ncclNdSameAddress · L46](../../../src/transport/net_nd/init.cc#L46)
- 函数 [ncclNdGetInterfaceRow · L59](../../../src/transport/net_nd/init.cc#L59)
- 函数 [ncclNdReadNetCfgInstanceId · L77](../../../src/transport/net_nd/init.cc#L77)
- 函数 [ncclNdGetPciPath · L91](../../../src/transport/net_nd/init.cc#L91)
- 函数 [ncclNdGetWindowsProperties · L133](../../../src/transport/net_nd/init.cc#L133)
- 函数 [ncclNdRecordDeviceInterfaceChange · L159](../../../src/transport/net_nd/init.cc#L159)
- 函数 [ncclNdRecordInterfaceChange · L176](../../../src/transport/net_nd/init.cc#L176)
- 函数 [ncclNdInterfaceChangeCallback · L184](../../../src/transport/net_nd/init.cc#L184)
- 函数 [ncclNdStartInterfaceMonitor · L197](../../../src/transport/net_nd/init.cc#L197)
- 函数 [ncclNdStopInterfaceMonitor · L211](../../../src/transport/net_nd/init.cc#L211)
- 函数 [ncclNdInterfaceMonitorActive · L219](../../../src/transport/net_nd/init.cc#L219)
- 函数 [ncclNdCheckAdapterHealth · L224](../../../src/transport/net_nd/init.cc#L224)
- 函数 [ncclNdCleanupInitFailure · L266](../../../src/transport/net_nd/init.cc#L266)
- 函数 [ncclNdInitDevices · L285](../../../src/transport/net_nd/init.cc#L285)
- 函数 [ncclNdInit · L530](../../../src/transport/net_nd/init.cc#L530)
- 函数 [ncclNdDevices · L546](../../../src/transport/net_nd/init.cc#L546)
- 函数 [ncclNdGetProperties · L552](../../../src/transport/net_nd/init.cc#L552)
- 函数 [ncclNdMakeVDeviceInternal · L627](../../../src/transport/net_nd/init.cc#L627)
- 函数 [ncclNdMakeVDevice · L681](../../../src/transport/net_nd/init.cc#L681)
- 函数 [ncclNdSetNetAttr · L687](../../../src/transport/net_nd/init.cc#L687)
- 函数 [ncclNdFinalizeDevices · L692](../../../src/transport/net_nd/init.cc#L692)
- 函数 [ncclNdFinalize · L728](../../../src/transport/net_nd/init.cc#L728)

## src/transport/net_nd/nddef.h

[整个文件](../../../src/transport/net_nd/nddef.h)

- 结构体 [_ND2_ADAPTER_INFO · L57](../../../src/transport/net_nd/nddef.h#L57)
- 结构体 [_ND2_ADAPTER_INFO32 · L82](../../../src/transport/net_nd/nddef.h#L82)
- 枚举 [_ND2_REQUEST_TYPE · L107](../../../src/transport/net_nd/nddef.h#L107)
- 结构体 [_ND2_RESULT · L116](../../../src/transport/net_nd/nddef.h#L116)
- 结构体 [_ND2_SGE · L124](../../../src/transport/net_nd/nddef.h#L124)

## src/transport/net_nd/ndspi.h

[整个文件](../../../src/transport/net_nd/ndspi.h)

- 结构体 [_ND_ADAPTER_INFO1 · L745](../../../src/transport/net_nd/ndspi.h#L745)
- 结构体 [_ND_RESULT · L768](../../../src/transport/net_nd/ndspi.h#L768)
- 结构体 [_ND_MW_DESCRIPTOR · L776](../../../src/transport/net_nd/ndspi.h#L776)
- 结构体 [_ND_SGE · L785](../../../src/transport/net_nd/ndspi.h#L785)

## src/transport/net_nd/ndstatus.h

[整个文件](../../../src/transport/net_nd/ndstatus.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/transport/net_nd/ndwrap.cc

[整个文件](../../../src/transport/net_nd/ndwrap.cc)

- 函数 [wrap_nd_get_provider · L32](../../../src/transport/net_nd/ndwrap.cc#L32)
- 函数 [ncclNdIsV2Provider · L38](../../../src/transport/net_nd/ndwrap.cc#L38)
- 函数 [ncclNdEnumerateProviders · L49](../../../src/transport/net_nd/ndwrap.cc#L49)
- 函数 [wrap_nd_symbols · L183](../../../src/transport/net_nd/ndwrap.cc#L183)
- 函数 [wrap_nd_unload · L224](../../../src/transport/net_nd/ndwrap.cc#L224)
- 函数 [wrap_nd_resolve_address · L252](../../../src/transport/net_nd/ndwrap.cc#L252)
- 函数 [wrap_nd_query_address_list · L263](../../../src/transport/net_nd/ndwrap.cc#L263)
- 函数 [wrap_nd_open_adapter · L274](../../../src/transport/net_nd/ndwrap.cc#L274)
- 函数 [wrap_nd_query_adapter · L284](../../../src/transport/net_nd/ndwrap.cc#L284)
- 函数 [wrap_nd_create_overlapped_file · L303](../../../src/transport/net_nd/ndwrap.cc#L303)
- 函数 [wrap_nd_create_completion_queue · L313](../../../src/transport/net_nd/ndwrap.cc#L313)
- 函数 [wrap_nd_create_memory_region · L324](../../../src/transport/net_nd/ndwrap.cc#L324)
- 函数 [wrap_nd_create_queue_pair · L335](../../../src/transport/net_nd/ndwrap.cc#L335)
- 函数 [wrap_nd_create_connector · L351](../../../src/transport/net_nd/ndwrap.cc#L351)
- 函数 [wrap_nd_create_listener · L362](../../../src/transport/net_nd/ndwrap.cc#L362)
- 函数 [wrap_nd_register_memory · L373](../../../src/transport/net_nd/ndwrap.cc#L373)
- 函数 [wrap_nd_deregister_memory · L387](../../../src/transport/net_nd/ndwrap.cc#L387)
- 函数 [wrap_nd_notify · L400](../../../src/transport/net_nd/ndwrap.cc#L400)
- 函数 [wrap_nd_write · L410](../../../src/transport/net_nd/ndwrap.cc#L410)
- 函数 [wrap_nd_connector_bind · L422](../../../src/transport/net_nd/ndwrap.cc#L422)
- 函数 [wrap_nd_connect · L432](../../../src/transport/net_nd/ndwrap.cc#L432)
- 函数 [wrap_nd_cq_get_status · L445](../../../src/transport/net_nd/ndwrap.cc#L445)
- 函数 [wrap_nd_cq_cancel_notifications · L456](../../../src/transport/net_nd/ndwrap.cc#L456)
- 函数 [wrap_nd_complete_connect · L466](../../../src/transport/net_nd/ndwrap.cc#L466)
- 函数 [wrap_nd_accept · L477](../../../src/transport/net_nd/ndwrap.cc#L477)
- 函数 [wrap_nd_bind · L489](../../../src/transport/net_nd/ndwrap.cc#L489)
- 函数 [wrap_nd_listen · L499](../../../src/transport/net_nd/ndwrap.cc#L499)
- 函数 [wrap_nd_get_listener_address · L509](../../../src/transport/net_nd/ndwrap.cc#L509)
- 函数 [wrap_nd_get_connection_request · L520](../../../src/transport/net_nd/ndwrap.cc#L520)
- 函数 [wrap_nd_listener_get_request_status · L532](../../../src/transport/net_nd/ndwrap.cc#L532)
- 函数 [wrap_nd_connector_get_status · L550](../../../src/transport/net_nd/ndwrap.cc#L550)
- 函数 [wrap_nd_prepare_overlapped · L571](../../../src/transport/net_nd/ndwrap.cc#L571)
- 函数 [wrap_nd_close_overlapped · L589](../../../src/transport/net_nd/ndwrap.cc#L589)

## src/transport/net_nd/ndwrap.h

[整个文件](../../../src/transport/net_nd/ndwrap.h)

- 函数 [wrap_nd_get_local_token · L43](../../../src/transport/net_nd/ndwrap.h#L43)
- 函数 [wrap_nd_get_remote_token · L46](../../../src/transport/net_nd/ndwrap.h#L46)
- 函数 [wrap_nd_get_results · L51](../../../src/transport/net_nd/ndwrap.h#L51)
- 函数 [wrap_nd_release · L86](../../../src/transport/net_nd/ndwrap.h#L86)

## src/transport/net_nd/p2p.cc

[整个文件](../../../src/transport/net_nd/p2p.cc)

- 枚举 [ncclNdCompletionOp · L12](../../../src/transport/net_nd/p2p.cc#L12)
- 结构体 [ncclNdDecodedCompletionContext · L39](../../../src/transport/net_nd/p2p.cc#L39)
- 函数 [ncclNdMakeCompletionContext · L47](../../../src/transport/net_nd/p2p.cc#L47)
- 函数 [ncclNdDecodeCompletionContext · L57](../../../src/transport/net_nd/p2p.cc#L57)
- 函数 [ncclNdCompletionCanFailover · L70](../../../src/transport/net_nd/p2p.cc#L70)
- 函数 [ncclNdGetCtsSlot · L81](../../../src/transport/net_nd/p2p.cc#L81)
- 函数 [ncclNdCompletionGeneration · L86](../../../src/transport/net_nd/p2p.cc#L86)
- 函数 [ncclNdCompletionValue · L93](../../../src/transport/net_nd/p2p.cc#L93)
- 函数 [ncclNdSendWasAcknowledged · L98](../../../src/transport/net_nd/p2p.cc#L98)
- 函数 [ncclNdInlineWriteFlag · L108](../../../src/transport/net_nd/p2p.cc#L108)
- 函数 [ncclNdSelectQp · L116](../../../src/transport/net_nd/p2p.cc#L116)
- 函数 [ncclNdDataDeadline · L142](../../../src/transport/net_nd/p2p.cc#L142)
- 枚举 [ncclNdDataFailureKind · L149](../../../src/transport/net_nd/p2p.cc#L149)
- 函数 [ncclNdFailDataPath · L156](../../../src/transport/net_nd/p2p.cc#L156)
- 函数 [ncclNdHandleRailFailure · L178](../../../src/transport/net_nd/p2p.cc#L178)
- 函数 [ncclNdCheckProvider · L202](../../../src/transport/net_nd/p2p.cc#L202)
- 函数 [ncclNdCheckPeer · L268](../../../src/transport/net_nd/p2p.cc#L268)
- 函数 [ncclNdNotifyPeerClosing · L323](../../../src/transport/net_nd/p2p.cc#L323)
- 函数 [ncclNdPostRequestOnQp · L336](../../../src/transport/net_nd/p2p.cc#L336)
- 函数 [ncclNdPostRequestWithFailover · L418](../../../src/transport/net_nd/p2p.cc#L418)
- 函数 [ncclNdIrecv · L447](../../../src/transport/net_nd/p2p.cc#L447)
- 函数 [ncclNdIsend · L541](../../../src/transport/net_nd/p2p.cc#L541)
- 函数 [ncclNdIflush · L655](../../../src/transport/net_nd/p2p.cc#L655)
- 函数 [ncclNdTest · L692](../../../src/transport/net_nd/p2p.cc#L692)

## src/transport/net_nd/reg.cc

[整个文件](../../../src/transport/net_nd/reg.cc)

- 结构体 [ncclNdSyncMemopsState · L20](../../../src/transport/net_nd/reg.cc#L20)
- 函数 [ncclNdCudaCallResult · L29](../../../src/transport/net_nd/reg.cc#L29)
- 函数 [ncclNdAcquireSyncMemops · L40](../../../src/transport/net_nd/reg.cc#L40)
- 函数 [ncclNdReleaseSyncMemops · L80](../../../src/transport/net_nd/reg.cc#L80)
- 函数 [ncclNdGetPageSize · L111](../../../src/transport/net_nd/reg.cc#L111)
- 函数 [ncclNdGetGpuDirectSupport · L123](../../../src/transport/net_nd/reg.cc#L123)
- 函数 [ncclNdMrCacheLookup · L236](../../../src/transport/net_nd/reg.cc#L236)
- 函数 [ncclNdMrCacheInsert · L248](../../../src/transport/net_nd/reg.cc#L248)
- 函数 [ncclNdMrCacheRemove · L273](../../../src/transport/net_nd/reg.cc#L273)
- 函数 [ncclNdRegMrDevice · L293](../../../src/transport/net_nd/reg.cc#L293)
- 函数 [ncclNdDeregMrDevice · L372](../../../src/transport/net_nd/reg.cc#L372)
- 函数 [ncclNdRegMr · L418](../../../src/transport/net_nd/reg.cc#L418)
- 函数 [ncclNdRegMrDmaBuf · L489](../../../src/transport/net_nd/reg.cc#L489)
- 函数 [ncclNdDeregMr · L495](../../../src/transport/net_nd/reg.cc#L495)
- 函数 [ncclNdFinalizeMrCache · L531](../../../src/transport/net_nd/reg.cc#L531)
