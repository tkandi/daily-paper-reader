<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-04-08
- 运行时间：2026-04-08 20:28:24 UTC
- 运行状态：成功
- 本次总论文数：19
- 精读区：8
- 速读区：11

### 今日简报（AI）
今日聚焦大模型工程极限，见证单卡训练百亿参数模型与 NVL72 推理性能的重大突破。
满分论文 MegaTrain 实现了单 GPU 全精度训练 100B+ 模型的壮举，DWDP 则显著优化了超大规模集群的推理效率。
建议开发者重点关注 Agent 统一记忆框架及生物大数据 TB 级训练的最新工程实践。
- 详情：[/202604/08/README](/202604/08/README)

### 精读区论文标签
1. [MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU](/202604/08/2604.05091v1-megatrain-full-precision-training-of-100b-parameter-large-language-models-on-a-single-gpu)  
   标签：评分：10.0/10、query:mlsys
   evidence：利用流水线执行在单GPU上训练千亿参数模型的以内存为中心的系统
2. [DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72](/202604/08/2604.01621v1-dwdp-distributed-weight-data-parallelism-for-high-performance-llm-inference-on-nvl72)  
   标签：评分：9.0/10、query:mlsys
   evidence：分布式推理并行化策略与MoE权重管理
3. [FlatAttention: Dataflow and Fabric Collectives Co-Optimization for Large Attention-Based Model Inference on Tile-Based Accelerators](/202604/08/2604.02110v1-flatattention-dataflow-and-fabric-collectives-co-optimization-for-large-attention-based-model-inference-on-tile-based-accelerators)  
   标签：评分：9.0/10、query:mlsys
   evidence：大模型推理的基础设施与数据流优化
4. [Minos: Systematically Classifying Performance and Power Characteristics of GPU Workloads on HPC Clusters](/202604/08/2604.03591v2-minos-systematically-classifying-performance-and-power-characteristics-of-gpu-workloads-on-hpc-clusters)  
   标签：评分：9.0/10、query:mlsys
   evidence：集群中GPU工作负载的性能与功耗特性
5. [BlazeFL: Fast and Deterministic Federated Learning Simulation](/202604/08/2604.03606v1-blazefl-fast-and-deterministic-federated-learning-simulation)  
   标签：评分：9.0/10、query:mlsys
   evidence：分布式训练模拟框架
6. [GENSERVE: Efficient Co-Serving of Heterogeneous Diffusion Model Workloads](/202604/08/2604.04335v1-genserve-efficient-co-serving-of-heterogeneous-diffusion-model-workloads)  
   标签：评分：9.0/10、query:mlsys
   evidence：在共享GPU集群上协同提供异构工作负载服务
7. [ALTO: Adaptive LoRA Tuning and Orchestration for Heterogeneous LoRA Training Workloads](/202604/08/2604.05426v1-alto-adaptive-lora-tuning-and-orchestration-for-heterogeneous-lora-training-workloads)  
   标签：评分：9.0/10、query:mlsys
   evidence：用于异构任务间高效集群共享和GPU利用率的训练系统
8. [GTaP: A GPU-Resident Fork-Join Task-Parallel Runtime with a Pragma-Based Interface](/202604/08/2604.05982v1-gtap-a-gpu-resident-fork-join-task-parallel-runtime-with-a-pragma-based-interface)  
   标签：评分：9.0/10、query:mlsys
   evidence：用于任务并行调度的GPU驻留运行时

### 速读区论文标签
1. [MemFactory: Unified Inference & Training Framework for Agent Memory](/202604/08/2603.29493v4-memfactory-unified-inference--training-framework-for-agent-memory)  
   标签：评分：8.0/10、query:mlsys
   evidence：AI智能体统一训练与推理框架
2. [Adaptive Parallel Monte Carlo Tree Search for Efficient Test-time Compute Scaling](/202604/08/2604.00510v1-adaptive-parallel-monte-carlo-tree-search-for-efficient-test-time-compute-scaling)  
   标签：评分：8.0/10、query:mlsys
   evidence：资源争用管理并集成至vLLM推理框架
3. [annbatch unlocks terabyte-scale training of biological data in anndata](/202604/08/2604.01949v2-annbatch-unlocks-terabyte-scale-training-of-biological-data-in-anndata)  
   标签：评分：8.0/10、query:mlsys
   evidence：TB级生物数据集的离存训练
4. [Backdoor Attacks on Decentralised Post-Training](/202604/08/2604.02372v1-backdoor-attacks-on-decentralised-post-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：LLM训练中流水线并行的安全性
5. [Causality-inspired Federated Learning for Dynamic Spatio-Temporal Graphs](/202604/08/2603.29384v1-causality-inspired-federated-learning-for-dynamic-spatio-temporal-graphs)  
   标签：评分：7.0/10、query:mlsys
   evidence：图神经网络的去中心化训练范式
6. [Quantization with Unified Adaptive Distillation to enable multi-LoRA based one-for-all Generative Vision Models on edge](/202604/08/2603.29535v1-quantization-with-unified-adaptive-distillation-to-enable-multi-lora-based-one-for-all-generative-vision-models-on-edge)  
   标签：评分：7.0/10、query:mlsys
   evidence：边缘端多任务AI推理基础设施
7. [GreenFLag: A Green Agentic Approach for Energy-Efficient Federated Learning](/202604/08/2603.29933v1-greenflag-a-green-agentic-approach-for-energy-efficient-federated-learning)  
   标签：评分：7.0/10、query:mlsys
   evidence：联邦学习资源编排框架
8. [Executing as You Generate: Hiding Execution Latency in LLM Code Generation](/202604/08/2604.00491v1-executing-as-you-generate-hiding-execution-latency-in-llm-code-generation)  
   标签：评分：7.0/10、query:mlsys
   evidence：LLM代码生成的并行执行范式
9. [An Empirical Study of Multi-Agent Collaboration for Automated Research](/202604/08/2603.29632v1-an-empirical-study-of-multi-agent-collaboration-for-automated-research)  
   标签：评分：6.0/10、query:mlsys
   evidence：用于自动化机器学习研究的多智能体系统架构
10. [Loss Gap Parity for Fairness in Heterogeneous Federated Learning](/202604/08/2603.29818v1-loss-gap-parity-for-fairness-in-heterogeneous-federated-learning)  
   标签：评分：6.0/10、query:mlsys
   evidence：异构环境下的分布式联邦学习算法
11. [Self-Routing: Parameter-Free Expert Routing from Hidden States](/202604/08/2604.00421v1-self-routing-parameter-free-expert-routing-from-hidden-states)  
   标签：评分：6.0/10、query:mlsys
   evidence：MoE架构的无参数专家路由机制


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
