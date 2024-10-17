from diffusers import DiffusionPipeline
import torch

weights_path = "/home/thebiglion/stable-diffusion/stable-diffusion-v1.0.0/snapshots/f03de327dd89b501a01da37fc5240cf4fdba85a1"
pipeline = DiffusionPipeline.from_pretrained(weights_path, torch_dtype=torch.float32)

prompt = 'a superman, trying to protect airplane from crashing'
height, width = 1024, 1024
num_inference_steps = 70

image = pipeline(prompt, height=height, width=width, num_inference_steps=num_inference_steps).images[0]
file_path='results/last_img_id.txt'
with open(file_path,'r') as read_file:
    id=read_file.read()
    img_dir='results/generated_samples/'
    with open(file_path,'w') as write_file:
        if id:
            incremented_id=str(int(id)+1)
            write_file.write(incremented_id)
            image.save(f"{img_dir}image{incremented_id}.png")
        else: 
            write_file.write('1')
            image.save(f"{img_dir}image{1}.png")
