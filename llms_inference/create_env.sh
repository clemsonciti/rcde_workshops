#!/bin/bash
#SBATCH --job-name=create_LLMs_env
#SBATCH --mem=12G
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=1
#SBATCH --output=create_LLMs_env_output.log

# Palmetto modules
module load miniforge3
module load cuda

export ENV_NAME=LLMsInferenceWorkshop

# Create environment
conda create --yes --name $ENV_NAME python=3.11
source activate $ENV_NAME

# Install packages with pinned versions
pip3 install torch==2.5.1+cu118 torchvision==0.20.1+cu118 torchaudio==2.5.1+cu118 \
  --index-url https://download.pytorch.org/whl/cu118

pip3 install accelerate==1.2.1 bitsandbytes==0.45.0 deepspeed==0.16.2
pip3 install transformers==4.48.0
pip3 install flash-attn==2.7.3
pip3 install scipy==1.15.1
pip3 install jupyterlab==4.3.4 ipykernel==6.29.5 ipywidgets==8.1.5
pip3 install qwen-vl-utils==0.0.8
pip3 install scikit-learn==1.6.1

echo "Done! $ENV_NAME environment created."

