import os
import re
import toml
from time import time

Model_list= {  "AnyLora":"https://huggingface.co/Lykon/AnyLoRA/resolve/main/AnyLoRA_noVae_fp16-pruned.ckpt",
               "Anime":"https://huggingface.co/hollowstrawberry/stable-diffusion-guide/resolve/main/models/animefull-final-pruned-fp16.safetensors",
               "Basic SD1.5 ":"https://huggingface.co/hollowstrawberry/stable-diffusion-guide/resolve/main/models/sd-v1-5-pruned-noema-fp16.safetensors"
            }





COLAB = True # low ram
XFORMERS = True
SOURCE = "https://github.com/kohya-ss/sd-scripts"
COMMIT = "9a67e0df390033a89f17e70df5131393692c2a55"
BETTER_EPOCH_NAMES = True
LOAD_TRUNCATED_IMAGES = True

# Please setup for your project name
project_name = input("Please input project name: ")
project_name = project_name.strip()
training_model = input("Please input training_model: ")
for training_model in Model_list:
    if training_model == Model_list:

# default choosing sd1.5

## Processing
resolution = 512
shuffle_tags = True
activation_tags = 2



resolution = 512
flip_aug = False
caption_extension = ".txt"
shuffle_tags = True
shuffle_caption = shuffle_tags
activation_tags = "1" #@param [0,1,2,3]
keep_tokens = int(activation_tags)

## Steps
num_repeats = 10
preferred_unit = "Epochs" or "steps" # 1 epochs = 200 steps
how_many = 2000
#Your images will repeat this number of times during training.
#I recommend that your images multiplied by their repeats is between 200 and 400.
# Use for comparing the Lora progress better
save_every_n_epochs = 1
keep_only_last_n_epochs = 10
train_batch_size = 2 # Recommended 2 or 3

## Learning
unet_lr = 5e-4
text_encoder_lr = 1e-4
lr_scheduler = "cosine_with_restarts"
lr_scheduler_number = 3
lr_warmup_ratio = 0.05
#More dim means larger Lora, it can hold more information but more isn't always better.
# A dim between 8-32 is recommended, and alpha equal to half the dim.

## Structure
network_dim = 16
network_alpha= 8

