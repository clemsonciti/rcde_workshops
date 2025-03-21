# Running LLMs on Palmetto

## Instructor
- **Instructor**: Carl Ehrett
- **Office**: 2105 Barre Hall, Clemson University
- **Email**: cehrett AT clemson DOT edu

## Workshop Description
This workshop series introduces essential concepts related to LLMs and works through the common steps in an LLM inference workflow. This workshop focuses on efficiently running LLMs, rather than on constructing, training or fine-tuning them. Throughout the sessions, students will learn how to use the Hugging Face Transformers library to run LLMs on the Palmetto Cluster. The workshop will also cover how to use the Palmetto Cluster to run LLMs on large datasets and how to use the Palmetto Cluster to run LLMs on multiple GPUs and multiple nodes.

## Prerequisites
* **All workshop participants should have a Palmetto Cluster account.** If you do not already have an account, you can visit our [getting started page](https://docs.rcd.clemson.edu/palmetto/starting).
* **Participants should be familiar with the Python programming language.** This requirement could be fulfilled by personal projects, coursework, or completion of the Introduction to [Python Programming workshop series](https://clemsonciti.github.io/rcde_workshops/python_programming/00-index.html).

## Accessing Workshop Files
You can download the notebooks and their contents as follows.
In the terminal, create or navigate to an empty folder. Run the following command: `wget https://raw.githubusercontent.com/clemsonciti/rcde_workshops/master/llms_inference/download.sh`
This copies to your drivespace a script `download.sh` that, when run, will copy the full workshop files to your drivespace. So now that you have that script, run the command: `bash download.sh`. You should now have a folder, `llms_inference`, which contains the workshop files.

## Environment
To run the code in this workshop, you will need a python environment with the appropriate libraries installed. You can create such an environment as follows. 

Navigate to the directory where the workshop contents are stored. Submit the script `create_env.sh` as a job, by running the command `sbatch create_env.sh`. This will create a conda environment named `LLMsInferenceWorkshop`. (This will take a while; up to 60 minutes.) You can then use that environment as the Jupyter kernel to run the notebooks in this environment.

Alternatively, if you'd rather run the script interactively: in the terminal (and not in JupyterLab), get an interactive session using `salloc --mem=12GB --time=01:30:00`. In the directory where the workshop contents are stored, run `bash create_env.sh`.

## Hugging Face Hub
In order to use the code in the Workshop notebooks, you will need a Hugging Face account. You can create one [here](https://huggingface.co/join).


