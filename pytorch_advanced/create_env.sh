#!/usr/bin/bash

ENV_NAME="PytorchWorkshop"

module load anaconda3

conda create -y -n $ENV_NAME python=3.11

source activate $ENV_NAME

pip install -r requirements.txt --no-cache-dir

python -m ipykernel install --user --name $ENV_NAME --display-name "$ENV_NAME"
