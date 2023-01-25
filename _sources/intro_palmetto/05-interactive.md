# Running an interactive job on Palmetto
teaching: 15
exercises: 0
questions:
- "How do I request and interact with a compute node?"
objectives:
- "`qsub`, `pbsnodes`, modules"
keypoints:
- "`whatsfree` shows the current Palmetto usage"
- "`qsub` sends a request for a compute node to the scheduler"
- "software available on Palmetto is organized into modules according to version"
- "modules need to be loaded before use"

Now, we arrive at the most important part of today's workshop: getting on the compute nodes. Compute nodes are the real power of Palmetto. Let's see which of the compute nodes are available at the moment:

~~~
whatsfree
~~~
{: .bash}

We can see that the cluster is quite busy, but there is a fair amount of compute nodes that are available for us. Now, let's request one compute node in the `skystd` queue. Please type the following (or paste from the website into your SSH terminal):

~~~
qsub -I -q skystd
~~~

The `qsub` command will send a request to the scheduler. Once the request is granted, you will see something like that:

~~~
qsub (Warning): Interactive jobs will be treated as not rerunnable
qsub: waiting for job 631266.pbs02 to start
qsub: job 631266.pbs02 ready

[gyourga@skystd01 ~]$ 
~~~
{: .output}

Importantly, you will see the prompt change. Perviously, the prompt was <your username>@login001, because you were at the login node. Now, you are on a compute node -- in this case, `skystd01` (you might be on a different compute node). To get back to the login node, let's type 
     
~~~
exit
~~~
{: .output}

Now, you will see the prompt changing back to `login001`. 

The `qsub` command that we have entered used the default parameters: one CPU, 2 Gb of RAM, and 24 hours of walltime (walltime is the amount of time you are requestng for the compute node; once this time is over, you are kicked out from the compute node). This request is very modest and not particularly practical. Let's do a more relevant request: four CPUs, 10 Gb of RAM, and two hours of walltime:

~~~
qsub -I -q skystd -l select=1:ncpus=4:mem=10gb,walltime=2:00:00
~~~
{: .bash}

It is very important not to make typos, use spaces and upper/lowercases exactly as shown, and use the proper punctuation (note the `:` between `ncpus` and `mem`, and the `,` before walltime). If you make a mistake, nothing wrong will happen, but the scheduler won't understand your request.

Now, let's carefully go through the request:

