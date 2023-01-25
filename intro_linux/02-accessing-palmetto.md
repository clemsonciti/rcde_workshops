# Accessing the Palmetto Cluster

## Remote login (SSH)

To be able to run commands on Palmetto from your own machine, you will first need to log in. We will login via **SSH** which will provide us a shell on one of Palmetto's login nodes.

For Mac OS X, you can open the Terminal Application (which is usually in Applications &rarr; Utilities folder) and run the following:

~~~
ssh <your Palmetto username>@login.palmetto.clemson.edu
~~~

For Windows, first you need to download and install
[MobaXterm Home Edition](https://mobaxterm.mobatek.net/download.html).

> It is important that you unzip the downloaded installer prior to installation.
> The zipped installer file contains an additional data file besides the installer
> executable. This data file is not accessible if the installer executable is
> called from insize the zipped file (something Windows allows you to do).


After MobaXterm starts, click the `Session` button.

![Main MobaXterm Windows](../fig/mobaxterm_0.png)

Select SSH session and use the following parameters (whichever required), then click `OK`:

* Remote host: `login.palmetto.clemson.edu`
* SSH-browser type: Enhanced SCP
* Port: 22

![MobaXterm SSH Session](../fig/mobaxterm_1.png)

At this stage, for both Mac and Windows, you will be asked to enter your username
and password, then DUO option.

![Login interface](../fig/mobaxterm_2.png)

> For MobaXterm, please select No when asked if you want to save your password.

![Password saving selection](../fig/mobaxterm_3.png)

When logged in, you are presented with a welcome message and the following "prompt":

~~~
[username@login001 ~]$
~~~

Let's enter our first command! 
Type the command `whoami`, then press the Enter key (sometimes marked Return) to send the command to the shell.
The command's output is the ID of the current user.

~~~
$ whoami
~~~