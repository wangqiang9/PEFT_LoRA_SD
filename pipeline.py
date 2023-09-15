from modelscope.models import Model
from peft import PeftModel
from modelscope.pipelines import pipeline
from modelscope.utils.constant import DownloadMode, Tasks
from diffusers import DiffusionPipeline
from modelscope import snapshot_download

model_path = snapshot_download("AI-ModelScope/stable-diffusion-v2-1")
model = Model.from_pretrained(model_path, device_map='auto')

pipeline = DiffusionPipeline.from_pretrained(
            '/mnt/workspace/.cache/modelscope/AI-ModelScope/stable-diffusion-v2-1')
pipeline = pipeline.to('cuda')
pipeline.unet = PeftModel.from_pretrained(pipeline.unet, './results/unet')
prompt = "a dog"
for index in range(20):
    image = pipeline(prompt).images[0]
    image.save(f"./lora_result_{index}.png")
