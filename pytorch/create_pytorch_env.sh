#!/bin/bash

# Create the environment with Python, PyTorch, and CUDA support
conda create -n PytorchWorkshop python=3.11 pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia -y

# Activate the environment
source activate PytorchWorkshop

# Install additional packages
conda install scikit-learn pandas pillow -c conda-forge -y
conda install matplotlib jupyter -c conda-forge -y
conda install ipykernel -y
conda install -c conda-forge pytorch-lightning -y
conda install wandb -y

# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name PytorchWorkshop --display-name "Pytorch Workshop"
