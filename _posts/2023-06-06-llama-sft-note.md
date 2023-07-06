---
layout:       post
title:        "【LLM】LLAMA-sft记录"
subtitle:     " \"时间是金\""
date:         2023-06-06 11:18:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - llama
    - SFT
---

# 一、背景目标

1. LLaMA是开源社区的主要研究模型，中文社区中LLaMA因为预训练阶段仅包含700个中文token导致中文预训练的匮乏，因此通常的做法是在LLaMA原生模型的基础上铜鼓哦扩充中文词表的方式做继续预训练。
2. 基于中文继续预训练后得到的模型，可以参与后续SFT/RM/RL stage的训练。
3. 目前中文继续预训练包括：崔一鸣的Chinese-LLaMA和 封神榜的Ziya模型 和Belle的13B-EXT
4. **特殊的：在原生LLaMA7B的基础上直接做中英文的SFT，在中文和英文的评测中获得非常好的效果（选择题），即在跨语言的理解层面得到了很强的对齐效果。**

-- 关于子牙 --
1. 没有提供预训练的学习率以及LR_Sceduler

# 二、下载

    export http_proxy=http://10.22.139.49:6666
    export https_proxy=http://10.22.139.49:6666

# 三、代码

基于Deepspeed-Chat进行多机多卡的训练

# 四、数据

    0.2294 merged
    0.1891 multiturn_chat
    0.1199 t0_fs_noopt.jsonlnew
    0.0884 search_jiaqi.txtnew
    0.0762 firefly
    0.0566 school_math
    0.0393 instruct
    0.0393 alpaca_data
    0.0391 instinwild
    0.0254 COIG_exam_instructions.jsonl
    0.0197 HC3_Human
    0.0191 HC3_Chinese_Human
    0.0191 HC3_Chinese_ChatGPT
    0.0173 alpaca_gpt4_data
    0.0164 alpaca_gpt4
    0.0047 COIG_leetcode_instructions.jsonl
    0.0012 COIG_human_value_alignment_instructions_part1.jsonl
