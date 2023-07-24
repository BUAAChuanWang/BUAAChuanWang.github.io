---
layout:       post
title:        "Activation SWIGLU的介绍"
subtitle:     " \"时间是金\""
date:         2023-07-24 16:08:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - swiglu
    - activation
---

# RMS Norm

在深度学习中，"RMS NORM"通常指的是"Root Mean Square Norm"，即"均方根范数"。它是一种用于计算张量（例如神经网络中的权重或梯度）范数的方法。范数是一个向量或矩阵的长度或大小度量，它可以帮助了解张量的重要性或稳定性，并在优化算法中用于控制参数更新的速度或幅度。

Root Mean Square Norm的计算过程如下：

1. 计算张量的所有元素的平方：将张量中的每个元素都平方。

2. 计算所有平方元素的平均值：将上一步得到的平方元素相加，然后除以张量的元素数量，得到平方元素的平均值。

3. 取平均值的平方根：对上一步得到的平方元素的平均值取平方根，即得到RMS NORM。

RMS NORM的计算公式如下：

```
RMS NORM = sqrt( sum(x_i^2) / n )
```

其中，x_i 表示张量中的第 i 个元素，sum 表示求和运算，n 表示张量中的元素数量。

RMS NORM常用于优化算法中的梯度裁剪（Gradient Clipping）和权重衰减（Weight Decay）。在梯度裁剪中，如果模型的梯度范数超过了设定的阈值，就会对梯度进行缩放，以控制梯度的大小，避免梯度爆炸的问题。在权重衰减中，RMS NORM被用作正则化项的一部分，以限制模型的权重大小，防止过拟合。

总结起来，RMS NORM是一种范数计算方法，用于衡量张量的大小或稳定性，并在优化算法中起到控制梯度或权重的作用。