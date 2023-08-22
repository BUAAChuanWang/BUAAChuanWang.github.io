---
layout:       post
title:        "GPT generate output fix Note"
subtitle:     " \"时间是金\""
date:         2023-07-25 12:08:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - generate
---

# 目的

为了让GPT在每次生成时都保持一致的结果，需要使用CUDNN的设置，仅使用torch.seed是不生效的。

# code

    os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
    torch.use_deterministic_algorithms(True)
    # Enable CUDNN deterministic mode
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
