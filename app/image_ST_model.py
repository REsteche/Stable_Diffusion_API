import torch
from diffusers import StableDiffusionPipeline
import os


access_token = "" # include your own acess token from hugging faces here
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, 
                    torch_dtype=torch.float16, 
                    revision="fp16", 
                    use_auth_token=access_token).to(device)


class ImageSTModel:
    def __init__(self, limit=1, adult_filter_off=True, 
                 force_replace=False, timeout=100):
        self.limit = limit
        self.adult_filter_off = adult_filter_off
        self.force_replace = force_replace
        self.timeout = timeout
        
    def get_image(self, download):
        torch.cuda.empty_cache()
        with torch.autocast("cuda"): #without autocast it -supposedly- gets 25% faster
            image = pipe(download.lower(), guidance_scale=7.5)[0] 
        
        outfilename = download.replace(' ', '_') + '.png'
        image.save(outfilename) 

        file_name = os.listdir(outfilename)[0]
        file_path = download+"/"+file_name
        return file_path
