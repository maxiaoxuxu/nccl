# include 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/include/alloc.h

[整个文件](../../../src/include/alloc.h)

- 函数 [ncclSizeOfT · L35](../../../src/include/alloc.h#L35)
- 函数 [ncclSizeOfT&lt;void&gt; · L39](../../../src/include/alloc.h#L39)
- 结构体 [ncclDeleterWrapper · L45](../../../src/include/alloc.h#L45)
- 函数 [operator() · L47](../../../src/include/alloc.h#L47)
- 函数 [ncclCuMemHostAllocDebug · L60](../../../src/include/alloc.h#L60)
- 函数 [ncclCuMemHostFree · L109](../../../src/include/alloc.h#L109)
- 函数 [ncclCuMemHostAllocDebug · L126](../../../src/include/alloc.h#L126)
- 函数 [ncclCuMemHostFree · L140](../../../src/include/alloc.h#L140)
- 函数 [ncclCudaHostCallocDebug · L148](../../../src/include/alloc.h#L148)
- 函数 [ncclCudaHostFree · L165](../../../src/include/alloc.h#L165)
- 函数 [ncclCallocDebug · L173](../../../src/include/alloc.h#L173)
- 函数 [ncclCallocDebug · L193](../../../src/include/alloc.h#L193)
- 函数 [ncclCallocDebug · L202](../../../src/include/alloc.h#L202)
- 函数 [ncclReallocDebug · L215](../../../src/include/alloc.h#L215)
- 函数 [ncclCuMemMapAndSetAccess · L246](../../../src/include/alloc.h#L246)
- 函数 [ncclCuMemAllocAddr · L261](../../../src/include/alloc.h#L261)
- 函数 [ncclCuMemFreeAddr · L278](../../../src/include/alloc.h#L278)
- 函数 [ncclCuMemAlloc · L312](../../../src/include/alloc.h#L312)
- 函数 [ncclCuMemFree · L348](../../../src/include/alloc.h#L348)
- 函数 [ncclCuMemGetAddressRange · L389](../../../src/include/alloc.h#L389)
- 函数 [ncclCuMemAlloc · L444](../../../src/include/alloc.h#L444)
- 函数 [ncclCuMemFree · L449](../../../src/include/alloc.h#L449)
- 函数 [ncclCuMemAllocAddr · L454](../../../src/include/alloc.h#L454)
- 函数 [ncclCuMemFreeAddr · L459](../../../src/include/alloc.h#L459)
- 函数 [ncclCuMemGetAddressRange · L464](../../../src/include/alloc.h#L464)
- 函数 [ncclCudaMallocDebug · L474](../../../src/include/alloc.h#L474)
- 函数 [ncclCudaCallocDebug · L499](../../../src/include/alloc.h#L499)
- 函数 [ncclCudaCallocAsyncDebug · L530](../../../src/include/alloc.h#L530)
- 函数 [ncclCudaMemcpy · L557](../../../src/include/alloc.h#L557)
- 函数 [ncclCudaMemcpyAsync · L573](../../../src/include/alloc.h#L573)
- 函数 [ncclCudaMemsetSync · L583](../../../src/include/alloc.h#L583)
- 函数 [ncclCudaFree · L595](../../../src/include/alloc.h#L595)
- 函数 [ncclIbMallocDebug · L618](../../../src/include/alloc.h#L618)

## src/include/allocator.h

[整个文件](../../../src/include/allocator.h)

- 结构体 [ncclSpace · L20](../../../src/include/allocator.h#L20)
- 结构体 [ncclShadowPool · L42](../../../src/include/allocator.h#L42)
- 函数 [ncclShadowPoolAlloc · L57](../../../src/include/allocator.h#L57)
- 函数 [ncclShadowPoolToHost · L68](../../../src/include/allocator.h#L68)

## src/include/argcheck.h

[整个文件](../../../src/include/argcheck.h)

- 结构体 [ncclArgsInfo · L14](../../../src/include/argcheck.h#L14)

## src/include/bitops.h

[整个文件](../../../src/include/bitops.h)

- 函数 [minval · L25](../../../src/include/bitops.h#L25)
- 函数 [minval · L29](../../../src/include/bitops.h#L29)
- 函数 [maxval · L38](../../../src/include/bitops.h#L38)
- 函数 [maxval · L42](../../../src/include/bitops.h#L42)
- 函数 [divUp · L62](../../../src/include/bitops.h#L62)
- 函数 [roundUp · L67](../../../src/include/bitops.h#L67)
- 函数 [roundDown · L71](../../../src/include/bitops.h#L71)
- 函数 [alignUp · L77](../../../src/include/bitops.h#L77)
- 函数 [alignUp · L81](../../../src/include/bitops.h#L81)
- 函数 [alignDown · L88](../../../src/include/bitops.h#L88)
- 函数 [alignDown · L93](../../../src/include/bitops.h#L93)
- 函数 [isPow2 · L99](../../../src/include/bitops.h#L99)
- 函数 [add4G · L104](../../../src/include/bitops.h#L104)
- 函数 [incWrap4G · L115](../../../src/include/bitops.h#L115)
- 函数 [decWrap4G · L127](../../../src/include/bitops.h#L127)
- 函数 [idivRcp32 · L139](../../../src/include/bitops.h#L139)
- 函数 [idivRcp64 · L142](../../../src/include/bitops.h#L142)
- 函数 [mul32hi · L146](../../../src/include/bitops.h#L146)
- 函数 [mul64hi · L153](../../../src/include/bitops.h#L153)
- 函数 [imulRcp32 · L165](../../../src/include/bitops.h#L165)
- 函数 [imulRcp64 · L173](../../../src/include/bitops.h#L173)
- 函数 [idivmodFast32 · L184](../../../src/include/bitops.h#L184)
- 函数 [idivmodFast64 · L197](../../../src/include/bitops.h#L197)
- 函数 [idivFast32 · L211](../../../src/include/bitops.h#L211)
- 函数 [idivFast64 · L216](../../../src/include/bitops.h#L216)
- 函数 [imodFast32 · L222](../../../src/include/bitops.h#L222)
- 函数 [imodFast64 · L227](../../../src/include/bitops.h#L227)
- 函数 [countOneBits · L234](../../../src/include/bitops.h#L234)
- 函数 [firstOneBit · L260](../../../src/include/bitops.h#L260)
- 函数 [popFirstOneBit · L285](../../../src/include/bitops.h#L285)
- 函数 [log2Down · L292](../../../src/include/bitops.h#L292)
- 函数 [log2Up · L324](../../../src/include/bitops.h#L324)
- 函数 [pow2Up · L357](../../../src/include/bitops.h#L357)
- 函数 [pow2Down · L362](../../../src/include/bitops.h#L362)
- 函数 [reverseSubBits · L369](../../../src/include/bitops.h#L369)
- 结构体 [ncclToUnsigned&lt;char&gt; · L397](../../../src/include/bitops.h#L397)
- 结构体 [ncclToUnsigned&lt;signed char&gt; · L401](../../../src/include/bitops.h#L401)
- 结构体 [ncclToUnsigned&lt;unsigned char&gt; · L405](../../../src/include/bitops.h#L405)
- 结构体 [ncclToUnsigned&lt;signed short&gt; · L409](../../../src/include/bitops.h#L409)
- 结构体 [ncclToUnsigned&lt;unsigned short&gt; · L413](../../../src/include/bitops.h#L413)
- 结构体 [ncclToUnsigned&lt;signed int&gt; · L417](../../../src/include/bitops.h#L417)
- 结构体 [ncclToUnsigned&lt;unsigned int&gt; · L421](../../../src/include/bitops.h#L421)
- 结构体 [ncclToUnsigned&lt;signed long&gt; · L425](../../../src/include/bitops.h#L425)
- 结构体 [ncclToUnsigned&lt;unsigned long&gt; · L429](../../../src/include/bitops.h#L429)
- 结构体 [ncclToUnsigned&lt;signed long long&gt; · L433](../../../src/include/bitops.h#L433)
- 结构体 [ncclToUnsigned&lt;unsigned long long&gt; · L437](../../../src/include/bitops.h#L437)
- 函数 [reverseBits · L443](../../../src/include/bitops.h#L443)
- 函数 [u32fpEncode · L470](../../../src/include/bitops.h#L470)
- 函数 [u32fpDecode · L482](../../../src/include/bitops.h#L482)
- 函数 [u32fp8MaxValue · L489](../../../src/include/bitops.h#L489)
- 函数 [u32fp8Encode · L493](../../../src/include/bitops.h#L493)
- 函数 [u32fp8Decode · L496](../../../src/include/bitops.h#L496)
- 函数 [eatHash · L502](../../../src/include/bitops.h#L502)
- 函数 [eatHash · L525](../../../src/include/bitops.h#L525)
- 函数 [digestHash · L529](../../../src/include/bitops.h#L529)
- 函数 [getHash · L539](../../../src/include/bitops.h#L539)
- 函数 [getHash · L545](../../../src/include/bitops.h#L545)

## src/include/bootstrap.h

[整个文件](../../../src/include/bootstrap.h)

- 结构体 [ncclBootstrapHandle · L14](../../../src/include/bootstrap.h#L14)

## src/include/ce_coll.h

[整个文件](../../../src/include/ce_coll.h)

- 枚举 [ncclCeMethodId · L20](../../../src/include/ce_coll.h#L20)
- 结构体 [ncclCeColl · L26](../../../src/include/ce_coll.h#L26)
- 结构体 [ncclCeInitTask · L41](../../../src/include/ce_coll.h#L41)
- 结构体 [ncclCeCollArgs · L46](../../../src/include/ce_coll.h#L46)
- 结构体 [ncclCeBatchOpsParams · L61](../../../src/include/ce_coll.h#L61)

## src/include/channel.h

[整个文件](../../../src/include/channel.h)

- 结构体 [ncclCollChannelLayout · L23](../../../src/include/channel.h#L23)
- 函数 [ncclP2pChannelBaseForRound · L42](../../../src/include/channel.h#L42)

## src/include/checks.h

[整个文件](../../../src/include/checks.h)

- 函数 [cuda_clear · L46](../../../src/include/checks.h#L46)

## src/include/coll_net.h

[整个文件](../../../src/include/coll_net.h)

- 函数 [collNetName · L18](../../../src/include/coll_net.h#L18)
- 函数 [collNetDevices · L21](../../../src/include/coll_net.h#L21)
- 函数 [collNetGetProperties · L25](../../../src/include/coll_net.h#L25)
- 函数 [collNetListen · L29](../../../src/include/coll_net.h#L29)
- 函数 [collNetConnect · L33](../../../src/include/coll_net.h#L33)
- 函数 [collNetReduceSupport · L38](../../../src/include/coll_net.h#L38)
- 函数 [collNetRegMr · L43](../../../src/include/coll_net.h#L43)
- 函数 [collNetRegMrDmaBuf · L49](../../../src/include/coll_net.h#L49)
- 函数 [collNetDeregMr · L54](../../../src/include/coll_net.h#L54)
- 函数 [collNetIallreduce · L58](../../../src/include/coll_net.h#L58)
- 函数 [collNetIflush · L65](../../../src/include/coll_net.h#L65)
- 函数 [collNetTest · L70](../../../src/include/coll_net.h#L70)
- 函数 [collNetCloseColl · L74](../../../src/include/coll_net.h#L74)
- 函数 [collNetCloseListen · L78](../../../src/include/coll_net.h#L78)
- 函数 [collNetFinalize · L82](../../../src/include/coll_net.h#L82)
- 函数 [collNetSupport · L87](../../../src/include/coll_net.h#L87)

## src/include/coll_sizes.h

[整个文件](../../../src/include/coll_sizes.h)

- 函数 [ncclTypeSize · L34](../../../src/include/coll_sizes.h#L34)
- 函数 [ncclDefaultChunkStep · L57](../../../src/include/coll_sizes.h#L57)
- 函数 [ncclDefaultSliceStep · L80](../../../src/include/coll_sizes.h#L80)
- 函数 [ncclGetChunkSteps · L103](../../../src/include/coll_sizes.h#L103)
- 函数 [ncclGetSliceSteps · L107](../../../src/include/coll_sizes.h#L107)
- 函数 [ncclSizePerChannel · L111](../../../src/include/coll_sizes.h#L111)
- 函数 [ncclGetChunkSize · L115](../../../src/include/coll_sizes.h#L115)
- 函数 [ncclNominalSliceSize · L122](../../../src/include/coll_sizes.h#L122)
- 函数 [ncclSimpleSliceSize · L129](../../../src/include/coll_sizes.h#L129)
- 函数 [ncclElementAlignedDivUp · L137](../../../src/include/coll_sizes.h#L137)

## src/include/collectives.h

[整个文件](../../../src/include/collectives.h)

- 结构体 [ncclConnFifo · L28](../../../src/include/collectives.h#L28)
- 类 [RingAlgorithm · L37](../../../src/include/collectives.h#L37)
- 函数 [incRefCount · L62](../../../src/include/collectives.h#L62)
- 函数 [decRefCount · L65](../../../src/include/collectives.h#L65)
- 函数 [RingAlgorithm · L68](../../../src/include/collectives.h#L68)
- 函数 [~RingAlgorithm · L71](../../../src/include/collectives.h#L71)
- 类 [RingARAlgorithm · L74](../../../src/include/collectives.h#L74)
- 函数 [getNextSendAddr · L82](../../../src/include/collectives.h#L82)
- 函数 [getNextRecvAddr · L125](../../../src/include/collectives.h#L125)
- 函数 [RingARAlgorithm · L169](../../../src/include/collectives.h#L169)
- 函数 [~RingARAlgorithm · L189](../../../src/include/collectives.h#L189)
- 类 [RingAGAlgorithm · L192](../../../src/include/collectives.h#L192)
- 函数 [getNextSendAddr · L200](../../../src/include/collectives.h#L200)
- 函数 [getNextRecvAddr · L234](../../../src/include/collectives.h#L234)
- 函数 [RingAGAlgorithm · L262](../../../src/include/collectives.h#L262)
- 函数 [~RingAGAlgorithm · L282](../../../src/include/collectives.h#L282)
- 类 [RingBCAlgorithm · L285](../../../src/include/collectives.h#L285)
- 函数 [getNextSendAddr · L292](../../../src/include/collectives.h#L292)
- 函数 [getNextRecvAddr · L320](../../../src/include/collectives.h#L320)
- 函数 [RingBCAlgorithm · L341](../../../src/include/collectives.h#L341)
- 函数 [~RingBCAlgorithm · L359](../../../src/include/collectives.h#L359)
- 结构体 [ncclPatStep · L372](../../../src/include/collectives.h#L372)
- 结构体 [ncclPatPeer · L381](../../../src/include/collectives.h#L381)
- 结构体 [ncclPatShmem · L395](../../../src/include/collectives.h#L395)
- 类 [PatRSAlgorithm · L411](../../../src/include/collectives.h#L411)
- 函数 [min · L433](../../../src/include/collectives.h#L433)
- 函数 [getNelem · L437](../../../src/include/collectives.h#L437)
- 函数 [mirrorInvert · L441](../../../src/include/collectives.h#L441)
- 函数 [firstBitSet · L449](../../../src/include/collectives.h#L449)
- 函数 [resetA · L459](../../../src/include/collectives.h#L459)
- 函数 [reset · L467](../../../src/include/collectives.h#L467)
- 函数 [nBitsSet · L475](../../../src/include/collectives.h#L475)
- 函数 [newPeer · L487](../../../src/include/collectives.h#L487)
- 函数 [PatRSAlgorithm · L493](../../../src/include/collectives.h#L493)
- 函数 [getParallelFactor · L518](../../../src/include/collectives.h#L518)
- 函数 [getNextOp · L522](../../../src/include/collectives.h#L522)
- 类 [PatAGAlgorithm · L674](../../../src/include/collectives.h#L674)
- 函数 [min · L700](../../../src/include/collectives.h#L700)
- 函数 [getNelem · L704](../../../src/include/collectives.h#L704)
- 函数 [mirror · L708](../../../src/include/collectives.h#L708)
- 函数 [firstBitSet · L716](../../../src/include/collectives.h#L716)
- 函数 [resetA · L726](../../../src/include/collectives.h#L726)
- 函数 [reset · L732](../../../src/include/collectives.h#L732)
- 函数 [nextAs · L745](../../../src/include/collectives.h#L745)
- 函数 [PatAGAlgorithm · L766](../../../src/include/collectives.h#L766)
- 函数 [getParallelFactor · L792](../../../src/include/collectives.h#L792)
- 函数 [getNextOp · L796](../../../src/include/collectives.h#L796)

## src/include/comm.h

[整个文件](../../../src/include/comm.h)

- 结构体 [cudaLaunchParams · L40](../../../src/include/comm.h#L40)
- 结构体 [ncclSendMem · L59](../../../src/include/comm.h#L59)
- 结构体 [ncclRecvMem · L73](../../../src/include/comm.h#L73)
- 枚举 [helperThreadState · L85](../../../src/include/comm.h#L85)
- 结构体 [ncclUserRedOp · L92](../../../src/include/comm.h#L92)
- 结构体 [ncclNodeRanks · L98](../../../src/include/comm.h#L98)
- 结构体 [cliqueInfo · L103](../../../src/include/comm.h#L103)
- 结构体 [ncclDestructor · L109](../../../src/include/comm.h#L109)
- 结构体 [ncclCommCallback · L116](../../../src/include/comm.h#L116)
- 结构体 [ncclCommEventCallback · L120](../../../src/include/comm.h#L120)
- 结构体 [ncclUncapturedStreamPoolNode · L126](../../../src/include/comm.h#L126)
- 结构体 [ncclUncapturedStreamPool · L131](../../../src/include/comm.h#L131)
- 结构体 [ncclSharedResources · L138](../../../src/include/comm.h#L138)
- 结构体 [ncclChannel · L166](../../../src/include/comm.h#L166)
- 结构体 [ncclWorkBatchList · L190](../../../src/include/comm.h#L190)
- 结构体 [ncclWorkList · L194](../../../src/include/comm.h#L194)
- 结构体 [ncclCollnetHandleList · L201](../../../src/include/comm.h#L201)
- 结构体 [ncclTaskColl · L209](../../../src/include/comm.h#L209)
- 结构体 [ncclTaskBcast · L273](../../../src/include/comm.h#L273)
- 结构体 [ncclTaskP2p · L295](../../../src/include/comm.h#L295)
- 结构体 [ncclTaskRma · L323](../../../src/include/comm.h#L323)
- 结构体 [ncclKernelPlan · L357](../../../src/include/comm.h#L357)
- 结构体 [ncclTaskCollSorter · L417](../../../src/include/comm.h#L417)
- 函数 [ncclTaskCollSorterInsert · L437](../../../src/include/comm.h#L437)
- 函数 [ncclTaskCollSorterEmpty · L467](../../../src/include/comm.h#L467)
- 函数 [ncclTaskCollSorterDequeueAll · L472](../../../src/include/comm.h#L472)
- 结构体 [ncclCudaStreamList · L480](../../../src/include/comm.h#L480)
- 结构体 [ncclKernelPlanner · L485](../../../src/include/comm.h#L485)
- 结构体 [Peer · L490](../../../src/include/comm.h#L490)
- 结构体 [WipPlan · L538](../../../src/include/comm.h#L538)
- 结构体 [Channel · L539](../../../src/include/comm.h#L539)
- 枚举 [ncclGroupTaskType · L566](../../../src/include/comm.h#L566)
- 枚举 [ncclCheckMode · L579](../../../src/include/comm.h#L579)
- 结构体 [ncclComm · L585](../../../src/include/comm.h#L585)
- 结构体 [P2pSchedulePair · L781](../../../src/include/comm.h#L781)
- 函数 [ncclNvlsTransportEnabled · L893](../../../src/include/comm.h#L893)
- 函数 [ncclNvlsSymmetricMultimemEnabled · L897](../../../src/include/comm.h#L897)
- 枚举 [ncclLaunchMode · L905](../../../src/include/comm.h#L905)
- 函数 [ncclCommPollCallbacks · L917](../../../src/include/comm.h#L917)
- 函数 [ncclCommNMaxChannels · L930](../../../src/include/comm.h#L930)
- 函数 [ncclCommPollEventCallbacks · L937](../../../src/include/comm.h#L937)
- 函数 [ncclCommIntraBarrierIn · L964](../../../src/include/comm.h#L964)
- 函数 [ncclCommIntraBarrierOut · L983](../../../src/include/comm.h#L983)
- 函数 [ncclUserRedOpMangle · L1004](../../../src/include/comm.h#L1004)

## src/include/compiler.h

[整个文件](../../../src/include/compiler.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/core.h

[整个文件](../../../src/include/core.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/cpuset.h

[整个文件](../../../src/include/cpuset.h)

- 函数 [ncclStrToCpuset · L29](../../../src/include/cpuset.h#L29)
- 函数 [ncclCpusetToRangeStr · L56](../../../src/include/cpuset.h#L56)
- 函数 [ncclStrListToCpuset · L81](../../../src/include/cpuset.h#L81)
- 函数 [ncclCpusetToStrList · L96](../../../src/include/cpuset.h#L96)

## src/include/crypt.h

[整个文件](../../../src/include/crypt.h)

- 枚举 [ncclCryptHelloVerdict · L26](../../../src/include/crypt.h#L26)

## src/include/cudawrap.h

[整个文件](../../../src/include/cudawrap.h)

- 函数 [printCudaDriverErrorHint · L33](../../../src/include/cudawrap.h#L33)
- 函数 [ncclCudaStreamIsLegacyNull · L217](../../../src/include/cudawrap.h#L217)
- 函数 [ncclCudaDriverVersion · L229](../../../src/include/cudawrap.h#L229)

## src/include/debug.h

[整个文件](../../../src/include/debug.h)

- 函数 [ncclDebugShouldLog · L27](../../../src/include/debug.h#L27)

## src/include/dev_runtime.h

[整个文件](../../../src/include/dev_runtime.h)

- 枚举 [ncclDevrRegisterCapability · L25](../../../src/include/dev_runtime.h#L25)
- 结构体 [ncclDevrWindow · L35](../../../src/include/dev_runtime.h#L35)
- 结构体 [ncclDevrRegTask · L49](../../../src/include/dev_runtime.h#L49)
- 结构体 [ncclDevrCommCreateTask · L57](../../../src/include/dev_runtime.h#L57)
- 结构体 [ncclDevrStateCftUc · L65](../../../src/include/dev_runtime.h#L65)
- 结构体 [ncclDevrState · L69](../../../src/include/dev_runtime.h#L69)
- 结构体 [ncclDevCommCompat · L116](../../../src/include/dev_runtime.h#L116)
- 结构体 [ncclGinBarrierReq · L134](../../../src/include/dev_runtime.h#L134)

## src/include/device.h

[整个文件](../../../src/include/device.h)

- 枚举 [ncclDevRedOp_t · L64](../../../src/include/device.h#L64)
- 结构体 [ncclDevRedOpFull · L72](../../../src/include/device.h#L72)
- 结构体 [ncclConnInfo · L104](../../../src/include/device.h#L104)
- 结构体 [ncclProxyConnector · L124](../../../src/include/device.h#L124)
- 结构体 [ncclConnector · L136](../../../src/include/device.h#L136)
- 结构体 [ncclRing · L146](../../../src/include/device.h#L146)
- 结构体 [ncclTree · L170](../../../src/include/device.h#L170)
- 结构体 [ncclDirect · L179](../../../src/include/device.h#L179)
- 结构体 [ncclNvls · L194](../../../src/include/device.h#L194)
- 结构体 [ncclChannelPeer · L211](../../../src/include/device.h#L211)
- 结构体 [ncclDevWorkP2p · L219](../../../src/include/device.h#L219)
- 函数 [ncclP2pPartBounds · L239](../../../src/include/device.h#L239)
- 函数 [ncclP2pChannelForPart · L256](../../../src/include/device.h#L256)
- 函数 [ncclP2pChannelToPart · L259](../../../src/include/device.h#L259)
- 结构体 [ncclDevWorkColl · L263](../../../src/include/device.h#L263)
- 结构体 [ncclDevWorkBcast · L294](../../../src/include/device.h#L294)
- 函数 [ncclProtoGrainSize · L304](../../../src/include/device.h#L304)
- 函数 [ncclCollCbdPart · L313](../../../src/include/device.h#L313)
- 结构体 [ncclDevWorkCollReg · L339](../../../src/include/device.h#L339)
- 枚举 [ncclDevWorkType · L346](../../../src/include/device.h#L346)
- 函数 [ncclDevWorkSize · L353](../../../src/include/device.h#L353)
- 函数 [ncclMaxDevWorkBatchBytes · L361](../../../src/include/device.h#L361)
- 结构体 [ncclDevWorkBatch · L376](../../../src/include/device.h#L376)
- 结构体 [ncclDevChannelPeer · L399](../../../src/include/device.h#L399)
- 结构体 [ncclDevChannel · L406](../../../src/include/device.h#L406)
- 结构体 [ncclDevProfiler · L418](../../../src/include/device.h#L418)
- 结构体 [ncclDevProfilerPhases · L437](../../../src/include/device.h#L437)
- 结构体 [ncclProgressCountersBlock · L446](../../../src/include/device.h#L446)
- 结构体 [ncclKernelComm · L452](../../../src/include/device.h#L452)
- 结构体 [ncclKernelCommAndChannels · L479](../../../src/include/device.h#L479)
- 枚举 [ncclDevWorkStorageType · L484](../../../src/include/device.h#L484)
- 结构体 [ncclDevKernelArgs · L490](../../../src/include/device.h#L490)
- 函数 [ncclMaxKernelArgsSize · L500](../../../src/include/device.h#L500)
- 结构体 [ncclDevKernelArgsStorage · L506](../../../src/include/device.h#L506)
- 函数 [min_constexpr · L517](../../../src/include/device.h#L517)
- 函数 [min_constexpr · L521](../../../src/include/device.h#L521)
- 函数 [max_constexpr · L526](../../../src/include/device.h#L526)
- 函数 [max_constexpr · L530](../../../src/include/device.h#L530)
- 函数 [ncclDevMaxChannelsForArgsBytes · L534](../../../src/include/device.h#L534)
- 函数 [ncclCalcUnroll · L543](../../../src/include/device.h#L543)
- 函数 [ncclCollUnroll · L552](../../../src/include/device.h#L552)
- 函数 [ncclNvlsUnrollBytes · L557](../../../src/include/device.h#L557)
- 函数 [ncclNvlsUnrollInsns · L560](../../../src/include/device.h#L560)
- 函数 [ncclNvlsUnroll · L564](../../../src/include/device.h#L564)
- 函数 [ncclShmemScratchWarpSize · L569](../../../src/include/device.h#L569)
- 函数 [ncclTmaShmemScratchWarpSize · L580](../../../src/include/device.h#L580)
- 函数 [ncclShmemDynamicSize · L585](../../../src/include/device.h#L585)
- 函数 [ncclNvlsSupported · L604](../../../src/include/device.h#L604)
- 函数 [ncclDevFuncId · L622](../../../src/include/device.h#L622)
- 函数 [ncclDevFuncId_P2p · L684](../../../src/include/device.h#L684)

## src/include/diagnostics_log.h

[整个文件](../../../src/include/diagnostics_log.h)

- 函数 [diagLogInit · L16](../../../src/include/diagnostics_log.h#L16)

## src/include/enqueue.h

[整个文件](../../../src/include/enqueue.h)

- 函数 [ncclFuncSendCount · L54](../../../src/include/enqueue.h#L54)
- 函数 [ncclFuncRecvCount · L58](../../../src/include/enqueue.h#L58)
- 函数 [ncclFuncMaxSendRecvCount · L62](../../../src/include/enqueue.h#L62)
- 函数 [ncclAllGatherIsInPlace · L68](../../../src/include/enqueue.h#L68)

## src/include/env.h

[整个文件](../../../src/include/env.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/gdrwrap.h

[整个文件](../../../src/include/gdrwrap.h)

- 函数 [wc_store_fence · L38](../../../src/include/gdrwrap.h#L38)
- 函数 [wc_store_fence · L41](../../../src/include/gdrwrap.h#L41)
- 函数 [wc_store_fence · L44](../../../src/include/gdrwrap.h#L44)
- 函数 [wc_store_fence · L46](../../../src/include/gdrwrap.h#L46)
- 枚举 [gdr_pin_flags · L54](../../../src/include/gdrwrap.h#L54)
- 结构体 [gdr_mh_s · L67](../../../src/include/gdrwrap.h#L67)
- 枚举 [gdr_mapping_type · L71](../../../src/include/gdrwrap.h#L71)
- 枚举 [gdr_attr · L79](../../../src/include/gdrwrap.h#L79)
- 结构体 [gdr_info_v2 · L86](../../../src/include/gdrwrap.h#L86)
- 结构体 [gdr_mem_desc · L126](../../../src/include/gdrwrap.h#L126)
- 函数 [ncclGdrInit · L134](../../../src/include/gdrwrap.h#L134)
- 函数 [ncclGdrCudaUnmapPointer · L179](../../../src/include/gdrwrap.h#L179)
- 函数 [ncclGdrCudaMapAligned · L186](../../../src/include/gdrwrap.h#L186)
- 函数 [ncclGdrCudaMapPointer · L210](../../../src/include/gdrwrap.h#L210)
- 函数 [ncclGdrCudaCalloc · L227](../../../src/include/gdrwrap.h#L227)
- 函数 [ncclGdrCudaCopy · L267](../../../src/include/gdrwrap.h#L267)
- 函数 [ncclGdrCudaRead · L273](../../../src/include/gdrwrap.h#L273)
- 函数 [ncclGdrCudaFree · L278](../../../src/include/gdrwrap.h#L278)
- 函数 [allocMemCPUAccessible · L289](../../../src/include/gdrwrap.h#L289)
- 函数 [freeMemCPUAccessible · L308](../../../src/include/gdrwrap.h#L308)

## src/include/gin.h

[整个文件](../../../src/include/gin.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/graph.h

[整个文件](../../../src/include/graph.h)

- 枚举 [ncclTopoGdrMode · L46](../../../src/include/graph.h#L46)
- 枚举 [ncclTopoFlushType · L55](../../../src/include/graph.h#L55)
- 函数 [ncclGdcPinFlag · L60](../../../src/include/graph.h#L60)
- 枚举 [netDevsPolicy · L104](../../../src/include/graph.h#L104)
- 结构体 [ncclTopoGraph · L173](../../../src/include/graph.h#L173)
- 结构体 [ncclTopoRanks · L199](../../../src/include/graph.h#L199)

## src/include/group.h

[整个文件](../../../src/include/group.h)

- 结构体 [ncclGroupJob · L35](../../../src/include/group.h#L35)
- 函数 [ncclGroupStartInternal · L64](../../../src/include/group.h#L64)
- 函数 [ncclGroupEnabled · L69](../../../src/include/group.h#L69)
- 函数 [ncclGroupErrCheck · L73](../../../src/include/group.h#L73)
- 函数 [ncclGroupCommJoin · L81](../../../src/include/group.h#L81)
- 函数 [ncclGroupCommPreconnect · L120](../../../src/include/group.h#L120)
- 函数 [ncclGroupCommLeave · L128](../../../src/include/group.h#L128)

## src/include/ibvcore.h

[整个文件](../../../src/include/ibvcore.h)

- 联合体 [ibv_gid · L58](../../../src/include/ibvcore.h#L58)
- 枚举 [ibv_node_type · L83](../../../src/include/ibvcore.h#L83)
- 枚举 [ibv_transport_type · L97](../../../src/include/ibvcore.h#L97)
- 枚举 [ibv_device_cap_flags · L109](../../../src/include/ibvcore.h#L109)
- 枚举 [ibv_atomic_cap · L129](../../../src/include/ibvcore.h#L129)
- 结构体 [ibv_device_attr · L135](../../../src/include/ibvcore.h#L135)
- 枚举 [ibv_mtu · L178](../../../src/include/ibvcore.h#L178)
- 枚举 [ibv_port_state · L186](../../../src/include/ibvcore.h#L186)
- 枚举 [ibv_port_cap_flags · L207](../../../src/include/ibvcore.h#L207)
- 枚举 [ibv_query_port_flags · L229](../../../src/include/ibvcore.h#L229)
- 结构体 [ibv_port_attr · L233](../../../src/include/ibvcore.h#L233)
- 枚举 [ibv_event_type · L259](../../../src/include/ibvcore.h#L259)
- 结构体 [ibv_async_event · L290](../../../src/include/ibvcore.h#L290)
- 枚举 [ibv_wc_status · L303](../../../src/include/ibvcore.h#L303)
- 枚举 [ibv_wc_opcode · L329](../../../src/include/ibvcore.h#L329)
- 枚举 [ibv_wc_flags · L344](../../../src/include/ibvcore.h#L344)
- 结构体 [ibv_wc · L349](../../../src/include/ibvcore.h#L349)
- 枚举 [ibv_access_flags · L365](../../../src/include/ibvcore.h#L365)
- 结构体 [ibv_pd · L374](../../../src/include/ibvcore.h#L374)
- 枚举 [ibv_xrcd_init_attr_mask · L379](../../../src/include/ibvcore.h#L379)
- 结构体 [ibv_xrcd_init_attr · L385](../../../src/include/ibvcore.h#L385)
- 结构体 [ibv_xrcd · L391](../../../src/include/ibvcore.h#L391)
- 枚举 [ibv_rereg_mr_flags · L395](../../../src/include/ibvcore.h#L395)
- 结构体 [ibv_mr · L402](../../../src/include/ibvcore.h#L402)
- 枚举 [ibv_mw_type · L412](../../../src/include/ibvcore.h#L412)
- 结构体 [ibv_mw · L417](../../../src/include/ibvcore.h#L417)
- 结构体 [ibv_global_route · L423](../../../src/include/ibvcore.h#L423)
- 结构体 [ibv_grh · L431](../../../src/include/ibvcore.h#L431)
- 枚举 [ibv_rate · L440](../../../src/include/ibvcore.h#L440)
- 结构体 [ibv_ah_attr · L488](../../../src/include/ibvcore.h#L488)
- 枚举 [ibv_srq_attr_mask · L498](../../../src/include/ibvcore.h#L498)
- 结构体 [ibv_srq_attr · L503](../../../src/include/ibvcore.h#L503)
- 结构体 [ibv_srq_init_attr · L509](../../../src/include/ibvcore.h#L509)
- 枚举 [ibv_srq_type · L514](../../../src/include/ibvcore.h#L514)
- 枚举 [ibv_srq_init_attr_mask · L519](../../../src/include/ibvcore.h#L519)
- 结构体 [ibv_srq_init_attr_ex · L527](../../../src/include/ibvcore.h#L527)
- 枚举 [ibv_qp_type · L538](../../../src/include/ibvcore.h#L538)
- 结构体 [ibv_qp_cap · L556](../../../src/include/ibvcore.h#L556)
- 结构体 [ibv_qp_init_attr · L564](../../../src/include/ibvcore.h#L564)
- 枚举 [ibv_qp_init_attr_mask · L576](../../../src/include/ibvcore.h#L576)
- 结构体 [ibv_qp_init_attr_ex · L582](../../../src/include/ibvcore.h#L582)
- 枚举 [ibv_qp_open_attr_mask · L596](../../../src/include/ibvcore.h#L596)
- 结构体 [ibv_qp_open_attr · L604](../../../src/include/ibvcore.h#L604)
- 枚举 [ibv_qp_attr_mask · L612](../../../src/include/ibvcore.h#L612)
- 枚举 [ibv_qp_state · L636](../../../src/include/ibvcore.h#L636)
- 枚举 [ibv_mig_state · L647](../../../src/include/ibvcore.h#L647)
- 结构体 [ibv_qp_attr · L653](../../../src/include/ibvcore.h#L653)
- 枚举 [ibv_wr_opcode · L681](../../../src/include/ibvcore.h#L681)
- 枚举 [ibv_send_flags · L691](../../../src/include/ibvcore.h#L691)
- 结构体 [ibv_sge · L698](../../../src/include/ibvcore.h#L698)
- 结构体 [ibv_send_wr · L704](../../../src/include/ibvcore.h#L704)
- 结构体 [ibv_recv_wr · L740](../../../src/include/ibvcore.h#L740)
- 结构体 [ibv_mw_bind · L747](../../../src/include/ibvcore.h#L747)
- 结构体 [ibv_srq · L756](../../../src/include/ibvcore.h#L756)
- 枚举 [ibv_event_flags · L781](../../../src/include/ibvcore.h#L781)
- 结构体 [ibv_qp · L787](../../../src/include/ibvcore.h#L787)
- 结构体 [ibv_comp_channel · L804](../../../src/include/ibvcore.h#L804)
- 结构体 [ibv_cq · L810](../../../src/include/ibvcore.h#L810)
- 结构体 [ibv_ah · L823](../../../src/include/ibvcore.h#L823)
- 枚举 [ibv_flow_flags · L829](../../../src/include/ibvcore.h#L829)
- 枚举 [ibv_flow_attr_type · L834](../../../src/include/ibvcore.h#L834)
- 枚举 [ibv_flow_spec_type · L847](../../../src/include/ibvcore.h#L847)
- 结构体 [ibv_flow_eth_filter · L854](../../../src/include/ibvcore.h#L854)
- 结构体 [ibv_flow_spec_eth · L864](../../../src/include/ibvcore.h#L864)
- 结构体 [ibv_flow_ipv4_filter · L871](../../../src/include/ibvcore.h#L871)
- 结构体 [ibv_flow_spec_ipv4 · L876](../../../src/include/ibvcore.h#L876)
- 结构体 [ibv_flow_tcp_udp_filter · L883](../../../src/include/ibvcore.h#L883)
- 结构体 [ibv_flow_spec_tcp_udp · L888](../../../src/include/ibvcore.h#L888)
- 结构体 [ibv_flow_spec · L895](../../../src/include/ibvcore.h#L895)
- 结构体 [ibv_flow_attr · L907](../../../src/include/ibvcore.h#L907)
- 结构体 [ibv_flow · L921](../../../src/include/ibvcore.h#L921)
- 结构体 [ibv_device_ops · L930](../../../src/include/ibvcore.h#L930)
- 结构体 [ibv_device · L940](../../../src/include/ibvcore.h#L940)
- 结构体 [verbs_device · L954](../../../src/include/ibvcore.h#L954)
- 结构体 [ibv_context_ops · L965](../../../src/include/ibvcore.h#L965)
- 结构体 [ibv_context · L1023](../../../src/include/ibvcore.h#L1023)
- 枚举 [verbs_context_mask · L1033](../../../src/include/ibvcore.h#L1033)
- 结构体 [verbs_context · L1041](../../../src/include/ibvcore.h#L1041)
- 函数 [verbs_get_ctx · L1072](../../../src/include/ibvcore.h#L1072)
- 函数 [verbs_get_device · L1093](../../../src/include/ibvcore.h#L1093)
- 函数 [ibv_post_send · L1099](../../../src/include/ibvcore.h#L1099)
- 结构体 [ibv_ece · L1103](../../../src/include/ibvcore.h#L1103)
- 函数 [ibv_query_port_ex · L1121](../../../src/include/ibvcore.h#L1121)

## src/include/ibvsymbols.h

[整个文件](../../../src/include/ibvsymbols.h)

- 结构体 [ncclIbvSymbols · L20](../../../src/include/ibvsymbols.h#L20)

## src/include/ibvwrap.h

[整个文件](../../../src/include/ibvwrap.h)

- 枚举 [ibv_return_enum · L23](../../../src/include/ibvwrap.h#L23)
- 函数 [wrap_ibv_poll_cq · L60](../../../src/include/ibvwrap.h#L60)
- 函数 [wrap_ibv_post_send · L77](../../../src/include/ibvwrap.h#L77)
- 函数 [wrap_ibv_post_recv · L87](../../../src/include/ibvwrap.h#L87)
- 函数 [ibvGetGidStr · L102](../../../src/include/ibvwrap.h#L102)

## src/include/info.h

[整个文件](../../../src/include/info.h)

- 结构体 [ncclInfo · L17](../../../src/include/info.h#L17)

## src/include/ipcsocket.h

[整个文件](../../../src/include/ipcsocket.h)

- 结构体 [ncclIpcSocket · L28](../../../src/include/ipcsocket.h#L28)

## src/include/mc_arena.h

[整个文件](../../../src/include/mc_arena.h)

- 结构体 [ncclMcArenaReg · L17](../../../src/include/mc_arena.h#L17)
- 结构体 [ncclMcArena · L27](../../../src/include/mc_arena.h#L27)
- 结构体 [ncclMcRetiredReg · L38](../../../src/include/mc_arena.h#L38)

## src/include/mem_manager.h

[整个文件](../../../src/include/mem_manager.h)

- 结构体 [CUmemFabricHandle_st · L28](../../../src/include/mem_manager.h#L28)
- 结构体 [ncclDynMemLocalDesc · L53](../../../src/include/mem_manager.h#L53)
- 结构体 [ncclDynMemImportDesc · L70](../../../src/include/mem_manager.h#L70)
- 结构体 [ncclDynMemEntry · L77](../../../src/include/mem_manager.h#L77)
- 结构体 [ncclDynMemP2pHandleInfo · L101](../../../src/include/mem_manager.h#L101)
- 结构体 [ncclMemManager · L114](../../../src/include/mem_manager.h#L114)
- 结构体 [ncclMemManagerTask · L133](../../../src/include/mem_manager.h#L133)
- 结构体 [ncclMemUntrackInfo · L154](../../../src/include/mem_manager.h#L154)

## src/include/mnnvl.h

[整个文件](../../../src/include/mnnvl.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/multicast.h

[整个文件](../../../src/include/multicast.h)

- 结构体 [ncclMcRequest · L22](../../../src/include/multicast.h#L22)
- 结构体 [ncclMcPartition · L29](../../../src/include/multicast.h#L29)
- 结构体 [ncclMcRankSet · L43](../../../src/include/multicast.h#L43)
- 枚举 [ncclMcBindStatus · L50](../../../src/include/multicast.h#L50)

## src/include/nccl_common.h

[整个文件](../../../src/include/nccl_common.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nccl_device.h

[整个文件](../../../src/include/nccl_device.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/net.h

[整个文件](../../../src/include/net.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nvls_ub.h

[整个文件](../../../src/include/nvls_ub.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/nvmlwrap.h

[整个文件](../../../src/include/nvmlwrap.h)

- 枚举 [nvmlEnableState_enum · L35](../../../src/include/nvmlwrap.h#L35)
- 枚举 [nvmlNvLinkCapability_enum · L40](../../../src/include/nvmlwrap.h#L40)
- 枚举 [nvmlReturn_enum · L51](../../../src/include/nvmlwrap.h#L51)
- 结构体 [nvmlPciInfo_st · L75](../../../src/include/nvmlwrap.h#L75)
- 枚举 [nvmlIntNvLinkDeviceType_enum · L109](../../../src/include/nvmlwrap.h#L109)
- 枚举 [nvmlGpuP2PStatus_enum · L117](../../../src/include/nvmlwrap.h#L117)
- 枚举 [nvmlGpuP2PCapsIndex_enum · L128](../../../src/include/nvmlwrap.h#L128)
- 枚举 [nvmlValueType_enum · L140](../../../src/include/nvmlwrap.h#L140)
- 联合体 [nvmlValue_st · L154](../../../src/include/nvmlwrap.h#L154)
- 结构体 [nvmlFieldValue_st · L197](../../../src/include/nvmlwrap.h#L197)
- 结构体 [nvmlConfComputeSystemState_st · L304](../../../src/include/nvmlwrap.h#L304)
- 枚举 [nvmlMemoryErrorType_enum · L332](../../../src/include/nvmlwrap.h#L332)
- 枚举 [nvmlEccCounterType_enum · L337](../../../src/include/nvmlwrap.h#L337)
- 枚举 [nvmlMemoryLocation_enum · L341](../../../src/include/nvmlwrap.h#L341)
- 结构体 [ncclNvmlDeviceInfo · L350](../../../src/include/nvmlwrap.h#L350)
- 结构体 [ncclNvmlDevicePairInfo · L355](../../../src/include/nvmlwrap.h#L355)
- 结构体 [ncclNvmlCCStatus · L362](../../../src/include/nvmlwrap.h#L362)

## src/include/nvtx.h

[整个文件](../../../src/include/nvtx.h)

- 结构体 [nccl_domain · L63](../../../src/include/nvtx.h#L63)
- 类 [payload_schema · L70](../../../src/include/nvtx.h#L70)
- 函数 [payload_schema · L72](../../../src/include/nvtx.h#L72)
- 类 [ncclOptionalNvtxScopedRange · L103](../../../src/include/nvtx.h#L103)
- 函数 [push · L105](../../../src/include/nvtx.h#L105)
- 函数 [~ncclOptionalNvtxScopedRange · L111](../../../src/include/nvtx.h#L111)
- 类 [ncclOptionalNvtxPayloadRange · L158](../../../src/include/nvtx.h#L158)
- 函数 [push · L160](../../../src/include/nvtx.h#L160)
- 函数 [~ncclOptionalNvtxPayloadRange · L166](../../../src/include/nvtx.h#L166)
- 函数 [setPayloadData · L177](../../../src/include/nvtx.h#L177)
- 函数 [isPushed · L190](../../../src/include/nvtx.h#L190)

## src/include/nvtx_payload_schemas.h

[整个文件](../../../src/include/nvtx_payload_schemas.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/os.h

[整个文件](../../../src/include/os.h)

- 结构体 [ncclShmHandleInternal · L116](../../../src/include/os.h#L116)

## src/include/os_socket_pair.h

[整个文件](../../../src/include/os_socket_pair.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/p2p.h

[整个文件](../../../src/include/p2p.h)

- 枚举 [ncclIpcRegType · L36](../../../src/include/p2p.h#L36)
- 结构体 [ncclIpcImpInfo · L41](../../../src/include/p2p.h#L41)
- 结构体 [ncclIpcRegInfo · L48](../../../src/include/p2p.h#L48)

## src/include/param.h

[整个文件](../../../src/include/param.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/profiler.h

[整个文件](../../../src/include/profiler.h)

- 结构体 [ncclProfilerWorkOp · L25](../../../src/include/profiler.h#L25)
- 结构体 [ncclProfilerCommState · L45](../../../src/include/profiler.h#L45)
- 枚举 [groupApiState · L67](../../../src/include/profiler.h#L67)
- 结构体 [ncclProfilerApiState · L74](../../../src/include/profiler.h#L74)

## src/include/profiler_event.h

[整个文件](../../../src/include/profiler_event.h)

- 结构体 [ncclProfilerEventRef · L29](../../../src/include/profiler_event.h#L29)

## src/include/progress_monitor.h

[整个文件](../../../src/include/progress_monitor.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/proxy.h

[整个文件](../../../src/include/proxy.h)

- 枚举 [ncclProxyOpState · L49](../../../src/include/proxy.h#L49)
- 联合体 [ncclProxyOpSpecifics · L61](../../../src/include/proxy.h#L61)
- 结构体 [ncclProxyOp · L73](../../../src/include/proxy.h#L73)
- 结构体 [ncclProxyEventHandle · L126](../../../src/include/proxy.h#L126)
- 结构体 [ncclProxySubArgs · L131](../../../src/include/proxy.h#L131)
- 结构体 [ncclProxyArgs · L176](../../../src/include/proxy.h#L176)
- 结构体 [ncclProxyOpsPool · L221](../../../src/include/proxy.h#L221)
- 结构体 [ncclProxyOps · L238](../../../src/include/proxy.h#L238)
- 结构体 [ncclProxySharedP2p · L247](../../../src/include/proxy.h#L247)
- 结构体 [ncclProxyPeer · L257](../../../src/include/proxy.h#L257)
- 结构体 [ncclSharedNetComms · L262](../../../src/include/proxy.h#L262)
- 结构体 [ncclProxyProgressState · L272](../../../src/include/proxy.h#L272)
- 结构体 [ncclExpectedProxyResponse · L289](../../../src/include/proxy.h#L289)
- 结构体 [ncclProxyAsyncOp · L298](../../../src/include/proxy.h#L298)
- 结构体 [ncclProxyLocalPeer · L307](../../../src/include/proxy.h#L307)
- 结构体 [ncclProxyRpcResponseHeader · L318](../../../src/include/proxy.h#L318)
- 结构体 [ncclIpcHdr · L325](../../../src/include/proxy.h#L325)
- 结构体 [ncclProxyState · L334](../../../src/include/proxy.h#L334)
- 枚举 [proxyConnectState · L385](../../../src/include/proxy.h#L385)
- 结构体 [proxyMemHandle · L394](../../../src/include/proxy.h#L394)
- 结构体 [ncclProxyConnection · L399](../../../src/include/proxy.h#L399)
- 枚举 [proxyMode · L418](../../../src/include/proxy.h#L418)
- 枚举 [ncclProxyMsgType · L433](../../../src/include/proxy.h#L433)

## src/include/ras.h

[整个文件](../../../src/include/ras.h)

- 结构体 [rasRankInit · L14](../../../src/include/ras.h#L14)

## src/include/register.h

[整个文件](../../../src/include/register.h)

- 结构体 [ncclPeerRegIpcAddr · L30](../../../src/include/register.h#L30)
- 结构体 [ncclRegNetHandles · L35](../../../src/include/register.h#L35)
- 结构体 [ncclReg · L41](../../../src/include/register.h#L41)
- 结构体 [ncclRegCache · L64](../../../src/include/register.h#L64)

## src/include/register_inline.h

[整个文件](../../../src/include/register_inline.h)

- 函数 [ncclRegFind · L14](../../../src/include/register_inline.h#L14)

## src/include/rma.h

[整个文件](../../../src/include/rma.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/scheduler.h

[整个文件](../../../src/include/scheduler.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/shm.h

[整个文件](../../../src/include/shm.h)

- 结构体 [shmLegacyIpc · L13](../../../src/include/shm.h#L13)
- 结构体 [shmCuIpc · L19](../../../src/include/shm.h#L19)
- 结构体 [shmIpcDesc · L28](../../../src/include/shm.h#L28)

## src/include/shmutils.h

[整个文件](../../../src/include/shmutils.h)

- 结构体 [ncclShmemCollBuff · L19](../../../src/include/shmutils.h#L19)

## src/include/socket.h

[整个文件](../../../src/include/socket.h)

- 联合体 [ncclSocketAddress · L43](../../../src/include/socket.h#L43)
- 联合体 [ncclSocketAddress · L51](../../../src/include/socket.h#L51)
- 枚举 [ncclSocketState · L60](../../../src/include/socket.h#L60)
- 枚举 [ncclSocketType · L76](../../../src/include/socket.h#L76)
- 结构体 [ncclSocket · L92](../../../src/include/socket.h#L92)
- 结构体 [ncclSocketOp · L111](../../../src/include/socket.h#L111)

## src/include/strongstream.h

[整个文件](../../../src/include/strongstream.h)

- 结构体 [ncclCudaGraph · L30](../../../src/include/strongstream.h#L30)
- 函数 [ncclCudaGraphNone · L39](../../../src/include/strongstream.h#L39)
- 函数 [ncclCudaGraphValid · L50](../../../src/include/strongstream.h#L50)
- 函数 [ncclCudaGraphSame · L58](../../../src/include/strongstream.h#L58)
- 结构体 [ncclStrongStream · L116](../../../src/include/strongstream.h#L116)
- 结构体 [ncclCudaContext · L131](../../../src/include/strongstream.h#L131)

## src/include/sym_kernels.h

[整个文件](../../../src/include/sym_kernels.h)

- 结构体 [ncclSymkAlltoAllLLScratchHandle · L83](../../../src/include/sym_kernels.h#L83)
- 结构体 [ncclSymkAlltoAllLLScratchState · L89](../../../src/include/sym_kernels.h#L89)
- 函数 [ncclSymkAlltoAllLLReceivePlaneOffset · L105](../../../src/include/sym_kernels.h#L105)
- 函数 [ncclSymkAlltoAllLLSendPlaneOffset · L109](../../../src/include/sym_kernels.h#L109)
- 函数 [ncclSymkAlltoAllLLLineCount · L114](../../../src/include/sym_kernels.h#L114)
- 函数 [ncclSymkAlltoAllLLWireBytes · L119](../../../src/include/sym_kernels.h#L119)
- 函数 [ncclSymkAlltoAllLLTotalLineCount · L123](../../../src/include/sym_kernels.h#L123)
- 函数 [ncclSymkAlltoAllLLGinLinesPerWarp · L132](../../../src/include/sym_kernels.h#L132)
- 函数 [ncclSymkAlltoAllLLChunksPerPeer · L143](../../../src/include/sym_kernels.h#L143)
- 函数 [ncclSymkAlltoAllLLChunkCount · L147](../../../src/include/sym_kernels.h#L147)
- 函数 [ncclSymkAlltoAllLLUsefulWarpCount · L154](../../../src/include/sym_kernels.h#L154)
- 函数 [ncclSymkAlltoAllLLBlockCount · L163](../../../src/include/sym_kernels.h#L163)
- 函数 [ncclSymkAlltoAllLLSelectedBlockCount · L171](../../../src/include/sym_kernels.h#L171)
- 函数 [ncclSymkAlltoAllLLRequiredPeerPlaneBytes · L182](../../../src/include/sym_kernels.h#L182)
- 函数 [ncclSymkAlltoAllLLRequiredReceivePlaneBytes · L187](../../../src/include/sym_kernels.h#L187)
- 函数 [ncclSymkAlltoAllLLRequiredSendPlaneBytes · L191](../../../src/include/sym_kernels.h#L191)
- 函数 [ncclSymkAlltoAllLLRequiredScratchBytes · L196](../../../src/include/sym_kernels.h#L196)
- 函数 [ncclSymkAlltoAllLLPlaneCapacityForBudget · L207](../../../src/include/sym_kernels.h#L207)
- 函数 [ncclSymkAlltoAllLLRequiredScratchBudgetBytes · L213](../../../src/include/sym_kernels.h#L213)
- 函数 [ncclSymkAlltoAllLLScratchFits · L218](../../../src/include/sym_kernels.h#L218)
- 函数 [ncclSymkAlltoAllLLRemotePeer · L228](../../../src/include/sym_kernels.h#L228)
- 函数 [ncclSymkLLMaxSlots · L243](../../../src/include/sym_kernels.h#L243)
- 枚举 [ncclSymkKernelId · L247](../../../src/include/sym_kernels.h#L247)
- 结构体 [ncclGenkRing · L317](../../../src/include/sym_kernels.h#L317)
- 结构体 [ncclGenkTree · L327](../../../src/include/sym_kernels.h#L327)
- 结构体 [ncclGenkDevComm · L338](../../../src/include/sym_kernels.h#L338)
- 结构体 [ncclSymkDevComm · L372](../../../src/include/sym_kernels.h#L372)
- 结构体 [ncclSymkState · L388](../../../src/include/sym_kernels.h#L388)
- 结构体 [ncclSymkChannelWorkRange · L406](../../../src/include/sym_kernels.h#L406)
- 结构体 [ncclSymkDevWork · L412](../../../src/include/sym_kernels.h#L412)
- 枚举 [ncclDevProfilerMode · L423](../../../src/include/sym_kernels.h#L423)
- 结构体 [ncclSymkDevWorkArgs · L429](../../../src/include/sym_kernels.h#L429)
- 结构体 [ncclGenkDevWorkArgs · L436](../../../src/include/sym_kernels.h#L436)
- 函数 [ncclSymkDevWorkArgsSize · L449](../../../src/include/sym_kernels.h#L449)
- 函数 [ncclSymkGetProfilerCounters · L455](../../../src/include/sym_kernels.h#L455)
- 函数 [ncclSymkGetWorkRange · L460](../../../src/include/sym_kernels.h#L460)
- 函数 [ncclSymkGetWorks · L467](../../../src/include/sym_kernels.h#L467)
- 联合体 [ncclSymkDevWorkArgs4K · L472](../../../src/include/sym_kernels.h#L472)
- 联合体 [ncclGenkDevWorkArgs4K · L477](../../../src/include/sym_kernels.h#L477)
- 函数 [ncclSymkGetBytesPerChunk · L545](../../../src/include/sym_kernels.h#L545)

## src/include/timer.h

[整个文件](../../../src/include/timer.h)

- 函数 [calibrate · L14](../../../src/include/timer.h#L14)
- 函数 [gettime · L26](../../../src/include/timer.h#L26)

## src/include/transport.h

[整个文件](../../../src/include/transport.h)

- 结构体 [ncclPeerInfo · L46](../../../src/include/transport.h#L46)
- 结构体 [ncclConnect · L83](../../../src/include/transport.h#L83)
- 结构体 [ncclNvlsUcSegment · L92](../../../src/include/transport.h#L92)
- 结构体 [ncclNvlsSharedRes · L98](../../../src/include/transport.h#L98)
- 结构体 [ncclCollNetSharedRes · L123](../../../src/include/transport.h#L123)
- 结构体 [ncclTransportComm · L134](../../../src/include/transport.h#L134)
- 结构体 [ncclTransport · L153](../../../src/include/transport.h#L153)

## src/include/trees.h

[整个文件](../../../src/include/trees.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/tuner.h

[整个文件](../../../src/include/tuner.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/tuning.h

[整个文件](../../../src/include/tuning.h)

- 函数 [ncclTuningFuncIndex · L26](../../../src/include/tuning.h#L26)
- 结构体 [ncclTuningInput_t · L70](../../../src/include/tuning.h#L70)
- 结构体 [ncclTuningContext_t · L96](../../../src/include/tuning.h#L96)

## src/include/utils.h

[整个文件](../../../src/include/utils.h)

- 结构体 [netIf · L46](../../../src/include/utils.h#L46)
- 函数 [log2i · L56](../../../src/include/utils.h#L56)
- 函数 [compareInts · L61](../../../src/include/utils.h#L61)
- 函数 [clockNano · L66](../../../src/include/utils.h#L66)
- 函数 [clockRealtime · L71](../../../src/include/utils.h#L71)
- 函数 [getRandomData · L80](../../../src/include/utils.h#L80)
- 函数 [gcd · L100](../../../src/include/utils.h#L100)
- 函数 [ncclAtomicRefCountIncrement · L113](../../../src/include/utils.h#L113)
- 函数 [ncclAtomicRefCountDecrement · L118](../../../src/include/utils.h#L118)
- 结构体 [ncclThreadSignal · L203](../../../src/include/utils.h#L203)
- 结构体 [ncclMemoryStack · L235](../../../src/include/utils.h#L235)
- 结构体 [Hunk · L236](../../../src/include/utils.h#L236)
- 结构体 [Unhunk · L240](../../../src/include/utils.h#L240)
- 结构体 [Frame · L244](../../../src/include/utils.h#L244)
- 函数 [ncclMemoryStackConstruct · L258](../../../src/include/utils.h#L258)
- 函数 [ncclMemoryStack::allocate · L268](../../../src/include/utils.h#L268)
- 函数 [ncclMemoryStackAlloc · L280](../../../src/include/utils.h#L280)
- 函数 [ncclMemoryStackAlloc · L287](../../../src/include/utils.h#L287)
- 函数 [ncclMemoryStackAllocInlineArray · L294](../../../src/include/utils.h#L294)
- 函数 [ncclMemoryStackPush · L304](../../../src/include/utils.h#L304)
- 函数 [ncclMemoryStackPop · L313](../../../src/include/utils.h#L313)
- 结构体 [ncclMemoryPool · L324](../../../src/include/utils.h#L324)
- 结构体 [Cell · L325](../../../src/include/utils.h#L325)
- 函数 [ncclMemoryPoolConstruct · L332](../../../src/include/utils.h#L332)
- 函数 [ncclMemoryPoolAlloc · L337](../../../src/include/utils.h#L337)
- 函数 [ncclMemoryPoolFree · L354](../../../src/include/utils.h#L354)
- 函数 [ncclMemoryPoolTakeAll · L362](../../../src/include/utils.h#L362)
- 结构体 [ncclIntruQueue · L374](../../../src/include/utils.h#L374)
- 函数 [ncclIntruQueueConstruct · L380](../../../src/include/utils.h#L380)
- 函数 [ncclIntruQueueEmpty · L387](../../../src/include/utils.h#L387)
- 函数 [ncclIntruQueueHead · L392](../../../src/include/utils.h#L392)
- 函数 [ncclIntruQueueTail · L397](../../../src/include/utils.h#L397)
- 函数 [ncclIntruQueueEnqueue · L402](../../../src/include/utils.h#L402)
- 函数 [ncclIntruQueueEnqueueFront · L410](../../../src/include/utils.h#L410)
- 函数 [ncclIntruQueueInsertSorted · L420](../../../src/include/utils.h#L420)
- 函数 [ncclIntruQueueDeleteNext · L438](../../../src/include/utils.h#L438)
- 函数 [ncclIntruQueueDequeue · L449](../../../src/include/utils.h#L449)
- 函数 [ncclIntruQueueDelete · L458](../../../src/include/utils.h#L458)
- 函数 [ncclIntruQueueTryDequeue · L482](../../../src/include/utils.h#L482)
- 函数 [ncclIntruQueueTransfer · L493](../../../src/include/utils.h#L493)
- 结构体 [ncclIntruQueueMpsc · L505](../../../src/include/utils.h#L505)
- 函数 [ncclIntruQueueMpscConstruct · L512](../../../src/include/utils.h#L512)
- 函数 [ncclIntruQueueMpscEmpty · L519](../../../src/include/utils.h#L519)
- 函数 [ncclIntruQueueMpscEnqueue · L524](../../../src/include/utils.h#L524)
- 函数 [ncclIntruQueueMpscDequeueAll · L545](../../../src/include/utils.h#L545)
- 函数 [ncclIntruQueueMpscAbandon · L590](../../../src/include/utils.h#L590)
- 结构体 [ncclIntruAddressMap_untyped · L680](../../../src/include/utils.h#L680)
- 结构体 [ncclIntruAddressMap · L688](../../../src/include/utils.h#L688)
- 函数 [ncclIntruAddressMapDestruct · L701](../../../src/include/utils.h#L701)
- 函数 [ncclIntruAddressMapInsert · L722](../../../src/include/utils.h#L722)
- 函数 [ncclIntruAddressMapFind · L734](../../../src/include/utils.h#L734)
- 函数 [ncclIntruAddressMapRemove · L747](../../../src/include/utils.h#L747)
- 函数 [ncclThreadJoin · L756](../../../src/include/utils.h#L756)
- 函数 [ncclVersionToString · L767](../../../src/include/utils.h#L767)
