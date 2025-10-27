#!/usr/bin/env bash
set -euo pipefail

# Simple, robust environment setup for this workshop using conda + pip.
# - Installs faiss-gpu and NumPy via conda-forge (built for NumPy 2.x)
# - Installs the rest via pip (no uv dependency)
# - Optionally installs PyTorch with CUDA wheels

ENV_NAME="llms-rag-workshop"
PY_VER="3.10"
TORCH_CUDA="cpu"   # options: cpu | cu118 | cu121 | cu122

usage() {
  cat <<USAGE
Usage: $0 [--name ENV_NAME] [--python PY_VER] [--torch {cpu|cu118|cu121|cu122}]

Examples:
  $0                                   # conda env=llms-rag-workshop, python=3.10, torch CPU
  $0 --torch cu121                     # install PyTorch CUDA 12.1 wheels via pip
  $0 --name rag-env --python 3.11      # custom env name and Python version
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -n|--name) ENV_NAME="$2"; shift 2;;
    -p|--python) PY_VER="$2"; shift 2;;
    -t|--torch) TORCH_CUDA="$2"; shift 2;;
    -h|--help) usage; exit 0;;
    *) echo "Unknown arg: $1"; usage; exit 1;;
  esac
done

if ! command -v conda >/dev/null 2>&1; then
  echo "Error: conda not found. Please install Miniconda/Conda and retry." >&2
  exit 1
fi

echo "Creating conda env: $ENV_NAME (python=$PY_VER)"
conda create -y -n "$ENV_NAME" "python=$PY_VER"

# Enable 'conda activate' in this script
eval "$(conda shell.bash hook)"
conda activate "$ENV_NAME"

echo "Installing FAISS GPU + NumPy from conda-forge (works with NumPy 2.x)"
conda install -y -c conda-forge "faiss-gpu>=1.8.0" "numpy>=2.0"

echo "Installing core Python deps via pip (no faiss from pip)"
python -m pip install --upgrade pip
python -m pip install \
  sentence-transformers \
  "transformers>=4.55.2" \
  accelerate \
  jsonpatch \
  "langchain>=0.2.16" \
  "langchain-core>=0.2.38" \
  "langchain-community>=0.2.16" \
  "langchain-huggingface>=0.0.6" \
  "langchain-text-splitters>=0.2.2" \
  pandas \
  matplotlib \
  scikit-learn \
  networkx \
  jupyter \
  jupyterlab \
  ipywidgets \
  notebook \
  tqdm \
  ipython

echo "Installing PyTorch (${TORCH_CUDA})"
case "$TORCH_CUDA" in
  cpu)
    python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    ;;
  cu118)
    python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    ;;
  cu121)
    python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    ;;
  cu122)
    python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu122
    ;;
  *)
    echo "Unknown --torch option: $TORCH_CUDA (use cpu|cu118|cu121|cu122)" >&2
    exit 1
    ;;
esac

echo "Registering Jupyter kernel: $ENV_NAME"
python -m ipykernel install --user --name "$ENV_NAME" --display-name "$ENV_NAME"

echo "Verifying FAISS and NumPy compatibility:"
python - <<'PY'
import numpy as np
import faiss
print('numpy', np.__version__, '| faiss', faiss.__version__)
PY

cat <<DONE

Success! Activate the env and launch Jupyter:
  conda activate $ENV_NAME
  jupyter lab

Select kernel "$ENV_NAME" in Jupyter for these notebooks.
DONE
