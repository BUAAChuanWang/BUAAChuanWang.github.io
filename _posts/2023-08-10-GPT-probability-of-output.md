---
layout:       post
title:        "GPT-probability of output Note"
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

discuss

https://discuss.huggingface.co/t/announcement-generation-get-probabilities-for-generated-output/30075

color

https://huggingface.co/spaces/joaogante/color-coded-text-generation

# generate

https://huggingface.co/blog/zh/how-to-generate

# code

transformers==4.23.1时没有compute_transition_scores，在更高版本4.31.0找到源码后，稍微改一下就行。

    from typing import Tuple, Optional
    import numpy as np
    
    def compute_transition_scores(
    #     self,
        model,
        sequences: torch.Tensor,
        scores: Tuple[torch.Tensor],
        beam_indices: Optional[torch.Tensor] = None,
        normalize_logits: bool = False,
    ) -> torch.Tensor:
        """
        Computes the transition scores of sequences given the generation scores (and beam indices, if beam search was
        used). This is a convenient method to quicky obtain the scores of the selected tokens at generation time.
    
        Parameters:
            sequences (`torch.LongTensor`):
                The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or
                shorter if all batches finished early due to the `eos_token_id`.
            scores (`tuple(torch.FloatTensor)`):
                Transition scores for each vocabulary token at each generation step. Beam transition scores consisting
                of log probabilities of tokens conditioned on log softmax of previously generated tokens Tuple of
                `torch.FloatTensor` with up to `max_new_tokens` elements (one element for each generated token), with
                each tensor of shape `(batch_size*num_beams, config.vocab_size)`.
            beam_indices (`torch.LongTensor`, *optional*):
                Beam indices of generated token id at each generation step. `torch.LongTensor` of shape
                `(batch_size*num_return_sequences, sequence_length)`. Only required if a `num_beams>1` at
                generate-time.
            normalize_logits (`bool`, *optional*, defaults to `False`):
                Whether to normalize the logits (which, for legacy reasons, may be unnormalized).
    
        Return:
            `torch.Tensor`: A `torch.Tensor` of shape `(batch_size*num_return_sequences, sequence_length)` containing
                the transition scores (logits)
    
        Examples:
    
        ```python
        >>> from transformers import GPT2Tokenizer, AutoModelForCausalLM
        >>> import numpy as np
    
        >>> tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        >>> model = AutoModelForCausalLM.from_pretrained("gpt2")
        >>> tokenizer.pad_token_id = tokenizer.eos_token_id
        >>> inputs = tokenizer(["Today is"], return_tensors="pt")
    
        >>> # Example 1: Print the scores for each token generated with Greedy Search
        >>> outputs = model.generate(**inputs, max_new_tokens=5, return_dict_in_generate=True, output_scores=True)
        >>> transition_scores = model.compute_transition_scores(
        ...     outputs.sequences, outputs.scores, normalize_logits=True
        ... )
        >>> # input_length is the length of the input prompt for decoder-only models, like the GPT family, and 1 for
        >>> # encoder-decoder models, like BART or T5.
        >>> input_length = 1 if model.config.is_encoder_decoder else inputs.input_ids.shape[1]
        >>> generated_tokens = outputs.sequences[:, input_length:]
        >>> for tok, score in zip(generated_tokens[0], transition_scores[0]):
        ...     # | token | token string | logits | probability
        ...     print(f"| {tok:5d} | {tokenizer.decode(tok):8s} | {score.numpy():.3f} | {np.exp(score.numpy()):.2%}")
        |   262 |  the     | -1.414 | 24.33%
        |  1110 |  day     | -2.609 | 7.36%
        |   618 |  when    | -2.010 | 13.40%
        |   356 |  we      | -1.859 | 15.58%
        |   460 |  can     | -2.508 | 8.14%
    
        >>> # Example 2: Reconstruct the sequence scores from Beam Search
        >>> outputs = model.generate(
        ...     **inputs,
        ...     max_new_tokens=5,
        ...     num_beams=4,
        ...     num_return_sequences=4,
        ...     return_dict_in_generate=True,
        ...     output_scores=True,
        ... )
        >>> transition_scores = model.compute_transition_scores(
        ...     outputs.sequences, outputs.scores, outputs.beam_indices, normalize_logits=False
        ... )
        >>> # If you sum the generated tokens' scores and apply the length penalty, you'll get the sequence scores.
        >>> # Tip: recomputing the scores is only guaranteed to match with `normalize_logits=False`. Depending on the
        >>> # use case, you might want to recompute it with `normalize_logits=True`.
        >>> output_length = input_length + np.sum(transition_scores.numpy() < 0, axis=1)
        >>> length_penalty = model.generation_config.length_penalty
        >>> reconstructed_scores = transition_scores.sum(axis=1) / (output_length**length_penalty)
        >>> print(np.allclose(outputs.sequences_scores, reconstructed_scores))
        True
        ```"""
        # 1. In absence of `beam_indices`, we can assume that we come from e.g. greedy search, which is equivalent
        # to a beam search approach were the first (and only) beam is always selected
        if beam_indices is None:
            beam_indices = torch.arange(scores[0].shape[0]).view(-1, 1).to(sequences.device)
            beam_indices = beam_indices.expand(-1, len(scores))
    
        # 2. reshape scores as [batch_size*vocab_size, # generation steps] with # generation steps being
        # seq_len - input_length
        scores = torch.stack(scores).reshape(len(scores), -1).transpose(0, 1)
    
        # 3. Optionally normalize the logits (across the vocab dimension)
        if normalize_logits:
            scores = scores.reshape(-1, model.config.vocab_size, scores.shape[-1])
            scores = torch.nn.functional.log_softmax(scores, dim=1)
            scores = scores.reshape(-1, scores.shape[-1])
    
        # 4. cut beam_indices to longest beam length
        beam_indices_mask = beam_indices < 0
        max_beam_length = (1 - beam_indices_mask.long()).sum(-1).max()
        beam_indices = beam_indices.clone()[:, :max_beam_length]
        beam_indices_mask = beam_indices_mask[:, :max_beam_length]
    
        # 5. Set indices of beams that finished early to 0; such indices will be masked correctly afterwards
        beam_indices[beam_indices_mask] = 0
    
        # 6. multiply beam_indices with vocab size to gather correctly from scores
        beam_sequence_indices = beam_indices * model.config.vocab_size
    
        # 7. Define which indices contributed to scores
        cut_idx = sequences.shape[-1] - max_beam_length
        indices = sequences[:, cut_idx:] + beam_sequence_indices
    
        # 8. Compute scores
        transition_scores = scores.gather(0, indices)
    
        # 9. Mask out transition_scores of beams that stopped early
        transition_scores[beam_indices_mask] = 0
    
        return transition_scores


