#!/bin/bash
# multi_node.pbs -- the pbs batch job script. Execute with `qsub multi_node.pbs` from a login node.
# Example pbs resource request for 2 nodes, 2 a100 gpus per node
#PBS -l select=2:ncpus=16:mem=32gb:ngpus=2:gpu_model=a100,walltime=0:5:00

PROJECT_DIR="/home/dane2/Code/rcde_workshops/pytorch_advanced"
cd ${PROJECT_DIR}

pbsdsh -- bash "$(pwd)"/multi_node_helper.sh $HOSTNAME $(pwd) 2 2