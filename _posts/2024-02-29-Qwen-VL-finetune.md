---
layout:       post
title:        "多模态：Qwen-VL/Qwen-VL-Chat MultiNode Finetune Note"
subtitle:     " \"时间是金\""
date:         2024-02-29 15:38:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - VL
    - Qwen-VL
    - finetune
---

# 背景

美团AI社交Wow APP已在LLM文本对话方面有稳定成果，为拓展更丰富更具吸引力的玩法，自研多模态能力的建设成为高优方向。

本文主要Focus 开源Qwen-VL以及Qwen-VL-Chat的多机多卡全参数微调。

# 实验报告

## 实验SOP

***实验依赖官方的Code修改，使得能够在多机多卡运行，如8机*8卡 共64卡运行。***

1. git clone (code and model)
2. 环境设置

   ```linux
   # torch安装
   pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1
   
   # deepspeed 和 peft 安装
   pip install deepspeed peft
   
   # 基本安装项目 参考requirements.txt
   pip install -r requirements.txt
   ```
   
3. 多机多卡环境代码
   ```shell
   NNODES=`python parse_environment.py nnodes`
   MASTER_ADDR=`python parse_environment.py master_addr`
   MASTER_PORT=`python parse_environment.py master_port`
   GPUS_PER_NODE=`python parse_environment.py nproc_per_node`
   NODE_RANK=`python parse_environment.py node_rank`
   echo NNODES:${NNODES}
   echo MASTER_ADDR:${MASTER_ADDR}
   echo MASTER_PORT:${MASTER_PORT}
   echo GPUS_PER_NODE:${GPUS_PER_NODE}
   echo NODE_RANK:${NODE_RANK}
   ```
   
4. 修改torchrun为内网服务器可访问地址
   ```shell
   /mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai-llms/users/x/env/chuan_vl/bin/torchrun $DISTRIBUTED_ARGS finetune.py \
    --model_name_or_path $MODEL \
    --data_path $DATA \
    --bf16 True \
    --fix_vit True \
    --output_dir ${output_dir} \
    --num_train_epochs 3 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 30 \
    --save_total_limit 3 \
    --learning_rate 1e-5 \
    --weight_decay 0.1 \
    --adam_beta2 0.95 \
    --warmup_ratio 0.01 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --report_to "none" \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --lazy_preprocess True \
    --deepspeed finetune/ds_config_zero3.json
   ```

5. hope提交

   ```linux
   # 1. 单独新建hope 文件夹 和 results文件夹 用于存放hope命令和模型结果
   mkdir hopes, results
   hope init ml-easy-job Qwen-VL-finetune
   
   # 提前复制finetune_ds.sh 到当前目录下的run.sh
   hope run Qwen-VL-finetune.hope
   ```
## 问题与解决

1. RuntimeError: "erfinv_cuda" not implemented for 'BFloat16'

    ```python
   # BUG https://mlp.sankuai.com/ml/#/job/logv2/task?from=job&jobId=psx58vxqjpjsdhm&roleName=Worker&taskId=0&attemptId=psx58vxqjpjsdhm-worker-0-1&fileName=stderr
   File "/home/hadoop-mtai-llms/.cache/huggingface/modules/transformers_modules/Qwen-VL/visual.py", line 118, in __init__
        trunc_normal_(self.query, std=.02)
      File "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai-llms/users/wangchuan16/env/chuan_vl/lib/python3.10/site-packages/torch/nn/init.py", line 176, in trunc_normal_
        tensor.erfinv_()
    RuntimeError: "erfinv_cuda" not implemented for 'BFloat16'
    ```
   
    ```python
    # 1. 修改bf16 为 fp16，扔报错 https://mlp.sankuai.com/ml/#/job/logv2/task?from=job&jobId=psx581xqjpjsdhm&roleName=Worker&taskId=0&attemptId=psx581xqjpjsdhm-worker-0-0&fileName=stderr
   RuntimeError: Error in dlopen for library libnvrtc.so.11.2and libnvrtc-d833c4f3.so.11.2
    ```
   解决：
    ```python
    18: from torch.nn.init import trunc_normal_ - > from torch.nn.init import normal_
    117: trunc_normal_(self.query, std=.02) -> normal_(self.query, std=.02)
    132: trunc_normal_(m.weight, std=.02) -> normal_(m.weight, std=.02)
    ```
2. Report_to问题
    ```python
   # bug https://mlp.sankuai.com/ml/#/job/logv2/task?from=job&jobId=psx59dxqjpjsdhm&roleName=Worker&taskId=0&attemptId=psx59dxqjpjsdhm-worker-0-0&fileName=stderr
   only azure_ml, comet_ml, mlflow, neptune, tensorboard, wandb, codecarbon, clearml, dagshub, flyte are supported
    ```
    解决
    ```python
    # 修改report_to 为"none" 该参数并不是tensorboard 或者log 的存储，而是wandb这种report保存的
   --report_to "none" \
    ```
   
3. TypeError: QWenPreTrainedModel._set_gradient_checkpointing() got an unexpected keyword argument 'enable'

    ```python
    # bug https://mlp.sankuai.com/ml/#/job/logv2/task?from=job&jobId=psx5e4xqjpjsdhm&roleName=Worker&taskId=0&attemptId=psx5e4xqjpjsdhm-worker-0-0&fileName=stderr
    Traceback (most recent call last):
      File "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai-llms/users/x/meituan/large_language_model/wow/vl/Qwen-VL/finetune.py", line 367, in <module>
        train()
      File "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai-llms/users/x/meituan/large_language_model/wow/vl/Qwen-VL/finetune.py", line 360, in train
        trainer.train()
      File "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai-llms/users/x/env/chuan_vl/lib/python3.10/site-packages/transformers/trainer.py", line 1555, in train
        return inner_training_loop(
      File "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai-llms/users/x/env/chuan_vl/lib/python3.10/site-packages/transformers/trainer.py", line 1668, in _inner_training_loop
        self.model.gradient_checkpointing_enable(gradient_checkpointing_kwargs=gradient_checkpointing_kwargs)
      File "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai-llms/users/x/env/chuan_vl/lib/python3.10/site-packages/transformers/modeling_utils.py", line 1872, in gradient_checkpointing_enable
        self._set_gradient_checkpointing(enable=True, gradient_checkpointing_func=gradient_checkpointing_func)
    TypeError: QWenPreTrainedModel._set_gradient_checkpointing() got an unexpected keyword argument 'enable'
    ```
    解决
    ```python
    # transformer 4.35有这个问题，可以降到4.34.0或者升级到最新 
    pip install transformers==4.37.2
    ```
   

## 实验结果


## 结果分析