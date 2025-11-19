"""Offline batch inference demo with vLLM for HPC-scale datasets."""

import argparse

import pandas as pd
import torch
from vllm import LLM, SamplingParams

PROMPT_TEMPLATE = (
    'Please extract from this tweet any factual claims about politics. '
    'Present all claims as a bullet point list, with one claim per line, and no other text. '
    'Do not include opinions, commentary, or subjective statements. '
    'If there are no factual political claims, say "NONE". Tweet: "{tweet}"'
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Batch all tweets into one vLLM.generate() call for max throughput."
    )
    parser.add_argument("--input-csv", default="synthetic_tweets.csv")
    parser.add_argument("--output-csv", default="tweet_claims.csv")
    parser.add_argument("--model", default="Qwen/Qwen3-VL-4B-Instruct")
    parser.add_argument("--batch-size", type=int, default=64)
    args = parser.parse_args()

    # Read once so the rows stay in order; 100 tweets are trivial to hold in RAM - larger datasets will require sharding.
    df = pd.read_csv(args.input_csv)
    if df.empty:
        raise ValueError("Input CSV is empty; nothing to infer on.")

    # Build the prompts before hitting the GPU. Clean quotes so the template stays valid.
    prompts = [
        PROMPT_TEMPLATE.format(tweet=str(text).replace('"', "'"))
        for text in df["tweet_text"]
    ]

    # Greedy decoding + fixed seed keeps outputs (mostly!) deterministic.
    sampling_params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=128, seed=42)

    # One shard per CUDA device keeps tensor parallelism simple; warn if we fall back to CPU.
    tp_size = torch.cuda.device_count() if torch.cuda.is_available() else 1
    if tp_size == 1 and not torch.cuda.is_available():
        print("Warning: CUDA not detected; vLLM on CPU is functionally correct but slow.")

    # vLLM's PagedAttention + continuous batching squeeze every byte of GPU RAM, so init once and reuse.
    llm = LLM(
        model=args.model,
        tensor_parallel_size=max(tp_size, 1),
        gpu_memory_utilization=0.9,
    )

    # Chunk prompts so memory stays bounded even when the dataset grows to millions of rows.
    outputs = []
    batch_size = max(1, args.batch_size)
    for start in range(0, len(prompts), batch_size):
        batch = prompts[start : start + batch_size]
        generations = llm.generate(batch, sampling_params)
        outputs.extend(
            (gen.outputs[0].text.strip() if gen.outputs else "") for gen in generations
        )

    # Persist tweet metadata, prompt, and model output for downstream scoring or inspection.
    df_out = pd.DataFrame(
        {
            "tweet_id": df["tweet_id"],
            "tweet_text": df["tweet_text"],
            "prompt": prompts,
            "model_output": outputs,
        }
    )
    df_out.to_csv(args.output_csv, index=False)
    print(f"Wrote {len(df_out)} rows with model outputs to {args.output_csv}")


if __name__ == "__main__":
    main()
