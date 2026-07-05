---
title: Client-server interfaces enable efficient agent-driven variant calling
title_zh: 客户端-服务器接口实现高效的智能体驱动变异检测
authors: "Yu, X., Zheng, Z., CHEN, L., QIn, Z., Guo, X., He, M., Luo, R."
date: 2026-06-28
pdf: "https://www.biorxiv.org/content/10.64898/2026.06.25.734665v1.full.pdf"
tags: ["query:mlsys"]
score: 6.0
evidence: 将深度学习变异检测工具重构为客户端-服务器系统，以便LLM智能体自动化
tldr: "目前LLM代理越来越多地自动化生物信息分析，但传统工具为人类专家独立使用而设计，代理驱动时需要反复推理配置，耗费大量回合和令牌，结果可靠性低。为此，将Clair3重构成客户端-服务器系统Clair3-Connect，客户端进行基因组处理并持有可识别数据，服务器仅执行神经网络推理，客户端发送特征张量，并暴露由模式定义的代理工具，通过单次结构化调用完成。在APOE二倍型分型任务上，60次代理运行全部正确，工具调用消耗12K令牌、3个回合，比基于shell的基线节省6.8至14倍令牌，运行时间约四分之一，令牌使用变异仅4%远低于35%，且在50倍覆盖度下SNP F1仅下降0.1-0.3，加密额外耗时7.2%。说明将现有算法重构为开发者内置的代理工具，结合安全边界，比第三方包装更高效可靠，代理接口应成为生物信息学工具的一等交付物。"
source: biorxiv
selection_source: fresh_fetch
motivation: 现有生物信息学工具缺乏面向LLM代理的接口，代理需耗费大量回合和令牌去理解并使用，效率低下且不稳定。
method: 重构Clair3为客户端-服务器系统Clair3-Connect，客户端保留数据并定义代理可调用的工具，服务器完成推理，通过单次结构化调用执行。
result: "代理工具仅需12K令牌和3回合，比shell方式少6.8-14倍，运行时间约四分之一，令牌使用变异仅4%远低于35%，且F1损失极小。"
conclusion: 将现有算法重构为代理工具可使其在代理驱动下更高效、可靠，应成为生物信息学工具交付的重要组成部分。
---

## 摘要
背景：大语言模型（LLM）智能体正日益自动化生物信息学分析，但现有大多数生物信息学工具是为人类专家独立使用而构建的。智能体驱动此类工具时，必须根据面向人类的文档推理其安装、配置和执行，每个结果需要花费大量回合、令牌和工具调用。因此，方法对智能体的暴露方式可能与方法本身一样重要。通过为这些工具设计智能体接口，智能体可以减少此类开销，提高智能体驱动分析的可靠性。

发现：为了验证这一设计，我们将广泛使用的基于深度学习的长读长变异检测工具 Clair3 重构为客户端-服务器系统 Clair3-Connect。客户端执行所有基因组学相关处理并保留可识别数据。服务器仅运行神经网络推理，客户端仅向服务器发送特征张量，样本标识符和基因组上下文保留在客户端。客户端暴露由模式定义的面向智能体的工具，智能体通过单一结构化调用即可调用这些工具。在一项 APOE 双倍体分型任务中，所有 60 次智能体运行均正确无误。智能体工具使用 3 轮 12K 令牌，比基于 shell 的基线（81K-163K 令牌）少 6.8 至 14 倍，挂钟时间约为四分之一，且稳定性大大提高（令牌使用变异 4% 对比 35%）。为保持客户端轻量化而舍弃堆叠和定相阶段后，在 50 倍覆盖度下，SNP F1 值比标准 Clair3 低 0.1-0.3 个点，而双向 TLS 和 AES-256-GCM 加密使端到端运行时间增加了 7.2%。

结论：将成熟算法重构为安全客户端-服务器边界背后的开发者构建的智能体工具，比第三方封装器更高效、更可靠、更易于 LLM 智能体部署，因为第三方封装器无法恢复只有开发者才知道的默认值和约定。智能体接口应成为生物信息学工具开发的一级交付物。

## Abstract
BackgroundLarge language model (LLM) agents increasingly automate bioinformatics analyses, but most existing bioinformatics tools were built for standalone use by human experts. An agent driving such a tool must reason about its installation, configuration, and execution from documentation for human, spending many turns, tokens, and tool calls per result. How a method is exposed to an agent can therefore matter as much as the method itself. By designing agentic interfaces for these tools, agent can reduce such overhead and improve the reliability of agent-driven analyses.

FindingsTo test this design, we re-architected Clair3, a widely used deep-learning-based long-read variant caller, into a client-server system, Clair3-Connect. The client performs all genomics related processing and holds the identifiable data. The server runs only neural-network inference, and the client sends only feature tensors to the server, while sample identifiers and genomic context remain on the client. The client exposes schema-defined agent-facing tools that an agent invokes through single structured calls. On an APOE diplotyping task, all 60 agent runs were correct. The agentic tools used 12K tokens in 3 turns, 6.8 to 14 times fewer tokens than the shell-driven baselines (81K-163K tokens), at about a quarter the wall-clock time and far more stably (4% versus 35% token usage variation). Dropping the pileup and phasing stages to keep the client light left SNP F1 within 0.1-0.3 points of standard Clair3 by 50x coverage, while mutual TLS and AES-256-GCM encryption added 7.2% to end-to-end runtime.

ConclusionsRecasting an established algorithm as developer-built, agentic tools behind a secure client-server boundary makes it more efficient, reliable, and easier to deploy for an LLM agent than a third-party wrapper, which cannot recover the defaults and conventions only its developers know. Agentic interfaces should be a first-class deliverable of bioinformatics tool development.