# Attention, Transformers, and LLMs: a hands-on introduction in Pytorch

## Instructor
- **Instructor**: Carl Ehrett
- **Office**: 2105 Barre Hall, Clemson University
- **Email**: cehrett@clemson.edu

## Workshop Description
This workshop focuses on developing an understanding of the fundamentals of attention and the transformer architecture so that you can understand how LLMs work and use them in your own projects.

## Prerequisites
* **All workshop participants should have a Palmetto Cluster account.** If you do not already have an account, you can visit our [getting started page](https://docs.rcd.clemson.edu/palmetto/starting).
* **Participants should be familiar with the Python programming language.** This requirement could be fulfilled by personal projects, coursework, or completion of the Introduction to [Python Programming workshop series](https://clemsonciti.github.io/rcde_workshops/python_programming/00-index.html).
* **The workshop assumes experience in numeric computing with the numpy, pytorch, tensorflow, or similar.** Participants are encouraged to work through our [Introduction to Deep Learning with Pytorch](https://clemsonciti.github.io/rcde_workshops/pytorch/00-index.html) series if they have no prior Pytorch experience.

## Accessing Workshop Files
You can download the notebooks and their contents as follows.
In the terminal, create or navigate to an empty folder. Run the following command: `wget https://raw.githubusercontent.com/clemsonciti/rcde_workshops/master/pytorch_llm/download.sh`
This copies to your drivespace a script `download.sh` that, when you run it, will copy the full workshop files to your drivespace. So now that you have that script, run it using the command: `bash download.sh`. You should now have a folder, `pytorch_llm`, which contains this notebook and the rest of the workshop.

## Creating a conda environment
In order to run the notebooks in this workshop, you will need a python environment into which you have installed the libraries we will be using. The below instructions will walk you through the process of creating such an environment. For our documentation regarding creating python environments, see the page [here](https://docs.rcd.clemson.edu/openod/apps/jupyter/#adding-new-notebook-kernels).
* Step 1: ssh into the cluster (see instructions [here](https://docs.rcd.clemson.edu/palmetto/connect/ssh/)).
* Step 2: Load miniforge, using the command `module load miniforge3`.
* Step 3: Create the new environment, using the command `conda create --name AttentionWorkshop python=3.12`.
* Step 4: Active the environment. (`source activate AttentionWorkshop`)
* Step 5: Install Pytorch. (`conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia`)
* Step 6: Install the `transformers` and `datasets` libraries. (`conda install -c huggingface transformers datasets`)
* Step 7: Install `ipykernel` so that we can use this environment as a Jupyter notebook kernel. (`conda install ipykernel`)
* Step 8: Install `ipywidgets` since our libraries will use it to display progress bars. (`conda install ipywidgets -c conda-forge`)
* Step 9: Register the environment as a Jupyter kernel. (`python -m ipykernel install --user --name AttentionWorkshop --display-name "AttentionWorkshop"`)
Now you’re ready to visit OpenOnDemand and request a Jupyter session using your new `AttentionWorkshop` environment.
