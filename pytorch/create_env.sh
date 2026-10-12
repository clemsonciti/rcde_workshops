#!/bin/bash
#SBATCH --job-name=create_pytorch_env
#SBATCH --output=create_pytorch_env.out
#SBATCH --error=create_pytorch_env.err
#SBATCH --partition=work1
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=01:00:00

set -euo pipefail

# These names match the kernel metadata in the workshop notebook.
ENV_NAME="PytorchWorkshopFA26"
KERNEL_NAME="pytorchworkshopFA26"
DISPLAY_NAME="Pytorch Workshop Fall 2026"
PYTHON_VERSION="3.11"
PYTORCH_WHEEL_INDEX="https://download.pytorch.org/whl/cu124"

echo "Loading Anaconda on Palmetto..."
module purge
module load anaconda3

# Make conda activation available in this non-interactive Slurm job.
CONDA_BASE="$(conda info --base)"
source "${CONDA_BASE}/etc/profile.d/conda.sh"

# Create the environment only when it does not already exist.
# conda-forge avoids the licensing restrictions associated with Anaconda's
# default package channel while still using the requested Anaconda module.
if conda env list | awk 'NF && $1 !~ /^#/ {print $1}' | grep -Fxq "${ENV_NAME}"; then
    echo "Conda environment '${ENV_NAME}' already exists; updating its required packages."
else
    echo "Creating Conda environment '${ENV_NAME}'..."
    conda create --name "${ENV_NAME}" --override-channels --channel conda-forge "python=${PYTHON_VERSION}" pip --yes
fi

conda activate "${ENV_NAME}"

# Install the non-PyTorch packages used directly by the workshop notebook.
conda install --override-channels --channel conda-forge numpy matplotlib pillow ipykernel --yes

# Install CUDA-enabled PyTorch packages from PyTorch's official wheel index.
python -m pip install --upgrade pip
python -m pip install torch torchvision --index-url "${PYTORCH_WHEEL_INDEX}"

# Register the environment as a selectable Jupyter kernel.
python -m ipykernel install --user --name "${KERNEL_NAME}" --display-name "${DISPLAY_NAME}"

# Confirm that the required libraries import successfully. CUDA availability
# should be checked later from a Jupyter session that was allocated a GPU.
python - <<'PY'
import matplotlib
import numpy
import torch
import torchvision

print("Environment verification succeeded.")
print(f"PyTorch: {torch.__version__}")
print(f"Torchvision: {torchvision.__version__}")
print(f"NumPy: {numpy.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"PyTorch CUDA build: {torch.version.cuda}")
PY

echo
echo "Environment '${ENV_NAME}' is ready."
echo "In Open OnDemand, launch Jupyter with a GPU and select the kernel:"
echo "  ${DISPLAY_NAME}"
