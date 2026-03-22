<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-03-22
- 运行时间：2026-03-22 19:30:39 UTC
- 运行状态：成功
- 本次总论文数：17
- 精读区：6
- 速读区：11

### 今日简报（AI）
今日深度解析 17 篇前沿论文，聚焦 NCCL 专家并行通信优化与 LLM 推理集群的科学规划。
重点推荐统一专家并行 API (NCCL EP) 及基于排队论的推理容量规划工具，大幅提升大规模模型训练与部署效率。
建议关注边缘端硬件加速微调与去中心化 AI 架构，探索模型在极致资源受限环境下的落地可能。
- 详情：[/202603/22/README](/202603/22/README)

### 精读区论文标签
1. [NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL](/202603/22/2603.13606v1-nccl-ep-towards-a-unified-expert-parallel-communication-api-for-nccl)  
   标签：评分：10.0/10、query:mlsys
   evidence：针对MoE扩展的专家并行通信库
2. [inference-fleet-sim: A Queueing-Theory-Grounded Fleet Capacity Planner for LLM Inference](/202603/22/2603.16054v1-inference-fleet-sim-a-queueing-theory-grounded-fleet-capacity-planner-for-llm-inference)  
   标签：评分：9.0/10、query:mlsys
   evidence：LLM推理的GPU集群容量规划与资源管理
3. [AI+HW 2035: Shaping the Next Decade](/202603/22/2603.05225v1-aihw-2035-shaping-the-next-decade)  
   标签：评分：8.0/10、query:mlsys
   evidence：AI与硬件协同设计及计算栈重构路线图
4. [LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing](/202603/22/2603.08453v1-lycheecluster-efficient-long-context-inference-with-structure-aware-chunking-and-hierarchical-kv-indexing)  
   标签：评分：8.0/10、query:mlsys
   evidence：长文本LLM推理中的高效KV缓存管理和分层索引
5. [SVD Contextual Sparsity Predictors for Fast LLM Inference](/202603/22/2603.14110v1-svd-contextual-sparsity-predictors-for-fast-llm-inference)  
   标签：评分：8.0/10、query:mlsys
   evidence：支持CUDA和CANN设备的推理执行器
6. [Parallel In-context Learning for Large Vision Language Models](/202603/22/2603.16092v1-parallel-in-context-learning-for-large-vision-language-models)  
   标签：评分：8.0/10、query:mlsys
   evidence：长上下文视觉语言模型的并行推理算法

### 速读区论文标签
1. [Split Federated Learning Architectures for High-Accuracy and Low-Delay Model Training](/202603/22/2603.08687v1-split-federated-learning-architectures-for-high-accuracy-and-low-delay-model-training)  
   标签：评分：8.0/10、query:mlsys
   evidence：用于模型训练的拆分联邦学习架构
2. [A Decentralized Frontier AI Architecture Based on Personal Instances, Synthetic Data, and Collective Context Synchronization](/202603/22/2603.08893v1-a-decentralized-frontier-ai-architecture-based-on-personal-instances-synthetic-data-and-collective-context-synchronization)  
   标签：评分：8.0/10、query:mlsys
   evidence：去中心化分布式 AI 框架架构
3. [TrainDeeploy: Hardware-Accelerated Parameter-Efficient Fine-Tuning of Small Transformer Models at the Extreme Edge](/202603/22/2603.09511v1-traindeeploy-hardware-accelerated-parameter-efficient-fine-tuning-of-small-transformer-models-at-the-extreme-edge)  
   标签：评分：8.0/10、query:mlsys
   evidence：极端边缘SoC上的设备端训练流水线
4. [CA-HFP: Curvature-Aware Heterogeneous Federated Pruning with Model Reconstruction](/202603/22/2603.12591v1-ca-hfp-curvature-aware-heterogeneous-federated-pruning-with-model-reconstruction)  
   标签：评分：8.0/10、query:mlsys
   evidence：异构边缘设备上的联邦学习与剪枝
5. [Privacy-Preserving Machine Learning for IoT: A Cross-Paradigm Survey and Future Roadmap](/202603/22/2603.13570v1-privacy-preserving-machine-learning-for-iot-a-cross-paradigm-survey-and-future-roadmap)  
   标签：评分：7.0/10、query:mlsys
   evidence：分布式训练流水线与系统架构综述
6. [FedPBS: Proximal-Balanced Scaling Federated Learning Model for Robust Personalized Training for Non-IID Data](/202603/22/2603.13909v1-fedpbs-proximal-balanced-scaling-federated-learning-model-for-robust-personalized-training-for-non-iid-data)  
   标签：评分：7.0/10、query:mlsys
   evidence：根据分布式客户端资源调整批处理大小的联邦学习算法
7. [True 4-Bit Quantized Convolutional Neural Network Training on CPU: Achieving Full-Precision Parity](/202603/22/2603.13931v1-true-4-bit-quantized-convolutional-neural-network-training-on-cpu-achieving-full-precision-parity)  
   标签：评分：7.0/10、query:mlsys
   evidence：在CPU上使用标准PyTorch操作训练CNN的实用方法
8. [Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys](/202603/22/2603.14224v1-self-indexing-kvcache-predicting-sparse-attention-from-compressed-keys)  
   标签：评分：7.0/10、query:mlsys
   evidence：硬件友好的KV缓存压缩与检索
9. [StatePlane: A Cognitive State Plane for Long-Horizon AI Systems Under Bounded Context](/202603/22/2603.13644v1-stateplane-a-cognitive-state-plane-for-long-horizon-ai-systems-under-bounded-context)  
   标签：评分：6.0/10、query:mlsys
   evidence：用于管理AI系统KV缓存和上下文的认知状态平面
10. [Knowledge Distillation for Large Language Models](/202603/22/2603.13765v1-knowledge-distillation-for-large-language-models)  
   标签：评分：6.0/10、query:mlsys
   evidence：通过知识蒸馏压缩大语言模型的资源高效型框架
11. [Greedy Information Projection for LLM Data Selection](/202603/22/2603.13790v1-greedy-information-projection-for-llm-data-selection)  
   标签：评分：6.0/10、query:mlsys
   evidence：大规模模型训练的数据选择优化


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
