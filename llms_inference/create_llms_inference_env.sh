#!/bin/bash

# Create the environment with Python, PyTorch, and CUDA support
conda create -n LLMsInferenceWorkshop python=3.12

# Activate the environment
source activate LLMsInferenceWorkshop

# Install additional packages
# TBD

# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name LLMsInferenceWorkshop --display-name "LLMs Inference Workshop"
