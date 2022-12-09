# Accessing the Palmetto Cluster

For this workshop, we will utilize Palmetto's new browser-based interface. 
This interface includes a directory navigation interface and a browser-based terminal. 

## OpenOnDemand Interface

Visit the following URL from your browser: 

```
https://openod02.palmetto.clemson.edu
```

You will need to login with your Clemson username and password, and perform a DUO check. 

<img src="../fig/openod_dashboard.png" alt="Open OnDemand Dashboard" style="height:600px">

On the top menu bar, click on `Clusters`, then `Palmetto Shell Access`

<img src="../fig/openod_shell_access.png" alt="Open OnDemand Shell Menu" style="height:300px">

Enter your account password, then DUO information to log in to the browser-based terminal

<img src="../fig/openod_shell.png" alt="Open OnDemand Shell Menu" style="height:500px">

When logged in,
you are presented with a welcome message
and the following "prompt":

~~~
[username@login001 ~]$
~~~
{: .bash}


The prompt in a bash shell usually
consists of a dollar (`$`) sign,
and shows that the shell is waiting for input.
The prompt may also contain other information:
this prompt tells you `your username` and which node
you are connected to -
`login001` is the "login" node.
It also tells you your current directory,
i.e., `~`, which, as you will learn shortly,
is short for your *home* directory.
We will mostly refer to the prompt as just `$`, i.e.,

~~~
$
~~~
{: .bash}

Let's enter our first command! 
Type the command `whoami`,
then press the Enter key (sometimes marked Return) to send the command to the shell.
The command's output is the ID of the current user.

~~~
$ whoami
~~~
{: .bash}



## Basic structure of the cluster

<img src="../fig/palmetto-structure.png" alt="Structure of the Palmetto Cluster" style="height:350px">

The Palmetto cluster has several "compute" nodes
that can perform fast calculations on large amounts of data.
It also has a few so-called "service" nodes,
that are *not* meant for this purpose.
Instead, they are meant to help users perform other actions
such as transfering code and data to and from the cluster.


## Remote login (for reference purpose)

To be able to run commands on the Palmetto from your own machine,
you will first need to be able to log in to the Palmetto.
This is known as a *remote login*.

For Mac OS X, you can open the Terminal Application (which is usually in Applications &rarr; Utilities folder) and run the following:

~~~
ssh <your Palmetto username>@login.palmetto.clemson.edu
~~~
{: .bash}

For Windows, first you need to download and install
[MobaXterm Home Edition](https://mobaxterm.mobatek.net/download.html).

> It is important that you unzip the downloaded installer prior to installation.
> The zipped installer file contains an additional data file besides the installer
> executable. This data file is not accessible if the installer executable is
> called from insize the zipped file (something Windows allows you to do).
{: .callout}

After MobaXterm starts, click the `Session` button.

<img src="../fig/mobaxterm_0.png" alt="Main MobaXterm Windows" style="height:350px">


Select SSH session and use the following parameters (whichever required), then click `OK`:

* Remote host: `login.palmetto.clemson.edu`
* SSH-browser type: Enhanced SCP
* Port: 22

<img src="../fig/mobaxterm_1.png" alt="MobaXterm SSH Session" style="height:350px">

At this stage, for both Mac and Windows, you will be asked to enter your username
and password, then DUO option.

<img src="../fig/mobaxterm_2.png" alt="Login interface" style="height:350px">

> For MobaXterm, please select No when asked if you want to save your password.
> <img src="../fig/mobaxterm_3.png" alt="Password saving selection" style="height:350px">
{: .callout}

When logged in,
you are presented with a welcome message
and the following "prompt":

~~~
[username@login001 ~]$
~~~
{: .bash}


