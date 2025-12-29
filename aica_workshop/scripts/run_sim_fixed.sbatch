#!/bin/bash

# Submit this script with: sbatch FILENAME

#SBATCH --ntasks 1           # number of tasks
#SBATCH --cpus-per-task 1    # number of cpu cores per task
#SBATCH --time 0:01:01       # walltime
#SBATCH --mem 1gb            # amount of memory per CPU core (Memory per Task / Cores per Task)
#SBATCH --nodes 1            # number of nodes
#SBATCH --job-name "EstimatePi" # job name
#SBATCH --account staff     # account name
# Created with the RCD Docs Job Builder
#
# Visit the following link to edit this job:
# https://docs.rcd.clemson.edu/palmetto/job_management/job_builder/?num_cores=4&num_mem=1kb&gpu_model=h200&walltime=0%3A00%3A01&account_name=stafff&job_name=EstimatePi

module load miniforge3

cd /home/cehrett/Projects/RCD_Workshops/rcde_workshops/aica_workshop/
python scripts/run_sim.py --n-samples 1_000_000