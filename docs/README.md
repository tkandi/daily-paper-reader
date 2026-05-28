<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-05-28
- 运行时间：2026-05-28 21:31:17 UTC
- 运行状态：成功
- 本次总论文数：5
- 精读区：3
- 速读区：2

### 今日简报（AI）
今日精读聚焦多模态大模型训练的异构并行新框架与变量异构消除方案，速读推式异步联邦学习偏差校正及GPU加速图构建。
最值得关注的方向：异构并行调度与 Entrain 方法分别从计算和变量同步层面解决分布式多模态训练的异构瓶颈。
建议读者结合这两项工作，进一步探索异构感知训练在跨模态大模型部署中的工程化实践。
- 详情：[/202605/28/README](/202605/28/README)

### 精读区论文标签
1. [Heterogeneous Parallelism for Multimodal Large Language Model Training](/202605/28/2605.27678v1-heterogeneous-parallelism-for-multimodal-large-language-model-training)  
   标签：评分：9.0/10、query:mlsys
   evidence：提出异构并行性，允许多模态LLM训练中不同模块使用独立布局，解决单一并行策略的局限。
2. [Addressing Variable Heterogeneity in Distributed Multimodal Training with Entrain](/202605/28/2605.27918v1-addressing-variable-heterogeneity-in-distributed-multimodal-training-with-entrain)  
   标签：评分：9.0/10、query:mlsys
   evidence：通过静态模型并行解决多模态分布式训练中负载异质性的框架
3. [How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving](/202605/28/2605.28302v1-how-far-can-disaggregation-go-a-design-space-exploration-of-attention-ffn-disaggregation-for-efficient-moe-llm-serving)  
   标签：评分：9.0/10、query:mlsys
   evidence：注意力-FFN解聚将MoE LLM服务调度到不同GPU组

### 速读区论文标签
1. [On the Push-Based Asynchronous Federated Learning: A Bias-Correction Aggregation Approach](/202605/28/2605.26162v1-on-the-push-based-asynchronous-federated-learning-a-bias-correction-aggregation-approach)  
   标签：评分：7.0/10、query:mlsys
   evidence：提出PushCen-ADFL，一种带偏差修正的通信高效异步联邦学习框架。
2. [SOLANET: Distributed Neighbor Graph Construction on GPU-Accelerated Systems](/202605/28/2605.27691v1-solanet-distributed-neighbor-graph-construction-on-gpu-accelerated-systems)  
   标签：评分：6.0/10、query:mlsys
   evidence：GPU加速的分布式邻域图构建工具包


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
