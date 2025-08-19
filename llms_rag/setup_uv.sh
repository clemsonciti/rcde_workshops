#!/usr/bin/env bash

# Simple UV-based environment setup for the RAG workshop
# Creates a local .venv, installs dependencies via uv, and optionally
# registers a Jupyter kernel for the notebooks.

set -euo pipefail

PYTHON_VERSION="3.11"
USE_GPU=false
KERNEL_NAME="llms-rag-workshop"
REGISTER_KERNEL=false
USER_SET_PY=false
DOWNLOAD_ONLY=false
WHEELHOUSE=""

usage() {
  cat <<USAGE
Usage: $0 [options]

Options:
  -p, --python VER     Python version for the venv (default: ${PYTHON_VERSION})
  -g, --gpu            Install GPU extras (equivalent to -e ".[gpu]")
  -k, --kernel NAME    Register a Jupyter kernel with this name
  -r, --register       Alias for --kernel ${KERNEL_NAME}
  -d, --download-only  Download/build wheels for deps into a wheelhouse (no env install)
  -w, --wheelhouse DIR Directory for wheels (used with --download-only, or as source for install)
  -h, --help           Show this help

Examples:
  # CPU-only
  ./setup_uv.sh

  # With GPU extras + kernel registration
  ./setup_uv.sh --gpu --kernel ${KERNEL_NAME}
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -p|--python)
      PYTHON_VERSION="$2"; USER_SET_PY=true; shift 2;;
    -g|--gpu)
      USE_GPU=true; shift;;
    -k|--kernel)
      KERNEL_NAME="$2"; REGISTER_KERNEL=true; shift 2;;
    -r|--register)
      REGISTER_KERNEL=true; shift;;
    -d|--download-only)
      DOWNLOAD_ONLY=true; shift;;
    -w|--wheelhouse)
      WHEELHOUSE="$2"; shift 2;;
    -h|--help)
      usage; exit 0;;
    *)
      echo "Unknown option: $1"; usage; exit 1;;
  esac
done

if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Install from https://docs.astral.sh/uv/getting-started/"
  echo "For example: curl -LsSf https://astral.sh/uv/install.sh | sh"
  exit 1
fi

# If GPU requested and user did not specify a Python version, prefer 3.10 for faiss-gpu wheels
if $USE_GPU && ! $USER_SET_PY; then
  PYTHON_VERSION="3.10"
fi

# Determine project root as the directory of this script
SCRIPT_DIR="$(cd -- "$(dirname "$0")" >/dev/null 2>&1; pwd -P)"

if $DOWNLOAD_ONLY; then
  # Pre-download wheels into a wheelhouse for later offline or fast installs
  WHEELHOUSE=${WHEELHOUSE:-"${SCRIPT_DIR}/wheelhouse"}
  echo "Preparing wheelhouse at: ${WHEELHOUSE}"
  mkdir -p "${WHEELHOUSE}"

  # Create a temporary venv to run pip wheel
  DL_VENV_DIR=$(mktemp -d "${SCRIPT_DIR}/.uv-dl-venv.XXXXXX") || DL_VENV_DIR="${SCRIPT_DIR}/.uv-dl-venv"
  echo "Creating temporary venv for download at: ${DL_VENV_DIR} (Python ${PYTHON_VERSION})"
  uv venv --python "${PYTHON_VERSION}" "${DL_VENV_DIR}"

  ACTIVATE_DL=". \"${DL_VENV_DIR}/bin/activate\""
  if [[ "$(uname -s)" == "MINGW" || "$(uname -s)" == *"NT"* ]]; then
    ACTIVATE_DL=". \"${DL_VENV_DIR}/Scripts/activate\""
  fi
  eval ${ACTIVATE_DL}
  python -V

  echo "Downloading/building wheels into ${WHEELHOUSE}..."
  python -m pip install -U pip wheel setuptools >/dev/null
  if $USE_GPU; then
    python -m pip wheel -w "${WHEELHOUSE}" "${SCRIPT_DIR}[gpu]"
  else
    python -m pip wheel -w "${WHEELHOUSE}" "${SCRIPT_DIR}"
  fi

  echo "Cleaning up temporary venv..."
  deactivate || true
  rm -rf "${DL_VENV_DIR}"

  echo "Wheelhouse ready at ${WHEELHOUSE}. To install from it on another node, run:\n  ./setup_uv.sh --gpu --wheelhouse '${WHEELHOUSE}' --kernel ${KERNEL_NAME}"
  exit 0
fi

echo "Creating .venv with Python ${PYTHON_VERSION} via uv..."
uv venv --python "${PYTHON_VERSION}" .venv

ACTIVATE=". .venv/bin/activate"
if [[ "$(uname -s)" == "MINGW" || "$(uname -s)" == *"NT"* ]]; then
  ACTIVATE=". .venv/Scripts/activate"
fi

eval "$ACTIVATE"
python -V

echo "Installing project dependencies with uv pip from ${SCRIPT_DIR}..."
EXTRA_ARGS=()
if [[ -n "${WHEELHOUSE}" && -d "${WHEELHOUSE}" ]]; then
  echo "Using wheelhouse: ${WHEELHOUSE}"
  EXTRA_ARGS+=("--find-links" "${WHEELHOUSE}")
fi

if $USE_GPU; then
  set +e
  uv pip install "${EXTRA_ARGS[@]}" -e "${SCRIPT_DIR}[gpu]"
  rc=$?
  set -e
  if [[ $rc -ne 0 ]]; then
    echo "[WARN] GPU extras failed to install. Falling back to CPU deps."
    uv pip install "${EXTRA_ARGS[@]}" -e "${SCRIPT_DIR}"
  fi
else
  uv pip install "${EXTRA_ARGS[@]}" -e "${SCRIPT_DIR}"
fi

if $REGISTER_KERNEL; then
  echo "Registering Jupyter kernel: ${KERNEL_NAME}"
  python -m ipykernel install --user --name "${KERNEL_NAME}" --display-name "Python (${KERNEL_NAME})"
fi

echo "Done. Activate with:"
echo "  source .venv/bin/activate   # (or .venv\\Scripts\\activate on Windows)"
echo "Start Jupyter Lab:"
echo "  jupyter lab"
