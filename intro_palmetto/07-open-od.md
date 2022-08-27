# Web-based access to the Palmetto Cluster
teaching: 15
exercises: 0
questions:
- "How can I access the Palmetto cluster from a web browser?"
objectives:
- "Logging into Palmetto from a browser."

We have an interface to Palmetto that works through a Web browser. This interface is called "Open On Demand", or OpenOD for short. To access it, go to 

```
https://openod02.palmetto.clemson.edu
```

You will need to login with your Clemson username and password, and perform a DUO check. 

<img src="../fig/openod_dashboard.png" alt="Open OnDemand Dashboard" style="height:400px">

One convenient feature of Open OnDemand is a file browser. In the top left corner, you will see the "Files" button, which will take you to your home diretory or to scratch directory. Click it and explore the files in your file system. You can use this feature to view, edit, and delete files. It is also a convenient way to upload and download the files. You can go to any folder that you have access to by clicking "Go to".

You can also use the web interface to run a terminal on Palmetto. This way, OpenOD becomes an alternative to MobaXTerm or to the Mac Terminal application. To start the terminal, click on `Clusters`, then `Palmetto Shell Access`:

<img src="../fig/openod_shell_access.png" alt="Open OnDemand Shell Menu" style="height:300px">

Enter your account password and do the two-factor identification. This will bring you to the login node of Palmetto:

<img src="../fig/openod_shell.png" alt="Open OnDemand Shell Menu" style="height:500px">

From here, you can run scripts on the login node (such as `checkquota`, `checkqueucfg`, `whatsfree`), and request compute nodes with `qsub`.

You can use OpenOD to run certain applications like Jupyter and Tensorflow notebooks, R Studio, and Matlab. Let's run R Studio. From "Interactive apps", please select "RStudio server":
<img src="../fig/rstudio1.png" style="height:300px">

Please fill out the request as shown on this picture (make sure the queue is set to `skystd` or to `skylm`):
<img src="../fig/rstudio2a.png" style="height:500px">

This is basically a graphical interface to `qsub`. You are asking for 1 compute node, 5 CPUs, 10 GB of memory, no GPU, 1g interconnect (that is, a c1 node), for the walltime duration of 6 hours. Once you are done entering this information, please click the blue "Launch" button at the bottom. It will bring out a new screen:

<img src="../fig/rstudio3.png">

This means your request is being processed. Once the compute node is ready, you will see a blue button under your request saying "Connect to RStudio server":

<img src="../fig/rstudio4.png">

Click on it, and it will start RStudio.

We won't go further into R Studio at this workshop, but if you are interested, please attend our "Introduction to R" workshop.

Thank you for your attention!
