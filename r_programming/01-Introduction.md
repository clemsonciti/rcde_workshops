---
title: "Introduction to R"
teaching: 5 min
exercises: 0
questions: "What is R?"
objectives:
- "Basic Introductory of R"
- "Why using R"
keypoints:
- "Advantage of using R"
---
- R is a language and environment for statistical computing and graphics
- R is developed at Bell Laboratories (formerly AT&T, now Lucent Technologies) by John Chambers and colleagues.
- R provides a wide variety of statistical (linear and nonlinear modelling, classical statistical tests, time-series analysis, classification, clustering, …) and graphical techniques, and is highly extensible. 
- R is available as Free Software 
- R runs on a wide variety of UNIX platforms and similar systems (including FreeBSD and Linux), Windows and MacOS.
- R can be extended (easily) via packages on CRAN (The Comprehensive R Archive Network)

![image](https://user-images.githubusercontent.com/43855029/114046192-a3f0aa80-9856-11eb-9646-995a67c144f9.png)

Users of the Palmetto cluster can run R on Palmetto. The most user-friendly way to do this is to run R Studio through a web interface (Open OnDemand). Let's start it. In your web browser (Chrome, Firefox, Edge, Safari, Opera etc.), please go to

```
https://openod02.palmetto.clemson.edu
```

You will need to login with your Clemson username and password, and perform a DUO check. 

<img src="../fig/openod_dashboard.png" alt="Open OnDemand Dashboard" style="height:400px">

You can use OpenOD to run certain graphical applications applications like Jupyter and Tensorflow notebooks, R Studio, and Matlab. Let's run R Studio. From "Interactive apps", please select "RStudio server":
<img src="../fig/rstudio1.png" style="height:300px">

Please fill out the request as shown on this picture:
<img src="../fig/rstudio2.png" style="height:500px">

This is basically a graphical interface to `qsub`. You are asking for 1 compute node, 5 CPUs, 10 GB of memory, no GPU, 1g interconnect (that is, a c1 node), for the walltime duration of 6 hours. Once you are done entering this information, please click the blue "Launch" button at the bottom. It will bring out a new screen:

<img src="../fig/rstudio3.png">

This means your request is being processed. Once the compute node is ready, you will see a blue button under your request saying "Connect to RStudio server":

<img src="../fig/rstudio4.png">

Click on it, and it will start RStudio. The final screen will be something like

<img src="../fig/rstudio_gui.png" style="width:600px">

