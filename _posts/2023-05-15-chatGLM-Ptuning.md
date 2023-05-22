---
layout:       post
title:        "chatGLM P-Tuning V2 SFT记录"
subtitle:     " \"时间是金\""
date:         2023-05-15 11:30:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - chatGLM
    - SFT
    - P-Tuning V2
---

# BUGS

1. wandb 

   BUGS：PermissionError: [Errno 13] Permission denied: '/var/run/secrets/kubernetes.io/serviceaccount/token'

    解决：ptuning/main.py中添加

   os.environ["WANDB_DISABLED"] = "true"

2. ChatGLMTokenizer


    Traceback (most recent call last):
      File "main.py", line 433, in <module>
        main()
      File "main.py", line 114, in main
        tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path, trust_remote_code=True)
      File "/usr/local/conda/envs/llm_fine_tune/lib/python3.8/site-packages/transformers/models/auto/tokenization_auto.py", line 686, in from_pretrained
        tokenizer_class = get_class_from_dynamic_module(
      File "/usr/local/conda/envs/llm_fine_tune/lib/python3.8/site-packages/transformers/dynamic_module_utils.py", line 388, in get_class_from_dynamic_module
        return get_class_in_module(class_name, final_module.replace(".py", ""))
      File "/usr/local/conda/envs/llm_fine_tune/lib/python3.8/site-packages/transformers/dynamic_module_utils.py", line 158, in get_class_in_module
        return getattr(module, class_name)
    AttributeError: module 'transformers_modules.chatglm-6b.tokenization_chatglm' has no attribute 'ChatGLMTokenizer'

解决方案：

    rm -rf ~/.cache/huggingface


参考：
https://github.com/THUDM/ChatGLM-6B/issues/102

根本解决方案：

    pip install git+https://github.com/huggingface/transformers
    
参考：
https://github.com/THUDM/ChatGLM-6B/issues/592