#!/bin/bash
#SBATCH --job-name=create_pytorch_env
#SBATCH --output=create_pytorch_env.out
#SBATCH --error=create_pytorch_env.err
#SBATCH --partition=work1
#SBATCH --mem=16G
#SBATCH --time=01:00:00

set -e  # Exit on first error

# Load Miniforge
module load miniforge3

# Create the environment
conda create -n PytorchWorkshop python=3.11 -y

# Activate the environment
source activate PytorchWorkshop

# Upgrade pip
pip install --upgrade pip

# Install PyTorch with CUDA 12.4 wheels
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Install other required packages
pip install \
    scikit-learn pandas pillow \
    matplotlib jupyter \
    ipykernel pytorch-lightning wandb ipywidgets

# Register the kernel for Jupyter
python -m ipykernel install --user --name PytorchWorkshop --display-name "Pytorch Workshop"

echo "Environment 'PytorchWorkshop' created and registered successfully."
