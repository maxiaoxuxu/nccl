# plugin 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/plugin/env.cc

[整个文件](../../../src/plugin/env.cc)

- 函数 [ncclEnvPluginLoad · L38](../../../src/plugin/env.cc#L38)
- 函数 [ncclEnvPluginUnload · L80](../../../src/plugin/env.cc#L80)
- 函数 [ncclEnvPluginInit · L96](../../../src/plugin/env.cc#L96)
- 函数 [ncclEnvPluginFinalize · L107](../../../src/plugin/env.cc#L107)
- 函数 [ncclEnvPluginGetEnv · L114](../../../src/plugin/env.cc#L114)
- 函数 [ncclEnvPluginInitialized · L118](../../../src/plugin/env.cc#L118)

## src/plugin/env/default_env.cc

[整个文件](../../../src/plugin/env/default_env.cc)

- 函数 [ncclEnvInit · L12](../../../src/plugin/env/default_env.cc#L12)
- 函数 [ncclEnvFinalize · L17](../../../src/plugin/env/default_env.cc#L17)
- 函数 [ncclEnvGetEnv · L21](../../../src/plugin/env/default_env.cc#L21)

## src/plugin/env/env_v1.cc

[整个文件](../../../src/plugin/env/env_v1.cc)

- 函数 [ncclEnv_init · L17](../../../src/plugin/env/env_v1.cc#L17)
- 函数 [getNcclEnv_v1 · L23](../../../src/plugin/env/env_v1.cc#L23)

## src/plugin/env/env_v2.cc

[整个文件](../../../src/plugin/env/env_v2.cc)

- 函数 [getNcclEnv_v2 · L15](../../../src/plugin/env/env_v2.cc#L15)

## src/plugin/gin.cc

[整个文件](../../../src/plugin/gin.cc)

- 枚举 [ncclGinPluginState · L32](../../../src/plugin/gin.cc#L32)
- 结构体 [ginPluginLib · L41](../../../src/plugin/gin.cc#L41)
- 函数 [ncclGinPluginUnload · L56](../../../src/plugin/gin.cc#L56)
- 函数 [ncclGinPluginLoad · L71](../../../src/plugin/gin.cc#L71)
- 函数 [ncclGinPluginInit · L104](../../../src/plugin/gin.cc#L104)
- 函数 [ncclGinPluginAssignToComm · L132](../../../src/plugin/gin.cc#L132)
- 函数 [initPluginLibsOnceFunc · L200](../../../src/plugin/gin.cc#L200)
- 函数 [ncclGinPluginFinalize · L264](../../../src/plugin/gin.cc#L264)
- 函数 [ncclGinInit · L275](../../../src/plugin/gin.cc#L275)
- 函数 [ncclGinInitFromParent · L311](../../../src/plugin/gin.cc#L311)
- 函数 [ncclGinFinalize · L324](../../../src/plugin/gin.cc#L324)
- 函数 [ncclGinGetDevCount · L333](../../../src/plugin/gin.cc#L333)
- 函数 [ncclGetBackendPriority · L343](../../../src/plugin/gin.cc#L343)
- 函数 [ncclCompareBackendPriority · L359](../../../src/plugin/gin.cc#L359)
- 函数 [ncclGinSetDefaultBackend · L375](../../../src/plugin/gin.cc#L375)

## src/plugin/gin/gin_v13.cc

[整个文件](../../../src/plugin/gin/gin_v13.cc)

- 函数 [ncclGin_getGinProperties · L16](../../../src/plugin/gin/gin_v13.cc#L16)
- 函数 [ncclGin_connect · L23](../../../src/plugin/gin/gin_v13.cc#L23)
- 函数 [ncclGin_createContext · L29](../../../src/plugin/gin/gin_v13.cc#L29)
- 函数 [getNcclGin_v13 · L41](../../../src/plugin/gin/gin_v13.cc#L41)

## src/plugin/gin/gin_v14.cc

[整个文件](../../../src/plugin/gin/gin_v14.cc)

- 函数 [ncclGin_v14_connect · L16](../../../src/plugin/gin/gin_v14.cc#L16)
- 函数 [ncclGin_v14_getGinProperties · L22](../../../src/plugin/gin/gin_v14.cc#L22)
- 函数 [ncclGin_v14_createContext · L33](../../../src/plugin/gin/gin_v14.cc#L33)
- 函数 [getNcclGin_v14 · L47](../../../src/plugin/gin/gin_v14.cc#L47)

## src/plugin/gin/gin_v15.cc

[整个文件](../../../src/plugin/gin/gin_v15.cc)

- 函数 [getNcclGin_v15 · L14](../../../src/plugin/gin/gin_v15.cc#L14)

## src/plugin/net.cc

[整个文件](../../../src/plugin/net.cc)

- 枚举 [ncclNetPluginState · L54](../../../src/plugin/net.cc#L54)
- 结构体 [netPluginLib · L63](../../../src/plugin/net.cc#L63)
- 函数 [ncclNetPluginUnload · L84](../../../src/plugin/net.cc#L84)
- 函数 [ncclNetPluginLoad · L103](../../../src/plugin/net.cc#L103)
- 函数 [ncclNetCheckDeviceVersion · L153](../../../src/plugin/net.cc#L153)
- 函数 [ncclNetGetProfilerCallback · L178](../../../src/plugin/net.cc#L178)
- 函数 [ncclNetPluginInit · L186](../../../src/plugin/net.cc#L186)
- 函数 [ncclNetPluginAssignToComm · L238](../../../src/plugin/net.cc#L238)
- 函数 [ncclNetPluginDisableOtherExternal · L257](../../../src/plugin/net.cc#L257)
- 函数 [ncclNetPluginRegisterInternal · L275](../../../src/plugin/net.cc#L275)
- 函数 [initPluginLibsOnceFunc · L288](../../../src/plugin/net.cc#L288)
- 函数 [ncclNetPluginFinalize · L342](../../../src/plugin/net.cc#L342)
- 函数 [ncclNetInit · L357](../../../src/plugin/net.cc#L357)
- 函数 [ncclNetInitFromParent · L392](../../../src/plugin/net.cc#L392)
- 函数 [ncclNetFinalize · L411](../../../src/plugin/net.cc#L411)
- 函数 [ncclNetGetDevCount · L418](../../../src/plugin/net.cc#L418)
- 函数 [ncclCollNetGetDevCount · L431](../../../src/plugin/net.cc#L431)
- 函数 [ncclNetSetVirtDevCount · L444](../../../src/plugin/net.cc#L444)
- 函数 [ncclCollNetSetVirtDevCount · L454](../../../src/plugin/net.cc#L454)
- 函数 [ncclGpuGdrSupport · L464](../../../src/plugin/net.cc#L464)

## src/plugin/net/net_v10.cc

[整个文件](../../../src/plugin/net/net_v10.cc)

- 函数 [ncclNet_getProperties · L23](../../../src/plugin/net/net_v10.cc#L23)
- 函数 [ncclNet_listen · L52](../../../src/plugin/net/net_v10.cc#L52)
- 函数 [ncclNet_connect · L56](../../../src/plugin/net/net_v10.cc#L56)
- 函数 [ncclNet_makeVDevice · L61](../../../src/plugin/net/net_v10.cc#L61)
- 函数 [ncclNet_finalize · L67](../../../src/plugin/net/net_v10.cc#L67)
- 函数 [ncclNet_init · L73](../../../src/plugin/net/net_v10.cc#L73)
- 函数 [getNcclNet_v10 · L119](../../../src/plugin/net/net_v10.cc#L119)
- 函数 [ncclCollNet_getProperties · L130](../../../src/plugin/net/net_v10.cc#L130)
- 函数 [ncclCollNet_listen · L159](../../../src/plugin/net/net_v10.cc#L159)
- 函数 [ncclCollNet_iallgather · L163](../../../src/plugin/net/net_v10.cc#L163)
- 函数 [ncclCollNet_ireducescatter · L170](../../../src/plugin/net/net_v10.cc#L170)
- 函数 [ncclCollNet_makeVDevice · L178](../../../src/plugin/net/net_v10.cc#L178)
- 函数 [ncclCollNet_finalize · L184](../../../src/plugin/net/net_v10.cc#L184)
- 函数 [ncclCollNet_init · L189](../../../src/plugin/net/net_v10.cc#L189)
- 函数 [getNcclCollNet_v10 · L219](../../../src/plugin/net/net_v10.cc#L219)

## src/plugin/net/net_v11.cc

[整个文件](../../../src/plugin/net/net_v11.cc)

- 函数 [ncclNet_getProperties · L17](../../../src/plugin/net/net_v11.cc#L17)
- 函数 [ncclNet_makeVDevice · L44](../../../src/plugin/net/net_v11.cc#L44)
- 函数 [ncclNet_setNetAttr · L50](../../../src/plugin/net/net_v11.cc#L50)
- 函数 [ncclNet_init · L54](../../../src/plugin/net/net_v11.cc#L54)
- 函数 [getNcclNet_v11 · L81](../../../src/plugin/net/net_v11.cc#L81)
- 函数 [ncclCollNet_getProperties · L92](../../../src/plugin/net/net_v11.cc#L92)
- 函数 [ncclCollNet_iallgather · L119](../../../src/plugin/net/net_v11.cc#L119)
- 函数 [ncclCollNet_ireducescatter · L127](../../../src/plugin/net/net_v11.cc#L127)
- 函数 [ncclCollNet_makeVDevice · L136](../../../src/plugin/net/net_v11.cc#L136)
- 函数 [ncclCollNet_init · L142](../../../src/plugin/net/net_v11.cc#L142)
- 函数 [getNcclCollNet_v11 · L164](../../../src/plugin/net/net_v11.cc#L164)

## src/plugin/net/net_v12.cc

[整个文件](../../../src/plugin/net/net_v12.cc)

- 函数 [getNcclNet_v12 · L15](../../../src/plugin/net/net_v12.cc#L15)
- 函数 [getNcclCollNet_v12 · L24](../../../src/plugin/net/net_v12.cc#L24)

## src/plugin/net/net_v6.cc

[整个文件](../../../src/plugin/net/net_v6.cc)

- 函数 [ncclNet_getProperties · L23](../../../src/plugin/net/net_v6.cc#L23)
- 函数 [ncclNet_regMr · L51](../../../src/plugin/net/net_v6.cc#L51)
- 函数 [ncclNet_listen · L56](../../../src/plugin/net/net_v6.cc#L56)
- 函数 [ncclNet_connect · L60](../../../src/plugin/net/net_v6.cc#L60)
- 函数 [ncclNet_accept · L65](../../../src/plugin/net/net_v6.cc#L65)
- 函数 [ncclNet_isend · L69](../../../src/plugin/net/net_v6.cc#L69)
- 函数 [ncclNet_irecv · L78](../../../src/plugin/net/net_v6.cc#L78)
- 函数 [ncclNet_finalize · L91](../../../src/plugin/net/net_v6.cc#L91)
- 函数 [ncclCollNet_getProperties · L96](../../../src/plugin/net/net_v6.cc#L96)
- 函数 [ncclCollNet_listen · L124](../../../src/plugin/net/net_v6.cc#L124)
- 函数 [ncclCollNet_regMr · L128](../../../src/plugin/net/net_v6.cc#L128)
- 函数 [ncclCollNet_iallreduce · L133](../../../src/plugin/net/net_v6.cc#L133)
- 函数 [ncclCollNet_finalize · L144](../../../src/plugin/net/net_v6.cc#L144)
- 函数 [ncclNet_init · L149](../../../src/plugin/net/net_v6.cc#L149)
- 函数 [getNcclNet_v6 · L182](../../../src/plugin/net/net_v6.cc#L182)
- 函数 [ncclCollNet_init · L193](../../../src/plugin/net/net_v6.cc#L193)
- 函数 [getNcclCollNet_v6 · L223](../../../src/plugin/net/net_v6.cc#L223)

## src/plugin/net/net_v7.cc

[整个文件](../../../src/plugin/net/net_v7.cc)

- 函数 [ncclNet_getProperties · L23](../../../src/plugin/net/net_v7.cc#L23)
- 函数 [ncclNet_listen · L51](../../../src/plugin/net/net_v7.cc#L51)
- 函数 [ncclNet_connect · L55](../../../src/plugin/net/net_v7.cc#L55)
- 函数 [ncclNet_regMr · L60](../../../src/plugin/net/net_v7.cc#L60)
- 函数 [ncclNet_isend · L65](../../../src/plugin/net/net_v7.cc#L65)
- 函数 [ncclNet_irecv · L74](../../../src/plugin/net/net_v7.cc#L74)
- 函数 [ncclNet_finalize · L87](../../../src/plugin/net/net_v7.cc#L87)
- 函数 [ncclCollNet_getProperties · L92](../../../src/plugin/net/net_v7.cc#L92)
- 函数 [ncclCollNet_listen · L120](../../../src/plugin/net/net_v7.cc#L120)
- 函数 [ncclCollNet_regMr · L124](../../../src/plugin/net/net_v7.cc#L124)
- 函数 [ncclCollNet_iallreduce · L129](../../../src/plugin/net/net_v7.cc#L129)
- 函数 [ncclCollNet_finalize · L140](../../../src/plugin/net/net_v7.cc#L140)
- 函数 [ncclNet_init · L145](../../../src/plugin/net/net_v7.cc#L145)
- 函数 [getNcclNet_v7 · L178](../../../src/plugin/net/net_v7.cc#L178)
- 函数 [ncclCollNet_init · L189](../../../src/plugin/net/net_v7.cc#L189)
- 函数 [getNcclCollNet_v7 · L218](../../../src/plugin/net/net_v7.cc#L218)

## src/plugin/net/net_v8.cc

[整个文件](../../../src/plugin/net/net_v8.cc)

- 函数 [ncclNet_getProperties · L23](../../../src/plugin/net/net_v8.cc#L23)
- 函数 [ncclNet_listen · L51](../../../src/plugin/net/net_v8.cc#L51)
- 函数 [ncclNet_connect · L55](../../../src/plugin/net/net_v8.cc#L55)
- 函数 [ncclNet_isend · L60](../../../src/plugin/net/net_v8.cc#L60)
- 函数 [ncclNet_irecv · L69](../../../src/plugin/net/net_v8.cc#L69)
- 函数 [ncclNet_finalize · L82](../../../src/plugin/net/net_v8.cc#L82)
- 函数 [ncclCollNet_getProperties · L87](../../../src/plugin/net/net_v8.cc#L87)
- 函数 [ncclCollNet_listen · L115](../../../src/plugin/net/net_v8.cc#L115)
- 函数 [ncclCollNet_iallreduce · L119](../../../src/plugin/net/net_v8.cc#L119)
- 函数 [ncclCollNet_iallgather · L130](../../../src/plugin/net/net_v8.cc#L130)
- 函数 [ncclCollNet_ireducescatter · L144](../../../src/plugin/net/net_v8.cc#L144)
- 函数 [ncclCollNet_finalize · L159](../../../src/plugin/net/net_v8.cc#L159)
- 函数 [ncclNet_init · L164](../../../src/plugin/net/net_v8.cc#L164)
- 函数 [getNcclNet_v8 · L197](../../../src/plugin/net/net_v8.cc#L197)
- 函数 [ncclCollNet_init · L208](../../../src/plugin/net/net_v8.cc#L208)
- 函数 [getNcclCollNet_v8 · L238](../../../src/plugin/net/net_v8.cc#L238)

## src/plugin/net/net_v9.cc

[整个文件](../../../src/plugin/net/net_v9.cc)

- 函数 [ncclNet_getProperties · L23](../../../src/plugin/net/net_v9.cc#L23)
- 函数 [ncclNet_isend · L52](../../../src/plugin/net/net_v9.cc#L52)
- 函数 [ncclNet_irecv · L57](../../../src/plugin/net/net_v9.cc#L57)
- 函数 [ncclNet_listen · L62](../../../src/plugin/net/net_v9.cc#L62)
- 函数 [ncclNet_connect · L66](../../../src/plugin/net/net_v9.cc#L66)
- 函数 [ncclNet_makeVDevice · L71](../../../src/plugin/net/net_v9.cc#L71)
- 函数 [ncclNet_finalize · L77](../../../src/plugin/net/net_v9.cc#L77)
- 函数 [ncclCollNet_getProperties · L82](../../../src/plugin/net/net_v9.cc#L82)
- 函数 [ncclCollNet_listen · L111](../../../src/plugin/net/net_v9.cc#L111)
- 函数 [ncclCollNet_iallgather · L115](../../../src/plugin/net/net_v9.cc#L115)
- 函数 [ncclCollNet_ireducescatter · L122](../../../src/plugin/net/net_v9.cc#L122)
- 函数 [ncclCollNet_makeVDevice · L130](../../../src/plugin/net/net_v9.cc#L130)
- 函数 [ncclCollNet_finalize · L136](../../../src/plugin/net/net_v9.cc#L136)
- 函数 [ncclNet_init · L141](../../../src/plugin/net/net_v9.cc#L141)
- 函数 [getNcclNet_v9 · L174](../../../src/plugin/net/net_v9.cc#L174)
- 函数 [ncclCollNet_init · L185](../../../src/plugin/net/net_v9.cc#L185)
- 函数 [getNcclCollNet_v9 · L215](../../../src/plugin/net/net_v9.cc#L215)

## src/plugin/plugin_open.cc

[整个文件](../../../src/plugin/plugin_open.cc)

- 函数 [tryOpenLib · L31](../../../src/plugin/plugin_open.cc#L31)
- 函数 [appendNameToList · L59](../../../src/plugin/plugin_open.cc#L59)
- 函数 [getLibPath · L65](../../../src/plugin/plugin_open.cc#L65)
- 函数 [getLibPath · L71](../../../src/plugin/plugin_open.cc#L71)
- 函数 [openPluginLib · L79](../../../src/plugin/plugin_open.cc#L79)
- 函数 [ncclOpenNetPluginLib · L132](../../../src/plugin/plugin_open.cc#L132)
- 函数 [ncclOpenGinPluginLib · L136](../../../src/plugin/plugin_open.cc#L136)
- 函数 [ncclOpenRmaPluginLib · L140](../../../src/plugin/plugin_open.cc#L140)
- 函数 [ncclOpenTunerPluginLib · L144](../../../src/plugin/plugin_open.cc#L144)
- 函数 [ncclOpenProfilerPluginLib · L148](../../../src/plugin/plugin_open.cc#L148)
- 函数 [ncclOpenEnvPluginLib · L152](../../../src/plugin/plugin_open.cc#L152)
- 函数 [ncclGetGinPluginLib · L156](../../../src/plugin/plugin_open.cc#L156)
- 函数 [ncclGetNetPluginLib · L166](../../../src/plugin/plugin_open.cc#L166)
- 函数 [ncclClosePluginLib · L176](../../../src/plugin/plugin_open.cc#L176)
- 函数 [ncclClosePluginLibHandle · L191](../../../src/plugin/plugin_open.cc#L191)
- 函数 [ncclDetachPluginLibHandle · L198](../../../src/plugin/plugin_open.cc#L198)
- 函数 [ncclGetPluginLibName · L207](../../../src/plugin/plugin_open.cc#L207)

## src/plugin/profiler.cc

[整个文件](../../../src/plugin/profiler.cc)

- 结构体 [ncclProfilerClockCalib · L59](../../../src/plugin/profiler.cc#L59)
- 结构体 [ncclProfilerThread · L74](../../../src/plugin/profiler.cc#L74)
- 枚举 [ncclProfilerThreadAction · L109](../../../src/plugin/profiler.cc#L109)
- 结构体 [ncclProfilerPlugin · L119](../../../src/plugin/profiler.cc#L119)
- 结构体 [ncclProfilerMultiContext · L135](../../../src/plugin/profiler.cc#L135)
- 函数 [profilerTsModeGet · L174](../../../src/plugin/profiler.cc#L174)
- 函数 [profilerApplyConfig · L178](../../../src/plugin/profiler.cc#L178)
- 函数 [profilerApplyPluginConfig · L207](../../../src/plugin/profiler.cc#L207)
- 函数 [profilerCpuNow · L226](../../../src/plugin/profiler.cc#L226)
- 函数 [profilerMonoNow · L246](../../../src/plugin/profiler.cc#L246)
- 函数 [profilerClockCalibInit · L262](../../../src/plugin/profiler.cc#L262)
- 函数 [profilerClockCalibFree · L278](../../../src/plugin/profiler.cc#L278)
- 函数 [profilerClockProbeReport · L294](../../../src/plugin/profiler.cc#L294)
- 函数 [profilerClockKeepBest · L306](../../../src/plugin/profiler.cc#L306)
- 函数 [profilerClockProbe · L319](../../../src/plugin/profiler.cc#L319)
- 函数 [profilerClockCalibUpdate · L347](../../../src/plugin/profiler.cc#L347)
- 函数 [profilerClockCalibMaybe · L365](../../../src/plugin/profiler.cc#L365)
- 函数 [profilerMapGpuToCpu · L376](../../../src/plugin/profiler.cc#L376)
- 函数 [profilerActivate · L403](../../../src/plugin/profiler.cc#L403)
- 函数 [profilerTrimRange · L408](../../../src/plugin/profiler.cc#L408)
- 函数 [profilerGetPlugin · L413](../../../src/plugin/profiler.cc#L413)
- 函数 [profilerPluginAdd · L437](../../../src/plugin/profiler.cc#L437)
- 函数 [ncclProfilerPluginLoad · L468](../../../src/plugin/profiler.cc#L468)
- 函数 [ncclProfilerPluginUnload · L558](../../../src/plugin/profiler.cc#L558)
- 函数 [printProfilerEventMask · L677](../../../src/plugin/profiler.cc#L677)
- 函数 [ncclProfilerEnforceMaskDeps · L708](../../../src/plugin/profiler.cc#L708)
- 函数 [profilerEventGate · L725](../../../src/plugin/profiler.cc#L725)
- 函数 [profilerMaskWithDeps · L755](../../../src/plugin/profiler.cc#L755)
- 函数 [profilerPluginEffectiveMask · L763](../../../src/plugin/profiler.cc#L763)
- 函数 [profilerRefreshEventMask · L771](../../../src/plugin/profiler.cc#L771)
- 函数 [ncclProfilerCurrentEventMask · L795](../../../src/plugin/profiler.cc#L795)
- 函数 [profilerApplyMaskDeps · L804](../../../src/plugin/profiler.cc#L804)
- 函数 [profilerLive · L811](../../../src/plugin/profiler.cc#L811)
- 函数 [profilerSetParents · L817](../../../src/plugin/profiler.cc#L817)
- 枚举 [profilerTimestampKind · L825](../../../src/plugin/profiler.cc#L825)
- 函数 [profilerStampDescr · L831](../../../src/plugin/profiler.cc#L831)
- 函数 [profilerStampArgs · L842](../../../src/plugin/profiler.cc#L842)
- 函数 [profilerStartDispatch · L859](../../../src/plugin/profiler.cc#L859)
- 函数 [profilerStart · L888](../../../src/plugin/profiler.cc#L888)
- 函数 [profilerStartNone · L893](../../../src/plugin/profiler.cc#L893)
- 函数 [profilerStartGpu · L899](../../../src/plugin/profiler.cc#L899)
- 函数 [profilerStopDispatch · L905](../../../src/plugin/profiler.cc#L905)
- 函数 [profilerStop · L927](../../../src/plugin/profiler.cc#L927)
- 函数 [profilerStopNone · L931](../../../src/plugin/profiler.cc#L931)
- 函数 [profilerStopGpu · L935](../../../src/plugin/profiler.cc#L935)
- 函数 [profilerRecordDispatch · L939](../../../src/plugin/profiler.cc#L939)
- 函数 [profilerRecord · L958](../../../src/plugin/profiler.cc#L958)
- 函数 [profilerRecordGpu · L965](../../../src/plugin/profiler.cc#L965)
- 函数 [profilerStartNet · L976](../../../src/plugin/profiler.cc#L976)
- 函数 [profilerStopNet · L994](../../../src/plugin/profiler.cc#L994)
- 函数 [profilerRecordNet · L1010](../../../src/plugin/profiler.cc#L1010)
- 函数 [profilerInitMulti · L1034](../../../src/plugin/profiler.cc#L1034)
- 函数 [profilerFinalizeMulti · L1069](../../../src/plugin/profiler.cc#L1069)
- 函数 [ncclProfilerSetRasOverride · L1081](../../../src/plugin/profiler.cc#L1081)
- 函数 [ncclProfilerPluginInit · L1098](../../../src/plugin/profiler.cc#L1098)
- 函数 [ncclProfilerPluginFinalize · L1148](../../../src/plugin/profiler.cc#L1148)
- 函数 [ncclProfilerStartGroupApiEvent · L1173](../../../src/plugin/profiler.cc#L1173)
- 函数 [ncclProfilerStopGroupApiEvent · L1194](../../../src/plugin/profiler.cc#L1194)
- 函数 [ncclProfilerRecordGroupApiEventState · L1199](../../../src/plugin/profiler.cc#L1199)
- 函数 [ncclProfilerStartP2pApiEvent · L1213](../../../src/plugin/profiler.cc#L1213)
- 函数 [ncclProfilerStopP2pApiEvent · L1238](../../../src/plugin/profiler.cc#L1238)
- 函数 [ncclProfilerStartCollApiEvent · L1243](../../../src/plugin/profiler.cc#L1243)
- 函数 [ncclProfilerStopCollApiEvent · L1269](../../../src/plugin/profiler.cc#L1269)
- 函数 [ncclProfilerStartKernelLaunchEvent · L1274](../../../src/plugin/profiler.cc#L1274)
- 函数 [ncclProfilerStopKernelLaunchEvent · L1309](../../../src/plugin/profiler.cc#L1309)
- 函数 [ncclProfilerStartGroupEvent · L1314](../../../src/plugin/profiler.cc#L1314)
- 函数 [ncclProfilerStopGroupEvent · L1346](../../../src/plugin/profiler.cc#L1346)
- 函数 [ncclProfilerStartTaskEvents · L1353](../../../src/plugin/profiler.cc#L1353)
- 函数 [ncclProfilerStopTaskEvents · L1426](../../../src/plugin/profiler.cc#L1426)
- 函数 [ncclProfilerStartProxyOpEvent · L1447](../../../src/plugin/profiler.cc#L1447)
- 函数 [ncclProfilerStopProxyOpEvent · L1466](../../../src/plugin/profiler.cc#L1466)
- 函数 [ncclProfilerStartSendProxyStepEvent · L1473](../../../src/plugin/profiler.cc#L1473)
- 函数 [ncclProfilerStartRecvProxyStepEvent · L1491](../../../src/plugin/profiler.cc#L1491)
- 函数 [ncclProfilerStopProxyStepEvent · L1509](../../../src/plugin/profiler.cc#L1509)
- 函数 [ncclProfilerStartProxyCtrlEvent · L1517](../../../src/plugin/profiler.cc#L1517)
- 函数 [ncclProfilerStopProxyCtrlEvent · L1529](../../../src/plugin/profiler.cc#L1529)
- 函数 [ncclProfilerStartKernelChEvent · L1536](../../../src/plugin/profiler.cc#L1536)
- 函数 [ncclProfilerStopKernelChEvent · L1547](../../../src/plugin/profiler.cc#L1547)
- 函数 [ncclProfilerRecordProxyOpEventState · L1557](../../../src/plugin/profiler.cc#L1557)
- 函数 [ncclProfilerRecordProxyStepEventState · L1565](../../../src/plugin/profiler.cc#L1565)
- 函数 [ncclProfilerRecordProxyCtrlEventState · L1576](../../../src/plugin/profiler.cc#L1576)
- 函数 [ncclProfilerAddPidToProxyOp · L1588](../../../src/plugin/profiler.cc#L1588)
- 函数 [profilerAllocOp · L1594](../../../src/plugin/profiler.cc#L1594)
- 函数 [profilerRecycleList · L1599](../../../src/plugin/profiler.cc#L1599)
- 函数 [profilerFireKernelPhaseEvents · L1611](../../../src/plugin/profiler.cc#L1611)
- 函数 [profilerProgressOps · L1662](../../../src/plugin/profiler.cc#L1662)
- 函数 [appendWorkToActiveQueue · L1706](../../../src/plugin/profiler.cc#L1706)
- 函数 [waitForAction · L1721](../../../src/plugin/profiler.cc#L1721)
- 函数 [cleanupAndStop · L1740](../../../src/plugin/profiler.cc#L1740)
- 函数 [updateProgressInterval · L1758](../../../src/plugin/profiler.cc#L1758)
- 函数 [ncclProfilerThreadFunc · L1763](../../../src/plugin/profiler.cc#L1763)
- 函数 [ncclProfilerThreadCreate · L1836](../../../src/plugin/profiler.cc#L1836)
- 函数 [profilerPurgeByContext · L1868](../../../src/plugin/profiler.cc#L1868)
- 函数 [ncclProfilerThreadDestroy · L1887](../../../src/plugin/profiler.cc#L1887)
- 函数 [profilerEnqueueOp · L1922](../../../src/plugin/profiler.cc#L1922)
- 函数 [profilerPostWorkInternal · L1989](../../../src/plugin/profiler.cc#L1989)
- 函数 [profilerGetSymCounters · L2003](../../../src/plugin/profiler.cc#L2003)
- 函数 [ncclProfilerReserveSymCounters · L2012](../../../src/plugin/profiler.cc#L2012)
- 函数 [profilerPostPlanWorkSym · L2026](../../../src/plugin/profiler.cc#L2026)
- 函数 [ncclProfilerPostPlanWork · L2057](../../../src/plugin/profiler.cc#L2057)
- 函数 [ncclProfilerPluginLoaded · L2107](../../../src/plugin/profiler.cc#L2107)
- 函数 [ncclProfilerDeviceMode · L2111](../../../src/plugin/profiler.cc#L2111)
- 函数 [ncclProfilerCallback · L2122](../../../src/plugin/profiler.cc#L2122)
- 函数 [ncclProfilerStartCeCollEvent · L2151](../../../src/plugin/profiler.cc#L2151)
- 函数 [ncclProfilerStopCeCollEvent · L2175](../../../src/plugin/profiler.cc#L2175)
- 函数 [ncclProfilerStartCeSyncEvent · L2182](../../../src/plugin/profiler.cc#L2182)
- 函数 [ncclProfilerStopCeSyncEvent · L2198](../../../src/plugin/profiler.cc#L2198)
- 函数 [ncclProfilerStartCeBatchEvent · L2206](../../../src/plugin/profiler.cc#L2206)
- 函数 [ncclProfilerStopCeBatchEvent · L2226](../../../src/plugin/profiler.cc#L2226)

## src/plugin/profiler/profiler_shim.h

[整个文件](../../../src/plugin/profiler/profiler_shim.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/plugin/profiler/profiler_v1.cc

[整个文件](../../../src/plugin/profiler/profiler_v1.cc)

- 函数 [ncclStringToFunc · L16](../../../src/plugin/profiler/profiler_v1.cc#L16)
- 函数 [ncclStringToAlgo · L27](../../../src/plugin/profiler/profiler_v1.cc#L27)
- 函数 [ncclStringToProto · L37](../../../src/plugin/profiler/profiler_v1.cc#L37)
- 函数 [ncclStringToDatatype · L43](../../../src/plugin/profiler/profiler_v1.cc#L43)
- 函数 [ncclProfiler_startEvent · L57](../../../src/plugin/profiler/profiler_v1.cc#L57)
- 函数 [ncclProfiler_recordEventState · L121](../../../src/plugin/profiler/profiler_v1.cc#L121)
- 函数 [ncclProfiler_finalize · L145](../../../src/plugin/profiler/profiler_v1.cc#L145)
- 函数 [ncclProfiler_stopEvent · L149](../../../src/plugin/profiler/profiler_v1.cc#L149)
- 函数 [ncclProfiler_init · L155](../../../src/plugin/profiler/profiler_v1.cc#L155)

## src/plugin/profiler/profiler_v2.cc

[整个文件](../../../src/plugin/profiler/profiler_v2.cc)

- 函数 [ncclProfiler_startEvent · L16](../../../src/plugin/profiler/profiler_v2.cc#L16)
- 函数 [ncclProfiler_recordEventState · L79](../../../src/plugin/profiler/profiler_v2.cc#L79)
- 函数 [ncclProfiler_finalize · L103](../../../src/plugin/profiler/profiler_v2.cc#L103)
- 函数 [ncclProfiler_stopEvent · L107](../../../src/plugin/profiler/profiler_v2.cc#L107)
- 函数 [ncclProfiler_init · L113](../../../src/plugin/profiler/profiler_v2.cc#L113)

## src/plugin/profiler/profiler_v3.cc

[整个文件](../../../src/plugin/profiler/profiler_v3.cc)

- 函数 [ncclProfiler_startEvent · L16](../../../src/plugin/profiler/profiler_v3.cc#L16)
- 函数 [ncclProfiler_recordEventState · L89](../../../src/plugin/profiler/profiler_v3.cc#L89)
- 函数 [ncclProfiler_finalize · L113](../../../src/plugin/profiler/profiler_v3.cc#L113)
- 函数 [ncclProfiler_stopEvent · L117](../../../src/plugin/profiler/profiler_v3.cc#L117)
- 函数 [ncclProfiler_init · L123](../../../src/plugin/profiler/profiler_v3.cc#L123)

## src/plugin/profiler/profiler_v4.cc

[整个文件](../../../src/plugin/profiler/profiler_v4.cc)

- 函数 [ncclProfiler_startEvent · L16](../../../src/plugin/profiler/profiler_v4.cc#L16)
- 函数 [ncclProfiler_recordEventState · L85](../../../src/plugin/profiler/profiler_v4.cc#L85)
- 函数 [ncclProfiler_finalize · L119](../../../src/plugin/profiler/profiler_v4.cc#L119)
- 函数 [ncclProfiler_stopEvent · L123](../../../src/plugin/profiler/profiler_v4.cc#L123)
- 函数 [ncclProfiler_init · L129](../../../src/plugin/profiler/profiler_v4.cc#L129)

## src/plugin/profiler/profiler_v5.cc

[整个文件](../../../src/plugin/profiler/profiler_v5.cc)

- 函数 [ncclProfiler_startEvent · L16](../../../src/plugin/profiler/profiler_v5.cc#L16)
- 函数 [ncclProfiler_recordEventState · L124](../../../src/plugin/profiler/profiler_v5.cc#L124)
- 函数 [ncclProfiler_finalize · L175](../../../src/plugin/profiler/profiler_v5.cc#L175)
- 函数 [ncclProfiler_stopEvent · L179](../../../src/plugin/profiler/profiler_v5.cc#L179)
- 函数 [ncclProfiler_init · L185](../../../src/plugin/profiler/profiler_v5.cc#L185)

## src/plugin/profiler/profiler_v6.cc

[整个文件](../../../src/plugin/profiler/profiler_v6.cc)

- 函数 [ncclProfiler_startEvent · L25](../../../src/plugin/profiler/profiler_v6.cc#L25)
- 函数 [ncclProfiler_recordEventState · L162](../../../src/plugin/profiler/profiler_v6.cc#L162)
- 函数 [ncclProfiler_finalize · L199](../../../src/plugin/profiler/profiler_v6.cc#L199)
- 函数 [ncclProfiler_stopEvent · L203](../../../src/plugin/profiler/profiler_v6.cc#L203)
- 函数 [ncclProfiler_init · L209](../../../src/plugin/profiler/profiler_v6.cc#L209)

## src/plugin/profiler/profiler_v7.cc

[整个文件](../../../src/plugin/profiler/profiler_v7.cc)

- 函数 [ncclProfiler_startEvent · L27](../../../src/plugin/profiler/profiler_v7.cc#L27)
- 函数 [ncclProfiler_stopEvent · L149](../../../src/plugin/profiler/profiler_v7.cc#L149)
- 函数 [ncclProfiler_recordEventState · L155](../../../src/plugin/profiler/profiler_v7.cc#L155)
- 函数 [ncclProfiler_init · L193](../../../src/plugin/profiler/profiler_v7.cc#L193)
- 函数 [ncclProfiler_finalize · L201](../../../src/plugin/profiler/profiler_v7.cc#L201)

## src/plugin/profiler/profiler_v8.cc

[整个文件](../../../src/plugin/profiler/profiler_v8.cc)

- 函数 [getNcclProfiler_v8 · L14](../../../src/plugin/profiler/profiler_v8.cc#L14)

## src/plugin/rma.cc

[整个文件](../../../src/plugin/rma.cc)

- 枚举 [ncclRmaPluginState · L35](../../../src/plugin/rma.cc#L35)
- 结构体 [rmaPluginLib · L44](../../../src/plugin/rma.cc#L44)
- 函数 [ncclRmaPluginUnload · L59](../../../src/plugin/rma.cc#L59)
- 函数 [ncclRmaPluginLoad · L74](../../../src/plugin/rma.cc#L74)
- 函数 [ncclRmaPluginInit · L107](../../../src/plugin/rma.cc#L107)
- 函数 [ncclRmaPluginAssignToComm · L138](../../../src/plugin/rma.cc#L138)
- 函数 [ncclRmaPluginDisableOtherExternal · L152](../../../src/plugin/rma.cc#L152)
- 函数 [initPluginLibsOnceFunc · L170](../../../src/plugin/rma.cc#L170)
- 函数 [ncclRmaPluginFinalize · L240](../../../src/plugin/rma.cc#L240)
- 函数 [ncclRmaInit · L251](../../../src/plugin/rma.cc#L251)
- 函数 [ncclRmaInitFromParent · L285](../../../src/plugin/rma.cc#L285)
- 函数 [ncclRmaFinalize · L291](../../../src/plugin/rma.cc#L291)
- 函数 [ncclRmaGetDevCount · L300](../../../src/plugin/rma.cc#L300)

## src/plugin/rma/rma_v13.cc

[整个文件](../../../src/plugin/rma/rma_v13.cc)

- 函数 [ncclRma_init · L17](../../../src/plugin/rma/rma_v13.cc#L17)
- 函数 [ncclRma_createContext · L30](../../../src/plugin/rma/rma_v13.cc#L30)
- 函数 [ncclRma_regMrSym · L41](../../../src/plugin/rma/rma_v13.cc#L41)
- 函数 [ncclRma_regMrSymDmaBuf · L48](../../../src/plugin/rma/rma_v13.cc#L48)
- 函数 [ncclRma_getRmaProperties · L55](../../../src/plugin/rma/rma_v13.cc#L55)
- 函数 [ncclRma_iputSignal · L62](../../../src/plugin/rma/rma_v13.cc#L62)
- 函数 [ncclRma_connect · L72](../../../src/plugin/rma/rma_v13.cc#L72)
- 函数 [ncclRma_iput · L78](../../../src/plugin/rma/rma_v13.cc#L78)
- 函数 [ncclRma_iget · L84](../../../src/plugin/rma/rma_v13.cc#L84)
- 函数 [getNcclRma_v13 · L91](../../../src/plugin/rma/rma_v13.cc#L91)

## src/plugin/rma/rma_v14.cc

[整个文件](../../../src/plugin/rma/rma_v14.cc)

- 函数 [ncclRma_v14_getRmaProperties · L17](../../../src/plugin/rma/rma_v14.cc#L17)
- 函数 [ncclRma_v14_connect · L23](../../../src/plugin/rma/rma_v14.cc#L23)
- 函数 [ncclRma_v14_createContext · L29](../../../src/plugin/rma/rma_v14.cc#L29)
- 函数 [ncclRma_v14_iput · L38](../../../src/plugin/rma/rma_v14.cc#L38)
- 函数 [ncclRma_v14_iputSignal · L46](../../../src/plugin/rma/rma_v14.cc#L46)
- 函数 [ncclRma_v14_iget · L55](../../../src/plugin/rma/rma_v14.cc#L55)
- 函数 [getNcclRma_v14 · L62](../../../src/plugin/rma/rma_v14.cc#L62)

## src/plugin/rma/rma_v15.cc

[整个文件](../../../src/plugin/rma/rma_v15.cc)

- 函数 [ncclRma_v15_getRmaProperties · L16](../../../src/plugin/rma/rma_v15.cc#L16)
- 函数 [ncclRma_v15_connect · L22](../../../src/plugin/rma/rma_v15.cc#L22)
- 函数 [ncclRma_v15_createContext · L28](../../../src/plugin/rma/rma_v15.cc#L28)
- 函数 [getNcclRma_v15 · L37](../../../src/plugin/rma/rma_v15.cc#L37)

## src/plugin/rma/rma_v16.cc

[整个文件](../../../src/plugin/rma/rma_v16.cc)

- 函数 [ncclRma_v16_connect · L16](../../../src/plugin/rma/rma_v16.cc#L16)
- 函数 [ncclRma_v16_createContext · L22](../../../src/plugin/rma/rma_v16.cc#L22)
- 函数 [getNcclRma_v16 · L31](../../../src/plugin/rma/rma_v16.cc#L31)

## src/plugin/rma/rma_v17.cc

[整个文件](../../../src/plugin/rma/rma_v17.cc)

- 函数 [getNcclRma_v17 · L14](../../../src/plugin/rma/rma_v17.cc#L14)

## src/plugin/tuner.cc

[整个文件](../../../src/plugin/tuner.cc)

- 函数 [ncclTunerPluginLoad · L40](../../../src/plugin/tuner.cc#L40)
- 函数 [ncclTunerPluginUnload · L115](../../../src/plugin/tuner.cc#L115)

## src/plugin/tuner/tuner_v2.cc

[整个文件](../../../src/plugin/tuner/tuner_v2.cc)

- 函数 [hasNvlsSupport · L17](../../../src/plugin/tuner/tuner_v2.cc#L17)
- 函数 [hasCollNetSupport · L34](../../../src/plugin/tuner/tuner_v2.cc#L34)
- 函数 [ncclTuner_getCollInfo · L39](../../../src/plugin/tuner/tuner_v2.cc#L39)
- 函数 [ncclTuner_finalize · L57](../../../src/plugin/tuner/tuner_v2.cc#L57)
- 函数 [ncclTuner_init · L61](../../../src/plugin/tuner/tuner_v2.cc#L61)
- 函数 [getNcclTuner_v2 · L70](../../../src/plugin/tuner/tuner_v2.cc#L70)

## src/plugin/tuner/tuner_v3.cc

[整个文件](../../../src/plugin/tuner/tuner_v3.cc)

- 函数 [ncclTuner_getCollInfo · L17](../../../src/plugin/tuner/tuner_v3.cc#L17)
- 函数 [ncclTuner_finalize · L25](../../../src/plugin/tuner/tuner_v3.cc#L25)
- 函数 [ncclTuner_init · L29](../../../src/plugin/tuner/tuner_v3.cc#L29)
- 函数 [getNcclTuner_v3 · L39](../../../src/plugin/tuner/tuner_v3.cc#L39)

## src/plugin/tuner/tuner_v4.cc

[整个文件](../../../src/plugin/tuner/tuner_v4.cc)

- 函数 [ncclTuner_finalize · L17](../../../src/plugin/tuner/tuner_v4.cc#L17)
- 函数 [ncclTuner_init · L21](../../../src/plugin/tuner/tuner_v4.cc#L21)
- 函数 [getNcclTuner_v4 · L31](../../../src/plugin/tuner/tuner_v4.cc#L31)

## src/plugin/tuner/tuner_v5.cc

[整个文件](../../../src/plugin/tuner/tuner_v5.cc)

- 函数 [ncclTuner_getCollInfo · L17](../../../src/plugin/tuner/tuner_v5.cc#L17)
- 函数 [ncclTuner_finalize · L25](../../../src/plugin/tuner/tuner_v5.cc#L25)
- 函数 [ncclTuner_init · L29](../../../src/plugin/tuner/tuner_v5.cc#L29)
- 函数 [getNcclTuner_v5 · L42](../../../src/plugin/tuner/tuner_v5.cc#L42)

## src/plugin/tuner/tuner_v6.cc

[整个文件](../../../src/plugin/tuner/tuner_v6.cc)

- 函数 [ncclTuner_init · L16](../../../src/plugin/tuner/tuner_v6.cc#L16)
- 函数 [getNcclTuner_v6 · L29](../../../src/plugin/tuner/tuner_v6.cc#L29)

## src/plugin/tuner/tuner_v7.cc

[整个文件](../../../src/plugin/tuner/tuner_v7.cc)

- 函数 [getNcclTuner_v7 · L14](../../../src/plugin/tuner/tuner_v7.cc#L14)
