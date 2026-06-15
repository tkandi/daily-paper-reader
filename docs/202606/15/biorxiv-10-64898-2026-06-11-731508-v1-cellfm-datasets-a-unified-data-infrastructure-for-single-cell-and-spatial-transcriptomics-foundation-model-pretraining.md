---
title: "Cellfm-datasets: A Unified Data Infrastructure for Single-Cell and Spatial Transcriptomics Foundation Model Pretraining"
title_zh: Cellfm-datasets：面向单细胞与空间转录组学基础模型预训练的统一数据基础设施
authors: "Zhang, L., Pang, J., Yan, J., Tang, W., Deng, Y., He, Y."
date: 2026-06-14
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.11.731508v1.full.pdf"
tags: ["query:mlsys"]
score: 7.0
evidence: 面向细胞基础模型分布式预训练的统一数据基础设施
tldr: "随着单细胞与空间组学数据规模扩大，传统H5AD格式难以满足大规模细胞基础模型预训练对高频随机采样和分布式加载的需求，成为数据加载瓶颈。Cellfm-datasets构建了统一的CSR memmap数据基础设施，通过Hugging Face Dataset接口支持细胞组、生物区域和空间块采样，并实现确定性分片；空间转录组实验展示了真实解剖结构上的区域和块采样。在公共scRNA-seq数据集上单核加载达60,571样本/秒，8 worker扩展至~160,000样本/秒，同时保持恒定的进程内存。该工作推动了可重复预训练的标准化，降低了混合模态复用与模型比较的工程负担。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有基于H5AD的数据存储难以支持大规模细胞模型预训练所需的高频随机采样与分布式加载，急需高效统一的数据基础设施。
method: 将H5AD转换为自描述CSR memmap布局，通过Hugging Face Dataset提供统一接口，支持随机细胞组、区域及空间块采样。
result: "单核随机加载达60,571样本/秒，8 worker扩展至约160,000样本/秒，内存占用恒定，并在百万细胞及空间数据上验证。"
conclusion: Cellfm-datasets通过标准化数据工件，简化了可重复预训练流程，降低了工程负担，并促进了模型比较与多模态数据重用。
---

## 摘要
大规模细胞基础模型日益受限于模型架构，也受限于从核外队列重复采样稀疏转录组谱所需的数据基础设施。AnnData/H5AD已成为单细胞和空间组学分析的标准交换格式，但其基于HDF5的布局并非为多工作节点和分布式预训练下的高频随机小批量加载而设计。我们提出Cellfm-datasets，一种将H5AD队列转换为自描述压缩稀疏行（CSR）内存映射布局的数据基础设施构件，并通过Hugging Face Dataset和IterableDataset接口暴露所得语料。该构件存储共享基因词汇、逐样本元数据、可选空间坐标、观测元数据、清单和校验和，并在运行时重建稀疏细胞或群组记录，无需密集扩展。统一的采样抽象支持随机细胞群组、清单定义的生物区域和基于坐标的空间块，并在分布式级别和数据加载工作节点间进行确定性分片。在小鼠P14脑转录组切片上的空间演示，展示了真实解剖结构上的区域和块级采样。在公开异构ModelScope scRNA-seq子集的受控基准测试中，Cellfm-datasets在单核随机加载下达到60,571±1,734样本/秒，使用八个工作节点时扩展到约160,000样本/秒，并在读取多达一百万个细胞时保持近乎恒定的进程私有内存。通过将稀疏单细胞和空间语料从模型特定的加载代码转移到可复用、经过验证且框架原生的数据集构件中，这一设计可减轻可复现细胞基础模型预训练的工程负担，并使重复训练运行、模型比较和混合模态数据重用更易于标准化。

## Abstract
Large-scale cell foundation models are increasingly limited not only by model architecture, but also by the data infrastructure required to repeatedly sample sparse transcriptomic profiles from out-of-core cohorts. AnnData/H5AD has become a standard exchange format for single-cell and spatial omics analysis, yet its HDF5-backed layout is not designed for high-frequency random mini-batch loading under multi-worker and distributed pretraining. We present Cellfm-datasets, a data infrastructure artifact that converts H5AD cohorts into a self-describing compressed sparse row (CSR) memmap layout and exposes the resulting corpus through Hugging Face Dataset and IterableDataset interfaces. The artifact stores a shared gene vocabulary, per-sample metadata, optional spatial coordinates, observation metadata, manifests, and checksums, and reconstructs sparse cell or group records at runtime without dense expansion. A unified sampling abstraction supports random-cell groups, manifest-defined biological regions, and coordinate-based spatial blocks, with deterministic sharding across distributed ranks and data-loader workers. Spatial demonstrations on P14 mouse brain transcriptomics sections illustrate region- and block-level sampling over real anatomical structures. In controlled benchmarks on a public heterogeneous ModelScope scRNA-seq subset, Cellfm-datasets reached 60,571 +/- 1,734 samples/s in single-core random loading, scaled to approximately 160,000 samples/s with eight workers, and maintained near-constant process-private memory while reading up to one million cells. By moving sparse single-cell and spatial corpora from model-specific loader code into reusable, validated, and framework-native dataset artifacts, this design may reduce the engineering burden of reproducible cell foundation model pretraining and make repeated training runs, model comparisons, and mixed-modality data reuse easier to standardize.