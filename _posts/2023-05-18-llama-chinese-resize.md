---
layout:       post
title:        "Chinese Llama 原理"
subtitle:     " \"时间是金\""
date:         2023-05-18 10:28:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - BLOOM
    - SFT
    - Megatron-Deepspeed
---

# Llama

llama是meta发布的预训练模型，但是巨大的预训练预料中仅有700多个中文token，因此没有中文语料的预训练无法再中文领域应用。

- **Chinese Llama**

    中文llama的常见做法是对llama模型embedding层做中文此表的扩充，做相应的中文语料的继续预训练。

# 如何新增中文语料

    
    def resize_model_embeddings(self, tokenizer_vocab_size):
        """Resizes model embeddings to match the tokenizer vocab size."""
        model_vocab_size = self.model.get_input_embeddings().weight.size(0)
        if model_vocab_size != tokenizer_vocab_size:
            logger.debug(
                f"Resize model embeddings to fit tokenizer, "
                f"Vocab of the base model: {model_vocab_size}, "
                f"Vocab of the tokenizer: {tokenizer_vocab_size}"
            )
            self.model.resize_token_embeddings(tokenizer_vocab_size)
            assert self.model.get_input_embeddings().weight.size(0) == len(self.tokenizer)
            logger.debug(f"Model token embeddings updated, size: {len(self.tokenizer)}")