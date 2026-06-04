<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-04
- 运行时间：2026-06-04 20:50:33 UTC
- 运行状态：成功
- 本次总论文数：8
- 精读区：6
- 速读区：2

### 今日简报（AI）
今日拆解8篇前沿论文，重点深挖流水线并行理论与临床AI能效调度两大突破。  
最值得关注：PipeDream流水线并行首次建立系统性理论框架，Night-Window批处理则证明错峰调度可将GPU碳排降低40%而不损伤模型性能。  
建议开发者从SIGMA流式图划分入手，体验分布式图训练的新平衡范式，同时警惕分布式训练可能带来的算力治理风险。
- 详情：[/202606/04/README](/202606/04/README)

### 精读区论文标签
1. [Demystifying Pipeline Parallelism: First Theory for PipeDream](/202606/04/2606.03498v1-demystifying-pipeline-parallelism-first-theory-for-pipedream)  
   标签：评分：10.0/10、query:mlsys
   evidence：首次为PipeDream流水线并行提供理论收敛保证
2. [Night-Window Batching versus Carbon-Aware Scheduling for Clinical AI GPU Workloads](/202606/04/2606.01766v1-night-window-batching-versus-carbon-aware-scheduling-for-clinical-ai-gpu-workloads)  
   标签：评分：9.0/10、query:mlsys
   evidence：比较13种GPU调度规则用于临床AI工作负载，包含碳感知和夜间批处理，直接针对资源调度目标。
3. [DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference](/202606/04/2606.02982v1-driftsched-adaptive-qos-aware-scheduling-under-runtime-token-drift-for-multi-tenant-gpu-inference)  
   标签：评分：9.0/10、query:mlsys
   evidence：面向LLM推理服务的自适应QoS感知GPU调度
4. [CXL-ClusterSim: Modeling CXL-based Disaggregated Memory Cluster for Pooling and Sharing using gem5 and SST](/202606/04/2605.27745v1-cxl-clustersim-modeling-cxl-based-disaggregated-memory-cluster-for-pooling-and-sharing-using-gem5-and-sst)  
   标签：评分：8.0/10、query:mlsys
   evidence：用于设计基于CXL内存解耦的AI基础设施的仿真工具
5. [GreenGNN: Energy-Aware Windowed Communication Optimization for Distributed GNN Training](/202606/04/2606.02916v1-greengnn-energy-aware-windowed-communication-optimization-for-distributed-gnn-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：GreenGNN通过窗口化训练并利用邻居采样的时间局部性来降低通信能耗。
6. [Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving](/202606/04/2606.02964v1-multi-segment-attention-enabling-efficient-kv-cache-management-for-faster-large-language-model-serving)  
   标签：评分：8.0/10、query:mlsys
   evidence：面向LLM服务的计算延迟感知KV缓存管理

### 速读区论文标签
1. [SIGMA: A Versatile Streaming Graph Partitioner for Vertex- and Edge-Balanced Distributed GNN Training](/202606/04/2606.03519v1-sigma-a-versatile-streaming-graph-partitioner-for-vertex--and-edge-balanced-distributed-gnn-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：SIGMA是支持顶点和边划分的多目标流式图划分器，用于分布式GNN训练优化。
2. [Does Distributed Training Undermine Compute Governance?](/202606/04/2605.29359v1-does-distributed-training-undermine-compute-governance)  
   标签：评分：7.0/10、query:mlsys
   evidence：分析分布式训练算法如何通过聚合硬件规避算力治理，与分布式训练框架直接相关


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
