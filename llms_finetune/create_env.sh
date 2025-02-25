#!/bin/bash
#SBATCH --job-name=create_LLMs_env
#SBATCH --mem=12G
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=1
#SBATCH --output=create_LLMs_env_output.log

# Palmetto modules
module load miniforge3
module load cuda

export ENV_NAME=LLMsFT  

# Create environment
conda create --yes --name $ENV_NAME python=3.10
source activate $ENV_NAME

# Install packages with pinned versions
pip3 install torch==2.5.1+cu118 torchvision==0.20.1+cu118 torchaudio==2.5.1+cu118 \
  --index-url https://download.pytorch.org/whl/cu118

pip3 install accelerate==1.2.1 bitsandbytes==0.45.0 deepspeed==0.16.2
pip3 install transformers==4.48.0
pip3 install flash-attn==2.7.3
pip3 install scipy==1.15.1
pip3 install jupyterlab==4.3.4 ipykernel==6.29.5 ipywidgets==8.1.5
pip3 install sentence-transformers==3.4.1
pip3 install faiss-gpu==1.7.2
pip3 install langchain==0.3.17 langchain-community==0.3.16
pip3 install unstructured==0.16.19
pip3 install datasets==3.2.0
pip3 install peft==0.14.0
pip3 install wandb==0.19.6

echo "Done! $ENV_NAME environment created."

