# Running an interactive job on Palmetto

## QSUB

Now, we arrive at the most important part of today's workshop: getting on the compute nodes. Compute nodes are the real power of Palmetto. Let's see which of the compute nodes are available at the moment:

```
whatsfree
```

We can see that the cluster is quite busy, but there is a fair amount of compute nodes that are available for us. Now, let's request one compute node. Please type the following (or paste from the website into your SSH terminal):

```bash
qsub -I -l select=1:ncpus=4:mem=10gb:interconnect=1g,walltime=2:00:00
```

It is very important not to make typos, use spaces and upper/lowercases exactly as shown, and use the proper punctuation (note the `:` between `ncpus` and `mem`, and the `,` before walltime). If you make a mistake, nothing wrong will happen, but the scheduler won't understand your request.

Now, let's carefully go through the request:

- `qsub` means that we are asking the scheduler to grant us access to a compute node;
- `-I` means it's an interactive job (we'll talk about it in a bit);
- `-l` is the list of resource requirements we are asking for;
- `select=1` means we are asking for one compute node;
- `ncpus=4` means that we only need four CPUs on the node (since all Palmetto compute nodes have at least 8 CPUs, we might share the compute node with other users, but it's OK because users who use the same node do not interfere with each other);
- `mem=10gb` means that we are asking for 10 Gb of RAM (you shouldn't ask for less than 8 Gb); again, memory is specific to the user, and not shared between different users who use the same node);
- `interconnect=1g` is the type of interconnect (the allowed types are `1g`, `10ge`, `fdr`, `hdr`, and `any`). If you look at the output of `whatsfree` and `cat /etc/hardware-table`, you will see the different CPU/RAM configurations that are available for these three types of interconnect. Typically, but not always, `1g` nodes have less RAM and a smaller number of CPUs than `fdr` and `hdr` (with the `hdr` nodes being the most powerful interms of RAM and CPUs).
- finally, `walltime=2:00:00` means that we are asking to use the node for 2 hours; after two hours we will be logged off the compute node if we haven't already disconnected.

This is actually a very modest request, and the scheduler should grant it right away. Sometimes, when we are asking for much substantial amount of resources (for example, 20 nodes with 40 cores and 370 Gb of RAM), the scheduler cannot satisfy our request, and will put us into the queue so we will have to wait until the node becomes available.

Once the request is granted, you will see something like that:

```
[dndawso@login002 ~]$ qsub -I -l select=1:ncpus=4:mem=10gb:interconnect=1g,walltime=2:00:00
qsub (Warning): Interactive jobs will be treated as not rerunnable
qsub: waiting for job 74956.pbs02 to start
qsub: job 74956.pbs02 ready

[dndawso@node0033 ~]$
```

Importantly, you will see the prompt change. Previously, the prompt was <your username>@login002, because you were at the login node. Now, you are on a compute node -- in this case, `node0033` (you might be on a different compute node). You can also see the job ID, in this case it is `74956.pbs02`.


We can see the information about the compute node by using the `pbsnodes` command:

```bash
pbsnodes node0033
```

Here is the information about the node that I was assigned to (node0033):

```
node0033
     Mom = node0033.palmetto.clemson.edu
     ntype = PBS
     state = free
     pcpus = 8
     Priority = 1
     jobs = 61932.pbs02/0, 74956.pbs02/1, 74956.pbs02/2, 74956.pbs02/3, 74956.pbs02/4
     resources_available.arch = linux
     resources_available.chip_manufacturer = intel
     resources_available.chip_model = xeon
     resources_available.chip_type = e5520
     resources_available.host = node0033
     resources_available.hpmem = 0b
     resources_available.interconnect = 1g, any
     resources_available.make = dell
     resources_available.manufacturer = dell
     resources_available.mem = 31876mb
     resources_available.model = r610
     resources_available.ncpus = 8
     resources_available.ngpus = 0
     resources_available.node_make = dell
     resources_available.node_manufacturer = dell
     resources_available.node_model = r610
     resources_available.phase = 1a
     resources_available.qcat = c1_workq_qcat, c1_solo_qcat, osg_qcat, phase01a_qcat, mx_qcat, gilligan_qcat
     resources_available.ssd = False
     resources_available.vmem = 32836mb
     resources_available.vnode = node0033
     resources_available.vntype = cpu_node
     resources_assigned.accelerator_memory = 0kb
     resources_assigned.hbmem = 0kb
     resources_assigned.mem = 1048576kb
     resources_assigned.naccelerators = 0
     resources_assigned.ncpus = 1
     resources_assigned.ngpus = 0
     resources_assigned.vmem = 0kb
     resv_enable = True
     sharing = default_shared
     last_state_change_time = Thu Jan 26 04:00:34 2023
     last_used_time = Thu Jan 26 10:25:35 2023
```

You can see that the node has 8 CPUs, no GPUs, and at the moment runs a couple of jobs. One of these jobs is mine (74956). When I submitted `qsub` request, the scheduler told me that my job ID is 74956. The `pbsnodes` command gives us the list of jobs that are currently running on the compute node, and, happily, I see my job on that list. It appears four times, because I have requested four CPUs. Somebody else runs a job (61932) which is using just one CPU.

To exit the compute node, type:

``` bash
exit
```

This will bring you back to the login node. See how your prompt has changed to `login002`. It is important to notice that you have to be on a login node to request a compute node. One you are on the compute node, and you want to go to another compute node, you have to exit first.

For some jobs, you might want to get a GPU, or perhaps two GPUs. For such requests, the `qsub` command needs to specify the number of GPUs and the type of GPUs (which you can get from `cat /etc/hardware-table`). For example, let's request a NVIDIA K20:

```bash
qsub -I -l select=1:ncpus=4:mem=10gb:ngpus=1:gpu_model=k20,walltime=0:10:00
```

You might have to wait for a bit if the K20 nodes are busy. Once you get on the compute node, you can run:

```bash
nvidia-smi
```

Then, **exit the compute node to let other people a chance to get on it**.

If you want a GPU but don't care about the type of the GPU, you can request `gpu_model=any`.

It is possible to ask for several compute nodes at a time, for example `select=4` will give you 4 compute nodes. Some programs, such as LAMMPS or NAMD, work a lot faster if you ask for several nodes. This is an advanced topic and we will not discuss it here, but you can find some examples on our website.

There are other resource limit selection options documented on our
[website](https://www.palmetto.clemson.edu/palmetto/basic/started/#resource-limits-specification).

:::{warning}
Please be considerate of others when you issue qsub. Remember that Palmetto is a shared resource. Don't request resources you don't plan on actually using. Jobs that request in-demand resources and don't use them are subject to termination.
:::

:::{important}
It is very important to remember that you shouldn't run computations on the login node, because the login node is shared between everyone who logs into Palmetto, so your computations will interfere with other people's login processes.
However, once you are on a compute node, you can run some computations, because each user gets their own CPUs and RAM so there is no interference.
:::

## Modules

If you are on the compute node, exit it. Once you get on the login node, type this:

```bash
qsub -I -l select=1:ncpus=4:mem=10gb,walltime=2:00:00
```

We have a lot of software installed on Palmetto, but most of it is organized into *modules*, which need to be loaded. To see which modules are available on Palmetto, please type

```bash
module avail
```

Hit `SPACE` several times to get to the end of the module list. This is a very long list, and you can see that there is a lot of software installed for you. If you want to see which versions of MATLAB are installed, you can type

```bash
module avail matlab
```

```
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
```

Let's say you want to use R. To load the module, you will need to specify its full name.To see which versions of R are available, type

```
module avail r
```

This will give you a list of all modules which have the letter "r" in them (`module avail` is not very sophisticated). Let's see what happens when you load the R 4.1.3 module:

```
module load  r/4.1.3-gcc/9.5.0
module list
```

```
Currently Loaded Modules:
  1) tcl/8.6.12-gcc/9.5.0       4) openjdk/11.0.15_10-gcc/9.5.0   7) glib/2.72.1-gcc/9.5.0
  2) sqlite/3.38.5-gcc/9.5.0    5) libxml2/2.9.13-gcc/9.5.0       8) cairo/1.16.0-gcc/9.5.0
  3) openssl/1.1.1o-gcc/9.5.0   6) libpng/1.6.37-gcc/9.5.0        9) r/4.1.3-gcc/9.5.0
```

R depends on other software to run, so we have configured the R module in a way that when you load it, it automatically loads other modules that it depends on.

To start command-line R, you can simply type
```
R
```

To quit R, type
```
quit()
```

:::{admonition} Key Points
- `qsub` sends a request for a compute node to the scheduler.
- Software available on Palmetto is organized into modules according to version.
- Modules need to be loaded before use.
:::
