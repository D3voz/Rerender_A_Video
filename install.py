import os
import requests
import launch

# Check and install necessary Python packages from requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.readlines()

for package in requirements:
    package_name = package.split("==")[0]
    if not launch.is_installed(package_name):
        launch.run_pip(f"install {package}", f"requirements for Rerender_A_Video ({package_name})")

# Function to download necessary models and files
def download(url, dir, name=None):
    os.makedirs(dir, exist_ok=True)
    if name is None:
        name = url.split('/')[-1]
    path = os.path.join(dir, name)
    if not os.path.exists(path):
        print(f'Installing {name} ...')
        open(path, 'wb').write(requests.get(url).content)
        print('Installed successfully.')

# Download necessary models and files
download('https://huggingface.co/PKUWilliamYang/Rerender/resolve/main/models/gmflow_sintel-0c07dcb3.pth', 'models')
download('https://huggingface.co/lllyasviel/ControlNet/resolve/main/models/control_sd15_canny.pth', 'models')
download('https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt', 'models')

print("Installation completed!")
