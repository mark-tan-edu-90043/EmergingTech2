from diffusers import StableDiffusionPipeline, DiffusionPipeline
import torch
import base64

def promptResponse(prompt) -> str:
    model_id = "stabilityai/stable-diffusion-xl-base-1.0"

    # model_id = "runwayml/stable-diffusion-v1-5" # Uncommnt this to use Stable Diffusion 1.5, if the XL Model is too large.


    pipe = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to("cuda")

    prompt = f"{prompt}, 3D Model, Blender, High Quality"
    image = pipe(prompt).images[0] 

    image_path = "result.png"
    image.save(image_path)
    return image_path