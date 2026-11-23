# rma 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/rma/rma.cc

[整个文件](../../../src/rma/rma.cc)

- 函数 [ncclRmaProxyEnabled · L19](../../../src/rma/rma.cc#L19)
- 函数 [ncclRmaInitialized · L24](../../../src/rma/rma.cc#L24)
- 函数 [isLsaAccessible · L34](../../../src/rma/rma.cc#L34)
- 函数 [ncclRmaWaitSignal · L43](../../../src/rma/rma.cc#L43)
- 函数 [ncclRmaPut · L76](../../../src/rma/rma.cc#L76)
- 函数 [ncclLaunchRma · L109](../../../src/rma/rma.cc#L109)
- 函数 [isRmaPutOrSignal · L133](../../../src/rma/rma.cc#L133)
- 函数 [scheduleRmaTasksToPlan · L141](../../../src/rma/rma.cc#L141)

## src/rma/rma_ce.cc

[整个文件](../../../src/rma/rma_ce.cc)

- 函数 [ncclRmaCeInit · L18](../../../src/rma/rma_ce.cc#L18)
- 函数 [ncclRmaCeFinalize · L104](../../../src/rma/rma_ce.cc#L104)
- 函数 [ncclRmaCePutLaunchPersist · L161](../../../src/rma/rma_ce.cc#L161)
- 函数 [ncclRmaCePutLaunchNonPersist · L250](../../../src/rma/rma_ce.cc#L250)
- 函数 [ncclRmaCePutLaunch · L427](../../../src/rma/rma_ce.cc#L427)
- 函数 [ncclRmaCeWaitLaunch · L439](../../../src/rma/rma_ce.cc#L439)

## src/rma/rma_proxy.cc

[整个文件](../../../src/rma/rma_proxy.cc)

- 函数 [ncclRmaProxyWorldToPeer · L30](../../../src/rma/rma_proxy.cc#L30)
- 函数 [ncclRmaProxyPeerToWorld · L52](../../../src/rma/rma_proxy.cc#L52)
- 函数 [ncclNumRmaIntCtx · L66](../../../src/rma/rma_proxy.cc#L66)
- 函数 [getDmaBufFd · L79](../../../src/rma/rma_proxy.cc#L79)
- 函数 [ncclRmaProxyRegMrSym · L105](../../../src/rma/rma_proxy.cc#L105)
- 函数 [isPowerOfTwo · L138](../../../src/rma/rma_proxy.cc#L138)
- 函数 [ncclRmaProxyCtxAlloc · L144](../../../src/rma/rma_proxy.cc#L144)
- 函数 [ncclRmaProxyCtxAllocGraph · L208](../../../src/rma/rma_proxy.cc#L208)
- 函数 [ncclRmaProxyCreateContext · L241](../../../src/rma/rma_proxy.cc#L241)
- 函数 [ncclRmaProxyDestroyContext · L283](../../../src/rma/rma_proxy.cc#L283)
- 函数 [ncclRmaProxyRegister · L371](../../../src/rma/rma_proxy.cc#L371)
- 函数 [ncclRmaProxyDeregister · L385](../../../src/rma/rma_proxy.cc#L385)
- 函数 [ncclRmaProxyProgressThread · L395](../../../src/rma/rma_proxy.cc#L395)
- 函数 [ncclRmaWantInternalCtx · L436](../../../src/rma/rma_proxy.cc#L436)
- 函数 [ncclRmaProxyConnectOnce · L440](../../../src/rma/rma_proxy.cc#L440)
- 函数 [ncclRmaProxyFinalize · L568](../../../src/rma/rma_proxy.cc#L568)
- 函数 [dumpRmaProxyState · L606](../../../src/rma/rma_proxy.cc#L606)
- 函数 [ncclDumpRmaProxyState · L675](../../../src/rma/rma_proxy.cc#L675)

## src/rma/rma_proxy_launch.cc

[整个文件](../../../src/rma/rma_proxy_launch.cc)

- 函数 [ncclRmaProxyPutBuildOp · L26](../../../src/rma/rma_proxy_launch.cc#L26)
- 函数 [ncclRmaProxyPutBuildDesc · L57](../../../src/rma/rma_proxy_launch.cc#L57)
- 函数 [ncclRmaProxyPutGroupBuildDesc · L115](../../../src/rma/rma_proxy_launch.cc#L115)
- 函数 [ncclRmaProxyPutDescFromTask · L171](../../../src/rma/rma_proxy_launch.cc#L171)
- 函数 [ncclRmaProxyWaitBuildDesc · L180](../../../src/rma/rma_proxy_launch.cc#L180)
- 函数 [ncclRmaProxyWaitDescFromTask · L230](../../../src/rma/rma_proxy_launch.cc#L230)
- 函数 [ncclRmaProxyDestroyDescNonPersistent · L241](../../../src/rma/rma_proxy_launch.cc#L241)
- 函数 [ncclRmaProxyDestroyDescPersistent · L253](../../../src/rma/rma_proxy_launch.cc#L253)
- 函数 [ncclRmaProxyDestroyDesc · L272](../../../src/rma/rma_proxy_launch.cc#L272)
- 函数 [ncclRmaProxyCircularBufFull · L287](../../../src/rma/rma_proxy_launch.cc#L287)
- 函数 [ncclRmaProxyCircularBufEmpty · L293](../../../src/rma/rma_proxy_launch.cc#L293)
- 函数 [ncclRmaProxyEnqueueFull · L306](../../../src/rma/rma_proxy_launch.cc#L306)
- 函数 [ncclRmaProxyEnqueueNonPersistentDesc · L327](../../../src/rma/rma_proxy_launch.cc#L327)
- 函数 [ncclRmaProxyEnqueuePersistentDesc · L347](../../../src/rma/rma_proxy_launch.cc#L347)
- 函数 [ncclRmaProxyEnqueueDesc · L379](../../../src/rma/rma_proxy_launch.cc#L379)
- 函数 [ncclRmaProxyPutStartNumOps · L417](../../../src/rma/rma_proxy_launch.cc#L417)
- 函数 [ncclRmaProxyPutStartParams · L422](../../../src/rma/rma_proxy_launch.cc#L422)
- 函数 [ncclRmaProxyPutDoneNumOps · L436](../../../src/rma/rma_proxy_launch.cc#L436)
- 函数 [ncclRmaProxyPutDoneParams · L441](../../../src/rma/rma_proxy_launch.cc#L441)
- 函数 [ncclRmaProxyPutGroupStartNumOps · L463](../../../src/rma/rma_proxy_launch.cc#L463)
- 函数 [ncclRmaProxyPutGroupStartParams · L470](../../../src/rma/rma_proxy_launch.cc#L470)
- 函数 [ncclRmaProxyPutGroupDoneNumOps · L484](../../../src/rma/rma_proxy_launch.cc#L484)
- 函数 [ncclRmaProxyPutGroupDoneParams · L491](../../../src/rma/rma_proxy_launch.cc#L491)
- 函数 [ncclRmaProxyWaitStartNumOps · L515](../../../src/rma/rma_proxy_launch.cc#L515)
- 函数 [ncclRmaProxyWaitStartParams · L521](../../../src/rma/rma_proxy_launch.cc#L521)
- 函数 [ncclRmaProxyWaitDoneNumOps · L538](../../../src/rma/rma_proxy_launch.cc#L538)
- 函数 [ncclRmaProxyWaitDoneParams · L546](../../../src/rma/rma_proxy_launch.cc#L546)
- 函数 [ncclRmaProxyWaitNumStreamOps · L584](../../../src/rma/rma_proxy_launch.cc#L584)
- 函数 [ncclRmaProxyWaitParams · L589](../../../src/rma/rma_proxy_launch.cc#L589)
- 函数 [ncclRmaProxyPutLaunch · L601](../../../src/rma/rma_proxy_launch.cc#L601)
- 函数 [ncclRmaProxyWaitLaunch · L704](../../../src/rma/rma_proxy_launch.cc#L704)
- 函数 [ncclRmaProxyReclaimPersistDescs · L765](../../../src/rma/rma_proxy_launch.cc#L765)
- 函数 [ncclRmaProxyReclaimPlan · L801](../../../src/rma/rma_proxy_launch.cc#L801)

## src/rma/rma_proxy_progress.cc

[整个文件](../../../src/rma/rma_proxy_progress.cc)

- 函数 [ncclRmaProxyCanIssueRequest · L16](../../../src/rma/rma_proxy_progress.cc#L16)
- 函数 [ncclRmaProxyIssuePutSignal · L21](../../../src/rma/rma_proxy_progress.cc#L21)
- 函数 [ncclRmaProxyTestPutSignal · L44](../../../src/rma/rma_proxy_progress.cc#L44)
- 函数 [ncclRmaProxyProgressPutSignalGroup · L58](../../../src/rma/rma_proxy_progress.cc#L58)
- 函数 [ncclRmaProxyPollNonPersistCompletion · L81](../../../src/rma/rma_proxy_progress.cc#L81)
- 函数 [ncclRmaProxyPollNonPersistDesc · L114](../../../src/rma/rma_proxy_progress.cc#L114)
- 函数 [ncclRmaProxyFlushNicGpuPath · L159](../../../src/rma/rma_proxy_progress.cc#L159)
- 函数 [ncclRmaProxyPollPersistDesc · L174](../../../src/rma/rma_proxy_progress.cc#L174)
- 函数 [ncclRmaProxyProgress · L278](../../../src/rma/rma_proxy_progress.cc#L278)
