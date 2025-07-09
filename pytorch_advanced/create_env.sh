#!/bin/bash
#SBATCH --job-name=create_pytorch_env
#SBATCH --output=create_pytorch_env.out
#SBATCH --error=create_pytorch_env.err
#SBATCH --partition=work1
#SBATCH --mem=16G
#SBATCH --time=01:00:00

set -e  # Exit on first error

# Load Miniforge (Conda base)
module load miniforge3

# Create a fresh environment with pinned Python version
conda create -y -n PytorchWorkshop "python==3.11" pip

# Activate the environment
source activate PytorchWorkshop

# Upgrade and pin pip
pip install --upgrade "pip==25.1.1"

# Install PyTorch with CUDA 12.4 wheels (pinned versions)
pip install \
  "torch==2.6.0+cu124" \
  "torchvision==0.21.0+cu124" \
  "torchaudio==2.6.0+cu124" \
  --index-url https://download.pytorch.org/whl/cu124

# Install key libraries (version-pinned)
pip install \
  "scikit-learn==1.7.0" \
  "pandas==2.3.0" \
  "pillow==11.0.0" \
  "matplotlib==3.10.3" \
  "jupyter==1.1.1" \
  "ipykernel==6.29.5" \
  "pytorch-lightning==2.5.2" \
  "wandb==0.21.0" \
  "ipywidgets==8.1.7"

# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name PytorchWorkshop --display-name "Pytorch Workshop"

echo "Environment 'PytorchWorkshop' created and registered successfully."
