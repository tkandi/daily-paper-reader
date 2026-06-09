<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-09
- 运行时间：2026-06-09 21:23:50 UTC
- 运行状态：成功
- 本次总论文数：7
- 精读区：5
- 速读区：2

### 今日简报（AI）
今日精读两篇满分论文，聚焦打破异步流水线并行的“气泡”与资源感知的计算通信重叠，速读则跟踪了极低比特量化和智能批次选择。
最值得关注：通过约束权重不一致性实现无阻塞的异步流水线，以及根据资源动态调度通信与计算重叠，可大幅提升多GPU训练效率。
下次实践建议：若你正为大模型训练的速度瓶颈发愁，务必关注有界不一致性流水线与通信重叠的合体方案，它们或许就是下一波提效的关键。
- 详情：[/202606/09/README](/202606/09/README)

### 精读区论文标签
1. [Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency](/202606/09/2606.07881v1-breaking-the-bubble-asynchronous-pipeline-parallel-training-with-bounded-weight-inconsistency)  
   标签：评分：10.0/10、query:mlsys
   evidence：提出PACI，一种无气泡的异步流水线并行方法，可控制权重不一致
2. [Resource-aware Computation-Communication Overlap for multi-GPU ML Workloads](/202606/09/2606.09200v1-resource-aware-computation-communication-overlap-for-multi-gpu-ml-workloads)  
   标签：评分：10.0/10、query:mlsys
   evidence：通过共享内存占用塑形和提升通信优先级实现资源感知的计算-通信重叠，直接优化GPU资源调度与管理
3. [FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training](/202606/09/2606.08476v1-flashcp-load-balanced-communication-efficient-context-parallelism-for-llm-training)  
   标签：评分：9.0/10、query:mlsys
   evidence：用于大规模长上下文LLM训练的负载均衡与通信高效上下文并行框架
4. [Semantic Quorum Assurance: Collective Certification for Non-Deterministic AI Infrastructure](/202606/09/2606.08021v1-semantic-quorum-assurance-collective-certification-for-non-deterministic-ai-infrastructure)  
   标签：评分：8.0/10、query:mlsys
   evidence：引入语义仲裁保证，一种新型控制平面，用于安全可靠的非确定性AI基础设施操作，扩展了经典共识以进行意图安全性认证。
5. [AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments](/202606/09/2606.08197v1-alignfed-alignment-aware-asynchronous-federated-fine-tuning-for-large-language-models-in-heterogeneous-edge-environments)  
   标签：评分：8.0/10、query:mlsys
   evidence：面向大语言模型的异步联邦微调框架，解决边缘环境中的掉队与异构问题

### 速读区论文标签
1. [Minimizing the Hidden Cost of Scales: Graph-Guided Ultra-Low-Bit Quantization for Large Language Models](/202606/09/2606.05429v1-minimizing-the-hidden-cost-of-scales-graph-guided-ultra-low-bit-quantization-for-large-language-models)  
   标签：评分：7.0/10、query:mlsys
   evidence：针对大语言模型的超低位量化框架减少隐藏扩展代价，提升部署效率
2. [Minibatch Selection via Partition Matroid Constrained Gradient Matching](/202606/09/2606.07954v1-minibatch-selection-via-partition-matroid-constrained-gradient-matching)  
   标签：评分：7.0/10、query:mlsys
   evidence：提出PartitionSel小批量选择方法，通过划分拟阵约束梯度匹配优化大规模模型训练中的数据利用。


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
