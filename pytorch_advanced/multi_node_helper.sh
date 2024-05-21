#!/bin/bash
# The script to run on each node. On pbs, called with `pbsdsh`.
# On slurm call with mpirun?

# resonable srun command:
# srun --nodes=2 --ntasks-per-node=1 --cpus-per-task=10 --mem-per-cpu=2GB --gpus=a100:2 --time=1:00:00 multi_node_helper.sh `hostname` `pwd` 2 2

MASTER_HOSTNAME=$1
PROJECT_DIR=$2
NNODES=$3
NGPUS_PER_NODE=$4

cd $PROJECT_DIR

module load anaconda3
source activate pytorch_bench
torchrun \
    --nnodes=$NNODES \
    --nproc_per_node=$NGPUS_PER_NODE \
    --rdzv_id=12345 \
    --rdzv_backend=c10d \
    --rdzv_endpoint=$MASTER_HOSTNAME:3000 \
    multi_node.py

echo "$HOSTNAME" finished tasks