# Deep Learning in Pytorch 

## Instructor
- **Instructor**: Carl Ehrett
- **Office**: 2105 Barre Hall, Clemson University
- **Email**: cehrett@clemson.edu

## Workshop Description
This workshop series introduces the essential concepts in deep learning and walks through the common steps in a deep learning workflow from data loading and preprocessing to training and model evaluation. Throughout the sessions, students participate in writing and executing simple deep learning programs using Pytorch -- a popular Python library for developing, training, and deploying deep learning models.

## Prerequisites
All students should have a Palmetto Cluster account. If you do not already have an account, you can visit our [getting started page](https://docs.rcd.clemson.edu/palmetto/starting). Students should be familiar with the Python programming language. This requirement could be fulfilled by personal projects, coursework, or completion of the Introduction to [Python Programming workshop series](https://clemsonciti.github.io/rcde_workshops/python_programming/00-index.html). Experience in numeric computing with the numpy library is helpful but not required.

## Accessing Workshop Files

You can download the notebooks and their contents as follows. If you are unfamiliar with using the terminal on Palmetto, please take our [self-guided onboarding training](https://docs.rcd.clemson.edu/palmetto/onboarding/).

In the terminal on the cluster, create or navigate to an empty folder. Then run the following command:

```
wget https://raw.githubusercontent.com/clemsonciti/rcde_workshops/master/pytorch/download.sh
```

This will download a script named `download.sh`. Run it with:

```
bash download.sh
```

This will create a folder named `pytorch` containing the notebooks and workshop materials.

## Environment

To run the code in this workshop, you’ll need a Python environment with the appropriate libraries installed. You can create this environment by submitting a job to the cluster.

From the terminal, after downloading the workshop files:

```
cd pytorch
sbatch create_env_pip.sh
```

This will submit a job that creates a Conda environment named `PytorchWorkshop` and installs all required libraries. The job may take up to 30 minutes to complete. You can monitor its progress using:

```
squeue -u $USER
```

Once the job finishes, the environment will be available as a Jupyter kernel named **"Pytorch Workshop"**, which you can select in JupyterLab to run the notebooks.

Note: Notebook 8 contains some code that requires you to have a free [Weights & Biases (WandB)](https://wandb.ai/home) account.

