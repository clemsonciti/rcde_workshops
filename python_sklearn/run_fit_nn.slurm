#!/bin/bash
#SBATCH --job-name=workshop_fit_nn
#SBATCH --output=logs/%x-%j.out   # Creates a log file in a logs/ directory
#SBATCH --error=logs/%x-%j.err
#SBATCH --time=00:05:00
#SBATCH --partition=work1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G

# Load your environment 
module load anaconda3
source activate hpc_ml  # or your preferred env

# Run the Python script
python fit_nn.py