# Access Control


```{dropdown} 1. Unix standards
- Access control decisions depend on which user is attempting to 
perform and operation on that user’s membership in a UNIX group.
- Objects have owners. Owners have broad (but not necessarily unrestricted) 
control over their objects.
- You own the object you create. 
- The special user account `root` can act as the owner of any object. 
Only `root` can perform certain sensitive administrative operation. 
```

```{dropdown} 2. CloudLab - a place with rootly power!    
- Visit [CloudLab’s website](https://cloudlab.us/)
- Click `Request an Account`
- Fill in the information as shown below and click `Submit Request`
  - `Username`: Use your WCUPA username. Make sure everything is 
  lowercase. 
  - `Full Name`: Your first and last name
  - `Email`: Use a non-WCUPA email. WCUPA email tends to block the 
  confirmation email. 
  - `Select Country`: United States
  - `Select State`: Pennsylvania
  - `City`: Malvern
  - `Institutional Affiliation`: West Chester University of Pennsylvania
  - Ignore the `SSH Public Key file` box for now. 
  - Enter a password of your choice in `Password` and `Confirm Password` boxes. 
  - Check `Join Existing Project` for `Project Information`.
  - `Project Name`: SecureEDU

:::{image} ../fig/csc586//04-access-control/cloudlab-signup.png
:alt: Sign up instructions for CloudLab account
:class: bg-primary mb-1
:height: 800px
:align: center
:::

- Wait for a confirm ation email to arrive in your mailbox. You 
might have to resubmit a new request if you don’t see this email 
in about half an hour.
- After your account is confirmed, the instructor will be able to 
see your application and can grant you access to CloudLab.
- If you already had a CloudLab account, you can select 
`Start/Join Project` under your username, then select 
`Join Existing Project` and provide the name `SecureEDU`.
```

```{dropdown} 3. What is CloudLab    
- Experimental testbed for future computing research
- Allow researchers control to the bare metal
- Diverse, distributed resources at large scale
- Allow repeatable and scientific design of experiments

:::{image} ../fig/csc586//04-access-control/cloudlab-geni.png
:alt: Sign up instructions for CloudLab account
:class: bg-primary mb-1
:height: 600px
:align: center
:::
```

```{dropdown} 4. What is GENI    
- Global Environment for Networking Innovation
- Combining heterogeneous resource types, each virtualized 
along one or more suitable dimensions, to produce a single 
platform for network science researchers
- Key components:
  - GENI racks: virtualized computation and storage resources
  - Software-defined networks (SDNs): virtualized, programmable 
  network resources
  - WiMAX: virtualized cellular wireless communication
- *Berman, M., Chase, J.S., Landweber, L., Nakao, A., Ott, M., Raychaudhuri, D., Ricci, R. , and Seskar, I., 2014. GENI: A federated testbed for innovative network experiments. Computer Networks, 61, pp.5-23.*
```

```{dropdown} 5. Key experimental concepts     
- Sliceability: the ability to support virtualization 
while maintaining some degree of isolation for simultaneous 
experiments
- Deep programmability: the ability to influence the behavior 
of computing, storage, routing, and forwarding components deep 
inside the network, not just at or near the network edge.
```

