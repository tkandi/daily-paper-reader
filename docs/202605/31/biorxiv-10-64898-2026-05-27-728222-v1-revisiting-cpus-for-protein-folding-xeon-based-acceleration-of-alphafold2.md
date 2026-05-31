---
title: "Revisiting CPUs for Protein Folding: Xeon-Based Acceleration of AlphaFold2"
title_zh: 重新审视CPU在蛋白质折叠中的应用：基于至强处理器的AlphaFold2加速
authors: "Chaudhary, N., Yang, W., Kalamkar, D., Zhou, J., Ghosh, S., Xia, L., Tiwari, M., Heinecke, A., Kaul, B., Misra, S."
date: 2026-05-29
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.27.728222v1.full.pdf"
tags: ["query:mlsys"]
score: 8.0
evidence: 针对Intel Xeon CPU优化AlphaFold2流水线，使用AMX加速
tldr: 为解决AlphaFold2在传统GPU上的执行瓶颈，本研究针对Intel Xeon CPU进行了全流水线优化。利用CPU处理稀疏前处理和低算术强度注意力模块的灵活性，结合Intel AMX矩阵扩展，将整个端到端流程加速至与GPU相竞争的水平。这项工作展示了CPU作为深度学习推理替代硬件的潜力，尤其适合异构计算场景。
source: biorxiv
selection_source: fresh_fetch
motivation: 针对Intel Xeon CPU优化AlphaFold2流水线，使用AMX加速。
method: 方法与实现细节请参考摘要与正文。
result: 结果与对比结论请参考摘要与正文。
conclusion: 总体而言，该工作在所述任务上展示了有效性，并提供了可复用的思路或工具。
---

## 摘要
通过AlphaFold2进行蛋白质结构预测已彻底改变了药物发现，但其端到端执行仍然计算密集。尽管传统上GPU在深度学习中更受青睐，但AlphaFold2算法包含异构阶段——预处理阶段涉及稀疏数据库搜索，模型推理阶段包含低算术强度的注意力模块——这带来了独特的架构挑战。在这项工作中，我们通过引入Open-Omics-AlphaFold2来应对这些瓶颈，这是针对英特尔至强CPU的高度优化实现。利用CPU处理稀疏预处理算法和通过英特尔高级矩阵扩展（AMX）进行稠密矩阵运算的多功能性，我们加速了整个端到端流程。我们的优化策略采用多级并行——涵盖多进程、多线程和向量化——以及缓存感知分块和算子融合。我们的结果表明，在至强CPU上，Open-Omics-AlphaFold2相比基线Deepmind-AlphaFold2，预处理速度提升2至7.58倍，模型推理速度提升19.8至29.2倍。此外，对于一个包含391个蛋白质的蛋白质组，运行在双路英特尔至强6980P系统上的Open-Omics-AlphaFold2，比在单路英特尔至强6980P CPU搭配NVIDIA H100卸载的最先进GPU加速方案FastFold，实现了高达76%的吞吐量提升。

## Abstract
Protein structure prediction via AlphaFold2 has revolutionized drug discovery, yet its end-to-end execution remains computationally intensive. While GPUs are traditionally favored for deep learning, the AlphaFold2 algorithm consists of heterogeneous phases --preprocessing with sparse database searches and model inference with low-arithmetic-intensity attention modules -- that present unique architectural challenges. In this work, we address these bottlenecks by introducing Open-Omics-AlphaFold2, a highly optimized implementation for Intel Xeon CPU. By leveraging the CPU's versatility in handling both sparse preprocessing algorithms and dense matrix operations via Intel Advanced Matrix Extensions (AMX), we accelerate the entire pipeline end-to-end. Our optimization strategy employs multi-level parallelism -- spanning multiprocessing, multi-threading, and vectorization -- alongside cache-aware tiling and operator fusion. Our results demonstrate that, on a Xeon CPU, Open-Omics-AlphaFold2 achieves 2 - 7.58x speedup for preprocessing and 19.8 - 29.2x speedup for model inference over baseline Deepmind-AlphaFold2 . Moreover, for a proteome of 391 proteins, Open-Omics AlphaFold2 running on a dual-socket Intel Xeon 6980P system achieves a remarkable 76% higher throughput over the state-of-the-art GPU accelerated solution, FastFold, running on a single-socket Intel Xeon 6980P CPU with an NVIDIA H100 offload.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义  
- **研究动机**：AlphaFold2 虽在蛋白质结构预测上取得突破，但其端到端流水线（预处理 + 模型推理）计算开销极大。传统方案依赖 GPU 加速，然而 AlphaFold2 中存在异质阶段——预处理包含大量稀疏数据库搜索，模型推理中注意力模块算术强度低——这些特性使 GPU 并非全局最优，往往成为瓶颈。  
- **整体含义**：该工作重新审视 CPU 在蛋白质折叠推理中的价值，利用英特尔至强 CPU 同时擅长稀疏任务和稠密矩阵运算（通过 AMX）的灵活性，构建全流水线 CPU 加速方案，挑战“深度学习必须用 GPU”的固有认知，为异构计算时代提供新选择。

