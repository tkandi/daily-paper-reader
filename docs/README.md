<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-04-23
- 运行时间：2026-04-23 20:40:22 UTC
- 运行状态：成功
- 本次总论文数：17
- 精读区：6
- 速读区：11

### 今日简报（AI）
今日深度解析 17 篇前沿论文，聚焦 GPU 通信无损压缩与云原生分布式大模型架构。
重点关注 UCCL-Zip 对 GPU 通信的性能飞跃，以及 MoE 模型在计算效率边界上的“向上回收”式突破。
建议优先研读云原生分布式系统研究议程，为构建高效可扩展的 AI 基础设施提供顶层设计参考。
- 详情：[/202604/23/README](/202604/23/README)

### 精读区论文标签
1. [UCCL-Zip: Lossless Compression Supercharged GPU Communication](/202604/23/2604.17172v2-uccl-zip-lossless-compression-supercharged-gpu-communication)  
   标签：评分：9.0/10、query:mlsys
   evidence：LLM基础设施中GPU通信的无损压缩技术
2. [Cloud-native and Distributed Systems for Efficient and Scalable Large Language Models -- A Research Agenda](/202604/23/2604.17227v1-cloud-native-and-distributed-systems-for-efficient-and-scalable-large-language-models----a-research-agenda)  
   标签：评分：9.0/10、query:mlsys
   evidence：探讨了用于LLM扩展和资源优化的云原生和分布式架构
3. [ReaLB: Real-Time Load Balancing for Multimodal MoE Inference](/202604/23/2604.19503v2-realb-real-time-load-balancing-for-multimodal-moe-inference)  
   标签：评分：9.0/10、query:mlsys
   evidence：专家并行下多模态 MoE 推理的实时负载均衡
4. [Stream-CQSA: Avoiding Out-of-Memory in Attention Computation via Flexible Workload Scheduling](/202604/23/2604.20819v1-stream-cqsa-avoiding-out-of-memory-in-attention-computation-via-flexible-workload-scheduling)  
   标签：评分：9.0/10、query:mlsys
   evidence：内存自适应调度框架，避免长上下文LLM注意力计算中的内存溢出
5. [MoE-nD: Per-Layer Mixture-of-Experts Routing for Multi-Axis KV Cache Compression](/202604/23/2604.17695v1-moe-nd-per-layer-mixture-of-experts-routing-for-multi-axis-kv-cache-compression)  
   标签：评分：8.0/10、query:mlsys
   evidence：使用MoE路由优化长上下文LLM推理的KV缓存内存
6. [Design Rules for Extreme-Edge Scientific Computing on AI Engines](/202604/23/2604.19106v1-design-rules-for-extreme-edge-scientific-computing-on-ai-engines)  
   标签：评分：8.0/10、query:mlsys
   evidence：FPGA SoC上AI引擎的设计规则

### 速读区论文标签
1. [Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts](/202604/23/2604.19835v1-expert-upcycling-shifting-the-compute-efficient-frontier-of-mixture-of-experts)  
   标签：评分：8.0/10、query:mlsys
   evidence：提出了专家上行转换方法，在预训练期间扩展MoE容量并管理通信成本
2. [Temporally Extended Mixture-of-Experts Models](/202604/23/2604.20156v1-temporally-extended-mixture-of-experts-models)  
   标签：评分：8.0/10、query:mlsys
   evidence：优化MoE专家切换以减少GPU显存抖动
3. [Federated Parameter-Efficient Adaptation for Interference Mitigation at the Wireless Edge](/202604/23/2604.15936v1-federated-parameter-efficient-adaptation-for-interference-mitigation-at-the-wireless-edge)  
   标签：评分：7.0/10、query:mlsys
   evidence：针对分布式基站的联邦学习与参数高效微调
4. [Active Inference-Based Adaptive Routing for Heterogeneous Edge AI Services](/202604/23/2604.17373v1-active-inference-based-adaptive-routing-for-heterogeneous-edge-ai-services)  
   标签：评分：7.0/10、query:mlsys
   evidence：跨云边基础设施的AI服务编排与资源利用
5. [LiteResearcher: A Scalable Agentic RL Training Framework for Deep Research Agent](/202604/23/2604.17931v2-literesearcher-a-scalable-agentic-rl-training-framework-for-deep-research-agent)  
   标签：评分：7.0/10、query:mlsys
   evidence：使用虚拟环境的基于LLM智能体的可扩展强化学习训练框架
6. [AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization](/202604/23/2604.18137v1-aqpim-breaking-the-pim-capacity-wall-for-llms-with-in-memory-activation-quantization)  
   标签：评分：7.0/10、query:mlsys
   evidence：针对大模型内存瓶颈的存内计算架构优化
7. [DASH-KV: Accelerating Long-Context LLM Inference via Asymmetric KV Cache Hashing](/202604/23/2604.19351v2-dash-kv-accelerating-long-context-llm-inference-via-asymmetric-kv-cache-hashing)  
   标签：评分：7.0/10、query:mlsys
   evidence：通过 KV 缓存哈希加速长文本 LLM 推理的框架
8. [Optimal Routing for Federated Learning over Dynamic Satellite Networks: Tractable or Not?](/202604/23/2604.19399v1-optimal-routing-for-federated-learning-over-dynamic-satellite-networks-tractable-or-not)  
   标签：评分：7.0/10、query:mlsys
   evidence：动态网络环境下分布式模型学习的路由优化
9. [LiteResearcher: A Scalable Agentic RL Training Framework for Deep Research Agent](/202604/23/2604.17931v1-literesearcher-a-scalable-agentic-rl-training-framework-for-deep-research-agent)  
   标签：评分：6.0/10、query:mlsys
   evidence：用于智能体强化学习的可扩展训练框架
10. [Architecture Matters More Than Scale: A Comparative Study of Retrieval and Memory Augmentation for Financial QA Under SME Compute Constraints](/202604/23/2604.17979v1-architecture-matters-more-than-scale-a-comparative-study-of-retrieval-and-memory-augmentation-for-financial-qa-under-sme-compute-constraints)  
   标签：评分：6.0/10、query:mlsys
   evidence：大模型推理的AI基础设施约束与架构效率
11. [ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning](/202604/23/2604.19254v1-shadowpeft-shadow-network-for-parameter-efficient-fine-tuning)  
   标签：评分：6.0/10、query:mlsys
   evidence：提出了一种带有深度共享影子模块的集中式参数高效微调框架


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
