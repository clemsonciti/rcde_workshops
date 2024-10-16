#!/bin/bash
#SBATCH --job-name=dask_job
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=2
#SBATCH --time=01:00:00
#SBATCH --output=dask_output.log

module load anaconda3  # Load Anaconda

# Ensure the conda environment is accessible across nodes
export PATH=$HOME/.conda/envs/hpc_ml/bin:$PATH

# Get the hostnames of the allocated nodes
hostnames=$(scontrol show hostnames $SLURM_JOB_NODELIST)

# Start the Dask scheduler on the first node
first_node=$(echo $hostnames | awk '{print $1}')
ssh $first_node "
    module load anaconda3 &&
    source activate hpc_ml &&
    dask-scheduler --scheduler-file=scheduler.json &
" &

# Start Dask workers on all nodes
for node in $hostnames; do
    ssh $node "
        module load anaconda3 &&
        source activate hpc_ml &&
        dask-worker --scheduler-file=scheduler.json --nthreads=1 --nprocs=2 --memory-limit=0 &
    " &
done

# Wait for all processes to complete
wait

