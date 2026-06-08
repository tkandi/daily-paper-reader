<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-08
- 运行时间：2026-06-08 20:54:58 UTC
- 运行状态：成功
- 本次总论文数：7
- 精读区：5
- 速读区：2

### 今日简报（AI）
今日精选「消除非可扩展开销让LLM推理真正走出阿姆达尔死胡同」与「MOSAIC动态调度多智能体」两篇高分文章，直击推理效率与智能体协同瓶颈。  
最值得跟进的结论是：通过剔除KV缓存、通信等不可扩展环节，推理吞吐可逼近线性扩展；而MOSAIC用自适应聚合与并发调度，将多智能体协作开销压到接近单次推理。  
想降本增效的读者，先别急着换硬件——这两项工作提供的系统层优化思路，比堆显卡更省钱。
- 详情：[/202606/08/README](/202606/08/README)

### 精读区论文标签
1. [Scaling LLM Inference Beyond Amdahl`s Limits via Eliminating Non-Scalable Overheads](/202606/08/2606.01927v1-scaling-llm-inference-beyond-amdahls-limits-via-eliminating-non-scalable-overheads)  
   标签：评分：9.0/10、query:mlsys
   evidence：Albireo并行推理系统通过重叠调度I/O与计算提高张量并行最优度
2. [MOSAIC: Efficient Mixture-of-Agent Scheduling via Adaptive Aggregation and Inference Concurrency](/202606/08/2606.03014v1-mosaic-efficient-mixture-of-agent-scheduling-via-adaptive-aggregation-and-inference-concurrency)  
   标签：评分：9.0/10、query:mlsys
   evidence：面向多智能体混合工作负载的GPU调度框架，减少空闲并提升吞吐
3. [Towards Serverless Semi-Decentralized Federated Learning with Heterogeneous Optimizers](/202606/08/2606.06687v1-towards-serverless-semi-decentralized-federated-learning-with-heterogeneous-optimizers)  
   标签：评分：9.0/10、query:mlsys
   evidence：提出无服务器半去中心化联邦学习用于集群构建，推动分布式训练框架发展。
4. [SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling](/202606/08/2606.06820v1-scale-scalable-cross-attention-learning-with-extrapolation-for-agentic-workflow-scheduling)  
   标签：评分：9.0/10、query:mlsys
   evidence：面向异构集群上大模型智能体工作流的深度强化学习调度器，能泛化到未见过的集群规模
5. [ANNS-AMP: Accelerating Approximate Nearest Neighbor Search via Adaptive Mixed-Precision Computing](/202606/08/2606.07156v1-anns-amp-accelerating-approximate-nearest-neighbor-search-via-adaptive-mixed-precision-computing)  
   标签：评分：8.0/10、query:mlsys
   evidence：为LLM和推荐系统中的关键操作近似最近邻搜索设计自适应混合精度框架与加速器

### 速读区论文标签
1. [LLM Compression with Jointly Optimizing Architectural and Quantization choices](/202606/08/2606.04063v1-llm-compression-with-jointly-optimizing-architectural-and-quantization-choices)  
   标签：评分：7.0/10、query:mlsys
   evidence：联合优化架构与混合精度量化以实现LLM的高效压缩和部署
2. [Skip a Layer or Loop It? Learning Program-of-Layers in LLMs](/202606/08/2606.06574v1-skip-a-layer-or-loop-it-learning-program-of-layers-in-llms)  
   标签：评分：6.0/10、query:mlsys
   evidence：用于高效推理的动态LLM层执行程序


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
