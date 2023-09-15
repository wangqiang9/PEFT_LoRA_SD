# PEFT LoRA for Stable Diffsuion Trainer and Pipeline Example
PEFT does not have a specific example for Stable Diffusion LoRA, so this repo demonstrates how to use PEFT to perform Lora training and inference.
The models weight is from modelscope.

## Docker
```
registry.cn-hangzhou.aliyuncs.com/modelscope-repo/modelscope:ubuntu20.04-cuda11.3.0-py38-torch1.11.0-tf1.15.5-1.6.1
```

## Install
```bash
pip install modelscope
pip install peft
pip install diffusers==0.20.2
```

## Train
```bash
bash train.sh
```

## Pipeline
```
python pipeline.py
```