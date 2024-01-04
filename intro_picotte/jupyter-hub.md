# Jupyter Hub service to the Picotte Cluster

Picotte has a Jupyter Hub service that works through a Web browser. To access it, go to

~~~bash
https://picottemgmt.urcf.drexel.edu:8000
~~~

You will need to login with your Picotte username and password:


:::{figure} ../fig/intro_picotte/jupyter-1.png
JupyterHub log in
:::

Once you are logged, the following interface appears:

:::{figure} ../fig/intro_picotte/jupyter-2.png
JupyterHub interface
:::

- `Reservation`: This is available for special requests. 
- `Account`: This is a list of Slurm accounts associated with your Picotte account. Go ahead 
and select `urcfprj`.
- `Partition`: List of partitions available on Picotte. Select `def-sm` for this workshop. 
- `CPU(s)`: This is equivalent to `--cpus-per-task`. Select `1`
- `Memory (in GB)`: This is quivalent to `--mem`. Select `1`
- `GPU(s)`: is available when the `gpu` or `gpulong` partitions are selected. 
- `Wall Time (in hours)`: select `1`. Maximum value is `12`. 

`Jupyter Hub` will launch a job on Picotte with the resource request specified. This job will 
launch a `Jupyter Server` on the compute node, then proxied to the user directly. 

:::{figure} ../fig/intro_picotte/jupyter-3.png
Jupyter Server interface
:::

More details on running Python notebooks and RStudio server can be found at:

https://docs.urcf.drexel.edu/software/jupyterhub/jupyterhub/


