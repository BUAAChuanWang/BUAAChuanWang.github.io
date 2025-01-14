---
layout:       post
title:        "Flash-Attention Note"
subtitle:     " \"时间是金\""
date:         2023-07-25 12:08:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - Flash-Attention1
    - Flash-Attention2
---

https://zhuanlan.zhihu.com/p/626079753

# Flash-Attention原理

FA与MHA在算法原理上无差异，FA是MHA的计算效率优化版，其核心在于通过拆分QKV矩阵与按行计算Softmax在SRAM上，通过内外双循环的方式将计算不断的从HBM读取到SRAM上计算再存在HBM上，从而充分加速运算效率，提高Attention的计算速度，这一切对于用户是无感的。

## 内循环与外循环

参考FA的论文介绍，对于K、V的拆分是外循环，对于Q的拆分是内循环，一般而言，外循环次数较少 如2，内循环次数较多 如16，这与N(SEQLEN)和d(numHEAD)有关。

## HBM和SRAM

HBM(high band memory)高带宽内存，HBM容量大但访问速度较慢，可以理解为GPU的显存。如A100 80G的HBM为80G。

SRAM(static random-access memory)静态随机存取内存，GPU上的超高速计算器，SRAM容量小但速度快，比HBM快一个数量级，大小 如192KB。

## 举例

可以参考知乎https://zhuanlan.zhihu.com/p/639362627

# Flash-Attention 2

https://zhuanlan.zhihu.com/p/645627275

FA2相比FA1的重要区别是，FA2中将Q的切分也放在了外循环，这样每次外循环都可以计算输出一个结果块 $O_i$ （即 $softmax(QK^TV)$ ），不需要像FA1一样Q在内循环 O_i不是一次性出来，而每次外循环都要重新导HBM里面去上次O_i-1 的结果来做rescaling

# flash-attn 1/2 安装

    export http_proxy=http://10.22.139.49:6666
    export https_proxy=http://10.22.139.49:6666
    -i https://pypi.tuna.tsinghua.edu.cn/simple
    
    pip install packaging
    pip install ninja
    ninja --version
    echo $?  # should return exit code 0)
    conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia  # 确保cuda>=11.4
    pip install flash-attn --no-build-isolation
    
    # 此外还有两个提速，可以参考QWen7B 和 Flash-Attn github介绍
    # flash-attn rotary
    "Warning: import flash_attn rotary fail, please install FlashAttention rotary to get higher efficiency "
    "https://github.com/Dao-AILab/flash-attention/tree/main/csrc/rotary"
    # flash-attn layer_norm
    "Warning: import flash_attn rms_norm fail, please install FlashAttention layer_norm to get higher efficiency "
    "https://github.com/Dao-AILab/flash-attention/tree/main/csrc/layer_norm"
    
    cd flash-attention/csrc/rotary
    python setup.py install
    cd flash-attention/csrc/layer_norm
    python setup.py install