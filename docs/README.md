<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-07-07
- 运行时间：2026-07-07 21:20:51 UTC
- 运行状态：成功
- 本次总论文数：8
- 精读区：6
- 速读区：2

### 今日简报（AI）
今日深入研读模型训练与推理的极致优化：从算子级 PyTorch 自动改造框架到超节点集群上的多模态大模型训练代数系统。  
最值得关注的两项突破是《Optimus》让 PyTorch 模型无需手动改代码即可实现通用算子级加速，以及《HyperParallel-Mpipe》用可组合代数编排超节点集群流水线，大幅提升多模态训练效率。  
建议跟进这些框架的开源动态，并优先在推理链路上测试基于策略梯度的自适应批处理，立即降低延迟成本。
- 详情：[/202607/07/README](/202607/07/README)

### 精读区论文标签
1. [Optimus: A Generic Operator-Level PyTorch Model Transformation Framework](/202607/07/2607.02945v1-optimus-a-generic-operator-level-pytorch-model-transformation-framework)  
   标签：评分：9.0/10、query:mlsys
   evidence：面向PyTorch 2.x编译器的算子级模型转换框架
2. [HyperParallel-Mpipe: A Composable Algebra System for Optimizing MLLM Training over Supernode Clusters](/202607/07/2607.03229v1-hyperparallel-mpipe-a-composable-algebra-system-for-optimizing-mllm-training-over-supernode-clusters)  
   标签：评分：9.0/10、query:mlsys
   evidence：提出一种用于多模态大模型训练的流水线并行调度代数，在昇腾集群上实现2.70倍加速
3. [A Reconfigurable and Representation-Adaptive ISA-Based Architecture for Efficient DNN Acceleration](/202607/07/2607.04475v1-a-reconfigurable-and-representation-adaptive-isa-based-architecture-for-efficient-dnn-acceleration)  
   标签：评分：9.0/10、query:mlsys
   evidence：基于ISA的DNN硬件加速器
4. [Direct Model State Migration for Elastic Training of Large Language Models](/202607/07/2607.04749v1-direct-model-state-migration-for-elastic-training-of-large-language-models)  
   标签：评分：9.0/10、query:mlsys
   evidence：面向弹性混合并行LLM训练的无检查点状态迁移
5. [Communication-Aware Placement and Pruning for Efficient Mixture-of-Experts Inference](/202607/07/2607.05116v1-communication-aware-placement-and-pruning-for-efficient-mixture-of-experts-inference)  
   标签：评分：9.0/10、query:mlsys
   evidence：提出通信感知的专家放置与剪枝框架，优化分布式MoE推理系统架构。
6. [BrownoutMoE: Structure-Aware Expert Grouping for Efficient and Accurate LLM Web-based Services](/202607/07/2607.04164v1-brownoutmoe-structure-aware-expert-grouping-for-efficient-and-accurate-llm-web-based-services)  
   标签：评分：8.0/10、query:mlsys
   evidence：结构感知专家分组提升MoE LLM推理的GPU利用率

### 速读区论文标签
1. [FAST: A Holistic Framework for Optimizing Memory-I/O, Computation, and Sampling in Temporal GNN Training](/202607/07/2607.05095v1-fast-a-holistic-framework-for-optimizing-memory-io-computation-and-sampling-in-temporal-gnn-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：整体优化时序图神经网络训练中内存I/O、计算和采样的框架
2. [Adaptive Inference Batching using Policy Gradients](/202607/07/2607.05272v1-adaptive-inference-batching-using-policy-gradients)  
   标签：评分：7.0/10、query:mlsys
   evidence：基于强化学习的自适应批处理和路由，用于GPU推理服务


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
