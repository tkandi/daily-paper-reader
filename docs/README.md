<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-23
- 运行时间：2026-06-23 22:19:57 UTC
- 运行状态：成功
- 本次总论文数：8
- 精读区：6
- 速读区：2

### 今日简报（AI）
今日深度解读大模型效率，精读Transformer微调能耗屋顶线模型与CTR推理双层并行框架。最值关注：微调能耗可精准建模，稀疏注意力即插即用降低长上下文成本。建议将能耗评估纳入模型选型，并尝试稀疏路由在实际长文本任务中的效果。
- 详情：[/202606/23/README](/202606/23/README)

### 精读区论文标签
1. [The Energy Consumption of Transformer Fine-Tuning: A Roofline-Inspired Scaling Model](/202606/23/2606.23546v1-the-energy-consumption-of-transformer-fine-tuning-a-roofline-inspired-scaling-model)  
   标签：评分：10.0/10、query:mlsys
   evidence：开发了受屋顶线启发的缩放模型，预测多GPU Transformer训练的能耗，捕捉张量并行和数据并行效应。
2. [DPIFrame: A Dual-Level Parallelism Acceleration Framework for CTR Model Inference](/202606/23/2606.21101v1-dpiframe-a-dual-level-parallelism-acceleration-framework-for-ctr-model-inference)  
   标签：评分：9.0/10、query:mlsys
   evidence：首个双层并行框架，用于在GPU上加速CTR模型推理，具备模块内和模块间并行及高效多表查找。
3. [SwarmX: Agentic Scheduling for Low-Latency Agentic Systems](/202606/23/2606.21401v1-swarmx-agentic-scheduling-for-low-latency-agentic-systems)  
   标签：评分：9.0/10、query:mlsys
   evidence：使用神经预测器的GPU-CPU集群智能体调度系统
4. [Breaking chains with trees: Deep learning with $\mathcal{O}(\log N)$ parallel time complexity](/202606/23/2606.21497v1-breaking-chains-with-trees-deep-learning-with-mathcalolog-n-parallel-time-complexity)  
   标签：评分：9.0/10、query:mlsys
   evidence：提出分层块局部学习，实现并行深度学习的对数时间复杂度
5. [Recency/Frequency Adaptive KV Caching for Large Language Model Serving](/202606/23/2606.21238v1-recencyfrequency-adaptive-kv-caching-for-large-language-model-serving)  
   标签：评分：8.0/10、query:mlsys
   evidence：自适应的KV缓存管理提升LLM推理服务缓存命中率与延迟
6. [FlowTrain: Flow-Based Decoupled Training for Industrial-Grade Vision-Language Models](/202606/23/2606.23087v1-flowtrain-flow-based-decoupled-training-for-industrial-grade-vision-language-models)  
   标签：评分：8.0/10、query:mlsys
   evidence：提出基于流的解耦训练框架，将VLM训练重构为统一内存池上的生产者-消费者数据流。

### 速读区论文标签
1. [Federated learning with heavy-tailed gradient noise and communication noise: a variance-reduction based algorithm](/202606/23/2606.22466v1-federated-learning-with-heavy-tailed-gradient-noise-and-communication-noise-a-variance-reduction-based-algorithm)  
   标签：评分：7.0/10、query:mlsys
   evidence：提出用于联邦学习的方差缩减算法以处理重尾噪声
2. [SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers](/202606/23/2606.22874v1-spotattention-plug-in-block-sparse-routing-for-pretrained-long-context-transformers)  
   标签：评分：7.0/10、query:mlsys
   evidence：轻量级选择器附加在冻结的预训练Transformer上，估计注意力并挑选top-K键，降低二次预填充和缓存成本。


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
