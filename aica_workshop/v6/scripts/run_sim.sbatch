#!/bin/bash

# Submit this script with: sbatch FILENAME

#SBATCH --ntasks 1           # number of tasks
#SBATCH --cpus-per-task 8    # number of cpu cores per task
#SBATCH --time 0:01:01       # walltime
#SBATCH --mem 16G            # amount of memory per CPU core (Memory per Task / Cores per Task)
#SBATCH --nodes 1            # number of nodes
#SBATCH --job-name "EstimatePi" # job name
#SBATCH --account staff     # account name
# Created with the RCD Docs Job Builder
#
# Visit the following link to edit this job:
# https://docs.rcd.clemson.edu/palmetto/job_management/job_builder/?num_cores=4&num_mem=1kb&gpu_model=h200&walltime=0%3A00%3A01&account_name=stafff&job_name=EstimatePi

module load miniforge3

echo ${SLURM_CPUS_PER_TASK:-1}  # Print number of CPUs allocated

python scripts/run_sim.py --n-samples 100_000_000 --workers "${SLURM_CPUS_PER_TASK:-1}"

## FAILURE MODES: insufficient walltime, insufficient mem, wrong account name, wrong module, wrong path to script.
## LAB2: Make use # workers equal to number of cores available
