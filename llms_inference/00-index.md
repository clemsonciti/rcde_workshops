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

## Environment
To run the code in this workshop, you will need a python environment with the appropriate libraries installed. I have created such an environment in a shared space, but that environment will not always be available to you. You can create such an environment yourself as follows. 

To set up your Python environment, load the Anaconda module provided on Palmetto (e.g., `module load anaconda3/2023.09-0`), which gives you access to the `conda` tool. Then create and activate your own conda environment (for example, `conda create -n llm_workshop python=3.11 && conda activate llm_workshop`). After that, install any additional packages your code requires — either one by one using `pip install packagename`, or from a `requirements.txt` file if you have one.ß

## Hugging Face Hub
In order to use the code in the Workshop notebooks, you will need a Hugging Face account. You can create one [here](https://huggingface.co/join).


