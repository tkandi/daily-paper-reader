---
title: "AutoZyme: An Autonomous Agentic Framework to Optimize Bioinformatics Software"
title_zh: AutoZyme：一种用于优化生物信息学软件的自主代理框架
authors: "Xie, E., Cheng, L., Cai, Y., Shireman, J., Kendziorski, C."
date: 2026-06-16
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.12.731250v1.full.pdf"
tags: ["query:mlsys"]
score: 6.0
evidence: 用于自动软件优化的代理框架，可应用于AI基础设施
tldr: "随着生物数据集快速增长，基因组学软件性能瓶颈日益严重，传统手动优化难以规模化。AutoZyme作为一种自主代理框架，可自动建立基准、识别瓶颈并迭代优化代码，保留提升速度且保持输出的变更。在45个函数上，超过95%案例无显著内存增加，中位加速8.52倍，最高超676倍。优化的函数通过AutoZyme-Library提供即插即用替代，并发布可复用框架以支持用户自定义优化。"
source: biorxiv
selection_source: fresh_fetch
motivation: 生物数据集规模激增，基因组学软件性能瓶颈严重，手动优化难以规模化。
method: AutoZyme自主代理框架通过建立基准、识别瓶颈并迭代优化代码，只保留提升运行时且保持输出的变更。
result: "在45个函数上超95%案例无显著内存增加，38个生物信息函数运行时中位数减少8.52倍，最大超676倍。"
conclusion: 发布AutoZyme-Library即插即用优化函数，并开放可复用框架，支持用户自定义软件功能优化。
---

## 摘要
随着生物数据集规模和数量的持续增长，广泛使用的基因组学和生物信息学软件中的性能瓶颈带来了日益沉重的负担。缓解这些瓶颈在很大程度上依赖专家手动优化，因此难以规模化。本文提出了AutoZyme，一个用于科学软件优化的代理框架。给定目标函数，AutoZyme构建基准测试、识别瓶颈，并迭代测试代码更改，仅保留那些提升运行时性能同时保持输出版本的内容。我们在45个函数上评估了AutoZyme，在超过95%的案例中，它在没有显著增加内存占用的前提下缩短了运行时间。在Seurat、Scanpy以及基因组学和生物信息学相关软件包的38个函数中，AutoZyme将运行时间中位数缩短了8.52倍，最大缩减幅度超过676倍。优化后的函数通过AutoZyme-Library分发，可作为现有分析流程的直接替代。我们还将AutoZyme作为一个可复用框架发布，用于优化其他用户指定的软件包和函数。

## Abstract
Performance bottlenecks in widely used genomics and bioinformatics software present a substantial and growing burden as biological datasets continue to increase in size and number. Relieving these bottlenecks relies largely on expert manual optimization and therefore remains difficult to scale. Here we present AutoZyme, an agentic framework for scientific software optimization. Given a target function, AutoZyme builds benchmarks, identifies bottlenecks, and iteratively tests code changes, retaining only those that improve runtime while preserving output. We evaluated AutoZyme on 45 functions, improving runtime without substantial memory increases in over 95% of cases considered. Across 38 functions from Seurat, Scanpy and related packages in genomics and bioinformatics, AutoZyme reduced runtime by a median of 8.52-fold, with the largest reductions exceeding 676-fold. The optimized functions are distributed through AutoZyme-Library as drop-in replacements for existing analysis pipelines. We also release AutoZyme as a reusable framework for optimizing additional user-specified packages and functions.