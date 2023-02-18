# Introduction to R

## Overview

```{admonition} The R programming language
:class: dropdown

- R is a language and environment for statistical computing and graphics
- R is developed at Bell Laboratories (formerly AT&T, now Lucent Technologies) 
by John Chambers and colleagues.
- R provides a wide variety of statistical (linear and nonlinear modelling, 
classical statistical tests, time-series analysis, classification, clustering, …) 
and graphical techniques, and is highly extensible. 
- R is available as Free Software 
- R runs on a wide variety of UNIX platforms and similar systems (including FreeBSD 
and Linux), Windows and MacOS.
- R can be extended (easily) via packages on CRAN (The Comprehensive R Archive Network)

```


```{admonition} R and RStudio on Palmetto
:class: dropdown

Users of the Palmetto cluster can run R on Palmetto. The most user-friendly way to do this 
is to run R Studio through a web interface (Open OnDemand). Let's start it. In your web 
browser (Chrome, Firefox, Edge, Safari, Opera etc.), please go to

https://openod.palmetto.clemson.edu

```


```{admonition} R/RStudio procedure
:class: dropdown

You will need to login with your Clemson username and password, and perform a DUO check. 

![Open OnDemand Dashboard](../fig/r_programming/openod_dashboard.png)

You can use OpenOD to run certain graphical applications applications like Jupyter 
and Tensorflow notebooks, R Studio, and Matlab. Let's run R Studio. From `Interactive apps`, 
please select `RStudio server`:

![RStudio](../fig/r_programming/rstudio1.png)

Please fill out the request as shown on this picture:

![Open OnDemand Dashboard](../fig/r_programming/rstudio2.png)

This is basically a graphical interface to `qsub`. You are asking for 1 compute node, 
5 CPUs, 10 GB of memory, no GPU, 1g interconnect (that is, a c1 node), for the walltime 
duration of 6 hours. Once you are done entering this information, please click the blue 
`Launch` button at the bottom. It will bring out a new screen:

![Open OnDemand Dashboard](../fig/r_programming/rstudio3.png)

This means your request is being processed. Once the compute node is ready, 
you will see a blue button under your request saying `Connect to RStudio server`:

![Open OnDemand Dashboard](../fig/r_programming/rstudio4.png)

Click on it, and it will start RStudio. The final screen will be something like

![Open OnDemand Dashboard](../fig/r_programming/rstudio_gui.png)

```

