FROM continuumio/miniconda3:latest

COPY ./requirements.txt /opt/rcde_workshops/requirements.txt
RUN conda create -n jupyter-book python==3.10.0 && \
    conda install \
        -n jupyter-book \
        --override-channels \
        -c conda-forge \
        --file /opt/rcde_workshops/requirements.txt

RUN conda init --system bash

RUN apt-get update && \
    apt-get install -y inotify-tools python3-pyinotify && \
    apt-get clean

# Add system packages to the conda environment so that pyinotify will be found.
RUN echo "/usr/lib/python3/dist-packages" >> \
    /opt/conda/envs/jupyter-book/lib/python3.10/site-packages/system-global.pth

RUN mkdir /app
VOLUME /app
WORKDIR /app

RUN useradd --create-home --shell /bin/bash jupyter
USER jupyter
