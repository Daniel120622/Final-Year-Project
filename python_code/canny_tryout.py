import sys
import numpy as np
import cv2
from PIL import Image
from diffusers import ControlNetModel, StableDiffusionControlNetPipeline, UniPCMultistepScheduler
import torch

def load_image(path):
    return Image.open(path)

def process_canny_images(image_path, output_path, low_threshold, high_threshold):
    try:
        image = load_image(image_path)
        image = np.array(image)

        image = cv2.Canny(image, low_threshold, high_threshold)
        image = image[:, :, None]
        image = np.concatenate([image, image, image], axis=2)
        image = Image.fromarray(image)  # become a canny_format_img
        image.save(output_path)
        print(f"Result image saved to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)

def canny_img2controlNet_img(image_path, output_path):
    print(f"Generating image for prompt: {'a man wearing a upper cloths'}")
    image = load_image(image_path)
    controlnet = ControlNetModel.from_pretrained(
        "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
    )

    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", controlnet=controlnet, safety_checker=None, torch_dtype=torch.float16
    )

    pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)

    # Remove if you do not have xformers installed
    # see https://huggingface.co/docs/diffusers/v0.13.0/en/optimization/xformers#installing-xformers
    # for installation instructions
    pipe.enable_xformers_memory_efficient_attention()
    pipe.enable_model_cpu_offload()
    image = pipe("a man wearing a upper cloths", image, num_inference_steps=20).images[0]
    image.save(output_path)
    print(f"Result image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python canny_tryout.py <image1_path> <image2_path> <output1_path> <output2_path> <low_threshold> <high_threshold>")
        sys.exit(1)

    image1_path = sys.argv[1]
    image2_path = sys.argv[2]
    output1_path = sys.argv[3]
    output2_path = sys.argv[4]
    low_threshold = int(sys.argv[5])
    high_threshold = int(sys.argv[6])

    process_canny_images(image1_path, output1_path, low_threshold, high_threshold)
    process_canny_images(image2_path, output2_path, low_threshold, high_threshold)

