#!/usr/bin/env python3
"""
Multi-node, multi-GPU “Hello World” inference example for Clemson’s Palmetto cluster.

Every Slurm task simply runs this file, which:
1. Prints the local Slurm + CUDA environment so we can prove that two nodes
   (with two A100 GPUs each) participated in the job.
2. Loads the Qwen/Qwen3-VL-30B-A3B-Instruct model using Hugging Face Transformers,
   requesting bfloat16 weights so the 30B parameter model fits in GPU memory.
3. Relies on `device_map=\"auto\"` so Transformers shards the model across whatever
   GPUs Slurm made visible
4. Generates a tiny greeting that includes the node ID, demonstrating that each
   node ran independently.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime
from typing import List

# Global constant so every step references the exact same model identifier.
MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct" # meta-llama/Llama-3.3-70B-Instruct


def log(message: str) -> None:
    """Small helper that prints and flushes immediately (Slurm buffers aggressively)."""
    print(message, flush=True)


def pretty_header(title: str) -> None:
    """Emit a banner so that each major step is easy to spot in job logs."""
    log("\n" + "=" * 80)
    log(title)
    log("=" * 80)


def dump_slurm_context() -> None:
    """Print the most helpful Slurm variables so users can confirm placement."""
    slurm_keys = [
        "SLURM_JOB_ID",
        "SLURM_PROCID",
        "SLURM_NODEID",
        "SLURM_JOB_NUM_NODES",
        "SLURM_JOB_NODELIST",
        "SLURM_LOCALID",
    ]
    for key in slurm_keys:
        log(f"{key:>22}: {os.environ.get(key, 'not-set')}")
    log(f"{'CUDA_VISIBLE_DEVICES':>22}: {os.environ.get('CUDA_VISIBLE_DEVICES', 'not-set')}")


def report_cuda_devices(torch_module) -> None:
    """List every visible GPU so users can verify both GPUs per node are active."""
    if not torch_module.cuda.is_available():
        log("CUDA is not reporting any devices. Did you request GPUs via Slurm?")
        return

    device_count = torch_module.cuda.device_count()
    log(f"Detected {device_count} CUDA device(s) visible to this process.")
    for idx in range(device_count):
        name = torch_module.cuda.get_device_name(idx)
        capability = torch_module.cuda.get_device_capability(idx)
        total_mem_gb = torch_module.cuda.get_device_properties(idx).total_memory / (1024**3)
        log(
            f"  GPU {idx}: {name} | compute capability {capability} | "
            f"~{total_mem_gb:.1f} GiB"
        )


def build_chat_prompt(node_identifier: str) -> List[dict]:
    """Create a tiny conversation highlighting which node ran the generation."""
    return [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant running on the Clemson Palmetto HPC cluster. "
                "Demonstrate that large language models can speak from different nodes."
            ),
        },
        {
            "role": "user",
            "content": (
                "Please greet the workshop attendees from node "
                f"{node_identifier} and mention you are using multiple GPUs."
            ),
        },
    ]


def main() -> None:
    pretty_header("Palmetto multi-node inference demo starting")
    log(f"Python executable : {sys.executable}")
    log(f"Start timestamp   : {datetime.now().isoformat(timespec='seconds')}")

    # ------------------------------------------------------------------
    # Step 1: Import heavy libraries. We purposely delay these imports so
    #         any import errors are clearly associated with this step.
    # ------------------------------------------------------------------
    pretty_header("Step 1: Importing libraries")
    try:
        import torch
        from transformers import AutoTokenizer, pipeline
    except Exception as exc:  # pragma: no cover - we want to re-raise loudly
        log(f"ERROR during Step 1 (importing libraries): {exc}")
        raise

    # ------------------------------------------------------------------
    # Step 2: Check CUDA + Slurm metadata so users can confirm placement.
    #         Each node prints the same script, so these diagnostics prove
    #         that both nodes/gpus participated.
    # ------------------------------------------------------------------
    pretty_header("Step 2: Checking CUDA environment")
    try:
        dump_slurm_context()
        report_cuda_devices(torch)
    except Exception as exc:
        log(f"ERROR during Step 2 (environment checks): {exc}")
        raise

    # ------------------------------------------------------------------
    # Step 3: Load the tokenizer. For chat models this encapsulates special
    #         tokens plus the chat template needed for role-based prompts.
    # ------------------------------------------------------------------
    pretty_header("Step 3: Loading tokenizer")
    try:
        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_ID,
            trust_remote_code=True,  # Qwen models ship custom helper code.
        )
    except Exception as exc:
        log(f"ERROR during Step 3 (loading tokenizer): {exc}")
        raise

    # ------------------------------------------------------------------
    # Step 4: Load the actual model via the high-level pipeline. We request
    #         bfloat16 weights because A100 GPUs support it efficiently and it
    #         halves the memory footprint compared to float32. The `device_map`
    #         argument lets Transformers automatically shard the model across
    #         the GPUs that Slurm exposed to this process (two per node here).
    #         No manual torch.distributed setup is required for this demo.
    # ------------------------------------------------------------------
    pretty_header("Step 4: Loading model (this can take a few minutes)")
    try:
        text_generator = pipeline(
            task="text-generation",
            model=MODEL_ID,
            tokenizer=tokenizer,
            device_map="auto",  # spread layers across all visible GPUs.
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,  # Qwen uses custom modeling code.
        )
    except Exception as exc:
        log(f"ERROR during Step 4 (loading model): {exc}")
        raise

    # ------------------------------------------------------------------
    # Step 5: Run a tiny generation so users see real output. Every node
    #         calls the same prompt, but we embed the local node ID so logs
    #         reveal which node produced which answer.
    # ------------------------------------------------------------------
    pretty_header("Step 5: Running generation")
    try:
        node_label = os.environ.get("SLURM_NODEID", "unknown-node")
        messages = build_chat_prompt(node_label)
        # The pipeline accepts chat-style messages directly for Qwen models.
        outputs = text_generator(
            messages,
            max_new_tokens=128,
            temperature=0.2,
            do_sample=True,
        )
        log("Model output:")
        if isinstance(outputs, list) and outputs:
            # Qwen chat pipelines usually return [{"generated_text": [...] }].
            generated = outputs[0]
            # Fall back to str() if the exact schema ever changes.
            if isinstance(generated, dict) and "generated_text" in generated:
                log(str(generated["generated_text"]))
            else:
                log(str(generated))
        else:
            log(str(outputs))
    except Exception as exc:
        log(f"ERROR during Step 5 (generation): {exc}")
        raise

    # ------------------------------------------------------------------
    # Step 6: Wrap up so the logs show a clean completion marker.
    # ------------------------------------------------------------------
    pretty_header("Step 6: Done. Model inference finished successfully.")


if __name__ == "__main__":
    main()
