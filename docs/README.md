<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-07-15
- 运行时间：2026-07-15 21:36:20 UTC
- 运行状态：成功
- 本次总论文数：4
- 精读区：4
- 速读区：0

### 今日简报（AI）
今日精读双9分论文，聚焦稀疏注意力在长上下文与硬件推理上的极致优化。  
最值得关注方向：利用高维特性设计融合索引-TopK算子，以及通过搜索-内核协同实现可落地的N:M稀疏推理。  
建议读者可结合具体GPU架构，追踪这些稀疏模式在生成式模型中的实测加速效果。
- 详情：[/202607/15/README](/202607/15/README)

### 精读区论文标签
1. [LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention](/202607/15/2607.11976v1-litetopk-exploiting-the-curse-of-dimensionality-for-a-fused-indexer-topk-kernel-in-long-context-sparse-attention)  
   标签：评分：9.0/10、query:mlsys
   evidence：提出高效的 GPU 融合 Indexer-TopK 核，用于大语言模型的稀疏注意力，减少内存流量和同步开销
2. [Realizable N:M Sparse Transformer Inference via Search-Kernel Co-Design](/202607/15/2607.12505v1-realizable-nm-sparse-transformer-inference-via-search-kernel-co-design)  
   标签：评分：9.0/10、query:mlsys
   evidence：协同设计稀疏 CUDA 核和稀疏配置，实现 ViT 在 GPU 上的高效推理，获得实际加速
3. [Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices](/202607/15/2607.10183v2-automated-tensor-scheduling-for-hybrid-cpu-gpu-llm-inference-on-consumer-devices)  
   标签：评分：8.0/10、query:mlsys
   evidence：面向消费级设备的混合CPU-GPU张量级推理卸载
4. [WSqD: A Horizon-Free Learning Rate Schedule for Large Model Training](/202607/15/2607.10959v1-wsqd-a-horizon-free-learning-rate-schedule-for-large-model-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：提出无训练时长依赖的学习率调度方案，优化大模型训练

### 速读区论文标签
- 本次无速读推荐。


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
