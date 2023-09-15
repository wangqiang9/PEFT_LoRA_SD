export MODEL_NAME="AI-ModelScope/stable-diffusion-v2-1"
export DATASET_NAME="dog"
python train.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$DATASET_NAME \
  --resolution=768 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --max_train_steps=400 \
  --learning_rate=1e-04 \
  --max_grad_norm=1 \
  --lora_r=16 --lora_alpha=32 \
  --validation_prompts "a dog" \
  --lr_scheduler="constant" --lr_warmup_steps=0 \
  --output_dir="results" 