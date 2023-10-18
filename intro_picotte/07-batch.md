# Running a batch job

Interactive jobs are great if you need to do something quick, or perhaps visualize some data. 
If you have some code which runs for seven hours, interactive jobs are not a great idea. Please 
keep in mind that an interactive job gets killed if you close the SSH connection. So for example, 
you connect to Picotte from your laptop, start an interactive job, but then your laptop runs out 
of battery power and you can't find your charger. SSH client quits, and your interactive job is killed.

If you have some truly serious, multi-hour computation project (and that's what Picotte is really 
good for), a better idea is to run it on the background. This is called a *batch job*. You submit 
it in a fashion which is conceptually similar to an interactive job, but then it runs on the compute 
node on the background until it's over. If it needs to take two days, it takes two days. You can quit 
the SSH client or close your laptop, it won't affect the batch job.

To submit a batch job, we usually create a separate file called a *Slurm script*. This file asks the 
scheduler for specific resources, and then specifies the actions that will be done once we get on a 
compute node.

Let us go through an example. We will use batch mode to create a small random matrix with 
normally-distributed values. We will create two scripts: an R script which does the computation, 
and a Slurm script which will execute the R script on a compute node in batch mode.

Picotte has a simple text editor which is called `nano`. It doesn't offer any fancy formatting, 
but it suffices for ceating and editing simple texts. Let's go to our home directory and create the 
R script:

~~~bash
cd
nano randmatrix.R
~~~

This will open the `nano` text editor:

:::{figure} ../fig/intro_Picotte/nano_empty.png
Nano just opened with empty file.
:::

Inside the editor, type this:

~~~R
size <- 5000
M <- matrix(rnorm(size*size), nrow=size)
ev <- eigen(M)
values <- ev$values
values[1]
~~~

Instead of typing, you can copy the text from the Web browser and paste it into `nano`. Windows users 
can paste with `Shift`+`Ins` (or by right-clicking the mouse). Mac users can paste with `Cmd`+`V`. At 
the end, your screen should look like this:

:::{figure} ../fig/intro_Picotte/nano_r.png
Nano with the R script filled in
:::

To save it, press `Ctrl`+`O`, and hit enter. To exit the editor, press `Ctrl`+`X`. To make sure the text is 
saved properly, print it on screen using the `cat` command:

~~~bash
cat randmatrix.R
~~~

Now, let's create the Slurm script:

~~~bash
nano randmatrix.sh
~~~

Inside the `nano` text editor, type this (or paste from the Web browser):

~~~bash
#!/bin/bash
#
#SBATCH --job-name=random_matrix
#SBATCH --account=urcfprj
#SBATCH --partition=def-sm
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=1GB
#SBATCH --time=0:30:00

module load R/4.2.2
Rscript randmatrix.R
~~~

Let's go through the script, line by line. The first cryptic line says that it's a script that is 
executed by the Linux shell. The next line is empty, followed by five lines that are the instructions 
to the scheduler (they start with `#SBATCH`):

- `--job-name` specifies the name of the job;
- `--partition`: specify the resource partition this job is going to
- `--account`: specify the **Slurm account** this job is going to
- `--nodes=1` means we are asking for one compute node;
- `--ntasks-per-node=1` means we are asking to run 1 process per node;
- `--cpus-per-task=2` means that we only need two CPUs on the node 
- `--mem=1gb` means that we are asking for 1 Gb of RAM; 
- `time=00:30:00` means that we are asking to use the node for half an hour; 

A very common question is how much time we should ask for. It's a tricky question because 
there is no way of knowing how much time you will need until you actually try it. One rule of 
thumb is: make a rough guess, and ask for twice as much.

Now, let's submit our batch job!

~~~bash
[lbn28@picotte001 ~]$ sbatch randmatrix.sh
Submitted batch job 9539504
[lbn28@picotte001 ~]$
~~~

If the submission was successful, it will give you the job ID, as shown above. 
We can monitor the job's progress with the `qstat` command. This is an example to list 
all jobs that are currently executed by you:

~~~bash
[lbn28@picotte001 ~]$ squeue -u lbn28
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           9539504    def-sm random_m    lbn28  R       0:42      1 node047
[lbn28@picotte001 ~]$
~~~

You see the job ID, your Picotte username, the name of the queue (more on that later), 
the name of the job (`random_matrix`), and the node(s) the job is placed on. 

Wait a little bit and do `scontrol` again (you can hit the `UP` arrow to show the previous command). 
`TIME` should now be a bit longer. The script should take a few minutes or so to execute. 

If everything went well, you should now see the file `slurm-9539504.out`. Let's print it on screen:

~~~bash
[lbn28@picotte001 ~]$ cat slurm-9539504.out
[1] 25.87044+66.89629i
[lbn28@picotte001 ~]$
~~~

We can look at the performance of the job

~~~bash
[lbn28@picotte001 ~]$ seff 9539504
Job ID: 9539504
Cluster: picotte
User/Group: lbn28/lbn28
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 00:01:15
CPU Efficiency: 81.52% of 00:01:32 core-walltime
Job Wall-clock time: 00:00:46
Memory Utilized: 662.08 MB
Memory Efficiency: 64.66% of 1.00 GB
[lbn28@picotte001 ~]$
~~~

We want to make sure that `CPU Efficiency` and `Memory Efficiency` are as closed to `100%` as 
possible. If you increased the `--cpus-per-task=` value to `4`, you will see that the 
efficiency values are reduced, indicitating that you asked for more resources and not able to 
utilize all of them. 

How many jobs can you run at the same time? It depends on how much resources you ask for. If 
each job asks for a small amount of resources, you can do a large amount of jobs simultaneously. 
If each job needs a large amount of resources, only a few of them can be running simultaneously, 
and the rest of them will be waiting in the queue until the jobs that are running are completed. 
This is a way to ensure that Picotte is used fairly.

