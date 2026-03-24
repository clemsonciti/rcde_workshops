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

In the terminal on the cluster, run the following command:

```
cp -R /project/rcde/cehrett/pytorch-intro/workshop/ ~/
```

This will create a folder named `workshop` in your home directory containing the notebooks and workshop materials.

## Environment

To run the code in this workshop, you’ll need a Python environment with the appropriate libraries installed. For the workshop, I have already created an environment that you can use. It is located at `/project/rcde/cehrett/pytorch-intro/env`. You can use it in JupyterLab via Open OnDemand by supplying the "Virtual environment activation command": 

```
source activate /project/rcde/cehrett/pytorch_intro/env
``` 

Long-term, if you want to be using Pytorch, you should have your own environment that you use. You can create this environment by submitting a job to the cluster. (**You do not need to do this for the workshop, since you can activate the environment as described above.**)

From the terminal, after copying the workshop files:

```
cd workshop
sbatch create_env.sh
```

This will submit a job that creates a Conda environment named `PytorchWorkshopSpr26` and installs all required libraries. The job may take up to 30 minutes to complete. You can monitor its progress using:

```
squeue -u $USER
```

Once the job finishes, the environment will be available as a Jupyter kernel named **"Pytorch Workshop Spr 2026"**, which you can select in JupyterLab to run the notebooks.

