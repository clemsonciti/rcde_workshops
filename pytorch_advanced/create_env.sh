#!/usr/bin/bash

module load anaconda3

conda create -y -n pytorch_bench python=3.11

source activate pytorch_bench

pip install -r requirements.txt --no-cache-dir