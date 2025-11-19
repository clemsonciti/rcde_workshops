#!/bin/bash
#SBATCH -J multinode_llm              # Friendly job name for queue listings.
#SBATCH -N 2                           # Request 2 physical nodes.
#SBATCH --ntasks-per-node=1            # Launch 1 Python process per node (2 total).
#SBATCH --gpus-per-node=a100:2         # Give each node its 2 local A100 40GB GPUs.
#SBATCH --mem=32G                      # Be polite: cap each node at ~32 GiB RAM usage.
#SBATCH -t 01:00:00                    # Plenty of time for model downloads + inference.
#SBATCH -o multinode_%j.out            # Stdout log file (%j expands to job ID).
#SBATCH -e multinode_%j.err            # Stderr log file.

set -euo pipefail

# ---------------------------------------------------------------------------
# Basic diagnostics so the log captures what Slurm actually allocated. This is
# especially useful when teaching because students can see both nodes listed.
# ---------------------------------------------------------------------------
echo "[Slurm] Job ID           : $SLURM_JOB_ID"
echo "[Slurm] Node list        : $SLURM_JOB_NODELIST"
echo "[Slurm] Node count       : $SLURM_JOB_NUM_NODES"
echo "[Slurm] Tasks per node   : $SLURM_NTASKS_PER_NODE"
echo "[Slurm] GPUs per node    : $SLURM_GPUS_PER_NODE"
echo "[Slurm] Mem per node     : ${SLURM_MEM_PER_NODE:-not-set}"
echo "[Slurm] Mem per CPU      : ${SLURM_MEM_PER_CPU:-not-set}"
echo "[Slurm] Mem per GPU      : ${SLURM_MEM_PER_GPU:-not-set}"
echo

# Palmetto sets multiple memory environment variables by default, which can
# confuse `srun` (fatal: mem-per-CPU, mem-per-GPU, mem-per-node are exclusive).
# We explicitly requested --mem=32G (per node), so drop the CPU/GPU entries.
unset SLURM_MEM_PER_CPU SLURM_MEM_PER_GPU

# ---------------------------------------------------------------------------
# Load / activate whatever environment already contains PyTorch + Transformers.
# Replace these commands with the environment module/path you actually use.
# ---------------------------------------------------------------------------
module load miniforge3
source /project/rcde/cehrett/running_llms_workshop/env/bin/activate

python --version
which python

# ---------------------------------------------------------------------------
# srun respects the Slurm directives given above. Because we asked for
# --ntasks-per-node=1, the following line launches exactly one Python process
# on each node. Each process automatically sees the two local GPUs so the
# Hugging Face pipeline can spread the 30B model layers via device_map="auto".
# ---------------------------------------------------------------------------
srun python multinode_infer.py
