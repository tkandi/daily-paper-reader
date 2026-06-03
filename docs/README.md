<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-03
- 运行时间：2026-06-03 21:59:24 UTC
- 运行状态：成功
- 本次总论文数：6
- 精读区：4
- 速读区：2

### 今日简报（AI）
今日聚焦大模型推理与训练的稳定性优化：NetKV 提出解耦式 LLM 推理的网络感知实例选择，GNMR 用运行时稳定性控制降低低精度训练崩溃风险。  
最值得关注的两个方向：一是如何让分布式推理的 KV 缓存调度贴近网络拓扑，二是如何在不牺牲精度的前提下动态守卫训练收敛。  
建议读者优先阅读 NetKV 的解耦调度思路，若关注训练成本可补看 GNMR 的混合精度稳定策略。
- 详情：[/202606/03/README](/202606/03/README)

### 精读区论文标签
1. [NetKV: Network-Aware Decode Instance Selection for Disaggregated LLM Inference](/202606/03/2606.03910v1-netkv-network-aware-decode-instance-selection-for-disaggregated-llm-inference)  
   标签：评分：10.0/10、query:mlsys
   evidence：NetKV利用网络感知调度优化分离式LLM推理中的GPU集群资源管理。
2. [GNMR: Runtime Stability Control for Low-Precision Large Language Model Training](/202606/03/2606.00539v1-gnmr-runtime-stability-control-for-low-precision-large-language-model-training)  
   标签：评分：9.0/10、query:mlsys
   evidence：用于低精度大语言模型训练稳定性的轻量级控制器
3. [HASTE: Hardware-Aware Dynamic Sparse Training for Large Output Spaces](/202606/03/2606.01117v1-haste-hardware-aware-dynamic-sparse-training-for-large-output-spaces)  
   标签：评分：9.0/10、query:mlsys
   evidence：硬件感知动态稀疏训练解决极端多标签分类的内存计算瓶颈
4. [FedMTFI: Feature Importance Based Optimized Multi Teacher Knowledge Distillation in Heterogeneous Federated Learning Environment](/202606/03/2606.01607v1-fedmtfi-feature-importance-based-optimized-multi-teacher-knowledge-distillation-in-heterogeneous-federated-learning-environment)  
   标签：评分：9.0/10、query:mlsys
   evidence：结合多教师知识蒸馏与特征重要性以提升异构联邦学习性能

### 速读区论文标签
1. [Continual Model Routing in Evolving Model Hubs](/202606/03/2605.28577v1-continual-model-routing-in-evolving-model-hubs)  
   标签：评分：7.0/10、query:mlsys
   evidence：将演进模型中心中的持续模型路由形式化，以扩展到数千个专家的模型选择。
2. [SuperValid: Capability-Aligned OOD Validation for Generalizable Downstream Scaling](/202606/03/2605.28179v1-supervalid-capability-aligned-ood-validation-for-generalizable-downstream-scaling)  
   标签：评分：6.0/10、query:mlsys
   evidence：SuperValid合成能力对齐的OOD验证数据改进缩放律预测，优化大规模模型训练。


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
