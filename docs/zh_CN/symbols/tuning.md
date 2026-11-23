# tuning 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/tuning/ce_model.cc

[整个文件](../../../src/tuning/ce_model.cc)

- 结构体 [ncclCeAgFloorParams · L18](../../../src/tuning/ce_model.cc#L18)
- 函数 [ncclCeArchBucket · L43](../../../src/tuning/ce_model.cc#L43)
- 函数 [ncclCeD2hBw · L51](../../../src/tuning/ce_model.cc#L51)
- 函数 [ncclCeAgLatencyUs · L56](../../../src/tuning/ce_model.cc#L56)
- 函数 [ncclTuningCeModelSim · L106](../../../src/tuning/ce_model.cc#L106)

## src/tuning/collnet.cc

[整个文件](../../../src/tuning/collnet.cc)

- 函数 [ncclTuningCollnetModelInit · L11](../../../src/tuning/collnet.cc#L11)
- 函数 [ncclTuningCollnetModelSim · L122](../../../src/tuning/collnet.cc#L122)

## src/tuning/cost_model.cc

[整个文件](../../../src/tuning/cost_model.cc)

- 函数 [parseList · L34](../../../src/tuning/cost_model.cc#L34)
- 函数 [isLL128Enabled · L125](../../../src/tuning/cost_model.cc#L125)
- 函数 [getModelEntry · L317](../../../src/tuning/cost_model.cc#L317)
- 函数 [ncclTuningCostModelPreInit · L331](../../../src/tuning/cost_model.cc#L331)
- 函数 [ncclTuningCostModelInit · L342](../../../src/tuning/cost_model.cc#L342)
- 函数 [ncclTuningCostModelFinalize · L489](../../../src/tuning/cost_model.cc#L489)
- 函数 [ncclTuningCostModelSimModel · L514](../../../src/tuning/cost_model.cc#L514)

## src/tuning/cost_model.h

[整个文件](../../../src/tuning/cost_model.h)

- 结构体 [ncclTuningModelState · L16](../../../src/tuning/cost_model.h#L16)
- 结构体 [ncclTuningModelEntry_t · L28](../../../src/tuning/cost_model.h#L28)

## src/tuning/genk_model.cc

[整个文件](../../../src/tuning/genk_model.cc)

- 函数 [ncclTuningGenkGetChannels · L22](../../../src/tuning/genk_model.cc#L22)
- 函数 [ncclGenkGetAlgorithmProtocol · L57](../../../src/tuning/genk_model.cc#L57)
- 函数 [ncclTuningGenkModelSim · L96](../../../src/tuning/genk_model.cc#L96)

## src/tuning/model.h

[整个文件](../../../src/tuning/model.h)

- 函数 [ncclSoftMin · L19](../../../src/tuning/model.h#L19)
- 函数 [ncclSoftPlus · L24](../../../src/tuning/model.h#L24)
- 函数 [ncclTuningProtoBWFactor · L39](../../../src/tuning/model.h#L39)
- 函数 [ncclTuningProtoBW · L45](../../../src/tuning/model.h#L45)

## src/tuning/nvls.cc

[整个文件](../../../src/tuning/nvls.cc)

- 函数 [ncclTuningNvlsModelInit · L12](../../../src/tuning/nvls.cc#L12)
- 函数 [ncclTuningNvlsModelSim · L123](../../../src/tuning/nvls.cc#L123)

## src/tuning/pat.cc

[整个文件](../../../src/tuning/pat.cc)

- 函数 [ncclPatEnable · L15](../../../src/tuning/pat.cc#L15)
- 函数 [ncclTuningPatModelInit · L27](../../../src/tuning/pat.cc#L27)
- 函数 [ncclTuningPatModelSim · L81](../../../src/tuning/pat.cc#L81)

## src/tuning/pipeline_model/nvls.cc

[整个文件](../../../src/tuning/pipeline_model/nvls.cc)

- 函数 [computeNVLSMaxBusBw · L15](../../../src/tuning/pipeline_model/nvls.cc#L15)
- 函数 [nvlsMaxBusBw · L38](../../../src/tuning/pipeline_model/nvls.cc#L38)
- 函数 [getNVLSSteps · L42](../../../src/tuning/pipeline_model/nvls.cc#L42)
- 函数 [ncclTuningPipelineNvlsGetAlgoStep · L46](../../../src/tuning/pipeline_model/nvls.cc#L46)
- 函数 [ncclTuningPipelineNvlsTreeGetAlgoStep · L66](../../../src/tuning/pipeline_model/nvls.cc#L66)
- 函数 [ncclTuningPipelineNVLSIsValid · L86](../../../src/tuning/pipeline_model/nvls.cc#L86)
- 函数 [ncclTuningPipelineNVLSTreeIsValid · L98](../../../src/tuning/pipeline_model/nvls.cc#L98)
- 函数 [ncclTuningPipelineNVLSComputePipeline · L108](../../../src/tuning/pipeline_model/nvls.cc#L108)
- 函数 [ncclTuningPipelineNvlsModelInit · L120](../../../src/tuning/pipeline_model/nvls.cc#L120)
- 函数 [ncclTuningPipelineNvlsTreeModelInit · L180](../../../src/tuning/pipeline_model/nvls.cc#L180)

## src/tuning/pipeline_model/pipeline_model.cc

[整个文件](../../../src/tuning/pipeline_model/pipeline_model.cc)

- 函数 [pipelineModel · L21](../../../src/tuning/pipeline_model/pipeline_model.cc#L21)
- 函数 [ncclTuningPipelineModelSim · L32](../../../src/tuning/pipeline_model/pipeline_model.cc#L32)

## src/tuning/pipeline_model/pipeline_model.h

[整个文件](../../../src/tuning/pipeline_model/pipeline_model.h)

- 结构体 [ncclTuningPipeline · L30](../../../src/tuning/pipeline_model/pipeline_model.h#L30)
- 结构体 [ncclTuningPipelineState · L38](../../../src/tuning/pipeline_model/pipeline_model.h#L38)
- 结构体 [ncclTuningPipelineStep · L45](../../../src/tuning/pipeline_model/pipeline_model.h#L45)
- 函数 [ncclTuningPipelineComputeSliceSize · L50](../../../src/tuning/pipeline_model/pipeline_model.h#L50)
- 函数 [ncclTuningPipelineComputeChunkSize · L73](../../../src/tuning/pipeline_model/pipeline_model.h#L73)
- 函数 [ncclTuningPreComputePipeline · L88](../../../src/tuning/pipeline_model/pipeline_model.h#L88)

## src/tuning/pipeline_model/ring.cc

[整个文件](../../../src/tuning/pipeline_model/ring.cc)

- 函数 [ringMaxBusBw · L15](../../../src/tuning/pipeline_model/ring.cc#L15)
- 函数 [ncclTuningPipelineRingGetAlgoStep · L25](../../../src/tuning/pipeline_model/ring.cc#L25)
- 函数 [ncclTuningPipelineRingIsValid · L44](../../../src/tuning/pipeline_model/ring.cc#L44)
- 函数 [ncclTuningPipelineRingComputePipeline · L49](../../../src/tuning/pipeline_model/ring.cc#L49)
- 函数 [ncclTuningPipelineRingModelInit · L83](../../../src/tuning/pipeline_model/ring.cc#L83)

## src/tuning/pipeline_model/tree.cc

[整个文件](../../../src/tuning/pipeline_model/tree.cc)

- 函数 [getTreeNsteps · L15](../../../src/tuning/pipeline_model/tree.cc#L15)
- 函数 [treeMaxBusBw · L22](../../../src/tuning/pipeline_model/tree.cc#L22)
- 函数 [ncclTuningPipelineTreeGetAlgoStep · L33](../../../src/tuning/pipeline_model/tree.cc#L33)
- 函数 [ncclTuningPipelineTreeIsValid · L50](../../../src/tuning/pipeline_model/tree.cc#L50)
- 函数 [ncclTuningPipelineTreeComputePipeline · L57](../../../src/tuning/pipeline_model/tree.cc#L57)
- 函数 [ncclTuningPipelineTreeModelInit · L76](../../../src/tuning/pipeline_model/tree.cc#L76)

## src/tuning/platforms/platforms.h

[整个文件](../../../src/tuning/platforms/platforms.h)

- 函数 [ncclTuningGetModelPlatformEntry · L17](../../../src/tuning/platforms/platforms.h#L17)
- 函数 [ncclTuningPlatformPreInit · L24](../../../src/tuning/platforms/platforms.h#L24)
- 函数 [ncclTuningPlatformChannelTuning · L31](../../../src/tuning/platforms/platforms.h#L31)

## src/tuning/platforms/rubin.h

[整个文件](../../../src/tuning/platforms/rubin.h)

- 函数 [ncclTuningRubinTuningConstants · L84](../../../src/tuning/platforms/rubin.h#L84)
- 函数 [ncclTuningRubinPreInit · L103](../../../src/tuning/platforms/rubin.h#L103)
- 函数 [ncclTuningRubinGetModelEntry · L111](../../../src/tuning/platforms/rubin.h#L111)
- 函数 [ncclTuningRubinChannelTuning · L118](../../../src/tuning/platforms/rubin.h#L118)

## src/tuning/ring.cc

[整个文件](../../../src/tuning/ring.cc)

- 函数 [getNetOverhead · L14](../../../src/tuning/ring.cc#L14)
- 函数 [ncclTuningRingModelInit · L21](../../../src/tuning/ring.cc#L21)
- 函数 [ncclTuningRingModelSim · L93](../../../src/tuning/ring.cc#L93)

## src/tuning/sym_model.cc

[整个文件](../../../src/tuning/sym_model.cc)

- 函数 [ncclSymkModelCtasEnvOverride · L23](../../../src/tuning/sym_model.cc#L23)
- 函数 [queryModel · L30](../../../src/tuning/sym_model.cc#L30)
- 函数 [ncclTuningSymkModelSim · L41](../../../src/tuning/sym_model.cc#L41)

## src/tuning/sym_model/gin.cc

[整个文件](../../../src/tuning/sym_model/gin.cc)

- 函数 [ncclTuningGetLsaBw · L29](../../../src/tuning/sym_model/gin.cc#L29)
- 函数 [ncclTuningGetGinLat · L34](../../../src/tuning/sym_model/gin.cc#L34)
- 函数 [ncclTuningGetGinBw · L39](../../../src/tuning/sym_model/gin.cc#L39)
- 函数 [ncclTuningGetBusMulReduceScatterRailA2A · L44](../../../src/tuning/sym_model/gin.cc#L44)
- 函数 [getSmBw_ReduceScatter_RailA2A · L61](../../../src/tuning/sym_model/gin.cc#L61)
- 函数 [ncclTuningGetSmLatReduceScatterRailA2A · L72](../../../src/tuning/sym_model/gin.cc#L72)
- 函数 [ncclTuningGetSmPenalty · L84](../../../src/tuning/sym_model/gin.cc#L84)
- 函数 [ncclSymkAlltoAllLLModel · L104](../../../src/tuning/sym_model/gin.cc#L104)
- 函数 [ncclTuningCalcSatBlocksReduceScatterRailA2A · L145](../../../src/tuning/sym_model/gin.cc#L145)
- 函数 [ncclSymkGinModel · L159](../../../src/tuning/sym_model/gin.cc#L159)

## src/tuning/sym_model/lsa.cc

[整个文件](../../../src/tuning/sym_model/lsa.cc)

- 函数 [evaluateLsaEstimate · L17](../../../src/tuning/sym_model/lsa.cc#L17)
- 函数 [ncclSymkLsaModel · L35](../../../src/tuning/sym_model/lsa.cc#L35)

## src/tuning/sym_model/lsa_a2a.cc

[整个文件](../../../src/tuning/sym_model/lsa_a2a.cc)

- 枚举 [ncclSymkLsaA2AAllGatherKernel · L16](../../../src/tuning/sym_model/lsa_a2a.cc#L16)
- 枚举 [ncclSymkLsaA2AReduceScatterKernel · L26](../../../src/tuning/sym_model/lsa_a2a.cc#L26)
- 枚举 [ncclSymkLsaA2AAllReduceKernel · L34](../../../src/tuning/sym_model/lsa_a2a.cc#L34)
- 结构体 [ncclSymkLsaA2ACtaScalingCurve · L43](../../../src/tuning/sym_model/lsa_a2a.cc#L43)
- 结构体 [ncclSymkLsaA2AKernelTuningParameters · L47](../../../src/tuning/sym_model/lsa_a2a.cc#L47)
- 结构体 [ncclSymkLsaA2AReduceScatterTuningParameters · L62](../../../src/tuning/sym_model/lsa_a2a.cc#L62)
- 枚举 [ncclSymkLsaA2AArch · L69](../../../src/tuning/sym_model/lsa_a2a.cc#L69)
- 结构体 [ncclSymkLsaA2AArchTuningParameters · L76](../../../src/tuning/sym_model/lsa_a2a.cc#L76)
- 函数 [lsaA2AParameters · L82](../../../src/tuning/sym_model/lsa_a2a.cc#L82)
- 函数 [lsaA2AArchTuningForComm · L179](../../../src/tuning/sym_model/lsa_a2a.cc#L179)
- 函数 [lsaA2AAllGatherKernelIndex · L186](../../../src/tuning/sym_model/lsa_a2a.cc#L186)
- 函数 [lsaA2AReduceScatterKernelIndex · L205](../../../src/tuning/sym_model/lsa_a2a.cc#L205)
- 函数 [lsaA2AAllReduceKernelIndex · L220](../../../src/tuning/sym_model/lsa_a2a.cc#L220)
- 函数 [lsaA2AActiveCtas · L237](../../../src/tuning/sym_model/lsa_a2a.cc#L237)
- 函数 [lsaA2AAllGatherCtaScale · L244](../../../src/tuning/sym_model/lsa_a2a.cc#L244)
- 函数 [lsaA2AParametersForKernel · L268](../../../src/tuning/sym_model/lsa_a2a.cc#L268)
- 函数 [ncclSymkLsaA2AModel · L303](../../../src/tuning/sym_model/lsa_a2a.cc#L303)

## src/tuning/sym_model/lsa_base.cc

[整个文件](../../../src/tuning/sym_model/lsa_base.cc)

- 函数 [ncclSymkLsaBaseModel · L15](../../../src/tuning/sym_model/lsa_base.cc#L15)

## src/tuning/sym_model/model.h

[整个文件](../../../src/tuning/sym_model/model.h)

- 结构体 [ncclSymkLsaEstimate · L19](../../../src/tuning/sym_model/model.h#L19)

## src/tuning/tree.cc

[整个文件](../../../src/tuning/tree.cc)

- 函数 [ncclTuningTreeModelInit · L11](../../../src/tuning/tree.cc#L11)
- 函数 [ncclTuningTreeModelSim · L64](../../../src/tuning/tree.cc#L64)

## src/tuning/tuning.cc

[整个文件](../../../src/tuning/tuning.cc)

- 函数 [ncclTuningResultListFree · L20](../../../src/tuning/tuning.cc#L20)
- 函数 [ncclTuningResultListPushFront · L30](../../../src/tuning/tuning.cc#L30)
- 函数 [ncclTuningInit · L42](../../../src/tuning/tuning.cc#L42)
- 函数 [ncclTuningFinalize · L110](../../../src/tuning/tuning.cc#L110)
- 函数 [ncclTuningComputeAllTunings · L126](../../../src/tuning/tuning.cc#L126)
- 函数 [ncclTuningSelectBestTuning · L153](../../../src/tuning/tuning.cc#L153)
- 函数 [ncclTuningCompute · L180](../../../src/tuning/tuning.cc#L180)
- 函数 [ncclTuningComputeTuning · L347](../../../src/tuning/tuning.cc#L347)

## src/tuning/tuning_general.cc

[整个文件](../../../src/tuning/tuning_general.cc)

- 函数 [ncclTuningGetNsteps · L18](../../../src/tuning/tuning_general.cc#L18)
- 函数 [ncclTuningGetCompCapIndex · L28](../../../src/tuning/tuning_general.cc#L28)
- 函数 [ncclTuningGetConstantsIndexes · L43](../../../src/tuning/tuning_general.cc#L43)
- 函数 [ncclTuningGetHwIndexes · L52](../../../src/tuning/tuning_general.cc#L52)
- 函数 [ncclTuningGetTime · L58](../../../src/tuning/tuning_general.cc#L58)
- 函数 [ncclTuningGetNthreads · L75](../../../src/tuning/tuning_general.cc#L75)
- 函数 [ncclTuningSetThreadThresholds · L94](../../../src/tuning/tuning_general.cc#L94)
- 函数 [ncclTuningGetChannels · L149](../../../src/tuning/tuning_general.cc#L149)
- 函数 [ncclTuningExpandId · L214](../../../src/tuning/tuning_general.cc#L214)
- 函数 [ncclTuningGetActiveChannels · L238](../../../src/tuning/tuning_general.cc#L238)

## src/tuning/tuning_int.h

[整个文件](../../../src/tuning/tuning_int.h)

- 结构体 [ncclTuningResultListNode · L15](../../../src/tuning/tuning_int.h#L15)
- 结构体 [ncclTuningResultList_t · L20](../../../src/tuning/tuning_int.h#L20)
