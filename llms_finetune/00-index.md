# Fine-tuning LLMs on Palmetto

## Instructor
- **Instructor**: Carl Ehrett
- **Office**: 2105 Barre Hall, Clemson University
- **Email**: cehrett AT clemson DOT edu

## Workshop Description
This workshop series introduces essential concepts related to the fine-tuning of large language models (LLMs), and teaches how to fine-tune an LLM using PyTorch on Palmetto. Topics include: when fine-tuning is appropriate (and when it is not the right solution), parameter-efficient fine-tuning methods vs. full fine-tuning, and what kind and quantity of data is required for fine-tuning. Participants will learn how to efficiently use Palmetto resources to fine-tune (pre-trained) LLMs.

## Prerequisites
* **All workshop participants should have a Palmetto Cluster account.** If you do not already have an account, you can visit our [getting started page](https://docs.rcd.clemson.edu/palmetto/starting).
* **Participants should be familiar with the Python programming language.** This requirement could be fulfilled by personal projects, coursework, or completion of the [Introduction to Python Programming workshop series](https://clemsonciti.github.io/rcde_workshops/python_programming/00-index.html).
* **Participants should have experience running (inferencing) LLMs through code**. This requirement could be satisfied by, e.g., completion of the [Attention, Transformers, and LLMs](https://clemsonciti.github.io/rcde_workshops/pytorch_llm/00-index.html) or the [Running LLMs on Palmetto](https://github.com/clemsonciti/rcde_workshops/tree/master/llms_inference) workshop series, or by personal experience.

## Accessing Workshop Files
You can download the notebooks and their contents as follows.
In the terminal, create or navigate to an empty folder. Run the following command: `wget https://raw.githubusercontent.com/clemsonciti/rcde_workshops/master/llms_finetune/download.sh`
This copies to your drivespace a script `download.sh` that, when run, will copy the full workshop files to your drivespace. So now that you have that script, run the command: `bash download.sh`. You should now have a folder, `llms_finetune`, which contains the workshop files.

## Environment
To run the code in this workshop, you will need a python environment with the appropriate libraries installed. You can create such an environment as follows. 

Navigate to the directory where the workshop contents are stored. Submit the script `create_env.sh` as a job, by running the command `sbatch create_env.sh`. This will create a conda environment named `LLMsFT`. (This will take a while; up to 60 minutes.) You can then use that environment as the Jupyter kernel to run the notebooks in this environment.

Alternatively, if you'd rather run the script interactively: in the terminal (and not in JupyterLab), get an interactive session using `salloc --mem=12GB --time=01:30:00`. In the directory where the workshop contents are stored, run `bash create_env.sh`.

## Other setup needed
In order to use the code in the Workshop notebooks, you will need a Hugging Face account. You can create one [here](https://huggingface.co/join). After doing so, you should get an *Access Token* for your Hugging Face account ([here](https://huggingface.co/settings/tokens)). You should then connect your `LLMsFT` python env to your Hugging Face account by activating that python env in a terminal on the cluster, and running `huggingface-cli login`. You will be prompted to supply your access token. It is recommended that you also add the line `export HF_HOME=/scratch/[YOUR PALMETTO USERNAME]/hf_cache/` to your `~/.bashrc` file, so that pre-trained LLMs will be downloaded to your `scratch` drive.

The code in notebook 05, on logging, requires you to have a (free) [Weights and Biases](https://wandb.ai/site) account.