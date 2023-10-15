# Running an interactive job on Picotte

## SLURM

Now, we arrive at the most important part of today's workshop: getting 
on the compute nodes. Compute nodes are the real power of Picotte. Let's 
see which of the compute nodes are available at the moment:

~~~bash
sinfo
~~~

We can see that the cluster is quite busy, but there is a fair amount of 
compute nodes that are available for us. Now, let's request one compute 
node. Please type the following (or paste from the website into your SSH terminal):

~~~bash
srun --nodes=1 --cpus-per-task=2 --mem=4G --time=00:30:00 --pty /bin/bash -l
~~~

It is very important not to make typos, use spaces and upper/lowercases exactly 
as shown, and use the proper punctuation. If you make a mistake, nothing bad 
will happen, but the scheduler won't understand your request.

Now, let's carefully go through the request:

- `srun` means that we are asking the scheduler to grant us access to 
a compute node;
- `--nodes=1` means we are asking for one compute node;
- `--cpus-per-task=2` means that we only need two CPUs on the node (since all 
Picotte compute nodes have at least 48 CPUs, we might share the compute node with 
other users, but it's OK because users who use the same node do not interfere with 
each other);
- `--mem=4gb` means that we are asking for 4 Gb of RAM; again, memory is 
specific to the user, and not shared between different users who use the same node;
- `walltime=00:30:00` means that we are asking to use the node for half an hour; after 
half an hour we will be logged off the compute node if we haven't already disconnected.
- `--pty /bin/bash -l` means that we want to launch `/bin/bash`. The `-l` is the option 
for `/bin/bash`, indicating that we want the Bash shell to behave as if it is launched 
directly from the login node. `--pty` lets Slurm runs this shell in a pseudo terminal 
mode. 

This is actually a very modest request, and the scheduler should grant it right away. 
Sometimes, when we are asking for much substantial amount of resources (for example, 20 nodes 
with 40 cores and 192 Gb of RAM), the scheduler cannot satisfy our request, and will put us 
into the queue so we will have to wait until the node becomes available.

Once the request is granted, you will see something like that:

~~~bash
[lbn28@picotte001 ~]$ srun --nodes=1 --cpus-per-task=2 --mem=4G --time=00:30:00 --pty /bin/bash -l
[lbn28@node047 ~]$ echo ${SLURM_JOBID}
9539478
[lbn28@node047 ~]$ 
~~~

Importantly, you will see the prompt change. Previously, the prompt was 
`<your username>@picotte001`, because you were at the login node. Now, you 
are on a compute node -- in this case, `node047` (you might be on a different 
compute node). You can run the commmand `echo ${SLURM_JOBID}` to see the job ID.

We can see the information about the compute node by using the `scontrol` command:

~~~bash
[lbn28@node047 ~]$ scontrol show nodes node049
NodeName=node049 Arch=x86_64 CoresPerSocket=12
CPUAlloc=42 CPUTot=48 CPULoad=38.44
AvailableFeatures=(null)
ActiveFeatures=(null)
Gres=(null)
NodeAddr=node049 NodeHostName=node049 Version=21.08.8-2
OS=Linux 4.18.0-147.el8.x86_64 #1 SMP Thu Sep 26 15:52:44 UTC 2019
RealMemory=192000 AllocMem=111616 FreeMem=88469 Sockets=4 Boards=1
State=MIXED ThreadsPerCore=1 TmpDisk=864000 Weight=1 Owner=N/A MCS_label=N/A
Partitions=def,def-sm,long
BootTime=2023-09-20T18:36:12 SlurmdStartTime=2023-09-20T18:38:11
LastBusyTime=2023-10-11T20:48:18
CfgTRES=cpu=48,mem=187.50G,billing=48
AllocTRES=cpu=42,mem=109G
CapWatts=n/a
CurrentWatts=0 AveWatts=0
ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s
~~~

You can see that the node has 48 CPUs, no GPUs, and at the moment runs a couple of jobs 
(`CPUAlloc`: 42 cores are allocated out of `CPUTot` of 48). 

To exit the compute node, type:

~~~ bash
exit
~~~

This will bring you back to the login node. See how your prompt has changed to `picotte001`. 
It is important to notice that you have to be on a login node to request a compute node. 
One you are on the compute node, and you want to go to another compute node, you have to 
exit first.

## Slurm partitions

Slurm allows the definition of `partitions`, or `queues`. These abstractions specify 
availabilities and limitations of resources for your job. 

To view all possible partitions:

~~~bash
scontrol show partition
~~~

## Slurm accounts

`Slurm account` (to distinguish with `Picotte login account`) is a Slurm-defined entity 
created to help tracking resource utilization. To view accounts that you are associated 
with, run: 

~~~bash
sacctmgr show user withassoc format=account,user,defaultaccount where user=$USER
~~~


:::{warning}
Please be considerate of others when you issue srun/sbatch. Remember that Picotte is a shared resource. 
Don't request resources you don't plan on actually using. 
:::

:::{important}
It is very important to remember that you shouldn't run computations on the login node, 
because the login node is shared between everyone who logs into Picotte, so your computations will 
interfere with other people's login processes. However, once you are on a compute node, you can run some 
computations, because each user gets their own CPUs and RAM so there is no interference.
:::

## Modules

If you are on the compute node, exit it. Once you get on the login node, type this:

~~~bash
qsub -I -l select=1:ncpus=4:mem=10gb,walltime=2:00:00
~~~

We have a lot of software installed on Picotte, but most of it is organized into *modules*, which need to be loaded. To see which modules are available on Picotte, please type

~~~bash
module avail
~~~

Hit `SPACE` several times to get to the end of the module list. This is a very long list, and you can see that there is a lot of software installed for you. If you want to see which versions of MATLAB are installed, you can type

~~~bash
module avail matlab
~~~

~~~
[dndawso@node0033 ~]$ module avail matlab

------------------------------------------------- /software/AltModFiles --------------------------------------------------
   matlab/MUSC2018b    matlab/2021a    matlab/2021b    matlab/2022a (D)

  Where:
   D:  Default Module

If the avail list is too long consider trying:

"module --default avail" or "ml -d av" to just list the default modules.
"module overview" or "ml ov" to display the number of modules for each name.

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
~~~

Let's say you want to use R. To load the module, you will need to specify its full name.To see which versions of R are available, type

~~~
module avail r
~~~

This will give you a list of all modules which have the letter "r" in them (`module avail` is not very sophisticated). Let's see what happens when you load the R 4.1.3 module:

~~~
module load  r/4.1.3-gcc/9.5.0
module list
~~~

~~~
Currently Loaded Modules:
  1) tcl/8.6.12-gcc/9.5.0       4) openjdk/11.0.15_10-gcc/9.5.0   7) glib/2.72.1-gcc/9.5.0
  2) sqlite/3.38.5-gcc/9.5.0    5) libxml2/2.9.13-gcc/9.5.0       8) cairo/1.16.0-gcc/9.5.0
  3) openssl/1.1.1o-gcc/9.5.0   6) libpng/1.6.37-gcc/9.5.0        9) r/4.1.3-gcc/9.5.0
~~~

R depends on other software to run, so we have configured the R module in a way that when you load it, it automatically loads other modules that it depends on.

To start command-line R, you can simply type
~~~
R
~~~

To quit R, type
~~~
quit()
~~~

:::{admonition} Key Points
- `qsub` sends a request for a compute node to the scheduler.
- Software available on Picotte is organized into modules according to version.
- Modules need to be loaded before use.
:::
