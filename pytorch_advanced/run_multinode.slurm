#!/usr/bin/bash
#SBATCH --job-name=multinode_job
#SBATCH --output=multinode_job.out
#SBATCH --error=multinode_job.err
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=2GB
#SBATCH --gpus=a100:4
#SBATCH --time=1:00:00

srun --nodes=2 --ntasks-per-node=1 --cpus-per-task=10 --mem-per-cpu=2GB --gpus=a100:4 --time=1:00:00 multi_node_helper.sh `hostname` `pwd` 2 2
