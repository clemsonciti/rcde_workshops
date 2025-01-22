#!/bin/bash
#SBATCH -N2
#SBATCH --time=00:30:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=12GB
#SBATCH --gpus-per-node=v100:1
#SBATCH --job-name=llm_inference
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --ntasks-per-node=1  

module load miniforge3
module load cuda

source activate LLMsInferenceWorkshop3
cd /home/cehrett/Projects/RCD_Workshops/rcde_workshops/llms_inference/

srun --export=ALL -N2 --ntasks=2 --gpus-per-node=v100:1 bash helper_inference.sh $(hostname) $PWD 2 1