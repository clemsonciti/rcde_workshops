#!/bin/bash
# The script to run on each node. On pbs, called with `pbsdsh`.
MASTER_HOSTNAME=$1
PROJECT_DIR=$2
NNODES=$3
NGPUS_PER_NODE=$4

cd $PROJECT_DIR
source /etc/profile.d/modules.sh
module load anaconda3/2022.05-gcc/9.5.0
source activate pytorch_workshop
torchrun \
    --nnodes=$NNODES \
    --nproc_per_node=$NGPUS_PER_NODE \
    --rdzv_id=12345 \
    --rdzv_backend=c10d \
    --rdzv_endpoint=$MASTER_HOSTNAME:3000 \
    multi_node.py

echo "$HOSTNAME" finished tasks