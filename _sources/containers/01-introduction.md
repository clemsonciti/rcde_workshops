
# Introduction to CloudLab

## 1. Access CloudLab    
 
- Visit [CloudLab's website](https://cloudlab.us)
- Click "Request an Account" 
- Fill in the information as follows, and click "Submit Request" afterward
  - `Username`: Create a unique username. You can attempt to reuse your Clemson 
  username. 
  - `Full Name`: Provide your full name. 
  - `Email`: Provide your Clemson email address
  - `Country`: United States
  - `State`: South Caroline
  - `Institution`: Clemson University
  - `SSH Public Key`: If you know where to get this public key file, you can upload 
  it now. We can/will do it later as well. 
  - `Password`/`Confirm Password`: Create a secure password for your account. 
  - `Join Existing Project`: `Clemson-RCDE`
- Wait for a confirmation email to arrive in your `clemson.edu` mailbox. You might have 
to resubmit a new request if you don't see this email in about half an hour. 
- After your account is confirmed, the instructor will be able to see your application 
and can grant you access to CloudLab. 
- If you already had a CloudLab account, you can select `Start/Join Project` under
your username, then select `Join Existing Project` and provide the name `Clemson-RCDE`. 

## 2. What is CloudLab

- Experimental testbed for future computing research
  - Built upon the GENI infrastructure
- Allow researchers control to the bare metal
- Diverse, distributed resources at large scale
- Allow repeatable and scientific design of experiments

```{admonition} What is GENI
:class: dropdown

- Global Environment for Networking Innovation
- Combining heterogeneous resource types, each virtualized 
along one or more suitable dimensions, to produce a single 
platform for network science researchers"
- Key components:
  - GENI racks: virtualized computation and storage resources
  - Software-defined networks (SDNs): virtualized, programmable network resources
  - WiMAX: virtualized cellular wireless communication

![GENI framework](../fig/containers/geni.png)

*Berman, M., Chase, J.S., Landweber, L., Nakao, A., Ott, M., Raychaudhuri, 
D., Ricci, R. , and Seskar, I., 2014. GENI: A federated testbed for innovative 
network experiments. Computer Networks, 61, pp.5-23.*

```

```{admonition} Key experimental concepts
:class: dropdown

- Sliceability: the ability to support virtualization while 
maintaining some degree of isolation for simultaneous experiments
- Deep programmability: the ability to influence the behavior of 
computing, storage, routing, and forwarding components deep inside the 
network, not just at or near the network edge.

```


## 3. CloudLab Hardware

CloudLab started out as three primary sites from University of Utah, 
University of Wisconsin, and Clemson University. 

:::::{tab-set} 
::::{tab-item} Utah

- Low-power ARM64 (785 nodes)
- 315 m400: 1X 8-core ARMv8 at 2.4GHz, 64GB RAM, 120GB flash
- 270 m510: 1X 8-core Intel Xeon D-1548 at 2.0 GHz, 64GB RAM, 256 GB flash
- 200 xl170: 1X 10-core Intel E5-2640v4 at 2.4 Ghz, 64 GB RAM, 480 GB SSD
 
::::
::::{tab-item} Wisconsin

- 90 c220g1: 2X 8-core Intel Haswell at 2.4GHz, 128GB RAM, 1X 480GB SDD, 2X 1.2TB HDD
- 10 c240g1: 2X 8-core Intel Haswell at 2.4GHz, 128GB RAM, 1X 480GB SDD, 1X 1TB HDD, 12X 3TB HDD
- 163 c220g2: 2X 10-core Intel Haswell at 2.6GHz, 160GB RAM, 1X 480GB SDD, 2X 1.2TB HDD
- 7 c240g2: 2X Intel Haswell 10-core at 2.6GHz, 160GB RAM, 2X 480GB SDD, 12X 3TB HDD
- 224 c220g5: 2X 10-core Intel Skylake at 2.20GHz, 192GB RAM, 1TB HDD
- 32 c240g5: 2X 10-core Intel Skylake at 2.20GHz, 192GB RAM, 1TB HDD, 1 NVIDIA P100 GPU
- 4 c4130: 2X 8-core Intel Broadwell at 3.20GHz, 128GB RAM, 2X 960GB HDD, 4 NVIDIA V100

::::
::::{tab-item} Clemson

- 96 c8220: 2X 10-core Intel Ivy Bridge at 2.2GHz, 256GB RAM, 2X 1TB HDD
- 4 c8220x: 2X 10-core Intel Ivy Bridge at 2.2GHz, 256GB RAM, 8X 1TB HDD, 12X 4TB HDD
- 84 c6420: 2X 14-core Intel Haswell at 2.0GHz, 256GB RAM, 2X 1TB HDD
- 2 c4130: 2X 12-core Intel Haswell at 2.5GHz, 256GB RAM, 2X 1TB HDD, 2 NVIDIA K40m
- 2 dss7500: 2X 6-core Intel Haswell at 2.4GHz, 128GN RAM, 2X 126GB SSD, 45X 6TB HDD
- 72 c6420: 2X 16-core Intel Skylake at 2.6GHz, 386GB RAM, 2X 1TB HDD
- 6 ibm8335: 2X 10-core IBM POWER8NVL at 2.87GHz, 512GB RAM, 1X 2TB HDD, 2 NVIDIA GV100GL
- 15 r7515: 2X 32-core AMD EPYC Rome at 2.9GHz, 512GB RAM, 1X 2TB HDD, 2 NVIDIA GV100GL

::::
:::::


## 4. Setup SSH

- Log into Palmetto
- All Palmetto accounts have SSH keys ready. 


```{admonition} Get your Palmetto account public key
:class: dropdown

- Run the following commands to print the key to 
the terminal screen. 

~~~bash
cd
cat ~/.ssh/id_rsa.pub
~~~

- Very carefully, use the mouse to paint over the key, 
starting from `ssh-rsa ...` until `...@login001.palmetto.clemson.edu`. 
- **Do not** have any extra spaces anywhere. 
- Log into CloudLab, click on your username (top right) and select `Manage SSH Keys`:

![Go to the Manage SSH Keys menu](../fig/containers/cloudlab-manage-ssh.png)

- Paste the key into the `Key` box and click `Add Key`

```

## 5. Setup GitHub repository


```{admonition} Create new GitHub repository
:class: dropdown

- Go to your GitHub account, under `Repositories`, select `New`. 
- You can select any name for your repo. 
- It must be `public`. 
- The `Add a README file` box must be checked. 
- Click `Create repository` when done.  

```

```{admonition} Adding file to repository
:class: dropdown

- Click `Add file` and select `Create new file`
- Type `profile.py` for the file name and enter the content below:

<script src="https://gist.github.com/linhbngo/6d5747ab8f04763f9dc265c361d7ebcf.js?file=profile-basic.py"></script>

- Click `Commit new file` when done. 

```


## 6. Setup CloudLab experimental profile

- Login to your CloudLab account, click `Experiments` on top left, 
select `Create Experiment Profile`. 

```{admonition} Create New Profile
:class: dropdown

![Create New Profile](../fig/containers/cloudlab-new-profile.png)

```

- Click on `Git Repo`
  - You might not have a dropdown `Project` box, unless you are members of multiple CloudLab
  projects.

```{admonition} Create New Profile
:class: dropdown

![Create New Profile from Git Repo](../fig/containers/cloudlab-profile-git.png)

```

- Open another browser tab, go to the previously created Git repository, and 
get the clone URL (HTTPS option) of your Git repository

```{admonition} HTTPS clone link
:class: dropdown

![Getting HTTPS clone link](../fig/containers/git-clone-https.png)

```

- Paste the URL of **your** previously created Git repo here and click `Confirm`
  - This must be the `HTTPS` option. 

```{admonition} Paste Git clone link
:class: dropdown

![Paste }HTTPS clone link](../fig/containers/cloudlab-profile-git-url.png)

```

- Enter the name for your profile, put in some words for the Description. 
- You will not have a drop-down list of Project. 
- Click `Create` when done. 

```{admonition} Complete and create profile
:class: dropdown

![Create CloudLab profile](../fig/containers/cloudlab-profile-create.png)

```

- Click `Instantiate` to launch an experiment from your profile. 

```{admonition} Instantiate an experiment from a profile
:class: dropdown

![Launch CloudLab experiment from profile](../fig/containers/cloudlab-profile-instantiate.png)

```

- Click `Next` on the first tab, `Select a Profile`.
- Select a Cluster from Wisconsin, Clemson, or Emulab, then click `Next`. 

```{admonition} Select cluster
:class: dropdown

![Select cluster to launch experiment](../fig/containers/cloudlab-instantiate-emulab.png)

```

- Do not do anything on the next `Start on date/time` screen. Click `Finish`.  




- Your experiment is now being `provision`, and then `booting  

```{admonition} Select cluster
:class: dropdown

![Select cluster to launch experiment](../fig/containers/cloudlab-instantiate-emulab.png)

```

> ## 3. A brief history of Spark
> 
> - Research project at UC Berkeley AMP Lab in 2009 to address drawbacks of 
> Hadoop MapReduce. 
> - Paper published in 2010: [Spark: Cluster Computing with Working Sets](https://static.usenix.org/events/hotcloud10/tech/full_papers/Zaharia.pdf) 
> - Source code is contributed to Apache in 2013. The project had more than 100 
> contributors from more than 30 organizations outside UC Berkeley. 
> - Version 1.0 was released in 2014. 
> - Currently, Spark is being used extensively in academic and industry 
> (NASA, CERN, Uber, Netflix …). 
>
{: .slide}

> ## 4. map and reduce
> 
> - What is `map`? A function/procedure that is applied to every individual 
> elements of a collection/list/array/…
>
> ~~~
> int square(x) { return x*x;}
> map square [1,2,3,4] -> [1,4,9,16]
> ~~~
> {: .language-bash}
>
> - What is “reduce”? A function/procedure that performs an operation on a list. 
> This operation will “fold/reduce” this list into a single value (or a smaller 
> subset).
>
> ~~~
> reduce ([1,2,3,4]) using sum -> 10
> reduce ([1,2,3,4]) using multiply -> 24
> ~~~
> {: .language-bash}
>
{: .slide}

> ## 5. MapReduce programming paradigm
> 
> - Programmers implement:
>   - Map function: Take in the input data and return a key,value pair.
>   - Reduce function: Receive the key,value pairs from the mapper and provide a
>   final output as a reduction operation on the pairs.
>
> - MapReduce Framework handles everything else.
> - Spark implements a MapReduce framework. 
>
{: .slide}

> ## 6. WordCount: the Hello, World! of Big Data
> 
> - Count how many unique words there are in a file/multiple files.
> - Standard parallel programming approach:
>   - Count number of files
>   - Set number of processes
>   - Possibly setting up dynamic workload assignment
>   - A lot of data transfer
>   - Significant coding effort
> 
> > ## MapReduce workflow
> > 
> > <img src="../fig/01-introduction/02.png" alt="Spark" style="height:400px">
> {: .slide}
>
> > ## MapReduce framework
> > 
> > <img src="../fig/01-introduction/03.png" alt="Spark" style="height:400px">
> {: .slide}
{: .slide}



