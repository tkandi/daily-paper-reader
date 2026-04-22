<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-04-22
- 运行时间：2026-04-22 20:29:36 UTC
- 运行状态：成功
- 本次总论文数：18
- 精读区：7
- 速读区：11

### 今日简报（AI）
聚焦分布式训练效能，今日深度解析 18 篇论文，重点突破 MoE 负载均衡与动态算子编译技术。
满分作 FEPLB 巧妙利用拷贝引擎实现 MoE 零成本调优，Event Tensor 则为复杂动态算子编译提供了高效统一框架。
建议开发者深入探索分布式优化与联邦 RLHF 领域，以应对超大规模模型的高效迭代需求。
- 详情：[/202604/22/README](/202604/22/README)

### 精读区论文标签
1. [FEPLB: Exploiting Copy Engines for Nearly Free MoE Load Balancing in Distributed Training](/202604/22/2604.19654v1-feplb-exploiting-copy-engines-for-nearly-free-moe-load-balancing-in-distributed-training)  
   标签：评分：10.0/10、query:mlsys
   evidence：利用GPU复制引擎进行分布式训练中的MoE负载均衡
2. [Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel](/202604/22/2604.13327v2-event-tensor-a-unified-abstraction-for-compiling-dynamic-megakernel)  
   标签：评分：9.0/10、query:mlsys
   evidence：LLM推理中动态GPU大内核的统一编译器抽象
3. [CoCoDiff: Optimizing Collective Communications for Distributed Diffusion Transformer Inference Under Ulysses Sequence Parallelism](/202604/22/2604.14561v2-cocodiff-optimizing-collective-communications-for-distributed-diffusion-transformer-inference-under-ulysses-sequence-parallelism)  
   标签：评分：9.0/10、query:mlsys
   evidence：优化序列并行下的集合通信
4. [A Stackelberg Game Framework with Drainability Guardrails for Pricing and Scaling in Multi-Tenant GPU Cloud Platforms](/202604/22/2604.16802v1-a-stackelberg-game-framework-with-drainability-guardrails-for-pricing-and-scaling-in-multi-tenant-gpu-cloud-platforms)  
   标签：评分：9.0/10、query:mlsys
   evidence：多租户GPU云平台中的定价与扩缩容
5. [ARGUS: Agentic GPU Optimization Guided by Data-Flow Invariants](/202604/22/2604.18616v1-argus-agentic-gpu-optimization-guided-by-data-flow-invariants)  
   标签：评分：9.0/10、query:mlsys
   evidence：用于GPU算子优化和指令调度的智能体框架
6. [UniEP: Unified Expert-Parallel MoE MegaKernel for LLM Training](/202604/22/2604.19241v1-uniep-unified-expert-parallel-moe-megakernel-for-llm-training)  
   标签：评分：9.0/10、query:mlsys
   evidence：用于扩展MoE模型训练的统一专家并行MegaKernel
7. [ReaLB: Real-Time Load Balancing for Multimodal MoE Inference](/202604/22/2604.19503v1-realb-real-time-load-balancing-for-multimodal-moe-inference)  
   标签：评分：9.0/10、query:mlsys
   evidence：MoE推理中专家并行性的实时负载均衡

### 速读区论文标签
1. [Distributed Nesterov Flows for Multi-agent Optimization](/202604/22/2604.17311v1-distributed-nesterov-flows-for-multi-agent-optimization)  
   标签：评分：8.0/10、query:mlsys
   evidence：分布式梯度下降与多智能体优化
2. [Efficient Federated RLHF via Zeroth-Order Policy Optimization](/202604/22/2604.17747v1-efficient-federated-rlhf-via-zeroth-order-policy-optimization)  
   标签：评分：8.0/10、query:mlsys
   evidence：低通信和内存复杂度的分布式联邦RLHF算法
3. [Accelerating Optimization and Machine Learning through Decentralization](/202604/22/2604.19518v1-accelerating-optimization-and-machine-learning-through-decentralization)  
   标签：评分：8.0/10、query:mlsys
   evidence：机器学习的去中心化优化
4. [Reducing Peak Memory Usage for Modern Multimodal Large Language Model Pipelines](/202604/22/2604.16734v1-reducing-peak-memory-usage-for-modern-multimodal-large-language-model-pipelines)  
   标签：评分：7.5/10、query:mlsys
   evidence：减少多模态大模型流水线的峰值显存占用
5. [FedSEA: Achieving Benefit of Parallelization in Federated Online Learning](/202604/22/2604.19336v1-fedsea-achieving-benefit-of-parallelization-in-federated-online-learning)  
   标签：评分：7.5/10、query:mlsys
   evidence：联邦在线学习算法中的并行化
6. [Are Large Language Models Economically Viable for Industry Deployment?](/202604/22/2604.19342v1-are-large-language-models-economically-viable-for-industry-deployment)  
   标签：评分：7.5/10、query:mlsys
   evidence：硬件利用率与部署效率基准测试
7. [Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling](/202604/22/2604.18264v1-universally-empowering-zeroth-order-optimization-via-adaptive-layer-wise-sampling)  
   标签：评分：7.0/10、query:mlsys
   evidence：识别LLM微调中零阶优化的系统瓶颈
8. [Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts](/202604/22/2604.18473v1-train-separately-merge-together-modular-post-training-with-mixture-of-experts)  
   标签：评分：7.0/10、query:mlsys
   evidence：基于混合专家模型的模块化后训练与独立领域专家训练
9. [Topology-Aware Layer Pruning for Large Vision-Language Models](/202604/22/2604.16502v1-topology-aware-layer-pruning-for-large-vision-language-models)  
   标签：评分：6.5/10、query:mlsys
   evidence：针对资源受限部署的优化
10. [GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models](/202604/22/2604.19398v1-grasprune-global-gating-for-budgeted-structured-pruning-of-large-language-models)  
   标签：评分：6.5/10、query:mlsys
   evidence：提升大模型推理效率的结构化剪枝框架
11. [Adaptive Data Dropout: Towards Self-Regulated Learning in Deep Neural Networks](/202604/22/2604.12945v1-adaptive-data-dropout-towards-self-regulated-learning-in-deep-neural-networks)  
   标签：评分：6.0/10、query:mlsys
   evidence：训练效率优化


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
