---
layout:       post
title:        "Multi-Query-Attention"
subtitle:     " \"时间是金\""
date:         2023-06-27 15:08:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - LLM
    - NLP
    - ChatGLM2
    - Multi-Query-Attention
---

# 背景

ChatGLM2中提到了训练和推理的加速，主要为X-transformer中的Flash Attention技术和Multi-Query-Attention技术。

本文主要记录Multi-Query-Attention的原理。

# MQA

- 在标准Transformer中使用的k 个注意力头，也就意味着Q、K、V三个矩阵的shape都是[k, h]，其中h的head数量。在PaLM中，K、V是共享的，并且维度变成[1,h]。Q仍然是[k, h]。这样做可以减少自回归解码的时间，同时对模型性能不会有太大的影响。
- 对训练速度和效果没什么影响，但却提升了decode的速度

1. 是原本多头的简化版，现在所有头都复用相同的key value，只有query还是每个头自己独立生成。

2. 看chatglm6b-v2的代码，就是query保持不变，key和value分块。然后丢到里面计算
    
    
    if self.multi_query_attention:
            key_layer = key_layer.unsqueeze(-2)
            key_layer = key_layer.expand(
                -1, -1, -1, self.num_attention_heads_per_partition // self.num_multi_query_groups_per_partition, -1
            )
            key_layer = key_layer.contiguous().view(
                key_layer.size()[:2] + (self.num_attention_heads_per_partition, self.hidden_size_per_attention_head)
            )
            value_layer = value_layer.unsqueeze(-2)
            value_layer = value_layer.expand(
                -1, -1, -1, self.num_attention_heads_per_partition // self.num_multi_query_groups_per_partition, -1
            )
            value_layer = value_layer.contiguous().view(
                value_layer.size()[:2] + (self.num_attention_heads_per_partition, self.hidden_size_per_attention_head)
            )

        # ==================================
        # core attention computation
        # ==================================

        context_layer = self.core_attention(query_layer, key_layer, value_layer, attention_mask)

3. falcon-7b模型也是这么做的


    if alibi is None:
        query_layer_ = query_layer.reshape(batch_size, self.num_heads, -1, self.head_dim)
        key_layer_ = key_layer.reshape(batch_size, self.num_kv, -1, self.head_dim)
        value_layer_ = value_layer.reshape(batch_size, self.num_kv, -1, self.head_dim)

        attn_output = F.scaled_dot_product_attention(
            query_layer_, key_layer_, value_layer_, None, 0.0, is_causal=True
        )

        x = attn_output.view(batch_size, self.num_heads, q_length, self.head_dim)
        x = x.permute(0, 2, 1, 3)
        attn_output = x.reshape(batch_size, q_length, self.num_heads * self.head_dim)

        output_tensor = self.dense(attn_output)

        outputs = (output_tensor, present)
        assert not output_attentions  # not supported.
        return outputs    