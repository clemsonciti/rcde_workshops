#!/bin/bash

# Submit this script with: sbatch FILENAME

#SBATCH --ntasks 1              # number of tasks
#SBATCH --cpus-per-task 8       # number of cpu cores per task
#SBATCH --time 0:20:00          # walltime
#SBATCH --mem 16G               # amount of memory per CPU core (Memory per Task / Cores per Task)
#SBATCH --nodes 1               # number of nodes
#SBATCH --job-name "PiBench"    # job name
#SBATCH --account rcd_workshop         # account name
#SBATCH --reservation=ai_code_workshop # reservation name
#SBATCH --partition=workshop # partition

module load miniforge3
source activate /project/rcde/cehrett/aica_workshop/env/

echo "CPUs per task: ${SLURM_CPUS_PER_TASK:-1}"

OUTPUT_DIR="results/sim_bench_${SLURM_JOB_ID:-manual}"

python scripts/run_sim_benchmark.py \
  --n-samples 2000000 \
  --repeats 10 \
  --output-dir "${OUTPUT_DIR}"
