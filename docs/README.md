<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-05-08
- 运行时间：2026-05-08 20:57:07 UTC
- 运行状态：成功
- 本次总论文数：20
- 精读区：9
- 速读区：11

### 今日简报（AI）
今日精选 20 篇前沿成果，重点攻克多 GPU 环境下交换机内计算（In-Switch Computing）对 MoE 与张量并行的极致加速。
满分论文揭示了软硬协同设计是突破 LLM 通信瓶颈的关键，同时本地学习与推理批处理优化也迎来新进展。
建议优先关注多 GPU 互联架构的硬件演进，这是理解大模型推理效率提升的核心赛道。
- 详情：[/202605/08/README](/202605/08/README)

### 精读区论文标签
1. [Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs](/202605/08/2605.05607v1-accelerating-moe-with-dynamic-in-switch-computing-on-multi-gpus)  
   标签：评分：10.0/10、query:mlsys
   evidence：加速多GPU上MoE通信的动态交换机内计算
2. [Towards Compute-Aware In-Switch Computing for LLMs Tensor-Parallelism on Multi-GPU Systems](/202605/08/2605.05628v1-towards-compute-aware-in-switch-computing-for-llms-tensor-parallelism-on-multi-gpu-systems)  
   标签：评分：10.0/10、query:mlsys
   evidence：多GPU系统中的张量并行与交换机内计算
3. [MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems](/202605/08/2605.05888v1-moe-hub-taming-software-complexity-for-seamless-moe-overlap-with-hardware-accelerated-communication-on-multi-gpu-systems)  
   标签：评分：10.0/10、query:mlsys
   evidence：优化多GPU系统上的MoE通信重叠
4. [ResiHP: Taming LLM Training Failures with Dynamic Hybrid](/202605/08/2605.06374v1-resihp-taming-llm-training-failures-with-dynamic-hybrid)  
   标签：评分：10.0/10、query:mlsys
   evidence：大规模LLM训练中的混合并行
5. [VUDA: Breaking CUDA-Vulkan Isolation for Spatial Sharing of Compute and Graphics on the Same GPU](/202605/08/2605.01352v1-vuda-breaking-cuda-vulkan-isolation-for-spatial-sharing-of-compute-and-graphics-on-the-same-gpu)  
   标签：评分：9.0/10、query:mlsys
   evidence：在同一GPU上实现计算与图形的显存空间共享
6. [Nitsum: Serving Tiered LLM Requests with Adaptive Tensor Parallelism](/202605/08/2605.05467v1-nitsum-serving-tiered-llm-requests-with-adaptive-tensor-parallelism)  
   标签：评分：9.0/10、query:mlsys
   evidence：具有自适应张量并行的分布式LLM推理系统，用于GPU资源管理
7. [EdgeServing: Deadline-Aware Multi-DNN Serving at the Edge](/202605/08/2605.05527v1-edgeserving-deadline-aware-multi-dnn-serving-at-the-edge)  
   标签：评分：9.0/10、query:mlsys
   evidence：GPU资源调度与管理
8. [VisMMOE: Exploiting Visual-Expert Affinity for Efficient Visual-Language MoE Offloading](/202605/08/2605.05899v1-vismmoe-exploiting-visual-expert-affinity-for-efficient-visual-language-moe-offloading)  
   标签：评分：9.0/10、query:mlsys
   evidence：针对内存受限平台的VL-MoE卸载系统
9. [Federation of Experts: Communication Efficient Distributed Inference for Large Language Models](/202605/08/2605.06206v1-federation-of-experts-communication-efficient-distributed-inference-for-large-language-models)  
   标签：评分：9.0/10、query:mlsys
   evidence：针对大语言模型推理的通信高效分布式架构，采用专家并行技术

### 速读区论文标签
1. [Rethinking Local Learning: A Cheaper and Faster Recipe for LLM Post-Training](/202605/08/2605.04913v2-rethinking-local-learning-a-cheaper-and-faster-recipe-for-llm-post-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：高效的大语言模型后训练策略
2. [DICE: Enabling Efficient General-Purpose SIMT Execution with Statically Scheduled Coarse-Grained Reconfigurable Arrays](/202605/08/2605.05496v1-dice-enabling-efficient-general-purpose-simt-execution-with-statically-scheduled-coarse-grained-reconfigurable-arrays)  
   标签：评分：8.0/10、query:mlsys
   evidence：替换SIMD后端以提高能效的新型架构
3. [Requests of a Feather Must Flock Together: Batch Size vs. Prefix Homogeneity in LLM Inference](/202605/08/2605.06046v1-requests-of-a-feather-must-flock-together-batch-size-vs-prefix-homogeneity-in-llm-inference)  
   标签：评分：8.0/10、query:mlsys
   evidence：提高LLM推理引擎的解码吞吐量和效率
4. [Finite-Size Gradient Transport in Large Language Model Pretraining: From Cascade Size to Intensive Transport Efficiency](/202605/08/2605.02968v1-finite-size-gradient-transport-in-large-language-model-pretraining-from-cascade-size-to-intensive-transport-efficiency)  
   标签：评分：7.0/10、query:mlsys
   evidence：大语言模型预训练中的梯度传输框架
5. [Replacing Parameters with Preferences: Federated Alignment of Heterogeneous Vision-Language Models](/202605/08/2605.03426v1-replacing-parameters-with-preferences-federated-alignment-of-heterogeneous-vision-language-models)  
   标签：评分：7.0/10、query:mlsys
   evidence：异构模型的联邦对齐框架
6. [Rethinking Local Learning: A Cheaper and Faster Recipe for LLM Post-Training](/202605/08/2605.04913v1-rethinking-local-learning-a-cheaper-and-faster-recipe-for-llm-post-training)  
   标签：评分：7.0/10、query:mlsys
   evidence：减少LLM后训练内存和计算开销的局部学习策略
7. [Expert Routing for Communication-Efficient MoE via Finite Expert Banks](/202605/08/2605.05278v1-expert-routing-for-communication-efficient-moe-via-finite-expert-banks)  
   标签：评分：7.0/10、query:mlsys
   evidence：MoE中控制计算和通信的路由接口
8. [Revealing Modular Gradient Noise Imbalance in LLMs: Calibrating Adam via Signal-to-Noise Ratio](/202605/08/2605.05794v1-revealing-modular-gradient-noise-imbalance-in-llms-calibrating-adam-via-signal-to-noise-ratio)  
   标签：评分：7.0/10、query:mlsys
   evidence：大规模模型训练中的优化挑战
9. [ViM-Q: Scalable Algorithm-Hardware Co-Design for Vision Mamba Model Inference on FPGA](/202605/08/2605.01935v1-vim-q-scalable-algorithm-hardware-co-design-for-vision-mamba-model-inference-on-fpga)  
   标签：评分：6.5/10、query:mlsys
   evidence：针对FPGA模型推理的算法-硬件协同设计
10. [VARS-FL: Validation-Aligned Client Selection for Non-IID Federated Learning in IoT Systems](/202605/08/2605.05896v1-vars-fl-validation-aligned-client-selection-for-non-iid-federated-learning-in-iot-systems)  
   标签：评分：6.5/10、query:mlsys
   evidence：联邦学习系统的客户端选择框架
11. [MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents](/202605/08/2605.03312v1-memflow-intent-driven-memory-orchestration-for-small-language-model-agents)  
   标签：评分：6.0/10、query:mlsys
   evidence：语言模型智能体的内存编排框架


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
