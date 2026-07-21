<div class="dpr-home-notice-card dpr-home-panel">
  <div class="dpr-home-notice-header dpr-home-panel-header">
    <h3 class="dpr-home-notice-title">公告与更新</h3>
    <a class="dpr-home-notice-tutorial" href="#/tutorial/README">使用教程 <span aria-hidden="true">›</span></a>
  </div>
  <div class="dpr-home-notice-entry">
    <time class="dpr-home-notice-date" datetime="2026-07-19">07.19</time>
    <div>
      <strong class="dpr-home-notice-entry-title">首页新增社区统计</strong>
      <span class="dpr-home-notice-entry-summary">现在可以看到今天看论文的人数和项目加入人数。</span>
    </div>
  </div>
  <div class="dpr-home-site-stats" data-dpr-site-stats hidden aria-live="polite">
    <span>今天有 <strong class="dpr-home-site-stat-value" data-dpr-daily-readers>--</strong> 人在看论文</span>
    <span class="dpr-home-site-stat-separator" aria-hidden="true">·</span>
    <span>已有 <strong class="dpr-home-site-stat-value" data-dpr-fork-count>--</strong> 人加入 Daily Paper Reader</span>
  </div>
</div>

## 每次日报
- 最新运行日期：2026-07-21
- 运行时间：2026-07-21 20:32:26 UTC
- 运行状态：成功
- 本次总论文数：11
- 精读区：6
- 速读区：5

### 今日简报（AI）
今日聚焦大模型推理优化，精读了两篇顶会高分论文，分别应对输出长度不确定下的KV缓存管理，以及千亿参数模型的会话感知无服务器化部署。  
最值得关注的方向是：如何精准处理缓存不确定性以降低成本，以及无服务器架构下巨型模型的弹性伸缩。  
下一步可探索将边缘端的分层协作推理方案落地，或在微调中尝试自编码器压缩的并行分割学习。
- 详情：[/202607/21/README](/202607/21/README)

### 精读区论文标签
1. [Robust KV Cache Management for LLM Serving under Output Token Length Uncertainty](/202607/21/2607.16892v1-robust-kv-cache-management-for-llm-serving-under-output-token-length-uncertainty)  
   标签：评分：9.0/10、query:mlsys
   evidence：在GPU集群上联合优化LLM服务的GPU并行配置、KV缓存预留和请求路由
2. [Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs](/202607/21/2607.17181v1-talaria-session-aware-serverless-serving-of-hundred-billion-parameter-llms)  
   标签：评分：9.0/10、query:mlsys
   evidence：在共享GPU池上实现千亿参数LLM的会话感知无服务器推理
3. [Harness Engineering for LLM-Driven GPU Kernel Generation](/202607/21/2607.17979v1-harness-engineering-for-llm-driven-gpu-kernel-generation)  
   标签：评分：9.0/10、query:mlsys
   evidence：提出以harness为中心的系统，用于LLM驱动的GPU内核优化，包含编译、正确性检查、性能分析和存档功能
4. [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](/202607/21/2607.18002v1-expertplex-a-high-goodput-disaggregated-serving-system-for-moe-llms-with-adaptive-persistent-kernels)  
   标签：评分：9.0/10、query:mlsys
   evidence：面向MoE大语言模型的解耦式推理系统，通过自适应持久内核优化GPU资源分配和阶段共置
5. [Sobek: Streaming Equivariant Tensor Product Convolutions](/202607/21/2607.18074v1-sobek-streaming-equivariant-tensor-product-convolutions)  
   标签：评分：9.0/10、query:mlsys
   evidence：等变卷积的流式GPU高效实现，减少内存传输
6. [Technical Report: AI-Assisted Gated DeltaNet Optimization on NVIDIA Blackwell](/202607/21/2607.16831v1-technical-report-ai-assisted-gated-deltanet-optimization-on-nvidia-blackwell)  
   标签：评分：8.0/10、query:mlsys
   evidence：利用AI辅助GPU内核优化在Blackwell上的ML推理

### 速读区论文标签
1. [EdgeCoInfer: Hierarchical Collaborative Inference for On-Device Multimodal Large Models](/202607/21/2607.17143v1-edgecoinfer-hierarchical-collaborative-inference-for-on-device-multimodal-large-models)  
   标签：评分：8.0/10、query:mlsys
   evidence：针对边缘多模态大模型，协同优化模型间共享与模型内细粒度划分的分层协同推理框架。
2. [LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters](/202607/21/2607.17175v1-lmedge-qos-aware-llm-inference-orchestration-on-edge-clusters)  
   标签：评分：8.0/10、query:mlsys
   evidence：在边缘集群上对LLM推理进行QoS感知编排，联合管理模型配置与执行位置以满足资源约束。
3. [AutoEncoder-Compressed Parallel Split Learning for Pre-trained Model Fine-Tuning](/202607/21/2607.17913v1-autoencoder-compressed-parallel-split-learning-for-pre-trained-model-fine-tuning)  
   标签：评分：8.0/10、query:mlsys
   evidence：分布式微调中的通信压缩，并行拆分学习
4. [Enabling Spatially Fine-Grained DVFS in Neural Processing Units for Energy-Efficient LLM Serving](/202607/21/2607.16473v1-enabling-spatially-fine-grained-dvfs-in-neural-processing-units-for-energy-efficient-llm-serving)  
   标签：评分：7.0/10、query:mlsys
   evidence：实现NPU组件级动态电压频率调节，优化大语言模型服务能效
5. [LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion Large Language Models](/202607/21/2607.16339v1-lacache-exact-caching-and-precision-adaptive-inference-for-diffusion-large-language-models)  
   标签：评分：6.0/10、query:mlsys
   evidence：通过缓存中间结果加速扩散大语言模型推理


<div class="dpr-home-promo-card dpr-home-panel">
  <div class="dpr-home-panel-header">
    <h3 class="dpr-home-promo-title">社区与支持</h3>
  </div>
  <p class="dpr-home-promo-copy">欢迎通过 Star、Fork、Issue 或 PR 一起完善 Daily Paper Reader。</p>
  <div class="dpr-home-promo-meta">
    <span>QQ群 <strong>583867967</strong></span>
    <span class="dpr-home-promo-separator" aria-hidden="true">·</span>
    <span>已有 <strong>1,491</strong> 人参与交流</span>
  </div>
</div>
