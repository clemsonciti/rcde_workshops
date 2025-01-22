#!/bin/bash
MASTER_HOSTNAME=$1
PROJECT_DIR=$2
NNODES=$3
NGPUS_PER_NODE=$4

cd $PROJECT_DIR
module load miniforge3
module load cuda

source activate LLMsInferenceWorkshop3

echo "[$(date)] Starting on node $HOSTNAME (Rank ${SLURM_PROCID})" >&2
echo "Master: $MASTER_HOSTNAME, Nodes: $NNODES, GPUs per node: $NGPUS_PER_NODE" >&2

torchrun \
    --nnodes=$NNODES \
    --nproc_per_node=$NGPUS_PER_NODE \
    --rdzv_id=12345 \
    --rdzv_backend=c10d \
    --rdzv_endpoint=$MASTER_HOSTNAME:3000 \
    inference.py

EXIT_CODE=$?
echo "[$(date)] Exiting with code $EXIT_CODE" >&2
exit $EXIT_CODE