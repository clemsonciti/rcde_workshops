# The structure of the Palmetto Cluster
questions:
- "What is the structure of the Palmetto Cluster?"
teaching: 15
exercises: 0
objectives:
- compute and login nodes, hardware table, `whatsfree`
keypoints:
- "Palmetto contains more than 2000 interconnected compute nodes"
- "a phase is a group of compute nodes that have the same architecture (CPUs, RAM, GPUs)"
- "a specialized login node runs the SSH server"

The computers that make up the Palmetto cluster are called *nodes*. Most of the nodes on Palmetto are *compute nodes*, 
that can perform fast calculations on large amounts of data. There is also a special node called the *login node*; it runs the server, 
which works like the interface 
between the cluster 
and the outside world. The people with Palmetto accounts can log into the server by running a client (such as `ssh`) on their local machines. 
Our client program passes our login credentials to this server, and if we are allowed to log in, the server runs a shell for us. 
Any commands that we enter into this shell are executed not by our own machines, but by the login node.

<img src="../fig/palmetto-structure.png" alt="Structure of the Palmetto Cluster" style="height:350px">

Another special node is the *scheduler*; Palmetto users can get from the
login node to the compute nodes by submitting a request to the scheduler, and the scheduler will assign them to the most appropriate compute node.
Palmetto also has a few so-called "service" nodes, which serve special purposes like transferring code and data to and from the cluster, and hosting web applications.

The Skylight nodes are integrated into Palmetto. To see the specifications of the Skylight compute nodes, let's type

~~~
cat /etc/hardware-skylight
~~~
{: .bash}

This will print out a text file with the hardware info. Please make sure you type exactly as shown; Linux is case-sensitive, space-sensitive, 
and typo-sensitive. The output will look something like this:

~~~
--------------------------------------------------------
SKYLIGHT HARDWARE TABLE      Last updated:  May 11 2021
--------------------------------------------------------

QUEUE   COUNT   MAKE   MODEL        CHIP(1)                CORES  RAM       /local_scratch   GPUs(2)

skystd    22    ACT    S2600TPFR    Intel Xeon E5-2640v4    20    125 GB    800 GB           0
skystd    24    Dell   R640         Intel Xeon 6230R        52    754 GB    3.4 TB           0

skylm      3    ACT    2USERVER     Intel Xeon E5-2680v4    28    503 GB    800 GB           0
skylm      5    Dell   R640         Intel Xeon 6230R        52   1500 GB    3.4 TB           0

skygpu     6    ACT    ESC4000G3    Intel Xeon E5-2640v4    20     62 GB    800 GB           4 x NVIDIA GTX1080
skygpu     2    ACT    2USERVER     Intel Xeon E5-2640v4    20    125 GB    800 GB           1 x NVIDIA P100
skygpu     6    Dell   DSS840       Intel Xeon 6230R        52    380 GB    3.4 TB           8 x NVIDIA RTX6000
~~~
{: .output}

The Skylight nodes are grouped into three *queues*: `skystd` (Skylight standard), `slylm` (Skylight large memory), and `skygpu` (Skylight GPU). The number of nodes accessible through each queue is respectively, 46, 8, and 14. The first queue is the "standard" nodes which are good for most applications. Each node has either 20 or 52 cores, or CPUs, or processors.  This means that you can run 20 (or 52) processes in parallel. If the software can organize its operations into 20 (or 52) parallel processes, it will run considerably faster (and a lot fo software is really good at this, Matlab and LAMMPS being just two examples). The standard nodes have 125 (or 754) Gb of RAM. If your software needs more RAM than that, you should use the nodes in the large memory queue; they have up to 1.5 Tb of RAM. Finally, some software really benefits from using GPU (graphical processing unit, which is basically a video card). In addition to running video, GPUs can be utilized for really fast and efficient computations. Six nodes in the GPU queue have GTX-1080 cards (four per node), two nodes have P100 cards (one per node), and six nodes have RTX-6000 cards; the P100 card is the most powerful. 

To see which nodes are available at the moment, you can type 

~~~
whatsfree
~~~
{: .bash}

It will produce a lot of output, but the relevant part is the Skylight nodes:

~~~
SKYLIGHT CLUSTER (Mercury Consortium)
PHASE 25a  TOTAL =  22  FREE =   0  OFFLINE =   1  TYPE = ACT            Intel Xeon  E5-2640v4, 20 cores,  125GB,  1ge
PHASE 25b  TOTAL =   3  FREE =   0  OFFLINE =   0  TYPE = ACT            Intel Xeon  E5-2680v4, 28 cores,  503GB,  1ge
PHASE 25c  TOTAL =   6  FREE =   0  OFFLINE =   0  TYPE = ACT            Intel Xeon  E5-2640v4, 20 cores,   62GB,  1ge, GTX1080
PHASE 25d  TOTAL =   2  FREE =   0  OFFLINE =   0  TYPE = ACT            Intel Xeon  E5-2640v4, 20 cores,  125GB,  1ge, P100
PHASE 26a  TOTAL =  24  FREE =   0  OFFLINE =   0  TYPE = Dell R640      Intel Xeon  6230R,     52 cores,  754GB, 25ge
PHASE 26b  TOTAL =   5  FREE =   0  OFFLINE =   0  TYPE = Dell R640      Intel Xeon  6230R,     52 cores, 1500GB, 25ge
PHASE 26c  TOTAL =   6  FREE =   0  OFFLINE =   0  TYPE = Dell DSS840    Intel Xeon  6230R,     52 cores,  380GB, 25ge, RTX6000
~~~
{: .output}

Phases 25 and 26 are the Skylight nodes. Phase 25 is the initial purchase, and phase 26 is the more recent one. Phases 25a and 26a are accessed through the `skystd` queue; phases 25b and 26b are accessed through `skylm` ("large memory") queue; and finally phases 25c, 25d, and 26c are accessed through the `skygpu` queue.

This table shows the amount of *completely free* nodes per each phase; a node which has, for example, 8 cores, but only 4 of them are used, would not be counted as "free". So this table is a conservative estimate. It is a good idea to run `whatsfree` when you log into Palmetto, to get a picture of how busy the cluster is. This picture can change pretty drastically depending on the time of the day and the day of the week.

If a compute node is not 100% busy, you can still get on it. For example, the compute nodes in phase 26c have 52 cores, 280 GB of RAM, and 8 GPUs. If you are fine with using a subset of these resources, the `freeres` script can be very convenient: it tells you which nodes are *partially* available. Let's run it for phase 26c:

~~~
freeres phase26c
~~~
{: .bash}

~~~
group file = /software/caci/cluster/phase26c
                 CPU       |       GPU       |   Memory (GB)   |
Node       Avail Used Free | Avail Used Free | Avail Used Free | State
---------------------------------------------------------------------------
skygpur1    52    51     1     8     3     5   376   186   190   free
skygpur2    52    51     1     8     3     5   376   186   190   free
skygpur3    52    51     1     8     3     5   376   186   190   free
skygpur4    52    51     1     8     3     5   376   186   190   free
skygpur5    52    34    18     8     2     6   376   124   252   free
skygpur6    52    51     1     8     3     5   376   224   152   free
checked 6 nodes in 0.40 Seconds
~~~
{: .output}

So if you ask for no more than 18 CPUs, 252 GB of RAM, and 6 GPUs, you will still be able to get on a Phase 26c compute node without having to wait in line.
