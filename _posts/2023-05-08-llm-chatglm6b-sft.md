---
layout:       post
title:        "【LLM】chatGLM-SFT记录"
subtitle:     " \"时间是金\""
date:         2023-05-11 13:18:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - peft
    - SFT
---

# 安装记录

## 安装torch
    
    # step1 proxy
    # 美团跳板机需要首先连接外网
    export http_proxy=http://10.22.139.49:6666
    export https_proxy=http://10.22.139.49:6666
    
    # step2 install
    # torch 1.13.1 cuda11.7
    pip install -i http://data-source-pip.sankuai.com/simple --trusted-host data-source-pip.sankuai.com torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117

    # torch 2.0
    pip install -i http://data-source-pip.sankuai.com/simple --trusted-host data-source-pip.sankuai.com torch==2.0.0+cu118 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
    


## 清华源（需要提前链接外网）
    # 添加proxy 
    export http_proxy=http://10.22.139.49:6666
    export https_proxy=http://10.22.139.49:6666
    
    #验证
    echo $http_proxy

    -i https://pypi.tuna.tsinghua.edu.cn/simple

# textgen安装
    
    

# peft安装

    # 1.安装accelerate
    git clone xxx.accelerate.git
    
    cd accelerate
    
    vi setup.cfg
    
    [easy_install]
    index_url = https://pypi.tuna.tsinghua.edu.cn/simple
    
    python setup.py install
    
    # 2.安装peft
    git clone xxx.pft.git
    
    cd peft
    
    touch setup.cfg
    
    vi setup.cfg
    
    [easy_install]
    index_url = https://pypi.tuna.tsinghua.edu.cn/simple
    
    python setup.py install