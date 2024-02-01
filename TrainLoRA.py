# @title ## 1.1. Install Dependencies
# @markdown Clone Kohya Trainer from GitHub and check for updates. Use textbox below if you want to checkout other branch or old commit. Leave it empty to stay the HEAD on main.  This will also install the required libraries.
import os
import zipfile
import shutil
import time
from subprocess import getoutput
from IPython.utils import capture



# root_dir
root_dir = "/content"
deps_dir = os.path.join(root_dir, "deps")
repo_dir = os.path.join(root_dir, "kohya-trainer")
training_dir = os.path.join(root_dir, "LoRA")
pretrained_model = os.path.join(root_dir, "pretrained_model")
vae_dir = os.path.join(root_dir, "vae")
config_dir = os.path.join(training_dir, "config")

# repo_dir
accelerate_config = os.path.join(repo_dir, "accelerate_config/config.yaml")
tools_dir = os.path.join(repo_dir, "tools")
finetune_dir = os.path.join(repo_dir, "finetune")

for store in [
    "root_dir",
    "deps_dir",
    "repo_dir",
    "training_dir",
    "pretrained_model",
    "vae_dir",
    "accelerate_config",
    "tools_dir",
    "finetune_dir",
    "config_dir",
]:
    with capture.capture_output() as cap:
        %store
        {store}
        del cap

repo_url = "https://github.com/Linaqruf/kohya-trainer"
bitsandytes_main_py = "/usr/local/lib/python3.10/dist-packages/bitsandbytes/cuda_setup/main.py"
branch = ""  # @param {type: "string"}
mount_drive = False  # @param {type: "boolean"}
verbose = False  # @param {type: "boolean"}


def read_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


def write_file(filename, contents):
    with open(filename, "w") as f:
        f.write(contents)


def clone_repo(url):
    if not os.path.exists(repo_dir):
        os.chdir(root_dir)
        !git
        clone
        {url}
        {repo_dir}
    else:
        os.chdir(repo_dir)
        !git
        pull
        origin
        {branch} if branch else !git
        pull


def install_dependencies():
    s = getoutput('nvidia-smi')

    if 'T4' in s:
        !sed - i
        "s@cpu@cuda@"
        library / model_util.py

    !pip
    install
    {'-q' if not verbose else ''} - -upgrade - r
    requirements.txt

    from accelerate.utils import write_basic_config

    if not os.path.exists(accelerate_config):
        write_basic_config(save_location=accelerate_config)


def remove_bitsandbytes_message(filename):
    welcome_message = """
def evaluate_cuda_setup():
    print('')
    print('='*35 + 'BUG REPORT' + '='*35)
    print('Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues')
    print('For effortless bug reporting copy-paste your error into this form: https://docs.google.com/forms/d/e/1FAIpQLScPB8emS3Thkp66nvqwmjTEgxp8Y9ufuWTzFyr9kJ5AoI47dQ/viewform?usp=sf_link')
    print('='*80)"""

    new_welcome_message = """
def evaluate_cuda_setup():
    import os
    if 'BITSANDBYTES_NOWELCOME' not in os.environ or str(os.environ['BITSANDBYTES_NOWELCOME']) == '0':
        print('')
        print('=' * 35 + 'BUG REPORT' + '=' * 35)
        print('Welcome to bitsandbytes. For bug reports, please submit your error trace to: https://github.com/TimDettmers/bitsandbytes/issues')
        print('For effortless bug reporting copy-paste your error into this form: https://docs.google.com/forms/d/e/1FAIpQLScPB8emS3Thkp66nvqwmjTEgxp8Y9ufuWTzFyr9kJ5AoI47dQ/viewform?usp=sf_link')
        print('To hide this message, set the BITSANDBYTES_NOWELCOME variable like so: export BITSANDBYTES_NOWELCOME=1')
        print('=' * 80)"""

    contents = read_file(filename)
    new_contents = contents.replace(welcome_message, new_welcome_message)
    write_file(filename, new_contents)


def main():
    os.chdir(root_dir)

    if mount_drive:
        if not os.path.exists("/content/drive"):
            drive.mount("/content/drive")

    for dir in [
        deps_dir,
        training_dir,
        config_dir,
        pretrained_model,
        vae_dir
    ]:
        os.makedirs(dir, exist_ok=True)

    clone_repo(repo_url)

    if branch:
        os.chdir(repo_dir)
        status = os.system(f"git checkout {branch}")
        if status != 0:
            raise Exception("Failed to checkout branch or commit")

    os.chdir(repo_dir)

    !apt
    install
    aria2
    {'-qq' if not verbose else ''}

    install_dependencies()
    time.sleep(3)

    remove_bitsandbytes_message(bitsandytes_main_py)

    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    os.environ["BITSANDBYTES_NOWELCOME"] = "1"
    os.environ["SAFETENSORS_FAST_GPU"] = "1"

    cuda_path = "/usr/local/cuda-11.8/targets/x86_64-linux/lib/"
    ld_library_path = os.environ.get("LD_LIBRARY_PATH", "")
    os.environ["LD_LIBRARY_PATH"] = f"{ld_library_path}:{cuda_path}"


main()




