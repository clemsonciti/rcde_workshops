from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import torch.distributed as dist
import os
import logging
from datetime import datetime

def setup_logging():
    rank = dist.get_rank() if dist.is_initialized() else 0
    logging.basicConfig(
        level=logging.INFO,
        format=f"%(asctime)s - Rank {rank} - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

def main():
    # Initialize distributed process group
    dist.init_process_group("nccl")
    global_rank = dist.get_rank()
    local_rank = int(os.environ['LOCAL_RANK'])
    world_size = dist.get_world_size()
    torch.cuda.set_device(local_rank)
    
    logger = setup_logging()
    logger.info(f"Initialized process group. Global rank: {global_rank}, Local rank: {local_rank}, World size: {world_size}")

    try:
        # Load model and tokenizer
        logger.info("Loading model and tokenizer...")
        start_time = datetime.now()
        
        tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")
        model = AutoModelForCausalLM.from_pretrained(
            "meta-llama/Llama-3.2-1B-Instruct",
            torch_dtype=torch.float16,
            device_map="auto"
        ).to(local_rank)
        
        load_duration = datetime.now() - start_time
        logger.info(f"Model loaded in {load_duration.total_seconds():.2f}s")

        # Example prompts
        prompts = [
            "The future of artificial intelligence is",
            "Renewable energy solutions are critical because",
        ]

        # Split prompts across processes
        chunk_size = len(prompts) // world_size
        start_idx = global_rank * chunk_size
        end_idx = start_idx + chunk_size if global_rank != world_size - 1 else len(prompts)
        local_prompts = prompts[start_idx:end_idx]
        
        logger.info(f"Processing {len(local_prompts)} prompts starting at index {start_idx}")

        # Process local prompts
        results = []
        for idx, prompt in enumerate(local_prompts):
            logger.info(f"Processing prompt {idx+1}/{len(local_prompts)}: {prompt[:50]}...")
            
            inputs = tokenizer(prompt, return_tensors="pt").to(local_rank)
            outputs = model.generate(
                **inputs,
                max_new_tokens=100,
                temperature=0.7,
                do_sample=True
            )
            results.append(tokenizer.decode(outputs[0], skip_special_tokens=True))

        # Gather results
        logger.info("Gathering results...")
        gathered_results = [None] * world_size
        dist.gather_object(results, gathered_results if global_rank == 0 else None, dst=0)

        # Save results from rank 0
        if global_rank == 0:
            all_results = [res for sublist in gathered_results for res in sublist]
            with open("inference_results.txt", "w") as f:
                for idx, result in enumerate(all_results):
                    f.write(f"Prompt {idx + 1}:\n{result}\n\n")
            logger.info("Inference complete. Results saved to inference_results.txt")

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)
        raise
    finally:
        dist.destroy_process_group()
        logger.info("Process group destroyed")

if __name__ == "__main__":
    main()