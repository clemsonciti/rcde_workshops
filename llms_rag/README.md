# RAG for Research Applications Workshop

This project provides hands-on materials for learning Retrieval-Augmented Generation (RAG) techniques for research applications.

## Environment Setup

This project supports uv-only setup or conda+uv. uv is recommended for a quick, lightweight venv.

### UV-only Quick Setup

1. Ensure `uv` is installed (see https://docs.astral.sh/uv/getting-started/). On Linux/macOS:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. From the repo root, create a local venv and install deps:
   ```bash
   ./setup_uv.sh                # CPU-only
   ./setup_uv.sh --gpu          # with GPU extras
   ./setup_uv.sh --kernel llms-rag-workshop  # optional Jupyter kernel
   ```

3. Activate and launch Jupyter Lab:
   ```bash
   source .venv/bin/activate    # .venv\Scripts\activate on Windows
   jupyter lab
   ```

The notebooks expect the demo dataset at `data/demo_corpus.jsonl` (already included).

### Conda + uv (alternative)

1. Create and activate the conda environment:
   ```bash
   conda create -n llms-rag-workshop python=3.11
   conda activate llms-rag-workshop
   ```

2. Install uv in the environment (if not already available):
   ```bash
   conda install -c conda-forge uv
   ```

3. Install dependencies using uv:
   ```bash
   uv pip install -e .
   ```

### Alternative Setup Script

You can also use the provided setup script:
```bash
bash setup_environment.sh
```

## Notebooks

The workshop consists of several Jupyter notebooks:

1. `01_introduction_to_rag.ipynb` - Introduction to RAG concepts
2. `02_document_retrieval_and_embeddings.ipynb` - Document retrieval and embeddings
3. `03_building_simple_rag_pipeline.ipynb` - Building a complete RAG pipeline
4. `04_advanced_retrieval_techniques.ipynb` - Advanced retrieval methods
5. `05_graph_rag.ipynb` - Graph-based RAG
6. `06_practical_research_applications.ipynb` - Real-world applications
7. `07_optional.ipynb` - Optional advanced topics

## Usage

After setting up the environment, launch Jupyter:

```bash
conda activate llms-rag-workshop
jupyter lab
```

## GPU Support

For GPU acceleration (recommended for larger models), install GPU-specific packages:

```bash
uv pip install -e ".[gpu]"
```

Note: This will install `faiss-gpu` instead of `faiss-cpu`. Make sure you have CUDA available.

## Requirements

- Python 3.10 or higher
- conda
- uv (for fast package installation)
- At least 8GB RAM (16GB+ recommended for larger models)
- GPU with CUDA support (optional but recommended)

## Troubleshooting

If you encounter issues with package installation, you can fall back to pip:

```bash
pip install -e .
```

For dependency conflicts, try creating a fresh environment:

```bash
conda env remove -n llms-rag-workshop
conda create -n llms-rag-workshop python=3.11
conda activate llms-rag-workshop
uv pip install -e .
```
