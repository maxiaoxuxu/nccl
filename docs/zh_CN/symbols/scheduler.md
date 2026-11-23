# scheduler 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/scheduler/allgatherv_sched.cc

[整个文件](../../../src/scheduler/allgatherv_sched.cc)

- 函数 [ncclScheduleBcastTasksToPlan · L13](../../../src/scheduler/allgatherv_sched.cc#L13)

## src/scheduler/symmetric_sched.cc

[整个文件](../../../src/scheduler/symmetric_sched.cc)

- 函数 [symkRedOp · L23](../../../src/scheduler/symmetric_sched.cc#L23)
- 函数 [convertSymTaskDevOp · L30](../../../src/scheduler/symmetric_sched.cc#L30)
- 函数 [symTaskHasForcedTuning · L66](../../../src/scheduler/symmetric_sched.cc#L66)
- 函数 [symBatchAlignment · L72](../../../src/scheduler/symmetric_sched.cc#L72)
- 函数 [symkMaxDevWorkArgsSize · L83](../../../src/scheduler/symmetric_sched.cc#L83)
- 函数 [setMinChunkPayloadBytes · L88](../../../src/scheduler/symmetric_sched.cc#L88)
- 函数 [setMinChunkPayloadBytes · L90](../../../src/scheduler/symmetric_sched.cc#L90)
- 函数 [ncclMakeSymmetricTaskList · L94](../../../src/scheduler/symmetric_sched.cc#L94)
- 函数 [ncclSymmetricTaskSchedulerImpl · L293](../../../src/scheduler/symmetric_sched.cc#L293)
- 函数 [ncclSymmetricTaskScheduler · L503](../../../src/scheduler/symmetric_sched.cc#L503)
