FROM continuumio/miniconda3:latest

COPY ./requirements.txt /opt/rcde_workshops/requirements.txt
RUN conda create -n jupyter-book python==3.10.0 && \
    conda install \
        -n jupyter-book \
        --override-channels \
        -c conda-forge \
        --file /opt/rcde_workshops/requirements.txt

RUN mkdir /app
VOLUME /app
WORKDIR /app

RUN conda init --system bash

RUN apt-get update && \
    apt-get install -y inotify-tools && \
    apt-get clean

RUN useradd --create-home --shell /bin/bash jupyter
USER jupyter
