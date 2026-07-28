# 日报 · 2026-07-28

- 最近生成时间：2026-07-28 21:40:20 UTC
- 今日累计更新：1 次
- 今日累计推荐总数：13
- 精读区：6
- 速读区：7

## 今日简报（AI）
今天深入剖析了大模型推理的异构协同与动态调度，覆盖统一内存计算、MoE分布感知及稀疏注意力索引优化。  
最值得关注的是FusionML在Apple Silicon统一内存上的CPU+GPU协同预填充机制，以及解构MoE专家负载倾斜的自适应内核分派方法。  
建议从这两篇高分论文入手，理解硬件特性如何重塑推理阶段的计算与数据调度策略。

## 精读区
1. [FusionML: Prefill, Not Decode - Mechanism and Boundaries of CPU+GPU Co-Execution on Unified-Memory Apple Silicon](/202607/28/2607.22785v1-fusionml-prefill-not-decode---mechanism-and-boundaries-of-cpugpu-co-execution-on-unified-memory-apple-silicon) （9.0/10）
2. [Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch](/202607/28/2607.23099v1-decoding-the-skew-distribution-aware-moe-inference-with-adaptive-kernel-dispatch) （9.0/10）
3. [Gleam: Adaptive Network-Efficient CUDA API Remoting for Cross-Device GPU Sharing over LANs](/202607/28/2607.23115v1-gleam-adaptive-network-efficient-cuda-api-remoting-for-cross-device-gpu-sharing-over-lans) （9.0/10）
4. [Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool](/202607/28/2607.23250v1-libra-taming-attention-workload-skew-in-long-context-llm-training-with-bounded-sequence-pool) （9.0/10）
5. [Structured Redundancy Modeling for Efficient Visual Token Pruning in High-Resolution MLLMs](/202607/28/2607.23046v1-structured-redundancy-modeling-for-efficient-visual-token-pruning-in-high-resolution-mllms) （8.0/10）
6. [X-Stage: An Overlooked Pipeline Stage for Communication-Computation Overlap in DiT Inference](/202607/28/2607.23264v1-x-stage-an-overlooked-pipeline-stage-for-communication-computation-overlap-in-dit-inference) （8.0/10）

## 速读区
1. [Kalypso: Relational LLM Serving](/202607/28/2607.23815v1-kalypso-relational-llm-serving) （8.0/10）
2. [BettiSplit: Topology-Guided Privacy-Aware Split Learning Against Feature Inversion and Gradient Leakage](/202607/28/2607.24556v1-bettisplit-topology-guided-privacy-aware-split-learning-against-feature-inversion-and-gradient-leakage) （8.0/10）
3. [PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention](/202607/28/2607.24593v1-pivot-efficient-query-group-indexing-for-token-level-sparse-attention) （8.0/10）
4. [Distributed Convolutional Rank Regression over Decentralized Networks](/202607/28/2607.23639v1-distributed-convolutional-rank-regression-over-decentralized-networks) （7.0/10）
5. [Adaptive Data Admission and Retention for Streaming Federated Learning](/202607/28/2607.23987v1-adaptive-data-admission-and-retention-for-streaming-federated-learning) （7.0/10）
6. [OrchNAS: Orchestrated Neural Architecture Search Service for Personalised Federated Edge Intelligence](/202607/28/2607.22805v1-orchnas-orchestrated-neural-architecture-search-service-for-personalised-federated-edge-intelligence) （6.0/10）
7. [iFVS: Towards Instance-Optimized Filtered Vector Search](/202607/28/2607.22922v1-ifvs-towards-instance-optimized-filtered-vector-search) （6.0/10）

---
使用键盘方向键可在日报/论文之间快速切换。
