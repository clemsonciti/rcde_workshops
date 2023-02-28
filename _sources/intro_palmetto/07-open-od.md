# Web-based access to the Palmetto Cluster

We have an interface to Palmetto that works through a Web browser. This interface is called "Open On Demand", or OpenOD for short. To access it, go to

```
https://openod.palmetto.clemson.edu
```

You will need to login with your Clemson username and password, and perform a DUO check.


:::{figure} ../fig/intro_palmetto/openod_1.png
Open OnDemand MOTD
:::

## File Browsing

One convenient feature of Open OnDemand is a file browser. In the top left corner, you will see the "Files" button, which will take you to your home diretory or to scratch directory. Click it and explore the files in your file system. You can use this feature to view, edit, and delete files. It is also a convenient way to upload and download the files. You can go to any folder that you have access to by clicking "Go to".

## Shell

You can also use the web interface to run a terminal on Palmetto. This way, OpenOD becomes an alternative to MobaXTerm or to the Mac Terminal application. To start the terminal, click on `Clusters`, then `Palmetto Shell Access`:

:::{figure} ../fig/intro_palmetto/openod_2.png
Palmetto Shell Access
:::

Enter your account password and do the two-factor identification. This will bring you to the login node of Palmetto:

:::{figure} ../fig/intro_palmetto/openod_3.png
Palmetto Shell Access -- On login node
:::

From here, you can run scripts on the login node (such as `checkquota`, `checkqueucfg`, `whatsfree`), and request compute nodes with `qsub`.

:::{warning}
There is currently an idle timeout that happens when you use the shell access feature of Open
OnDemand.  If you are inactive for a period of time, the shell will need to be restarted.
:::

## Jupyter Notebook

You can use OpenOD to run certain applications like Jupyter and Tensorflow notebooks, R Studio, and Matlab. Let's run Jupyter. From "Interactive apps", please select "Jupyter Notebook":

:::{figure} ../fig/intro_palmetto/openod_4.png
Select Jupyter Notebook
:::

Please fill out the request as shown on this picture:

:::{figure} ../fig/intro_palmetto/openod_5.png
Fill Jupyter Notebook Options
:::

This is basically a graphical interface to `qsub`. You are asking for 1 compute node, 5 CPUs, 10 GB of memory, no GPU, 1g interconnect (that is, a c1 node), for the walltime duration of 1 hours. Once you are done entering this information, please click the blue "Launch" button at the bottom. It will bring out a new screen:

:::{figure} ../fig/intro_palmetto/openod_6.png
Jupyter Notebook is starting
:::

This means your request is being processed. Once the compute node is ready, you will see a blue button under your request saying "Connect to Jupyter":

:::{figure} ../fig/intro_palmetto/openod_7.png
Connect to Jupyter
:::

Click on it, and it will start Jupyter.

We won't go further into Jupyter notebooks at this workshop.  To exit the interactive app, you can
close the browser tab, but that won't stop the underlying job.  Those resources will still be
locked.  To stop the job, select the "my interactive sessions" icon at the top:

:::{figure} ../fig/intro_palmetto/openod_8.png
My Interactive Sessions icon
:::

You can then press the Delete button on the session you are done with.

:::{figure} ../fig/intro_palmetto/openod_9.png
Press the red Delete button to stop the job and release the resources back to the cluster
:::

:::{admonition} Key Points
- Open OnDemand can be used to launch interactive applications with a GUI that run on Palmetto
- Open OnDemand has a file browser
:::