```{dropdown} 6. Hardware    
- Utah/HP: Low-power ARM64 (785 nodes)
  - 315 m400: 1X 8-core ARMv8 at 2.4GHz, 64GB RAM, 120GB flash
  - 270 m510: 1X 8-core Intel Xeon D-1548 at 2.0 GHz, 64GB RAM, 256 GB flash
  - 200 xl170: 1X 10-core Intel E5-2640v4 at 2.4 Ghz, 64 GB RAM, 480 GB SSD
- Wisconsin/Cisco: 530 nodes
  - 90 c220g1: 2X 8-core Intel Haswell at 2.4GHz, 128GB RAM, 1X 480GB SDD, 2X 1.2TB HDD
  - 10 c240g1: 2X 8-core Intel Haswell at 2.4GHz, 128GB RAM, 1X 480GB SDD, 1X 1TB HDD, 12X 3TB HDD
  - 163 c220g2: 2X 10-core Intel Haswell at 2.6GHz, 160GB RAM, 1X 480GB SDD, 2X 1.2TB HDD
  - 7 c240g2: 2X Intel Haswell 10-core at 2.6GHz, 160GB RAM, 2X 480GB SDD, 12X 3TB HDD
  - 224 c220g5: 2X 10-core Intel Skylake at 2.20GHz, 192GB RAM, 1TB HDD
  - 32 c240g5: 2X 10-core Intel Skylake at 2.20GHz, 192GB RAM, 1TB HDD, 1 NVIDIA P100 GPU
  - 4 c4130: 2X 8-core Intel Broadwell at 3.20GHz, 128GB RAM, 2X 960GB HDD, 4 NVIDIA V100
- Clemson/Dell: 281 nodes
  - 96 c8220: 2X 10-core Intel Ivy Bridge at 2.2GHz, 256GB RAM, 2X 1TB HDD
  - 4 c8220x: 2X 10-core Intel Ivy Bridge at 2.2GHz, 256GB RAM, 8X 1TB HDD, 12X 4TB HDD
  - 84 c6420: 2X 14-core Intel Haswell at 2.0GHz, 256GB RAM, 2X 1TB HDD
  - 2 c4130: 2X 12-core Intel Haswell at 2.5GHz, 256GB RAM, 2X 1TB HDD, 2 NVIDIA K40m
  - 2 dss7500: 2X 6-core Intel Haswell at 2.4GHz, 128GN RAM, 2X 126GB SSD, 45X 6TB HDD
  - 72 c6420: 2X 16-core Intel Skylake at 2.6GHz, 386GB RAM, 2X 1TB HDD
  - 6 ibm8335: 2X 10-core IBM POWER8NVL at 2.87GHz, 512GB RAM, 1X 2TB HDD, 2 NVIDIA GV100GL
  - 15 r7515: 2X 32-core AMD EPYC Rome at 2.9GHz, 512GB RAM, 1X 2TB HDD, 2 NVIDIA GV100GL
```

```{dropdown} 7. Setup SSH

- Log into `molly`
- Run the following commands to check if you have already 
setup SSH keys from a previous class

~~~
$ cd
$ ls -l ~/.ssh
~~~

::::{admonition} If you already have keys setup
:class: dropdown

- If the outcome of the `ls -l ~/ssh` command contains the `id_rsa`
`id_rsa.pub` (screenshot below), then you already have the keys. 
- If you don't have the files, you need to generate the keys. 

:::{image} ../fig/csc586//04-access-control/ssh-files.png
:alt: showing available SSH keys 
:class: bg-primary mb-1
:height: 200px
:align: center
:::
::::

::::{admonition} Generate SSH keys
:class: dropdown

- Run the following commands to generate the keys
  - Keep pressing `Enter` to accept all default answers
  - **Do not** type in anything else.

~~~
$ cd
$ ssh-keygen -t rsa
$ ls -l ~/.ssh
~~~

:::{image} ../fig/csc586//04-access-control/ssh-keygen.png
:alt: steps to generate SSH keys 
:class: bg-primary mb-1
:height: 200px
:align: center
:::
::::

::::{admonition} Upload SSH public key to CloudLab
:class: dropdown

- Run the following commands to print the key to 
the terminal screen. 

~~~
$ cd
$ cat ~/.ssh/id_rsa.pub
~~~

- Very carefully, use the mouse to paint over the key, 
starting from `ssh-rsa ...` until `...@molly`. 
- **Do not** have any extra spaces anywhere. 

:::{image} ../fig/csc586//04-access-control/id_rsa_pub.png
:alt: steps to generate SSH keys 
:class: bg-primary mb-1
:height: 200px
:align: center
:::

- Log into CloudLab, click on your username (top right) and select `Manage SSH Keys`:

:::{image} ../fig/csc586//04-access-control/cloudlab-manage-ssh.png
:alt: Go to the Manage SSH Keys menu 
:class: bg-primary mb-1
:height: 150px
:align: center
:::

- Paste the key into the `Key` box and click `Add Key`:

:::{image} ../fig/csc586//04-access-control/cloudlab-addkey.png
:alt: Go to the Manage SSH Keys menu 
:class: bg-primary mb-1
:height: 300px
:align: center
:::
::::


```


