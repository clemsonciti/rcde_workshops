#!/bin/bash
#SBATCH --job-name=create_LLMs_env
#SBATCH --mem=12G
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=1
#SBATCH --output=create_LLMs_env_output.log

# Palmetto modules
module load miniforge3

ENV_NAME="PytorchWorkshop2"

conda create -y -n $ENV_NAME python=3.11

source activate $ENV_NAME

pip install -r requirements.txt --no-cache-dir

python -m ipykernel install --user --name $ENV_NAME --display-name "$ENV_NAME"
