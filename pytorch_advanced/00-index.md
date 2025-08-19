# Advanced Deep Learning in Pytorch 

## Instructor
- **Instructor**: Carl Ehrett
- **Office**: 2105 Barre Hall, Clemson University
- **Email**: cehrett@clemson.edu

## Workshop Description
Welcome to the advanced pytorch workshop series. In this series we will start with a simple deep learning example and then iteratively add in more advanced approaches and tooling. We will work through the following techniques: 
* Downloading and fine-tuning pre-trained models
* Script-based development workflow
* Organizing model code with [Pytorch Lightning](https://www.lightning.ai/)
    * Checkpointing
* Experiment tracking with [Weights & Biases](https://wandb.ai/site)
* Using multiple-GPUs
    * Using pytorch syntax
    * In Pytorch Lightning
    * Profiling GPU usage
* Reproducible research with Pytorch
    * Version control
    * Setting random seeds
    * Logging results
* Hyperparameter tuning
    * Bash scripting
    * Using Sweeps

## Prerequisites
All students should have a Palmetto Cluster account. If you do not already have an account, you can visit our [getting started page](https://docs.rcd.clemson.edu/palmetto/starting). Students must have basic familiarity with Python programming and a good grasp of Pytorch fundamentals. This requirement is satisified by taking the the [introductory pytorch series](https://clemsonciti.github.io/rcde_workshops/pytorch/00-index.html) or other experience using Pytorch. 

## Accessing Workshop Files
You can download the notebooks and their contents as follows.
In the terminal, create or navigate to an empty folder. Run the following command: `wget https://raw.githubusercontent.com/clemsonciti/rcde_workshops/master/pytorch_advanced/download.sh`
This copies to your drivespace a script `download.sh` that, when run, will copy the full workshop files to your drivespace. So now that you have that script, run the command: `bash download.sh`. You should now have a folder, `pytorch_advanced`, which contains the workshop files.

## Environment
To run the code in this workshop, you will need a python environment with the appropriate libraries installed. You can create such an environment as follows. 

Navigate to the directory where the workshop contents you downloaded are stored. Submit the script `create_env.sh` as a job, by running the command `sbatch create_env.sh` from the directory containing the workshop files. This will create a conda environment named `PytorchWorkshop`. (This will take a while; up to 20 minutes.) You can then use that environment as the Jupyter kernel to run the notebooks in this environment.

Alternatively, if you'd rather run the script interactively: in the terminal (and not in JupyterLab), get an interactive session using `salloc --mem=12GB --time=01:30:00`. In the directory where the workshop contents are stored, run `bash create_env.sh`.

Some of the code, related to logging, requires you to have a (free) [Weights and Biases](https://wandb.ai/site) account.