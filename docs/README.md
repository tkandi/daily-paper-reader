<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-05-14
- 运行时间：2026-05-14 21:34:01 UTC
- 运行状态：成功
- 本次总论文数：19
- 精读区：8
- 速读区：11

### 今日简报（AI）
今日聚焦大模型训练的容错与效率优化，深度解析 ResiHP 与 ReCoVer 等满分系统架构。
核心结论指出动态混合并行与 CPU-GPU 协同显存交换是解决训练中断及长文本推理瓶颈的关键。
建议开发者重点关注分布式系统中的故障恢复机制，以提升超大规模模型生产的稳定性。
- 详情：[/202605/14/README](/202605/14/README)

### 精读区论文标签
1. [ResiHP: Taming LLM Training Failures with Dynamic Hybrid Parallelism](/202605/14/2605.06374v2-resihp-taming-llm-training-failures-with-dynamic-hybrid-parallelism)  
   标签：评分：10.0/10、query:mlsys
   evidence：大规模LLM训练中混合并行的容错系统
2. [ReCoVer: Resilient LLM Pre-Training System via Fault-Tolerant Collective and Versatile Workload](/202605/14/2605.11215v1-recover-resilient-llm-pre-training-system-via-fault-tolerant-collective-and-versatile-workload)  
   标签：评分：10.0/10、query:mlsys
   evidence：针对大规模GPU集群的弹性LLM预训练系统
3. [ChunkFlow: Communication-Aware Chunked Prefetching for Layerwise Offloading in Distributed Diffusion Transformer Inference](/202605/14/2605.11335v1-chunkflow-communication-aware-chunked-prefetching-for-layerwise-offloading-in-distributed-diffusion-transformer-inference)  
   标签：评分：9.5/10、query:mlsys
   evidence：分布式推理中预取与通信的协同调度
4. [Unleashing Scalable Context Parallelism for Foundation Models Pre-Training via FCP](/202605/14/2605.08524v1-unleashing-scalable-context-parallelism-for-foundation-models-pre-training-via-fcp)  
   标签：评分：9.0/10、query:mlsys
   evidence：基础模型预训练的可扩展上下文并行
5. [Training-Inference Consistent Segmented Execution for Long-Context LLMs](/202605/14/2605.11744v1-training-inference-consistent-segmented-execution-for-long-context-llms)  
   标签：评分：9.0/10、query:mlsys
   evidence：长文本大模型的分段执行框架
6. [D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models](/202605/14/2605.13276v1-d-vla-a-high-concurrency-distributed-asynchronous-reinforcement-learning-framework-for-vision-language-action-models)  
   标签：评分：9.0/10、query:mlsys
   evidence：分布式异步强化学习框架
7. [TurboGR: An Accelerated Training System for Large-Scale Generative Recommendation](/202605/14/2605.13433v1-turbogr-an-accelerated-training-system-for-large-scale-generative-recommendation)  
   标签：评分：9.0/10、query:mlsys
   evidence：针对NPU的大规模生成式推荐加速训练系统
8. [Rescaled Asynchronous SGD: Optimal Distributed Optimization under Data and System Heterogeneity](/202605/14/2605.13434v1-rescaled-asynchronous-sgd-optimal-distributed-optimization-under-data-and-system-heterogeneity)  
   标签：评分：9.0/10、query:mlsys
   evidence：系统异构下分布式优化的异步SGD算法

### 速读区论文标签
1. [An Efficient Hybrid Sparse Attention with CPU-GPU Parallelism for Long-Context Inference](/202605/14/2605.07719v1-an-efficient-hybrid-sparse-attention-with-cpu-gpu-parallelism-for-long-context-inference)  
   标签：评分：8.5/10、query:mlsys
   evidence：针对长上下文推理的CPU-GPU并行与跨设备协同执行
2. [OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models](/202605/14/2605.11678v1-oom-free-alpamayo-via-cpu-gpu-memory-swapping-for-vision-language-action-models)  
   标签：评分：8.5/10、query:mlsys
   evidence：通过CPU-GPU内存交换实现显存高效VLA推理的系统级优化
3. [Distributed Seeking for Fixed Points of Biased Stochastic Operators: A Communication Efficient Approach](/202605/14/2605.07633v1-distributed-seeking-for-fixed-points-of-biased-stochastic-operators-a-communication-efficient-approach)  
   标签：评分：8.0/10、query:mlsys
   evidence：具有压缩功能的通信高效分布式算法
4. [SlimQwen: Exploring the Pruning and Distillation in Large MoE Model Pre-training](/202605/14/2605.08738v1-slimqwen-exploring-the-pruning-and-distillation-in-large-moe-model-pre-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：预训练规模下MoE压缩与剪枝的系统研究
5. [Rethinking Local Learning: A Cheaper and Faster Recipe for LLM Post-Training](/202605/14/2605.04913v3-rethinking-local-learning-a-cheaper-and-faster-recipe-for-llm-post-training)  
   标签：评分：7.5/10、query:mlsys
   evidence：局部学习后训练策略，减少反向耦合和激活存储
6. [Beyond Factor Aggregation: Gauge-Aware Low-Rank Server Representations for Federated LoRA](/202605/14/2605.06733v1-beyond-factor-aggregation-gauge-aware-low-rank-server-representations-for-federated-lora)  
   标签：评分：7.5/10、query:mlsys
   evidence：针对去中心化数据和有限客户端资源的联邦LoRA聚合规则
7. [Toward Communication-Efficient Space Data Centers: Bottlenecks, Architectures, and New Paradigms](/202605/14/2605.12681v1-toward-communication-efficient-space-data-centers-bottlenecks-architectures-and-new-paradigms)  
   标签：评分：7.5/10、query:mlsys
   evidence：天基AI计算基础设施的架构与范式
8. [GeoStack: A Framework for Quasi-Abelian Knowledge Composition in VLMs](/202605/14/2605.06477v1-geostack-a-framework-for-quasi-abelian-knowledge-composition-in-vlms)  
   标签：评分：7.0/10、query:mlsys
   evidence：视觉语言模型知识组合的模块化框架
9. [Enhancing Federated Quadruplet Learning: Stochastic Client Selection and Embedding Stability Analysis](/202605/14/2605.07888v1-enhancing-federated-quadruplet-learning-stochastic-client-selection-and-embedding-stability-analysis)  
   标签：评分：6.5/10、query:mlsys
   evidence：分布式客户端之间的联邦学习
10. [DataMaster: Data-Centric Autonomous AI Research](/202605/14/2605.10906v2-datamaster-data-centric-autonomous-ai-research)  
   标签：评分：6.5/10、query:mlsys
   evidence：通过自主数据工程改进机器学习系统
11. [Stabilizing LLM Supervised Fine-Tuning via Explicit Distributional Control](/202605/14/2605.04468v1-stabilizing-llm-supervised-fine-tuning-via-explicit-distributional-control)  
   标签：评分：6.0/10、query:mlsys
   evidence：稳定LLM有监督微调的框架


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
