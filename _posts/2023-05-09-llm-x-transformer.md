---
layout:       post
title:        "【LLM】x-transformer 训练Speed UP！"
subtitle:     " \"时间是金\""
date:         2023-05-00 17:57:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - x-transformer
    - flash-attn
---

# 地址

https://github.com/lucidrains/x-transformers#flash-attention

# HBM 和 SRAM分别是什么？

ChatGPT：

    HBM和SRAM都是计算机内存类型，但它们在构造和用途上有很大的不同。
    
    HBM是“High Bandwidth Memory”的缩写，它是一种3D堆叠内存技术，它将高速DRAM存储器芯片垂直层叠在一起，形成多层堆叠，提供非常高的带宽和低能耗。HBM的设计使其能够在很短的时间内处理大量数据，因此适合用于需要大量数据传输的计算应用，如图形处理、机器学习等。
    
    SRAM是“Static Random Access Memory”的缩写，它是一种静态随机访问存储器，它使用逻辑门来存储每个位，并保持其状态，因此它不需要刷新。相比DRAM（动态随机访问存储器），SRAM的速度更快，但密度更低，因此成本更高。SRAM通常用于计算机的高速缓存和寄存器，因为它能够快速访问数据。
    
    总体而言，HBM和SRAM都是内存类型，但它们在构造和用途上有很大的不同。HBM适用于需要大量数据传输的计算应用，而SRAM适用于需要快速访问数据的高速缓存和寄存器。

# 自动评估

1. Microsoft-AGIEval

    https://github.com/microsoft/AGIEval

2. SuperCLUE（中文LLM版CLUE）

    https://github.com/CLUEbenchmark/SuperCLUE