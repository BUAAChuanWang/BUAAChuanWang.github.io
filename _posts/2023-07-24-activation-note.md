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

https://zhuanlan.zhihu.com/p/621058772

# activation functions

SWISH（或称为SWIGLU）是一种激活函数，而GLU（Gated Linear Unit）、ReLU（Rectified Linear Unit）、Sigmoid和Tanh也都是深度学习中常见的激活函数。它们在神经网络中用于引入非线性性，使得模型可以学习复杂的非线性关系。下面将详细介绍每个激活函数的特点和区别：

SWISH（SWIGLU）激活函数：
SWISH是"Swish Activation"的缩写，也被称为Swish-Gated Linear Unit（SWIGLU）。它由Google在2017年提出，其公式如下：

f(x) = x * sigmoid(x)

SWISH激活函数结合了线性操作和Sigmoid操作。它具有Sigmoid函数的非线性性，同时又包含线性操作，这使得它相对于ReLU等激活函数更平滑，有助于减轻梯度消失问题。SWISH在一些深度学习任务中表现良好，但在其他任务中可能不如其他激活函数效果好，因此在实际应用中需要根据具体问题进行选择。

GLU（Gated Linear Unit）激活函数：
GLU是"Gated Linear Unit"的缩写。它最初是由Google在2017年提出，用于自然语言处理（NLP）领域中的一种模型结构Transformer。其公式如下：

f(x) = x * sigmoid(x)

GLU激活函数和SWISH的公式相同，但是GLU通常用于特定的神经网络层或模型结构，如Transformer的编码器中。GLU通过门控机制，使得输入信号在经过Sigmoid激活后与原始输入进行点积操作，从而实现特定的特征选择和过滤。

ReLU（Rectified Linear Unit）激活函数：
ReLU是深度学习中最常用的激活函数之一。它的公式如下：

f(x) = max(0, x)

简单来说，ReLU将所有小于零的输入值设置为零，而大于零的输入值保持不变。这使得ReLU具有非常简单和高效的计算，同时也帮助解决了梯度消失问题。然而，ReLU对负数输入的输出恒为零，可能导致“神经元死亡”问题，在反向传播过程中，这些神经元的梯度将永远为零，无法更新参数。

Sigmoid激活函数：
Sigmoid函数的公式如下：

f(x) = 1 / (1 + exp(-x))

Sigmoid函数将输入映射到0和1之间的范围，具有平滑的S形曲线。在过去，Sigmoid函数在神经网络中被广泛使用，但它也存在梯度消失的问题。当输入较大或较小时，Sigmoid函数的导数接近于零，导致梯度消失。因此，在深度学习中，Sigmoid函数现在主要用于二元分类任务的输出层，而不再被普遍作为隐藏层的激活函数。

Tanh激活函数：
Tanh函数的公式如下：

f(x) = (2 / (1 + exp(-2x))) - 1

Tanh函数类似于Sigmoid函数，但它将输入映射到-1和1之间的范围。与Sigmoid函数相比，Tanh函数的输出范围更广，均值接近零，具有更好的中心化特性。然而，Tanh函数也存在梯度消失的问题，尤其是在输入较大或较小的情况下。

在选择激活函数时，通常需要根据具体的任务和模型结构进行权衡。ReLU是目前最常用的激活函数之一，但在某些情况下，SWISH、GLU或其他激活函数可能表现更好，因此需要进行实验和调整以找到最适合的激活函数。