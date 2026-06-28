<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-28
- 运行时间：2026-06-28 21:30:58 UTC
- 运行状态：成功
- 本次总论文数：8
- 精读区：5
- 速读区：3

### 今日简报（AI）
今日聚焦AI系统效率：从训练集群的防崩溃妙招到MoE模型推理的异步加速。  
最值得看的是给万卡集群装上“共振安全阀”（预调度准则）和把MoE预填充拆细了异步跑的通路设计。  
下一步建议关注异构NPU上的稀疏计算与通信优化，它们正成为大模型落地的关键拼图。
- 详情：[/202606/28/README](/202606/28/README)

### 精读区论文标签
1. [A Pre-Dispatch Resonance Safety Criterion for AI Training Clusters](/202606/28/2606.22096v1-a-pre-dispatch-resonance-safety-criterion-for-ai-training-clusters)  
   标签：评分：9.0/10、query:mlsys
   evidence：推导出闭式预调度安全准则以避免AI训练集群中电网共振
2. [ASAP: A Disaggregated and Asynchronous Inference System for MoE Prefill](/202606/28/2606.22541v1-asap-a-disaggregated-and-asynchronous-inference-system-for-moe-prefill)  
   标签：评分：9.0/10、query:mlsys
   evidence：解耦异步推理系统消除 MoE 预填充服务中的同步停顿
3. [Subspace-Constrained Federated Learning with Low-Rank Adaptation](/202606/28/2606.22724v1-subspace-constrained-federated-learning-with-low-rank-adaptation)  
   标签：评分：9.0/10、query:mlsys
   evidence：联邦学习结合低秩适应解决客户端局部更新间的几何错位问题。
4. [Cache-Resident LLM Inference in GB-Scale Last-Level Caches](/202606/28/2606.25353v1-cache-resident-llm-inference-in-gb-scale-last-level-caches)  
   标签：评分：9.0/10、query:mlsys
   evidence：驻留缓存执行模型利用GB级末级缓存减少数据移动并提升LLM推理吞吐
5. [EGG: An Expert-Guided Agent Framework for Kernel Generation](/202606/28/2606.26758v1-egg-an-expert-guided-agent-framework-for-kernel-generation)  
   标签：评分：8.0/10、query:mlsys
   evidence：提出专家引导的LLM框架，自动生成面向大语言模型的高性能GPU内核

### 速读区论文标签
1. [NeutronSparse: Coordinating Heterogeneous Engines for Sparse Matrix Multiplication on NPUs](/202606/28/2606.22482v1-neutronsparse-coordinating-heterogeneous-engines-for-sparse-matrix-multiplication-on-npus)  
   标签：评分：7.0/10、query:mlsys
   evidence：协调NPU上稀疏矩阵乘法的异构引擎以提升AI加速器效率
2. [Quantization in Federated Learning: Methods, Challenges and Future Directions](/202606/28/2606.26822v1-quantization-in-federated-learning-methods-challenges-and-future-directions)  
   标签：评分：7.0/10、query:mlsys
   evidence：联邦学习量化综述提升分布式训练效率
3. [BitNet Text Embeddings](/202606/28/2606.25674v1-bitnet-text-embeddings)  
   标签：评分：6.0/10、query:mlsys
   evidence：极低位宽框架降低LLM嵌入推理成本和存储开销，用于大规模部署


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
