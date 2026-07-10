#!/bin/bash

# Submit this script with: sbatch FILENAME

#SBATCH --ntasks 1           # number of tasks
#SBATCH --cpus-per-task 1    # number of cpu cores per task
#SBATCH --time 0:00:01       # walltime
#SBATCH --mem 1kb            # amount of memory per CPU core (Memory per Task / Cores per Task)
#SBATCH --nodes 1            # number of nodes
#SBATCH --job-name "EstimatePi" # job name
#SBATCH --account=rcde_workshop # account name
#SBATCH --reservation=ai_code_workshop # reservation name
#SBATCH --partition=workshop # partition
# Created with the RCD Docs Job Builder

module load python
source activate /project/rcde/cehrett/aica_workshop/env/

python run_sim.py --n-samples 1_000_000

