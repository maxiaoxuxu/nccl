# enqueue 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/enqueue/enqueue.cc

[整个文件](../../../src/enqueue/enqueue.cc)

- 函数 [symCeAllGatherThreshold · L46](../../../src/enqueue/enqueue.cc#L46)
- 函数 [ncclInitKernelsForDevice · L57](../../../src/enqueue/enqueue.cc#L57)
- 函数 [ncclAddProxyOpIfNeeded · L149](../../../src/enqueue/enqueue.cc#L149)
- 函数 [ncclAddWorkBatchToPlan · L162](../../../src/enqueue/enqueue.cc#L162)
- 函数 [finishPlan · L245](../../../src/enqueue/enqueue.cc#L245)
- 结构体 [ncclKernelPlanBudget · L347](../../../src/enqueue/enqueue.cc#L347)
- 函数 [ncclTestBudget · L352](../../../src/enqueue/enqueue.cc#L352)
- 函数 [ncclTasksRegAndEnqueue · L360](../../../src/enqueue/enqueue.cc#L360)
- 函数 [ncclValidateCollConfigLaunchCompletionEvents · L422](../../../src/enqueue/enqueue.cc#L422)
- 函数 [ncclPrepareTasks · L432](../../../src/enqueue/enqueue.cc#L432)
- 函数 [scheduleCollTasksToPlan · L658](../../../src/enqueue/enqueue.cc#L658)
- 函数 [computeP2pChannels · L940](../../../src/enqueue/enqueue.cc#L940)
- 函数 [computeP2pChunkSize · L956](../../../src/enqueue/enqueue.cc#L956)
- 函数 [p2pPayloadPerChunk · L966](../../../src/enqueue/enqueue.cc#L966)
- 函数 [addP2pToPlan · L974](../../../src/enqueue/enqueue.cc#L974)
- 函数 [calcP2pChannelCount · L1241](../../../src/enqueue/enqueue.cc#L1241)
- 函数 [scheduleP2pTasksToPlan · L1251](../../../src/enqueue/enqueue.cc#L1251)
- 函数 [waitWorkFifoAvailable · L1368](../../../src/enqueue/enqueue.cc#L1368)
- 结构体 [uploadWork_cleanup_t · L1387](../../../src/enqueue/enqueue.cc#L1387)
- 函数 [uploadWork_cleanup_fn · L1391](../../../src/enqueue/enqueue.cc#L1391)
- 函数 [uploadWork · L1400](../../../src/enqueue/enqueue.cc#L1400)
- 函数 [geteActivationMask · L1529](../../../src/enqueue/enqueue.cc#L1529)
- 函数 [gettaskEventHandle · L1539](../../../src/enqueue/enqueue.cc#L1539)
- 函数 [uploadProxyOps · L1549](../../../src/enqueue/enqueue.cc#L1549)
- 函数 [hostStreamPlanTask · L1593](../../../src/enqueue/enqueue.cc#L1593)
- 函数 [hostStreamPlanCallback · L1614](../../../src/enqueue/enqueue.cc#L1614)
- 函数 [reclaimPlan · L1624](../../../src/enqueue/enqueue.cc#L1624)
- 函数 [persistentDestructor · L1690](../../../src/enqueue/enqueue.cc#L1690)
- 枚举 [ncclImplicitOrder · L1703](../../../src/enqueue/enqueue.cc#L1703)
- 函数 [ncclGraphStreamOrderingSerialize · L1710](../../../src/enqueue/enqueue.cc#L1710)
- 函数 [getImplicitOrder · L1715](../../../src/enqueue/enqueue.cc#L1715)
- 函数 [isolateP2pCollTasks · L1730](../../../src/enqueue/enqueue.cc#L1730)
- 函数 [ncclLaunchPrepare · L1755](../../../src/enqueue/enqueue.cc#L1755)
- 函数 [ncclLaunchKernelBefore_NoUncapturedCuda · L1930](../../../src/enqueue/enqueue.cc#L1930)
- 函数 [ncclLaunchKernel · L1947](../../../src/enqueue/enqueue.cc#L1947)
- 函数 [ncclLaunchKernelAfter_NoCuda · L2075](../../../src/enqueue/enqueue.cc#L2075)
- 结构体 [KernelFinishCallback · L2085](../../../src/enqueue/enqueue.cc#L2085)
- 函数 [KernelFinishCallback_fn · L2089](../../../src/enqueue/enqueue.cc#L2089)
- 函数 [ncclLaunchFinish · L2098](../../../src/enqueue/enqueue.cc#L2098)
- 函数 [ncclGetCollNetSupport · L2182](../../../src/enqueue/enqueue.cc#L2182)
- 函数 [ncclGetRegBuff · L2201](../../../src/enqueue/enqueue.cc#L2201)
- 函数 [ncclGetAlgoInfo · L2220](../../../src/enqueue/enqueue.cc#L2220)
- 函数 [calcCollChunking · L2294](../../../src/enqueue/enqueue.cc#L2294)
- 函数 [hostToDevRedOp · L2599](../../../src/enqueue/enqueue.cc#L2599)
- 函数 [ncclPlannerSetCapturingGraph · L2705](../../../src/enqueue/enqueue.cc#L2705)
- 函数 [p2pTaskAppend · L2735](../../../src/enqueue/enqueue.cc#L2735)
- 函数 [collConfigIsProfilerTagOnly · L2824](../../../src/enqueue/enqueue.cc#L2824)
- 函数 [collTaskAppend · L2832](../../../src/enqueue/enqueue.cc#L2832)
- 结构体 [ncclCeInitAsyncJob · L2931](../../../src/enqueue/enqueue.cc#L2931)
- 函数 [ncclCeInitAsyncJobFree · L2936](../../../src/enqueue/enqueue.cc#L2936)
- 函数 [ncclCeInitJob · L2940](../../../src/enqueue/enqueue.cc#L2940)
- 函数 [ceCollTaskAppend · L2954](../../../src/enqueue/enqueue.cc#L2954)
- 函数 [rmaTaskAppend · L3030](../../../src/enqueue/enqueue.cc#L3030)
- 函数 [rawTaskAppend · L3268](../../../src/enqueue/enqueue.cc#L3268)
- 函数 [ncclInfoHasLaunchCompletionEvent · L3399](../../../src/enqueue/enqueue.cc#L3399)
- 函数 [ncclRecordCollConfigLaunchCompletionEvent · L3404](../../../src/enqueue/enqueue.cc#L3404)
- 函数 [taskAppend · L3417](../../../src/enqueue/enqueue.cc#L3417)
- 函数 [ncclEnqueueCheck · L3570](../../../src/enqueue/enqueue.cc#L3570)
- 函数 [ncclRedOpCreatePreMulSum · L3627](../../../src/enqueue/enqueue.cc#L3627)
- 函数 [ncclRedOpDestroy · L3669](../../../src/enqueue/enqueue.cc#L3669)

## src/enqueue/mgmt_task_enq.cc

[整个文件](../../../src/enqueue/mgmt_task_enq.cc)

- 函数 [ncclMgmtTaskEnqueue · L11](../../../src/enqueue/mgmt_task_enq.cc#L11)

## src/enqueue/task_prep/task_classify.cc

[整个文件](../../../src/enqueue/task_prep/task_classify.cc)

- 函数 [classifyFillSendRecvTuningInput · L14](../../../src/enqueue/task_prep/task_classify.cc#L14)
- 函数 [classifyEnqueueP2pTask · L35](../../../src/enqueue/task_prep/task_classify.cc#L35)
- 函数 [classifyCollToP2pTasks · L61](../../../src/enqueue/task_prep/task_classify.cc#L61)
- 函数 [taskUsesSymKernel · L115](../../../src/enqueue/task_prep/task_classify.cc#L115)
- 函数 [taskUsesCe · L120](../../../src/enqueue/task_prep/task_classify.cc#L120)
- 函数 [taskUsesAllGatherV · L125](../../../src/enqueue/task_prep/task_classify.cc#L125)
- 函数 [ncclTaskClassification · L129](../../../src/enqueue/task_prep/task_classify.cc#L129)

## src/enqueue/task_prep/task_posttuning.cc

[整个文件](../../../src/enqueue/task_prep/task_posttuning.cc)

- 函数 [postTuningSetChunkSteps · L37](../../../src/enqueue/task_prep/task_posttuning.cc#L37)
- 函数 [fillCollTaskFromRaw · L42](../../../src/enqueue/task_prep/task_posttuning.cc#L42)
- 函数 [postTuneSymFreeTuningInfoRaw · L90](../../../src/enqueue/task_prep/task_posttuning.cc#L90)
- 函数 [postTuneP2pChannelBase · L98](../../../src/enqueue/task_prep/task_posttuning.cc#L98)
- 函数 [postTuneP2pRecordPreconnect · L107](../../../src/enqueue/task_prep/task_posttuning.cc#L107)
- 函数 [fillP2pTaskFromRaw · L146](../../../src/enqueue/task_prep/task_posttuning.cc#L146)
- 函数 [postTuneP2pRegisterBuffer · L175](../../../src/enqueue/task_prep/task_posttuning.cc#L175)
- 函数 [postTuneTasksDebug · L220](../../../src/enqueue/task_prep/task_posttuning.cc#L220)
- 函数 [postTuneSymTasksLazyInit · L230](../../../src/enqueue/task_prep/task_posttuning.cc#L230)
- 函数 [postTuneRmaFreeTuningInfoRaw · L236](../../../src/enqueue/task_prep/task_posttuning.cc#L236)
- 函数 [postTuneRmaTaskAppend · L244](../../../src/enqueue/task_prep/task_posttuning.cc#L244)
- 函数 [postTuneRmaTasks · L488](../../../src/enqueue/task_prep/task_posttuning.cc#L488)
- 函数 [postTuneCeTasksLazyInit · L498](../../../src/enqueue/task_prep/task_posttuning.cc#L498)
- 函数 [postTuneSymTasks · L505](../../../src/enqueue/task_prep/task_posttuning.cc#L505)
- 函数 [applyTuningToCollTask · L542](../../../src/enqueue/task_prep/task_posttuning.cc#L542)
- 函数 [postTuneLegacyRegisterCollBuffers · L575](../../../src/enqueue/task_prep/task_posttuning.cc#L575)
- 函数 [postTuneLegacyRegisterNvlsCollBuffers · L585](../../../src/enqueue/task_prep/task_posttuning.cc#L585)
- 函数 [postTuneLegacyEnqueueCollWork · L597](../../../src/enqueue/task_prep/task_posttuning.cc#L597)
- 函数 [postTuneLegacyRecordAlgoNeedConnect · L643](../../../src/enqueue/task_prep/task_posttuning.cc#L643)
- 函数 [postTuneLegacyTasks · L659](../../../src/enqueue/task_prep/task_posttuning.cc#L659)
- 函数 [postTuneAllGatherVEnsureRingConnected · L717](../../../src/enqueue/task_prep/task_posttuning.cc#L717)
- 函数 [postTuneAllGatherVEnqueueBroadcastTask · L729](../../../src/enqueue/task_prep/task_posttuning.cc#L729)
- 函数 [postTuneAllGatherVEnqueueBcastTasks · L779](../../../src/enqueue/task_prep/task_posttuning.cc#L779)
- 函数 [postTuneAllGatherVTasks · L840](../../../src/enqueue/task_prep/task_posttuning.cc#L840)
- 函数 [postTuneP2pTasks · L850](../../../src/enqueue/task_prep/task_posttuning.cc#L850)
- 函数 [postTuneCeFreeTuningInfoRaw · L885](../../../src/enqueue/task_prep/task_posttuning.cc#L885)
- 函数 [postTuneCeCollTaskAppend · L893](../../../src/enqueue/task_prep/task_posttuning.cc#L893)
- 函数 [postTuneCeTasks · L930](../../../src/enqueue/task_prep/task_posttuning.cc#L930)
- 函数 [postTuningAccumulateTime · L948](../../../src/enqueue/task_prep/task_posttuning.cc#L948)
- 函数 [postTuningSimulation · L955](../../../src/enqueue/task_prep/task_posttuning.cc#L955)
- 函数 [ncclTaskPostTuning · L970](../../../src/enqueue/task_prep/task_posttuning.cc#L970)

## src/enqueue/task_prep/task_prep.cc

[整个文件](../../../src/enqueue/task_prep/task_prep.cc)

- 函数 [ncclTaskPrepare · L11](../../../src/enqueue/task_prep/task_prep.cc#L11)

## src/enqueue/task_prep/task_pretuning.cc

[整个文件](../../../src/enqueue/task_prep/task_pretuning.cc)

- 函数 [fillCollTuningInput · L24](../../../src/enqueue/task_prep/task_pretuning.cc#L24)
- 函数 [fillSendRecvTuningInput · L89](../../../src/enqueue/task_prep/task_pretuning.cc#L89)
- 函数 [fillRmaTuningInput · L110](../../../src/enqueue/task_prep/task_pretuning.cc#L110)
- 函数 [fillAllGatherVTuningInput · L131](../../../src/enqueue/task_prep/task_pretuning.cc#L131)
- 函数 [preTuningInitAllGatherVRaw · L147](../../../src/enqueue/task_prep/task_pretuning.cc#L147)
- 函数 [preTuningAllGatherVRootUsed · L163](../../../src/enqueue/task_prep/task_pretuning.cc#L163)
- 函数 [preTuningAddBcastToAllGatherV · L167](../../../src/enqueue/task_prep/task_pretuning.cc#L167)
- 函数 [preTuningRawTaskPtrEqual · L180](../../../src/enqueue/task_prep/task_pretuning.cc#L180)
- 函数 [preTuningBcastFallsBack · L184](../../../src/enqueue/task_prep/task_pretuning.cc#L184)
- 函数 [preTuningBcastFitsAllGatherV · L189](../../../src/enqueue/task_prep/task_pretuning.cc#L189)
- 函数 [preTuningRemoveBcastRawFromQueue · L195](../../../src/enqueue/task_prep/task_pretuning.cc#L195)
- 函数 [preTuningMergeBcastQueue · L203](../../../src/enqueue/task_prep/task_pretuning.cc#L203)
- 函数 [preTuningEnqueueRawTask · L241](../../../src/enqueue/task_prep/task_pretuning.cc#L241)
- 函数 [ncclTaskPreTuning · L266](../../../src/enqueue/task_prep/task_pretuning.cc#L266)

## src/enqueue/task_sched/allgatherv_sched.cc

[整个文件](../../../src/enqueue/task_sched/allgatherv_sched.cc)

- 函数 [ncclScheduleAllGatherVTasks · L11](../../../src/enqueue/task_sched/allgatherv_sched.cc#L11)

## src/enqueue/task_sched/ce_sched.cc

[整个文件](../../../src/enqueue/task_sched/ce_sched.cc)

- 函数 [ncclScheduleCeTasks · L11](../../../src/enqueue/task_sched/ce_sched.cc#L11)

## src/enqueue/task_sched/legacy_sched.cc

[整个文件](../../../src/enqueue/task_sched/legacy_sched.cc)

- 函数 [ncclScheduleLegacyTasks · L11](../../../src/enqueue/task_sched/legacy_sched.cc#L11)

## src/enqueue/task_sched/p2p_sched.cc

[整个文件](../../../src/enqueue/task_sched/p2p_sched.cc)

- 函数 [ncclScheduleP2pTasks · L11](../../../src/enqueue/task_sched/p2p_sched.cc#L11)

## src/enqueue/task_sched/rma_sched.cc

[整个文件](../../../src/enqueue/task_sched/rma_sched.cc)

- 函数 [ncclScheduleRmaTasks · L11](../../../src/enqueue/task_sched/rma_sched.cc#L11)

## src/enqueue/task_sched/sym_sched.cc

[整个文件](../../../src/enqueue/task_sched/sym_sched.cc)

- 函数 [ncclScheduleSymTasks · L11](../../../src/enqueue/task_sched/sym_sched.cc#L11)

## src/enqueue/task_sched/task_sched.cc

[整个文件](../../../src/enqueue/task_sched/task_sched.cc)

- 函数 [ncclTaskSchedule · L12](../../../src/enqueue/task_sched/task_sched.cc#L12)
