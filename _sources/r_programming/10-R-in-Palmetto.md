---
title: "R in Palmetto"
teaching: 10
exercises: 0
questions:
- "How to run R scripts in Palmetto"
objectives:
- "Learn how to run R in Palmetto"
- "Learn how to install R packages in Palmetto"
keypoints:
- "Rscript"
---

If you need to process a large amount of data and you think your laptop / desktop is not fast enough, you can utilize the power of the Palmetto supercomputing cluster. If you have an account on Palmetto, you can log in as described in [our manual](https://www.palmetto.clemson.edu/palmetto/basic/login/).

Let's request a compute node:
```bash
qsub -I -l select=1:ncpus=4:mem=32gb:interconnect=fdr,walltime=2:00:00
```

In order to run R, you will first need to load the R module. We have several versions of R installed on Palmetto, most recent being 4.0.3:

```bash
module load r/4.0.3-gcc/8.4.1
```

We can now open R in interactive mode (text-only console). Let's install a package `doParallel`:

```bash
R
> install.packages("doParallel")
```

To quit the R console, type `quit()`. Let's create a simple script and run it. We can use the text editor called `nano`:

```bash
nano randmatrix.r
```

This will open a text editor. Let's paste these lines which create a random 4x4 matrix (to paste, Mac users can use Cmd+V, and PC users can use Shift+Ins):
```
M <- matrix(rnorm(16), nrow=4)
M
```

Let's save it by pressing Ctrl+O, then Enter, then Ctrl+X. We can run this script with the `RScript` command:

```bash
Rscript randmatrix.r
```

If you want to use RStudio on Palmetto, you can use OpenOnDemand interface -- please see our [manual](https://www.palmetto.clemson.edu/palmetto/openondemand/intro/).