```{dropdown} 8. Setup GitHub repository

- If you don't already have one, create a GitHub account. 
- Go to your GitHub account, under `Repositories`, select `New`.
---
:::{image} ../fig/csc586//04-access-control/github-new.png
:alt: Create a new repository on GitHub 
:class: bg-primary mb-1
:height: 100px
:align: center
:::
---
- You can select any name for your repo.
- It must be `public`.
- The `Add a README file` box must be checked.
- Click `Create repository` when done.
---
:::{image} ../fig/csc586//04-access-control/github-create-repo.png
:alt: Create a new repository on GitHub 
:class: bg-primary mb-1
:height: 900px
:align: center
:::
---
- Click `Add file` and select `Create new file`.
---
:::{image} ../fig/csc586//04-access-control/github-create-new-file.png
:alt: Create a new repository on GitHub 
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- Type `profile.py` for the file name and enter the code below into the 
text editor.
- Click `Commit new file` when done.
---
<script src="https://gist.github.com/linhbngo/060f8a99fbc3666b6abf8f05be54a28c.js?file=profile-basic.py"></script>
---
:::{image} ../fig/csc586//04-access-control/github-commit-new-file.png
:alt: Commit the newly created profile.py to the repo 
:class: bg-primary mb-1
:height: 1000px
:align: center
:::
```


```{dropdown} 9. Setup CloudLab profile

- Login to your CloudLab account, click `Experiments`
 on top left, select `Create Experiment Profile`.
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-1.png
:alt: Navigate to create experimental profile 
:class: bg-primary mb-1
:height: 300px
:align: center
:::
---
- Click on `Git Repo` 
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-2.png
:alt: Select Git Repo as a mean to create profile 
:class: bg-primary mb-1
:height: 300px
:align: center
:::
---
- Open another browser tab, go to the previously created Git repository, 
and get the URL of your Git repository
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-3.png
:alt: Getting the public URL of the git repo 
:class: bg-primary mb-1
:height: 300px
:align: center
:::
---
- Paste the URL of your previously created Git repo and click Confirm
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-4.png
:alt: Copy and paste the URL of the Git repo then click Confirm 
:class: bg-primary mb-1
:height: 300px
:align: center
:::
---
- Enter the name for your profile, put in some words for the Description.
- You will not have a drop-down list of Project.
- Click Create when done.
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-5.png
:alt: Create new CloudLab profile 
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- Click `Instantiate` to launch an experiment from your profile.
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-6.png
:alt: Instantiate an experiment from the profile 
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- Select a Cluster from Emulab, then click `Next`.
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-7.png
:alt: Select the cluster from which the experiment will be instantiated
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- Do not do anything on the next Start on date/time screen. Click `Finish`.
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-8.png
:alt: Finish instantiating the experiment
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- Your experiment is now being provisioned
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-9.png
:alt: Provisioning resources for experiment
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- Your experiment is now being booted up
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-10.png
:alt: Resource is provisioned and is now being booted up
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- A view of the booting experiment via the `List View` tab. 
  - Note the `Cluster` and `Status` column.
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-11.png
:alt: Finish instantiating the experiment
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- Your experiment is now ready. 
  - Note the `Cluster` and `Status` column.
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-12.png
:alt: Experiment is ready
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- You can ssh to the experiment from `molly` using the `ssh` command 
shown in the previous screenshot:
  - Type `yes` and press Enter when inquired about `The authenticity of host ...`
  - Type 2 to go with the default setting of zshell
---
:::{image} ../fig/csc586//04-access-control/cloudlab-profile-14.png
:alt: Experiment is ready
:class: bg-primary mb-1
:height: 500px
:align: center
:::
```

```{dropdown} 10. Unix/Linux standards for access control    
- Access control decisions depend on which user is attempting to perform 
and operation on that user’s membership in a UNIX group.
- Objects have owners. Owners have broad (but not necessarily unrestricted) 
control over their objects.
- You own the object you create. 
- The special user account `root` can act as the owner of any object. 
Only `root` can perform certain sensitive administrative operation. 
```

```{dropdown} 11. Root and Rootly Powers    
- The omnipotent administrative user (superuser)
  - Can perform all restrictive operations:
  - Creating device files
  - Setting the system clock
  - Raising resource usage limits and process priorities
  - Setting the system’s hostname
  - Configuring network interfaces
  - Opening privileged network ports (those below 1024)
  - Shutting down the system
- `sudo`: Running the commands as another user. If there is no username
  provided, the user is going to be `root`. 
  - For security purposes, the password of the `root` account should always 
  be very complicated and not be given out lightly. 
  - Administrative teams are often granted `sudo` power, meaning that they 
  can execute commands `in the name of` other accounts, including `root`. 
---
:::{image} ../fig/csc586//04-access-control/sudo.png
:alt: Experiment is ready
:class: bg-primary mb-1
:height: 500px
:align: center
:::
---
- **How does it help with security aspects, since technically everyone 
  have rootly power anyway with sudo?**
```