推理：

    MAX_LENGTH = 2048
    
    
    def inference_with_logits(input: str, temperature=0.55, top_p=0.55, max_new_tokens=128, top_k=None, num_return_sequences=1, min_length=None, no_repeat_ngram_size=None) -> str:
        inputs = tokenizer([input], max_length=MAX_LENGTH, truncation=True, return_tensors="pt").to("cuda:0")
        inputs["input_ids"] = inputs["input_ids"][:, -MAX_LENGTH:]
        
        outputs =model.generate(
            **inputs, 
            max_new_tokens=max_new_tokens, 
            min_length=min_length, 
            do_sample = True, 
            top_k=top_k, 
            top_p = top_p, 
            temperature = temperature, 
    #         repetition_penalty=1.2, 
    #         no_repeat_ngram_size=3, 
            num_return_sequences=num_return_sequences, 
            eos_token_id=2, 
            bos_token_id=1, 
            pad_token_id=0,
            no_repeat_ngram_size=no_repeat_ngram_size,
    #         use_cache=True,  # 加速
            return_dict_in_generate=True, 
            output_scores=True, 
        )
        
        input_length = inputs.input_ids.shape[-1]
        print(f"input_length {input_length}")
    #     print(f"outputs :{outputs}")
        print(f"outputs.sequences: {outputs.sequences.shape} {outputs.sequences}")
        print(f"outputs.scores: {len(outputs.scores)}*{outputs.scores[0].shape}")
        print(f"outputs.scores:{outputs.scores}")
        
        results = []
        lengths = []
        for i, beam_output in enumerate(outputs.sequences):
            output = tokenizer.decode(beam_output[input_length:])
    #         results.append(tokenizer.decode(beam_output[input_length:]))
            results.append(tokenizer.decode(beam_output)[len(input):].replace("</s>", "").replace("<unk>", "").replace("<pad>", "").strip())
            lengths.append(len(output.replace("<unk>", "").replace("<pad>", "")))
        
        transition_scores = compute_transition_scores(
            model, outputs.sequences, outputs.scores, normalize_logits=True
        )
        transition_scores = transition_scores.cpu()
        generated_tokens = outputs.sequences[:, input_length:].cpu()
        print(f"transition_scores :{transition_scores.shape}, generated_tokens :{generated_tokens.shape}")
        scores = []
        toks = []
        for tok, score in zip(generated_tokens[0], transition_scores[0]):
            # | token | token string | logits | probability
            print(f"| {tok:5d} | {tokenizer.decode(tok):8s} | {score.numpy():.3f} | {np.exp(score.numpy()):.2%}")
            scores.append(np.exp(score.numpy()))
            toks.append(tokenizer.decode(tok))
        print(f"np.array(scores).sum() :{np.array(scores).sum()}")
    
        print(f"torch.exp(transition_scores).sum() :{torch.exp(transition_scores).sum()}")
    
        print(f"np.array(scores).sum()/len(scores): {np.array(scores).sum()/len(scores)}")
        print(f"transition_scores.exp().sum(axis=1): {transition_scores.exp().sum(axis=1).shape} {transition_scores.exp().sum(axis=1)}")
        print(f"torch.tensor(lengths): {torch.tensor(lengths).shape} {torch.tensor(lengths)}")
        num_scores = transition_scores.exp().sum(axis=1)/torch.tensor(lengths)
        print(f"num_scores: {num_scores}")
    
        
        return results

测试：

    idx = 38
    
    input = singleturn_input(test["inputs"].values[idx])
    input = singleturn_input("Human:请问三文鱼怎么吃?")
    
    
    inference_with_logits(input=input, num_return_sequences=3)