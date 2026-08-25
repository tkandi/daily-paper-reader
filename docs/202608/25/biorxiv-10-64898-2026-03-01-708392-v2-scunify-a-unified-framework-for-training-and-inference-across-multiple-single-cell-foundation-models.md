---
title: "scUnify: a unified framework for training and inference across multiple single-cell foundation models"
title_zh: scUnify：一个跨多个单细胞基础模型进行训练和推理的统一框架
authors: "KIM, D., Hong, A., Jeong, K., KIM, K."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.01.708392v2.full.pdf"
tags: ["query:mlsys"]
score: 6.0
evidence: 跨多个基础模型的统一训练与推理框架，组件可复用
tldr: 不同单细胞基础模型在软件需求和下游任务性能上表现差异显著，严重阻碍了系统比较与复用。scUnify提出一个统一框架，将模型特定训练器、下游任务和适应策略解耦为可重用组件，并保留各骨干必要处理。在五个scFMs上复现原始工作流，扩展多种参数高效微调方法，并演示自定义任务的可扩展连接。该框架使研究人员能在统一流程内系统比较各组合并扩展自定义任务。
source: biorxiv
selection_source: fresh_fetch
motivation: 现有单细胞基础模型在软件需求和下游任务性能上差异大，难以系统比较与复用。
method: scUnify将模型特定训练器、下游任务和适应策略解耦为可重用组件，并保留各骨干的必要处理。
result: 在五个scFMs上复现原始工作流，扩展多种参数高效微调方法，并展示自定义任务的可扩展连接。
conclusion: scUnify使研究人员能够在统一流程中系统比较各种组合，并扩展自定义任务等。
---

## 摘要
单细胞基础模型（scFMs）在软件需求以及下游任务和适应策略中的性能各不相同，这给比较和复用带来了困难。我们提出了 scUnify，该框架在保留每个骨干网络所需处理流程的同时，将模型特定的训练器、下游任务和适应策略分离为可复用组件。在五个 scFMs 上，scUnify 复现了原始推理和训练工作流，通过多种参数高效微调方法扩展了模型原生任务，并通过将一个新实现的可定制训练任务连接到多个骨干网络和适应策略，展示了其可扩展性。综合来看，这些能力使研究人员能够在统一工作流中系统比较这些组合，并在异构 scFMs 之间扩展定制任务。

## Abstract
Single-cell foundation models (scFMs) differ in software requirements and performance across downstream tasks and adaptation strategies, complicating comparison and reuse. We present scUnify, a framework that preserves each backbone's required processing while separating model-specific trainers, downstream tasks, and adaptation strategies as reusable components. Across five scFMs, scUnify reproduced original inference and training workflows, extended model-native tasks with multiple parameter-efficient fine-tuning methods, and demonstrated extensibility by connecting a newly implemented custom trainable task to multiple backbones and adaptation strategies. Together, these capabilities enable researchers to systematically compare these combinations and extend custom tasks across heterogeneous scFMs within a common workflow.