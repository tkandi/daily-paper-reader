<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-04-26
- 运行时间：2026-04-26 20:24:52 UTC
- 运行状态：成功
- 本次总论文数：17
- 精读区：6
- 速读区：11

### 今日简报（AI）
今日精选 17 篇前沿论文，深度聚焦 GPU 通信压缩与大规模分布式数据流水线的性能巅峰。
重点推荐 CCCL 架构实现的 GPU 内压缩通信技术，以及能显著提升大规模深度学习复现效率的高吞吐数据管道优化方案。
建议关注系统底层优化与算力能效比，通过 TLoRA 等轻量化技术平衡模型性能与资源消耗。
- 详情：[/202604/26/README](/202604/26/README)

### 精读区论文标签
1. [CCCL: In-GPU Compression-Coupled Collective Communication](/202604/26/2604.17172v1-cccl-in-gpu-compression-coupled-collective-communication)  
   标签：评分：10.0/10、query:mlsys
   evidence：针对LLM工作负载的GPU内压缩耦合集合通信库
2. [Optimizing High-Throughput Distributed Data Pipelines for Reproducible Deep Learning at Scale](/202604/26/2604.21275v1-optimizing-high-throughput-distributed-data-pipelines-for-reproducible-deep-learning-at-scale)  
   标签：评分：10.0/10、query:mlsys
   evidence：优化分布式GPU训练流水线和数据加载瓶颈
3. [Decoupled DiLoCo for Resilient Distributed Pre-training](/202604/26/2604.21428v1-decoupled-diloco-for-resilient-distributed-pre-training)  
   标签：评分：10.0/10、query:mlsys
   evidence：Decoupled DiLoCo 框架用于弹性分布式预训练和异步同步
4. [Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs](/202604/26/2604.18788v1-efficient-mixture-of-experts-llm-inference-with-apple-silicon-npus)  
   标签：评分：9.0/10、query:mlsys
   evidence：针对MoE推理的AI基础设施优化与NPU卸载
5. [Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional Communication Optimization](/202604/26/2604.21072v1-distributed-generative-inference-of-llm-at-internet-scales-with-multi-dimensional-communication-optimization)  
   标签：评分：9.0/10、query:mlsys
   evidence：具有多维通信优化的互联网规模分布式 LLM 推理框架
6. [Nesterov Accelerated Distributed Optimization with Efficient Quantized Communication](/202604/26/2604.16906v1-nesterov-accelerated-distributed-optimization-with-efficient-quantized-communication)  
   标签：评分：8.0/10、query:mlsys
   evidence：针对大规模系统的量化通信分布式优化算法

### 速读区论文标签
1. [TLoRA: Task-aware Low Rank Adaptation of Large Language Models](/202604/26/2604.18124v1-tlora-task-aware-low-rank-adaptation-of-large-language-models)  
   标签：评分：8.0/10、query:mlsys
   evidence：LLM微调资源分配的联合优化
2. [EnergAIzer: Fast and Accurate GPU Power Estimation Framework for AI Workloads](/202604/26/2604.20105v1-energaizer-fast-and-accurate-gpu-power-estimation-framework-for-ai-workloads)  
   标签：评分：8.0/10、query:mlsys
   evidence：专为数据中心AI工作负载设计的快速GPU功耗估算框架。
3. [Decentralized Machine Learning with Centralized Performance Guarantees via Gibbs Algorithms](/202604/26/2604.20492v1-decentralized-machine-learning-with-centralized-performance-guarantees-via-gibbs-algorithms)  
   标签：评分：8.0/10、query:mlsys
   evidence：具有通信协议的去中心化机器学习框架
4. [DiP-SD: Distributed Pipelined Speculative Decoding for Efficient LLM Inference at the Edge](/202604/26/2604.20919v1-dip-sd-distributed-pipelined-speculative-decoding-for-efficient-llm-inference-at-the-edge)  
   标签：评分：8.0/10、query:mlsys
   evidence：大语言模型推理的分布式流水线调度
5. [D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation](/202604/26/2604.16940v1-d-qrelo-training--and-data-free-delta-compression-for-large-language-models-via-quantization-and-residual-low-rank-approximation)  
   标签：评分：7.0/10、query:mlsys
   evidence：针对大语言模型微调的增量压缩技术，减少内存开销
6. [Joint Scheduling of Multi-Band Radar Sensing and DNN Inference for Cross-Stage Parallelism](/202604/26/2604.18520v1-joint-scheduling-of-multi-band-radar-sensing-and-dnn-inference-for-cross-stage-parallelism)  
   标签：评分：7.0/10、query:mlsys
   evidence：感知与DNN推理的联合调度，支持跨阶段并行和多核执行
7. [$R^2$-dLLM: Accelerating Diffusion Large Language Models via Spatio-Temporal Redundancy Reduction](/202604/26/2604.18995v1-r2-dllm-accelerating-diffusion-large-language-models-via-spatio-temporal-redundancy-reduction)  
   标签：评分：7.0/10、query:mlsys
   evidence：通过训练和推理中的时空冗余减少来加速dLLM
8. [Ocean: Fast Estimation-Based Sparse General Matrix-Matrix Multiplication on GPU](/202604/26/2604.19004v1-ocean-fast-estimation-based-sparse-general-matrix-matrix-multiplication-on-gpu)  
   标签：评分：7.0/10、query:mlsys
   evidence：针对机器学习工作负载的GPU内核优化
9. [SinkRouter: Sink-Aware Routing for Efficient Long-Context Decoding in Large Language and Multimodal Models](/202604/26/2604.16883v1-sinkrouter-sink-aware-routing-for-efficient-long-context-decoding-in-large-language-and-multimodal-models)  
   标签：评分：6.0/10、query:mlsys
   evidence：通过 Sink 感知路由实现的高效长文本解码系统
10. [Scalable Memristive-Friendly Reservoir Computing for Time Series Classification](/202604/26/2604.19343v1-scalable-memristive-friendly-reservoir-computing-for-time-series-classification)  
   标签：评分：6.0/10、query:mlsys
   evidence：深度学习应用中可扩展并行计算的架构设计
11. [Improved large-scale graph learning through ridge spectral sparsification](/202604/26/2604.20078v1-improved-large-scale-graph-learning-through-ridge-spectral-sparsification)  
   标签：评分：6.0/10、query:mlsys
   evidence：大规模图学习的分布式流式设置


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