### 2. 论文提出的方法论  
- **核心思想**：针对 AlphaFold2 的两大异质阶段，深度定制 CPU 实现，通过软硬件协同榨取至强平台的算力。  
- **关键技术细节**：  
  - **硬件基石**：采用支持英特尔 AMX（高级矩阵扩展）的至强处理器，加速推理中的矩阵乘等稠密算子。  
  - **多级并行策略**：  
    - 多进程并行：在流水线级别将独立任务分配到不同进程。  
    - 多线程并行：在单任务内利用所有 CPU 核心进行数据并行或算子内并行。  
    - 向量化：利用 AVX-512 等指令集进一步利用单核宽度。  
  - **内存与计算优化**：  
    - 缓存感知分块（cache‑aware tiling）：使频繁访问的数据驻留在高速缓存，减少内存带宽压力。  
    - 算子融合（operator fusion）：合并相邻算子降低访存与调度开销，尤其针对低算术强度的注意力模块。  
  - **实现名称**：该系统命名为 **Open‑Omics‑AlphaFold2**，对比基线为 DeepMind 官方 AlphaFold2 实现。

### 3. 实验设计  
- **数据集/场景**：  
  - 单蛋白预测：测量预处理耗时和模型推理时间，未指明具体蛋白质 ID（推断为常用基准蛋白，如 T1050 等经典案例）。  
  - 蛋白质组级预测：使用一个包含 **391 个蛋白质** 的蛋白质组，模拟真实药物发现或基因组学场景。  
- **基准与对比方法**：  
  - **基准**：DeepMind‑AlphaFold2 原始实现。  
  - **竞品**：**FastFold**（最先进的 GPU 加速方案），运行配置为单路英特尔至强 6980P CPU 搭配 **NVIDIA H100** 卸载计算。  
  - **本文方案**：Open‑Omics‑AlphaFold2 运行在 **双路** 英特尔至强 6980P 系统（仅 CPU，无 GPU）。  
- **评估指标**：  
  - 预处理加速比（speedup）  
  - 模型推理加速比  
  - 蛋白质组端到端吞吐量（单位时间内完成的蛋白数）

### 4. 资源与算力  
- **推理硬件**：  
  - 主测系统：双路英特尔至强 6980P（仅 CPU，利用 AMX）。  
  - 对比系统：单路英特尔至强 6980P + NVIDIA H100（FastFold 方案）。  
  - 未提及训练阶段的硬件或时长（本工作聚焦于推理加速，若 AlphaFold2 模型使用预训练参数，则无额外训练开销）。  
- **说明**：论文摘要未给出训练配置，仅交代推理环境，但基于上下文，该研究属于推理流水线优化，训练部分非重点。

### 5. 实验数量与充分性  
- **实验组数**：从摘要推断至少包含两组主要对比——  
  1. 单蛋白预处理与推理的加速比对比（2‑7.58倍预处理，19.8‑29.2倍推理）。  
  2. 391 蛋白蛋白质组的吞吐量对比（76% 提升 vs FastFold）。  
- **充分性评价**：  
  - 对比了官方实现和当时 SOTA 的 GPU 加速方案，纵向、横向兼具。  
  - 缺乏不同蛋白长度、不同模型版本（如 AlphaFold2 的 5 个模型）或消融研究的细节，但因摘要篇幅限制，正文可能包含更多实验（如仅 CPU 无 AMX、各优化阶段收益等）。  
  - 公平性方面：使用双路 CPU 对比单路 CPU+GPU，算力绝对成本可能不同，但反映了实际服务器配置的灵活性，后续若提供单路 CPU 结果将更完善。

### 6. 论文的主要结论与发现  
- 在至强 CPU 上，Open‑Omics‑AlphaFold2 相比 DeepMind 原始实现取得 **2–7.58 倍预处理加速** 与 **19.8–29.2 倍模型推理加速**。  
- 在 **391 蛋白蛋白质组** 端到端任务中，**纯 CPU 方案（双路 Xeon 6980P）** 的吞吐量比 **CPU + NVIDIA H100 的 SOTA 方案** 高出 **76%**。  
- 证明了 CPU 通过专用矩阵引擎（AMX）和精细软件栈，能在蛋白质折叠这类混合负载上超越传统异构加速组合，为大规模蛋白质组分析提供了低成本、高灵活性的替代平台。

### 7. 优点  
- **算法‑架构协同**：深刻认识 AlphaFold2 的稀疏/低强度阶段，巧妙发挥 CPU 的通用性与 AMX 的矩阵能力。  
- **全流水线优化**：非局部调优，覆盖预处理与推理全程，端到端收益显著。  
- **与 GPU SOTA 正面交锋**：没有刻意选择弱基线，而是对比 FastFold + H100，且实现了逆袭，结论说服力强。  
- **工程实用性**：所提多级并行、缓存分块、融合等技术具有可泛化性，对 CPU 深度学习推理部署有参考价值。

### 8. 不足与局限  
- **硬件配置不对称**：双路 CPU 与单路 CPU+H100 对比，总功耗、成本、对等配置的公平性可进一步讨论（如缺少双路 CPU 对双路 CPU+GPU 的对比）。  
- **实验粒度受限**：摘要未展示消融分析（如纯线程优化、AMX 开关、分块大小影响）、不同蛋白质长度下的延迟变化、内存容量上限等，可能影响结论的泛化性。  
- **数据集大小**：仅用一个 391 蛋白的蛋白质组，缺少更大规模乃至全基因组级别或跨物种的测试。  
- **H100 软件成熟度**：FastFold 在 H100 上的优化程度是否与 CPU 版本同等深度未知，若 H100 亦经极致调优，结果可能变化。  
- **适用的模型范围**：仅限于 AlphaFold2 推理，未涉及类似模型（如 AlphaFold-Multimer、ESMFold）或其他科学计算负载，生态兼容性待考察。  

（完）