```{dropdown} 12. Hands-on: Rootly power    
- SSH into the CloudLab experiment launched earlier. 
- `whoami`: Give you the effective user id of the one running the shell. 
- Run the following bash commands to observe the power of `sudo`:
~~~
$ whoami
$ sudo whoami
$ cat /etc/shadow
$ sudo cat /etc/shadow
~~~
```

```{dropdown} 13. Other (less secure) means of granting rootly powers    
- [`setuid`](https://man7.org/linux/man-pages/man2/setuid.2.html)
  - Grant privilege to the task (the program), not the user
  - Possible by leveraging a process' user ID:
    - real user ID (ruid)
    - effective user ID (euid)
    - saved user ID (suid)

~~~
$ id
~~~
 
- A way to grant privileges to `non-root` and `non-sudo` account. 

~~~
$ man chown
$ man chmod
$ cat /etc/shadow
$ which cat
$ cp $(which cat) mycat
$ ./mycat /etc/shadow
$ sudo chown root mycat
$ sudo chmod 4755 mycat
$ ./mycat /etc/shadow
~~~
```

```{dropdown} 14. Managemen of the root account    
- Why direct log in of root account is a bad idea. 
  - Root logins leave no record of what operations where performed as root. 
  - We also don't know who logged in as root. 
- By default, most systems allow root login to be disabled on
terminals, through the windows systems, and across the network.
  - Passwordless root account is another solution. 
- If root is accessible, password must be really good. 
```

```{dropdown} 15. Challenge  

- Run the following command to create a new account called `student`.  

~~~
sudo useradd -s /bin/sh -d /home/student -m student
~~~

- Search for documentation to find out how to turn `student` into an account 
with passwordless power. 

```

```{dropdown} 16. Drawback of standard models  
   
- Root access presents a potential single point of failure. 
- The `setuid` alternative is difficult to manage due to potential capability leaks
from complex software suites. 
- Minimal control over network security. 
- Group management cannot be done by users (more work for adminsitrators). 
- Access control rules are embedded in individual codes, cannot be easily rewritten. 
- Little to no support for auditing and logging.  

``` 


```{dropdown} 17. Extensions to standard models  
   
- PAM: Pluggable Authentication Modules
  - Wrapper for various method-specific authentication libraries
  - SSO (Single Sign-On)
- Kerberos: netowrk cryptographic authentication
  - Authentication rather than accesss control
  - Uses trusted third party to perform authentication for an entire network. 
- Filesystem access control lists )ACL)
  - Set permissions for multiple users and groups at once. 
- Linux capabilities
  - [man capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)
  - Privileges traditionally associated with superuser are divided into 
  units, known as capabilities, which can be independently enabled and disabled. 
  - Capabilities are a per-thread attribute. 
  - This is in use extenively for higher-level systems like `AppArmor` or `Docker`. 
- Linux namespaces
  - Processes can be separated into hierarchical partitions (`namespaces`) from 
  which they see only a subset of the system's files, network ports, and processes. 
  - Preemptive access control. 
  - Foundation for software containerization
  - Docker
``` 


```{dropdown} 18. Modern access control  
   
- Linux's standard access control model is considered `discretionary access control` (DAC)
  - Owners of access-controlled entities to set the permissions on them. 
  - Bad example: users expose their home directories. 
- Mandatory access control (MAC)
  - Adminstrators write access control policies that override or supplement DAC. 
  - Enabling technology for new security models. 
  - Principle of least privilege
- Role-based access contrl (RBAC)
  - Added layer of indirection to access control calculations
  - Permissions are granted to intermediate constructs (`roles`), and 
  `roles` are assigned to `users`. 
  - `roles` can have hierarchical relationships (easier to administer)
- SELinux: Security-Enhanced Linux
  - MAC model
  - Created by NSA
  - Difficult to administer and troubleshoot
``` 

