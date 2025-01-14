---
layout:       post
title:        "【LLM】chatGLM6B的不同版本"
subtitle:     " \"时间是金\""
date:         2023-05-08 19:57:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - chatGLM
---

# 背景

# ChatGLM-6B 原版
## 介绍
ChatGLM-6B 是一个开源的、支持中英双语问答的对话语言模型，基于 [General Language Model (GLM)](https://github.com/THUDM/GLM) 架构，具有 62 亿参数。结合模型量化技术，用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）。ChatGLM-6B 使用了和 [ChatGLM](https://chatglm.cn) 相同的技术，针对中文问答和对话进行了优化。经过约 1T 标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，62 亿参数的 ChatGLM-6B 已经能生成相当符合人类偏好的回答。

# ChatGLM-6B-INT4-QE
## 介绍

ChatGLM-6B-INT4-QE 是 ChatGLM-6B 量化后的模型权重。具体的，ChatGLM-6B-INT4-QE 对 ChatGLM-6B 中的 28 个 GLM Block 、 Embedding 和 LM Head 进行了 INT4 量化。量化后的模型权重文件仅为 3G ，理论上 6G 显存（使用 CPU 即 6G 内存）即可推理，具有在嵌入式设备（如树莓派）上运行的可能。

在 CPU 上运行时，会根据硬件自动编译 CPU Kernel ，请确保已安装 GCC 和 OpenMP （Linux一般已安装，对于Windows则需手动安装），以获得最佳并行计算能力。

# ChatGLM-6B-Slim: 低显存版ChatGLM-6B
## 介绍
ChatGLM-6B-Slim是在[ChatGLM-6B](https://huggingface.co/THUDM/chatglm-6b)的基础上通过裁剪词表构建的。因为ChatGLM-6B使用了icetk，在其词表中，前20000个token是预留给图片的，在文本模型中没有用到这些图片token，但是在infer和微调的时候，这些token对应的embedding依然需要被加载，并且在解码每一个token的时候需要多计算20K个logits，会占用不少显存。因此将这一部分token裁剪掉以节省显存。

除了词表外，ChatGLM-6B-Slim的其他结构与ChatGLM-6B完全一致，性能也完全一样，可以认为是ChatGLM-6B的一个低显存版等价平替。

ChatGLM-6B 是一个开源的、支持中英双语问答的对话语言模型，基于 [General Language Model (GLM)](https://github.com/THUDM/GLM) 架构，具有 62 亿参数。结合模型量化技术，用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）。ChatGLM-6B 使用了和 [ChatGLM](https://chatglm.cn) 相同的技术，针对中文问答和对话进行了优化。经过约 1T 标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，62 亿参数的 ChatGLM-6B 已经能生成相当符合人类偏好的回答。

## 软件依赖

```shell
pip install protobuf==3.20.0 transformers==4.26.1 icetk cpm_kernels
```

## 代码调用

可以通过如下代码调用 ChatGLM-6B-Slim 模型来生成对话：

```ipython
>>> from transformers import AutoTokenizer, AutoModel
>>> tokenizer = AutoTokenizer.from_pretrained("silver/chatglm-6b-slim", trust_remote_code=True)
>>> model = AutoModel.from_pretrained("silver/chatglm-6b-slim", trust_remote_code=True).half().cuda()
>>> response, history = model.chat(tokenizer, "你好", history=[])
>>> print(response)
你好👋!我是人工智能助手 ChatGLM-6B,很高兴见到你,欢迎问我任何问题。
>>> response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
>>> print(response)
晚上睡不着可能会让你感到焦虑或不舒服,但以下是一些可以帮助你入睡的方法:

1. 制定规律的睡眠时间表:保持规律的睡眠时间表可以帮助你建立健康的睡眠习惯,使你更容易入睡。尽量在每天的相同时间上床,并在同一时间起床。
2. 创造一个舒适的睡眠环境:确保睡眠环境舒适,安静,黑暗且温度适宜。可以使用舒适的床上用品,并保持房间通风。
3. 放松身心:在睡前做些放松的活动,例如泡个热水澡,听些轻柔的音乐,阅读一些有趣的书籍等,有助于缓解紧张和焦虑,使你更容易入睡。
4. 避免饮用含有咖啡因的饮料:咖啡因是一种刺激性物质,会影响你的睡眠质量。尽量避免在睡前饮用含有咖啡因的饮料,例如咖啡,茶和可乐。
5. 避免在床上做与睡眠无关的事情:在床上做些与睡眠无关的事情,例如看电影,玩游戏或工作等,可能会干扰你的睡眠。
6. 尝试呼吸技巧:深呼吸是一种放松技巧,可以帮助你缓解紧张和焦虑,使你更容易入睡。试着慢慢吸气,保持几秒钟,然后缓慢呼气。

如果这些方法无法帮助你入睡,你可以考虑咨询医生或睡眠专家,寻求进一步的建议。
```

关于更多的使用说明，包括如何运行命令行和网页版本的 DEMO，以及使用模型量化以节省显存，请参考我们的 [Github Repo](https://github.com/THUDM/ChatGLM-6B)。