- `qsub` means that we are asking the scheduler to grant us access to a compute node;
- `-I` means it's an interactive job (we'll talk about it in a bit);
- `-q` specifies the Skylight queue;
- `-l` is the list of resource requirements we are asking for;
- `select=1` means we are asking for one compute node;
- `ncpus=4` means that we only need four CPUs on the node (since all Palmetto compute nodes have at least 8 CPUs, we might share the compute node with other users, but it's OK because users who use the same node do not interfere with each other);
- `mem=10gb` means that we are asking for 10 Gb of RAM (you shouldn't ask for less than 8 Gb); again, memory is specific to the user, and not shared between different users who use the same node);
- finally, `walltime=2:00:00` means that we are asking to use the node for 2 hours; after two hours we will be logged off the compute node if we haven't already disconnected.

This is actually a quite modest request as well, and the scheduler should grant it right away. Sometimes, when we are asking for much substantial amount of resources (for example, 10 nodes with 20 cores and 370 Gb of RAM), the scheduler cannot satisfy our request, and will put us into the queue so we will have to wait until the node becomes available. If you don't want to wait, you can press Ctrl+C.

Once the request is granted, you will see something like that:

~~~
qsub (Warning): Interactive jobs will be treated as not rerunnable
qsub: waiting for job 1649928.pbs02 to start
qsub: job 1649928.pbs02 ready

(base) [gyourga@skystd01 ~]$
~~~
{: .output}

Please note two important things. First, our prompt changes from `login001` no `skystdXX`, where `XX` is some four-digit number. This is the number of the node that we got (in our case, 01). The second one is the job ID, which is 1649928. We can see the information about the compute node by using the `pbsnodes` command:

~~~
pbsnodes skystd01
~~~
{: .bash}

Here is the information about the node that I was assigned to (skystd01):

~~~
(skystd01
     Mom = skystd01.palmetto.clemson.edu
     ntype = PBS
     state = job-busy
     pcpus = 20
     Priority = 25
     jobs = 1636248.pbs02/0, 1636248.pbs02/1, 1636248.pbs02/2, 1636248.pbs02/3, 1636248.pbs02/4, 1636248.pbs02/5, 1636248.pbs02/6, 1636248.pbs02/7, 1636248.pbs02/8, 1636248.pbs02/9, 1636248.pbs02/10, 1636248.pbs02/11, 1636248.pbs02/12, 1636248.pbs02/13, 1636248.pbs02/14, 1636248.pbs02/15, 1649928.pbs02/16, 1649928.pbs02/17, 1649928.pbs02/18, 1649928.pbs02/19
     resources_available.arch = linux
     resources_available.chip_manufacturer = intel
     resources_available.chip_model = xeon
     resources_available.chip_type = e5-2640v4
     resources_available.host = skystd01
     resources_available.hpmem = 0b
     resources_available.interconnect = 1g, 56g, fdr
     resources_available.make = act
     resources_available.manufacturer = act
     resources_available.mem = 131659892kb
     resources_available.model = act
     resources_available.ncpus = 20
     resources_available.ngpus = 0
     resources_available.node_make = act
     resources_available.node_manufacturer = act
     resources_available.node_model = act
     resources_available.nphis = 0
     resources_available.phase = 25a
     resources_available.qcat = skylight_qcat, skystd_qcat, c2_workq_qcat
     resources_available.ssd = False
     resources_available.vmem = 129470mb
     resources_available.vnode = skystd01
     resources_assigned.accelerator_memory = 0kb
     resources_assigned.hbmem = 0kb
     resources_assigned.mem = 73400320kb
     resources_assigned.naccelerators = 0
     resources_assigned.ncpus = 20
     resources_assigned.ngpus = 0
     resources_assigned.nphis = 0
     resources_assigned.vmem = 0kb
     resv_enable = True
     sharing = default_shared
     last_state_change_time = Fri Feb 12 14:07:24 2021
     last_used_time = Fri Feb 12 14:07:24 2021
~~~
{: .output}

You can see that the node has 20 CPUs, no GPUs, and at the moment runs a bunch of jobs. One of these jobs is mine (1649928). When I submitted `qsub` request, the scheduler told me that my job ID is 1649928. The `pbsnodes` command gives us the list of jobs that are currently running on the compute node, and, happily, I see my job on that list. It appears four times, because I have requested four CPUs. Somebody else runs a job (1636248) which takes the remaining 16 CPUs.

To exit the compute node, type:

~~~
exit
~~~
{: .bash}

This will bring you back to the login node. See how your prompt has changed to `login001`. It is important to notice that you have to be on a login node to request a compute node. One you are on the compute node, and you want to go to another compute node, you have to exit first.

For some jobs, you might want to get a GPU, or perhaps two GPUs. For such requests, the `qsub` command needs to specify the number of GPUs and the type of GPUs (which you can get from `cat /etc/hardware-skylight`); we will also have to use the `skygpu` queue. For example, let's request a NVIDIA Tesla GTX-1080: 

~~~
qsub -I -q skygpu -l select=1:ncpus=4:mem=10gb:ngpus=1:gpu_model=gtx1080,walltime=2:00:00
~~~
{: .bash}

You might have to wait for a bit of the GTX-1080 nodes are busy. Once you get on the compute node, exit it to let other people a chance to get on it.

If you want a GPU but don't care about the type of the GPU, you can request `gpu_model=any`. 

It is possible to ask for several compute nodes at a time, for example `select=4` will give you 4 compute nodes. Some programs, such as LAMMPS or NAMD, work a lot faster if you ask for several nodes. This is an advanced topic and we will not discuss it here, but you can find some examples on our website.

NOTE: please be considerate of others when you issue qsub. Remember that Palmetto is a shared resource. For example, maximum walltime is 10 days, but please don't ask for 10 days of walltime if you only plan to run your program for two hours. The same goes for CPUs and memory: if you have a small program, don't ask for 500 Gb of RAM.  

It is very important to remember that you shouldn't run computations on the login node, because the login node is shared between everyone who logs into Palmetto, so your computations will interfere with other people's login processes. However, once you are on a compute node, you can run some computations, because each user gets their own CPUs and RAM so there is no interference. If you are on the compute node, exit it. Once you get on the login node, type this:

~~~
qsub -I -q skystd -l select=1:ncpus=4:mem=10gb,walltime=2:00:00
~~~
{: .bash}

We have a lot of software installed on Palmetto, but most of it is organized into *modules*, which need to be loaded. To see which modules are available on Palmetto, please type

~~~
module avail
~~~
{: .bash}

Hit `SPACE` several times to get to the end of the module list. This is a very long list, and you can see that there is a lot of software installed for you. If you want to see which versions of LAMMPS are installed, you can type

~~~
 module avail lammps
 ~~~
{: .bash}

~~~
---------------------------------------------------- /software/ModuleFiles/modules/linux-centos8-x86_64 -----------------------------------------------------
   lammps/20190807-gcc/8.3.1-cuda10_2-mpi-openmp-user-omp                    lammps/20200505-gcc/8.3.1-cuda10_2-kokkos-mpi-nvidia_V-openmp-user-omp
   lammps/20200505-gcc/8.3.1-cuda10_2-kokkos-mpi-nvidia_K-openmp-user-omp    lammps/20200505-gcc/8.3.1-cuda10_2-mpi-nvidia_K-openmp-user-omp        (D)
   lammps/20200505-gcc/8.3.1-cuda10_2-kokkos-mpi-nvidia_P-openmp-user-omp

------------------------------------------------------------------- /software/AltModFiles -------------------------------------------------------------------
   lammps/20200505-nvidia_V_kokkos

  Where:
   D:  Default Module

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
~~~
{: .output}

Let's say you want to use R. To load the module, you will need to specify its full name.To see which versions of R are available, type

~~~
module avail r
~~~
{: .bash}

This will give you a list of all modules which have the letter "r" in them (`module avail` is not very sophisticated). Let's see what happens when you load the R 4.0.2 module:

~~~
module load r/4.0.2-gcc/8.3.1
module list
~~~
{: .bash}

~~~
Currently Loaded Modules:
  1) tcl/8.6.8-gcc/8.3.1   2) openjdk/11.0.2-gcc/8.3.1   3) libxml2/2.9.10-gcc/8.3.1   4) libpng/1.6.37-gcc/8.3.1   5) r/4.0.2-gcc/8.3.1
~~~
{: .output}

R depends on other software to run, so we have configured the R module in a way that when you load it, it automatically loads other modules that it depends on.

To start command-line R, you can simply type
~~~
R
~~~
{: .bash}

To quit R, type
~~~
quit()
~~~
{: .bash}
