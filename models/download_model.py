from diffusers import DiffusionPipeline
import torch
model_id=""
# Remove torch_dtype=torch.float16
pipeline = DiffusionPipeline.from_pretrained(model_id)

# Use a GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
pipeline.to(device)

pipeline("An image of a squirrel in Picasso style").images[0]