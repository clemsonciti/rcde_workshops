# Deep Learning in Pytorch 

## Instructor
- **Instructor**: Carl Ehrett
- **Office**: 2105 Barre Hall, Clemson University
- **Email**: cehrett AT clemson DOT edu

## Workshop Description
This workshop series introduces the essential concepts in deep learning and walks through the common steps in a deep learning workflow from data loading and preprocessing to training and model evaluation. Throughout the sessions, students participate in writing and executing simple deep learning programs using Pytorch -- a popular Python library for developing, training, and deploying deep learning models.

## Prerequisites
All students should have a Palmetto Cluster account. If you do not already have an account, you can visit our [getting started page](https://docs.rcd.clemson.edu/palmetto/starting). Students should be familiar with the Python programming language. This requirement could be fulfilled by personal projects, coursework, or completion of the Introduction to [Python Programming workshop series](https://clemsonciti.github.io/rcde_workshops/python_programming/00-index.html). Experience in numeric computing with the numpy library is helpful but not required.

## Accessing Workshop Files
You can download the notebooks and their contents as follows.
In the terminal, create or navigate to an empty folder. Run the following command: `wget https://raw.githubusercontent.com/clemsonciti/rcde_workshops/master/pytorch/download.sh`
This copies to your drivespace a script `download.sh` that, when run, will copy the full workshop files to your drivespace. So now that you have that script, run the command: `bash download.sh`. You should now have a folder, `pytorch`, which contains this notebook and the rest of the workshop.

## Environment
To run the code in this workshop, you will need a python environment with the appropriate libraries installed. You can create such an environment as follows. 
In the terminal (and not in JupyterLab), get an interactive session using `salloc --mem=12GB`. Use `module load miniforge3` to load miniforge. In the directory where the workshop contents are stored, run `bash create_pytorch_env.sh`. Running that script will create a conda environment named `PytorchWorkshop`. (This will take a while; up to 20 minutes.) You can then use that environment as the Jupyter kernel to run the notebooks in this environment. (Notebook 8 contains some code which will require you to have a free [WandB](https://wandb.ai/home) account.)
